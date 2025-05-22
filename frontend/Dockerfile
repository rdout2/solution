FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

# Pour le développement, expose vite server
EXPOSE 5173

CMD ["npm", "run", "dev"]




