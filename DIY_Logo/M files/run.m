% About IMWRITE
% Presented by JinLibao
% Copyright (c) 2013 JinLibao
% All Rights Reserved
% Show the usages of IMWRITE

clear;clc;
% Grayscale Images (black and white)
% print logo "ZJUT" and save the picture as a file
ZJUT = [letterz(5) letterj(7) letteru(9) lettert(11)];
ZJUT = ZJUT(100:-1:1,:);
mesh(ZJUT);
ZJUT = ZJUT(100:-1:1,:);
ZJUT = ZJUT/11;
figure;
imshow(ZJUT);                                % display the logo
imwrite(ZJUT,'..\Results\ZJUT.png','png');   % save the picture of format "png"
ZJUT2 = ones(100,320)-ZJUT;
figure;
imshow(ZJUT2);                                 % display the logo
imwrite(ZJUT2,'..\Results\ZJUT2.png','png');   % save the picture of format "png"

% Color Images (black and white)
% print logo "ZJUT" and save the picture as a file
red = 250;
green = 30;
blue = 100;
redZJUT = red*ZJUT;
greenZJUT = green*ZJUT;
blueZJUT = blue*ZJUT;
colorZJUT(:,:,1) = redZJUT;
colorZJUT(:,:,2) = greenZJUT;
colorZJUT(:,:,3) = blueZJUT;
colorZJUT = uint8(colorZJUT); 
figure;
imshow(colorZJUT);                                    % display the logo
imwrite(colorZJUT,'..\Results\color_ZJUT.png'); % save the picture of format "png"


% You can use imwrite to convert the format of the picture file
JinLibao = imread('..\Pictures\JinLibao.png');
JinLibao4D(:,:,:,1) = JinLibao;
JinLibao4D(:,:,:,2) = uint8(255-JinLibao);
imwrite(JinLibao4D,'..\Results\JinLibao.gif','Writemode','overwrite','DisposalMethod','doNotSpecify','DelayTime',100,'TransparentColor',0,'BackgroundColor',0,'LoopCount',Inf);
imwrite(JinLibao,'..\Results\JinLibao.hdf');
imwrite(JinLibao,'..\Results\JinLibao.jpg');
imwrite(JinLibao,'..\Results\JinLibao.tiff');
imwrite(JinLibao,'..\Results\JinLibao.ras');
imwrite(JinLibao,'..\Results\JinLibao.pbm');
imwrite(JinLibao,'..\Results\JinLibao.pgm');
imwrite(JinLibao,'..\Results\JinLibao.ppm');
JinLibaohaf = imread('..\Results\JinLibao.hdf');
figure; imshow(JinLibaohaf);
JinLibaopbm = imread('..\Results\JinLibao.pbm');
figure; imshow(JinLibaopbm);
JinLibaopgm= imread('..\Results\JinLibao.pgm');
figure; imshow(JinLibaopgm);
JinLibaoppm = imread('..\Results\JinLibao.ppm');
figure; imshow(JinLibaoppm);
JinLibaoras = imread('..\Results\JinLibao.ras');
imshow(JinLibaoras);

% You can use imwrite to convert the forms of picture
Library = imread('..\Pictures\Library.png');
Librarygray = rgb2gray(Library);                    % convert RGB image to grayscale
imwrite(Librarygray,'..\Results\Library_gray.png');

[Libraryindexed,map] = rgb2ind(Library,256);        % convert RGB image to indexed image
imwrite(Libraryindexed,'..\Results\Library_indexed.png');

Libraryntsc = rgb2ntsc(Library);                    % convert RGB color values to NTSC color space
imwrite(Libraryntsc,'..\Results\Library_ntsc.png');

Librarybw = im2bw(Library,0.5);                     % converts the truecolor image RGB to a binary image
imwrite(Librarybw,'..\Results\Library_bw.png');

figure;
subplot(2,2,1); imshow(Librarygray); title('Grayscale image');
subplot(2,2,2); imshow(Libraryindexed); title('Indexed image');
subplot(2,2,3); imshow(Libraryntsc); title('NTSC color space');
subplot(2,2,4); imshow(Librarybw); title('Binary image');

% The general imwrite syntax applicable for jpg image
% syntax: imwrite(A,'filename.jpg','quality',q), q range from 0 to 100
Lotus = imread('..\Pictures\Lotus.png');
imwrite(Lotus,'..\Results\Quality\Lotus_0.jpg','quality',0);
imwrite(Lotus,'..\Results\Quality\Lotus_5.jpg','quality',5);
imwrite(Lotus,'..\Results\Quality\Lotus_10.jpg','quality',10);
imwrite(Lotus,'..\Results\Quality\Lotus_15.jpg','quality',15);
imwrite(Lotus,'..\Results\Quality\Lotus_30.jpg','quality',30);
imwrite(Lotus,'..\Results\Quality\Lotus_50.jpg','quality',50);
imwrite(Lotus,'..\Results\Quality\Lotus_100.jpg','quality',100);
Lotus0 = imread('..\Results\Quality\Lotus_0.jpg');
Lotus5 = imread('..\Results\Quality\Lotus_5.jpg');
Lotus10 = imread('..\Results\Quality\Lotus_10.jpg');
Lotus15 = imread('..\Results\Quality\Lotus_15.jpg');
Lotus30 = imread('..\Results\Quality\Lotus_30.jpg');
Lotus50 = imread('..\Results\Quality\Lotus_50.jpg');
Lotus100 = imread('..\Results\Quality\Lotus_100.jpg');
figure;
subplot(2,4,1); imshow(Lotus); title('Original Image');
subplot(2,4,2); imshow(Lotus0); title('Image with q=0');
subplot(2,4,3); imshow(Lotus5); title('Image with q=5');
subplot(2,4,4); imshow(Lotus10); title('Image with q=10');
subplot(2,4,5); imshow(Lotus15); title('Image with q=15');
subplot(2,4,6); imshow(Lotus30); title('Image with q=30');
subplot(2,4,7); imshow(Lotus50); title('Image with q=50');
subplot(2,4,8); imshow(Lotus100); title('Image with q=100');

% Another usage
COS = imread('..\Pictures\College of Science.png');
COSd = double(COS);
Cosinv = COSd(512:-1:1,:);
figure;
mesh(Cosinv);
axis image;
[nx,ny]=size(Cosinv);
para = 1.;
gamma = 1;
newb =255*para*(COSd/255).^gamma;
newb1=uint8(newb);
imwrite(newb1,'..\Results\College of Science.png');

% DIY a simple logo for yourself
diylogo;
diycolorlogo;