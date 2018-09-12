import Vue from 'vue';
import TweetForm from '../../../src/TweetForm';
import { mount } from '@vue/test-utils';
import Vuelidate from 'vuelidate'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(Vuelidate)

function setInput(wrapper, id, value) {
  var input = wrapper.find(id)
  input.element.value = value
  input.trigger('input')
}

function setName(wrapper, id, value) {
  wrapper.setData({name: value})
  var input = wrapper.find(id)
  input.element.value = value
  input.trigger('input')
}

function setName(wrapper, id, value) {
  wrapper.setData({name: value})
  setInput(wrapper, id, value)
}

function setMessage(wrapper, id, value) {
  wrapper.setData({message: value})
  setInput(wrapper, id, value)
}

const MAX_NAME_SIZE = 15
const MAX_MESSAGE_SIZE = 50

describe('TweetForm.vue', () => {
  it(`should accept valid parameters`, () => {
    const wrapper = mount(TweetForm);
    wrapper.setData({name: 'test',  message: 'test', status: ''})
    setName(wrapper, "#nameInput", 'X'.repeat(MAX_NAME_SIZE))
    setMessage(wrapper, "#messageInput", 'X'.repeat(MAX_MESSAGE_SIZE))
    expect(wrapper.find('#nameFeedback').exists()).to.equal(false)
    expect(wrapper.find('#messageFeedback').exists()).to.equal(false)
  });

  it(`should reject invalid name`, () => {
    const wrapper = mount(TweetForm);
    wrapper.setData({name: 'test',  message: 'test', status: ''})
    setName(wrapper, "#nameInput", 'X'.repeat(MAX_NAME_SIZE + 1))
    setMessage(wrapper, "#messageInput", 'X'.repeat(MAX_MESSAGE_SIZE ))
    expect(wrapper.find('#nameFeedback').exists()).to.equal(true)
    expect(wrapper.find('#messageFeedback').exists()).to.equal(false)
  });

  it(`should reject invalid message`, () => {
    const wrapper = mount(TweetForm);
    setName(wrapper, "#nameInput", 'X'.repeat(MAX_NAME_SIZE))
    setMessage(wrapper, "#messageInput", 'X'.repeat(MAX_MESSAGE_SIZE + 1))
    expect(wrapper.find('#nameFeedback').exists()).to.equal(false)
    expect(wrapper.find('#messageFeedback').exists()).to.equal(true)
  });
});
