## webnite - Easy website foundations from popular frameworks using Python
## -----------------------------------------------------------------------
## Authored by Avery Ross (averyre) © 2015
## Released under the GNU General Public License v2.0
## -----------------------------------------------------------------------

## Modules for system operations like moving and deleting files.
import os
import shutil
## Module required for dealing with compressed archives.
import zipfile
## Module that displays and logs output.
import output

## This function creates structured sites from the foundation framework.
## Where siteName is the name of the site passed from webnite.py
## Where kitName is the name of the kit (foundation) passed from webnite.py
## Where disallowRobots is if robots are allowed or disallowed
## Where skipFavicon is if the default placeholder favicon is to be skipped or not
def buildFoundation(siteName, kitName, disallowRobots, skipFavicon):

    ## Grab the kit archive.
    output.out("Grabbing kits/" + kitName + ".zip...")
    kitarchive = zipfile.ZipFile("kits/" + kitName + ".zip")

    ## Extract the kit to the site directory.
    output.out("Extracting " + kitName + ".zip to " "sites/" + siteName + "...")
    kitarchive.extractall("sites/" + siteName)

    ## Cleanup the default files. We do this because webnite uses its own.
    output.out("Removing default files...")
    if os.path.isfile("sites/" + siteName + "/index.html"):
        os.remove("sites/" + siteName + "/index.html")
        output.out("Deleted " + "sites/" + siteName + "/index.html")
    if os.path.isfile("sites/" + siteName + "/robots.txt"):
        os.remove("sites/" + siteName + "/robots.txt")
        output.out("Deleted " + "sites/" + siteName + "/robots.txt")
    if os.path.isfile("sites/" + siteName + "/humans.txt"):
        os.remove("sites/" + siteName + "/humans.txt")
        output.out("Deleted " + "sites/" + siteName + "/humans.txt")

    ## See if robots are allowed and copy the corresponding robots.txt file.
    if disallowRobots == 1:
        shutil.copyfile("pieces/allow_robots/robots.txt","sites/" + siteName + "/robots.txt")
        output.out("Created " + "sites/" + siteName + "/robots.txt")
    else:
        output.out("Robots are NOT allowed to crawl this site.")
        shutil.copyfile("pieces/disallow_robots/robots.txt","sites/" + siteName + "/robots.txt")
        output.out("Created " + "sites/" + siteName + "/robots.txt")

    ## Copy the humans.txt file.
    shutil.copyfile("pieces/foundation_humans/humans.txt","sites/" + siteName + "/humans.txt")
    output.out("Created " + "sites/" + siteName + "/humans.txt")

    ## If -sf was argued we skip adding the default placeholder favicon.
    if skipFavicon ==1:
        shutil.copyfile("pieces/favicon/favicon.ico","sites/" + siteName + "/favicon.ico")
        output.out("Created " + "sites/" + siteName + "/favicon.ico")
    else:
        output.out("Skipping creating the default placeholder favicon...")

    ## Copy the logo.png file.
    shutil.copyfile("logo.png","sites/" + siteName + "/img/logo.png")
    output.out("Created " + "sites/" + siteName + "/img/logo.png")

    ## Finally, copy the index.html file.
    shutil.copyfile("pieces/foundation_index/index.html","sites/" + siteName + "/index.html")
    output.out("Created " + "sites/" + siteName + "/index.html")

    ## All done!
    output.out("Done.")

    ## Display the final message detailing successfully completion.
    output.outblank()
    output.out("Your new Foundation website has been successfully created in sites/" + siteName)
    output.outblank()
