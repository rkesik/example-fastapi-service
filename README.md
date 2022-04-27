## Note
It is a very simple approach to fulfill assignment requirements.

We are using `fastAPI` because of its async nature which for task of getting other page contents. Docker compose is here in case we would like to add other services e.g database. Pre-commit keeps code cleaner.  
  
A litte bit more:   
+ Additional a new endpoint was added: `/pings`  which can accpet a list of URLs  

To play with project (after sucesfull setup) visit  http://localhost:8001/docs  in a browser.


## Setup

Using a docker build is recomended way to setup project.  

### Build with Docker

Make sure that you have docker installed on your machine if not please read: https://docs.docker.com/get-docker/    

After cloning repo enter root dir and build docker:
```bash
cd cisco-assignemnt/
docker-compose up --build
```

Note: you can use `-d` swich to start in deamon mode

### Locally (without docker)

```bash
cd cisco-assignemnt/
pipenv shell
pipenv install
python3 app/main.py
```


## Run test

We can run tests locally, firstly we need to build a local environment using pipenv.

```bash
cd cisco-assignemnt/
pipenv shell
pipenv install --dev
pytest .
```

## Important

* It is strongly recomended to follow: https://google.github.io/styleguide/pyguide.html
* Use `black` for code formating: https://github.com/psf/black
* It is strongly recomended to utilize pre-commit (to save our CI/CD resources) that should prevent us from seeing "pip-fix" changes.

## Next steps:
+ add MongoDb support to store results (useing Motor client would make most of sense)
+ add more tests with `aioresposnes`
