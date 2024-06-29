---
title: The two flavors of Python 3.13
sub_title: PyHEP 2024 • Henry Schreiner
author: https://iscinumpy.dev/post/python-313
options:
  end_slide_shorthand: true

theme:
  override:
    footer:
      style: template
      left: Henry Schreiner
      center: PyHEP 2024
      right: "{current_slide} / {total_slides}"
---

# Python release schedule

## Python is released every October

* **EoL**: 5 year security support window
* **SPEC 0**: 3 year support *(Science libraries)*

## Support table

| **Python** | **Release** | **EoL**  | **SPEC 0**  |
|--------|---------|------|----------|
| 3.8    | 2019    | 2024 | ~~2022~~ |
| 3.9    | 2020    | 2025 | ~~2023~~ |
| 3.10   | 2021    | 2026 | 2024     |
| 3.11   | 2022    | 2027 | 2025     |
| 3.12   | 2023    | 2028 | 2026     |
| 3.13   | 2024    | 2029 | 2027     |

---

# Reminder for past versions

<!-- column_layout: [4, 3] -->

<!-- column: 0 -->

## Python 3.10

* Pattern matching
* Type unions
* Much better errors

## Python 3.11

* Fastest version of Python yet
* Exception groups and notes
* Built-in TOML support
* Annotated tracebacks

## Python 3.12

* Typing Generics
* Native f-strings
* Per-interpreter GIL(\*)
* Partial Perf support

## Python 3.13

Releasing this October! Beta 3 is already out.

<!-- column: 1 -->

```python
match item:
    case int(x):
        print("Integer", x)
    case _:
        print("Not integer")
```

```python
try:
    ...
except* TypeError as err:
    ...
except* KeyError as err:
    ...
```

```python
from numbers import Real

def f[T: Real](x: T) -> T:
    return 2 * x
```

---

<!-- jump_to_middle -->


**Python 3.13 is the most forward thinking version of Python ever.**

---


# Major new features

<!-- new_line -->

<!-- column_layout: [1, 1] -->

<!-- column: 0 -->


## New REPL

For the first time in 30 years, rewritten in Python!

## Static typing

Several new features, including a bit of new syntax!

<!-- column: 1 -->

## JIT compiler (optional)

Can be enabled when compiling! Only a few percent _slower_ currently.

## Free threading (optional)

Second half of the talk on this one!

<!-- reset_layout -->

<!-- new_line -->

# Smaller features


**Typing improvements**: `TypeIs` • Generics defaults • Protocol additions • `ReadOnly`

`@warnings.deprecated` • `process_cpu_count()` • `math.fma()` • `Path.from_uri()`

`python -m random` • 19 modules removed • `2to3` removed • Incremental Garbage collector

iOS support • Perf without frame pointers • 2-year full support window


---

# New REPL


First thing you see when you start up Python!

## Demo

<!-- pause -->

* Color prompt!
* Multiline input
    * Automatic indentation
    * Up/down arrow keys
* `help`, `exit`, `quit` commands
* **F1**: Help mode
* **F2**: History mode
* **F3**: Paste mode


Disable with `PYTHON_BASIC_REPL` if you like the pain of the old one!

Based on the PyPy REPL.


---

# Color Exceptions

Like the new REPL, exceptions also have color!

![Color Error](color_err.png)

* Control with `FORCE_COLOR` / `NO_COLOR`

---



# New error messages

## Mistyped keyword suggests matches

```python
print("hi", endl="")
```
TypeError: print() got an unexpected keyword argument 'endl'. Did you mean 'end'?

<!-- pause -->

## Attributes from global/installed modules covered by local ones

```bash
touch pathlib.py
python -c "import pathlib; pathlib.Path"
```


AttributeError: module 'pathlib' has no attribute 'Path' (consider renaming '/Users/henryschreiner/git/presentations/python313/pathlib.py' since it has the same name as the standard library module named 'pathlib' and the import system gives it precedence)

Note this does not work with `from X import Y` syntax, only `AttributeError`'s.

---

# Typing features

## TypeIs

Similar to `TypeGaurd`, but narrows out the matched type!

```python
def is_string(x: int | str) -> TypeGuard[str]:
    return isinstance(x, str)

if not is_string(value):
    typing.reveal_type(value)
# Revealed type is 'int | str'
```

```python
def is_string(x: int | str) -> TypeIs[str]:
    return isinstance(x, str)

if not is_string(value):
    typing.reveal_type(value)
# Revealed type is 'int'
```

---

# Typing features

## Generics defautls

```python
@dataclass
class Box[T = int]:
    value: T | None = None
```

This can be used without specifying `T`! What common thing is this useful for?

<!-- pause -->

```python
def f() -> Generator[int, None, None]:
    yield 42
```
Is now just:
```python
def f() -> Generator[int]:
    yield 42
```

---

# Almost a typing feature

## Deprecated

New decorator for deprecated code that supports type checking too!

```python
@warnings.deprecated("msg")
def function():
   return "Don't use me!"
```

The backport is `typing_extensions.deprecated("msg")`.

## Argparser

There's also a new `deprecated=` parameter for `argparser` methods too!


---

# Other typing features

## New Protocol functions

```python
import typing

class Vector(typing.Protocol):
    x: float
    y: float

print(typing.get_protocol_members(Vector)) # {'x', 'y'}
print(typing.is_protocol(Vector)) # True
```

## ReadOnly dict items

```python
class Movie(TypedDict):
   title: ReadOnly[str]
   year: int
```
