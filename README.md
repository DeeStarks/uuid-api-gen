# UUID API

A simple API that randomly generates UUID and returns a key-value pair, with the key as a timestamp and a UUID as value. Whenever the API is called, it returns all previously generated UUIDs alongside a new UUID

## Setup
- `mkdir uuid-api`
- `cd uuid-api && pipenv shell` to create a virtual environment. Note: You can also use your preferred virtual environment manager.
- Clone repo: `git clone https://github.com/DeeStarks/uuid-api-gen.git`
- `cd uuid_api`
- `pip install -r requirements.txt`
- `python manage.py runserver`

## Example

```bash
$ curl -X GET http://localhost:8000/uuid/
{
    "2022-02-03T14:13:14.805790Z": "a2086226ee764258be744fbb9c3b6645",
    "2022-02-03T14:14:32.279086Z": "0cce77ce5a46408a894e3c9e2f122161",
    "2022-02-03T14:27:43.240245Z": "00fb5436603649afbb051575032b2e74"
}
```