![Alt text](https://github.com/CourbotA/Naruto/blob/main/logo.svg)
<img scr="https://github.com/CourbotA/Naruto/blob/main/logo.svg">
# Naruto: shape and color recognition project.

The goal of this project is to interpret the signs of naruto from a database that contains images of people who make signs with their hands.
We take a minimum of 20 images for each sign, to have a diversity of data, and measure the quality of our processing.
Technologies that we will use:
we will use **Python** to process images and to create interfaces.

**Python** is a high level, easy to use language that offers efficient features for image processing and simple features for creating graphical interfaces.

##  Contributors(in alphabetical order):
- BOURLET Clement
- COURBOT Antoine
- GONCALVES DE CARVALHO Mathilde
- LELIEVRE Kevin
- SABIR Ilyass

## Data acquisition
Taking pictures of the following 12 signs of naruto: 
<img align="right" alt="coding" width="400" src="https://github.com/CourbotA/Naruto/blob/main/narutoSignes.jpg">
*  Bird
*  Boar
*  Dog
*  Dragon
*  Hare
*  Horse
*  Monkey
*  Ox
*  Ram
*  Rat
*  Serpant
*  Tiger.

We took **13 pictures per sign**, so 156 pictures in total.

here is an extract of the data base we built: 

![Alt text](https://github.com/CourbotA/Naruto/blob/main/extrait_BDD.png)
<img scr="https://github.com/CourbotA/Naruto/blob/main/extrait_BDD.png">

Since our goal is to recognize the signs of Naruto, we chose to put a blank sheet of paper of A3 size.

## Image preprocessing
The first step consist on segmenting the hands using color attributes to get a mask of the hands.

## Feature choice and detection
This step consist on finding the relevent features of the dataset whiwh will allow us to classify our images.
We therefore have to calculate the feature vector of each image and elaborate a classification method that works on our dataset 
with an accuracy > 0.9X

## GUI
The objective is to build an interface in C++ and create a fighting game.
The user will upload hand signs, that the software will recognize those and combination will launch attacks on the other player.
## Segmentation of the region of interest (**ROI**)
By color segmentation in the HSV color space, we were able to extract the hand masks.
![Alt text](https://github.com/CourbotA/Naruto/blob/main/Extrait_ROI.png)
<img scr="https://github.com/CourbotA/Naruto/blob/main/Extrait_ROI.png">
