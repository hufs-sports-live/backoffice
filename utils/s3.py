from decouple import config
import boto3

class S3Connect:
    _aws_access_key = config('S3_ACCESS_KEY')
    _aws_secret_key = config('S3_SECRET_ACCESS_KEY')
    _bucket_name = config('BUCKET_NAME')
    
    def __init__(self):
        self._s3_conn = boto3.client('s3', aws_access_key_id=self._aws_access_key, aws_secret_access_key=self._aws_secret_key)

    def make_s3_key(self, image_data, team_name: str, league_name: str):
        object_name = f"{team_name}.{image_data.content_type.split('/')[-1]}"
        return league_name + '/' + object_name
    
    def upload_to_s3(self, image_data, team_name: str, league_name: str):
        key = self.make_s3_key(image_data, team_name, league_name)
        self._s3_conn.put_object(Body=image_data, Bucket=self._bucket_name, Key=key, ContentType=image_data.content_type)
        url = f"https://{self._bucket_name}.s3.ap-northeast-2.amazonaws.com/{key}"
        return url

    def delete_object(self, key: str):
        self._s3_conn.delete_object(Bucket=self._bucket_name, Key=key)
