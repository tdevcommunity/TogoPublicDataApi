# h23_team4
 Repertoire pour le hacktoberfest Lome de l'equipe 4

# Projet 2
## Descriptions:
Un hub centralisé pour accéder à des données publiques du Togo, destiné à promouvoir la transparence et à stimuler l'innovation technologique.
## Objectifs principaux :
- Centraliser et structurer les données publiques du Togo.
- Promouvoir la transparence gouvernementale.
- Faciliter l'accès aux données pour les chercheurs, développeurs et le grand public.

**Ressources**: sites de l’INSEED, mais vous pouvez utiliser d’autres sources. Tant que ca concerne le Togo.


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