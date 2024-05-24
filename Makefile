.PHONY: all install format lint security run-scripts clean streamlit

VENV := venv

install: 
	@echo "Installing requirements..."
		python3.10 -m venv $(VENV) && \
		source venv/bin/activate && \
		pip install -r requirements.txt

format:
	@echo "Running Python scripts..."
	black inference.py
	black test.py

lint:
	@echo "Running Python scripts..."
	flake8 inference.py --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 test.py --count --select=E9,F63,F7,F82 --show-source --statistics

security:
	@echo "Running Python scripts..."
	bandit inference.py
	bandit test.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

run: 
	python inference.py model/water_potability.pkl scaler/scaler.pkl data/test_data_water_potability.csv

test: 
	python test.py data/groundtruth.csv


all: install format lint security clean run
