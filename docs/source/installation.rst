Guide d'installation
====================


Prérequis
---------
* Python 3.8
* Git CLI
* SQLite3 CLI
* Compte Github avec accès en lecture à ce repository
* Accès au compte Docker
* Accès au Web Service Render
* (Optionnel) Accès au compte Sentry


Étapes d'installation
---------------------

1. Clôner le repository
.. code-block:: bash
    git clone https://github.com/anselmlys/OC_P13_Lettings.git
    cd OC_P13_Lettings

2. Créer l'environnement virtuel
.. code-block:: bash
    python -m venv venv
    source venv/bin/activate

3. Installation des dépendances
.. code-block:: bash
    pip install -r requirements.txt


Variables d'environnement
-------------------------
Un fichier .env est nécessaire pour définir des variables d'environnement spécifiques :

+----------------+-----------------------------------------------+
| Variable       | Description                                   |
+================+===============================================+
| SECRET_KEY     | Clé secrète Django                            |
+----------------+-----------------------------------------------+
| DEBUG          | Mode debug de Django (True/False)             |
+----------------+-----------------------------------------------+
| ALLOWED_HOSTS  | Nom de domaine que le site Django peut servir |
+----------------+-----------------------------------------------+
| DATABASE_NAME  | Chemin vers la base de donnée                 |
+----------------+-----------------------------------------------+
| SENTRY_DSN     | Lien de connexion vers Sentry                 |
+----------------+-----------------------------------------------+
