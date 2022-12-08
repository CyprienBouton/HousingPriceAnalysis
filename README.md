# HousePricingAnalysis
The goal of the project is to predict the price of a flat in Paris.
The analysis is based on all the transactions in Paris between 2017 and 2022.

It could be use for both buyers and sellers, to know the price of an accomodation before consedering to buy or sell it.

# Table of contents

- [Dataset]
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Development]
- [Commit Policy](#commit-policy)

# Dataset

All the transactions on the housing market in France are available here https://files.data.gouv.fr/geo-dvf/latest/csv/

# Installation

To use this project, first clone the repo on your device using the command below:
```
git clone git@github.com:19bouton/HousePricingAnalysis.git
```
Then run the following comand to install libraries needed:
```
pip3 install -r requirements.txt
```
Install the model on your local environment using:
'''
python model.py
''' 

# Quit Start

The report is a streamlit app which can be run with the following command line:
```
streamlit run app.py
```

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