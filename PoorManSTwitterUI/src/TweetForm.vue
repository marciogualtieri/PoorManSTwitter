<template>
  <div class="container" inline>
      <b-form inline @submit="submitTweet">
        <b-form-row>
         <b-col class="col-lg-3">
          <label for="nameInput">Name:</label>
          <b-form-input id="nameInput" type="text"
                        v-model="name"
                        placeholder="Your Poor Man's Twitter Name">
          </b-form-input>
          <b-form-invalid-feedback id="nameFeedback" v-if="!($v.name.required && $v.name.maxLength)">
             Name is required and must be at most 15 characters long.
          </b-form-invalid-feedback>

          </b-col>
          <b-col class="col-lg-9">
            <label for="messageInput">Message:</label>
            <b-form-input id="messageInput"
                          type="text"
                          v-model="message"
                          placeholder="Your Poor Man's Twitter Message">
            </b-form-input>
            <b-form-invalid-feedback id="messageFeedback" v-if="!($v.message.required && $v.message.maxLength)">
               Message is required and must be at most 50 characters long.
            </b-form-invalid-feedback>
          </b-col>
       </b-form-row>
       <b-form-row>
         <b-col class="col-lg-12">
          <b-button size="lg" type="submit" :disabled="$v.$invalid">Tweet</b-button>
         </b-col>
      </b-form-row>

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

<style>
button {
  margin-top: 15px!important;
}

input {
  width: 100%!important;
}

.container {
   padding: 0px;
}
</style>
