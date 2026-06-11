## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

#### Fonctionnement

Le déploiement est automatisé grâce à l'utilisation de Github Actions.
Lorsque l'on push un commit sur le repository, une pipeline CI/CD se lance. Si l'une des étapes de la pipeline échoue, la pipeline s'arrête et le déploiement n'est pas effectué.
Il faut que le commit concerne la branche "master" pour que la pipeline aille jusqu'au déploiement. Sinon, elle s'arrêtera après avoir validé les tests.

#### Etapes de la pipeline

1. test (sur toutes les branches)
    * Lance les tests
    * Lance le linting
    * Vérifie le coverage (>80%)

2. build-and-push-docker (sur branche master)
    * Crée une image docker
    * Push l'image sur Docker Hub

3. deploy (sur branche master)
    * Déploie l'image via Render

Chaque étape attend que la précédente soit validée avant de se lancer. Il est possible de consulter l'ensemble de la pipeline dans le fichier "django.yml".

#### Configuration

- Docker Hub : c'est là où l'image sera stockée. Dans les settings du repo Github, les secrets "DOCKERHUB_USERNAME" et "DOCKERHUB_TOKEN" sont renseignés afin que la pipeline de Github puisse communiquer avec Docker et enregistrer la nouvelle image.

- Render : [Render](https://render.com/) est l'hébergeur de ce projet. Le Web Service qui sert à déployer l'app est lié à l'image Docker ayant le tag "latest". Afin que le déploiement soit automatisé, "RENDER_DEPLOY_HOOK_URL" est ajouté aux secrets du repo Github.

- Fichiers statiques : "collectstatic" est executé lors du build Docker. Les fichiers sont ensuite servis par Whitenoise.

- Base de donnée : les données sont actuellement stockées sur le fichier "oc-lettings-site.sqlite3" qui est présent dans l'image. L'utilisation de la version gratuite du Web Service de Render fait que les modifications de données ne sont pas persistantes après redéploiement du service. Pour les rendre persistantes, il faut passer à une version payante, créer un disque dans le service Render et copier le ficher SQLite dans ce disque persistant.

#### Test image en local

Il est possible de générer une image en local à partir de la racine du projet avec la commande :
```
docker compose up
```

Toujours depuis la racine du projet, on peut récupérer la dernière version de l'image sur Docker Hub avec la commande :
```
docker compose -f compose.prod.yaml up
```
