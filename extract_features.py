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

  flann_params = dict(algorithm=1, trees=4)
  flann = cv2.flann_Index(descr, flann_params)
  idx, dist = flann.knnSearch(descr, 1, params={})
  del flann

  kp_serializable = []
  for kp in key_points:
    kp_serializable.append((kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id))

  # print key_points[0].angle
  x=yaml.dump({'key_points': kp_serializable})
  print yaml.load(x)

extract_features(cv2.imread(sys.argv[1]));