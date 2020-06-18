compose_config = -f docker-compose.yml
apps = web refresh_rates_job

up:
	docker-compose ${compose_config} up -d ${apps}

down:
	docker-compose ${compose_config} down

rebuild:
	docker-compose ${compose_config} up -d --build ${apps}

build:
	docker-compose ${compose_config} build --no-cache ${apps}

restart:
	docker-compose ${compose_config} restart ${apps}
