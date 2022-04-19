close all;clear vars;

%% Data

chien = [1.403, 1.410, 1.375, 1.461, 1.017, 1.081, 1.229, 1.010, 1.207, 1.129];
boeuf = [0.714, 0.715, 0.674, 0.649, 0.720, 0.675, 0.679, 0.679, 0.656, 0.596];
cheval = [0.795, 0.814, 0.954, 0.951, 0.715, 0.714, 0.705, 0.999, 0.999, 1.047];
chevre = [0.438, 0.512, 0.357, 0.359, 0.372, 0.375, 0.343, 0.390, 0.389, 0.415];
cochon = [0.792, 0.780, 0.805, 0.829, 0.465, 0.466, 0.463, 0.598, 0.594, 0.542];
dragon = [0.855, 0.864, 0.923, 0.880, 0.620, 0.750, 0.695, 0.649, 0.669, 0.689];
lapin = [0.914, 0.906, 1.271, 1.262, 1.187, 1.015, 1.010, 1.058, 1.043, 1.013];
oiseau = [0.750, 0.750, 0.615, 0.618, 0.799, 0.665, 0.673, 0.682, 0.665, 0.608];
rat = [0.612, 0.562, 0.730, 0.718, 0.325, 0.350, 0.362, 0.505, 0.517, 0.500];
serpent = [0.607, 0.618, 0.479, 0.490, 0.597, 0.594, 0.577, 0.519, 0.793, 0.456];
singe = [1.236, 1.071, 1.578, 1.519, 1.233, 1.083, 1.052, 1.162, 1.256, 1.181];
tigre = [0.424, 0.420, 0.371, 0.386, 0.427, 0.434, 0.430, 0.426, 0.426, 0.468];

%% Tracé des données de l'élongation

indice = linspace(1,10,10);
figure();
% plot(indice, chien);hold on
% plot(indice, boeuf);hold on
% plot(indice, cheval);hold on
% plot(indice, chevre);hold on
% plot(indice, cochon);hold on
% plot(indice, dragon);hold on
% plot(indice, lapin);hold on
% plot(indice, oiseau);hold on
% plot(indice, rat);hold on
% plot(indice, serpent);hold on
% plot(indice, singe);hold on
% plot(indice, singe);hold on

plot(chien,indice);hold on
plot(boeuf,indice);hold on
plot(cheval,indice);hold on
plot(chevre,indice);hold on
plot(cochon,indice);hold on
plot(dragon,indice);hold on
plot(lapin,indice);hold on
plot(oiseau,indice);hold on
plot(rat,indice);hold on
plot(serpent,indice);hold on
plot(singe,indice);hold on
plot(tigre,indice);hold on

legend("chien", "boeuf", "cheval", "chevre", "cochon", "dragon", "lapin", "oiseau", "rat", "serpent", "singe", "tigre");
ylabel("indice échantillon");
xlabel("élongation");

%% Moyenne et écart type de la caractéristique élongation

Tab_moy = [mean(chien), mean(boeuf), mean(cheval), mean(chevre), mean(cochon), mean(dragon), mean(lapin), mean(oiseau), mean(rat), mean(serpent), mean(singe), mean(tigre)];
Tab_std = [std(chien), std(boeuf), std(cheval), std(chevre), std(cochon), std(dragon), std(lapin), std(oiseau), std(rat), std(serpent), std(singe), std(tigre)];