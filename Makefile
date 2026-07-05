install:
	pip install -r requirements.txt

run:
	python bot.py

lint:
	python -m compileall .
