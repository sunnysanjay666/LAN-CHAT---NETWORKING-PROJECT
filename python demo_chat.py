import threading

# Simulated chat messages
messages = []

# Function to handle sending messages
def send():
    while True:
        msg = input()
        messages.append(f"You: {msg}")
        print_chat()

# Function to display chat
def print_chat():
    # Clear terminal (works in most terminals)
    print("\033c", end="")
    for m in messages:
        print(m)

# Function to simulate receiving messages
def receive():
    while True:
        # Simulate a received message (replace with AI reply for demo)
        import time
        time.sleep(5)
        messages.append("Friend: Hello! This is a demo message.")
        print_chat()

# Start sending and receiving threads
threading.Thread(target=send, daemon=True).start()
threading.Thread(target=receive, daemon=True).start()

# Keep the main thread alive
while True:
    pass