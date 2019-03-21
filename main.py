import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('test-for-downloading-with-dialog')

print(bucket.name)

data = open('image.jpg', 'rb')
bucket.put_object(Key='image.jpg', Body=data, ContentType='binary/octet-stream')

print('uploaded')