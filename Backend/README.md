# Backend

## Project setup

```bash
pip install -r requirement.txt
```

### intialize the project database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create SuperUser For filling the database

```bash
python manage.py createsuperuser
```

### Start up development server

```bash
python manage.py runserver
```

### Fill the database

- Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) or [http://localhost:8000/admin](http://localhost:8000/admin)
- Login using the super user credential
- Add some Todo.

### Go to the Front-end Folder