# This sample exercises the type analyzer's type narrowing
# logic for assert statements, specifically for tests of the
# form "type(X) is Y" or "type(X) is not Y".

from typing import Any, Dict, Literal, Optional, Union


def func1(a: Union[str, int]) -> int:

    if type(a) is not str:
        # This should generate an error because
        # "a" is potentially a subclass of str.
        return a

    # This should generate an error because
    # "a" is provably type str at this point.
    return a


def func2(a: Optional[str]) -> str:

    if type(a) is str:
        return a

    # This should generate an error because
    # "a" is provably type str at this point.
    return a


def func3(a: Dict[str, Any]) -> str:
    val = a.get("hello")
    if type(val) is str:
        return val

    return "none"


class A:
    pass


class B(A):
    pass


def func4(a: Union[str, A]):
    if type(a) is B:
        t1: Literal["B"] = reveal_type(a)
    else:
        t2: Literal["str | A"] = reveal_type(a)
