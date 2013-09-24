function extract_features(filename)

I = single(rgb2gray(imresize(imread(filename), 0.2, 'Antialiasing', true)));
features = struct()

[frames, descriptors] = vl_sift(I);
features = setfield(features, 'frames', frames);
features = setfield(features, 'descriptors', descriptors);

% get exif data
exif = imfinfo(filename);
features = setfield(features, 'Model', exif.Model);
features = setfield(features, 'DateTime', datenum(exif.DateTime, 'yyyy:mm:dd HH:MM:SS'));

if isfield(exif, 'GPSInfo') && isfield(exif.GPSInfo, 'GPSLatitude')
    lat =  exif.GPSInfo.GPSLatitude(1)+ exif.GPSInfo.GPSLatitude(2)/60 +  exif.GPSInfo.GPSLatitude(3)/3600;
    lon =  exif.GPSInfo.GPSLongitude(1)+ exif.GPSInfo.GPSLongitude(2)/60 +  exif.GPSInfo.GPSLongitude(3)/3600;
    if(exif.GPSInfo.GPSLatitudeRef == 'S') lat = -lat; end
    if(exif.GPSInfo.GPSLongitudeRef == 'W') lon = -lon; end
    features = setfield(features, 'Latitude', lat);
    features = setfield(features, 'Longitude', lon);
else
    features = setfield(features, 'Latitude', NaN);
    features = setfield(features, 'Longitude', NaN);
end


save([filename(1:end-4), '_features.mat'], 'features');

end



