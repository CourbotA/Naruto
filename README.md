![Alt text](https://github.com/CourbotA/Naruto/blob/main/logo.svg)
<img scr="https://github.com/CourbotA/Naruto/blob/main/logo.svg">
# <span style="color:red; font-family: 'Bebas Neue';">Naruto: shape and color recognition project.</span>

The goal of this project is to interpret the signs of naruto from a database that contains images of people who make signs with their hands.
We take a minimum of 20 images for each sign, to have a diversity of data, and measure the quality of our processing.
Technologies that we will use:
we will use **Python** to process images and to create interfaces.

**Python** is a high level, easy to use language that offers efficient features for image processing and simple features for creating graphical interfaces.

##  <span style="color:blue">Contributors:</span>
- BOURLET Clement
- COURBOT Antoine
- GONCALVES DE CARVALHO Mathilde
- LELIEVRE Kevin
- SABIR Ilyass

## Acquisition des données
Prise en photos des 12 signes da naruto suivantes: 
<img align="right" alt="coding" width="400" src="https://github.com/CourbotA/Naruto/blob/main/narutoSignes.jpg">
*  L'oiseau (ou le coq)
*  Le cochon ( porc ou sanglier)
*  Le chien
*  Le Dragon
*  Le Lapin
*  Le cheval
*  Le Boeuf (ou bufffle)
*  Le Singe
*  Le Mouton (ou chèvre)
*  Le Rat
*  Le Serpent
*  Le Tigre.

On a pris **13 photos par signe**, et donc 156 images au total.

## Image preprocessing
The first step consist on segmenting the hands using color attributes to get a mask of the hands.

## Feature choice and detection
This step consist on finding the relevent features of the dataset whiwh will allow us to classify our images.
We therefore have to calculate the feature vector of each image and elaborate a classification method that works on our dataset 
with an accuracy > 0.9X

## GUI
The objective is to build an interface in C++ and create a fighting game.
The user will upload hand signs, that the software will recognize those and combination will launch attacks on the other player.
