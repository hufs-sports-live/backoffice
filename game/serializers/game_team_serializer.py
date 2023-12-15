from rest_framework import serializers
from game.domain import GameTeam, GameTeamPlayer

class GameTeamSaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeam
        fields = '__all__'

class GameTeamRequestSerializer(serializers.Serializer):
    teamIds = serializers.ListField(child=serializers.IntegerField(), source='team_ids')

class GameTeamPlayerRequestSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeamPlayer
        fields = ('name', 'description',)

class GameTeamPlayerSaveSerialzier(serializers.ModelSerializer):

    class Meta:
        model = GameTeamPlayer
        fields = '__all__'

class GameTeamPlayerChangeSerialzier(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = GameTeamPlayer
        fields = ('id', 'name', 'description',)

class _GameTeamScoreMappingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    score = serializers.IntegerField()

class GameScoreChangeSerializer(serializers.Serializer):
    teamIdScore = _GameTeamScoreMappingSerializer(many=True, source='team_score')