# huntrace

Command line interface to ionelmc's [hunter](https://github.com/ionelmc/python-hunter) tracing library.
Analogous to ltrace.

# Usage

```
# Trace the top level code in cookiecutter
> huntrace cookiecutter

# Trace the the top level and what it calls / imports in cookiecutter
> huntrace cookiecutter --depth 2

# Print the filterwarnings function call
> huntrace cookiecutter --depth 2 -f filterwarnings
```
