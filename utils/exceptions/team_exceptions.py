from rest_framework.exceptions import APIException

class S3UploadError(APIException):
    status_code = 400
    default_detail = "S3 업로드를 실패하였습니다."
    default_code = 's3_upload_error'

    def __init__(self, team_name):
        self.team_name = team_name
        super().__init__(self.default_detail, self.default_code)

class TeamSaveError(APIException):
    status_code = 500
    default_detail = "팀 정보 저장을 실패하였습니다."
    default_code = 'team_save_error'

    def __init__(self, team_name):
        self.team_name = team_name
        super().__init__(self.default_detail, self.default_code)

class EmptyLogoError(APIException):
    status_code = 400
    default_detail = "로고를 업로드 하지 않은 팀이 존재합니다."
    default_code = 'empty_logo_error'
