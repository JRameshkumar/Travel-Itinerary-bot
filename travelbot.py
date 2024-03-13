import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

st.title("Travel Itenary Generator Assistant:airplane:")

destination = st.text_input("Enter your destination place:")
days = st.number_input("Number of travel days:", min_value=1)
budget_level = st.selectbox(
    "Select budget level:",
    ("Low", "Medium", "High")
)
interests = st.multiselect(
    "Select your interests: ",
    ["History & Culture", "Nature & Outdoors", "Food & Drinks", "Nightlife", "Shopping", "Releaxation"]
)

button = st.button("Generate Itenary",type="primary")

if button:
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=3000,
        temperature=0.8,
        system=f"You are an expert tour guide for {destination}. You have an extensive knowledge of the area, including popular and beautiful attractions, hidden gems, local experiences, and practical travel tips. Provide a detailed itenary keeping in mind that the travellers budgets and their interests. ",
        messages=[
                {
                    "role": "user",
                    "content": [
                                    {
                                        "type": "text",
                                        "text": f"Create a travel itenary for a trip to a {destination} lasting {days} days. The traveler has a {budget_level} budget and is interested in {interests}.\n\nConsiderations:\nInclude a mix of popular attractions and some lesser known spots relevant spots relevant to the interests.\nProvide a short descriptions of each suggested activity.\nIncorporate the estimated costs wherever possible, considering the budget level.\nAim for a balance of activities that match the selected interests."
                                    }
                                ]
                }
            ]
        )
    raw_text=message.content
    itinerary=raw_text[0].text
    st.write(itinerary)



