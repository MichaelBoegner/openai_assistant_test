from dotenv import load_dotenv
from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler
load_dotenv()
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

# assistant = client.beta.assistants.create(
# name="Math Tutor",
# instructions="You are a personal math tutor. Write and run code to answer math questions.",
# tools=[{"type": "code_interpreter"}],
# model="gpt-4o",
# )

# thread = client.beta.threads.create()

# message = client.beta.threads.messages.create(
# thread_id=thread.id,
# role="user",
# content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )

# run = client.beta.threads.runs.create_and_poll(
#   thread_id=thread.id,
#   assistant_id=assistant.id,
#   instructions="Please address the user as Jane Doe. The user has a premium account."
# )

# if run.status == 'completed': 
#   messages = client.beta.threads.messages.list(
#     thread_id=thread.id
#   )
#   print(messages)
# else:
#   print(run.status)