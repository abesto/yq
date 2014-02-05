yq
==

Aims to be a little brother to `jq`, but for YAML documents.

Here's an example showcasing all the syntax currently supported:

```sh
$ cat example.yaml
foo:
  bar:
    - baz
    - 3
$ cat example.yaml | python ./yq.py '.foo | {boo: .bar[1]}'
{boo: 3}
```
