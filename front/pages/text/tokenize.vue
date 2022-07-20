<template>
  <v-row>
    <v-col cols="12">
      <v-textarea v-model="text"></v-textarea>
    </v-col>
    <v-col cols="2">
      <v-select v-model="lang" :items="langOpts"></v-select>
    </v-col>
    <v-col cols="2">
      <v-select v-model="outputFormat" :items="outputFormatOpts"></v-select>
    </v-col>
    <v-col cols="12">
      <v-btn :disabled="!validateInput()" @click="onClickTokenize">Tokenize</v-btn>
    </v-col>
    <v-col cols="12" class="mt-6">
      <h2>Tokenized result</h2>
    </v-col>
    <v-col v-if="responseData && outputFormat==='wakachi'" cols="12">
      <div>
        <p>{{ responseData.result }}</p>
      </div>
    </v-col>
    <v-col v-else-if="responseData && outputFormat==='all_info'" cols="12">
      <v-expansion-panels>
        <v-expansion-panel v-for="(sent, i) in responseData.result" :key="i">
          <v-expansion-panel-header>{{ sent.wakachi }}</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-data-table
              :headers="tokenizedResultHeaders"
              :items="sent.tokens"
              :items-per-page="8"
              class="elevation-1"
            ></v-data-table>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-col>
    <v-col v-else>No result</v-col>
  </v-row>
</template>

<script lang="ts">

import { Component, Vue, Watch } from 'nuxt-property-decorator'
import {
  LangOption,
  OutputFormat,
  TokenizationResponse,
  tokenizedResultHeaders,
} from '~/models/tokenization'

@Component
export default class Tokenize extends Vue {
  text: string = ''
  lang: LangOption = 'ja'
  outputFormat: OutputFormat = 'wakachi'
  langOpts: LangOption[] = ['ja', 'en']
  outputFormatOpts: OutputFormat[] = ['wakachi', 'all_info']

  tokenizedResultHeaders = tokenizedResultHeaders
  responseData: TokenizationResponse | null = null

  async onClickTokenize() {
    try {
      const response = await this.$axios.post('/api/text/tokenize/', {
        data: this.text.trim(),
        lang: this.lang,
        params: {
          format: this.outputFormat,
        },
      })
      this.responseData = response.data
    } catch (err) {
      alert(err)
    }
  }

  @Watch('text')
  private validateInput() {
    return this.text.trim().length != 0
  }
}
</script>
