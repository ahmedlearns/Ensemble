function out = score_comparison(group, gps_weight, time_weight, sift_weight, filename)
    load([filename(1:end-4), '_features.mat']);
    img_features = features;

    fl = group.file_list;
    gps_lats = img_features.Latitude;
    gps_lons = img_features.Longitude;
    times = img_features.DateTime;
    scores = [];
    
%     indices = unique(1 + round(rand(1, min(length(fl),50)) * (length(fl)-1)));
    indices = length(fl);
    for i = 1:indices
        f = fl{i};
        load([f(1:end-4), '_features.mat']);
        
        if ~isnan(features.Latitude)
            gps_lats(end + 1) = features.Latitude;
            gps_lons(end + 1) = features.Longitude;
        end
        
        times(end + 1) = features.DateTime;
        
        scores(end+1) = match(f, filename, 2.5);
        if isnan(scores(end))
            scores(end) = 80000;
        end
    end

%     gps_lats = gps_lats - min(gps_lats);
%     gps_lats = gps_lats / max(gps_lats);
% 
%     gps_lons = gps_lons - min(gps_lons);
%     gps_lons = gps_lons / max(gps_lons);
%     
%     times = times - min(times);
%     if max(times) == 0
%         times = times*0;
%     else
%         times = times / max(times);
%     end

    gps_lats_group = mean(gps_lats(2:end));
    gps_lons_group = mean(gps_lons(2:end));
    times_group = mean(times(2:end));
    scores = mean(scores) / 80000;

    out = gps_weight * abs(gps_lats(1) - gps_lats_group) + ...
        gps_weight * abs(gps_lons(1) - gps_lons_group) + ...
        time_weight * (abs(times(1) - times_group)) + ...
        sift_weight * (scores);
    
    out = out / (2*gps_weight + time_weight + sift_weight);
    
end