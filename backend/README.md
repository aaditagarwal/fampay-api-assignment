# FamPay Backend Engineer Intern Assignment - Backend

*Backend Subdirectory*

## Features

- Polls the Youtube API every 10 seconds to fetch latest videos based on a predeined search query and saves video metadata into a MongoDB database.
- Fetch API to fetch paginated videos sorted in descending order of published datetime.
- Search API to filter through the list of videos index on title and description based on search query with partial match for the search query.
- Multiple API key support providing automatic use of  a different API key when one key's quota is exhausted.

## Pre-Requisites

- Google API key. Create a `.env` file in the root folder following the template given in [.env.example](./.env.example) and add the API key(s) to the file.
- Docker and docker-compose.
- Instead of Docker, you can use Python and MongoDb.

## Instructions to Execute

<small>Configure config.ts for MongoDB database</small>
- <strong>Docker Based</strong>

```console
docker build . -t backend && docker run -p 8080:8080 backend
``` 
- <strong>Python Based</strong>\
<small>To start server in deployment mode.</small>
```shell
pip install -r requirements.txt
python server.py
```

## Tech Stack Used
- Python (Flask), MongoDB, Docker
## Code Navigation
- The entry point into the server codebase is [server.py](./server.py).
- All the available API routes can be found in the server file.
- All the services can be found in the [Service/](./Service/) directory.
- The youtube API services are coded in the [youtube_service.py](./Service/youtube_service.py), while the database services are in the [database_service.py](./Service/database_service.py)
- The database related code pieces are in the [Database/](./Database/) directory.
- The MongoDB connection is defined in [mongoDb.py](./Database/mongoDB.py), while the Schema used in [schema.py](./Database/schema.py). And the queries execting on the database are coded in [queries.py](./Database/queries.py)
- Any addition utility functions are configurations are in [lib/](./lib/) directory.

## Trying it out
- The Server is up on [http://localhost:8080](http://localhost:8080)
- [http://localhost:8080/search?query=<search_query_string>&page=<page_number>](http://localhost:8080/search?query=<search_query_string>&page=<page_number>) to try out the filtered search API with partial string match.