# database/db.py

# Simple in-memory storage (for hackathon)

research_data = []

def save_research(data):
    research_data.append(data)

def get_all_research():
    return research_data