# -*- coding: utf-8 -*-
"""Explications détaillées de chaque exercice, derrière le bouton « i » de l'appli.
Clé : le nom exact de l'exercice dans prog.py. Valeur : liste de (titre, texte).
Quatre rubriques par exercice : à quoi ça sert, comment le faire, le piège, la progression."""

A, C, P, G = "À quoi ça sert", "Comment", "Le piège", "Progression"

INFOS = {

# ---------------- J1 · Lundi · tirage ----------------
"Tractions, prise supination ou neutre": [
 (A, "L'exercice roi du dos : le grand dorsal (la largeur), le biceps, et surtout le geste qui protège l'épaule quand il est bien fait. Tant que le pli du coude est sensible, prise neutre uniquement : elle ménage le tendon du biceps."),
 (C, "Mains à largeur d'épaules, jamais plus large. Pendu à la barre, commence par abaisser les épaules et ranger les omoplates, sans plier les coudes : c'est le premier centimètre qui compte. Ensuite tire les coudes vers les hanches, poitrine vers la barre, menton neutre. Redescends en 2 à 3 secondes, et arrête-toi juste avant que les coudes soient verrouillés."),
 (P, "Se balancer, tendre le cou vers la barre, se laisser tomber en bas épaules aux oreilles, prendre large. En bas, c'est le moment où l'épaule et le tendon du biceps prennent le coup : garde les coudes très légèrement fléchis."),
 (G, "Moins de 5 reps : des négatives de 5 secondes (tu montes avec le banc, tu descends seul). Au-delà de 12 à 15 reps propres : sac à dos lesté, 5 puis 10 kg, à noter dans la case « lest ». Tant que le coude parle, tu t'arrêtes 2 reps avant l'échec et tu ne lestes pas."),
],
"Rowing haltères buste penché": [
 (A, "L'épaisseur du dos : rhomboïdes, milieu des trapèzes, grand dorsal. C'est l'exercice qui redresse un haut du dos voûté et qui équilibre toutes les poussées de la semaine."),
 (C, "Pieds largeur de hanches, genoux souples, tu bascules le buste à 45° en reculant les fesses, dos plat, tête dans l'axe. Les haltères pendent bras tendus. Tire les coudes vers l'arrière, près du corps, jusqu'à amener les haltères vers le nombril ou les hanches, serre les omoplates une seconde, redescends en 2 à 3 secondes."),
 (P, "Le buste qui rebondit à chaque rep, le bas du dos qui s'arrondit, les coudes qui partent sur les côtés (l'épaule n'aime pas), et l'à-coup au départ quand l'haltère pend bras tendu : démarre en douceur, c'est ça qui tire sur le tendon du biceps."),
 (G, "Quand tu fais 10 reps sur les 3 séries, +2 kg par haltère et tu repars à 8."),
],
"Rowing unilatéral, appui sur le banc": [
 (A, "Le grand dorsal en amplitude complète, un côté à la fois : ça corrige le déséquilibre entre ton côté douloureux et l'autre, et le banc protège le bas du dos."),
 (C, "Genou et main du même côté sur le banc, l'autre pied au sol, dos plat parallèle au sol. L'haltère pend, laisse l'omoplate s'étirer vers l'avant en bas. Tire le coude vers la hanche, l'haltère finit contre le bas des côtes, serre une seconde, redescends lentement jusqu'à l'étirement complet."),
 (P, "Tourner le buste pour soulever plus lourd, le coude qui s'écarte, la traction sèche depuis le bras tendu. Le buste reste carré, face au sol."),
 (G, "12 reps propres sur les 3 séries, puis +2 kg et retour à 10. Commence toujours par le côté le plus faible."),
],
"Oiseau sur banc incliné": [
 (A, "Le deltoïde postérieur, le muscle qui tire l'épaule vers l'arrière. Chez quelqu'un qui a les épaules enroulées, il est faible, et c'est une des clés d'une épaule qui va mieux."),
 (C, "Poitrine posée sur le banc à 30°, les haltères pendent sous les épaules, coudes très légèrement fléchis et figés. Écarte les bras sur les côtés jusqu'à hauteur d'épaule, petits doigts légèrement plus hauts que les pouces, serre une seconde, redescends en 3 secondes. 3 à 5 kg, pas plus."),
 (P, "Prendre lourd : les trapèzes et l'élan font le travail à la place du deltoïde. Hausser les épaules. Plier les coudes en montant."),
 (G, "15 reps parfaites sur 3 séries, puis +1 kg. La lenteur vaut plus que les kilos ici."),
],
"Élévations en Y sur banc incliné": [
 (A, "Le bas du trapèze, le muscle qui fait tourner l'omoplate vers le haut quand le bras monte. Il dort chez presque tout le monde qui a un conflit sous-acromial ; le réveiller, c'est permettre au bras de monter sans pincer."),
 (C, "Poitrine sur le banc à 30°, bras pendants, pouces vers le plafond. Monte les bras tendus en Y, à 30° de l'axe de la tête, jusqu'à hauteur d'épaule, tiens une seconde, redescends lentement. 2 à 4 kg, ou à vide au début."),
 (P, "Hausser les épaules vers les oreilles (le haut du trapèze prend le relais, à l'opposé du but), cambrer, prendre trop lourd. Si tu ne sens pas entre les omoplates, allège."),
 (G, "+1 kg uniquement quand les 3 × 12 sont propres sans aucun haussement d'épaule."),
],
"Curl marteau": [
 (A, "Le biceps, le brachial et le long supinateur : le volume du bras. La prise neutre charge moins le tendon du biceps au coude que la supination, c'est pour ça qu'elle est là."),
 (C, "Debout, coudes collés au corps, paumes face à face. Monte en 2 secondes, serre en haut, redescends en 3 secondes sans jamais lâcher le poids en bas. Tant que le pli du coude est sensible, garde une légère flexion en bas : le coude ne se verrouille pas."),
 (P, "Balancer le buste, les coudes qui avancent, le poids qui tombe en fin de descente. C'est précisément le lâcher en bas qui irrite le tendon."),
 (G, "12 reps sur les 3 séries, puis +1 kg par haltère. Tant que le coude parle : même charge, et la troisième série remplacée par une tenue de 45 secondes coude à 90°."),
],

# ---------------- J2 · Mardi · quadriceps ----------------
"Squat goblet": [
 (A, "La base de la séance jambes : quadriceps, fessiers, et le haut du dos qui tient la charge. Il t'apprend à descendre bas avec le dos droit."),
 (C, "Prends l'haltère posé debout sur le banc, en descendant en squat devant lui, jamais en le soulevant avec les bras. Vertical contre le sternum, coudes rentrés dessous. Pieds largeur d'épaules, pointes un peu ouvertes. Assieds-toi entre les genoux, coudes à l'intérieur des cuisses en bas, poitrine haute, et remonte en poussant dans tout le pied. 2 secondes pour descendre."),
 (P, "Les talons qui décollent, les genoux qui rentrent, le dos qui s'arrondit en bas. Et monter l'haltère à la poitrine par un curl : c'est ce qui tire sur le tendon du biceps."),
 (G, "12 reps sur 3 séries, puis +2 kg. Si tenir l'haltère réveille le pli du coude, passe en sumo : haltère tenu bras tendus entre les cuisses."),
],
"Squat bulgare (pied arrière sur le banc)": [
 (A, "Le meilleur exercice de jambes sans barre : quadriceps et fessiers une jambe à la fois, avec une charge énorme par jambe pour des haltères légers, plus l'équilibre et la stabilité de la hanche."),
 (C, "Pied arrière sur le banc, lacets vers le bas. Le pied avant assez loin pour que le genou reste au-dessus du pied en bas. Haltères le long du corps. Descends à la verticale jusqu'à ce que le genou arrière frôle le sol, buste légèrement penché en avant, et remonte en poussant dans le talon avant."),
 (P, "Le pied avant trop près (le talon décolle, le genou file devant), rebondir sur la jambe arrière, le buste qui s'effondre. La jambe arrière ne pousse pas, elle équilibre."),
 (G, "10 reps par jambe sur 3 séries, puis +2 kg par haltère. Commence par la jambe la plus faible."),
],
"Fentes avant haltères": [
 (A, "Quadriceps et fessiers en mouvement, et le freinage du pas qui protège le genou. Elles complètent le bulgare avec un geste dynamique."),
 (C, "Haltères le long du corps, grand pas en avant, descends à la verticale jusqu'à ce que le genou arrière frôle le sol, tibia avant vertical, puis repousse dans le talon avant pour revenir debout. Buste droit, regard devant."),
 (P, "Le pas trop court (le genou dépasse loin le pied), le buste qui bascule, les vacillements : ralentis plutôt que d'alourdir."),
 (G, "10 reps par jambe sur 3 séries, puis +2 kg. Si tu manques de temps, c'est l'exercice à sauter après le bulgare : ils travaillent la même chose."),
],
"Mollets debout haltères": [
 (A, "Les jumeaux, le gros muscle visible du mollet. Les mollets répondent aux séries longues, à l'amplitude complète et à la pause en haut, pas aux à-coups."),
 (C, "Avant-pied sur une marche ou un disque, un haltère dans la main du côté qui travaille, l'autre main au mur pour l'équilibre. Descends le talon jusqu'à l'étirement, monte sur la pointe le plus haut possible, une seconde de pause en haut, 2 secondes pour redescendre."),
 (P, "Rebondir en bas, faire des demi-amplitudes, aller vite."),
 (G, "20 reps sur 3 séries, puis +2 kg. Ensuite, une jambe à la fois."),
],
"Crunch haltère sur la poitrine": [
 (A, "Le grand droit sous charge : les abdos grossissent comme les autres muscles, à condition d'être chargés. Le mouvement court protège le bas du dos."),
 (C, "Allongé, genoux pliés, l'haltère tenu contre la poitrine. Enroule les côtes vers le bassin jusqu'à décoller les omoplates, tiens une seconde, redescends lentement. Menton décollé de la poitrine, souffle en montant."),
 (P, "Tirer sur la nuque, monter jusqu'à s'asseoir (ce sont les fléchisseurs de hanche qui travaillent), bloquer la respiration."),
 (G, "15 reps sur 3 séries, puis +2 kg ou un tempo plus lent."),
],
"Gainage planche": [
 (A, "Les abdos dans leur vrai rôle, la stabilité : c'est ce qui tient le bas du dos sur les squats et les soulevés de terre. Et ça t'apprend la rétroversion du bassin."),
 (C, "Sur les avant-bras, coudes sous les épaules, pieds joints. Serre les fessiers, bascule le bassin (le pubis vers le nombril), pousse le sol avec les avant-bras pour arrondir légèrement le haut du dos, et respire."),
 (P, "Les hanches qui descendent ou qui montent, la tête qui pend, l'apnée. Une planche de 30 secondes parfaite vaut mieux qu'une minute bancale."),
 (G, "30 puis 45 secondes. Ensuite un pied décollé, ou un disque sur le dos."),
],

# ---------------- R · Mercredi · rééducation ----------------
"Rentrés de menton": [
 (A, "Les fléchisseurs profonds du cou sont faibles, et la tête part en avant : c'est l'exercice qui la remet sur les épaules, et qui soulage le haut du trapèze qui travaille à sa place toute la journée."),
 (C, "Debout dos au mur, l'arrière de la tête contre le mur, ou allongé sur le dos. Fais glisser le menton vers l'arrière, comme pour faire un double menton, sans lever ni baisser la tête. Tu dois sentir un étirement à la base du crâne et un travail devant le cou. Tiens 5 secondes, relâche lentement."),
 (P, "Baisser la tête au lieu de la reculer, serrer les mâchoires, forcer. C'est un geste petit et précis."),
 (G, "5 puis 10 secondes de tenue, ensuite une légère résistance de deux doigts sur le front. À refaire dans la journée, au bureau, autant de fois que tu y penses."),
],
"Extension du haut du dos sur le banc": [
 (A, "Un haut du dos raide et voûté oblige le cou et l'épaule à compenser. Redonner de la mobilité entre les omoplates, c'est laisser à l'épaule la place de monter le bras sans pincer."),
 (C, "Allongé en travers du banc, le bord juste sous les omoplates, pieds au sol, mains derrière la tête pour soutenir la nuque. Laisse le haut du dos s'ouvrir en arrière par-dessus le bord pendant 3 secondes en soufflant, puis reviens. Tout se passe entre les omoplates."),
 (P, "Cambrer le bas du dos à la place du haut (garde les fessiers serrés), tirer sur la nuque, aller chercher l'amplitude en force."),
 (G, "Pas de progression : c'est de l'entretien. Tu peux déplacer le bord du banc un peu plus haut ou plus bas dans le dos pour mobiliser d'autres étages."),
],
"Étirement du trapèze supérieur": [
 (A, "Avec la tête en avant, le haut du trapèze travaille en permanence et tire l'épaule vers l'oreille. L'étirer fait redescendre l'épaule et détend la nuque."),
 (C, "Assis ou debout, une main posée sur la tête, tu inclines l'oreille vers l'épaule opposée, l'autre bras tendu vers le sol (ou la main coincée sous la cuisse). 30 secondes, en respirant, tout en douceur."),
 (P, "Tirer avec la main : elle ne fait que peser, elle ne tracte pas. Tourner la tête. Hausser l'épaule qu'on étire."),
 (G, "Pas de progression : entretien. Regarder légèrement vers l'aisselle déplace l'étirement sur l'élévateur de l'omoplate, l'autre muscle qui tire sur le cou."),
],
"Rotation externe couchée sur le côté": [
 (A, "L'infra-épineux et le petit rond, les muscles qui retiennent la tête de l'humérus au centre et vers l'arrière. C'est le cœur du recentrage, et ils sont faibles dans presque tous les conflits sous-acromiaux."),
 (C, "Allongé sur le côté, le bras à travailler au-dessus, coude plié à 90° et collé au flanc, une serviette roulée entre le coude et les côtes. Haltère de 1 à 2 kg. L'avant-bras part du ventre et tourne vers le plafond, tu t'arrêtes juste avant la verticale, une seconde de tenue, et tu redescends en 3 secondes."),
 (P, "Le coude qui décolle du flanc, aller au-delà de la verticale, basculer le corps en arrière pour aider, prendre trop lourd. Rien ne bouge à part l'avant-bras."),
 (G, "+1 kg quand tu tiens 3 × 15 propres, jusqu'à 3 kg. L'appli te le propose. Ensuite, plus lent plutôt que plus lourd."),
],
"Rotation interne à l'élastique": [
 (A, "Le sous-scapulaire, le muscle de la coiffe qui est devant l'épaule : le jumeau de la rotation externe, dans l'autre sens. Il faut les deux pour que la tête de l'humérus reste centrée."),
 (C, "Élastique accroché à hauteur de coude, tu te mets de profil, l'épaule à travailler côté accroche. Coude plié à 90° et collé au flanc (serviette coincée si besoin), l'avant-bras pointe vers l'accroche. Amène l'avant-bras devant le ventre comme une porte qui se ferme, 2 secondes, puis reviens en freinant, 3 secondes, jusqu'à ce que l'avant-bras pointe droit devant toi, pas plus loin."),
 (P, "Ouvrir trop loin vers l'extérieur au retour : le coude décolle et l'épaule roule vers l'avant. L'élastique mou en position de départ : recule d'un pas au lieu d'ouvrir plus."),
 (G, "Éloigne-toi de l'accroche, puis élastique plus épais. Note le niveau dans la case « élast. »."),
],
"Abaissement à l'élastique": [
 (A, "Pour ton épaule, le plus important des onze. Le conflit, c'est une tête d'humérus qui remonte et coince le tendon sous l'acromion. Le grand dorsal et le bas du trapèze la tirent vers le bas : c'est eux qu'on renforce ici, et c'est le geste que les tractions ne t'apprennent pas."),
 (C, "Élastique en haut, à la barre de traction. Face à l'accroche, un pas en arrière, bras tendu devant toi à hauteur d'épaule, coude déverrouillé mais figé. Pousse la main vers le bas et l'arrière, bras tendu, jusqu'à côté de la cuisse et un peu derrière. Tiens 5 secondes en bas, laisse remonter lentement. Pendant que la main descend, l'omoplate descend et se rapproche de la colonne : tu la ranges dans la poche arrière du short."),
 (P, "L'épaule qui remonte vers l'oreille, au départ ou pendant la tenue : c'est l'inverse de ce qu'on cherche. Se pencher en arrière pour tricher. Si ça pince bras haut, commence avec le bras à 45° et remonte le point de départ au fil des semaines."),
 (G, "Recule d'un pas, puis élastique plus épais ; note le niveau dans « élast. ». Et reproduis ce geste au début de chaque traction : épaules abaissées avant de plier les coudes."),
],
"Isométriques contre le mur": [
 (A, "Une contraction sans mouvement calme la douleur du tendon pendant plusieurs heures et charge la coiffe sans aucun risque. C'est le seul exercice faisable tous les jours, et le bon réflexe quand l'épaule est grognon."),
 (C, "Debout à côté d'un mur, coude à 90° collé au corps, avant-bras horizontal. Dos de la main contre le mur : pousse vers l'extérieur pendant 10 secondes. Tourne-toi, paume contre le mur : pousse vers l'intérieur 10 secondes. À 30-40 % de ta force, rien ne bouge, et tu respires."),
 (P, "Hausser l'épaule, le coude qui décolle, l'apnée, pousser trop fort. C'est une pression tranquille et continue."),
 (G, "De 30-40 % à 50-60 % de ta force, puis 15 secondes. Note les secondes dans la case « s »."),
],
"Anges au mur": [
 (A, "La mobilité et le contrôle de l'omoplate quand le bras monte, avec le haut du dos ouvert. C'est aussi le test qui te montre exactement où ton épaule est bloquée."),
 (C, "Dos au mur, pieds à 10-15 cm, le bas du dos proche du mur, l'arrière de la tête en contact. Coudes et poignets contre le mur en W. Fais glisser les bras vers le haut en Y en gardant tous les contacts, puis redescends. Lentement, 3 secondes dans chaque sens."),
 (P, "Cambrer pour garder le contact (réduis l'amplitude), hausser les épaules, les poignets qui décollent. Arrête-toi avant le pincement, pas après."),
 (G, "L'amplitude : les bras montent un peu plus haut chaque semaine en gardant le contact, jusqu'au Y complet."),
],
"Face pull à l'élastique": [
 (A, "Le deltoïde postérieur, les rotateurs externes et le milieu du dos en un seul geste : l'anti-épaules-enroulées. Il équilibre toutes les poussées."),
 (C, "Élastique à hauteur du visage, une extrémité dans chaque main, recule pour le tendre. Tire vers le front, coudes hauts et écartés. À la fin, les mains arrivent de chaque côté des oreilles, ce qui fait tourner les épaules vers l'extérieur ; serre les omoplates une seconde, reviens lentement."),
 (P, "Les coudes qui descendent (ça devient un rowing), hausser les épaules, se pencher en arrière, un élastique trop dur qui casse la technique."),
 (G, "Recule d'un pas, puis élastique plus épais ; note le niveau dans « élast. »."),
],
"Pompes au mur avec poussée finale": [
 (A, "Le dentelé antérieur, le muscle qui plaque l'omoplate contre les côtes et la fait tourner quand le bras monte. S'il dort, l'omoplate décolle et l'épaule pince : la poussée finale, c'est lui, et lui seul."),
 (C, "Mains sur le mur à hauteur d'épaule, bras tendus, corps droit. Plie les coudes pour amener la poitrine vers le mur, repousse jusqu'aux bras tendus, et là, pousse encore : les omoplates s'écartent, le haut du dos s'arrondit un peu. Tiens une seconde, reviens."),
 (P, "Hausser les épaules pendant la poussée finale, cambrer, les coudes écartés. Le mouvement de fin est petit, quelques centimètres."),
 (G, "Les mains de plus en plus bas : mur, puis bord du banc, puis sol."),
],
"Étirement du pectoral à la porte": [
 (A, "Des pectoraux raccourcis tirent l'épaule vers l'avant et ferment l'espace sous l'acromion. Les étirer, c'est laisser les muscles du dos faire leur travail de recentrage."),
 (C, "Avant-bras contre le montant de la porte, coude à hauteur d'épaule ou un peu plus bas. Avance doucement le pied du même côté et laisse le buste passer devant, jusqu'à sentir l'étirement devant l'épaule et sur le pectoral. 30 secondes, en respirant, l'épaule basse et en arrière."),
 (P, "Le coude au-dessus de l'épaule (ça pince), tourner le buste, forcer. C'est l'épaule qui commande l'intensité, pas le pectoral."),
 (G, "Pas de progression : entretien. Tu peux varier la hauteur du coude d'une série à l'autre, toujours sous la hauteur de l'épaule."),
],

# ---------------- J3 · Jeudi · poussée ----------------
"Développé incliné haltères, PRISE NEUTRE": [
 (A, "Le constructeur des pectoraux de la semaine. L'inclinaison et la prise neutre mettent l'épaule dans sa position la plus sûre : coudes à 30-45° du corps, sans rotation interne."),
 (C, "Banc à 30°, paumes face à face. Avant la première rep, tire les omoplates en arrière et vers le bas, et garde-les là toute la série. Descends en 2 à 3 secondes jusqu'à ce que le bras arrive au niveau du torse, pas plus bas, et pousse vers le haut et légèrement vers l'intérieur sans cogner les haltères."),
 (P, "Descendre trop bas (c'est l'épaule qui paie), les épaules qui roulent vers l'avant en haut, les coudes à 90° du corps, rebondir en bas."),
 (G, "10 reps sur 3 séries, puis +2 kg par haltère et retour à 8. Toujours 1 ou 2 reps en réserve : jamais à l'échec sur une poussée."),
],
"Développé au sol, prise neutre": [
 (A, "Le sol bloque la descente exactement là où l'épaule est en sécurité. Pectoraux, et surtout triceps : la fin de poussée."),
 (C, "Allongé au sol, genoux pliés, haltères paumes face à face, omoplates serrées. Descends lentement jusqu'à ce que l'arrière des bras touche le sol, marque une seconde sans relâcher, et pousse."),
 (P, "Laisser tomber les coudes au sol pour rebondir, cambrer, les coudes écartés."),
 (G, "12 reps sur 3 séries, puis +2 kg par haltère."),
],
"Pompes au sol, LESTÉES au-delà de 15 reps": [
 (A, "La poussée où l'omoplate bouge librement, contrairement au banc : parfait pour le dentelé et l'épaule. Le seul exercice où tu peux aller près de l'échec."),
 (C, "Mains un peu plus larges que les épaules, doigts vers l'avant, corps rigide, fessiers serrés, coudes à 45°. La poitrine vient frôler le sol en 2 secondes, tu pousses, et tu finis en écartant les omoplates, comme sur les pompes au mur."),
 (P, "Les hanches qui tombent, la tête qui pend, les coudes à 90°, les demi-amplitudes."),
 (G, "Au-delà de 15 reps propres : sac à dos de 5 puis 10 kg, à noter dans « lest ». Ensuite, la descente en 3 secondes."),
],
"Rowing buste appuyé sur banc incliné": [
 (A, "Du tirage un jour de poussée, pour que l'épaule finisse la séance équilibrée. La poitrine appuyée, il n'y a ni bas du dos ni triche possible, et le geste ouvre l'espace sous l'acromion."),
 (C, "Poitrine sur le banc à 30°, pieds au sol, haltères pendants. Tire les coudes vers l'arrière et vers les hanches, à 45° du corps, serre les omoplates une seconde, redescends lentement jusqu'à l'étirement complet sans laisser les épaules partir vers l'avant."),
 (P, "Les coudes à 90° (l'épaule), hausser les épaules, l'à-coup au départ bras tendu (le tendon du biceps), décoller la poitrine du banc."),
 (G, "12 reps propres sur 3 séries, puis +2 kg."),
],
"Élévations en scaption, pouces vers le haut": [
 (A, "Le deltoïde latéral sans le pincement : 30° vers l'avant (le plan de l'omoplate) et les pouces en l'air ouvrent l'espace sous l'acromion. C'est la version sûre de l'élévation latérale."),
 (C, "Debout, haltères de 3 à 5 kg, bras à 30° devant le corps, pouces vers le plafond, coudes très légèrement fléchis et figés. Monte jusqu'à hauteur d'épaule, jamais plus haut, une seconde, redescends en 3 secondes."),
 (P, "Dépasser la hauteur d'épaule, hausser les épaules, prendre de l'élan avec le buste, laisser les pouces se tourner vers le bas."),
 (G, "15 reps sur 3 séries, puis +1 kg. Lent avant lourd."),
],
"Extension couché sur le banc, prise neutre": [
 (A, "Le triceps, et surtout sa longue portion, isolé. Allongé, coudes vers le plafond, tu remplaces l'extension au-dessus de la tête qui irrite l'épaule."),
 (C, "Allongé sur le banc, haltères au-dessus de la poitrine, paumes face à face. Les bras restent verticaux, coudes pointés au plafond ; plie les coudes pour amener les haltères de chaque côté du front en 2 à 3 secondes, puis tends. Le bras ne bouge pas, seul l'avant-bras travaille."),
 (P, "Les coudes qui s'écartent, les bras qui basculent vers l'arrière, laisser tomber le poids (c'est le coude qui encaisse)."),
 (G, "12 reps sur 3 séries, puis +1 kg par haltère. Reste léger : c'est un exercice de coude."),
],

# ---------------- J4 · Vendredi · chaîne postérieure ----------------
"Soulevé de terre roumain haltères": [
 (A, "Les ischios et les fessiers en étirement, et surtout le geste de la hanche qui bascule, celui qui protège le bas du dos pour la vie."),
 (C, "Haltères devant les cuisses, bras tendus, genoux légèrement fléchis et figés. Recule les fesses, dos plat, les haltères glissent le long des cuisses jusqu'à mi-tibia ou jusqu'à ce que l'arrière des cuisses tire fort, 3 secondes. Tu remontes en poussant les hanches vers l'avant, fessiers serrés en haut, sans te pencher en arrière."),
 (P, "Plier les genoux (ça devient un squat), arrondir le dos, descendre plus bas que ta souplesse. Et plier les coudes pour aider les haltères : les bras restent parfaitement tendus, c'est le mécanisme classique de blessure du tendon du biceps."),
 (G, "12 reps sur 3 séries, puis +2 kg par haltère."),
],
"Hip thrust haltère sur le banc": [
 (A, "L'exercice des fessiers, le muscle le plus puissant du corps, avec la contraction maximale en haut. Sprint, squat, posture, tout part de là."),
 (C, "Haut du dos sur le bord du banc, pieds à plat largeur de hanches, genoux à 90° en haut, l'haltère sur le bassin avec une serviette dessous. Menton rentré, côtes basses. Pousse dans les talons jusqu'à l'alignement cuisses-buste, serre les fessiers 2 secondes, redescends en contrôle."),
 (P, "Cambrer en haut (rentre le menton, baisse les côtes), les pieds trop loin (ce sont les ischios) ou trop près (les quadriceps), les demi-amplitudes."),
 (G, "15 reps sur 3 séries, puis +2 à 4 kg. Ensuite 3 secondes de tenue en haut, puis une jambe à la fois."),
],
"Soulevé de terre unilatéral": [
 (A, "Ischios et fessiers avec l'équilibre et la stabilité de la hanche en prime, un côté à la fois. Léger mais exigeant."),
 (C, "Haltère dans la main opposée à la jambe d'appui, genou souple. Bascule le buste vers l'avant pendant que la jambe arrière s'étend derrière, hanches bien face au sol (les orteils du pied arrière pointent vers le sol), dos plat, l'haltère descend vers le sol. Remonte en serrant le fessier de la jambe d'appui."),
 (P, "La hanche qui s'ouvre, le dos qui s'arrondit, la précipitation. Fixe un point au sol devant toi."),
 (G, "10 reps par jambe sur 3 séries, puis +2 kg. Au début, une main au banc si l'équilibre lâche."),
],
"Mollets assis haltère sur le genou": [
 (A, "Genou plié, c'est le soléaire qui travaille, le muscle profond qui fait l'épaisseur du bas du mollet. Il complète le travail debout."),
 (C, "Assis sur le banc, avant-pieds sur une marche ou un disque, l'haltère posé sur le genou avec une serviette. Descends le talon jusqu'à l'étirement, monte le plus haut possible, une seconde de pause, 2 secondes pour redescendre."),
 (P, "Rebondir, réduire l'amplitude quand ça brûle."),
 (G, "20 reps sur 3 séries, puis +2 kg."),
],
"Gainage latéral": [
 (A, "Les obliques et le fessier moyen, les muscles qui empêchent le buste et le bassin de basculer sur le côté. C'est ce qui tient sur tout le travail à une jambe."),
 (C, "Coude sous l'épaule, pieds l'un sur l'autre ou le pied du dessus devant. Monte les hanches jusqu'à ce que le corps soit une ligne droite, pousse le sol avec l'avant-bras, hanches vers l'avant, et respire."),
 (P, "Les hanches qui descendent, le buste qui tourne vers l'avant, la tête qui pend."),
 (G, "20 puis 30 secondes par côté. Ensuite la jambe du dessus levée, puis les pieds sur le banc."),
],
"Relevé de jambes suspendu à la barre": [
 (A, "Le bas des abdos et les fléchisseurs de hanche, avec les côtes tirées vers le bas. Pendu à la barre, tu décomprimes aussi la colonne et tu travailles la poigne."),
 (C, "Suspendu, épaules abaissées et actives (jamais pendu épaules aux oreilles, même geste que l'abaissement à l'élastique). Monte les genoux vers la poitrine en basculant le bassin, le bas du dos s'arrondit, une seconde en haut, redescends lentement sans te balancer. Jambes tendues quand les genoux sont devenus faciles."),
 (P, "Se balancer, cambrer, prendre de l'élan, rester pendu passif. Si le pli du coude tire, garde les coudes très légèrement fléchis."),
 (G, "15 reps genoux pliés, puis jambes tendues, puis la descente en 3 secondes."),
],
}
