# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:04:38 2020

@author: RuiRui
"""

import numpy as np
import cv2

def create_base (img,color,pixel_line):
	cv2.line(img,(131,382),(131,305),color,pixel_line)
	cv2.line(img,(131,305),(139,305),color,pixel_line)
	cv2.line(img,(139,305),(139,302),color,pixel_line)
	cv2.line(img,(139,302),(197,302),color,pixel_line)
	cv2.line(img,(197,302),(203,306),color,pixel_line)
	cv2.line(img,(203,306),(203,368),color,pixel_line)
	cv2.line(img,(203,368),(207,383),color,pixel_line)
	cv2.line(img,(207,383),(202,386),color,pixel_line)
	cv2.line(img,(202,386),(188,388),color,pixel_line)
	cv2.line(img,(188,388),(143,388),color,pixel_line)
	cv2.line(img,(143,388),(134,386),color,pixel_line)
	cv2.line(img,(134,386),(131,382),color,pixel_line)

def create_stick (img,color,pixel_line):	
	cv2.line(img,(203,306),(448,306),color,pixel_line)
	cv2.line(img,(448,306),(448,380),color,pixel_line)
	cv2.line(img,(448,380),(206,380),color,pixel_line)

def create_base_scope (img,color,pixel_line):
	cv2.line(img,(235,306),(247,293),color,pixel_line)
	cv2.line(img,(247,293),(327,293),color,pixel_line)
	cv2.line(img,(327,293),(357,306),color,pixel_line)

def create_scope (img,color,pixel_line):
	cv2.line(img,(266,293),(266,289),color,pixel_line)
	cv2.line(img,(266,289),(270,283),color,pixel_line)	
	cv2.line(img,(270,283),(296,283),color,pixel_line)
	cv2.line(img,(296,283),(309,293),color,pixel_line)	

def create_support (img,color,pixel_line):
	cv2.line(img,(448,395),(448,300),color,pixel_line)
	cv2.line(img,(448,300),(450,296),color,pixel_line)
	cv2.line(img,(450,296),(457,296),color,pixel_line)
	cv2.line(img,(457,296),(459,294),color,pixel_line)
	cv2.line(img,(459,294),(482,294),color,pixel_line)
	cv2.line(img,(482,294),(482,395),color,pixel_line)
	cv2.line(img,(482,395),(448,395),color,pixel_line)

def create_envolve (img,color,pixel_line):
	cv2.line(img,(482,294),(501,286),color,pixel_line)
	cv2.line(img,(501,286),(523,269),color,pixel_line)
	cv2.line(img,(523,269),(547,269),color,pixel_line)
	cv2.line(img,(547,269),(554,367),color,pixel_line)
	cv2.line(img,(554,367),(554,407),color,pixel_line)
	cv2.line(img,(554,407),(553,427),color,pixel_line)
	cv2.line(img,(553,427),(526,425),color,pixel_line)
	cv2.line(img,(526,425),(501,409),color,pixel_line)
	cv2.line(img,(501,409),(482,395),color,pixel_line)

def create_protection (img,color,pixel_line):
	cv2.line(img,(548,272),(579,272),color,pixel_line)
	cv2.line(img,(579,272),(579,277),color,pixel_line)
	cv2.line(img,(579,277),(574,284),color,pixel_line)
	cv2.line(img,(574,284),(573,293),color,pixel_line)
	cv2.line(img,(573,293),(572,315),color,pixel_line)
	cv2.line(img,(572,315),(573,363),color,pixel_line)
	cv2.line(img,(573,363),(575,392),color,pixel_line)
	cv2.line(img,(575,392),(581,424),color,pixel_line)
	cv2.line(img,(581,424),(554,425),color,pixel_line)

	
	cv2.line(img,(579,272),(586,281),color,pixel_line)
	cv2.line(img,(586,281),(594,300),color,pixel_line)
	cv2.line(img,(594,300),(601,330),color,pixel_line)
	cv2.line(img,(601,330),(602,371),color,pixel_line)
	cv2.line(img,(602,371),(600,385),color,pixel_line)
	cv2.line(img,(600,385),(595,401),color,pixel_line)
	cv2.line(img,(595,401),(591,407),color,pixel_line)
	cv2.line(img,(591,407),(585,419),color,pixel_line)
	cv2.line(img,(585,419),(581,424),color,pixel_line)

def create_lampshade (img,color,pixel_line):
	cv2.line(img,(575,289),(587,308),color,pixel_line)
	cv2.line(img,(587,308),(589,321),color,pixel_line)
	cv2.line(img,(589,321),(590,349),color,pixel_line)
	cv2.line(img,(590,349),(589,372),color,pixel_line)
	cv2.line(img,(589,372),(586,385),color,pixel_line)
	cv2.line(img,(586,385),(578,399),color,pixel_line)

def create_image():

	img = np.ones((720,720,3), np.uint8)


	red = (25,25,255)
	white = (255,255,255)
	yellow = (0,255,255)
	pixel_line = 1


	create_base(img,white,pixel_line)
	create_stick (img,red,pixel_line)
	create_base_scope (img,white,pixel_line)
	create_scope (img,red,pixel_line)
	create_support (img,white,pixel_line)
	create_envolve (img,red,pixel_line)
	create_protection (img,white,pixel_line)
	create_lampshade (img,yellow,pixel_line)
	
	return img

def show_image(img):
	cv2.imshow("Lampshade",img)
	#key = cv2.waitKey(0)

def translate_image(img,h,v):
	height, width = img.shape[0], img.shape[1]

	move = np.float32([[1, 0, -v], [0, 1, -h]])
	new_img = cv2.warpAffine(img, move, (height, width))
	cv2.imshow("Settings has changed", new_img)


def rotate_image(img,angle):
	height, width = img.shape[0], img.shape[1]
	point =  (width/2,height/2)
	rotate = cv2.getRotationMatrix2D(point, angle, 1.0)
	new_img = cv2.warpAffine(img, rotate, (width, height))
	cv2.imshow("Rotation", new_img)
	img = new_img

def flip_image(img, flip):
	new_img = cv2.flip(img, flip)
	cv2.imshow("Flip", new_img)
	img = new_img

def scale_image(img,scale):
	height, width = img.shape[0], img.shape[1]
	point =  (width/2,height/2)
	scale = cv2.getRotationMatrix2D(point, 0, scale)
	new_img = cv2.warpAffine(img, scale, (width, height))
	cv2.imshow("Rotation", new_img)
	img = new_img
