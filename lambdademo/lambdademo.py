import json

def welcome():
    return "welcome to serverless deployment"

def lambda_handler(event, context):
    # TODO implement
    msg = welcome()
    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }
