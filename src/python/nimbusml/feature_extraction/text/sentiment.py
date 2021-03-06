# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Sentiment
"""

__all__ = ["Sentiment"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.feature_extraction.text.sentiment import \
    Sentiment as core
from ...internal.utils.utils import trace


class Sentiment(core, BaseTransform, TransformerMixin):
    """

    Scores natural language text and assesses
    the probability the sentiments are positive.

    .. remarks::
        The ``Sentiment`` transform returns the probability that the
        sentiment of a natural text is positive.  The model
        was trained with the :py:class:`WordEmbedding
        <nimbusml.feature_extraction.text.WordEmbedding>` and
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`
        on Twitter sentiment
        data, similarly to the sentiment analysis part of the `Text Analytics
        cognitive service <https://www.microsoft.com/cognitive-services/en-
        us/text-analytics-api>`_.
        The transform outputs a score between 0 and 1 as a sentiment
        prediction (where 0 is a negative sentiment and 1 is a positive
        sentiment). Currently it
        supports only English.

    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`,
        :py:class:`WordEmbedding
        <nimbusml.feature_extraction.text.WordEmbedding>`.

    .. index:: transform, text, sentiment, nlp

    Example:
       .. literalinclude:: /../nimbusml/examples/Sentiment.py
              :language: python
    """

    @trace
    def __init__(
            self,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
