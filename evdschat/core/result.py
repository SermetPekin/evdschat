from dataclasses import dataclass
import pandas as pd

from evdspy.EVDSlocal.index_requests.get_series_indexes_exp import Result

from enum import Enum
from typing import Any


class Status(Enum):
    success = 1
    failed = 0
    unknown = 2


@dataclass
class ResultChat(Result):
    status: Status = Status.unknown
    reason: str = ""

    def __str__(self):
        content = super().__str__()
        return (
            f"""
    ! get_series_exp function returns instance of this class 
    <ResultChat>
    status   : {self.status.name}   => Indicates the status of the result
    reason   : {self.reason}        => Provides additional context if the status is not success
    data     : pd.DataFrame         => Contains data [same as what get_series function returns] 
    metadata : pd.DataFrame         => Contains metadata if available 
    write    : Callable             => Creates an Excel file with data and metadata in two sheets 
    to_excel : Callable             => Same as write to meet pandas to_excel function 
    
    """
            + content
        )


def create_result(result: Any, status: Status = None, reason: str = "") -> ResultChat:
    if status is None:
        status = Status.unknown

    if isinstance(result, Result):
        return ResultChat(
            data=result.data,
            metadata=result.metadata,
            write=result.write,
            status=status,
            reason=reason,
        )

    if isinstance(result, pd.DataFrame):
        r = Result(data=result, metadata=pd.DataFrame(), write=None)
        return ResultChat(
            data=r.data,
            metadata=r.metadata,
            write=r.write,
            status=status,
            reason=reason,
        )

    if result is None:
        r = Result(data=pd.DataFrame(), metadata=pd.DataFrame(), write=None)
        return ResultChat(
            data=r.data,
            metadata=r.metadata,
            write=r.write,
            status=status,
            reason=reason,
        )


__all__ = ["ResultChat"]
