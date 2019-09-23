import cv2
import numpy as np
from util import Util
from time import sleep

frameCount = 0
kills = 0
template = Util.resize(cv2.imread('template.png'))
tempGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

print('Starting')
while True:
	frameCount += 1
	image = Util.screenshot()
	if image.any():
		image = Util.resize(image)
		image = Util.get_roi(image)
		grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		result = cv2.matchTemplate(grayImage, tempGray, cv2.TM_CCOEFF_NORMED)
		threshold = 0.7
		loc = np.where(result >= threshold)

		if np.any(loc):
			print("Matched")
			kills += 1
			print('Kills: ', kills)

			Util.found_kill()

			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
			top_left = max_loc
			h,w = tempGray.shape
			bottom_right = (top_left[0] + w, top_left[1] + h)
			cv2.rectangle(image, top_left, bottom_right,(0, 0, 255), 4)
			cv2.imwrite("./Captured/hitframe%d.jpg" % frameCount, image)
			sleep(3)

print('Total Kills: ', kills)
