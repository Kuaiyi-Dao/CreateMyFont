import os
import fontProcessing

def init():
	fz_out_path = "./fz_out"
	fz_svg_path = "./fz_svg"
	output_path = "./output"
	pathList = os.listdir(fz_out_path)
	for file in pathList:
		os.remove(fz_out_path+'/'+file)
	pathList = os.listdir(fz_svg_path)
	for file in pathList:
		os.remove(fz_svg_path+'/'+file)
	pathList = os.listdir(output_path)
	for file in pathList:
		os.remove(output_path+'/'+file)

if __name__ == '__main__':
	PythonPath = "ffpython\\python.exe"
	impofilePath = 'import.py'
	expofilePath = 'export.py'
	init()
	Command = PythonPath+' '+expofilePath
	os.system(Command)
	fontProcessing.start()
	Command = PythonPath+' '+impofilePath
	os.system(Command)


