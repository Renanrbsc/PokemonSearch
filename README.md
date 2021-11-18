-------------------------------------------
# PokemonSearch
-------------------------------------------

Repository for system development that gathers information from Pokemon and Trainers contained in the animation, which can be accessed via API and Web with FastAPI.

Back-End developed using Python language, using a framework FastAPI, contains 'MONGODB' for database.

Front-End developed through the FastAPI framework.

The application returns a CRUD system that gathers information from Pokémon and trainers contained in the animation. We can view approximately 809 Pokemons that have been obtained through data cleaning.

-------------------------------------------
# Steps to start
-------------------------------------------

install mongodb

1: pip install virtualenv
2: virtualenv env
3: \env\Scripts\activate
4: pip install -r requirements.txt
5: python app/main.py

-------------------------------------------
# Project Structure
-------------------------------------------

├── app
│   │
│   └── routes
│   │   └── routes
│   └── server
│   │   ├── __init__.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   └── data.py
│   │   │   └── connection.py
│   │   └── domains
│   │       ├── __init__.py
│   │       └── pokemon
│   │           ├── __init__.py
│   │           └── actions.py
│   │           └── models.py
│   │           └── routes.py
│   └── static
│   │   └── images
│   │   └── js
│   │   └── style
│   └── templates
│   └── utils
│   │   ├── __init__.py
│   │   └── convert_txt.py
│   ├── __init__.py
│   └── main.py
└── env
└── README.md          <- you're here
└── requirements.txt

-------------------------------------------