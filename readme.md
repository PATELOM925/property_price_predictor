# Property Price Predictor

This is a Flask-based web application for predicting property prices of Vadodara City based on features such as area, number of bedrooms, bathrooms, and location.

## Live Application

- [Property Price Predictor](https://property-price-predictor-onxd.onrender.com/)

## Features

- Predict property prices for Vadodara City.
- Future price estimation is based on the years ahead.

## Technology Stack

- Python 3
- Machine learning algorithm
- Data Analysis
- Flask
- Gunicorn
- Render.com for deployment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PATELOM925/property_price_predictor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd property_price_predictor
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

To run the application locally:

```bash
gunicorn app:app
```

This will start the application on `http://localhost:5000`.

## Deployment

The application is deployed on Render.com. Access it at [Property Price Predictor](https://property-price-predictor-onxd.onrender.com/).

## Usage

1. Enter property details such as area, number of bedrooms, bathrooms, and location.
2. Click **Predict Price**.
3. View the current and future estimated property prices.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.

## Contact
Developed by [@SnehSolanki](https://github.com/snehsolanki1583)
