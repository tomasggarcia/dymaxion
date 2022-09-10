
## Run app
```bash
docker build -t dymaxion .
docker run -dp 8000:8000  --name dycontainer dymaxion
```


## Push to AWS ECR
```bash
export AWS_ACCESS_KEY_ID=****
export AWS_SECRET_ACCESS_KEY=****
docker build -t 085419913565.dkr.ecr.us-east-1.amazonaws.com/dymaxion_challenge .
docker push 085419913565.dkr.ecr.us-east-1.amazonaws.com/dymaxion_challenge
```
## Home url example
```bash
http://localhost:8000/home/email@test.com
```

## Chat url example
```bash
http://localhost:8000/chat/631c1a51bb9df9c1d383c867?email=email@test.com
```


## Create virtual environment

```bash
python3 -m venv venv
```

## Activate venv
```bash
. venv/bin/activate
```

## Freeze dependencies

```bash
pip freeze > requirements.txt
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Run project

```bash
uvicorn main:app --reload
```

