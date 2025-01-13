# Project Name: Multiple-Container

This project is a template for multi-container applications using Docker Compose. It can run a Flask backend, a PostgreSQL database, pgAdmin and Nginx (as a reverse proxy) containers. 

Also if you want GUI for the PostgreSQL database, you can use pgAdmin. Which is running as a container service. In the container network, you can access the pgAdmin GUI by typing `http://localhost:6010` in your browser.


## Prerequisites

- Python 3.7 or higher
- Docker extension for Visual Studio Code
- Docker Engine (We have tried using Docker Desktop for Windows)

## Installation and Running the project

1. Clone the repository:

```bash
git clone https://github.com/bahshat/Multiple-Containers.git
cd Multiple-Containers
code . # Open the project in Visual Studio Code
```

2. How to run:
Right click on the docker-compose.yml file and click on "Docker Compose Up"


