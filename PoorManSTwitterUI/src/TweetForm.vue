<template>
  <div>
    <b-form @submit="submitTweet">
      <b-form-group label="Name:">
        <b-form-input id="nameInput" type="text"
                      v-model="name"
                      placeholder="Your Poor Man's Twitter Name">
        </b-form-input>
        <b-form-invalid-feedback id="nameFeedback" v-if="!($v.name.required && $v.name.maxLength)">
           Name is required and must be at most 15 characters long.
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="Message:">
        <b-form-input id="messageInput"
                      type="text"
                      v-model="message"
                      placeholder="Your Poor Man's Twitter Message">
        </b-form-input>
        <b-form-invalid-feedback id="messageFeedback" v-if="!($v.message.required && $v.message.maxLength)">
           Message is required and must be at most 50 characters long.
        </b-form-invalid-feedback>
      </b-form-group>
      <b-button type="submit" :disabled="$v.$invalid">Tweet</b-button>
    </b-form>

    <p id="status" v-if="status">{{status}}</p>
  </div>
</template>

<script>
import {API_BASE_URL} from './config.js';
import Vuelidate from 'vuelidate';
import { required, maxLength, between } from 'vuelidate/lib/validators';

export default {
  name: 'tweet-form',
  data() {
    return {status: '',
            name: '',
            message: ''};
  },
  validations: {
    name: {
      required,
      maxLength: maxLength(15)
    },
    message: {
      required,
      maxLength: maxLength(50)
    }
},
  methods: {
    submitTweet() {
      var that = this;
      var resource = API_BASE_URL + '/tweets';
      var data = {
      'name': this.name,
      'message': this.message
      };
      $.ajax({
        async: true, type: 'POST', url: resource, data: data,
        success: function (response) {
        },
        error: function(xhr, status, error) {
          that.status = 'Error: ' + resource + ' status is ' + xhr.status + '.';
        }
     });
    }
  }
};

</script>
