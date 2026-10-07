# py_bracket_validator

## Description

`py_bracket_validator` is a Python exercise from the Codam / 42 Rank 03 exam practice set.

The goal is to implement a function that determines whether all brackets in a string are correctly matched and properly nested.

Supported brackets are:

```text
()
[]
{}
```

Characters that are not brackets are ignored.

---

## Function

```python
def bracket_validator(s: str) -> bool:
```

The function returns:

- `True` if all brackets are correctly matched and nested.
- `False` otherwise.

---

## Examples

```python
bracket_validator("()")
# True
```

```python
bracket_validator("()[]{}")
# True
```

```python
bracket_validator("(]")
# False
```

```python
bracket_validator("([)]")
# False
```

```python
bracket_validator("{[]}")
# True
```

```python
bracket_validator("hello(world)")
# True
```

```python
bracket_validator("((())")
# False
```

```python
bracket_validator("")
# True
```
