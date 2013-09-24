function normalize_features(list_of_images)

time_max = -Inf;
time_min = Inf;

lat_max = -Inf;
lat_min = Inf;

lon_max = -Inf;
lon_min = Inf;


for photo_id = 1:length(list_of_images)
    filename = list_of_images{photo_id};
    load([filename(1:end-4), '_features.mat']);
    
    if features.DateTime > time_max
        time_max = features.DateTime
    end
    if features.DateTime < time_min
        time_min = features.DateTime
    end
    
    if ~isnan(features.Latitude)
        if features.Latitude > lat_max
            lat_max = features.Latitude
        end
        if features.Latitude < lat_min
            lat_min = features.Latitude
        end

        if features.Longitude > lon_max
            lon_max = features.Longitude
        end
        if features.Longitude < lon_min
            lon_min = features.Longitude
        end
    end
    
end

for photo_id = 1:length(list_of_images)
    filename = list_of_images{photo_id};
    load([filename(1:end-4), '_features.mat']);
    
    features.DateTime = (features.DateTime - time_min);
    features.DateTime = features.DateTime / (time_max - time_min);
    
    features.Latitude = (features.Latitude - lat_min);
    features.Latitude = features.Latitude / (lat_max - lat_min);
    
    features.Longitude = (features.Longitude - lon_min);
    features.Longitude = features.Longitude / (lon_max - lon_min);
    
    save([filename(1:end-4), '_features.mat'], 'features');
end

end