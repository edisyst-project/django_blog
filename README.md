# Installazione
```bash
# Clonare il repository
git clone https://github.com/tuo-username/django_blog.git
cd django_blog

# OPZIONALE. Qualora non sia installato nel PC, installare Django
pip install django

# OPZIONALE. Creare un ambiente virtuale (se si usa Pipenv)
pipenv install --dev
pipenv shell

# OPZIONALE. Creare un ambiente virtuale (se si usa venv)
python3 -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# OPZIONALE. Una volta attivato l'ambiente virtuale, installa le dipendenze
pip install -r requirements.txt

# OPZIONALE. Creare il file .env e scriverci dentro questo
SECRET_KEY=tuo-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost

# Eseguire le migrazioni del database
python manage.py makemigrations
python manage.py migrate

# Popolare il database con dati fake
python manage.py create_fake_posts --number 10

# Creare un superutente
python manage.py createsuperuser

# Esecuzione dei test
python manage.py test

# Avvio server per eseguire l'applicazione
python manage.py runserver
```
  


# Filesystem di un progetto Django:
```
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Tipicamente avremo almeno una app installata nel progetto, che include i seguenti file:
```
nome_progetto/
│
├── manage.py
├── nome_progetto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app1/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
└── templates/
```


`manage.py`
- strumento da riga di comando per interagire con il progetto Django.  
- Usato per eseguire migrazioni, avviare il server, creare superuser, etc.
  - Simile a `artisan` in Laravel


`nome_progetto/` (cartella principale del progetto)
- `init.py`: File vuoto che dice a Python che questa directory dovrebbe essere considerata un package Python.
- `settings.py`: Contiene tutte le configurazioni del progetto (DB, app installate, ecc.).
  - È l'equivalente di `config/app.php` in Laravel.
- `urls.py`: Definisce le URL a livello di progetto.
  - Definisce le rotte del progetto, simile a `routes/web.php` in Laravel.
- `asgi.py` e `wsgi.py`: Punti di ingresso per server web compatibili con ASGI e WSGI.



## Creare una App Django
In Django, una "app" è un modulo indipendente all'interno del progetto, simile a un "modulo" in Laravel.  
Puoi avere più app in un progetto, e ogni app gestisce una parte dell'applicazione.

`app1/` (un'applicazione Django)
- `migrations/`: Contiene i file di migrazione del database.
- `init.py`: Rende l'app un package Python.
- `admin.py`: Configurazione per l'interfaccia di amministrazione di Django. Qui puoi registrare i modelli per farli apparire nel pannello di amministrazione di Django.
- `apps.py`: Configurazione dell'applicazione.
- `models.py`: Definisce i modelli del database (la "M" in MVT). sono l'equivalente delle classi Eloquent in Laravel.
- `tests.py`: Test unitari per l'app.
- `views.py`: Contiene la logica di presentazione (la "V" in MVT). in Django combinano il concetto di controller e le funzioni di visualizzazione.
- `urls.py`: Definisce le URL specifiche dell'app.


`templates/` (opzionale, può essere all'interno di ogni app)
- Contiene i file HTML (la "T" in MVT).



## Funzionamento di Django
URL Configuration:
- Quando arriva una richiesta, Django cerca in urls.py una corrispondenza con l'URL richiesto.
- Se trova una corrispondenza, chiama la vista associata.

Views:
- Le viste (in views.py) sono funzioni o classi che processano la richiesta e restituiscono una risposta.
- Spesso interagiscono con i modelli per ottenere dati e li passano ai template.

Models:
- Definiti in models.py, rappresentano le tabelle del database.
- Django utilizza l'ORM per interagire con il database.
  - In Django, i modelli rappresentano le tabelle del database, analogamente a come Eloquent in Laravel rappresenta le tabelle attraverso le classi.

Templates:
- File HTML con sintassi speciale di Django per il rendering dinamico.
- Ricevono dati dalle viste e li mostrano all'utente.

Forms:
- Gestiscono l'input dell'utente, la validazione e la conversione in tipi di dati Python.

Admin:
- Django fornisce un'interfaccia di amministrazione automatica basata sui tuoi modelli.

Middleware:
- Componenti che processano la richiesta/risposta globalmente prima che raggiungano la vista o l'utente.

ORM (Object-Relational Mapping):
- Permette di interagire con il database usando Python invece di SQL.

Migrations:
- Sistema per gestire le modifiche al database in modo controllato.
- Dopo aver definito il modello, dobbiamo creare e applicare le migrazioni al database





# Creare un nuovo progetto Django
```shell
django-admin startproject blogproject
cd blogproject
```

Creare un'applicazione:
```shell
python manage.py startapp posts
```

Aggiungi l'app al progetto: apri `blog_project/settings.py` e aggiungi:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',  # Questa è la riga da aggiungere
]
```

Esegui le migrazioni:
```shell
python manage.py makemigrations
python manage.py migrate
```

Avvia il server:
```shell
python manage.py runserver
```

> ORA PUOI APRIRE IL FE: http://127.0.0.1:8000


## Inserimento dati di test utilizzando l'interfaccia di amministrazione

Prima, crea un superutente:
```shell
python manage.py createsuperuser
```
Segui le istruzioni per creare un nome utente e una password. (admin - admin)

Aggiungi il modello Post all'interfaccia di amministrazione, nel file `blog/admin.py`

> ORA PUOI APRIRE IL BE: http://127.0.0.1:8000/admin

