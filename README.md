Django(DRF), React(SPA), nginx, Docker 

Django DRF + Frontend served separately (same domain)

Authenticate Single-Page Applications (SPAs) with session-based authentication.  
Using Django for our backend while the frontend will be built with React, a JavaScript library designed for building user interfaces.


        ├── backend
        │   ├── Dockerfile
        │   ├── api
        │   │   ├── __init__.py
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   │   └── __init__.py
        │   │   ├── models.py
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── djangocookieauth
        │   │   ├── __init__.py
        │   │   ├── asgi.py
        │   │   ├── settings.py
        │   │   ├── urls.py
        │   │   └── wsgi.py
        │   ├── manage.py
        │   └── requirements.txt
        ├── docker-compose.yml
        ├── frontend
        │   ├── Dockerfile
        │   ├── README.md
        │   ├── package-lock.json
        │   ├── package.json
        │   ├── public
        │   │   ├── favicon.ico
        │   │   ├── index.html
        │   │   ├── manifest.json
        │   │   └── robots.txt
        │   └── src
        │       ├── App.js
        │       ├── index.css
        │       └── index.js
        └── nginx
            ├── Dockerfile
            └── nginx.conf


*****************************
        $ docker-compose up -d --build
        
        $ docker-compose exec backend python manage.py makemigrations
        $ docker-compose exec backend python manage.py migrate
        $ docker-compose exec backend python manage.py createsuperuser
        




pip install Django
pip install djangorestframework

npm install universal-cookie