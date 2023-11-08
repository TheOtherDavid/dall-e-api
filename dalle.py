import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ['API_KEY'])

response = client.images.generate(
  model="dall-e-3",
  prompt="A watercolor painting of a bear in the snow, huddling around a fire.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)