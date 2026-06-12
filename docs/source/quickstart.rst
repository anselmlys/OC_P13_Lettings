Démarrage rapide
================

Prérequis
---------

Les outils suivants doivent être installés sur la machine :

* Git
* Docker Desktop


Cloner le repository
--------------------

``git clone https://github.com/anselmlys/OC_P13_Lettings.git
cd OC_P13_Lettings``


Créer le fichier d'environnement
--------------------------------

Créer un fichier .env à la racine du projet :

    ``SECRET_KEY=your-secret-key
    DEBUG=True
    SENTRY_DSN=
    ALLOWED_HOSTS=127.0.0.1,localhost
    DATABASE_NAME=/app/data/db.sqlite3``


Lancer l'application avec Docker
--------------------------------

Depuis la racine du projet, exécuter :

``docker compose up --build``

Le site sera ensuite accessible à l'adresse suivante :
http://127.0.0.1:8000/


Lancer l'image Docker Hub
-------------------------

Il est également possible de lancer directement l'image Docker Hub :

``docker compose -f compose.prod.yaml up``


Arrêter l'application
---------------------

Pour arrêter les conteneurs Docker :

``docker compose down``
