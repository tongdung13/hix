from fastapi import FastAPI
from mangum import Mangum
import json

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root(event, context):
    # Process the CloudWatch event payload
    print("Received event: " + json.dumps(event))
    
    # Add your event processing logic here

    return {
        'statusCode': 200,
        'body': json.dumps('Event processed successfully')
    }
