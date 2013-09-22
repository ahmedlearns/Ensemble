import datetime as dt
#in -> 2 dictionaries from get_exif()
#out -> difference in location (GPS data)
def compare_pictures(pic1, pic2):
    if pic1["GPSInfo"] != None and pic2["GPSInfo"] != None:
        r = ((pic1["GPSInfo"][0]-pic2["GPSInfo"][0])**2 + (pic1["GPSInfo"][1]-pic2["GPSInfo"][1])**2) ** .5
    else:
        r = 0
    deltaT =(dt.datetime((int)(pic1["DateTime"][:4]), (int)(pic1["DateTime"][5:7]), (int)(pic1["DateTime"][8:10]), (int)(pic1["DateTime"][11:13]), (int)(pic1["DateTime"][14:16]), (int)(pic1["DateTime"][17:19])) - dt.datetime((int)(pic2["DateTime"][:4]), (int)(pic2["DateTime"][5:7]), (int)(pic2["DateTime"][8:10]), (int)(pic2["DateTime"][11:13]), (int)(pic2["DateTime"][14:16]), (int)(pic2["DateTime"][17:19]))).total_seconds()
    #deltaT1 = dt.datetime(int(pic2[:4]), int(pic2[5:7]), int(pic2[8:10]), int(pic2[11:13]), int(pic2[14:16]), int(pic2[17:19]))
    return [r, deltaT]

#test case
#pic1 = {'Make': 'Motorola', 'DateTime': '2013:10:20 10:40:24', 'Model': 'MB855', 'GPSInfo': [33.775, -84.3963888888889]}
#pic2 = {'Make': 'Motorola', 'DateTime': '2013:09:20 09:50:32', 'Model': 'MB855', 'GPSInfo': [33.775, -84.3963888888889]}
#print compare_pictures(pic1, pic2)


#def matmult(a):
#    #b = [WEIGHTED MATRIX]
#    zip_b = zip(*b)
#    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]
