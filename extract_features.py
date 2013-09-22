from PIL import Image
from PIL.ExifTags import TAGS
from urllib import FancyURLopener

import pickle
import cv2
import numpy as np
import itertools
import sys
import yaml


def extract_features(img):
  detector = cv2.FeatureDetector_create("SIFT")
  descriptor = cv2.DescriptorExtractor_create("SIFT")

  key_points = detector.detect(img)
  key_points, descr = descriptor.compute(img, key_points)

  kp_serializable = []
  for kp in key_points:
    kp_serializable.append((kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id))

  f = open("kp_dump.pkl", 'w')
  pickle.dump(kp_serializable, f)
  f.close()
  f = open("des_dump.pkl", 'w')
  pickle.dump(descr, f)
  f.close()


  #### DESERIALIZING - FOR RETRIEVING INFO #########
  # kp_serializable = pickle.load(open("kp_dump.pkl", 'r'))
  # descr = pickle.load(open("des_dump.pkl", 'r'))

  # key_points = []
  # for kp in kp_serializable:
  #   key_points.append(cv2.KeyPoint(x=kp[0][0],y=kp[0][1], _size=kp[1], _angle=kp[2], 
  #                           _response=kp[3], _octave=kp[4], _class_id=kp[5]))


def get_exif(fn):
    ret = {}
    try:
        i = Image.open(fn)
        info = i._getexif()
    except:
        sys.exit()
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


#prevents websites thinking that this code is from a spam/robot/hacker, even though it is...
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

if len(sys.argv) == 2:
    myopener = MyOpener()
    myopener.retrieve(sys.argv[1], "downloaded_image.jpg")
    extract_features(cv2.imread("downloaded_image.jpg"))
    exif = get_exif("downloaded_image.jpg")
    #store into rails db?!
    print exif
    os.remove("downloaded_image.jpg")
else:
    sys.exit("Incorrect number of arguments")
