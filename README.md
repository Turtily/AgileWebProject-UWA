# Agile Web Development Project - UWA

## Setup
  * Clone repo to your local directory: **git clone https://github.com/systemvaz/AgileWebProject-UWA.git**
  * From within local repo directory, create new python virtual environment **venv**.
  * Activate virtual environment.
  * With virtual environment activated, install dependencies: **pip install -r requirements.txt**

## Run
  * No need to set environmental variables. Already defined in .flaskenv
  * Command: flask run

## Maintenance
  * .gitignore will prevent git from pushing dependencies in virtual environment **venv**, python cache files or .vscode settings
  * use the following to add pip installed dependencies to the requirements file instead: **pip freeze requirements.txt**
