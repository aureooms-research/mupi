# MUPI

Experiment with Merging under Partial Information

## Use

```sh
python3 information.py 450 450 > data/450-450
/usr/bin/diff <(python3 linext.py data/450-450) <(python3 merge.py <(python3 erase.py data/450-450) data/450-450 -v)
```
