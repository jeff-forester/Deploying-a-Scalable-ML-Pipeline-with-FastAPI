Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up (pip or conda)
* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip
    
## Repositories
* Create a directory for the project and initialize git.
    * As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.
    * Make sure you set up the GitHub Action to have the same version of Python as you used in development.

# Data
* Download census.csv and commit it to dvc.
* This data is messy, try to open it in pandas and see what you get.
* To clean it, use your favorite text editor to remove all spaces.

# Model
* Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data.
    * Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
* Write a model card using the provided template.

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST that does model inference.

# Submission Details

GitHub Repository:
https://github.com/jeff-forester/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

The project trains a Random Forest classifier using the Census Income dataset and deploys the model using FastAPI.

The API includes:
* A GET endpoint at `/` that returns a welcome message.
* A POST endpoint at `/data/` that performs model inference.

The trained model achieved:
* Precision: 0.7353
* Recall: 0.6378
* F1 Score: 0.6831

The repository also includes:
* Unit tests for the machine learning functions.
* Slice-based model performance results in `slice_output.txt`.
* A completed `model_card.md`.
* GitHub Actions continuous integration using Python 3.10, pytest, and flake8.
* Screenshots for unit testing, local API testing, and continuous integration.
