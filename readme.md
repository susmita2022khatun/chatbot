# Negotiation Chat Application

This project implements a negotiation chat application using FastAPI and a simple negotiation logic model. The application allows users to simulate negotiations with a seller based on their offers for products, providing feedback and suggestions for improvement.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Negotiation Logic](#negotiation-logic)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Sample output](#Sample-output)

## Features

- Interactive chat interface for negotiation.
- Users can input offers for products (e.g., Laptop and Warranty).
- The application provides feedback on offers and seller proposals.
- Accept and decline buttons for managing negotiation outcomes.
- Integration with a conversational AI model for realistic interactions.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python.
- **Jinja2**: A templating engine for rendering HTML pages.
- **HTML/CSS**: For structuring and styling the web application.
- **Hugging Face Transformers**: For integrating a conversational AI model (optional).

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your_username/negotiation-chat.git
   cd negotiation-chat
    ```
2. **Create a Virtual Environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Required Packages:**

    Make sure you have pip installed, then run:

    ```bash
    pip install fastapi uvicorn jinja2
    ```

    
    If you're using the Hugging Face model, you may also need to install:

    ```bash
    pip install transformers torch
    ```
4. **Directory Structure:**

    Ensure you have the following directory structure:

    ```arduino
    negotiation-chat/
    ├── main.py
    ├── negotiation.py
    ├── templates/
    │   └── index.html
    └── static/
        └── style.css
    ```
5. **Run the Application:**

    Start the FastAPI server with the following command:

    ```bash
    uvicorn main:app --reload
    ```
    Your application will be available at `http://127.0.0.1:8000`.

## Negotiation Logic

The negotiation model is based on a simple framework that simulates the negotiation process between a buyer and a seller. The following components are included:

- **Products**: The items being negotiated (e.g., Laptop and Warranty).

- **Reservation Values**: Each product has a minimum and maximum price, defined as a tuple (min_value, max_value).

- **Weights**: Each product is assigned a weight that reflects its importance in the negotiation.

- **Concession Speed**: Determines how quickly the seller will adjust their offers over multiple rounds.

- **Negotiation Rounds**: The process consists of several rounds where the buyer submits offers, and the seller responds with counter-offers.

### Key Methods

- **Kt**: Computes a factor for adjusting the seller's proposals based on the current round.

- **seller_proposal**: Generates a seller's offer based on the buyer's last offer.

- **compute_score**: Evaluates the buyer's and seller's offers against the reservation values and weights.

- **negotiate**: Main method that processes the buyer's offer, generates a seller's proposal, and provides feedback based on scores.

### Usage

- Open your web browser and navigate to http://127.0.0.1:8000.

- Input your offers for the products in the designated fields.

- Click the Submit Offer button to send your offer to the seller.

- Review the chat box for feedback and suggestions based on your offer.

- Optionally, click the Accept or Decline buttons to manage the negotiation outcome (implement logic as needed).

## Project Structure

- `main.py`: Contains the FastAPI application and routes.
- `negotiation.py`: Defines the Negotiation class and related logic for processing offers and generating responses.
- `templates/`: Directory containing HTML templates.
- `index.html`: Main HTML file for rendering the negotiation interface.
- `static/`: Directory for CSS and static files.
- `style.css`: Styles for the application interface.

## Sample output

```yaml
Negotiation Chat

Round 1:
  Seller offer: {0: 800, 1: 150}
  Your offer: [750, 100], Score: 0.6
  Seller offer: {0: 800, 1: 150}, Score: 0.75
  You might want to increase your offer.

Round 2:
  Seller offer: {0: 780, 1: 140}
  Your offer: [800, 120], Score: 0.8
  Seller offer: {0: 780, 1: 140}, Score: 0.7
  Your offer is good, consider keeping it or slightly increasing it.

AI: Thank you for your offer! Let’s see how we can reach a favorable agreement.

```