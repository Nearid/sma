couleur :
- SuperPredator : bleu
- Carnivore : rouge
- Herbivore : vert
- Décomposeur : marron


- Agent endormi : point noir
- Agent mort : point blanc

Le cercle autour des agents veulent dire qu'ils chassent. Ils chassent si leur jauge de faim est rempli à au moins 50%

Comportements :

Le "comportement" est spécifié dans la méthode update() de la classe Agent. Cette méthode "choisit" une action
en fonction de l'environnement.

Si dans ma perception j'ai :

- des prédateurs et des "amis*" : je suis mon ami
- dans prédateurs, mais pas d'amis : je fuis mes prédateurs
- des proies, des amis, mais pas de prédateurs :
    - si j'ai "faim" (càd je suis en mode "chasse" comme expliqué plus haut) → je chasse ma proie la plus proche
    - sinon → je suis mon ami
- des proies et que je chasse → je chasse ma proie la plus proche
- dans tous les autres cas → je me déplace aléatoirement



*ami = agent symbiotique*