<template>

  <b-table striped hover
           :items="tweets"
           :sort-by.sync="sortBy"
           :sort-desc.sync="sortDesc"
           :fields="fields">
  </b-table>

</template>

<script>
  export default {
      name: 'tweet-list',
      props: ['tweets'],
      data () {
        return {
          sortBy: 'name datetime',
          sortDesc: false,
          fields: [
            { key: 'name', sortable: true },
            { key: 'datetime', sortable: true },
            { key: 'message', sortable: false }
          ],
        }
     }
  };
</script>
