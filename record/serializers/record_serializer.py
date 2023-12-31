from rest_framework import serializers
from record.domain import Record

class RecordRequestSerializer(serializers.ModelSerializer):
    gameTeamId = serializers.IntegerField(source='game_team_id')
    gameTeamPlayerId = serializers.IntegerField(source='game_team_player_id')
    score = serializers.IntegerField()
    quarterId = serializers.IntegerField(source='quarter_id')

    class Meta:
        model = Record
        fields = ('gameTeamId', 'gameTeamPlayerId', 'score', 'quarterId')