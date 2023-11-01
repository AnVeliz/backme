VENV_NAME = .backme_venv

.PHONY: setup install lint run clean

setup:
	python3 -m venv $(VENV_NAME)

install: setup
	@echo "Installing Poetry within the virtual environment..."
	@. ./$(VENV_NAME)/bin/activate && pip install poetry

	@echo "Installing project dependencies..."
	@. ./$(VENV_NAME)/bin/activate && poetry install

lint: install
	@echo "Running linter..."
	@. ./$(VENV_NAME)/bin/activate && poetry run flake8 ./backme/

run: install
	@echo "Running the script..."
	@. ./$(VENV_NAME)/bin/activate && poetry run python ./backme/archiver.py $(ARGS)

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)
