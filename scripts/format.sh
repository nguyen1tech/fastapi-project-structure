#!/bin/sh -e
set -x

ruff check --fix app
ruff format app