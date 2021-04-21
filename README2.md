# Présentation du jeu

Le jeu que nous avons produit consiste à resister face aux astronautes venus nous envahir et à une pluit de météorites. Afin de se défendre, en tant qu'alien, nous avons le pouvoir de tirer des projectiles sur les envahisseurs avec la touche espace. 
Pour échapper aux météorites, il faut simplement les ésquiver en allant à droite ou à gauche, grace aux flèches present sur le clavier.
Ce jeu contient différents niveaux, il faut d'abord tuer tous les astronautes pour ensuite affronter les météorites. Une fois terminer, le niveau suivant est activé et la difficulté est augmenté. le but finale de ce jeu est de faire le plus de point possible

## exemple
![Below sleeping surface](img/IMG_6404.JPG)
Ici, il s'agit du menu du jeu. Lorsque le START est enclencher, la class GAME/update et le "while running" se mette en marche pour générer le jeu.

![Below sleeping surface](img/IMG_6405.JPG)
L'alien perd des points de vie lorsqu'il rentre en contact avec l'astronautes.
L'alien est géré par une classe Player, qui hérite de sprite. Cette classe est composé de plusieur méthode tel que, par exemple, move_r/l qui gère les déplacements. 
L'astronaute est gérer par sa propre classe Astro. Cette classe gère les dégat, la vitesse etc de l'astronaute mais aussi les collisions propre à ce dernier et les dégat qu'elle génère sur l'alien.

![Below sleeping surface](img/IMG_6406.JPG)
l'alien est confronter a une pluit de météorites. Ces dernieres sont gérer par une classe Comet. L'événement de la chute d'asteroid est gérer par la classe CometFallEvent. Cette classe enclanche la chute de météorite quand certain critère sont rempli, tel que la bar d'événement en bas de l'écran. Cette dernière doit être pleine pour enclencher l'événement.
Les projectile tiré par l'alien, qui permette d'éliminer les astronaute sont gérés par une class Projectiles. Cette dernière gère la vitesse, la rotation et les collisions des projectiles.

Pour faire fonctionner notre jeu, nous avons utilisé des classes dites héréditaires




Source : pygame.org
 #          youtube.com/Collisons in Pygame
 #          youtube.com/Pygame in 90 Minutes - For beginners
 #          youtube.com/Python Final Fantasy Style RPG Battle Beginner Tutorial in Pygame
