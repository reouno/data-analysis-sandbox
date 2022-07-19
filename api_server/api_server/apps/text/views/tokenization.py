"""Text analysis APIs"""

import spacy
import spacy.tokens
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_server.apps.custom_accounts.models import CustomUser
from api_server.apps.text.models import TextData, AnalysisType
from api_server.apps.text.serializers.tokenization import TokenizationRequestSerializer, \
    TokenizationResponseSerializer, \
    TokenizationOutputFormat


class TokenizationAPI(APIView):
    """Tokenization api"""

    def post(self, request):
        """Tokenize"""
        user: CustomUser = CustomUser.objects.get_by_natural_key(self.request.user)
        request_data = TokenizationRequestSerializer(data=request.data)
        if not request_data.is_valid():
            return Response(request_data.errors, status=status.HTTP_400_BAD_REQUEST)

        text_data = request_data.validated_data['data']
        lang = request_data.validated_data['lang']
        params = request_data.validated_data['params']

        # NLP
        nlp: spacy.Language = spacy.load('ja_ginza_electra')
        doc: spacy.tokens.doc.Doc = nlp(text_data)

        if params['format'] == TokenizationOutputFormat.ALL_INFO.value:
            result = []
            for sent in doc.sents:
                tokens = []
                for tk in sent:
                    readings = tk.morph.get('Reading')
                    tokens.append({
                        'i': tk.i,
                        'orth_': tk.orth_,
                        'reading': readings[0] if len(readings) else '',
                        'lemma_': tk.lemma_,
                        'pos_': tk.pos_,
                        'tag_': tk.tag_,
                        'head_i': tk.head.i,
                        'dep_': tk.dep_,
                        'ent_iob_': tk.ent_iob_,
                    })
                result.append({
                    'raw': sent.text,
                    'wakachi': ' '.join([tk.text for tk in sent]),
                    'tokens': tokens,
                })
        else:
            wakachi_tokens = [token.text for token in doc]
            result = ' '.join(wakachi_tokens)

        textData = TextData(
            user=user,
            data=text_data,
            lang=lang,
            analysis_type=AnalysisType.TOKENIZE,
            params=params,
            result=result
        )
        textData.save()

        response_data = TokenizationResponseSerializer(data={
            'result': result,
            'lang': lang,
            'params': params,
        })
        if not response_data.is_valid():
            return Response(response_data.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data.validated_data, status=status.HTTP_200_OK)
