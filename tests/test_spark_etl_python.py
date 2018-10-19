#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `spark_etl_python` package."""

import pandas as pd
from pandas.testing import assert_frame_equal


def test_content():
    df_expected = pd.DataFrame({'a': [0]})
    df_actual = pd.DataFrame({'a': [0]})
    assert_frame_equal(df_expected, df_actual)
