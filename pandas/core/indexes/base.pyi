import numpy as np
from pandas.core.arrays import ExtensionArray
from pandas.core.base import IndexOpsMixin, PandasObject
from typing import Any, Dict, Hashable, Optional, Sequence


class InvalidIndexError(Exception): ...

class Index(IndexOpsMixin, PandasObject):
    str: Any = ...
    def __new__(cls: Any, data: Any = ..., dtype: Any = ..., copy: Any = ..., name: Any = ..., tupleize_cols: Any = ..., **kwargs: Any) -> Index: ...
    @property
    def asi8(self) -> None: ...
    def is_(self, other: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype: Any = ...) -> np.ndarray: ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...) -> Any: ...
    def dtype(self) -> Any: ...
    def ravel(self, order: str = ...) -> Any: ...
    def view(self, cls: Optional[Any] = ...) -> Any: ...
    def astype(self, dtype: Any, copy: bool = ...) -> Any: ...
    def take(self, indices: Any, axis: int = ..., allow_fill: bool = ..., fill_value: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def repeat(self, repeats: Any, axis: Optional[Any] = ...) -> Any: ...
    def copy(self, name: Optional[Any] = ..., deep: bool = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def __copy__(self, **kwargs: Any) -> Any: ...
    def __deepcopy__(self, memo: Optional[Any] = ...) -> Any: ...
    def format(self, name: bool = ..., formatter: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def to_native_types(self, slicer: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def to_flat_index(self) -> Any: ...
    def to_series(self, index: Optional[Any] = ..., name: Optional[Any] = ...) -> Any: ...
    def to_frame(self, index: bool = ..., name: Optional[Any] = ...) -> Any: ...
    @property
    def name(self) -> Any: ...
    @name.setter
    def name(self, value: Any) -> None: ...
    names: Any = ...
    def set_names(self, names: Any, level: Optional[Any] = ..., inplace: bool = ...) -> Any: ...
    def rename(self, name: Any, inplace: bool = ...) -> Any: ...
    @property
    def nlevels(self) -> int: ...
    def sortlevel(self, level: Optional[Any] = ..., ascending: bool = ..., sort_remaining: Optional[Any] = ...) -> Any: ...
    get_level_values: Any = ...
    def droplevel(self, level: int = ...) -> Any: ...
    @property
    def is_monotonic(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> Any: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_integer(self) -> bool: ...
    def is_floating(self) -> bool: ...
    def is_numeric(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_categorical(self) -> bool: ...
    def is_interval(self) -> bool: ...
    def is_mixed(self) -> bool: ...
    def holds_integer(self) -> Any: ...
    def inferred_type(self) -> Any: ...
    def is_all_dates(self) -> bool: ...
    def __reduce__(self) -> Any: ...
    def hasnans(self) -> Any: ...
    def isna(self) -> Any: ...
    isnull: Any = ...
    def notna(self) -> Any: ...
    notnull: Any = ...
    def fillna(self, value: Optional[Any] = ..., downcast: Optional[Any] = ...) -> Any: ...
    def dropna(self, how: str = ...) -> Any: ...
    def unique(self, level: Optional[Any] = ...) -> Any: ...
    def drop_duplicates(self, keep: str = ...) -> Any: ...  # type: ignore
    def duplicated(self, keep: str = ...) -> Any: ...
    def __add__(self, other: Any) -> Any: ...
    def __radd__(self, other: Any) -> Any: ...
    def __iadd__(self, other: Any) -> Any: ...
    def __sub__(self, other: Any) -> Any: ...
    def __rsub__(self, other: Any) -> Any: ...
    def __and__(self, other: Any) -> Any: ...
    def __or__(self, other: Any) -> Any: ...
    def __xor__(self, other: Any) -> Any: ...
    def __nonzero__(self) -> None: ...
    __bool__: Any = ...
    def union(self, other: Any, sort: Optional[Any] = ...) -> Any: ...
    def intersection(self, other: Any, sort: bool = ...) -> Any: ...
    def difference(self, other: Any, sort: Optional[Any] = ...) -> Any: ...
    def symmetric_difference(self, other: Any, result_name: Optional[Any] = ..., sort: Optional[Any] = ...) -> Any: ...
    def get_loc(self, key: Any, method: Optional[Any] = ..., tolerance: Optional[Any] = ...) -> Any: ...
    def get_indexer(self, target: Any, method: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...) -> Any: ...
    def reindex(self, target: Any, method: Optional[Any] = ..., level: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...) -> Any: ...
    def join(self, other: Any, how: str = ..., level: Optional[Any] = ..., return_indexers: bool = ..., sort: bool = ...) -> Any: ...
    @property
    def values(self) -> Any: ...
    def array(self) -> ExtensionArray: ...
    def memory_usage(self, deep: bool = ...) -> Any: ...
    def where(self, cond: Any, other: Optional[Any] = ...) -> Any: ...
    def is_type_compatible(self, kind: Any) -> bool: ...
    def __contains__(self, key: Any) -> bool: ...
    def __hash__(self) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, key: Any) -> Any: ...
    def append(self, other: Any) -> Any: ...
    def putmask(self, mask: Any, value: Any) -> Any: ...
    def equals(self, other: Any) -> bool: ...
    def identical(self, other: Any) -> bool: ...
    def asof(self, label: Any) -> Any: ...
    def asof_locs(self, where: Any, mask: Any) -> Any: ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ...) -> Any: ...
    def sort(self, *args: Any, **kwargs: Any) -> None: ...
    def shift(self, periods: int = ..., freq: Optional[Any] = ...) -> None: ...
    def argsort(self, *args: Any, **kwargs: Any) -> Any: ...
    def get_value(self, series: Any, key: Any) -> Any: ...
    def set_value(self, arr: Any, key: Any, value: Any) -> None: ...
    def get_indexer_non_unique(self, target: Any) -> Any: ...
    def get_indexer_for(self, target: Any, **kwargs: Any) -> Any: ...
    def groupby(self, values: Any) -> Dict[Hashable, np.ndarray]: ...
    def map(self, mapper: Any, na_action: Optional[Any] = ...) -> Any: ...
    def isin(self, values: Any, level: Optional[Any] = ...) -> Any: ...
    def slice_indexer(self, start: Optional[Any] = ..., end: Optional[Any] = ..., step: Optional[Any] = ..., kind: Optional[Any] = ...) -> Any: ...
    def get_slice_bound(self, label: Any, side: Any, kind: Any) -> Any: ...
    def slice_locs(self, start: Optional[Any] = ..., end: Optional[Any] = ..., step: Optional[Any] = ..., kind: Optional[Any] = ...) -> Any: ...
    def delete(self, loc: Any) -> Any: ...
    def insert(self, loc: Any, item: Any) -> Any: ...
    def drop(self, labels: Any, errors: str = ...) -> Any: ...
    @property
    def shape(self) -> Any: ...

def ensure_index(index_like: Any, copy: bool) -> None: ...

def maybe_extract_name(name: str, obj: Any, cls: Any) -> Optional[Hashable]: ...

def _new_Index(cls: Any, d: Any) -> Any: ...

def ensure_index_from_sequences(sequences: Any, names: Optional[Sequence[str]]) -> Any: ...