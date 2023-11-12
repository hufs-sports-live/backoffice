from team.domain import TeamRepository
from accounts.domain import Member
from django.core.exceptions import PermissionDenied
from team.serializers import TeamRegisterRequestSerializer, TeamChangeRequestSerializer, TeamSaveSerializer
from utils.upload_to_s3 import upload_to_s3
from team.domain import Team
from league.domain import League

class TeamService:
    def __init__(self, team_repository: TeamRepository, *args, **kwargs):
        self._team_repository = team_repository

    def register_teams(self, request_data, league: League, user_data: Member):
        teams_data_serializer = TeamRegisterRequestSerializer(data=request_data)
        teams_data_serializer.is_valid(raise_exception=True)
        team_data = teams_data_serializer.validated_data
        teams_names = team_data.get('names')
        teams_logos = team_data.get('logos')
        error_team = []

        for i, team_name in enumerate(teams_names):
            team_logo = teams_logos[i]
            try:
                logo_url = upload_to_s3(image_data=team_logo, team_name=team_name, league_name=league.name)
                new_team = Team(name=team_name, logo_image_url=logo_url, league=league, administrator=user_data, organization=user_data.organization)
                self._team_repository.save_team(new_team)
            except:
                error_team.append(team_name)
        if error_team:
            return {"errorTeams": error_team}
        
    def change_team(self, request_data, league: League, team: Team, user_data: Member):
        if team.organization != user_data.organization:
            raise PermissionDenied

        team_change_request_serializer = TeamChangeRequestSerializer(data=request_data)
        team_change_request_serializer.is_valid(raise_exception=True)
        team_change_data = team_change_request_serializer.validated_data
        team_name = team_change_data.get('names')[0]
        team_logo = team_change_data.get('logos')[0]
        logo_url = upload_to_s3(image_data=team_logo, team_name=team_name, league_name=league.name)

        team_save_serialzier = TeamSaveSerializer(team, data={'name': team_name, 'logo_image_url': logo_url, 'administrator': user_data.id}, partial=True)
        team_save_serialzier.is_valid(raise_exception=True)
        team_save_serialzier.save()

    def find_one_team(self, team_id: int):
        return self._team_repository.find_team_by_id(team_id)