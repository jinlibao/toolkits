function merged_picture = merge_pictures(working_directory)

%MERGE_PICTURES
% This program aims to merge pictures more conveniently.
% 
% Parameters:
%   working_directory: location of pictures to be merged
%   merged_picture: a matrix which comprises all pictures
% 
% Syntax:
%   1. merged_picture = merge_picture(working_directory)
%   2. merged_picture = merge_picture()
% 
% Author: Libao Jin
% Date: August 26, 2015
% Copyright (c) 2015 Libao Jin
% All rights reserved.
% License: The MIT License (MIT)


if nargin == 0
    working_directory = 'pictures';
end

% Get all filenames in the directory
cd(working_directory)
dirs = dir;
number_of_dirs = length(dirs);
pictures = {};

for i = 1:number_of_dirs
    if dirs(i).isdir == 0
        pictures{length(pictures) + 1, 1} = dirs(i).name;
    end
end

% Get the number of pictures
number_of_pictures = length(pictures);

% Merge all the pictures
merged_picture = [];
file_format = 'png';
file_location = strcat(working_directory, 'output\');
mkdir(file_location)
file_name = strcat(file_location, 'merged_picture.png');

for i = 1:number_of_pictures
    picture_name = pictures{i};
    picture = imread(picture_name);
    merged_picture = [merged_picture; picture];
end

% Show the picture and save it as local file
imshow(merged_picture)
imwrite(merged_picture, file_name, file_format)
sprintf('Summary:\n\t%d pictures have been merged.\n\tSee %s', number_of_pictures, file_name)
