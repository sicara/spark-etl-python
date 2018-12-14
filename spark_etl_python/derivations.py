# -*- coding: utf-8 -*-
from pyspark.sql.functions import concat_ws


def derive_full_address(personal_info_rdd, address_columns, full_address_column_name='full_address'):
    full_address_column = concat_ws("", *address_columns)
    personal_info_with_full_address_rdd = personal_info_rdd.withColumn(full_address_column_name, full_address_column)
    return personal_info_with_full_address_rdd
