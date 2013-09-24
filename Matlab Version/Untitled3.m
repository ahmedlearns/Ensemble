figure; hold on;
imshow(rgb2gray(imread('2013-05-12 13.24.34.jpg')))
perm = randperm(size(fa, 2))
sel = perm(1:2000)
h1 = vl_plotframe(fa(:, sel));
h2 = vl_plotframe(fa(:, sel));
set(h1, 'color', 'k', 'linewidth', 3)
set(h2, 'color', 'y', 'linewidth', 2)