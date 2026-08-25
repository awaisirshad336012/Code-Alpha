# Roast & Ritual — Simple E-Commerce Store

Built for the **CodeAlpha Full Stack Development Internship** — Task 1: Simple E-commerce Store.

A small coffee/tea/brew-gear shop with product listings, a shopping cart, checkout with order
processing, and user registration/login — built with Django.

## Features

- **Product listings** — browse by category (Coffee, Tea, Brew Gear), with a product detail page
- **Shopping cart** — session-based cart: add, update quantity, remove
- **Order processing** — checkout form → order + order items saved to the database, with a
  confirmation page and an order history page
- **User registration/login** — Django's built-in auth system, checkout requires login
- **Admin panel** — manage products, categories, and orders at `/admin/`

## Tech stack

- Backend: Django 5/6 (Python)
- Frontend: Django templates, HTML/CSS (no JS framework — plain CSS in `static/css/style.css`)
- Database: SQLite (default, zero config)

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Load sample products (optional but recommended)
python manage.py loaddata sample_data

# 5. Create an admin account (optional, for /admin/)
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

## Project structure

```
CodeAlpha_ECommerceStore/
├── manage.py
├── requirements.txt
├── ecommerce/          # Django project settings, root URLs
├── store/              # The app: models, views, urls, forms, admin
│   ├── models.py       # Category, Product, Order, OrderItem
│   ├── cart.py         # Session-based cart class
│   ├── views.py
│   ├── forms.py        # Registration + checkout forms
│   ├── admin.py
│   └── fixtures/sample_data.json
├── templates/store/    # All page templates
└── static/css/style.css
```

## Notes for submission

- Repo name follows the required convention: `CodeAlpha_ECommerceStore`
- `db.sqlite3` is intentionally not committed (see `.gitignore`) — it's created locally by
  `migrate`. Anyone cloning the repo just runs the setup steps above.
- Remember to also: share your internship status on LinkedIn tagging @CodeAlpha, post a short
  video walkthrough with the GitHub link, and submit through the WhatsApp submission form.
