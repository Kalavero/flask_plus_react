FROM node:10

WORKDIR /srv/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "start", "--host", "0.0.0.0"  ]
