import boto3

ficheroUpload = "data.csv"
nombreBucket = "jss-output-s3"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")
