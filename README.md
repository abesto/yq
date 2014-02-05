yq
==

Aims to be a little brother to `jq`, but for YAML documents.

Here's an example showcasing all the syntax currently supported:

```sh
(virtualenv)9:54:00 abesto@pro yq master ? cat example.yaml
foo:
  bar:
    - baz
    - 3
(virtualenv)9:54:21 abesto@pro yq master ? cat example.yaml | python ./yq.py '.foo | {boo: .bar[1]}'
{boo: 3}
```
