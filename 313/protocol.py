import typing

class Vector(typing.Protocol):
    x: float
    y: float

print(typing.get_protocol_members(Vector))
print(typing.is_protocol(Vector))
