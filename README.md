# Survey

Small and simple survey tool for API testing. Created for some tests with AEM Forms.


## Dependencies

pip install "fastapi[all]"
pip install tinydb
pip install pandas

## run

uvicorn main:app --reload 

## swagger

http://127.0.0.1:8000/docs

## Openapi

http://127.0.0.1:8000/openapi.json

This file is not working in AEM as a Forms Datasource. 402 responses and Validation schemas have to be removed. A fixed and static version is [here](openapi.json). 






