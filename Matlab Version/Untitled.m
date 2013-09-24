function extract_features(filename)

I = single(rgb2gray(imread(filename)));

[frames, descriptors] = vl_sift(I);

save([filename, '_frames.mat'], frames);

end



