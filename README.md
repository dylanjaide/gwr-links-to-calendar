# GWR Links to Calendar

Converts a GWR links document from PDF into a CSV list of events for importing into your calendar (eg. Google Calendar)


## Disclaimer

I don't work for GWR. This repository contains only my own intellectual property, or more specifically, it contains no GWR materials whatsoever.

Please note that this is not a perfect system. Reading from the PDF file is messy and complicated, and there are a whole host of things that could go wrong. This means that there could be mistakes in the calendar events produced by this code. The purpose of this project is to save people time, not to create a 100% accurate calendar.

It is critical that you thoroughly check the results created by this code for yourself before acting on them. I take no responsibility whatsoever for any inaccurate information produced by this code, and by using this code you agree that you take full responsibility for anything produced by it. In other words, if you don't show up for work at the right time, it's your fault, not mine. ♥


## Setup

These are the steps you should only need to perform the first time you use this tool.

First, [install python 3](https://www.python.org/downloads/) if you haven't already.

Next, download the files from this repository. Make sure to extract this .zip file.

Finally, install the dependencies by running `python3 -m pip install -r requirements.txt` on Unix/macOS, or `py -m pip install -r requirements.txt` on Windows.


## How to use

These are the steps you will need to follow each time you use this tool. If you haven't already completed the [setup steps](#setup), do that first.

You will need a links document/timetable, provided by GWR as a PDF file. You'll need to get this yourself, and place it in the same folder that you downloaded the files from this repository to (i.e. inside the folder you extracted the .zip to).

Open a terminal, and navigate to the folder you downloaded the files from this repository to. You will need to change directory (`cd`) from your home directory to this folder. Depending on where you saved these files, this might look something like `cd Downloads/gwr-links-to-calendar/`; or, `cd Downloads` followed by `cd gwr-links-to-calendar`. You can always run `ls` to see what files and folders are inside the current directory, or `pwd` to view the current directory. You can look up a "shell navigation" tutorial if you're having trouble with this.

If you run `ls` in your terminal and it lists the files from this repository and the links PDF, then you're ready!

### Simple

Default usage requires only two parameters:

```python3 main.py -i <PATH_TO_LINKS_PDF> -n "<NAME_AS_INITIAL_SURNAME>"```

* `-i` (`--input`): Path to input file
* `-n` (`--name`): Name of the staff member. This should be given in the same format as found in the PDF: first initial followed by surname, in all capital letters

For example, running

```python3 main.py -i links.pdf -n "J SMITH"```

will create a file `shifts.csv` which can be imported into your calendar. This will contain events for as many weeks as there are people in the given person's table.

### Advanced

You can optionally specify additional parameters:

```python3 main.py -i <PATH_TO_LINKS_PDF> -n "<NAME_AS_INITIAL_SURNAME>" -w <NUMBER_OF_WEEKS> -o <PATH_TO_OUTPUT_CSV>```

* `-w` (`--num-weeks`): Number of weeks of events to be created. If this exceeds the number of people in the table, it will continue to loop through the table in sequence
* `-o` (`--output`): Path to output file

For example, running

```python3 main.py -i links.pdf -n "J SMITH" -w 52 -o for_my_calendar.csv```

will create events covering the next year (52 weeks) in a file called `for_my_calendar.csv`.
