#Gem powerplant-coding-challenge

## 1. Build and run the container

1. On the command line, within this directory, do this to build the image and start the container:

 docker-compose build

2. If that's successful you can then start it up. This will start up the server, and display the Django runserver logs:

 docker-compose up


## 2. Consume de API

You can use curl or postman,

Example:

curl --location --request POST 'localhost:8888/productionplan' \
--header 'Content-Type: text/plain' \
--data-raw '{
  "load": 910,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 16
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 36
    }
  ]
}'

## 3. Some explanation

In the route /code_challenge/utils.py you will find the functions that perform the calculation of the power to be produced by each plant according to the load.