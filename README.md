# :gear: B3-Web-Scrapping

<p align="center">
  
<img src="https://img.shields.io/badge/Python-00ADD8?style=for-the-badge&logo=go&logoColor=white">
<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white">

</p>


## :white_check_mark: About
Application ready to deploy to Google App Engine Standard Environment to daily get all B3 transactions and save it to Google Cloud Storage (GCS).

| <!-- --> | <!-- --> | 
--------------- |  ---------------
First Launch:   | **2021-09-11**    
Last Revision:  | **2021-09-11**    
Version:        | **1.0**

## :white_check_mark: Features

- [x] Daily get all B3 transactions
- [x] Cron job to automate execute the application every day at the same hour
- [x] Cloud build file with needed steps to automate deploy the application and the cron job  

## :white_check_mark: Pendency

- [ ] Modify the cron to not execute the application on holidays

## :white_check_mark: How it works

This is an application to daily collect all transactions that happen on brazilian stock market. In Brazil the organization that centralizes all those transactions is B3. The periodicity of this application is given on cron.yaml file, where is set to only execute the application on working days (from monday to friday) at 10PM using Sao Paulo timezone. This application was created initially to be executed on Google Cloud Platform (GCP), using Google App Engine (GAE) and to save all the transactions on a bucket on Google Cloud Storage (GCS).

## :white_check_mark: Project Structure

    .
    ├── bolsa-web-scraping                     
    │   ├── __init__.py
    │   ├── main.py
    │   ├── utils.py
    │   ├── app.yaml
    │   ├── cron.yaml
    │   ├── cloudbuild.yaml
    │   ├── requirements.txt
    │   ├── test
    |   |   └── __init__.py     
    |   |   └── main_test.py   
    |   |   └── utils_test.py  
    |   |   └── requirements-test.py  
    └── ...
