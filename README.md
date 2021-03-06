# Movie-Recommeder-System-Deployment
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

The aim of this project is to generate a content-based movie recommender system for 5000 movies on tmdb dataset obtained from kaggle.

### Dataset
You can find the dataset [here.](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

• This repository consists of files required for end to end implementation of Movie recommender system ___Machine Learning Web App___ created with ___Streamlit___ on ___Heroku___ platform.

## setup
- Clone the repository : https://github.com/ni3choudhary/Movie-Recommeder-System-Deployment.git
- Inside the project root directory, Create Python Virtual Environment and activate it using below commands 
```console
$ python3 -m venv env
``` 

Activate Virtual Environment
```console
$ .env/bin/activate 
          OR
$ .\env\Scripts\activate
```
Install Libraries using below command
```console
$ pip install -r requirements.txt
```
Generate an API key from tmdb website and then create a .env file in root directory with below details.
```console
API_KEY = "Your-API-Key"
```
- Run jupyter notebook to get the pickle files

- Run app.py on terminal to start local server.
```console
$ streamlit run app.py
```

• If you want to view the deployed model, click on the following link: Deployed at: https://movie-recommeder-ni3.herokuapp.com/

• Please do ⭐ the repository, if it helped you in anyway.

