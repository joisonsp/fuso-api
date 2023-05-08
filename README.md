# Desafio 2 - API

uma API em FastAPI com um endpoint que retorne o horario atual dos fusos horarios informados por parametro.

## Table of Contents

- **[Getting Started](#getting-started)**
  - [System Requirements](#system-requirements)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- **[Deployment](#deploying)**
  - [Deploy tools](#deploy-tools)
  - [Installing in Windows](#installing-in-windows)
  - [Installing in ubuntu](#installing-in-ubuntu)
  - [Deploying](#deploying)
  
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### System Requirements

* OS: Ubuntu 18.04.2 LTS or later
* OS: Windows 10 or later

### Prerequisites

Before starting the installation, you need to install some prerequisites:

[Python](https://www.python.org/downloads/)


### Installing

After installing all the prerequisites, install the project by running the command:

```sh
pip install -r requirements.txt
```

```sh
uvicorn main:app --reload
```

To test the installation [click here](http://localhost:8080/horario?fuso_horario=America/Sao_Paulo) to simply start the application in your browser

## Deployment

These instructions will get you a copy of the project up and running on a live System.

### Deploy Tools

To fully deployment of this project its necessary to have installed and configured the Docker Engine.

### Installing in Windows

[Docker](https://docs.docker.com/desktop/install/windows-install/)

### Installing in ubuntu

Update the apt package index:

```sh
sudo apt update
```

Install packages to allow apt to use a repository over HTTPS:

```sh
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

Add Docker’s official GPG key:

```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Use the following command to set up the stable repository:

```sh
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Update the apt package index:

```sh
sudo apt update
```

Install the latest version of Docker and containerd:

```sh
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

### Deploying

```sh
docker run -d --name desafio-joison -p 8080:80 joisonsp/desafio-joison
```