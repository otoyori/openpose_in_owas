import My_OpenPose
import pyopenpose as op
import sys
import cv2
import os
from sys import platform
import argparse
import time
import pprint
class main(My_OpenPose.openpose):
	
	def add_path(self):
		for i in range(0, len(self.args[1])):
			curr_item = self.args[1][i]
			if i != len(self.args[1])-1: next_item = self.args[1][i+1]
			else: next_item = "1"
			if "--" in curr_item and "--" in next_item:
				key = curr_item.replace('-','')
				if key not in self.params:  self.params[key] = "1"
			elif "--" in curr_item and "--" not in next_item:
				key = curr_item.replace('-','')
				if key not in self.params: self.params[key] = next_item

	def start(self):
		self.params["face"] = True
		self.params["hand"] = True
		self.add_path()

		pprint.pprint(self.params)
		opWrapper = op.WrapperPython(3)
		opWrapper.configure(self.params)
		opWrapper.execute()
		
	def key_start(self):
		self.params["face"] = True
		self.params["hand"] = True
		self.add_path()

		pprint.pprint(self.params)

		posture = [0]*4
		print(posture)
		try:
			opWrapper = op.WrapperPython()
			opWrapper.configure(self.params)
			opWrapper.start()
			print("AAAAAA  1")
			# Process Image
			datum = op.Datum()
			print("AAAAAA  2")
			print(self.args[0].image_path)
			imageToProcess = cv2.imread("D.jpg")
			print("AAAAAA  3")
			datum.cvInputData = imageToProcess
			print("AAAAAA  4")
			opWrapper.emplaceAndPop([datum])
			
			# Display Image
			print("Body keypoints: \n" + str(datum.poseKeypoints[0][1]))
			print("Body keypoints: \n" + str(datum.poseKeypoints[0][8]))
			#print("Face keypoints: \n" + str(datum.faceKeypoints))
			#print("Left hand keypoints: \n" + str(datum.handKeypoints[0]))
			#print("Right hand keypoints: \n" + str(datum.handKeypoints[1]))


			#print( abs(datum.poseKeypoints[0][1][0] - datum.poseKeypoints[0][8][0]))
			#print( datum.poseKeypoints[0][8][0] - datum.poseKeypoints[0][1][0])
			#背部の判定
			if abs(datum.poseKeypoints[0][1][0] - datum.poseKeypoints[0][8][0]) <= 10:
				posture[0] = 1
			else:
				posture[0] = 2

			#print(datum.poseKeypoints[0][2])
			#print(datum.poseKeypoints[0][3])
			#print("-----------------------")
			#print(datum.poseKeypoints[0][5])
			#print(datum.poseKeypoints[0][6])

			#上肢の判定
			if (datum.poseKeypoints[0][2][1] < datum.poseKeypoints[0][3][1]) and (datum.poseKeypoints[0][5][1] < datum.poseKeypoints[0][6][1]):
				posture[1] = 1
			elif(datum.poseKeypoints[0][2][1] < datum.poseKeypoints[0][3][1]) or (datum.poseKeypoints[0][5][1] < datum.poseKeypoints[0][6][1]):
				posture[1] = 2
			elif(datum.poseKeypoints[0][2][1] > datum.poseKeypoints[0][3][1]) and (datum.poseKeypoints[0][5][1] > datum.poseKeypoints[0][6][1]):
				posture[1] = 3


			#下肢の判定
			print(datum.poseKeypoints[0][9][0])
			print(datum.poseKeypoints[0][10][0])
			print(datum.poseKeypoints[0][11][0])


			print(max(datum.poseKeypoints[0][10][0],datum.poseKeypoints[0][9][0],datum.poseKeypoints[0][11][0]))
			if abs(datum.poseKeypoints[0][9][0]-datum.poseKeypoints[0][10][0]) > abs(datum.poseKeypoints[0][9][1]-datum.poseKeypoints[0][10][1]) and abs(datum.poseKeypoints[0][12][0]-datum.poseKeypoints[0][13][0]) > abs(datum.poseKeypoints[0][12][1]-datum.poseKeypoints[0][13][1]) :
				posture[2] = 1
			elif abs(datum.poseKeypoints[0][9][0]-datum.poseKeypoints[0][10][0]) < abs(datum.poseKeypoints[0][9][1]-datum.poseKeypoints[0][10][1]) and abs(datum.poseKeypoints[0][12][0]-datum.poseKeypoints[0][13][0]) < abs(datum.poseKeypoints[0][12][1]-datum.poseKeypoints[0][13][1]) :
				posture[2] = 2
			elif max(datum.poseKeypoints[0][9][0],datum.poseKeypoints[0][10][0],datum.poseKeypoints[0][11][0]) == datum.poseKeypoints[0][10][0] and max(datum.poseKeypoints[0][12][0],datum.poseKeypoints[0][13][0],datum.poseKeypoints[0][14][0]) == datum.poseKeypoints[0][13][0]:
				posture[2] = 4
			elif (datum.poseKeypoints[0][10][1] > datum.poseKeypoints[0][24][1]) or (datum.poseKeypoints[0][13][1] > datum.poseKeypoints[0][21][1] ):
				posture[2] = 6
			print(posture)
			cv2.imshow("OpenPose 1.5.0 - Tutorial Python API", datum.cvOutputData)
			cv2.waitKey(0)
		except Exception as e:
			print(e)
			sys.exit(-1)
		
print("Main_program")
main().key_start()
