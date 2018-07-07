
import json
import watson_developer_cloud
from pprint import pprint
fhand  = open("workspace.json")
# Set up Assistant service.
service = watson_developer_cloud.AssistantV1(
  username = "ae5f898a-90da-4827-b431-81ec5b21edba",
  password = "3wgeXwQhxBha",
  version = '2017-10-16'
)

workspace_id = '7c0875d3-02a0-450e-8eee-0bd4011ccae3' # replace with workspace ID
user_input = ''
context = {}
current_action = ''

workspace = json.load(fhand)
pprint(workspace)

while current_action != 'end_conversation':

  # Send message to Assistant service.
  response = service.message(
    workspace_id = workspace_id,
    input = {
      'text': user_input
    },
    context = context
  )

  # Print the output from dialog, if any.
  if response['output']['text']:
    print(response['output']['text'][0])

  # Update the stored context with the latest received from the dialog.
  context = response['context']
  # Check for action flags sent by the dialog.
  if 'action' in response['output']:
    current_action = response['output']['action']
  # If we're not done, prompt for next round of input.
  if current_action != 'end_conversation':
    user_input = input('>> ')
