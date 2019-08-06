import os
from PIL import Image
import image_slicer
#from earthexplorer import _download
from landsatxplore.earthexplorer import EarthExplorer

ee = EarthExplorer("yashkasturi100@gmail.com", "Yashkasturi100")

ee.download(scene_id='LC81480462018321LGN00', output_dir='')

#print (earthexplorer._download.name)
a=ee.printf()
print (a)

#print (ee.name)

ee.logout()

a.replace("LC08_L1TP_","")
a.replace("_01_T1","")

print(a)

#partialFileName = "*_*_*"

#for f in os.listdir():
 #   if partialFileName = f[:len(partialFileName)]:
  #      print(f)

#for filename in os.listdir('C:/Users/Yash/Desktop/B.E Project/landsatxplore-master'):
#	if fnmatch.fnmatch(filename, '*_*_*.jpeg'):
#print(filename)

colorImage  = Image.open(a)

# Rotate it by 45 degrees
rotated     = colorImage.rotate(13)
#rotated.show()
rotated.save('r.jpg')

#cropping of black frame
img = Image.open("r.jpg")
area =(679,639,6998,7208)
cropped = img.crop(area)
cropped.save('148_46.jpg')


#slicing of cropped image into 100 parts
tiles=image_slicer.slice('148_46.jpg', 100, save=False)
image_slicer.save_tiles(tiles, directory='C:/Users/SnehaDL/Desktop/landsatxplore-master/save',\
	prefix='148_46', format='jpeg')
