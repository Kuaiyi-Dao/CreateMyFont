import os
import cv2 as cv
import numpy as npy
import hashlib
import imgFuntions

InfoFile = open('infoFile.txt','r')
Info = InfoFile.read()
if Info == '':
	print('no infomation!')
	exit(-1)
keystr =b'{Info}'
key_md5 = hashlib.md5(keystr)
key_md5_str = str(key_md5.hexdigest())

def main():
	g = os.walk("./output")
	for path,dir_list,file_list in g:
		for file_name in file_list:
			img = cv.imread("./output/"+file_name, 0)
			imgarray = img // 255
			imgarray = imgarray *255
			CheckArray = npy.zeros((len(imgarray[:,1]),len(imgarray[1,:])))
			moveCount = 0
			# print(len(imgarray[:,1]),len(imgarray[1,:]))
			for raw in range(len(imgarray[:,1])):
				for col in range(len(imgarray[1,:])):
					if imgarray[raw,col] != 255 and CheckArray[raw,col] != 1:
						CheckArray[raw,col] = 1
						direction = imgFuntions.WhiteEdge(raw,col,CheckArray,imgarray)
						path = imgFuntions.getStraightEdge(raw,col,direction,CheckArray,imgarray)
						if (direction != None and path != None):
							moveCount = imgFuntions.straightEdgeChange(direction,path,key_md5_str,moveCount,imgarray,CheckArray)
			cv.imwrite("./fz_out/"+file_name,imgarray)

main()






