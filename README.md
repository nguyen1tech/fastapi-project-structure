# fastapi-project-structure

The template for FastAPI project

export PYTHONPATH="${PYTHONPATH}:app/"
export PYTHONUNBUFFERED=1
export HOST=0.0.0.0
export PORT=8000

uvicorn app.main:app --host ${HOST} --port ${PORT} --reload

# List of example repos:

1. https://github.com/Longdh57/fastapi-base
2. https://github.com/tiangolo/full-stack-fastapi-template
3. https://github.com/mjhea0/awesome-fastapi?tab=readme-ov-file#boilerplate
4. https://github.com/ets-labs/python-dependency-injector/blob/master/examples/miniapps/application-multiple-containers-runtime-overriding/example/__main__.py
5. https://github.com/Blueswen/fastapi-observability
