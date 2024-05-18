from dotenv import load_dotenv
from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler
load_dotenv()
client = OpenAI()

from openai import OpenAI
client = OpenAI()

file = client.files.create(
  file=open("./tse_takehome_dataset.csv", "rb"),
  purpose='assistants'
)  

assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="The attached csv file has a list of people. The column headers represent their interests. Use the data to build a fictional story that is three sentences long about their interests that are similar to the column headers. Help the user as much as possible with getting better at using OpenAI's Assistants code_interpreter.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What is Tina Escobar's favorite city and why?"
)

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Michael Boegner. They are still learning about openAI."
)

if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)


