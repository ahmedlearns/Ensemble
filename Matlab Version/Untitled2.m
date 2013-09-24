figure;
subplot(1, 2, 1)
for match = matches
    subplot(1, 2, 1);
    imshow(img1); hold on;
    %perm = randperm(size(img1_f, 2))
    sel = match(1, :)
    h1 = vl_plotframe(img1_f(:, sel));
    h2 = vl_plotframe(img1_f(:, sel));
    set(h1, 'color', 'k', 'linewidth', 3)
    set(h2, 'color', 'y', 'linewidth', 2)
    hold off;
    
    subplot(1, 2, 2)
    imshow(img2); hold on;
    % perm = randperm(size(img2_f, 2))
    sel = match(2, :)
    h1 = vl_plotframe(img2_f(:, sel));
    h2 = vl_plotframe(img2_f(:, sel));
    set(h1, 'color', 'k', 'linewidth', 3)
    set(h2, 'color', 'y', 'linewidth', 2)
    hold off;
    
    pause(2)
end