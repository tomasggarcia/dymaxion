## Home url
```bash
http://localhost:8000/home?email=email@test.com
```

## Chat url
```bash
http://localhost:8000/chat?email=algo@gmail.com
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

