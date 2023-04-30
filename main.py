import os
import datetime
import requests

def main(mytimer: func.TimerRequest) -> None:
    # Call API and get data
    response = requests.get(os.environ['API_URL'])
    data = response.json()

    # Create notification content
    now = datetime.datetime.now()
    message = f"Daily report for {now.strftime('%m/%d/%Y')}:\n\n{data}"

    # Send notification to Discord
    payload = {
        "content": message
    }
    response = requests.post(os.environ['DISCORD_WEBHOOK_URL'], json=payload)
    print(response.status_code)
    
    
