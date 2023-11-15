from game.domain import GameRepository
from game.serializers import GameTeamSaveSerializer, GameTeamRequestSerializer
from team.domain import TeamRepository

class GameTeamService:

    def __init__(self, game_repository: GameRepository, team_repository: TeamRepository, *args, **kwargs):
        self._game_repository = game_repository
        self._team_repository = team_repository

    def create_game_team(self, request_data, game_id: int):
        game_team_request_serializer = GameTeamRequestSerializer(data=request_data)
        game_team_request_serializer.is_valid(raise_exception=True)
        game_team_data = game_team_request_serializer.validated_data
        team_ids: list = game_team_data.get('team_ids')

        game = self._game_repository.find_game_by_id(game_id)

        for team_id in team_ids:
            team = self._team_repository.find_team_by_id(team_id)
            game_team_save_serializer = GameTeamSaveSerializer(data={'game': game.id, 'team': team.id})
            game_team_save_serializer.is_valid(raise_exception=True)
            game_team_save_serializer.save()