from datetime import date, time, timedelta
import re

from gwr_links_to_calendar.shift import Shift
from gwr_links_to_calendar.utils import TIME_REGEX, DURATION_REGEX, DATE_REGEX, NAME_REGEX, ROW_NUMBER_REGEX, WEEKLY_HOURS_REGEX, SHIFT_DETAILS_REGEXES

def filter_page(page):
    rows = []
    for line in page.split("\n"):
        if "hrs" in line and "mins" in line:
            rows.append(line)
    return rows


def offset_start_row_from_name(rows: list, name: str):
    for i in range(len(rows)):
        if rows[i][0] == name:
            return rows[i:]+rows[:i]


def parse_commencing_date(page):
    start_date_line_match = re.search("Commencing " + DATE_REGEX, page)
    start_date_str = re.search(DATE_REGEX, start_date_line_match.group()).group()
    date_elements = start_date_str.split("/") # d,m,y
    date_elements.reverse() # y,m,d
    date_elements[0] = "20" + date_elements[0]
    start_date = date(*[int(x) for x in date_elements])
    return start_date


# Split a line up into key segments
# Each line gets 10 entries:
# 0: name (first initial + surname)
# 1: row number
# 2: weekly hours
# 3-9: details of day's shift (sun-sat)
def parse_table_row(line):

    result = [""]*10

    row_prefix_regex = "^" + " ".join([NAME_REGEX, ROW_NUMBER_REGEX, WEEKLY_HOURS_REGEX])
    row_prefix_match = re.search(row_prefix_regex, line)
    
    result[0] = re.search("^" + NAME_REGEX, row_prefix_match.group()).group()
    result[1] = re.search(ROW_NUMBER_REGEX, row_prefix_match.group()).group()
    result[2] = re.search(WEEKLY_HOURS_REGEX, row_prefix_match.group()).group()

    shifts = line[row_prefix_match.span()[1]+1:]
    shift_matches = re.findall("(" + "|".join(list(SHIFT_DETAILS_REGEXES.values())) + ")", shifts)
    assert 6 <= len(shift_matches) <= 7, f"Wrong number of shift matches (should be 6 or 7, got {len(shift_matches)})"

    # This is really messy... but making do with what I've got in this PDF
    # Any day where there is nothing in the "Turn" column messes things up
    # As far as I can tell, this only happens on Sundays (start of row)
    # So, this writes into the array backwards starting from Saturday (index 9)
    for i in range(min(len(shift_matches), 7)):
        result[9-i] = shift_matches[len(shift_matches)-1-i][0]

    return result


def create_schedule(table_rows: list, start_date: date, n_weeks: int = None):
        
        if n_weeks is None:
            n_weeks = len(table_rows)

        schedule_raw = []
        for i in range(n_weeks):
            for j in range(3,10):
                schedule_raw.append(table_rows[i % len(table_rows)][j])
        
        shifts = []
        for i in range(len(schedule_raw)):
            if re.match("^" + SHIFT_DETAILS_REGEXES["SHIFT"] + "$", schedule_raw[i]):
                vals = schedule_raw[i].split(" ")
                st = time(*[int(x) for x in vals[0].split(":")])
                et = time(*[int(x) for x in vals[1].split(":")])
                sd = start_date + timedelta(days=i)
                ed = sd + timedelta(days=int(et < st))

                shifts.append(Shift(
                    name=vals[2],
                    start_date=sd,
                    start_time=st,
                    end_date=ed,
                    end_time=et,
                ))
        
        return shifts