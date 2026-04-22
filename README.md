# 🌿 Coopérative AIT TAMNAT — Site E-commerce Flask

Site e-commerce complet pour la Coopérative AIT TAMNAT, spécialisée dans les produits d'argan 100% naturels du Maroc.

## 📋 Fonctionnalités

### Client (visiteur)
- Navigation et consultation du catalogue de produits
- Recherche et filtrage par catégorie et prix
- Panier d'achat (géré en session, sans inscription)
- Commande par email (numéro #CMD-XXXX généré automatiquement)
- Suivi de commande en temps réel
- Blog éducatif sur l'argan
- Avis clients avec notation étoiles (1-5)
- Traduction multilingue : Français, Anglais, Arabe (avec support RTL)
- Design responsive (mobile-first)

### Administrateur (back-office)
- Tableau de bord avec statistiques en temps réel
- Gestion CRUD des produits
- Gestion des commandes (consultation, changement de statut)
- Historique des commandes
- Export des rapports de ventes (Excel / PDF)

## 🛠️ Technologies

- **Backend** : Python 3 + Flask
- **Base de données** : SQLite (SQLAlchemy ORM)
- **Templating** : Jinja2
- **Frontend** : HTML5, CSS3, JavaScript vanilla
- **Emails** : Flask-Mail (SMTP Gmail)
- **Export** : openpyxl (Excel), reportlab (PDF)

## 🚀 Installation & Lancement

### 1. Prérequis
- Python 3.8+
- pip

### 2. Installation

```bash
# Cloner ou extraire le projet
cd argan_shop

# Créer un environnement virtuel (recommandé)
python -m venv venv

# Activer l'environnement virtuel
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Initialiser la base de données

```bash
python seed.py
```

Cela crée la base de données SQLite et charge :
- 36 produits répartis en 7 catégories
- 3 articles de blog éducatifs
- 5 avis clients exemples
- 1 compte administrateur

### 4. Lancer le serveur

```bash
python app.py
```

Le site sera accessible à : **http://localhost:5000**

## 🔑 Compte Administrateur

- **URL** : http://localhost:5000/admin/login
- **Email** : `admin@aittamnat.com`
- **Mot de passe** : `Admin@2024`

## 📧 Configuration Email

Pour activer l'envoi d'emails, modifiez `config.py` :

```python
MAIL_USERNAME = 'votre_email@gmail.com'
MAIL_PASSWORD = 'votre_mot_de_passe_application'
```

> ⚠️ Utilisez un **mot de passe d'application** Gmail (pas votre mot de passe principal).
> Générez-le dans : Google Account → Sécurité → Mots de passe des applications

## 📁 Structure du projet

```
argan_shop/
├── app.py                  # Application Flask principale
├── config.py               # Configuration
├── models.py               # Modèles SQLAlchemy
├── seed.py                 # Script de pré-chargement
├── requirements.txt        # Dépendances Python
├── routes/
│   ├── client.py           # Routes client (public)
│   └── admin.py            # Routes admin (back-office)
├── services/
│   ├── email_service.py    # Envoi d'emails
│   └── export_service.py   # Export PDF/Excel
├── translations/
│   ├── fr/messages.json    # Français
│   ├── en/messages.json    # Anglais
│   └── ar/messages.json    # Arabe
├── static/
│   ├── css/style.css       # Styles (palette marron/doré/crème)
│   ├── js/main.js          # JavaScript
│   └── images/products/    # Images produits
└── templates/
    ├── base.html           # Template de base
    ├── client/             # Templates client
    └── admin/              # Templates admin
```

## 🎨 Charte graphique

| Couleur        | Code Hex  | Usage                |
|----------------|-----------|----------------------|
| Marron foncé   | `#5C3D2E` | Fond navbar, titres  |
| Doré           | `#C5A55A` | Accents, boutons CTA |
| Crème          | `#F5F0E8` | Fond de page         |
| Blanc cassé    | `#FAFAF5` | Cartes, contenus     |
| Texte sombre   | `#2D1F14` | Texte principal      |

## 📞 Informations de contact

- **Coopérative** : AIT TAMNAT
- **Email** : 81.amhabou@gmail.com
- **Téléphone** : +212 6 53 64 16 29
- **Adresse** : Douar Ighrem Nogdal, 125 km de Marrakech

## 📝 Notes

- Les images produits doivent être placées dans `static/images/products/`
- Le panier est stocké en session Flask (pas de base de données)
- Les commandes sont envoyées par email à `zakariabenhachlaf44@gmail.com`
- Le site supporte le mode RTL pour l'arabe
