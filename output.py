## webnite - Easy website foundations from popular frameworks using Python
## -----------------------------------------------------------------------
## Authored by Avery Ross (averyre) © 2015
## Released under the GNU General Public License v2.0
## -----------------------------------------------------------------------

## Module for creating and appending to a logfile.
import logging
## Module for accessing system date and time.
import datetime

## Get the current datetime.
dt = datetime.datetime.now()

## Generate a timestamp to be used in the next functions.
ts = "[" + str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year) + " " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second) + "] "

## Define the logfile to append to.
logfile = "WEBNITE_LOG.txt"
logging.basicConfig(filename=logfile,level=logging.DEBUG)

## This function will output to the terminal and append to the logfile.
def out(inp):
    print("WEBNITE: " + inp)
    logging.debug("WEBNITE: " + ts + inp)

## This function will append to the logfile only.
def logonly(inp):
    logging.debug("WEBNITE:SYSTEM: " + ts + inp)

## This function simply prints an empty line. Somewhat useful?
def outblank():
    print("")
