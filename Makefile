
.PHONY: migrate
migrate:
	@python manage.py migrate

.PHONY: install
install:
	@pip install -r requirements.txt
	@make migrate

.PHONY: run
run:
	@python manage.py runserver

.PHONY: test
test:
	@pytest
