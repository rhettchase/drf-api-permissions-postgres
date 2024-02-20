# LAB - Class 31

## Project: Django REST Framework & Docker

### Project Description

Fully functional CRUD API app that allows users to view the collection of brews (GET), as well as Create, Update, and Delete brews from the collection.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Beginners Guide to Docker](https://wsvincent.com/beginners-guide-to-docker/)

### Setup

#### To run in Docker

- Install Docker Desktop and verify installation
  - Run `docker --version` and `docker-compose --version` to ensure both are correctly installed.

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- `PORT` - 8000

#### How to initialize/run your application (where applicable)

- Clone repo
- Install dependencies (see above)
- See the page in browser by running `docker-compose up`
- Open the page in the localhost specified in the terminal to view GET request and add `/api/v1/brews` to end of url

#### How to use your library (where applicable)

Once server is running, use Thunder Bird or other application of your choice to complete GET, PUT, POST, DELETE Requests. GET requests also can be completed in the browser.

##### GET Requests (Read)

- [`http://0.0.0.0:8000/api/v1/brews`](http://0.0.0.0:8000/api/v1/brews/)

##### POST Requests (Add)

- User Thunder Client to add JSON body, OR go to bottom of page [`http://0.0.0.0:8000/api/v1/brews/`](http://0.0.0.0:8000/api/v1/brews/)

```json
{
    "owner": 1,
    "name": "Vanilla Porter",
    "brew_type": "ST",
    "brewery": "Breckenridge Brewery",
    "description": "Aromas of vanilla and toasted grain set the stage for mellow flavors of vanilla and dark roasted malts in this popular porter."
}
```

##### PUT Requests (Update)

- [`http://0.0.0.0:8000/api/v1/brews/{id}/`](http://0.0.0.0:8000/api/v1/brews/2/)
- edit JSON body (see example above)

##### DELETE Requests

- [`http://0.0.0.0:8000/api/v1/brews/{id}/`](http://0.0.0.0:8000/api/v1/brews/2/)

#### Tests

- `python manage.py test`
