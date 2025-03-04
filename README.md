## Project Overview
    
### The project consists of:

### Games:
- Memory Game
- Guess Game
- Currency Roulette Game

### Score Service:
- A Flask app that serves and validates scores.

### Jenkins Pipeline:
- Automates testing and deployment.

---
## Features

### Games:
- #### Interactive command-line games.
- #### Scores are saved and validated by the Flask score service.
### Score Service:
- #### Flask app to serve and validate scores.
- #### Endpoint to retrieve the current score.
### Jenkins Integration:
- #### Automated testing of the score service.
- #### Dockerized environment for consistent testing.
---
## File Structure
```
.
├── .gitignore               # Git ignore file
├── Dockerfile               # Docker configuration
├── Jenkinsfile              # Jenkins pipeline configuration
├── README.md                # Project documentation
├── app.py                   # Main Flask application
├── currency_roulette_game.py # Currency Roulette Game
├── docker-compose.yml       # Docker Compose configuration
├── guess_game.py            # Guess Game
├── main.py                  # Entry point for the games
├── main_score.py            # Flask score service entry point
├── memory_game.py           # Memory Game
├── requirements.txt         # Python dependencies
├── score.py                 # Score-related logic
├── utils.py                 # Utility functions
├── tests/                   # End-to-end tests
│   └── e2e.py               # End-to-end test script
└── templates/               # HTML templates
    └── score.html           # Score html page template
    └── error.html           # Error html page template

```