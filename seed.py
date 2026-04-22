"""
Script de pré-chargement des données pour la Coopérative AIT TAMNAT.
Usage: python seed.py
"""
from app import create_app
from models import db, Utilisateur, Categorie, Produit, Article, Avis
from datetime import datetime

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # ========== ADMIN ==========
    admin = Utilisateur(
        nom='Admin',
        prenom='AIT TAMNAT',
        email='admin@aittamnat.com',
        role='ADMIN'
    )
    admin.set_password('Admin@2024')
    db.session.add(admin)

    # ========== CATEGORIES ==========
    categories_data = [
        ("Huiles d'Argan", "Huiles d'argan pures cosmétiques et alimentaires"),
        ("Crèmes & Soins Visage", "Crèmes hydratantes et soins pour le visage à l'argan"),
        ("Lotions d'Argan", "Lotions corporelles parfumées à l'huile d'argan"),
        ("Crème Mains & Laits Corps", "Crèmes pour les mains et laits corporels à l'argan"),
        ("Soins Cheveux", "Shampooings, sérums et après-shampooings à l'argan"),
        ("Savons Naturels", "Savons artisanaux et savons noirs traditionnels"),
        ("Alimentation & Bien-Être", "Amlou, miel et produits alimentaires à l'argan"),
    ]

    cat_objects = {}
    for libelle, desc in categories_data:
        cat = Categorie(libelle=libelle, description=desc)
        db.session.add(cat)
        cat_objects[libelle] = cat

    db.session.flush()

    # ========== PRODUITS ==========
    produits_data = [
        # Cat 1: Huiles d'Argan
        ("Huile d'Argan Cosmétique – 500ml", "Coopérative AIT TAMNAT",
         "Huile d'argan pure non torréfiée pour les soins cosmétiques. Riche en vitamine E et acides gras essentiels, elle nourrit, hydrate et protège la peau et les cheveux en profondeur.",
         900, "huile_argan_cosmetique_500ml.jpg", "Huiles d'Argan", "Visage · Corps · Cheveux"),

        ("Huile d'Argan Cosmétique – 100ml (spray)", "Coopérative AIT TAMNAT",
         "Huile d'argan cosmétique non torréfiée en 100ml avec vaporisateur. Application facile et précise sur visage, corps ou cheveux.",
         300, "huile_argan_cosmetique_100ml_spray.jpg", "Huiles d'Argan", "Visage · Corps · Cheveux"),

        ("Huile d'Argan Cosmétique – 100ml (flacon noir)", "Coopérative AIT TAMNAT",
         "Huile d'argan cosmétique en flacon opaque noir avec pompe doseur, préservant ses propriétés actives à l'abri de la lumière.",
         300, "huile_argan_cosmetique_100ml_noir.jpg", "Huiles d'Argan", "Visage · Corps · Cheveux"),

        ("Huile d'Argan Alimentaire – 250ml", "Coopérative AIT TAMNAT",
         "Huile d'argan 100% biologique extraite d'amandes torréfiées. Saveur unique pour les plats marocains et richesse nutritionnelle exceptionnelle.",
         400, "huile_argan_alimentaire_250ml.jpg", "Huiles d'Argan", "Cuisine · Salade · Amlou"),

        ("Huile d'Argan Alimentaire – 100ml", "Coopérative AIT TAMNAT",
         "Huile d'argan culinaire 100% bio en format 100ml. Extraite de l'amande grillée de l'arganier, indispensable dans la cuisine marocaine.",
         200, "huile_argan_alimentaire_100ml.jpg", "Huiles d'Argan", "Cuisine · Assaisonnement"),

        ("Huile de Cactus – 30ml", "Coopérative AIT TAMNAT",
         "Huile précieuse extraite des graines de figue de barbarie. L'une des plus riches en vitamine E, aux propriétés anti-âge et régénératrices reconnues.",
         800, "huile_cactus_30ml.jpg", "Huiles d'Argan", "Anti-âge · Éclat · Réparation"),

        # Cat 2: Crèmes & Soins Visage
        ("Crème d'Argan Hydratante – Willcos", "Argan Willcos",
         "Crème hydratante à l'huile d'argan bio. Texture légère et fondante qui nourrit en profondeur et restaure l'éclat naturel du teint.",
         150, "creme_argan_hydratante_willcos.jpg", "Crèmes & Soins Visage", "Visage · Tous types de peaux"),

        ("Crème d'Argan Fleur d'Oranger – Willcos", "Argan Willcos",
         "Crème argan bio enrichie à la fleur d'oranger. Allie les bienfaits de l'argan à la douceur florale pour une peau apaisée et lumineuse.",
         150, "creme_argan_fleur_oranger_willcos.jpg", "Crèmes & Soins Visage", "Visage · Peau sensible"),

        ("Soin Anti-Cernes à l'Huile d'Argan", "Argan Willcos",
         "Sérum en flacon compte-gouttes pour le contour des yeux. Réduit les cernes, atténue les poches et illumine le regard.",
         200, "soin_anti_cernes_argan.jpg", "Crèmes & Soins Visage", "Contour des yeux"),

        ("Day Cream – Crème de Jour – 50ml", "Coopérative AIT TAMNAT",
         "Crème de jour à l'huile d'argan, protège et hydrate la peau toute la journée. Convient à tous types de peaux.",
         150, "day_cream_50ml.jpg", "Crèmes & Soins Visage", "Visage · Tous types de peaux"),

        # Cat 3: Lotions d'Argan
        ("Lotion d'Argan au Gardénia", "Arganisme",
         "Lotion légère à l'argan parfumée au gardénia. Hydrate et adoucit avec un sillage floral élégant. Formule naturelle du Maroc.",
         200, "lotion_argan_gardenia.jpg", "Lotions d'Argan", "Corps · Soin quotidien"),

        ("Lotion d'Argan à l'Orchidée", "Arganisme",
         "Lotion à l'argan infusée à l'essence d'orchidée. Propriétés nourrissantes de l'argan et notes florales précieuses.",
         200, "lotion_argan_orchidee.jpg", "Lotions d'Argan", "Corps · Soin quotidien"),

        ("Lotion d'Argan au Jasmin", "Arganisme",
         "Lotion d'argan au jasmin pour une peau douce et parfumée. Vertus apaisantes et parfum envoûtant du jasmin.",
         200, "lotion_argan_jasmin.jpg", "Lotions d'Argan", "Corps · Peau sèche"),

        ("Lotion d'Argan à l'Ambre", "Arganisme",
         "Lotion d'argan aux notes chaleureuses de l'ambre. Soin hydratant au parfum oriental profond et enveloppant.",
         200, "lotion_argan_ambre.jpg", "Lotions d'Argan", "Corps · Soin quotidien"),

        ("Lotion d'Argan à la Rose", "Arganisme",
         "Lotion d'argan enrichie à l'essence de rose. Douceur florale et bienfaits de l'argan pour un soin corps délicat.",
         200, "lotion_argan_rose.jpg", "Lotions d'Argan", "Corps · Peau sensible"),

        ("Lotion d'Argan au Pamplemousse", "Arganisme",
         "Lotion d'argan vivifiante aux notes fraîches de pamplemousse. Tonifie, hydrate et aide à lutter contre les signes du vieillissement.",
         200, "lotion_argan_pamplemousse.jpg", "Lotions d'Argan", "Corps · Peau terne"),

        ("Lotion d'Argan au Thé Vert", "Arganisme",
         "Lotion d'argan antioxydante au thé vert. Protège la peau des agressions extérieures et lui apporte fraîcheur et vitalité.",
         200, "lotion_argan_the_vert.jpg", "Lotions d'Argan", "Corps · Peau fatiguée"),

        # Cat 4: Crème Mains & Laits Corps
        ("Crème Mains à l'Huile d'Argan – 50ml", "Coopérative AIT TAMNAT",
         "Crème mains nourrissante à l'huile d'argan, pour les mains abîmées, sèches et très sèches. Douceur immédiate et protection durable.",
         150, "creme_mains_argan_50ml.jpg", "Crème Mains & Laits Corps", "Mains sèches & abîmées"),

        ("Lait d'Argan Hydratant – 200ml", "Arganisme",
         "Lait corporel à l'argan nature, 100% naturel, sans paraben. Texture légère à absorption rapide pour une hydratation longue durée.",
         200, "lait_argan_hydratant_200ml.jpg", "Crème Mains & Laits Corps", "Corps · Hydratation quotidienne"),

        ("Lait d'Argan au Gardénia – 200ml", "Arganisme",
         "Lait corporel à l'argan et au gardénia. Soin hydratant intense aux notes fleuries, 100% naturel et sans paraben.",
         200, "lait_argan_gardenia_200ml.jpg", "Crème Mains & Laits Corps", "Corps · Soin parfumé"),

        ("Lait d'Argan Hydratant – 100ml", "Arganisme",
         "Format voyage du lait corporel à l'argan. 100% naturel, sans paraben, idéal pour emporter partout.",
         150, "lait_argan_hydratant_100ml.jpg", "Crème Mains & Laits Corps", "Corps · Format voyage"),

        ("Lait d'Argan au Gardénia – 100ml", "Arganisme",
         "Version 100ml du lait corporel argan-gardénia. Pratique et généreux, toujours 100% naturel et sans paraben.",
         150, "lait_argan_gardenia_100ml.jpg", "Crème Mains & Laits Corps", "Corps · Format voyage"),

        # Cat 5: Soins Cheveux
        ("Sérum Cheveux Argan – Willcos", "Argan Willcos",
         "Sérum capillaire à l'huile d'argan en flacon pompe. Répare et sublime les cheveux secs et abîmés, apporte brillance et protection. 50g.",
         200, "serum_cheveux_argan_willcos.jpg", "Soins Cheveux", "Tous types de cheveux"),

        ("Shampooing d'Argan Nature", "Arganisme",
         "Shampooing extra doux et nourrissant à l'argan. Rééquilibre le cuir chevelu, convient à tous types de cheveux. Produit du Maroc.",
         200, "shampooing_argan_nature.jpg", "Soins Cheveux", "Tous types de cheveux"),

        ("Après-Shampooing à l'Argan – Extra Doux", "Arganisme",
         "Démêlant conditionneur à l'argan. Nourrit et lisse intensément les cheveux secs et abîmés pour des cheveux soyeux.",
         150, "apres_shampooing_argan.jpg", "Soins Cheveux", "Cheveux secs & abîmés"),

        # Cat 6: Savons Naturels
        ("Savon d'Argan Nature", "Arganisme",
         "Savon naturel à l'huile d'argan. Nourrit, hydrate et tonifie. Formule douce pour toute la famille. Produit du Maroc.",
         70, "savon_argan_nature.jpg", "Savons Naturels", "Corps · Visage"),

        ("Savon d'Argan avec Nila", "Arganisme",
         "Savon naturel à l'argan et au nila (indigo marocain). Nourrit, hydrate, tonifie et purifie grâce aux propriétés traditionnelles du nila.",
         70, "savon_argan_nila.jpg", "Savons Naturels", "Corps · Peau terne"),

        ("Savon Naturel Ambre", "Coopérative AIT TAMNAT",
         "Savon naturel aux notes sensuelles de l'ambre. Fabriqué artisanalement à Douar Ighrem Nogdal.",
         80, "savon_naturel_ambre.jpg", "Savons Naturels", "Corps"),

        ("Savon Naturel Pêche", "Coopérative AIT TAMNAT",
         "Savon naturel fruité à la pêche. Doux et parfumé, laisse la peau douce et délicatement parfumée.",
         80, "savon_naturel_peche.jpg", "Savons Naturels", "Corps"),

        ("Savon Naturel Musc", "Coopérative AIT TAMNAT",
         "Savon naturel au musc blanc. Parfum enveloppant et élégant pour un soin quotidien subtil.",
         80, "savon_naturel_musc.jpg", "Savons Naturels", "Corps"),

        ("Savon Noir Nature", "Arganisme",
         "Savon beldi noir traditionnel marocain. Nettoyant, il élimine les cellules mortes et impuretés. Idéal avant le gommage au hammam.",
         150, "savon_noir_nature.jpg", "Savons Naturels", "Corps · Hammam"),

        ("Savon Noir à la Lavande", "Arganisme",
         "Savon beldi noir enrichi à la lavande. Vertus exfoliantes du savon noir et propriétés apaisantes de la lavande.",
         150, "savon_noir_lavande.jpg", "Savons Naturels", "Corps · Hammam"),

        ("Savon Noir à la Rose", "Arganisme",
         "Savon beldi noir infusé à la rose. Geste de beauté ancestral qui exfolie et régénère la peau en profondeur.",
         150, "savon_noir_rose.jpg", "Savons Naturels", "Corps · Hammam"),

        ("Savon Noir Argan & Eucalyptus", "Arganisme",
         "Savon noir à l'argan et à l'eucalyptus. Nettoie, adoucit et exfolie. L'eucalyptus apporte ses propriétés purifiantes.",
         150, "savon_noir_argan_eucalyptus.jpg", "Savons Naturels", "Corps · Gommage"),

        # Cat 7: Alimentation & Bien-Être
        ("Amlou – Pâte d'Amande, Miel & Argan – 250g", "Coopérative AIT TAMNAT",
         "Spécialité marocaine : pâte d'amande, miel et huile d'argan bio. Nutritif et délicieux, idéal au petit-déjeuner avec du pain frais.",
         150, "amlou_250g.jpg", "Alimentation & Bien-Être", "Petit-déjeuner · Collation"),

        ("Miel aux Plantes Médicinales", "Coopérative AIT TAMNAT",
         "Miel artisanal aux plantes médicinales récolté à Douar Ighrem Nogdal. Bienfaits du miel pur et des herbes médicinales locales.",
         150, "miel_plantes_medicinales.jpg", "Alimentation & Bien-Être", "Bien-être · Cuisine · Remèdes naturels"),
    ]

    for nom, marque, desc, prix, image, categorie, usage in produits_data:
        cat = cat_objects.get(categorie)
        produit = Produit(
            nom=nom,
            marque=marque,
            description=desc,
            prix=prix,
            image=image,
            categorie=categorie,
            categorie_id=cat.id if cat else None,
            usage=usage,
            disponible=True
        )
        db.session.add(produit)

    # ========== ARTICLES DE BLOG ==========
    articles_data = [
        (
            "Les bienfaits de l'huile d'argan pour la peau",
            """<p>L'huile d'argan, surnommée <strong>« l'or liquide du Maroc »</strong>, est extraite des amandons de l'arganier, un arbre endémique du sud-ouest marocain. Depuis des siècles, les femmes berbères l'utilisent pour nourrir et protéger leur peau des conditions climatiques arides.</p>

<h3>Propriétés hydratantes</h3>
<p>Riche en acides gras essentiels (oméga-6 et oméga-9), l'huile d'argan pénètre rapidement la peau sans laisser de film gras. Elle restaure le film hydrolipidique naturel et prévient la déshydratation cutanée. Quelques gouttes suffisent pour nourrir l'ensemble du visage.</p>

<h3>Vertus anti-âge</h3>
<p>Sa haute teneur en vitamine E (tocophérols) en fait un puissant antioxydant naturel. Elle combat les radicaux libres responsables du vieillissement prématuré, atténue les rides et ridules, et redonne élasticité et fermeté à la peau.</p>

<h3>Propriétés réparatrices</h3>
<p>L'huile d'argan favorise la régénération cellulaire. Elle est particulièrement efficace pour apaiser les irritations, les cicatrices légères, et les vergetures. Les dermatologues la recommandent pour les peaux sensibles et réactives.</p>

<h3>Comment l'utiliser ?</h3>
<p>Appliquez quelques gouttes d'huile d'argan cosmétique pure sur le visage propre et humide, matin et soir. Massez doucement en mouvements circulaires ascendants. Vous pouvez aussi l'ajouter à votre crème habituelle pour booster son efficacité.</p>"""
        ),
        (
            "L'argan dans la cuisine marocaine : traditions et recettes",
            """<p>Si l'huile d'argan cosmétique est mondialement connue, l'<strong>huile d'argan alimentaire</strong> (torréfiée) est un trésor de la gastronomie marocaine. Issue d'amandes d'arganier grillées, elle développe un arôme de noisette intense et une saveur unique.</p>

<h3>L'Amlou : la pâte à tartiner marocaine</h3>
<p>L'amlou est sans doute la recette la plus emblématique à base d'argan. Ce mélange d'amandes grillées pilées, de miel pur et d'huile d'argan alimentaire constitue un petit-déjeuner royal. Traditionnellement servi avec du pain frais, l'amlou est considéré comme un aliment énergétique et revitalisant.</p>

<h3>En assaisonnement</h3>
<p>L'huile d'argan alimentaire s'utilise exclusivement à froid ou en fin de cuisson pour préserver ses qualités nutritionnelles. Elle sublime les salades marocaines (tomates, poivrons grillés), les couscous, les tajines, et même les soupes traditionnelles comme la harira.</p>

<h3>Bienfaits nutritionnels</h3>
<p>L'huile d'argan alimentaire est riche en acides gras insaturés, en vitamine E et en polyphénols. Des études ont montré qu'elle contribue à réduire le cholestérol, protège le système cardiovasculaire et possède des propriétés anti-inflammatoires.</p>

<h3>Recette simple : Salade tiède à l'huile d'argan</h3>
<p>Faites griller des poivrons et des tomates au four. Épluchez-les et coupez-les en lanières. Disposez dans une assiette, ajoutez un filet d'huile d'argan alimentaire, du cumin, du sel et quelques gouttes de jus de citron. Un délice simple et authentique !</p>"""
        ),
        (
            "Le savon noir marocain : rituel du hammam",
            """<p>Le <strong>savon noir</strong> (savon beldi) est un pilier incontournable du rituel de beauté marocain. Fabriqué à partir d'un mélange d'huile d'olive et d'olives noires macérées, il se présente sous forme d'une pâte dense et onctueuse de couleur brune à noire.</p>

<h3>Le rituel du hammam</h3>
<p>Le hammam marocain est bien plus qu'un simple bain : c'est un rituel de purification du corps et de l'esprit pratiqué depuis des siècles. Voici les étapes traditionnelles :</p>

<p><strong>1. La vapeur :</strong> Restez 10 à 15 minutes dans la chaleur humide du hammam pour ouvrir les pores et préparer la peau au gommage.</p>

<p><strong>2. Application du savon noir :</strong> Étalez une couche généreuse de savon noir sur l'ensemble du corps humide. Laissez poser 5 à 10 minutes pour que les actifs pénètrent la peau.</p>

<p><strong>3. Le gommage au kessa :</strong> À l'aide d'un gant de kessa (gant exfoliant traditionnel), frottez vigoureusement la peau par mouvements circulaires. Vous verrez des rouleaux de peau morte se détacher : c'est normal et signe que le gommage fonctionne.</p>

<p><strong>4. Le rinçage :</strong> Rincez abondamment à l'eau tiède puis froide pour refermer les pores.</p>

<h3>Les bienfaits</h3>
<p>Le savon noir élimine en profondeur les cellules mortes, les impuretés et les toxines. Il laisse la peau douce, lisse et lumineuse. Enrichi à l'huile d'argan, il apporte en plus une nutrition intense. Les versions à la lavande, à la rose ou à l'eucalyptus ajoutent leurs propriétés aromathérapeutiques respectives.</p>

<h3>Conseil de la coopérative</h3>
<p>Pour un rituel hammam à la maison, prenez un bain chaud ou une douche bien chaude pendant 10 minutes, puis appliquez le savon noir. Vous obtiendrez des résultats similaires au hammam traditionnel !</p>"""
        ),
    ]

    for titre, contenu in articles_data:
        article = Article(
            titre=titre,
            contenu=contenu,
            auteur='Coopérative AIT TAMNAT'
        )
        db.session.add(article)

    # ========== AVIS EXEMPLES ==========
    db.session.flush()
    produits = Produit.query.limit(5).all()
    avis_data = [
        (5, "Excellente huile d'argan, je l'utilise tous les jours pour mon visage. Ma peau est transformée !", "Fatima Z."),
        (4, "Très bon produit, livraison rapide. Je recommande la coopérative.", "Mohammed A."),
        (5, "L'amlou est délicieux ! Le goût authentique du Maroc.", "Sarah L."),
        (4, "Le savon noir est incroyable pour le gommage. Ma peau n'a jamais été aussi douce.", "Khadija M."),
        (5, "Produits 100% naturels, on sent la qualité. Bravo à la coopérative !", "Youssef B."),
    ]
    for i, (note, commentaire, nom) in enumerate(avis_data):
        if i < len(produits):
            avis = Avis(
                note=note,
                commentaire=commentaire,
                nom_client=nom,
                produit_id=produits[i].id
            )
            db.session.add(avis)

    db.session.commit()
    print("✅ Base de données initialisée avec succès !")
    print(f"   → {Produit.query.count()} produits")
    print(f"   → {Categorie.query.count()} catégories")
    print(f"   → {Article.query.count()} articles de blog")
    print(f"   → {Avis.query.count()} avis clients")
    print(f"   → Admin: admin@aittamnat.com / Admin@2024")
