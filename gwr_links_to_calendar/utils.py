TIME_REGEX = r"\d{1,2}:\d{2}"
DURATION_REGEX = r"\d{1,2}.\d{2}"
DATE_REGEX = r"\d*/\d*/\d*"

NAME_REGEX = r"[A-Z] [A-Z]+"
ROW_NUMBER_REGEX = r"[1-9]\d*"
WEEKLY_HOURS_REGEX = r"\d* hrs \d* mins"
SHIFT_DETAILS_REGEXES = {
    #"ZS": r"ZS",
    "RDNA": r"RDNA",
    "RD": r"RD",
    "SHIFT": " ".join([TIME_REGEX, TIME_REGEX, r"(\d+|A/R)", DURATION_REGEX]),
}