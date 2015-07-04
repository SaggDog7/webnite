## webnite - Easy website foundations from popular frameworks using Python
## -----------------------------------------------------------------------
## Originally authored by Avery Ross (averyre) © 2015
## Modified by Cory Andrews (SaggDog7)
## Released under the GNU General Public License v2.0
## -----------------------------------------------------------------------

## Modules for system operations like moving and deleting files.
import os
import shutil
import sys
import traceback
## Module required for dealing with command line arguments.
import argparse
## Module required for dealing with compressed archives.
import zipfile
## Module that displays and logs output.
import output
## "Builder" modules that create structured sites from each supported framework.
import build_foundation

## The function that checks if a site already exists and gives the option to overwrite if so.
def checkSiteExist(sitePath):
    if(os.path.isdir(sitePath)):
        output.outBlank()
        output.out(sitePath + " already exists! Overwrite? (Y/N)")
        overwriteInput = input(" > ")

        ## Log user input into the logFile for possible future error checking purposes.
        output.logOnly("User input: " + overwriteInput)

        ## Handle the input and either overwrite the existing site or exit webnite.
        if(overwriteInput == "y" or overwriteInput == "Y"):
            output.outBlank()
            output.out("Overwriting...")
            shutil.rmtree(sitePath, onerror=lambda func, path, exc_info: \
                output.logOnly("".join(traceback.format_exception(exc_info[0], exc_info[1], exc_info[2]))))
        else:
            output.outBlank()
            output.out("Aborting...")
            output.outBlank()
            sys.exit()

def initArgs():
    ## Define the command line argument parser.
    cmdLineParse = argparse.ArgumentParser()

    ## Define the command line arguments themselves.
    ## A mutually exclusive group, kitArg, disallows the user to mix up frameworks.
    cmdLineParse.add_argument("projectName", help="Define the name of the site to be created")
    kitArg = cmdLineParse.add_mutually_exclusive_group(required = True)
    kitArg.add_argument("-f", action="store_true",help="Create a new site using Foundation")
    kitArg.add_argument("-b", action="store_true",help="Create a new site using Bootstrap")
    cmdLineParse.add_argument("-dr", action="store_true",help="Disallow robots to crawl your site")
    cmdLineParse.add_argument("-sf", action="store_true",help="Skip creating the default placeholder favicon")

    return cmdLineParse.parse_args()

if __name__ == '__main__':
    ## Define the version of webnite and kits.
    webniteVersion = "0.0.1"
    foundationVersion = "5.5.2"
    activeKit = "None"

    ## Initialize and parse command line arguments
    cmdLineArgs = initArgs()

    ## If the foundation argument was passed through cmdLineParse.
    if cmdLineArgs.f:
        ## Call the function that checks if a site with the same name exists already.
        checkSiteExist("sites/" + cmdLineArgs.projectName)

        ## Tell the user that we're starting up.
        output.outBlank()
        output.out("Creating new site using Foundation " + foundationVersion + ": " + cmdLineArgs.projectName)
        output.out("Setting active kit to Foundation...")

        ## Set the kit to foundation.
        activeKit = "foundation"

        ## Start building foundation by passing the necessary arguments to buildFoundation.
        build_foundation.buildFoundation(cmdLineArgs.projectName, activeKit, cmdLineArgs.dr, cmdLineArgs.sf)
