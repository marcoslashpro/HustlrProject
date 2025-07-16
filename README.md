# Hustlr Project

Hello Hustlr Team! I am so excited for you to be here and giving me a shot!

Let's jump straight into the application.

## Tech Stack
The stack used in this project is:
- `Python`: The programming language of choice,
- `FastAPI`: As the framework used to build the RESTfulAPI;
- `Pydantic`: As the Data validation model, used in combination with `FastAPI` it significantly streamlines the process of authenticating both data sent from the user and fetched from databases.
- `SQLAlchemy`: As the Database management system of choice. `SQLAlchemy` makes very easy to setup and spin a database with very few lines of code, allowing us to create stable connections and sessions in a breeze.

## How to run the project
I suggest using `uv` as the package manager as it benchmarked to be **10x to 100x** fater than PIP and makes the entire project management process super easy, from start to end, but every step here can be also done using PIP.
1. Clone the repo and cd into it:
```
git clone https://github.com/marcoslashpro/HustlrProject.git && cd HustlrProject
```
2. Install dependencies
```
uv sync
```
3. Run the server
```
uv run uvicorn src.main:app --reload
```

## How to use it(And Docs)
The API comes with a couple of sample data within the database. Those can be used in order to try different features of the API.

After spinning up the server, you can access the localhost at `http://127.0.0.1:8000`, where you will see a health check message.
In order to access the documenttion please go to `http://127.0.0.1:8000/docs` after having spun the server.

Get/Post request can all be done from the swagger UI found at `http://127.0.0.1:8000/docs`, but in order to send request through the terminal is sufficient to send the curl request to the local host + the proxy specified in the test document, e.g.
```
curl -X GET "http://127.0.0.1:8000/products
```

The given items in the database are:
```
{
  "price": 100,
  "n_items_in_stock": 10,
  "category": "Tech",
  "name": "Monitor",
  "id": "81cd6b02-b7f1-47d7-982a-161f29fe1307"
}
{
  "price": 90,
  "n_items_in_stock": 900,
  "category": "Clothes",
  "name": "Air Max 90",
  "id": "67be6eca-e32d-47b8-a797-d19dfc898281"
}
{
  "price": 150,
  "n_items_in_stock": 200,
  "category": "Hobbies",
  "name": "Acoustic Guitar",
  "id": "67be6eca-e32d-47b8-a797-d19dfc897408"
}
```

As we can see each item in the database has the following fields:
- `price`: int,
- `n_items_in_stock`: int, the number of the items still available in stock, this would be a synamic column in te databse to update after each purchase,
- `name`: string,
- `category`: string, the category of which the item is part.

Have fun!
