.PHONY: help install test run clean lint

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make install-dev - Install dev dependencies"
	@echo "  make test       - Run tests"
	@echo "  make run        - Run speed test"
	@echo "  make clean      - Remove cache files"
	@echo "  make lint       - Check code style"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt -r requirements-dev.txt

test:
	python -m pytest tests/ -v

run:
	python speedtest_cli.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf build dist *.egg-info

lint:
	python -m py_compile speedtest_cli.py
