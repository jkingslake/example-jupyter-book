# API reference


Using Autodoc2 you can generate a summary of the functions in the module.

```{autodoc2-summary}
:renderer: myst

~lumache.get_random_ingredients
~lumache.get_random_ingredients_B
```

You can also extract a single docstring. 

```{autodoc2-docstring} lumache.get_random_ingredients
    :literal:
    :literal-linenos:
    :literal-lexer: markdown
```

You can also extract formatted descriptions individual functions.

```{autodoc2-object} lumache.get_random_ingredients
render_plugin = "myst"
no_index = false
```


```{autodoc2-object} lumache.get_random_ingredients_B
render_plugin = "myst"
no_index = false
```