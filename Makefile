up:
	docker compose up -d

down:
	docker compose down

rebuild:
	docker compose build --no-cache

exec-app:
	docker compose exec app /bin/bash

logs:
	docker compose logs -f