# Books To Scrape - Scraper

Le but du projet est de récupérer les informations produit du site books.toscrape.com afin d'effectuer un suivi des prix des produits souhaités.
il se compose de trois scripts qui permettent de scraper les informations d'un produit, de tout les produits d'une catégorie ou de tout les produits du site, et de charger ces données extraites dans un fichier data_books.csv pour les données textuelles, et dans un dossier books_images pour les images en jpg.
Il contient en outre un fichier json recensant l'ensemble des titres des produits du site ainsi que l'adresse de leur page web. Ce fichier permet au script one_book_scraper.py de trouver efficacement la page d'un produit à partir de son titre.

Pour pouvoir utliser les scripts de scraping, commencez par configurer votre environnement.
En premier lieu assurez vous que python 3 et le gestionnaire de paquets pip sont bien installés sur votre système.

## Créer un environnement virtuel
Créez un environnement virtuel afin que toutes les commandes python et pip que vous executerez depuis le repertoire BooksToScrape_Project soient isolées dasn cet environnement.

    Pour créer un environnement virtuel en Python, suivez ces étapes :
        1) Ouvrez le terminal : Utilisez l'invite de commande, PowerShell, ou le terminal intégré de  Visual Studio Code.

        2) Naviguez jusqu'au répertoire de votre projet : Utilisez la commande cd pour naviguer jusqu'au dossier où vous souhaitez créer l'environnement virtuel. Par exemple :
        
        cd C:\Users\NomUtilisateur\Documents\MonProjet

        3) Créez l'environnement virtuel : Utilisez la commande suivante pour créer un environnement virtuel dans le répertoire actuel. Remplacez nom_env par le nom que vous souhaitez donner à votre environnement virtuel.

            - Sur Windows : python -m venv nom_env

            - Sur macOS et Linux : python3 -m venv nom_env

        4) Activez l'environnement virtuel : Une fois l'environnement virtuel créé, vous devez l'activer pour utiliser ses packages isolément.

            - Sur Windows : .\nom_env\Scripts\activate

            - Sur macOS et Linux : source nom_env/bin/activate

        Après avoir activé l'environnement virtuel, votre terminal affichera le nom de l'environnement virtuel, indiquant que toutes les commandes python et pip que vous exécutez seront maintenant isolées dans cet environnement.

## Installer les dépendences nécessaires au fonctionnement des scripts. 

    Ces modules sont listés dans le fichier requirements.txt. Pour les installer, après avoir activé votre environnement virtuel, suivez ces étapes :

        1) Assurez-vous que votre environnement virtuel est activé. Vous devriez voir le nom de votre environnement virtuel entre parenthèses au début de la ligne de commande dans votre terminal.

        2) Utilisez la commande suivante pour installer les dépendances listées dans requirements.txt :

            - Sur Windows : pip install -r requirements.txt

            - Sur macOS et Linux : pip install -r requirements.txt
            
    Cette commande va lire chaque ligne du fichier requirements.txt et installer les modules Python spécifiés avec les versions indiquées, en utilisant pip, le gestionnaire de paquets pour Python.

## Executer les scripts.

Une fois ces prérequis effectués vous pouvez lancer les scripts. L'execution de chaque script aura pour effet la création d'un fichier csv nommé data_books qui recueillera les donnés d'un ou plusieurs produits selon le script, et d'un dossier books_images qui recueillera spécifiquement les images de chaque produit.

        one_book_scraper.py permet de récuperer les données d'un produit.

        one_category_scraper.py permet de récupérer les données d'une catégorie entière

        all_site_scraper.py permet de récupérer les données de tout les produits du site
        
    Pour executer un script, assurez vous d'être dans le répertoire du projet (BooksToScrape_Project), utilisez la commande cd dans votre terminal pour naviguer vers celui-ci si nécessaire.
    Ensuite utilisez la commande suivante en remplacant nom_du_script.py par le nom du script souhaité :  

        - Sur windows : python nom_du_script.py

        - Sur macOS et Linux : python3 nom_du_script.py

    Notez qu'a l'execution des script scraper_booksToScrape_oneBook.py et scraper_booksToScrape_oneCategory.py il vous sera demandé d'inserer le titre d'un ouvrage ou le nom d'une categorie. Entrez le titre/nom complet. préferez un copier coller pour eviter tout risque d'erreur.