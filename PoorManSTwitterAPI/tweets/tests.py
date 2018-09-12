from rest_framework import status
from rest_framework.test import APITestCase
import json
from tweets.models import Tweet


class TestUtils:

    VALID_TEST_TWEET = {
        'message': 'Outside of a dog, a book is a man\'s best friend. Inside of a dog it\'s too dark to read.',
        'name': 'Groucho Marx'
    }

    MISSING_MESSAGE_TEST_TWEET = {
                  'name': 'Marcel Marceau'
    }

    MISSING_NAME_TEST_TWEET = {
                  'message': 'Love is grand; divorce is a hundred grand.'
    }

    ALL_TWEETS = [
        {'id': 1,
         'message': 'Perfect is the enemy of good.',
         'name': 'Voltaire',
         'datetime': '2018-09-11T08:55:08.144000Z'},
        {'id': 2,
         'message': 'I don\'t want to achieve immortality through my work ... I want to achieve it through not dying.',
         'name': 'Woody Allen',
         'datetime': '2018-09-11T09:02:47.533000Z'},
        {'id': 3,
         'message': 'If I had a dollar for every million-dollar idea I\'ve had, I\'d be rich.',
         'name': 'Greg Meyer',
         'datetime': '2018-09-11T09:03:40.435000Z'}
    ]

    @staticmethod
    def _decode_content_(response):
        return response.content.decode('utf-8')

    @staticmethod
    def _model_object_to_dictionary_(model_object, exclusions):
        dictionary = model_object.__dict__
        for exclusion in exclusions + ['_state']:
            dictionary.pop(exclusion, None)
        return dictionary

    def _parse_response_(self, response):
        return json.loads(self._decode_content_(response))


class TweetViewSetTests(APITestCase, TestUtils):

    fixtures = ['fixtures/test_data.json']

    def test_get_all_tweets(self):
        response = self.client.get('/tweets')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tweets = self._parse_response_(response)
        self.assertEqual(len(tweets), 3)
        self.assertEqual(tweets, self.ALL_TWEETS)

    def test_create_a_tweet(self):
        response = self.client.post('/tweets', self.VALID_TEST_TWEET)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tweet = Tweet.objects.get(name='Groucho Marx')
        self.assertEqual(self._model_object_to_dictionary_(tweet, exclusions=['datetime', 'id']), self.VALID_TEST_TWEET)

    def test_attempt_to_create_a_tweet_missing_message(self):
        response = self.client.post('/tweets', self.MISSING_MESSAGE_TEST_TWEET)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("'message' is a required property" in self._decode_content_(response))

    def test_attempt_to_create_a_tweet_missing_name(self):
        response = self.client.post('/tweets', self.MISSING_NAME_TEST_TWEET)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("'name' is a required property" in self._decode_content_(response))
