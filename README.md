# Note from author
It is a very simple approach to fulfill assignment requirements. We are using fastAPI because of its async nature. Docker compose is here in case we want to extend that demo and add other services like database. Pre-commit keeps code cleaner.

Extension: 
+ additional endpoint was added: `/pings`  which can accpet a list of URLs 


# Build with Docker

Make sure that you have a docker installed on your machine if not please visit: https://docs.docker.com/get-docker/  
After cloning repo enter root dir:  
```bash
cd assignemnt/
```
run docker:
```bash
docker-compose up --build
```
note: you can use `-d` swich to start in deamon mode

# How to play

Just enter http://localhost:8001/docs to play with API  

or visit main page: http://localhost:8001/

# Run test

We can run tests locally, firstly we need to build a local environment using pipenv.

```bash
pipenv shell
pipenv install --dev
pytest .
```

# Style guidelince

* It is strongly recomended to follow: https://google.github.io/styleguide/pyguide.html
* Use `black` for code formating: https://github.com/psf/black

