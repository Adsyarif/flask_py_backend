pip install poetry
poetry new <FOLDER_NAME>
cd <FOLDER_NAME>
poetry add flask
poetry add Flask-SQLAlchemy (ORM)
poetry add psycopg2 (db connector)

<!-- incase no .venv in project:  -->

poetry config virtualenvs.in-project true

<!-- make venv -->

python -v venv .venv or poetry shell

poetry run flask --app .\app\ run

instal .env: poetry add poetry-dotenv-plugin

PdulMo1YJPIbhelU

<!-- migration set file -->

poetry run flask python db init

<!-- migrate run: run every updated the models -->

poetry run flask db migrate -m "add customer table"

<!-- update database -->

poetry run flask db upgrade
