import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

GEMINI_API_KEY="" #Remove this line in production code

load_dotenv()

# Configure Gemini API
api_key = "" #Remove this line in production code
genai.configure(api_key=api_key)

# Load the data from sas platform for the forward analysis, now it is done through the file later plan on doing it using connect API. 

df = pd.read_csv("grand_people_sas.csv", sep=';')  
df.columns = df.columns.str.strip()  # remove extra spaces in column names

# Split hobbies into a list
def parse_hobbies(hobbies_str):
    return [h.strip() for h in str(hobbies_str).split(';') if h.strip()]

def get_person(name: str):
    """Return a dictionary with a person's data by name."""
    person = df[df["Name"] == name]

    if person.empty:
        raise ValueError(f"No person found with name: {name}")

    data = person.iloc[0].to_dict()
    data["Hobbies_List"] = parse_hobbies(data.get("Hobbies / Interests", ""))
    return data

# GENERATE VOICE CALL SCRIPT USING GEMINI
def generate_voice_script(person_data):
    """Send data to Gemini and get a call script."""
    hobbies = person_data.get("Hobbies_List", [])
    hobbies_text = ", ".join(hobbies[:2])  # take first two hobbies

    prompt = f"""
    Create a warm, friendly, human-sounding phone call script based on this person's data:

    Name: {person_data['Name']}
    Age: {person_data['Age']}
    Steps Yesterday: {person_data['Steps Yesterday']}
    Relative: {person_data['Relative Name']} ({person_data['Relative Age']} years old)
    Hobbies: {hobbies_text}

    The call should:
    - sound empathetic and natural
    - mention their steps yesterday
    - reference one or two hobbies
    - be no more than 8–10 sentences
    - feel like a real person checking in on them
    """

    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content(prompt)

    return response.text

# RUN

if __name__ == "__main__":
    # Choose the person you want
    name_to_lookup = "Maria Johnson"

    # Get their data
    person = get_person(name_to_lookup)

    # Generate the script
    script = generate_voice_script(person)

    print("\n--- Voice Call Script ---\n")
    print(script)
    print("\n-------------------------\n")
