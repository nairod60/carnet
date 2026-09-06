# -*- coding: utf-8 -*-
"""Programme 4 jours, épaule ménagée. Source unique pour les fiches et le tableur."""

SEANCES = [
 dict(id="J1", jour="Lundi", titre="Haut A — Tirage",
      focus="Dos, deltoïde postérieur, biceps — la séance qui protège ton épaule",
      exos=[
   ("Dos","Tractions, prise supination ou neutre","3","max","120 s",
    "LARGEUR D'ÉPAULES, jamais large : la prise large bloque l'omoplate. Si tu ne fais pas 5 reps, fais des négatives de 5 s."),
   ("Dos","Rowing haltères buste penché","3","8-10","90 s","Buste à 45°, tire vers le nombril, coudes près du corps."),
   ("Dos","Rowing unilatéral, appui sur le banc","3","10-12 / bras","75 s","Genou et main sur le banc, amplitude complète."),
   ("Deltoïde postérieur","Oiseau sur banc incliné","3","15","60 s","Poitrine sur le banc à 30°. Léger : 3 à 5 kg."),
   ("Trapèzes / stabilisateurs","Élévations en Y sur banc incliné","3","12","60 s",
    "Bras tendus en Y, pouces vers le haut, 2 à 4 kg. C'est ce qui fait tourner l'omoplate et libère l'épaule."),
   ("Biceps","Curl marteau","3","10-12","60 s","Prise neutre. Les tractions en supination ont déjà chargé lourdement le biceps."),
   ]),
 dict(id="J2", jour="Mardi", titre="Bas A — Quadriceps",
      focus="Quadriceps, mollets, sangle abdominale",
      exos=[
   ("Quadriceps","Squat goblet","3","10-12","90 s","Haltère vertical contre la poitrine. Descends bas, dos droit."),
   ("Quadriceps","Squat bulgare (pied arrière sur le banc)","3","8-10 / jambe","90 s",
    "Le meilleur exercice de jambes disponible sans barre. Un haltère dans chaque main."),
   ("Quadriceps","Fentes avant haltères","3","10 / jambe","75 s","Buste droit, genou arrière proche du sol."),
   ("Mollets","Mollets debout haltères","3","15-20","45 s","Amplitude complète, une seconde de pause en haut."),
   ("Abdos","Crunch haltère sur la poitrine","3","15","45 s","Mouvement court, on enroule le buste."),
   ("Abdos","Gainage planche","3","30-45 s","45 s","Bassin en rétroversion, fessiers serrés."),
   ]),
 dict(id="J3", jour="Jeudi", titre="Haut B — Poussée",
      focus="Pectoraux (la seule fois de la semaine), triceps, deltoïde latéral",
      exos=[
   ("Pectoraux","Développé incliné haltères, PRISE NEUTRE","3","8-10","90 s",
    "Banc à 30°, paumes face à face. Descends jusqu'à ce que le bras arrive au niveau du torse, PAS plus bas."),
   ("Pectoraux","Développé au sol, prise neutre","3","10-12","90 s",
    "Allongé par terre : les coudes touchent le sol et bloquent la descente. L'amplitude dangereuse devient impossible."),
   ("Pectoraux","Pompes au sol, LESTÉES au-delà de 15 reps","3","10-15","75 s",
    "Mains un peu plus larges que les épaules, coudes à 45°. Au-delà de 15 reps propres : sac à dos chargé de 5 puis 10 kg. Va à 1 rep de l'échec, c'est le seul exercice où tu peux."),
   ("Dos","Rowing buste appuyé sur banc incliné","3","12","75 s",
    "Poitrine posée sur le banc à 30°. Équilibre la poussée du jour et ouvre l'espace sous l'acromion."),
   ("Deltoïde latéral","Élévations en scaption, pouces vers le haut","3","12-15","60 s",
    "Monte à 30° vers l'avant, pas sur le côté, pouces au plafond. STOP à hauteur d'épaule. 3 à 5 kg."),
   ("Triceps","Extension couché sur le banc, prise neutre","3","10-12","60 s",
    "Allongé, coudes vers le plafond. Remplace l'extension debout au-dessus de la tête."),
   ]),
 dict(id="J4", jour="Vendredi", titre="Bas B — Chaîne postérieure",
      focus="Ischios, fessiers, mollets, gainage",
      exos=[
   ("Ischios / fessiers","Soulevé de terre roumain haltères","3","10-12","90 s",
    "Jambes quasi tendues, bassin qui recule, dos plat. Tu dois sentir l'arrière des cuisses."),
   ("Ischios / fessiers","Hip thrust haltère sur le banc","3","12-15","75 s",
    "Omoplates sur le banc, haltère sur le bassin, monte jusqu'à l'alignement."),
   ("Ischios / fessiers","Soulevé de terre unilatéral","3","10 / jambe","75 s","Travail d'équilibre en prime. Charge modérée."),
   ("Mollets","Mollets assis haltère sur le genou","3","15-20","45 s","Cible le soléaire, complémentaire du travail debout."),
   ("Abdos","Gainage latéral","3","20-30 s / côté","45 s","Corps aligné, bassin haut."),
   ("Abdos","Relevé de jambes suspendu à la barre","3","10-15","45 s","Genoux ou jambes tendues selon le niveau. Ne te balance pas."),
   ]),
]

