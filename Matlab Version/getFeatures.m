function getFeatures(filename)

i1 = rgb2gray(imresize(imread(filename), 0.2));
im1 = single(i1);
[features, descriptors] = vl_sift(im1);
save([filename, '_features.mat'], 'features', 'descriptors')

end