# Introduction
This projects was first elaborated in the scope of a project with Mines Paris PSL - University in partnership with [AccroHome](https://accrohome.fr/). Then I have completed this project to build a streamlit app.

The goal of the project is to predict the price of flats in Paris.
The analysis is based on all the transactions in Paris between 2017 and 2022.

It could be used for both buyers and sellers to find out the price of an accommodation before considering buying or selling it.

# Table of contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Commit Policy](#commit-policy)

# Dataset

All the transactions on the housing market in France are available [here](https://files.data.gouv.fr/geo-dvf/latest/csv/).
For more information on the dataset, you can consult this [link](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/#description).

This project uses all the housing transactions from 2017 to 2022. This dataset includes the localization of the accomodation and information about the transactions.

This project uses only the most relevent features of the government's dataset:
- Transaction cost
- Transaction date
- Built surface
- Number of rooms
- Longitude
- Latitude

And other additional features:
- District 
- Delta days: number of days since the first transaction in the dataset

# Installation

To use this project, first clone the repo on your device using the command below:
```
git clone git@github.com:CyprienBouton/HousingPriceAnalysis.git
```
After creating and activating a virtual environment, install the required libraries:
```
pip3 install -r requirements.txt
```
Then, you can install the model on your local machine using:
```
py model.py
``` 

# Usage

This project is an app which could be used to predict the price of flats or to visualize 
the housing market in Paris.
To launch the app click [here](https://cyprienbouton-housingpriceanalysis-app-ilt2rx.streamlit.app/)

To predict the price of flats you can either use the model downloaded above or use your own model.

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

Feel free to fork this repository and suggest a pull request if you respect the above commit policy.