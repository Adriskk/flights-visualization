# Flight Visualization

### Find aircrafts above your head


**Adison#5555** submission for **Timathon 2021 (Mar-Apr)** - [vote for me](#)

An application which shows the current USA map with
thousands of aircrafts markers, containing some features regarding to planes. 



## Features
1. [Separate data for each aircraft]()
2. [Saving map ready for any use]()
3. [Get the exact position of clicked plane]()
4. [Calculate the aircrafts aggregate on map using Machine Learning]()



## Installation
Project uses the OpenSky API
You can easily download and set it up when following the instructions
on [this repository](https://github.com/openskynetwork/opensky-api).

You need to install the modules from **requirements.txt** file too.
You can do it by typing the following command in cmd console:

```bash
cd flights-visualization
pip install -r requirements.txt
```
or 

```bash
cd flights-visualization
pip3 install -requirements.txt
```



## Setup
API uses an account to eliminate request limitations.
You can use yours created [here](https://opensky-network.org/my-opensky/profile/profile) or default set in **config.ini** file.



## About
Move on the map and discover aircrafts nearby. By clicking on the plane marker you can learn more about clicked
plane like current position, speed, update time and heading direction. App uses K-Means Machine Learning algorithm to find the aggregate of 
aircrafts on the map. 

---
* You can change the colors of the map to dark by clicking ```Change colors``` button - and to white by clicking the same
* To refresh the map click ```Refresh```
* Save map by clicking the ```Save map``` button

---
![Application](https://user-images.githubusercontent.com/65545676/111904476-80042b00-8a47-11eb-9d10-f22b41ec8603.png)
