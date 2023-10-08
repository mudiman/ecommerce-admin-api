
# Ecommerce Admin API

This api provides ecommerce sales stats using api

Sales Status:
* Endpoints to retrieve, filter, and analyze sales data.
* Endpoints to analyze revenue on a daily, weekly, monthly, and annual basis.
* Ability to compare revenue across different periods and categories.
* Provide sales data by date range, product, and category.
Inventory Management:
* Endpoints to view current inventory status, including low stock alerts.
* Functionality to update inventory levels, and track changes over time.

## Requirements
* python 3.9
* pip
* docker
* docker-compose

## Setup

```
docker-compose up -d
pip install
alembic check
alembic upgrade head
```
To seed demo data run below command
```
python seeder.py
```

Run app
```
uvicorn main:app --reload
```

## API docs
It can be accessed using link 
```
http://localhost:8000/docs#/
```

## Extra
Run below if need to generate new migration for changes to model
```
alembic revision --autogenerate -m "comment"
```
