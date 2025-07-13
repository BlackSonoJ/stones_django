1. curl -LsSf https://astral.sh/uv/install.sh | sh или brew install uv
2. в корне пропиши uv sync для установки зависимостей
3. source .venv/bin/activate
4. cd stones
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver