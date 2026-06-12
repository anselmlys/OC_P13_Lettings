Déploiement et gestion de l'application
=======================================


Architecture de déploiement
---------------------------

Le déploiement de l'application repose sur les technologies suivantes :

* Docker
* Docker Hub
* GitHub Actions
* Render
* Gunicorn
* WhiteNoise

Lorsqu'un commit est réalisé sur le repository Github, la pipeline CI/CD se lance.
C'est cette pipeline qui est responsable des vérifications et du déploiement de l'application.

Pipeline CI/CD
--------------

La pipeline CI/CD est définie dans le fichier :

.. code-block:: text
    .github/workflows/django.yml

Le workflow contient trois jobs principaux :

1. test
    * exécution des tests Pytest
    * exécution du linting avec Flake8
    * vérification du coverage supérieur à 80 %
2. build-and-push-docker
    * création de l'image Docker
    * génération du tag latest
    * génération d'un tag basé sur le hash du commit
    * push de l'image sur Docker Hub
3. deploy
    * déclenchement du déploiement Render via un Deploy Hook

Seule la branche "master" déclenche l'ensemble des jobs. Les autres branches s'arrêtent après avoir effectuées les tests.


Monitoring et gestion des erreurs
---------------------------------

L'application utilise Sentry pour le monitoring des erreurs.

Les erreurs serveur et exceptions sont automatiquement remontées vers Sentry afin de faciliter :
* le débogage
* le monitoring
* l'analyse des erreurs de production
