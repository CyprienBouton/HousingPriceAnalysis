# HousePricingAnalysis
The goal of the project is to predict the price of a flat in Paris.
The analysis is based on all the transactions in Paris between 2017 and 2022.

It could be use for both buyers and sellers, to know the price of an accomodation before consedering to buy or sell it.

# Table of contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Commit Policy](#commit-policy)

# Dataset

All the transactions on the housing market in France are available here https://files.data.gouv.fr/geo-dvf/latest/csv/
<br/>For more information on the dataset consult the following link https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/#description

This project use all the housing transactions from 2017 to 2022. This dataset includes the localization of the accomodation and information about the transaction.

This project use only the most relevent features of the government's dataset:
- Transaction cost
- Transaction date
- Built surface
- Number of rooms
- Longitude
- Latitude

And other additional features:
- District 
- Delta days The number of days since the first transaction of the dataset

# Installation

To use this project, first clone the repo on your device using the command below:
```
git clone git@github.com:CyprienBouton/HousePricingAnalysis.git
```
After creating and activating a virtual environment, install libraries needed:
```
pip3 install -r requirements.txt
```
Install the model on your local machine using:
```
python model.py
``` 

# Usage

This project is an app which could be use to predict the price of a flat or to visualize 
the housing market in Paris.
To launch the app
https://cyprienbouton-housepricinganalysis-app-mzrf4h.streamlit.app/
To predict the price of flats you can also use your own model

# Development

Development flow:
- Cleaning the dataset **prepare_data.py**
- Creating and trainning a Random Forest model using sklearn **model.py**
- Building a streamlit app **app.py** using 4 pages in the folder **markdown/**

# Commit Policy

Please, respect the following commit policy:
```
[START]     first commit describing the branch you created
[ADD]       commit describing new elements or functionalities
[UP]        commit describing elements or functionalities updated
[FIX]       commit describing the error and how it has been fixed
[DEL]       commit describing elements or functionalities deleted
[PR]        pull request
```