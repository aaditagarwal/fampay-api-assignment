# FamPay Backend Engineer Intern Assesment

This application is a demonstration of following:
- Calls YouTube API continuously in background (async) with some intervals for fetching the latest videos for a predefined search query.
- Stores specific metadata of fetched Youtube Videos in a MongoDB database indexed on Title and Description of the Videos.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A search API to search the stored videos using their title and description.
- Search API also provides partial matches for the search query.
- Dockerized Project, allowing docker-compose based deployment on a single machine.

---
Backend Server hosted on: [http://localhost:8080](http://localhost:8080)\
Website hosted on: [http://localhost:3000](http://localhost:3000)

---
## Pre-requistites
- Docker and Docker-compose
- Create a `.env` file in the [backend/](./backend/) subdirectory using the provided example [.env.example](./backend/.env.example)\
(or set an environment variable):
```sh
GOOGLE_API_KEYS=api,keys,separated,by,comma
```
<small>**NOTE**: To get the keys, follow [YouTube's specifications](https://developers.google.com/youtube/v3/getting-started).</small>

## Instructions to Execute
The whole project is dockerized (by composing dockerized versions of client and server individually)\
\
To Run
```console
docker-compose build && docker-compose up
```

_If you prefer a non dockerized version, follow the instructions in [Frontend](./frontend/README.md) and [Backend](./backend/README.md), You can also find more details for the client and server side in the mentioned subdirectories._

## About
__Aadit Agarwal__ - [aaditagarwal.in](https://aaditagarwal.in)

