from tweets.models import Tweet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tweets.serializers import TweetSerializer
import json
import jsonschema


with open('schemas/tweet_schema.json', 'r') as schema_file:
    SCHEMA = schema_file.read()


class TweetList(APIView):

    @staticmethod
    def __validate_data__(data):
        jsonschema.validate(
            data,
            json.loads(SCHEMA)
        )

    @staticmethod
    def __persist_tweet__(tweet_data):
        Tweet.objects.create(message=tweet_data['message'], name=tweet_data['name'])

    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        try:
            self.__validate_data__(data)
            self.__persist_tweet__(data)
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
