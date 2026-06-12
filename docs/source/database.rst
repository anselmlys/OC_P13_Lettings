Base de donnée
==============

Cette section décrit la structure de la base de données et les principaux modèles utilisés par l'application.


Type de base de données
-----------------------

L'application utilise actuellement une base de données SQLite.

En environnement local avec Docker, la base peut être montée via un volume Docker afin de conserver les données entre les redémarrages des conteneurs.

En environnement de déploiement gratuit sur Render, la base SQLite est intégrée à l'image Docker. Les données initiales sont donc disponibles au démarrage de l'application.

**Attention :** Avec la version gratuite de Render, les modifications de données ne sont pas persistantes après un redéploiement du service.
Pour une persistance complète, il est recommandé d'utiliser un disque persistant Render.


Modèles de données
------------------

L'application est organisée autour des modèles suivants :

+----------------+------------------------------------------------+
| Modèle         | Description                                    |
+================+================================================+
| Address        | Représente une adresse physique                |
+----------------+------------------------------------------------+
| Letting        | Représente une location associée à une adresse |
+----------------+------------------------------------------------+
| Profile        | Représente le profil d'un utilisateur Django   |
+----------------+------------------------------------------------+
| User           | Modèle utilisateur fourni par Django           |
+----------------+------------------------------------------------+


Modèle Address
--------------

Le modèle Address stocke les informations liées à une adresse.

Champs principaux :

+------------------+----------------------+------------------------------+
| Champ            | Type                 | Description                  |
+==================+======================+==============================+
| number           | PositiveIntegerField | Numéro de rue                |
+------------------+----------------------+------------------------------+
| street           | CharField            | Nom de la rue                |
+------------------+----------------------+------------------------------+
| city             | CharField            | Ville                        |
+------------------+----------------------+------------------------------+
| state            | CharField            | État                         |
+------------------+----------------------+------------------------------+
| zip_code         | PositiveIntegerField | Code postal                  |
+------------------+----------------------+------------------------------+
| country_iso_code | CharField            | Code ISO du pays             |
+------------------+----------------------+------------------------------+


Modèle Letting
--------------

Le modèle Letting représente une location.

Champs principaux :

+------------+---------------+------------------------------------+
| Champ      | Type          | Description                        |
+============+===============+====================================+
| title      | CharField     | Titre de la location               |
+------------+---------------+------------------------------------+
| address    | OneToOneField | Adresse associée à la location     |
+------------+---------------+------------------------------------+

Relation :

* un Letting est associé à une seule Address
* une Address ne peut être associée qu'à un seul Letting


Modèle Profile
--------------

Le modèle Profile représente les informations complémentaires d'un utilisateur.

Champs principaux :

+----------------+---------------+------------------------------------+
| Champ          | Type          | Description                        |
+================+===============+====================================+
| user           | OneToOneField | Utilisateur Django associé         |
+----------------+---------------+------------------------------------+
| favorite_city  | CharField     | Ville favorite de l'utilisateur    |
+----------------+---------------+------------------------------------+

Relation :

* un Profile est associé à un seul User Django
* un User ne possède qu'un seul Profile
