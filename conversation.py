# Experimenting with Amazon Lex integration.
# Relevant documentation: https://boto3.readthedocs.io/en/latest/reference/services/lex-runtime.html
# Also: https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html


import boto3


client = boto3.client('lex-runtime')
# the userId is used to identify who is speaking to the bot - ex. to separate conversations
# Might need a way to assign unique identifiers (ex. discord ID)
userId = "Speaker"


test_message = "Is it going to rain"

# See documentation for full explanation of parameters
response = client.post_content(
    botName='Lurky',
    botAlias='Main',
    userId='userId',
    sessionAttributes=None,
    requestAttributes=None,
    contentType='text/plain; charset=utf-8',
    accept='text/plain; charset=utf-8',
    inputStream=test_message
)

# Below is all diagnostic info to figure out what is being received/returned.
print("Intent: " + response["intentName"])
print("Message: " + response["message"])
print("DialogState: " + response["dialogState"])
print("Response Content Type: " + response["contentType"])

# This only really applies to audio messages. Prints a transcript of what lex thought was said.
if response["contentType"] != "text/plain;charset=utf-8":
	print("InputTranscript: " + response["inputTranscript"])

# Only if dialogState is ElicitSlot - waiting for a response from user before continuing with response
if response["dialogState"] == "ElicitSlot":
    print("Slot which needs a value before completing response: " + response["slotToElicit"])
    if response["slotToElicit"] == "City":
        print("Which city do you want to know about?")
        inputCity = input()
        test_message = "Is it going to rain in " + inputCity
        print("New query: " + test_message)
        response = client.post_content(
            botName='Lurky',
            botAlias='Main',
            userId='userId',
            sessionAttributes=None,
            requestAttributes=None,
            contentType='text/plain; charset=utf-8',
            accept='text/plain; charset=utf-8',
            inputStream=test_message)
        # Repeat to test elicit-slot-Response
        # Below is all diagnostic info to figure out what is being received/returned.
        print("Intent: " + response["intentName"])
        print("Message: " + response["message"])
        print("DialogState: " + response["dialogState"])
        print("Response Content Type: " + response["contentType"])

        # Adding in a weather module to get data from Openeweathermap.org.  Probably should move This


print("End program.")

# Expected response syntax (from documentation) - dict format:
# InputTranscript: only if audio was sent
"""
{
    'contentType': 'string',
    'intentName': 'string',
    'slots': {...}|[...]|123|123.4|'string'|True|None,
    'sessionAttributes': {...}|[...]|123|123.4|'string'|True|None,
    'message': 'string',
    'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
    'dialogState': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
    'slotToElicit': 'string',
    'inputTranscript': 'string',
    'audioStream': StreamingBody()
}
"""
