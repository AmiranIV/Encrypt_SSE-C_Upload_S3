import boto3
import os

BUCKET = 'YourBucketName'
KEY = os.urandom(32) #ENCRYPTION 
s3 = boto3.client('s3') # Only works if you preformed AWS CONFIGURE

print("Uploading S3 object with SSE-C")
s3.put_object(Bucket=BUCKET,          
              Key='NAME OF FILE IN S3',
              Body=b'YOUR/FILE/PATH',
              SSECustomerKey=KEY,
              SSECustomerAlgorithm='AES256') #Encryption Algorithm used
print("Done")
