from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
import enum

db = SQLAlchemy()


class RoleEnum(enum.Enum):
    CLIENT = "CLIENT"
    ADMIN = "ADMIN"


class StatutCommande(enum.Enum):
    CONFIRMEE = "CONFIRMEE"
    EN_PREPARATION = "EN_PREPARATION"
    EXPEDIEE = "EXPEDIEE"
    LIVREE = "LIVREE"


class Utilisateur(UserMixin, db.Model):
    __tablename__ = 'utilisateur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default=RoleEnum.ADMIN.value)

    def set_password(self, password):
        self.mot_de_passe = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.mot_de_passe, password)

    def is_admin(self):
        return self.role == RoleEnum.ADMIN.value


class Categorie(db.Model):
    __tablename__ = 'categorie'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, default='')
    produits = db.relationship('Produit', backref='categorie_rel', lazy=True)


class Produit(db.Model):
    __tablename__ = 'produit'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    categorie = db.Column(db.String(100), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=True)
    marque = db.Column(db.String(100), default='')
    prix = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), default='default.jpg')
    usage = db.Column(db.String(255), default='')
    date_ajout = db.Column(db.DateTime, default=datetime.utcnow)
    disponible = db.Column(db.Boolean, default=True)
    avis = db.relationship('Avis', backref='produit_rel', lazy=True)

    def calculer_note_moyenne(self):
        if not self.avis:
            return 0
        return round(sum(a.note for a in self.avis) / len(self.avis), 1)


class Avis(db.Model):
    __tablename__ = 'avis'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Integer, nullable=False)
    commentaire = db.Column(db.Text, default='')
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)
    nom_client = db.Column(db.String(100), default='Anonyme')
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'), nullable=False)


class Commande(db.Model):
    __tablename__ = 'commande'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), unique=True, nullable=False)
    date_commande = db.Column(db.DateTime, default=datetime.utcnow)
    montant_total = db.Column(db.Float, default=0)
    statut = db.Column(db.String(30), default=StatutCommande.CONFIRMEE.value)
    nom_client = db.Column(db.String(100), nullable=False)
    email_client = db.Column(db.String(150), nullable=False)
    telephone_client = db.Column(db.String(30), default='')
    adresse_client = db.Column(db.Text, default='')
    lignes = db.relationship('LigneCommande', backref='commande_rel', lazy=True)

    @staticmethod
    def generer_numero():
        last = Commande.query.order_by(Commande.id.desc()).first()
        num = (last.id + 1) if last else 1
        return f"#CMD-{num:04d}"


class LigneCommande(db.Model):
    __tablename__ = 'ligne_commande'
    id = db.Column(db.Integer, primary_key=True)
    commande_id = db.Column(db.Integer, db.ForeignKey('commande.id'), nullable=False)
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'), nullable=False)
    nom_produit = db.Column(db.String(200), default='')
    quantite = db.Column(db.Integer, default=1)
    prix_unitaire = db.Column(db.Float, default=0)
    produit = db.relationship('Produit')

    def sous_total(self):
        return self.quantite * self.prix_unitaire


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    auteur = db.Column(db.String(100), default='Coopérative AIT TAMNAT')
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)
