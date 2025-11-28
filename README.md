# GWR Links to Calendar

Converts a GWR links document from PDF into a CSV list of events for importing into your calendar (eg. Google Calendar)


## Disclaimer

I don't work for GWR. This repository contains only my own intellectual property, or more specifically, it contains no GWR materials whatsoever.

Please note that this is not a perfect system. Reading from the PDF file is messy and complicated, and there are a whole host of things that could go wrong. This means that there could be mistakes in the calendar events produced by this code. The purpose of this project is to save people time, not to create a 100% accurate calendar.

It is critical that you thoroughly check the results created by this code for yourself before acting on them. I take no responsibility whatsoever for any inaccurate information produced by this code, and by using this code you agree that you take full responsibility for anything produced by it. In other words, if you don't show up for work at the right time, it's your fault, not mine. ♥


## Setup

First, [install python 3](https://packaging.python.org/en/latest/tutorials/installing-packages/) if you haven't already.

Next, download the files from this repository, and from a terminal navigate to that folder.

Finally, install the dependencies by running `python3 -m pip install -r requirements.txt` on Unix/macOS, or `py -m pip install -r requirements.txt` on Windows.


## How to use

You will need a links document/timetable, provided by GWR as a PDF file. You'll need to get this yourself, and place it in the same folder where you downloaded the files from this repository.

### Simple

Default usage requires only two parameters:

```python main.py -i <PATH_TO_LINKS_PDF> -n "<NAME_AS_INITIAL_SURNAME>"```

* `-i` (`--input`): Path to input file
* `-n` (`--name`): Name of the staff member. This should be given in the same format as found in the PDF: first initial followed by surname, in all capital letters

For example, running

```python main.py -i links.pdf -n "J SMITH"```

will create a file `shifts.csv` which can be imported into your calendar. This will contain events for as many weeks as there are people in the given person's table.

### Advanced

You can optionally specify additional parameters:

```python main.py -i <PATH_TO_LINKS_PDF> -n "<NAME_AS_INITIAL_SURNAME> -w <NUMBER_OF_WEEKS> -o <PATH_TO_OUTPUT_CSV>"```

* `-w` (`--num-weeks`): Number of weeks of events to be created. If this exceeds the number of people in the table, it will continue to loop through the table in sequence
* `-o` (`--output`): Path to output file

For example, running

```python main.py -i links.pdf -n "J SMITH" -w 52 -o for_my_calendar.csv```

will create events covering the next year (52 weeks) in a file called `for_my_calendar.csv`.