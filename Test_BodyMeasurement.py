# install Package
# pip install shakuapi

#import
from shakuapi import ShakuClient

client = ShakuClient(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")

# login
client.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")

# get size measurement
result = client.size_measurement(
    present_height=YOUR_HEIGHT,
    img_full_view_body="full_view.jpg",
    img_side_view_body="side_view.jpg"
)

print(result)