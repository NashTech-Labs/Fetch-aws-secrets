import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name):
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        # Fetch the secret value
        response = client.get_secret_value(SecretId=secret_name)
        
        # Secrets Manager returns two fields, depending on whether the secret is a binary or string
        if 'SecretString' in response:
            secret = response['SecretString']
        else:
            secret = response['SecretBinary']
        
        return secret

    except ClientError as e:
        # Handle specific exceptions and error messages
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Handle the exception for KMS key issues
            print("Secrets Manager can't decrypt the secret using the provided KMS key.")
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(f"The requested secret {secret_name} was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print(f"Invalid request: {e}")
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print(f"Invalid parameter: {e}")
        else:
            print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    # Replace 'my-secret' with your secret name and region with the AWS region where your secret is stored.
    secret_name = "my-secret"
    region_name = "us-east-1"
    
    secret_value = get_secret(secret_name, region_name)
    
    if secret_value:
        print(f"Fetched secret: {secret_value}")
