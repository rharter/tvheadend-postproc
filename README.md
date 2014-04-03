# Postproc

TV Show post processing script for TVHeadend.  The rename.py script uses the video metadata to rename the file with season and episode data so processors like Plex Media Server and XBMC can properly identify the files.

## TODO

I'd like to add commercial detection and removal to the script
Better handle errors or missing meta data

## Usage

This script should be installed somewhere on your system.  Once I learn a bit more about packaging python apps, this part should get much easier.

The script depends on the pymediainfo package, which you can install with:

	sudo pip install pymediainfo

Then just set this script as your Post-processor command in TVHeadend like so:

	python /usr/local/bin/rename.py %f /opt/recordings/

Where `/usr/local/bin/rename.py` is the path to the rename script, and `/opt/recordings` is the output directory where you'd like your renamed videos written to.