<h1 align="center"> 
🍲 FastAPI Boilerplate
</h1>

<h2 align="center">
  A production ready Django like simplest FastAPI boilerplate 🐍
</h2>

# 💎 Features

✅ Production ready with one docker-compose command. \
✅ Similar to Django Code Structure. \
✅ Local dockerized db.\
✅ Dockerized PgAdmin to check the db records.\
✅ Migrations, Serializers and ORM configured.\
✅ CRUD APIs (Sneaker App).\
✅ Token Authentication.\
✅ Logging Mechanism.\
✅ Testcases with FastAPI, Pytest. \
✅ Test Driven Development.\
✅ Seperate Database(Sqlite) adn mock session configured for test cases.


# ⚒️ Techologies Used

- Alembic: For Database Migrations.
- SQLAlchemy: For ORM.
- Pydantic: For Typing or Serialization.
- Pytests: For TDD or Unit Testing.
- Poetry: For Package management. (Better than pip)
- Docker & docker-compose : For Virtualization.
- postgresSQL: Database.
- Loguru: Easiest logging ever done.

# 🚀 Up and run in 5 mins 🕙
Make sure you have docker and docker-compose installed [docker installation guide](https://docs.docker.com/compose/install/)
## Step 1
create **.env** file in root folder fastapi-boilerplate/.env
```
DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/boiler_plate_db
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=boiler_plate_db 
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
X_TOKEN=12345678910
```

## Step 2
```
docker-compose build
```

## Step 3
```
docker-compose up
```

Your Production Ready FastAPI CRUD backend app is up and running.

- App on `localhost:8000`
- Swagger docs on `localhost:8000/docs`
- PgAdmin on `localhost:5050`


