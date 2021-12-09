test:
	python -m pytest

mypy:
	python -m mypy .

flake:
	python -m flake8 --max-line-length=120

quality: mypy flake

run:
	cd advent2021 && python day_$$day.py