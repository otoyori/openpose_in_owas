#import pyopenpose as op
import sys
import cv2
from sys import platform
import argparse
import os
import pprint
class openpose:
	def __init__(self):
		self.Now_path = os.path.dirname(os.path.realpath(__file__))
		#self.dir_path = os.path.dirname("C://tools//openpose//examples//tutorial_api_python//openpose.py")
		self.dir_path = os.path.dirname("C:\tools\openpose\examples\tutorial_api_python\openpose.py")
		self.model_path = "C:/tools/openpose/models/"

		try:
			if platform =="win32":
				sys.path.append(self.dir_path + '/../../python/openpose/Release');
				
				os.environ['PATH']  = os.environ['PATH'] + ';' + self.dir_path + '/../../x64/Release;' +  self.dir_path + '/../../bin;'
				import pyopenpose as op
				
			else:
				sys.path.append('../../python');
				from openpose import pyopenpose as op
		except ImportError as e:
			print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
			raise e

		# Flags
		self.parser = argparse.ArgumentParser()
		#self.parser.add_argument("--image_path", default="../../../examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
		self.parser.add_argument("--image_path", default="C:\tools\openpose\examples\media\COCO_val2014_000000000564.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
		self.args = self.parser.parse_known_args()

		# Custom Params (refer to include/openpose/flags.hpp for more parameters)
		self.params = dict()
		self.params["model_folder"] = self.model_path
		
		# Add others in path?
		#for i in range(0, len(self.args[1])):
		#	curr_item = self.args[1][i]
		#	if i != len(self.args[1])-1: next_item = self.args[1][i+1]
		#	else: next_item = "1"
		#	if "--" in curr_item and "--" in next_item:
		#		key = curr_item.replace('-','')
		#		if key not in self.params:  self.params[key] = "1"
		#	elif "--" in curr_item and "--" not in next_item:
		#		key = curr_item.replace('-','')
		#		if key not in self.params: self.params[key] = next_item

		print(self.params)
		# Starting OpenPose
		#opWrapper = op.WrapperPython(3)
		#opWrapper.configure(self.params)
		#opWrapper.execute()
