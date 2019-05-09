from typing import Union, overload, Any, List


@overload
def double(i: int) -> int:
    ...


@overload
def double(i: str) -> str:
    ...


# Wrong
# def double(i: Union[str, int, List[Any]]) -> Union[str, int, List[Any]]:
#     return i * 2


def double(i):
    return i * 2


print(double(2))
print(double("hello"))
print(double(0.3))
