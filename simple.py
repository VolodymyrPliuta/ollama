from ollama import chat

model = "phi:latest"   # use the exact installed model name

# Memory context (starts empty except for system prompt)
messages = [
    {"role": "system", "content": "You are Splinter from Teenage Mutant Ninja Turtles."},
    {"role": "system", "content": "Respond in title case letters."},
    {"role": "system", "content": "Limit your answers to 50 words."}
]

print("Just a chat. Type 'exit' to quit.\n")

while True:
    user_input = input("Me: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    # Add user's message to memory
    messages.append({"role": "user", "content": user_input})

    # Generate response with the full context
    response = chat(
        model=model,
        messages=messages
    )

    answer = response.message.content
    print("AI:", answer, "\n")

    # Add assistant reply to memory
    messages.append({"role": "assistant", "content": answer})
