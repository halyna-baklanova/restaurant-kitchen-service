# restaurant-kitchen-service

Description. This website is designed for convenient management of the actions of chefs in a restaurant. It provides the ability to assign responsible registered chefs to specific dishes. Therefore, the site administrator should be the head chef, who chooses who prepares what. Regular chefs can view their responsibilities and, in their free time, create their own recipes, which the head chef can review and assign executors for.

## Technologies Used

- Python
- Django
- HTML/CSS (Bootstrap)
- SQLite

## DB Structure:

![DB Structure](static/image_readme/db_structure.png)

## Installation

Clone the project:

`git clone https://github.com/halyna-baklanova/restaurant-kitchen-service/`

Create virtual environment and activate it

for Unix OC

`python3 -m venv .venv`

`source venv/bin/activate` for Unix OC

for Windows

`python -m venv venv`

`venv\Scripts\activate`


Install dependencies

`pip install -r requirements.txt`

Run migrations

`python manage.py migrate`

Create superuser

`python manage.py createsuperuser` (enter your username and password)

Run server on local host

you must create .env file with your data (look at exemple in .env.sample)

`python manage.py runserver`

Open your web browser and go to `http://127.0.0.1:8000`

Home page:
![Home page](static/image_readme/home_page.jpg)

![Cooks list](static/image_readme/cooks_list.jpg)

![Dish list](static/image_readme/dishes_list.jpg)

![Dish type list](static/image_readme/dishes_type.jpg)

![Dish detail](static/image_readme/dish_detail.jpg)

![Assign cooks](static/image_readme/assign_cooks.jpg)


