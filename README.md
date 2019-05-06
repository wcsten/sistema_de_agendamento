### Requirements

* An activated python virtualenv.
* django and djangorestframework installed and running.

Virtualenv installation/activation example:
```bash
pip install virtualenv
virtualenv env
source env/bin/activate
```

#### After installation all of the above requirements:

### Installing the project

Clone the repository and install it:

```bash 
git clone https://github.com/wcsten/sistema_de_agendamento.git
```

Go to `/sistema_de_agendamento` directory:

```bash
cd sistema_de_agendamento
```

Run the following command to install:

```bash
make install
```

And this to run:

```bash
make run
```

Run the command to create a superuser:
```bash
./manage.py createsuperuser
```

### Running

Running the application:
```bash
./manage.py runserver
```


In your browser access:

```
http://localhost:8000/
```
To use the api it is necessary to log in with the super user credentials inside the api, by clicking the login button our access:

```
http://localhost:8000/auth/login/?next=/
```

### Testing

Running tests:

Let's use the pytest to do the tests, with it properly installed we will execute the following codes in the terminal inside the directory
/sistema_de_agendamento:



```bash
export DJANGO_SETTINGS_MODULE=sistema_de_agendamento.settings
```

and to run all tests

```bash
pytest
```
our a specific test

```bash
pytest tests/tests_schedule/test_resources.py::test_name_here
```

