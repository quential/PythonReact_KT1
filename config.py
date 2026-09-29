from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

front_url = os.getenv('FRONTEND_URL')
origins = [front_url] if front_url else []

