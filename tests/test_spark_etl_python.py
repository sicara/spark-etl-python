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

def filter_df(df):
    return df.filter(df.year >= 2000)


def assert_frame_equal_with_sort(results, expected, keycolumns):
    results_sorted = results.sort_values(by=keycolumns).reset_index(drop=True)
    expected_sorted = expected.sort_values(by=keycolumns).reset_index(drop=True)
    assert_frame_equal(results_sorted, expected_sorted)

def test_do_filter(sql_context):
    """ test that a single event is parsed correctly
    Args:
        sql_context: test fixture SQLContext
    """
    data_pandas = pd.DataFrame({'make': ['Jaguar', 'MG', 'MINI', 'Rover', 'Lotus'],
                                'registration': ['AB98ABCD', 'BC99BCDF', 'CD00CDE', 'DE01DEF', 'EF02EFG'],
                                'year': [1998, 1999, 2000, 2001, 2002]})

    input_rdd = sql_context.createDataFrame(data_pandas)
    results_df = filter_df(input_rdd).toPandas()
    expected_results = pd.DataFrame({'make': ['Rover', 'Lotus', 'MINI'],
                                     'registration': ['DE01DEF', 'EF02EFG', 'CD00CDE'],
                                     'year': [2001, 2002, 2000]})
    assert_frame_equal_with_sort(expected_results, results_df, ['make'])
