import pandas as pd

data = {
    "Name": [
        "Maria Johnson",
        "George Braun",
        "Anna Lindberg",
        "Samuel Novak",
        "Laura Rossi"
    ],
    "Recommendation": [
        "User needs to go for a walk or exercise",
        "User needs to go for a walk or exercise",
        "User needs to call relatives or friends",
        "User has an event today, remind them to go to it",
        "User has an event today, remind them to go to it"
    ],
    "Recommendation Context": [
        "Low step count",
        "Low step count",
        "Its been a while since your last call",
        "Its great to get out of the house",
        "Its great to get out of the house"
    ]
}

df = pd.DataFrame(data)
filepath = "sas_recommendations.csv"
df.to_csv(filepath, index=False, sep=';')

df
