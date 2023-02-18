import requests
import os
import json

# Set OpenAI API key from environment variable
openai_token = os.environ["OPENAI_API_KEY"]

# Set API request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {openai_token}'
}

# Set model and API parameters
model = "text-davinci-003"
max_tokens = 4000
temperature = 1.0

# Main loop
while True:
    # Get input from user
    input_text = input("You: ")

    # Set API request body
    body = {
        "prompt": input_text,
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    # Convert body to JSON
    jsonBody = json.dumps(body)

    # Send API request and capture response
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers=headers,
        data=jsonBody
    )

    # Check if API request was successful
    if response.status_code == 200:
        # Extract response text from JSON
        output_text = response.json()["choices"][0]["text"]
        print("AI: " + output_text)
    else:
        print("API request failed with status code", response.status_code)
