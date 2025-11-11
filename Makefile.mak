PYTHON = python

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -r requirements-dev.txt

train:
	$(PYTHON) train.py

serve:
	uvicorn app:app --reload

test:
	pytest --cov=. --cov-report=xml --cov-report=term-missing

pytest:
	pytest --maxfail=1 --disable-warnings -q

format:
	black .
	isort .

lint:
	flake8 .

typecheck:
	mypy .

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache models/*.pkl
