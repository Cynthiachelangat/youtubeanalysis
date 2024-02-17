import google.auth
from googleapiclient.discovery import build

# Replace with your API key
api_key = 'AIzaSyAfVIvO9G1pN74uaFePoo92sNO_dYwlif8'

# Replace with the desired region code
region_code = 'KE'

# Set up the YouTube client
youtube = build('youtube', 'v3', developerKey=api_key)

# Get all channels in the specified region and country
request = youtube.search().list(
    part='snippet',
    type='channel',
    regionCode=region_code,
    maxResults=50  # You can adjust this number based on your needs
)
response = request.execute()

# Extract channel IDs
channel_ids = [item['id']['channelId'] for item in response.get('items', [])]

# Retrieve channel statistics for each channel
channels_info = []
for channel_id in channel_ids:
    channel_request = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id
    )
    channel_response = channel_request.execute()
    channels_info.append(channel_response['items'][0])

# Sort the channels based on subscriber count
sorted_channels = sorted(channels_info, key=lambda x: int(x['statistics']['subscriberCount']), reverse=True)

# Extract top 5 channels
top_5_channels = sorted_channels[:5]

# Print the top 5 channels
print(f"Top 5 YouTube channels in {region_code} based on subscriber count:")
for i, channel_info in enumerate(top_5_channels, start=1):
    channel_title = channel_info['snippet']['title']
    total_subscribers = channel_info['statistics']['subscriberCount']
    channel_id = channel_info['id']
    channel_link = f"https://www.youtube.com/channel/{channel_id}"
    print(f"{i}. Channel: {channel_title} | Subscribers: {total_subscribers} | Channel Link: {channel_link}")
