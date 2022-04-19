clc; close all; clear all;

rep = 'BDD/';
list=dir([rep '*.bmp']);
nbIm=numel(list);
moy = zeros(nbIm,1);

for i = 1:nbIm
    moy(i,1) = mean(mean(mean(imread(sprintf('%s%s',rep,list(i).name)))));
end

%% boite a moustache

figure()
moustache = boxplot(moy');title("boite à moustache des intensités des images")
Moyenne = mean(moy);
ecarttype = std(moy);