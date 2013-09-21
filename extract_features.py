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

  # print len(key_points)
  # print descr.shape
  # print type(float(descr[0][0]))

  #######################################################################
  # serializable = []
  # for i = range(0 to len(key_points)):
  #   serializable.append((kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id, float(descr[i]) ))
  #######################################################################


  kp_serializable = []
  for kp in key_points:
    kp_serializable.append((kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id))

  f = open("kp_dump.pkl", 'wb')
  pickle.dump(kp_serializable, f)
  f.close()
  f = open("des_dump.pkl", 'wb')
  pickle.dump(descr, f)
  f.close()

  kp_serializable = pickle.load(open("kp_dump.pkl", 'r'))
  descr = pickle.load(open("des_dump.pkl", 'r'))

  key_points = []
  for kp in kp_serializable:
    key_points.append(cv2.KeyPoint(x=kp[0][0],y=kp[0][1], _size=kp[1], _angle=kp[2], 
                            _response=kp[3], _octave=kp[4], _class_id=kp[5]))
  

  # descr_serializable = []
  # for i in xrange(len(descr)):
  #   descr_serializable.append([0 for j in xrange(len(descr[i]))])

  # # print descr_serializable

  # for d in range(len(descr)):
  #   descr_serializable.append([float(x) for x in descr[d]])
    # for x in descr[d]:
    #   descr_serializable[d].append(float(x))

  # print descr_serializable
  # print key_points[0].angle
  # x = yaml.dump({'key_points': kp_serializable}) #, 'descriptors': descr})
  # print yaml.load(x)


  # print type(descr[0][0])
  # x =yaml.dump({'test': descr_serializable})
  # print yaml.load(x);
  # print x

extract_features(cv2.imread(sys.argv[1]))