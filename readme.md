## Python Installation

- Install python on OS (v3.11.1 used)

- Install python extension on VSCode

## Set up and run

1. Clone the repository

```bash
https://github.com/SabbirHosen/Web-quiz.git
```

2. Change the working directory

```bash
cd Web-quiz
```

3. Install virtual environment (command prompt)

```bash
pip install virtualenv
```

4. Create virtual environment - "venv"

```bash
virtualenv venv
```

5. Activate virtual environment

```bash
cd venv
cd Scripts
activate
```

6. Back to root

```bash
cd ..
cd ..
```

7. Install requirements

```bash
pip install -r requirements.txt
```

8. Database migration

```bash
python manage.py migrate
```

9. Create super user

```bash
python manage.py createsuperuser
```

> Fillup user details:
>
> - userName
>
> - email
>
> - password (hidden field)

10. Run the server in localhost

```bash
python manage.py runserver
```
We can find your app run in [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
<br>
11. To run this app in local network find your device IP (YOUR-IP:PORT)
```bash
python manage.py runserver 192.168.0.1:8000
```
