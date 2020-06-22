Simple logical expression parser using lark-parser module.

Expression example:
```
Пол="М" AND (Возраст>25 OR (Стаж>.5 AND Должность!="Руководитель"))
```

# Use 
To get dict with AST (abstract syntax tree) use function `parse` from module `main` and pass valid logical expression string to it. (Check `parser.py` for grammar):

```python
from main import parse
print(parse('Стаж>.5 AND Должность!="Руководитель"'))

OR 

Import `ExpressionParser` from `parser` module and call parse function on it to get `lark.tree.Tree` object, that you can print with `pretty()` function:

```python
from parser import ExpressionParser as logic_parser
ast = logic_parser.parse('Стаж>.5 AND Должность!="Руководитель"')
print(ast.pretty())
```

# Test

To test call module `main.py`.
