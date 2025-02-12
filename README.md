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
   ```sh
   git clone https://github.com/votre-utilisateur/ewallet.git
   cd ewallet
   ```

## How to Test

Pour exécuter les tests unitaires, utilisez la commande suivante :
   
```sh
python ewallet/manage.py makemigrations
python ewallet/manage.py migrate
python ewallet/manage.py test accounts
python ewallet/manage.py test finance
```

## How to Run Locally

### 1. Exécution en local (Mode traditionnel)

1. Assurez-vous que toutes les dépendances sont installées (voir la section "How to Build").
2. Configurez les variables d'environnement en créant un fichier `.env` à partir du modèle `.env.sample` :
   ```sh
   cp .env.sample .env
   ```
3. Modifiez le fichier `.env` pour y ajouter vos propres valeurs :
   ```sh
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
   ```
4. Démarrez les services Docker :
   ```sh
   docker-compose up --build
   ```
5. Accédez à l'application dans votre navigateur à l'adresse [http://localhost:8000](http://localhost:8000).

### 2. Exécution en local avec une image Docker pré-construite

Si vous souhaitez utiliser une image Docker déjà construite, suivez ces étapes :

1. Créez un fichier `.env` en utilisant le modèle existant :
   ```sh
   cp .env.sample .env
   ```
2. Modifiez les valeurs dans `.env` si nécessaire.
3. Utilisez le fichier `docker-compose.yml` suivant :
   ```yaml
   version: '3.8'
   
   services:
     db:
       image: postgres:17
       environment:
         POSTGRES_DB: ${DATABASE_NAME}
         POSTGRES_USER: ${DATABASE_USERNAME}
         POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
       ports:
         - "5432:5432"
       volumes:
         - postgres_data:/var/lib/postgresql/data
       env_file:
         - .env
   
     django-web:
       image: rexmicool/ewallet:release1.0.3
       container_name: django-docker
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         DJANGO_SECRET_KEY: ${DJANGO_SECRET_KEY}
         DEBUG: ${DEBUG}
         DJANGO_LOGLEVEL: ${DJANGO_LOGLEVEL}
         DJANGO_ALLOWED_HOSTS: ${DJANGO_ALLOWED_HOSTS}
         DATABASE_ENGINE: ${DATABASE_ENGINE}
         DATABASE_NAME: ${DATABASE_NAME}
         DATABASE_USERNAME: ${DATABASE_USERNAME}
         DATABASE_PASSWORD: ${DATABASE_PASSWORD}
         DATABASE_HOST: ${DATABASE_HOST}
         DATABASE_PORT: ${DATABASE_PORT}
         API_KEY: ${API_KEY}
       env_file:
         - .env
   
   volumes:
     postgres_data:
   ```

4. Lancez les services en mode détaché :
   ```sh
   docker compose up -d --build
   ```
5. Accédez à l'application à l'adresse [http://localhost:8000](http://localhost:8000).

Avec cette méthode, vous utilisez directement une image Docker pré-construite sans avoir à builder le projet vous-même.

