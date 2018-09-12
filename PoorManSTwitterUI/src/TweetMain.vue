<template>
  <div class="container">
    <b-card-group deck>
      <b-card header="Tweet a Message"
              border-variant="secondary"
              header-bg-variant="primary"
              header-text-variant="white">
          <tweet-form />
      </b-card>
      <p/>
      <b-card header="All Tweets"
              border-variant="secondary"
              header-bg-variant="primary"
              header-text-variant="white">
          <tweet-list :tweets="tweets" />
      </b-card>
    </b-card-group deck>
  </div>
</template>

<script>
  import {API_BASE_URL} from './config.js';
  import {TWEET_LIST_UPDATE_INTERVAL_MILISECS} from './config.js';
  import TweetForm from './TweetForm.vue';
  import TweetList from './TweetList.vue';

  export default {
      name: 'tweet-main',
      components: {
          'tweet-list': TweetList,
          'tweet-form': TweetForm
      },
      data: function () {
        return {tweets: []};
      },
      methods: {
        loadTweets: function() {
          var tweets = [];
          $.getJSON(API_BASE_URL + '/tweets')
              .done(data => {this.tweets = data;});
        }
      },
      created: function () {
        this.loadTweets();
        setInterval(function () {
           this.loadTweets();
          }.bind(this), TWEET_LIST_UPDATE_INTERVAL_MILISECS
        );
      }
  };
</script>

<style>
  .dark-border {
     border:1px solid black;
     margin: 25px 50px 75px 100px
  }
</style>
