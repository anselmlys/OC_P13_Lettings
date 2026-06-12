Interfaces de programmation
===========================

Cette section décrit les principales interfaces de communication utilisées par l'application Django.


Architecture générale
---------------------

L'application utilise le framework Django et suit une architecture de type MVT (Model - View - Template).

Les requêtes HTTP sont envoyées par le navigateur vers les routes Django configurées dans le projet.
Les vues récupèrent ensuite les données nécessaires depuis les modèles Django avant de générer une réponse HTML via les templates.


Routes principales
------------------

L'application expose les routes suivantes :

+--------------------------------+---------------------------------------------+
| URL                            | Description                                 |
+================================+=============================================+
| /                              | Page d'accueil                              |
+--------------------------------+---------------------------------------------+
| /lettings/                     | Liste des locations                         |
+--------------------------------+---------------------------------------------+
| /lettings/<id>/                | Détail d'une location                       |
+--------------------------------+---------------------------------------------+
| /profiles/                     | Liste des profils utilisateurs              |
+--------------------------------+---------------------------------------------+
| /profiles/<username>/          | Détail d'un profil utilisateur              |
+--------------------------------+---------------------------------------------+
| /admin/                        | Interface d'administration Django           |
+--------------------------------+---------------------------------------------+


Interface d'administration
--------------------------

L'application utilise l'interface d'administration fournie par Django.

Cette interface permet :

* de créer des objets
* de modifier les données
* de supprimer des objets
* de gérer les utilisateurs

L'accès à l'interface admin nécessite un compte administrateur Django.
Il est possible de se connecter avec l'utilisateur admin, mot de passe Abc1234!
