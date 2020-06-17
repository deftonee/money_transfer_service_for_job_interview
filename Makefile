compose_config = -f docker-compose.yml

up:
	docker-compose ${compose_config} up -d web

down:
	docker-compose ${compose_config} down

rebuild:
	docker-compose ${compose_config} up -d --build web

build:
	docker-compose ${compose_config} build --no-cache web

restart:
	docker-compose ${compose_config} restart web
