srcFiles = dir('./ori_img/*.JPG');  % the folder in which ur images exists
for i = 1 : length(srcFiles)
filename = strcat('./ori_img/',srcFiles(i).name);
im = imread(filename);
k=imresize(im,[2160,3840]);
newfilename=strcat('./resized_img_4k/',srcFiles(i).name);
imwrite(k,newfilename,'jpg');
end

%%
cameraCalibrator("./resized_img_4k", 30)