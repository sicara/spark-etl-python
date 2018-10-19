#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `spark_etl_python` package."""


from __future__ import print_function
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal


pytestmark = pytest.mark.usefixtures("spark_context")


def test_content():
    df_expected = pd.DataFrame({'a': [0]})
    df_actual = pd.DataFrame({'a': [0]})
    assert_frame_equal(df_expected, df_actual)

from operator import add


def do_word_counts(lines):
    """ count of words in an rdd of lines """

    counts = (lines.flatMap(lambda x: x.split())
                  .map(lambda x: (x, 1))
                  .reduceByKey(add)
             )
    results = {word: count for word, count in counts.collect()}
    return results


def test_do_word_counts(spark_context):
    """ test that a single event is parsed correctly
    Args:
        spark_context: test fixture SparkContext
        hive_context: test fixture HiveContext
    """

    test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]

    input_rdd = spark_context.parallelize(test_input, 1)
    results = do_word_counts(input_rdd)

    expected_results = {'hello': 2, 'spark': 3, 'again': 1}
    assert results == expected_results
