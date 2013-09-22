import cv2
import numpy as np
import itertools
import sys
import pickle

def findKeyPoints(img, template, distance=200):
    detector = cv2.FeatureDetector_create("SIFT")
    descriptor = cv2.DescriptorExtractor_create("SIFT")

    skp = detector.detect(img)
    skp, sd = descriptor.compute(img, skp)

    tkp = detector.detect(template)
    tkp, td = descriptor.compute(template, tkp)

    print("length of pre tkp: "+ str(len(tkp)))
    print("length of pre td: "+ str(len(td)))
    print("length of pre skp: "+ str(len(skp)))
    print("length of pre sd: "+ str(len(sd)))

    

    ###############################################################################################

    skp_serializable = []
    for kp in skp:
      skp_serializable.append((kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id))

    f = open("kp_dump.pkl", 'wb')
    pickle.dump(skp_serializable, f)
    f.close()
    f = open("des_dump.pkl", 'wb')
    pickle.dump(sd, f)
    f.close()

    skp_serializable = pickle.load(open("kp_dump.pkl", 'r'))
    sd = pickle.load(open("des_dump.pkl", 'r'))

    skp = []
    for kp in skp_serializable:
      skp.append(cv2.KeyPoint(x=kp[0][0], y=kp[0][1], _size=kp[1], _angle=kp[2], 
                        _response=kp[3], _octave=kp[4], _class_id=kp[5]))



    tkp_serializable = []
    for kp in tkp:
      tkp_serializable.append((kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id))

    f = open("kp_dump.pkl", 'w')
    pickle.dump(tkp_serializable, f)
    f.close()
    f = open("des_dump.pkl", 'w')
    pickle.dump(td, f)
    f.close()

    tkp_serializable = pickle.load(open("kp_dump.pkl", 'r'))
    td = pickle.load(open("des_dump.pkl", 'r'))

    tkp = []
    for kp in tkp_serializable:
      tkp.append(cv2.KeyPoint(x=kp[0][0], y=kp[0][1], _size=kp[1], _angle=kp[2], 
                        _response=kp[3], _octave=kp[4], _class_id=kp[5]))

    ###########################################################################################

    print("length of post tkp: "+ str(len(tkp)))
    print("length of post td: "+ str(len(td)))
    print("length of post skp: "+ str(len(skp)))
    print("length of post sd: "+ str(len(sd)))

    flann_params = dict(algorithm=1, trees=4)
    flann = cv2.flann_Index(sd, flann_params)
    idx, dist = flann.knnSearch(td, 1, params={})
    del flann

    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices]
    idx = [idx[i] for i in indices]
    skp_final = []
    for i, dis in itertools.izip(idx, dist):
        if dis < distance:
            skp_final.append(skp[i])

    flann = cv2.flann_Index(td, flann_params)
    idx, dist = flann.knnSearch(sd, 1, params={})
    del flann

    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices]
    idx = [idx[i] for i in indices]
    tkp_final = []
    for i, dis in itertools.izip(idx, dist):
        if dis < distance:
            tkp_final.append(tkp[i])

    return skp_final, tkp_final

def drawKeyPoints(img, template, skp, tkp, num=-1):
    h1, w1 = img.shape[:2]
    h2, w2 = template.shape[:2]
    nWidth = w1+w2
    nHeight = max(h1, h2)
    hdif = (h1-h2)/2
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)
    newimg[hdif:hdif+h2, :w2] = template
    newimg[:h1, w2:w1+w2] = img

    maxlen = min(len(skp), len(tkp))
    if num < 0 or num > maxlen:
        num = maxlen
    for i in range(num):
        pt_a = (int(tkp[i].pt[0]), int(tkp[i].pt[1]+hdif))
        pt_b = (int(skp[i].pt[0]+w2), int(skp[i].pt[1]))
        cv2.line(newimg, pt_a, pt_b, (255, 0, 0))
    return newimg


def match():
    img = cv2.imread(sys.argv[1])
    temp = cv2.imread(sys.argv[2])
    try:
        dist = int(sys.argv[3])
    except IndexError:
        dist = 200
    try:
        num = int(sys.argv[4])
    except IndexError:
        num = -1
    skp, tkp = findKeyPoints(img, temp, dist)
    newimg = drawKeyPoints(img, temp, skp, tkp, num)
    cv2.imshow("image", newimg)
    cv2.waitKey(0)

match()