#conding=utf8  
import os
def bmp2svg():
	g = os.walk("./fz_out")
	potracePath = '.\\potrace-1.16.win32\\potrace.exe'
	for path,dir_list,file_list in g:
	    for file_name in file_list:
	        inf=".\\fz_out\\"+file_name
	        outf=".\\fz_svg\\"+file_name[:-4]+".svg"
	        s=f"{potracePath} "+inf+" -s -o "+outf
	        print(s)
	        os.system(s)
#font.generate("output.ttf")



