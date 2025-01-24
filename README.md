# WordSuggestor

WordSuggestor leverages n-gram models built from datasets to suggest words. Here’s a breakdown of its core logic:

- **N-gram Model**: The application uses an n-gram model to predict the next word based on the previous words. It is configurable, allowing users to change the value of `n` to experiment with different n-gram lengths.
- **Multi-language Support**: The model can handle multiple languages as long as the appropriate dataset is provided for each language.
- **Dynamic Updates**: There is an endpoint that allows new data to be added to the n-gram model, enabling it to learn and adapt over time.

## Project Structure


## Backend

The backend is built using Django. It contains the main application logic and manages word suggestions using n-grams.

### Setting Up the Backend

1. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
2. Navigate to the `backend` directory:
    ```sh
    cd backend
    ```
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```sh
    python manage.py makemigrations & python manage.py migrate
    ```
5. Run load_csv command for creating model:
    ```sh
    python manage.py loac_csv
    ```
6. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

## Frontend

The frontend is managed using npm and React. The `public` and `src` directories contain static assets and source files, respectively.

### Setting Up the Frontend

1. Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```
2. Install the required Node.js packages:
    ```sh
    npm install
    ```
3. Build the frontend assets:
    ```sh
    npm run build
    ```

## Running the Application

Once both the backend and frontend are set up, you can start the Django server and access the application at `http://localhost:3000`.

## Running Unit Tests

To run unit tests, use the following command:

```sh
cd backend
python manage.py test ngram.tests
```
## Video

[Video.webm](https://github.com/user-attachments/assets/b023ec2b-d612-450f-9a14-e6b70ac4bdae)
