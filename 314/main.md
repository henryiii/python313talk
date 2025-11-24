---
title: What's new in Python π
sub_title: Princeton RSE 2025-11-24 • Henry Schreiner
author: https://iscinumpy.dev/post/python-314
options:
  end_slide_shorthand: true

theme:
  override:
    footer:
      style: template
      left: Henry Schreiner
      center: Princeton RSE
      right: "{current_slide} / {total_slides}"
---

Python release schedule
=======================

# Python is released every October

* **EoL**: 5 year security support, 2 year bugfixes (new)
* **SPEC 0**: 3 year support *(Science libraries)*

# Support table

| **Python** | **Release** | **EoL**  | **SPEC 0**  |
|------------|-------------|----------|-------------|
| 3.9        | 2020        | ~~2025~~ | ~~2023~~    |
| 3.10       | 2021        | 2026     | ~~2024~~    |
| 3.11       | 2022        | 2027     | ~~2025~~    |
| 3.12       | 2023        | 2028     | 2026        |
| 3.13       | 2024        | 2029     | 2027        |
| 3.14       | 2025        | 2030     | 2028        |

---


Python π (3.14)
===============

![Python 3.14 feature image](python-3.14.png)

---

Free threaded
=============

Free threaded mode is no longer experimental!

* Would require a PEP to stop it now!
* Still a separate build
* No JIT support yet
* Nearly matches single threaded performance now
* A lot more library support (`cffi`, finally!)

---

Template strings
================

Like an f-string, but doesn't turn into a string.


```python
from string.templatelib import Template, Interpolation

def to_string(template: Template) -> str:
    return "".join(
        item.value if isinstance(item, Interpolation) else item
        for item in template
    )

world = "world"
assert f"hello {world}" == to_string(t"hello {world}")
```

---

Template strings: usage
=======================


What would you use them for?

* Safe interpolation (databases, html, etc)
* Some eDSL potential

`tdom` example:


```python
>>> from tdom import html
>>>
>>> attrs = {"id": "yum", "data-act": "submit"}
>>> disabled = True
>>> t = t'<button {attrs} disabled={disabled}>Yum!</button>'
>>> node = html(t)
>>> str(node)
'<button id="yum" data-act="submit" disabled>Yum!</button>'
```

---

Color everywhere
================

* The REPL now has **syntax highlighting**!
* `--help` now is in color in `argparse`
* Many CLI's now have color too, including the new `python -m json`
* `argparse` also gets `suggest_on_error`, too.


Remote debugging
================

You can now debug one Python process from another!

```bash
python -m pdb -p <PID>
```

You can also inspect `asyncio` from another process, too!

```bash
python -m asyncio ps <PID>
python -m asyncio ptree <PID>
```

---

Error messages
==============

This continues to expand; you get the benefit just by using the latest Python!

* "Did you mean" for Python keyword typos
* Argument unpacking length hints
* `elif` following `else` dedicated message
* Highlighting for statements in the wrong place
* Better incorrectly closed string message
* Incompatible string prefix explanation
* Better messages for incompatible `as` targets
* Better JSON serialization errors with added notes

---

Faster CPython
==============

Some speedups from the Faster CPython team (fired by Microsoft earlier this year):

* Opt-in tail call interpreter (LLVM 19+), 3-5% mean, 30% max faster
* JIT now runtime opt-in on official builds, 0% faster/slower
* Faster module startup time for modules like `subprocess`, `tomllib`, `asyncio`
* `pdb` now much faster (using `sys.monitoring`)
* `sys.monitoring` now handles branching, makes libraries like coverage much faster

The *entire test runtime* of `packaging` went from 55 seconds to 35 seconds!

---

Subinterpreters
===============

Not happy with free-threading? Supinterpeters finally landed in pure Python!

(Available since 3.12 for C extensions)

* Low level: `concurrent.interpreters`
* High level: `concurrent.futures.InterpreterPoolExecutor`

This is a different model than free-threading, you can do things like load
different versions of libraries in each interpreter!

Communication between subinterpreters is pretty basic at the moment.

---

Static typing
=============

Deferred evaluation has landed! (PEP 649/749)

(No more `from __future__ import annotations` required)

* New `annotationlib` for working with annotations
    * High level functions updated to work correctly, too
* Unions now unified (`A | B` identical to `Union[A, B]`)
* `memoryview` is now generic

---


Compression
===========

New `compression.zstd` library, for the popular `zstd` compression format!

Can now access all other compression libraries from `compression.*` too.


---

Other features
==============


* No parens required for multiple exceptions (Python 2 holdout)
* `pathlib.Path` new methods for moving/copying and `.info` attribute
* `map` supports `strict=True` (like `zip` in 3.10+)
* `python -c` finally dedents code
* `ast` module improvements
* `functools.Placeholder`
* `inspect.ispackage()`
* `os.reload_environ()`

See https://iscinumpy.dev/post/python-314/ for more!


---

Developer changes
=================

* `SyntaxWarning` for control flow inside `finally:`
* iOS testing/output improvements
* Complex arithmetic now matches C99
* `forkserver` default instead of `fork` on Linux
* Pickle default protocol now 5
* Windows finally includes ABIFLAGS in `sysconfig.get_config_vars()`

See https://iscinumpy.dev/post/python-314/ for more!


---

Future: 3.15 and beyond
=======================

These features are coming next year and might change before release!

---

Future: 3.15 alpha 2
====================

* Unicode by default
* `python -m profiling.sampling`, up to 1,000,000 Hz
* Error messages suggest similar *nested* attributes
* Can specify regular expressions for warnings (surround with `/`)


---

Future: Accepted PEPs
=====================

* `math.integer` submodule
* Typed extras on `TypedDict`
* `PyModExport`: New entryppoint for C extensions
* `PyBytesWriter`: C API for making `bytes`
* And: Explicit lazy imports!

```python
lazy import slow_to_import
lazy from slow_mod import slow_func

def might_not_be_called():
    slow_to_import.func()
    slow_func()
```

---

Future: Open PEPs
=================

* `frozendict` (better subinterperter sharing)
* Stable ABI for free-threading
* Unpacking in comprehensions

```python
a = [1, 2, 3]
b = [*a for _ in range(2)]
b == [1, 2, 3, 1, 2, 3]
```

---

Summary
=======

![Python 3.14 feature image](python-3.14.png)
