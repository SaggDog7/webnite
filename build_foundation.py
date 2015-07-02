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
## Where siten is the name of the site passed from webnite.py
## Where kitn is the name of the kit (foundation) passed from webnite.py
## Where rob is if robots are allowed or disallowed
def bfoundation(siten, kitn, rob):

    ## Grab the kit archive.
    output.out("Grabbing kits/" + kitn + ".zip...")
    kitarchive = zipfile.ZipFile("kits/" + kitn + ".zip")

    ## Extract the kit to the site directory.
    output.out("Extracting " + kitn + ".zip to " "sites/" + siten + "...")
    kitarchive.extractall("sites/" + siten)

    ## Cleanup the default files. We do this because webnite uses its own.
    output.out("Removing default files...")
    if os.path.isfile("sites/" + siten + "/index.html"):
        os.remove("sites/" + siten + "/index.html")
        output.out("Deleted " + "sites/" + siten + "/index.html")
    if os.path.isfile("sites/" + siten + "/robots.txt"):
        os.remove("sites/" + siten + "/robots.txt")
        output.out("Deleted " + "sites/" + siten + "/robots.txt")
    if os.path.isfile("sites/" + siten + "/humans.txt"):
        os.remove("sites/" + siten + "/humans.txt")
        output.out("Deleted " + "sites/" + siten + "/humans.txt")

    ## See if robots are allowed and copy the corresponding robots.txt file.
    if rob == 1:
        output.out("Robots are allowed to crawl this site.")
        shutil.copyfile("pieces/allow_robots/robots.txt","sites/" + siten + "/robots.txt")
        output.out("Created " + "sites/" + siten + "/robots.txt")
    else:
        output.out("Robots are NOT allowed to crawl this site.")
        shutil.copyfile("pieces/disallow_robots/robots.txt","sites/" + siten + "/robots.txt")
        output.out("Created " + "sites/" + siten + "/robots.txt")

    ## Copy the humans.txt file.
    shutil.copyfile("pieces/foundation_humans/humans.txt","sites/" + siten + "/humans.txt")
    output.out("Created " + "sites/" + siten + "/humans.txt")

    ## Copy the favicon.ico file.
    shutil.copyfile("pieces/favicon/favicon.ico","sites/" + siten + "/favicon.ico")
    output.out("Created " + "sites/" + siten + "/favicon.ico")

    ## Copy the logo.png file.
    shutil.copyfile("logo.png","sites/" + siten + "/img/logo.png")
    output.out("Created " + "sites/" + siten + "/img/logo.png")

    ## Finally, copy the index.html file.
    shutil.copyfile("pieces/foundation_index/index.html","sites/" + siten + "/index.html")
    output.out("Created " + "sites/" + siten + "/index.html")

    ## All done!
    output.out("Done.")
    output.outblank()
