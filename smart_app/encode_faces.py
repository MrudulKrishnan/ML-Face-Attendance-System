# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
# from imutils import paths
import face_recognition
# from django.db import connection
import argparse
import pickle
import cv2
import os
import pymysql


def enf(fn):
	imagePaths = [fn]
	knownEncodings = []
	knownNames = []
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
		print("imagepath-------",imagePath)
		name = "face"
		print("id=",name)
		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)

		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		print("++++++++++++++++++++++++++++++++",image)
		# detect the (x, y)-coordnates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb, model='hog')

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			knownEncodings.append(encoding)
			knownNames.append(name)

	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f = open('faces.pickles', "wb")
	f.write(pickle.dumps(data))
	f.close()
	con = pymysql.connect(host='localhost', port=3306, user='root', password='123456789', db='smart_attendance')
	cmd = con.cursor()
	# cursor = connection.cursor()
	cmd.execute("SELECT * FROM smart_app_student")
	s=cmd.fetchall()
	for r in s:
		data = pickle.loads(open('faces.pickles', "rb").read())
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		# load the input image and convert it from BGR to RGB
		image = cv2.imread(r"E:\WORK\PROGRAM FILES\PROJECTS\Smart_Attendance\Smart_Attendance\media//"+r[11])
		print(r[11])
		print(image)
		h, w, ch = image.shape
		print(ch)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes corresponding
		# to each face in the input image, then compute the facial embeddings
		# for each face
		print("[INFO] recognizing faces...")
		boxes = face_recognition.face_locations(rgb, model='hog')
		encodings = face_recognition.face_encodings(rgb, boxes)

		# initialize the list of names for each face detected
		names = []
		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"], encoding,tolerance=0.4)
			# check to see if we have found a match
			if True in matches:
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}
				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1
				cmd.execute("SELECT * FROM `smart_app_attendance` WHERE `Date`=CURDATE() AND `STUDENT_ID_id`="+str(r[0]))
				s=cmd.fetchone()
				if s is  None:
					cmd.execute("insert into smart_app_attendance values(null,curdate(),1,'"+str(r[0])+"')")
					con.commit()
			else:
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}
				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1
				cmd.execute(
					"SELECT * FROM `smart_app_attendance` WHERE `Date`=CURDATE() AND `STUDENT_ID_id`=" + str(r[0]))
				s = cmd.fetchone()
				if s is None:
					cmd.execute("insert into smart_app_attendance values(null,curdate(),0,'" + str(r[0]) + "')")
					con.commit()
	return "na"

