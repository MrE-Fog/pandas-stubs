from .masked import BaseMaskedArray as BaseMaskedArray
from pandas._libs import lib as lib
from pandas.compat import set_function_name as set_function_name
from pandas.core import nanops as nanops, ops as ops
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe

from pandas.core.dtypes.dtypes import register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.ops import invalid_comparison as invalid_comparison
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.tools.numeric import to_numeric as to_numeric
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Any, Optional, Type

class _IntegerDtype(ExtensionDtype):
    name: str
    base: Any = ...
    type: Type[Any]
    na_value: Any = ...
    def is_signed_integer(self) -> Any: ...
    def is_unsigned_integer(self) -> Any: ...
    def numpy_dtype(self) -> Any: ...
    def kind(self) -> Any: ...
    def itemsize(self) -> Any: ...
    @classmethod
    def construct_array_type(cls) -> Any: ...
    def __from_arrow__(self, array: Any) -> Any: ...

def integer_array(values: Any, dtype: Optional[Any] = ..., copy: bool = ...) -> Any: ...
def safe_cast(values: Any, dtype: Any, copy: Any) -> Any: ...
def coerce_to_array(values: Any, dtype: Any, mask: Optional[Any] = ..., copy: bool = ...) -> Any: ...

class IntegerArray(BaseMaskedArray):
    def dtype(self) -> Any: ...
    def __init__(self, values: Any, mask: Any, copy: bool = ...) -> None: ...
    def __array_ufunc__(self, ufunc: Any, method: Any, *inputs: Any, **kwargs: Any) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def astype(self, dtype: Any, copy: bool = ...) -> Any: ...

Int8Dtype: Any
Int16Dtype: Any
Int32Dtype: Any
Int64Dtype: Any
UInt8Dtype: Any
UInt16Dtype: Any
UInt32Dtype: Any
UInt64Dtype: Any
