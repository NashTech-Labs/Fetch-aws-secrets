# AWS Secrets Manager Script

This script uses AWS Secrets Manager to retrieve secret values stored in your AWS account. It leverages the `boto3` library to interact with AWS services.

## Prerequisites

1. **AWS Account**: Ensure you have access to an AWS account and have secrets stored in AWS Secrets Manager.
2. **AWS IAM Permissions**: The AWS Identity and Access Management (IAM) role/user executing this script must have appropriate permissions to access the Secrets Manager API.
   - Example IAM Policy:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "secretsmanager:GetSecretValue",
           "Resource": "*"
         }
       ]
     }
     ```
3. **AWS CLI or AWS Credentials**: You must have valid AWS credentials set up locally to authenticate to AWS services.

   - To configure AWS CLI, run:
     ```bash
     aws configure
     ```
     Provide your access key, secret key, region, and output format during configuration.

## Installation

1. **Python 3.x**: Ensure you have Python 3.x installed. You can download it from [Python's official site](https://www.python.org/).

2. **Install boto3**: You need to install the `boto3` package, which is the AWS SDK for Python, to interact with AWS services.

   To install `boto3`, run:
   ```bash
   pip install boto3
****
## Usage

### Set Your Secret and Region

Before running the script, update the following placeholders in the script with your values:

- `secret_name`: The name of the secret stored in AWS Secrets Manager.
- `region_name`: The AWS region where the secret is stored (e.g., `us-east-1`).

Example modification in the script:

```python
secret_name = "my-secret"
region_name = "us-east-1"
```
### Run script
Once you have set the secret_name and region_name, run the script using Python:
```
python secrets_manager.py
```
