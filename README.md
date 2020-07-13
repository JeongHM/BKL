BKL Project
---
This is Login REST API

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