import base64
import json
import sys
import os


def image_to_base64(image_path):
	if not os.path.isfile(image_path):
		return None
	
	with open(image_path, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
	return f"data:image/png;base64,{encoded_string}"


def change_field_credentials(playlist, image, name):
	with open(playlist, 'r') as json_change_infile:
		data = json.load(json_change_infile)
	
	data['image'] = image
	data['playlistTitle'] = name

	with open(playlist, 'w') as json_change_outfile:
		json.dump(data, json_change_outfile, indent=4)


def check_inputs():
	try:
		while True:
			playlist = str(input("Playlist: "))
			if not os.path.isfile(playlist):
				print("Playlist doesn't exist. Check the name and check if you put .json on the end")
			else:
				break
		playlist_name = str(input("Playlist name: "))
		while True:
			image_path = str(input("Image (only PNGs): "))
			if not os.path.isfile(image_path):
				print("Image doesnt exist. Check the name and check if you put .png on the end")
			else:
				break
		return playlist, playlist_name, image_path
	except KeyboardInterrupt:
		sys.exit(0)


plist, plist_name, img_path = check_inputs()
if plist and plist_name and img_path:
	base64_image = image_to_base64(img_path)
	if not base64_image:
		print("Image does not exist")
	playlist_exist = change_field_credentials(plist, base64_image, plist_name)