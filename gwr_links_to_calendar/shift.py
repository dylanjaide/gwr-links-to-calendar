from dataclasses import dataclass
from datetime import date, time

@dataclass
class Shift:
    name: str
    start_date: date
    start_time: time
    end_date: date
    end_time: time

    def to_output_dict(self):
        return {
            "Subject": self.name,
            "Start Date": self.start_date.strftime("%d/%m/%Y"),
            "Start Time": self.start_time.strftime("%I:%M %p"),
            "End Date": self.end_date.strftime("%d/%m/%Y"),
            "End Time": self.end_time.strftime("%I:%M %p"),
        }
    
    def to_str(self):
        return " ".join([
            self.name,
            "-",
            self.start_time.strftime("%H:%M"),
            self.start_date.strftime("%d/%m/%Y"),
            "to",
            self.end_time.strftime("%H:%M"),
            self.end_date.strftime("%d/%m/%Y"),
        ])