ECHAUFFEMENT = [
 ("Cercles de bras","1 min","10 en avant, 10 en arrière, amplitude progressive, sans charge."),
 ("Passages de bras (bâton ou serviette)","1 min","Mains larges, on passe devant/derrière. On s'arrête AVANT la gêne."),
 ("Rotation externe légère","2 x 15","1 à 2 kg. Réveille les rotateurs avant de charger."),
 ("Élévations en Y sur banc incliné","2 x 12","Sans charge ou 1 kg. Active l'omoplate."),
 ("Séries d'approche","2 séries","50 % puis 75 % du poids de travail, sur le 1er exercice seulement."),
]

DOULEUR = [
 ("0 à 3 / 10", False, "Gêne sourde qui ne change pas ton mouvement : tu peux continuer la série."),
 ("Au-dessus de 3 / 10", True, "Arrête la série. Réduis l'amplitude, puis la charge de 20 %. Si ça persiste, passe à l'exercice suivant."),
 ("Douleur vive, en éclair", True, "Stop immédiat sur cet exercice. Ne le refais pas cette semaine."),
 ("Encore douloureux le lendemain", True, "Retire 20 % de charge sur les poussées à la prochaine séance."),
 ("Douleur la nuit, ou qui réveille", True, "Consulte. Ce n'est pas un signal d'entraînement."),
 ("Perte de force inexpliquée", True, "Consulte. Ce n'est pas de la fatigue."),
 ("Douleur qui descend dans le bras", True, "Consulte."),
 ("Rien n'a changé après 2-3 semaines", True, "Consulte un kiné du sport : ce plan ménage l'épaule, il ne la soigne pas."),
]

PROGRESSION = [
 ("La règle", "Double progression : tu montes les répétitions AVANT de monter la charge."),
 ("Poids du corps", "Tractions et pompes suivent la même règle, en trois temps : les répétitions, puis le lestage (sac à dos, 5 puis 10 kg), puis le ralentissement de la descente à 3 secondes. Sans lestage au-delà de 15-20 reps, un exercice au poids du corps cesse de faire grossir."),
 ("Comment", "Reste sur le même poids jusqu'à atteindre le haut de la fourchette sur les 3 séries. Là seulement, tu ajoutes 2 kg par haltère et tu redescends en bas de la fourchette."),
 ("L'intensité", "Arrête chaque série avec 1 ou 2 répétitions encore en réserve. Jamais à l'échec sur les poussées : c'est là que la technique se dégrade et que l'épaule paie."),
 ("En déficit", "Tu manges 250 kcal sous ta dépense : la progression sera plus lente qu'en prise de masse. Une répétition de plus toutes les deux semaines, c'est déjà une victoire."),
 ("Si ça bloque", "Deux séances de suite sans progresser sur un exercice : baisse de 10 % et remonte. Ne force pas."),
 ("Toutes les 6 à 8 semaines", "Une semaine allégée : mêmes exercices, 2 séries au lieu de 3, charges à 70 %. L'épaule apprécie."),
]
