# FamPay Backend Engineer Intern Assignment - Frontend
*Frontend Subdirectory*
## Featues

- Display video thumbnail and title in the form of cards.
- Navigate through pages to view more videos.
- Filter through the videos using the search box.
## Instrutions to Execute
Update the `globals.ts` file to configure backend of the Application.\
<small>*Currently configured for Dockerized Solution*</small>
- <strong>Docker Based</strong>
```console
docker build . -t frontend && docker run -p 3000:3000 frontend
```
- <strong>NPM Based</strong>\
<small>make sure the backend is running and configured.</small>
```console
npm i && npm start
```
## Tech Stack Used
- React Js, TypeScript, Npm, Docker
You can access the website at [http://localhost:3000](http://localhost:3000)