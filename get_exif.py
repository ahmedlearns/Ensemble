#these might be just installed on the heroku instance, that will save some computational time

from PIL import Image
from PIL.ExifTags import TAGS
from urllib import FancyURLopener
import os
import sys


def get_exif(fn):
    ret = {}
    try:
        i = Image.open(fn)
        info = i._getexif()
    except: 
       os.remove(fn)
       return 1 

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded in ["Make", "DateTime", "Model"]:
            ret[decoded] = value
        elif decoded == "GPSInfo":
            if len(value.keys()) > 2:
                longitude = value[2]
                longitude = (float)(longitude[0][0]*1.0 + longitude[1][0]/60.0 + longitude[2][0]/3600.)
                if value[1] == 'S':
                        longitude *= -1
                latitude = value[4]
                latitude = (float)(latitude[0][0]*1.0 + latitude[1][0]/60.0 + latitude[2][0]/3600.0)
                if value[3] == 'W':
                    latitude *= -1
                    ret[decoded] = [longitude, latitude]
            else:
                 ret[decoded] = None
    return ret
#prevents websites thinking that this code is from a spam/robot/hacker, even though it is...
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

if len(sys.argv) == 2:
    myopener = MyOpener()
    myopener.retrieve(sys.argv[1], "file.jpg")
    exif = get_exif("file.jpg")
    #store into rails db?!
    os.remove("file.jpg")
else:
    sys.exit("Incorrect number of arguments")

