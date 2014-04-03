"""Script to rename a tv episode file based on information from theTVDB.org"""
import os, sys, shutil
from pymediainfo import MediaInfo
from pprint import pprint

def main():
	"""Main entry point for the script."""
	file = sys.argv[1]
	file_path = sys.argv[2]
	out_path = sys.argv[3]

	title = get_show_title(file)
	print "Title: " + title
	
	season_num = get_season_number(file)
	print "Season: " + str(season_num)
	
	episode_num = get_episode_number(file)
	print "Episode: " + str(episode_num)

	name = build_file_name(title, season_num, episode_num)
	print "Renaming to: " + name

	path, ext = os.path.splitext(file_path)
	new_path = os.path.join(out_path, name + ext)

	print "Moving file[" + file_path + "] to: " + new_path
	shutil.move(file_path, new_path)


def get_show_title(file):
	"""Return the show name from the file metadata"""
	media_info = MediaInfo.parse(file)
	for track in media_info.tracks:
		if track.track_type == 'General':
			return track.title

def get_season_number(file):
	"""Get the season number from the SYNOPSIS field in the file metadata"""
	media_info = MediaInfo.parse(file)
	for track in media_info.tracks:
		if track.track_type == 'General':
			synopsis = track.synopsis

			"""We assume that there won't be more than 99 episodes 
			in a season here, so just trim the last two characters
			and what remains must be our season number.  There has
			to be a smarter way."""
			season_num = synopsis[:-2]
			return int(season_num)

def get_episode_number(file):
	"""Return the episode number from the SYNOPSIS field in the file metadata"""
	media_info = MediaInfo.parse(file)
	for track in media_info.tracks:
		if track.track_type == 'General':
			synopsis = track.synopsis

			"""We assume that there won't be more than 99 episodes 
			in a season here, so just trim the last two characters
			and what remains must be our season number.  There has
			to be a smarter way."""
			episode_num = synopsis[-2:]
			return int(episode_num)

def build_file_name(title, season_num, episode_num):
	"""Constructs a file name based on the provided information, excluding extension"""
	return title + "-S" + str('%02d' % season_num) + "E" + str('%02d' % episode_num)


if __name__ == '__main__':
	sys.exit(main())