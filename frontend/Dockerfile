FROM node:22

WORKDIR /app

COPY package*.json ./
RUN npm install --no-cache

COPY . .

RUN npm run build

# Pour le développement, expose vite server
EXPOSE 5173

CMD ["npm", "run", "dev"]




