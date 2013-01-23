## Overview
NIRail Reader tool that scrapes train timetable data from the timetables provided on the translink website (http://www.translink.co.uk/).

Currently this data is output into a single xml document, further development may include a JSON output.

This project is a work-in-progress, and probably contains many bugs.  Any and all feedback is welcome!

##Using NIRail Reader
NIRail Reader is a python script, so just run ```python TrainScrape.py``` from the correct dir.  Data output will also be to this location.

Timetable names and web addresses are stored in an external text file ```TimetableURLs.txt```.  This can be updated as and when url's change or new timetables are introduced.

It should also be noted that I am using the Beautiful Soup library to simplify some of the parsing, you may need to install it (http://pypi.python.org/pypi/BeautifulSoup).

##Legal
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.