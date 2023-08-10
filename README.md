# Motivational Quote API

Welcome to the Motivational Quote API, built with FastAPI! This API provides inspirational and motivational quotes to uplift your spirits. Whether you're looking for a full quote with formatting or just the quote itself, this API has you covered.

## Endpoints

### `/`

- Method: `GET`
- Description: Root endpoint that returns a simple greeting indicating the presence of the Motivational Quote API.
- Example Response:
  Motivational API

### `/quote`

- Method: `GET`
- Description: Returns a random motivational quote along with its author and an HTML-formatted version of the quote.
- Example Response:

```json
{
  "quote": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
  "author": "Christian D. Larson",
  "html_quote": "<blockquote>&ldquo;Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.&rdquo;<br>- Christian D. Larson</blockquote>"
}
```

### '/quote/single'

- Method: GET
- Description: Returns a random motivational quote without the author and HTML formatting.
- Example Response:

```json
{
  "quote": "The only way to do great work is to love what you do."
}
```

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using 'pip':

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the project directory.
2. Run the FastAPI application using the following command:

```bash
uvicorn main:app --reload
```

3. Access the API endpoints in your browser or using tools like curl or Postman.

## Credits

- This API is built using the [FastAPI](https://fastapi.tiangolo.com/) framework.
- Quotes are sourced from various motivational sources.

## License

This project is licensed under the MIT License [MIT LICENSE](LICENSE) - see the LICENSE file for details.
