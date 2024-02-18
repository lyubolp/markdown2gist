venv:
    . .venv/bin/activate

init:
    python3 -m venv .venv
    venv
    pip install -r requirements.txt

lint: venv
    python3 -m pylint src/* main --fail-under 9
    mypy src main.py --ignore-missing-imports
    flake8 src main.py

test: venv
    python3 -m unittest discover -s tests

push: venv lint test
    git push

coverage: venv
    coverage run -m unittest discover -s tests
    coverage report -m --fail-under 75

run: venv
    python3 src/main.py