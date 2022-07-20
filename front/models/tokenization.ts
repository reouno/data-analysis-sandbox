export type LangOption = 'ja' | 'en'
export type OutputFormat = 'wakachi' | 'all_info'

export interface Token {
  i: number
  orth_: string
  reading: string
  lemma_: string
  pos_: string
  tag_: string
  head_i: number
  dep_: string
  ent_iob_: string
}

export interface TokenizedSentence {
  raw: string
  wakachi: string
  tokens: Token[]
}

export interface TokenizationResponse {
  result: string | TokenizedSentence[]
  lang: LangOption
  params: any
}

export const outputFormatOf = (response: TokenizationResponse): OutputFormat => {
  return response.params.format
}

export const tokenizedResultHeaders = [
  { text: 'Idx', value: 'i' },
  { text: 'orth_', value: 'orth_' },
  { text: 'reading', value: 'reading' },
  { text: 'lemma_', value: 'lemma_' },
  { text: 'pos_', value: 'pos_' },
  { text: 'tag_', value: 'tag_' },
  { text: 'head.i', value: 'head_i' },
  { text: 'dep_', value: 'dep_' },
  { text: 'ent_iob_', value: 'ent_iob_' },
]
