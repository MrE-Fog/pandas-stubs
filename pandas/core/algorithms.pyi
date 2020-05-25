import numpy as np
from pandas import Series as Series
from pandas._libs import Timestamp as Timestamp, algos as algos, lib as lib
from pandas._libs.tslib import iNaT as iNaT
from pandas.core.construction import array as array, extract_array as extract_array
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike as construct_1d_object_array_from_listlike, infer_dtype_from_array as infer_dtype_from_array, maybe_promote as maybe_promote
from pandas.core.dtypes.common import ensure_float64 as ensure_float64, ensure_int64 as ensure_int64, ensure_object as ensure_object, ensure_platform_int as ensure_platform_int, ensure_uint64 as ensure_uint64, is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_complex_dtype as is_complex_dtype, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_period_dtype as is_period_dtype, is_scalar as is_scalar, is_signed_integer_dtype as is_signed_integer_dtype, is_timedelta64_dtype as is_timedelta64_dtype, is_unsigned_integer_dtype as is_unsigned_integer_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexers import validate_indices as validate_indices
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Any, Optional, Tuple, Union

def unique(values: Any) -> Any: ...
unique1d = unique

def isin(comps: Any, values: Any) -> np.ndarray: ...
def factorize(values: Any, sort: bool=..., na_sentinel: int=..., size_hint: Optional[int]=...) -> Tuple[np.ndarray, Union[np.ndarray, ABCIndex]]: ...
def value_counts(values: Any, sort: bool=..., ascending: bool=..., normalize: bool=..., bins: Any = ..., dropna: bool=...) -> Series: ...
def duplicated(values: Any, keep: Any = ...) -> np.ndarray: ...
def mode(values: Any, dropna: bool=...) -> Series: ...
def rank(values: Any, axis: int=..., method: str=..., na_option: str=..., ascending: bool=..., pct: bool=...) -> Any: ...
def checked_add_with_arr(arr: Any, b: Any, arr_mask: Optional[Any] = ..., b_mask: Optional[Any] = ...) -> Any: ...
def quantile(x: Any, q: Any, interpolation_method: str = ...) -> Any: ...

class SelectN:
    obj: Any = ...
    n: Any = ...
    keep: Any = ...
    def __init__(self, obj: Any, n: int, keep: str) -> None: ...
    def nlargest(self) -> Any: ...
    def nsmallest(self) -> Any: ...
    @staticmethod
    def is_valid_dtype_n_method(dtype: Any) -> bool: ...

class SelectNSeries(SelectN):
    def compute(self, method: Any) -> Any: ...

class SelectNFrame(SelectN):
    columns: Any = ...
    def __init__(self, obj: Any, n: int, keep: str, columns: Any) -> None: ...
    def compute(self, method: Any) -> Any: ...

def take(arr: Any, indices: Any, axis: int=..., allow_fill: bool=..., fill_value: Any = ...) -> Any: ...
def take_nd(arr: Any, indexer: Any, axis: int=..., out: Any = ..., fill_value: Any = ..., allow_fill: bool=...) -> Any: ...
take_1d = take_nd

def take_2d_multi(arr: Any, indexer: Any, fill_value: Any = ...) -> Any: ...
def searchsorted(arr: Any, value: Any, side: str = ..., sorter: Optional[Any] = ...) -> Any: ...
def diff(arr: Any, n: int, axis: int=..., stacklevel: Any = ...) -> Any: ...
def safe_sort(values: Any, codes: Any = ..., na_sentinel: int=..., assume_unique: bool=..., verify: bool=...) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]: ...
