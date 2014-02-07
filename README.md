yq
==

Aims to be a little brother to `jq`, but for YAML documents.

Everything from the [Basic Filters](http://stedolan.github.io/jq/manual/#Basicfilters) section of the `jq` manual is
supported - at least `yq` acts the same way as `jq` in the examples there. Object construction also more or less
works.

## Testing
There are basic unit-tests for some of the operators, but the meat of the test suite are the functional tests defined
in `functional_tests/*.yml` files and run by `run_functional_tests.py`. They're all started by `nosetests`.

## Roadmap
 - Work the same way as `jq` for the "Types and Values" section
 - Operators, functions
 - Check if operators can be refactored
 - Package, release
 - Conditionals, comparisons
 - "Advanced features", Assignment from the `jq` manual

