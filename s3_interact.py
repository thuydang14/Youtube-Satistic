import boto3
import os
import glob

dir = os.getcwd()
# AWS_KEY = os.environ.get('ACCESS_KEY')
# AWS_SEC = os.environ.get("SECRET_KEY")


def get_file(dir, file_type):
    listfile = []
    for r, d, f in os.walk(f"{dir}\data"):
        for file in f:
            if file.endswith(f".{file_type}"):
                listfile.append(os.path.join(r, file))
    return listfile


def upload_to_s3(s3, bucket, key, listfile):
    for file in listfile:
        filename = file.split("\\")
        s3.upload_file(file, bucket, f"{key}/{filename[-1]}")

def main():
    s3_client = boto3.client("s3")
    bucket = "bigdata-youtube-raw-dev-thuydang"
    
    category = get_file(dir, "json")
    video = get_file(dir, "csv")

    upload_to_s3(s3_client, bucket, "raw_category",category)
    upload_to_s3(s3_client, bucket , "raw_video",video)

if __name__ == "__main__":
    main()




    