# Objectif

L'objectif est de prédire le prix médian des maisons appartenant à un *block group*

# Premières observations

Il semblerait que le prix de l'immobilier soit lié aux variables suivantes :
 * **Nature environnnante** (montagne, mer, beauté du paysage) : si colline ou plage de qualité accessible rapidement, alors prix de l'immobilier haut
 * Le **salaire médian des blocks voisins** : les blocks voisins semblent exercer une pression sur le block à prédire. Si les voisins ont un salaire médian plus élevé que le salaire du block target, alors l'immobilier du block target est plus haut
 * Le **degré d'isolement du block** par rapport à ses voisins : si ses voisins sont séparés de lui par une barrière quelconque comme une autoroute, une forêt, un fleuve alors ils ont moins d'influence sur lui
 * La **taille moyenne des maisons** : évidemment si les maisons sont grandes, alors le prix des maisons est plus élevé
 * La **densité de ménages dans le block** : variable compliquée à interpréter, toutefois, il semble qu'une densité faible de ménages alors que le block groupe se trouve à distance raisonnable d'un pôle urbain très dense fait monter les prix. Autrement dit, ne pas se marcher dessus, tout en étant proche des zones urbaines denses

