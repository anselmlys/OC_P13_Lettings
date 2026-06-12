Guide d'utilisation
===================


Accéder à l'application
-----------------------

Une fois l'application lancée, le site est accessible à l'adresse suivante :
http://127.0.0.1:8000/

La page d'accueil permet d'accéder aux différentes sections du site.


Consulter les locations
-----------------------

Les locations disponibles peuvent être consultées depuis la page :
http://127.0.0.1:8000/lettings/

Cette page affiche la liste des locations enregistrées dans l'application.

Chaque location possède une page de détail accessible en cliquant sur son titre.


Consulter les profils utilisateurs
----------------------------------

Les profils utilisateurs sont accessibles depuis :
http://127.0.0.1:8000/profiles/

Cette page affiche les profils enregistrés dans l'application.

Chaque profil possède une page dédiée contenant les informations de l'utilisateur.


Interface d'administration
--------------------------

L'interface d'administration Django est accessible à l'adresse :
http://127.0.0.1:8000/admin/

Cette interface permet de gérer les données de l'application.

L'accès à l'interface admin nécessite un compte administrateur Django.
Il est possible de se connecter avec l'utilisateur admin, mot de passe Abc1234!


Cas d'utilisation
-----------------

1. Consultation des location:
    * Accéder à la page d'accueil
    * Ouvrir la section "Lettings"
    * Séléctionner une location
    * Consulter les informations détaillées

2. Consultation d'un profil:
    * Accéder à la page d'accueil
    * Ouvrir la section "Profiles"
    * Séléctionner un utilisateur
    * Consulter les informations détaillées

3. Administration des données:
    * Se connecter à l'interface admin de Django
    * Séléctionner un modèle
    * Ajouter, modifier ou supprimer des données
    * Sauvegarder les modifications
