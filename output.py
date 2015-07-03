## webnite - Easy website foundations from popular frameworks using Python
## -----------------------------------------------------------------------
## Authored by Avery Ross (averyre) © 2015
## Released under the GNU General Public License v2.0
## -----------------------------------------------------------------------

## Module for creating and appending to a logFile.
import logging
## Module for accessing system date and time.
import datetime

## Get the current datetime.
dateTime = datetime.datetime.now()

## Generate a timestamp to be used in the next functions.
timeStamp = "[" + str(dateTime.month) + "/" + str(dateTime.day) + "/" + str(dateTime.year) + " " + str(dateTime.hour) + ":" + str(dateTime.minute) + ":" + str(dateTime.second) + "] "

## Define the logFile to append to.
logFile = "WEBNITE_LOG.txt"
logging.basicConfig(filename=logFile,level=logging.DEBUG)

## This function will output to the terminal and append to the logFile.
def out(inputItems):
    print("WEBNITE: " + inputItems)
    logging.debug("WEBNITE: " + timeStamp + inputItems)

## This function will append to the logFile only.
def logonly(inputItems):
    logging.debug("WEBNITE:SYSTEM: " + timeStamp + inputItems)

## This function simply prints an empty line. Somewhat useful?
def outblank():
    print("")
