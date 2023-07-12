# Survey

Small and simple survey tool for API testing. Created for some tests with AEM Forms.

## Dependencies

```
pip install "fastapi[all]"
pip install tinydb
pip install pandas

pip install -U fastapi==0.98.0
```

## run

```
source ./.venvs/bin/activate
uvicorn main:app --reload  --host localhost --port 8000
```

## swagger

http://localhost:8000/docs

## Openapi

http://localhost:8000/openapi.json

This file is not working in AEM as a Forms Datasource. Some issues withe the validation schema. 402 responses and Validation schemas have to be removed: 

### Static Swagger file for AEM

```
api-spec-converter --from=openapi_3 --to=swagger_2 --syntax=json --order=alpha http://localhost:8000/openapi.json > static/swagger.json

json -I -f static/swagger.json -e "this.definitions.HTTPValidationError={}"
json -I -f static/swagger.json -e "this.definitions.ValidationError={}"
```

#### Requirements

```
npm install -g api-spec-converter
npm install -g json
```

https://github.com/LucyBot-Inc/api-spec-converter

