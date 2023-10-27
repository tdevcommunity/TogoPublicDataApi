# Hacktoberfest projet 2 : Hub centralisé de données publiques du Togo | Equipe 4
Ce projet a vu le jour dans le cadre du Hacktoberfest Lomé 2023.

## Objectif
Ce projet consiste à centraliser et à rendre accessibles les données publiques du Togo, dans le but de promouvoir la transparence et de stimuler l'innovation technologique.

Pour plus de détails, veuillez consulter le wiki : https://github.com/tdevcommunity/h23_team4/wiki/Accueil

## Exécuter le projet
- Créer un environnement virtuel  
    ```sh
    python3 -m venv venv
    ```

- Activer l'environnement virtuel  
    - Unix
        ```sh
        source venv/bin/activate
        ```
    - Windows
        ```sh
        venv/bin/activate
        ```
- Installer les dépendances  
    ```sh
    pip install -r requirements.txt
    ```
- Démarrer le serveur  
    ```sh
    uvicorn main:app --reload
    ```
- L'API est disponible sur le
    ```
    localhost:8000
    ```
- La documentation est accessible au
    ```
    localhost:8000/docs
    ```

## Documentation 
Une fois le projet lancé, la documentation est accessible sur le lient 
    ```
    localhost:8000/docs
    ```