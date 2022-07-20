<template>
  <v-row v-if="!$auth.loggedIn" align="center" justify="center">
    <v-col cols="12" md="6" sm="8">
      <v-card>
        <v-card-title>Sign In</v-card-title>
        <v-card-text>
          <v-text-field v-model="email" label="email" required></v-text-field>
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            label="Password"
            name="input-10-1"
            @click:append="show1 = !show1"
            @keydown.enter.exact="login"
          ></v-text-field>
          <v-btn @click="login">Sign In</v-btn>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class Login extends Vue {
  email: string = ''
  password: string = ''
  show1: boolean = false

  baseEndpoint = '/api/accounts'

  created() {
    // Force re-fetch user and set cookies and vuex state
    // because auto-fetch does not work in some cases.
    if (process.client) {
      if (!this.$auth.loggedIn) {
        this.$auth.reset()
      } else {
        this.$router.push('/')
      }
    }
  }

  async login() {
    await this.$auth
      .loginWith('cookie', {
        data: {email: this.email, password: this.password},
      })
      .catch((reason) => {
        alert(`Failed to sign in: ${reason}`)
      })
  }
}
</script>
