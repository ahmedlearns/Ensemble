function score = match(f1, f2, threshold)

load([f1(1:end-4), '_features.mat'])
img1_f = features.frames;
img1_d = features.descriptors;

load([f2(1:end-4), '_features.mat'])
img2_f = features.frames;
img2_d = features.descriptors;

[matches, scores] = vl_ubcmatch(img1_d, img2_d, threshold);
score = mean(scores);

end