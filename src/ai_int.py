#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-02-12
"""
from openai import OpenAI
import os , time, json

marker = 'marker'

def create_client():
    return OpenAI(api_key=os.getenv("OPEN_KEY"))

def create_thread(client):
    return client.beta.threads.create()

def send_message(client, thread_id, user_input):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_input
    )

def create_run(client, thread_id):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=os.environ.get("ASS_ID"),
        tool_choice="auto"
    )

def handle_run(client, thread_id, run_id):
    """Continuously checks the run status and processes function calls."""
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id, run_id=run_id)
        print(f"🔄 Checking run status: {run_status.status}")

        if run_status.status == "completed":
            print("\n✅ Assistant has finished responding.\n")

            messages = client.beta.threads.messages.list(thread_id=thread_id)
            for msg in messages.data:
                if msg.role == "assistant":
                    print(f"🤖 Assistant: {msg.content}")
            return False 

        elif run_status.status == "requires_action":
            print("\n⚡ Function Call Required! Processing...")

            tool_calls = getattr(
                run_status.required_action.submit_tool_outputs, "tool_calls", None)

            if tool_calls is None or len(tool_calls) == 0:
                print("⚠️ Warning: No function calls were detected.")
                return False 

            for tool_call in tool_calls:
                print("\n🔍 Function Call Detected!")
                print(f"📌 Function Name: {tool_call.function.name}")
                print(
                    f"📄 Function Arguments:\n{json.dumps(tool_call.function.arguments, indent=4)}")

                event_details = json.loads(tool_call.function.arguments)

                print("\n📅 Creating Calendar Event...")
                # Nicely formatted JSON
                print(json.dumps(event_details, indent=4))


                print("\n✅ Event Created! Sending Output to OpenAI...\n")



                return True  # Function executed, end conversation

        time.sleep(0.5)  # Avoid excessive API calls


def interactive_chat():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)

    # Creating client and thread
    client = create_client()
    thread = create_thread(client)
    print(f"🧵 Thread Created: {thread.id}")
    print(f"🤖 Nancy: Hi, I'm Nancy, your AI calendar assistant, how can I help you today?")
    while True:
        user_input = input("\n🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Ending conversation. Goodbye!")
            break

        # Send user message to assistant
        send_message(client, thread.id, user_input)

        # Start a run
        run = create_run(client, thread.id)

        # Handle run, determine if function was called
        function_executed = handle_run(client, thread.id, run.id)

        # If a function was executed, conversation ends
        if function_executed:
            break

if __name__ == '__main__':
    interactive_chat()