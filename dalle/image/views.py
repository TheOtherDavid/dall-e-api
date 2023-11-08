from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def generate_image(prompt):
  client = OpenAI(api_key=os.environ['API_KEY'])
  
  response = client.images.generate(
    model="dall-e-3", 
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
  )

  image_url = response.data[0].url

  return image_url

def image(request):
  prompt = request.GET.get('prompt') # get from request 
  print(prompt)
  if not prompt:
    return HttpResponse("No prompt provided")
  
  img_url = generate_image(prompt)
  return HttpResponse(img_url)