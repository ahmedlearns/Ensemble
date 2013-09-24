function group_pictures(gps_weight, time_weight, sift_weight, reset_db)
clc;close all;

dir_listing = dir;
list_of_images = {};
for item_index = 1:length(dir_listing)
    item = dir_listing(item_index);
    if length(strfind(item.name, '.jpg')) > 0
        list_of_images{end+1} = item.name;
    end
end

if reset_db
% PRE-Processing
for photo_id = 1:length(list_of_images)
    extract_features(list_of_images{photo_id});
end
% Normalize
normalize_features(list_of_images);
end

groups = {};
threshold = 0.2;
% gps_weight = 0; time_weight = 0; sift_weight = 3;
for photo_id = 1:length(list_of_images)
    scores = [];
%     imshow(list_of_images{photo_id})
    for group_id = 1:length(groups)
        scores(end+1) = score_comparison(groups{group_id}, gps_weight, time_weight, sift_weight, list_of_images{photo_id});
    end
    if(length(groups) == 0 || min(scores) > threshold)
        group = struct();
        group = setfield(group, 'file_list', list_of_images(photo_id));
        groups{end+1} = group;
    else
        [m, loc] = min(scores);
        groups{loc}.file_list(end+1) = list_of_images(photo_id);
    end
end


for group_id = 1:length(groups)
    fl = groups{group_id}.file_list
    counter = 1;
    figure;
    for x = fl
        subplot(1, length(fl), counter)
        hold on
        x = x{1};
        imshow(imread(x));
        load([x(1:end-4), '_features.mat']);
        title(features.DateTime);
        features.DateTime
        counter = counter + 1;
    end
    hold off
end
