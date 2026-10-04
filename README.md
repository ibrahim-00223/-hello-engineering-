# Hello Engineering

Ce repository correspond au premier exercice de mon auto-learning assisté par IA pour devenir **AI Applied Architect**.

## Objectif de l'exercice

L'objectif était de pratiquer les bases d'un workflow de développement Python moderne :

- créer un repository GitHub ;
- initialiser un projet local avec Git ;
- créer et utiliser un environnement virtuel Python ;
- utiliser un fichier `.gitignore` pour éviter de versionner les fichiers inutiles ;
- écrire du code Python simple ;
- utiliser une dépendance externe avec `requests` ;
- appeler une API publique depuis un script Python.

## Fonctionnalité

Le script `main.py` effectue une requête HTTP vers l'API publique de recherche d'entreprises du gouvernement français :

```text
https://recherche-entreprises.api.gouv.fr/search?q=la%20poste&page=1&per_page=1
```

Il récupère les données associées à la recherche `la poste` et affiche la réponse JSON.

## Lancer le projet

Créer et activer l'environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installer la dépendance :

```bash
pip install requests
```

Lancer le script :

```bash
python main.py
```

## Compétences travaillées

- Git et GitHub
- Environnement virtuel Python
- Gestion des dépendances
- Appels HTTP avec Python
- Lecture d'une réponse JSON
- Structuration simple d'un projet
