# Ewallet

## What is it?

Ewallet est une application de portefeuille électronique qui permet aux utilisateurs de gérer leurs comptes et leurs finances en ligne. Elle offre des fonctionnalités telles que la gestion des comptes, les transactions financières, et bien plus encore.

## Features

- Authentification de l'utilisateur
- Création d'un portefeuille
- Ajout de valeurs au portefeuille
- Suivi des valeurs

## How to Build

Pour construire l'application, suivez les étapes ci-dessous :

1. Clonez le repository :
   ```
   git clone https://github.com/votre-utilisateur/ewallet.git
   cd ewallet

## How to Test

Pour exécuter les tests unitaires, utilisez la commande suivante :
   
    python ewallet/manage.py makemigrations
    python ewallet/manage.py migrate
    python ewallet/manage.py test accounts
    python ewallet/manage.py test finance

## How to Run Locally
Pour exécuter l'application localement, suivez les étapes ci-dessous :

1. Assurez-vous que toutes les dépendances sont installées (voir la section "How to Build").

2. Configurez les variables d'environnement nécessaires en créant un fichier .env à partir du modèle .env.sample :
   ```
    cp .env.sample .env

3. Modifiez le fichier .env pour y ajouter vos propres valeurs :
   ```
    DJANGO_SECRET_KEY=XXXX
    DEBUG=True
    DJANGO_LOGLEVEL=info
    DJANGO_ALLOWED_HOSTS=localhost
    DATABASE_ENGINE=postgresql_psycopg2
    DATABASE_NAME=ewallet_db
    DATABASE_USERNAME=ewallet_user
    DATABASE_PASSWORD=XXXX
    DATABASE_HOST=db
    DATABASE_PORT=5432
    API_KEY=XXXX

4. Démarrez les services Docker :
   ```
    docker-compose up --build

5. Accédez à l'application dans votre navigateur à l'adresse http://localhost:8000.
