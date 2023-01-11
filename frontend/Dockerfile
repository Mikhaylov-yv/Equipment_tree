#STAGE 1
FROM node:18.12.1 AS build
WORKDIR /usr/src/app
COPY ./angular_front/package.json ./angular_front/package-lock.json ./
RUN npm install
COPY ./angular_front .
RUN npm run build

#STAGE 2
FROM nginx:1.23.3
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /usr/src/app/dist/angular /usr/share/nginx/html