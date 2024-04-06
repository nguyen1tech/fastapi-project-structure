# fastapi-project-structure

The template for FastAPI project

## Motivation

It's time consuming whenever I initialize a new FastAPI project. It would be great If there is a project template so when needed I can simply clone and get it running.

The project structure was inspired by: https://github.com/zhanymkanov/fastapi-best-practices

## How to

1. Set environment variables

   ```
   export PYTHONPATH="${PYTHONPATH}:app/"
   export PYTHONUNBUFFERED=1
   export HOST=0.0.0.0
   export PORT=8000
   ```

2. Start command

   ```
   uvicorn app.main:app --host ${HOST} --port ${PORT} --reload
   ```

## References:

- https://github.com/Longdh57/fastapi-base
- https://github.com/tiangolo/full-stack-fastapi-template
- https://github.com/mjhea0/awesome-fastapi?tab=readme-ov-file#boilerplate
- https://github.com/ets-labs/python-dependency-injector/blob/master/examples/miniapps/application-multiple-containers-runtime-overriding/example/__main__.py
- https://github.com/Blueswen/fastapi-observability
