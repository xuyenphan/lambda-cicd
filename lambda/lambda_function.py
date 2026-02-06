import json
def lambda_handler(event,context):
    return {
        "status code":200,
        "body":json.dumps('hello from cicd github actions workflow vscode')
    }