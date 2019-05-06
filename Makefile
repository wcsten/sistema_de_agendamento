
.PHONY: migrate
migrate:
	@python src/manage.py migrate

.PHONY: setup
setup:
	@pip install -r requirements.txt
	@make migrate

.PHONY: run
run:
	@python manage.py runserver
