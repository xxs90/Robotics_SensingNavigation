% draw features
I = imread('./resized_img/IMG_5412.jpg');
I = im2gray(I);
points = detectSIFTFeatures(I);
figure
imshow(I)
hold on
plot(points,'ShowScale',false)
hold off

%%
% time consuming
% ORB
tStart = tic; 
srcFiles = dir('./resized_img/*.jpg');  % the folder in which ur images exists
T_ORB = zeros(1,length(srcFiles));
for i = 1 : length(srcFiles)
filename = strcat('./resized_img/',srcFiles(i).name);
im = imread(filename);
tic
points = detectORBFeatures(I);
T_ORB(i)= toc;
end
toc

%SURF

tStart = tic; 
srcFiles = dir('./resized_img/*.jpg');  % the folder in which ur images exists
T_SURF = zeros(1,length(srcFiles));
for i = 1 : length(srcFiles)
filename = strcat('./resized_img/',srcFiles(i).name);
im = imread(filename);
tic
points = detectSURFFeatures(I);
T_SURF(i)= toc;
end


%SIFT

tStart = tic; 
srcFiles = dir('./resized_img/*.jpg');  % the folder in which ur images exists
T_SIFT = zeros(1,length(srcFiles));
for i = 1 : length(srcFiles)
filename = strcat('./resized_img/',srcFiles(i).name);
im = imread(filename);
tic
points = detectSIFTFeatures(I);
T_SIFT(i)= toc;
end

plot(T_ORB)
hold on

plot(T_SURF)
hold on

plot(T_SIFT)
hold on

legend('ORB','SURF',"SIFT")
title('time consuption of different detectors')
