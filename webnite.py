## webnite - Easy website foundations from popular frameworks using Python
## -----------------------------------------------------------------------
## Authored by Avery Ross (averyre) © 2015
## Released under the GNU General Public License v2.0
## -----------------------------------------------------------------------

## Modules for system operations like moving and deleting files.
import os
import shutil
import sys
## Module required for dealing with command line arguments.
import argparse
## Module required for dealing with compressed archives.
import zipfile
## Module that displays and logs output.
import output
## "Builder" modules that create structured sites from each supported framework.
import build_foundation

## Define the version of webnite and kits.
webniteVersion = "0.0.1"
foundationVersion = "5.5.2"

## Define the activeKit variable.
activeKit = ""

## Define the command line argument parser.
commandlineParse = argparse.ArgumentParser()

## Define the command line arguments themselves.
## A mutually exclusive group, kitArgument, disallows the user to mix up frameworks.
commandlineParse.add_argument("projectname", help="Define the name of the site to be created")
kitArgument = commandlineParse.add_mutually_exclusive_group(required = True)
kitArgument.add_argument("-f", action="store_true",help="Create a new site using Foundation")
kitArgument.add_argument("-b", action="store_true",help="Create a new site using Bootstrap")
commandlineParse.add_argument("-dr", action="store_true",help="Disallow robots to crawl your site")
commandlineParse.add_argument("-sf", action="store_true",help="Skip creating the default placeholder favicon")
commandlineArguments = commandlineParse.parse_args()

## The function that checks if a site already exists and gives the option to overwrite if so.
def checkSiteExists(siteLocation):
    if(os.path.isdir(siteLocation) == True):
        output.outBlank()
        output.out("sites/" + commandlineArguments.projectname + " already exists! Overwrite? (Y/N)")
        overwriteInput = input(" > ")

        ## Log user input into the logFile for possible future error checking purposes.
        output.logOnly("User input: " + overwriteInput)

        ## Handle the input and either overwrite the existing site or exit webnite.
        if(overwriteInput == "y" or overwriteInput == "Y"):
            output.outBlank()
            output.out("Overwriting...")
            shutil.rmtree(siteLocation)

        else:
            output.outBlank()
            output.out("Aborting...")
            output.outBlank()
            sys.exit()

## If the foundation argument was passed through commandlineParse.
if commandlineArguments.f:

    ## Call the function that checks if a site with the same name exists already.
    checkSiteExists("sites/" + commandlineArguments.projectname)

    ## Tell the user that we're starting up.
    output.outBlank()
    output.out("Creating new site using Foundation " + foundationVersion + ": " + commandlineArguments.projectname)
    output.out("Setting the active kit to Foundation...")

    ## Set the activeKit to foundation.
    activeKit = "foundation"

    ## Start building foundation by passing the necessary arguments to buildFoundation.
    build_foundation.buildFoundation(commandlineArguments.projectname, activeKit, commandlineArguments.dr, commandlineArguments.sf)
