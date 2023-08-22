import json
from flask import request, jsonify
import numpy as np
from app.app import app
from app import openai_utils
from sklearn.metrics.pairwise import cosine_similarity
from app.models import db, Symptom


