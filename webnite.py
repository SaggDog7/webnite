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
version = "0.0.1"
foundation_version = "5.5.2"

## Define the kit variable.
kit = ""

## Define the robots variable. 1 = allow, 0 = disallow
robots = 1

## Define the favicon variable. 1 = use favicon, 0 = don't use favicon
favicon = 1

## Define the command line argument parser.
clparse = argparse.ArgumentParser()

## Define the command line arguments themselves.
## A mutually exclusive group, kitarg, disallows the user to mix up frameworks.
clparse.add_argument("sitename", help="Define the name of the site to be created")
kitarg = clparse.add_mutually_exclusive_group(required = True)
kitarg.add_argument("-f", action="store_true",help="Create a new site using Foundation")
kitarg.add_argument("-b", action="store_true",help="Create a new site using Bootstrap")
clparse.add_argument("-dr", action="store_true",help="Disallow robots to crawl your site")
clparse.add_argument("-sf", action="store_true",help="Skip creating the default placeholder favicon")
clargs = clparse.parse_args()

## The function that checks if a site already exists and gives the option to overwrite if so.
def checkse(loc):
    if(os.path.isdir(loc) == True):
        output.outblank()
        output.out("sites/" + clargs.sitename + " already exists! Overwrite? (Y/N)")
        ovrc = input(" > ")

        ## Log user input into the logfile for possible future error checking purposes.
        output.logonly("User input: " + ovrc)

        ## Handle the input and either overwrite the existing site or exit webnite.
        if(ovrc == "y" or ovrc == "Y"):
            output.outblank()
            output.out("Overwriting...")
            shutil.rmtree(loc)

        else:
            output.outblank()
            output.out("Aborting...")
            output.outblank()
            sys.exit()


## If the disallow robots argument was passed through clparse.
if clargs.dr:
    robots = 0
else:
    robots = 1

## If the skip favicon argument was passed through clparse.
if clargs.sf:
    favicon = 0
else:
    favicon = 1

## If the foundation argument was passed through clparse.
if clargs.f:

    ## Call the function that checks if a site with the same name exists already.
    checkse("sites/" + clargs.sitename)

    ## Tell the user that we're starting up.
    output.outblank()
    output.out("Creating new site using Foundation " + foundation_version + ": " + clargs.sitename)
    output.out("Setting active kit to Foundation...")

    ## Set the kit to foundation.
    kit = "foundation"

    ## Start building foundation by passing the necessary arguments to bfoundation.
    build_foundation.bfoundation(clargs.sitename, kit, robots, favicon)
