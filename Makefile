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


lint:
	@echo "Running Python scripts..."
	flake8 inference.py

security:
	@echo "Running Python scripts..."
	bandit inference.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

run: 
	python inference.py model/water-potability.pkl scaler/scaler.pkl data/test_data_water_potability.csv

all: install format lint security clean run
