version: "3.8"
services:
  evochat_app:
    build: ./evoMatrixChat
    ports:
      - "8000:8000"
    volumes:
      - ./evoMatrixChat:/app
    environment:
      - ENV=production

  redis:
    image: redis:alpine
