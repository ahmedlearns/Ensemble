from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded in ["Make", "DateTime", "Model"]:
	    ret[decoded] = value
	elif decoded == "GPSInfo":
            if len(value) > 2:
                longitude = value[2]
     	        print longitude
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
