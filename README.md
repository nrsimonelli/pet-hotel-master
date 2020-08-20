# Pet Hotel Project

_Duration - half day sprint_

> By Nick Simonelli, Ross Hutchens, Tom Hoffman, Robert Wolfe Johnson

## Description

Welcome to Pet Hotel! Here you can view, add, and delete pets from our wonderful hotel. You can even update their check-in status or view which owners have the most pets! All server side code written in Python while client side interaction was built via React.


## Installation

1. Create database named `pet_hotel` we recommend using Postico for easy integration
2. Run the queries located inthe `database.sql` file to create starter tables and data
3. Install the latest version of python3 in your project foler and setup your venv via `python3 -m venv venv`
4. Install dependencies with `pip3 install -r requirements.txt` using your terminal
5. Once up and running `export FLASK_APP=main.py` 
6. To run the project in development mode, set up development enviorment `export FLASK_ENV=development`
7. To run project run command `flask run`
8. To use routes, use Postman to send requests to the server. This project uses GET, POST, DELETE, and PATCH.


## Usage

1. check routes using Postman at local host 5000
2. get request will return all pets
3. post to add a new pet to the db
4. patch to change the check-in status of any p
5. delete to remove pet from the db
6. advanced get to view pet count by owner


### Prerequisites

- [Postman](https://www.postman.com/)
- [Postico](https://eggerapps.at/postico/)
- [Python](hhttps://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Psychopg2](https://pypi.org/project/psycopg2/)
- All project dependencies are included in `requirements.txt`


## Built With

- Python3
- Flask
- PostgreSQL
- psycopg2


## Acknowledgement

Thanks to [Prime Digital Academy](www.primeacademy.io) for the knowledge, skills, and support needed for us to make this application a reality.
