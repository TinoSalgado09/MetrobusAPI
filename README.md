<h1 align="center" id="title"> :bus: Metrobus pipeline data analysis</h1>

This project focus on development a pipeline data analysis to data open Metrobus CDMX System. 


## Features
Here're some of the project's best features:
- ✅ Consume the Metrobus CDMX API for get an dataframe with information about the location of vehicles.
- ✅ Design the pipeline's architecture to data analysis of data open of Metrobus CDMX.
- ✅ Identify and create a data model and a ddl script for storage the processed data.
- ✅ Implement functions for load of processed data to the database.
- ✅ Desing and implement an API for get information about the location of vehicles.

## The process



### Creation of architecture

The first step to work on this project was creating an architecure to be implemented, in wich I separate in two parts:
- The **clients's part** that will consume all the information of our solution.
- The **Services part** which is going to be divided in 3:
  - A **GraphQL server** that is goint to have schema for the entities and it goint response to requests from front-end.
  - A **Database layer** to storage the proccesed data.
  - The **ETL layer** to download, proccess and load the data to data base.

![Creation of architecture](/docs/images/architecture.png)

### Identification of entities related to my solution
Once I decided how to work, I started to identify objects and attributes for the database.
- Vehicle
- City
- Ubication

<div align="center" id="container">

  ![Creation of architecture](/docs/images/entities_and_attributes.png)
  
</div>


**Why I put city and ubication in this abstraction:**
A location corresponds to a geographical point, but is associated with a city and additional information (street, neighborhood, number, state, country, etc). Creating a city entity allows us to avoid data duplication. In this project, geopy was used, a free python code library that allows to implement reverse geocoding to obtain the address given a geographic point. Geopy is not very precise with the city, but with the neighborhood, I store the neighborhood as a city. An alternative is to consume the Google Maps API, however a key is required.


### Interpretation of relationship between entities
Considering the problem statement and the data set, I was able to identify that a vehicle can have one or many locations. Likewise, a location is associated with only one city, but a city can have many locations.

<div align="center" id="container">
  
![Creation of architecture](/docs/images/relationship_between_entities.png)
   
</div>
  


## 🚀Getting Started


The application is built with this stack:
- [FastAPI](https://fastapi.tiangolo.com/) 
- [SqlAlchemy](https://www.sqlalchemy.org/)
- [Strawberry](https://strawberry.rocks/)



## Installation Steps:
### Clone repository
1.- Clone the repository

### 🚀 Run the project

1.- Open the project and navigate to functions directory using your terminal.

2.- Set values in .env (see file .env.example)

3.- Run `docker-compose up --build`

4.- Open browser and visit 127.0.0.1:8000/graphql



## Execute queries

### :mag: get available vehicles

```
  query getAvailableVehicles{
    getAvaibleVehicle{  
      id    
      label    
      currentStatus    
    }  
  }
```


### :mag: get location by vehicle id

```
  query getVehicleById{
    ubicationVehicleById(id:100){  
      id    
      latitude    
      longitude    
      city    
      {    
        name    
      }    
      vehicle    
      {     
        id      
        label      
        currentStatus
      }
    }
   }
```

### :mag: get available cities
```
query getAvailableCities{
  getAvailableCities{
    vehicle
    {
      id
      label
      currentStatus
    }
    city{
      id
      name
    }
  }
}
```


### :mag: get vehicles by city
```
query getVehiclesByCityId{
  getVehiclesByCity(id:10){
    vehicle
    {
      id
      label
      currentStatus
    }
  }
}
```


## Other queries
In adition, you can execute other queries. For example: 


### :mag: get all vehicles
```
query getVehicles{
	allVehicles{
    id
    label
    currentStatus
  }
}
```

### :mag: get vehicle by id

```
query getVehicleById {
  getVehicleById(id : 200){
    id
    label
    currentStatus
  }
}
```

### :mag: get all cities

```
query allCities{
  allCities{
    id
    name
  }
}
```


### :mag: get all locations
```
query allUbications{
  allUbications{
    id
    latitude
    longitude
    vehicle{
      id
      label
      currentStatus
    }
    city{
      id
      name
    }
  }
}
```


