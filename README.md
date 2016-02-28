yq
==

Pure Python implementation of a subset of the features of
[`jq`](https://stedolan.github.io/jq/) for `YAML` documents. 

**Status**: No active development planned, maintenance work only.

If you're looking for a way to do `jq`-like filtering on `YAML` documents,
you'll probably be better off using the `yq` provided by
[`j2y`](https://github.com/wildducktheories/y2j). `y2j` provides a wrapper
around `jq` that transforms the input `YAML` into `JSON`, calls out to `jq`,
then transforms the result back. This means it automatically supports the full
feature set of `jq`.

If for some reason you need a pure python implementation, this repo is for you.

## What's implemented?

Everything from the [Basic Filters](http://stedolan.github.io/jq/manual/#Basicfilters) section of the `jq` manual is
supported - at least `yq` acts the same way as `jq` in the examples there. Object construction also more or less
works.

## Known limitations

The parsing technology used in this project (parser combinators) is powerful
enough to support parsing some of the more complex features of `jq`.

## Install dependencies

    pip install -r requirements.txt

## Install package

    pip install .

## Testing

There are basic unit-tests for some of the operators, but the meat of the test suite are the functional tests defined
in `functional_tests/*.yml` files and run by `run_functional_tests.py`.

The whole test suite of `jq` is in `functional_tests/jq.txt`, run by `run_jq_tests.py`. Sections starting with a line
containing `skip` are, surprisingly, skipped - until that functionality is implemented.

They're all started by `nosetests`

## Roadmap

Here are some steps that'd need to be taken to bring the feature set of this `yq` closer to that of `jq`.

 - Work the same way as `jq` for the "Types and Values" section
 - Operators, functions
 - Check if operators can be refactored
 - Package, release
 - Conditionals, comparisons
 - "Advanced features", Assignment from the `jq` manual
