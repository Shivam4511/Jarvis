from openai import OpenAI
client = OpenAI(api_key="")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant"},
        {
            "role": "user",
            "content": "what is coding"
        }
    ]
)

print(completion.choices[0].message)













completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and google cloud"},
        {"role":"user", "content":"what is coding"}
    ]
)

print(completion.choices[0].message)
