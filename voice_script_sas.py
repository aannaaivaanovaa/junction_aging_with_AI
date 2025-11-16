import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- API CONFIG ---

GEMINI_API_KEY = ""  # REMOVE IN PRODUCTION
load_dotenv()
genai.configure(api_key=GEMINI_API_KEY)

# --- LOAD SAS RECOMMENDATIONS FILE ---

df = pd.read_csv("sas_recommendations.csv", sep=';')
df.columns = df.columns.str.strip()

def get_recommendation(name: str):
    """Return recommendation row for a user."""
    person = df[df["Name"] == name]
    if person.empty:
        raise ValueError(f"No person found with name: {name}")
    return person.iloc[0].to_dict()

# --- GENERATE SIMPLE VOICE CALL SCRIPT ---

def generate_voice_call(rec):
    """Generate simple human-like call script using SAS recommendation data."""

    prompt = f"""
    Create a very simple, friendly phone call script for an elderly person.

    Use the following SAS recommendation data:
    - Name: {rec['Name']}
    - Recommendation: {rec['Recommendation']}
    - Context: {rec['Recommendation Context']}

    Requirements:
    - 5–7 short sentences
    - Warm, caring, and easy to understand
    - Start by greeting the person by name
    - Mention the recommendation clearly in everyday language
    - Keep it simple and human
    """

    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content(prompt)

    return response.text

# --- RUN TEST ---

if __name__ == "__main__":
    # Example: generate call for each person in your example
    names = ["Maria Johnson", "George Braun", "Anna Lindberg", "Samuel Novak", "Laura Rossi"]

    for name in names:
        rec = get_recommendation(name)
        script = generate_voice_call(rec)

        print("\n============================")
        print(f"VOICE CALL FOR: {name}")
        print("============================\n")
        print(script)
        print("\n")
