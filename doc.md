# Documentation


## l'objectif du projet est de permetre a un agent IA d'utilisé un extrait de porte folio pour repondre a des question sur moi 

la methode utilisé est de decoupé des fichier markdown dans lesquels sont ecrite les informations du portfolio en chunk  puis de les indexé dans une base upstash qui va les transformer en vecteurs lisible par un agent IA  qui par la suite pourras les utilisés pour repondre au question de l'utilisateur 

le fichier indexation.py contient les fonction de pour decoupé les info en chunk chunk() et la fonciton pour envoyer les donnée sur upstash  upsert() 
en executant indexation les fonciton precedente vont faire l'indexation des fichier markdown dans la variable data (lst des chemin des md)

le fichier agent.py construit l'agent IA pour qu'il reponde en utilisant les donnée sur upstash 

le fichier lit.py contient le code de l'application streamlit qui permet de creer une interface de communication avec l'agent IA 

les fichier doivent etre executer dan sl'ordre suivant indexation.py > agent.py > lit.py