BKL Project
---
Login REST API
- Sign up
- Sign in
- Sign out
- Search user info
- Search user detail
- Create JWT
- Validate JWT
- Refresh JWT
- User Login Block

Structure of repo
---

The repository is laid out in the following structure

```markdown
├── controllers - Contains API Controllers (Router)
│   ├── __init__.py
│   └── ..
├── models - Contains Model file 
│   ├── __init__.py
│   └── ..
├── services - Contains Business Logic 
│   ├── __init__.py
│   └── ..
├── swagger - Contains swagger yaml files
│   └── index.yaml
├── utils - Contains Util file use in only this project
│   ├── __init__.py
│   └── ..
├── validators - Contains Validate file when using body, parameters validate
│   ├── __init__.py
│   └── ..
├── application.py - Contains the entry point for the Flask app
├── requirements.txt - Project Package files
├── .gitignore - Files that shouldn't be committed by Git
├── Dockerfile
├── docker-compose.yaml
├── 00_build.sh 
└── README.md
```

Gettting Started
---
Pre-requisites

- Python3
- Docker version 19.03.8 / Docker CLI
- pip3
- redis
- mongoDB (v4.2.8)

Quick Start
---
```shell script

# pwd : ~~/BKL

# start flask application / mongo db / redis
$ sh start.sh

# attach docker shell
$ docker exec -it flask_application bash

# after build docker-compose
$ cd swagger

# install dependencies
$ npm install 

# start swagger server
$ node index.js

# swagger server = http://127.0.0.1/3031/docs
```
