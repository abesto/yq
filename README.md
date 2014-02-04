yq
==

Aims to be a little brother to `jq`, but for YAML documents. Currently a proof of concept, supports only the dot
and array subscript operation:

```sh
(virtualenv)21:38:28 abesto@pro yq master ? cat example.yaml | ./yq.py '.'
foo:
  bar: [baz, 3]

(virtualenv)21:38:33 abesto@pro yq master ? cat example.yaml | ./yq.py '.foo'
bar: [baz, 3]

(virtualenv)21:39:15 abesto@pro yq master ? cat example.yaml | ./yq.py '.foo.bar'
[baz, 3]

(virtualenv)22:02:51 abesto@pro yq master ? cat example.yaml | ./yq.py '.foo.bar[1]'
3
```
