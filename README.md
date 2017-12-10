### Requirements

* An activated python virtualenv.
* django and restframework installed and running.

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

Run the following command:

```bash
pip install -r requirements.txt
```

Run the Migrate command to synchronize the database with the final version.

```bash
./manage.py migrate
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

### Testing

Running tests:

Let's use the pytest to do the tests, with it properly installed we will execute the following code in the terminal inside the directory
/sistema_de_agendamento:

```bash
pytest
```
