# floz-keroz-apis

Floz-Keroz API est une application backend construite avec Flask et SQLAlchemy. Elle fournit une interface RESTful permettant de gérer des utilisateurs, leurs revenus et leurs dépenses. Ce projet est conçu pour offrir un suivi simple et efficace des finances personnelles.

---

## 📑 Fonctionnalités principales

### Utilisateurs (`/users`)

- **Créer un utilisateur** : Ajoutez un utilisateur avec ses informations personnelles.
- **Lister tous les utilisateurs** : Récupérez la liste de tous les utilisateurs enregistrés.
- **Récupérer un utilisateur par ID** : Obtenez les informations d’un utilisateur spécifique.
- **Mettre à jour un utilisateur** : Modifiez les informations d’un utilisateur existant.
- **Supprimer un utilisateur** : Supprimez un utilisateur et ses données associées.

### Dépenses (`/expenses`)

- **Ajouter une dépense** : Ajoutez une nouvelle dépense liée à un utilisateur.
- **Lister toutes les dépenses** : Obtenez un aperçu global des dépenses.
- **Lister les dépenses d’un utilisateur** : Filtrez les dépenses pour un utilisateur spécifique.
- **Mettre à jour une dépense** : Modifiez les détails d’une dépense existante.
- **Supprimer une dépense** : Supprimez une dépense.

### Revenus (`/incomes`)

- **Ajouter un revenu** : Ajoutez une nouvelle source de revenu.
- **Lister tous les revenus** : Consultez tous les revenus enregistrés.
- **Lister les revenus d’un utilisateur** : Filtrez les revenus pour un utilisateur spécifique.
- **Mettre à jour un revenu** : Modifiez les détails d’un revenu existant.
- **Supprimer un revenu** : Supprimez un revenu.

---

## 📋 Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/username/floz-keroz-api.git
   cd floz-keroz-api

2. **Installer les dépendances** :  

   ```bash
   pip install -r requirements.txt

3. **Configurer la base de données** :

   Configurez SQLAlchemy avec une base de données PostgreSQL dans le fichier de configuration Flask.

4. **Lancer l'application** :

   ```bash
   flask run
