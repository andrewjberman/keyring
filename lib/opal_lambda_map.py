"""opal_lambda_map.py -- the one Python reader of the Lambda function map (NFRA_CTLPLN TO-CT-ca-1, round 30).

The map is one JSON file per function: <repo>/infra/aws/lambda/ci/function-map/<function-name>.json, each holding the
entry object of that function alone (no wrapper; the file name is the function name). Standard library only, ASCII only.

The reader never writes. A missing folder, a missing file or an empty folder RAISES: a reader that finds nothing must
not return an empty answer that looks like a clean one (the four silent readers of the old single file did exactly that).

  load_entry(name, root=None)  the entry object of one function; FileNotFoundError naming the path when absent
  load_all(root=None)          {name: entry} for every function, sorted by name; FileNotFoundError when the folder is
                               absent, ValueError when it holds no function file

root is the repository root (default: the repository this file sits in). The folder is <root>/infra/aws/lambda/ci/function-map.
"""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(_HERE)
FOLDER_REL = os.path.join("infra", "aws", "lambda", "ci", "function-map")
SUFFIX = ".json"


def folder(root=None):
    """The function-map folder under the repository root (default: this repository)."""
    return os.path.join(REPO if root is None else root, FOLDER_REL)


def load_entry(name, root=None):
    """The entry object of one function. Raises FileNotFoundError naming the path when its file is absent."""
    path = os.path.join(folder(root), name + SUFFIX)
    if not os.path.isfile(path):
        raise FileNotFoundError("no function-map entry for %r: %s" % (name, path))
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_all(root=None):
    """{name: entry} for every function file, sorted by name. Never written back."""
    d = folder(root)
    if not os.path.isdir(d):
        raise FileNotFoundError("function-map folder is absent: %s" % d)
    names = sorted(f[:-len(SUFFIX)] for f in os.listdir(d) if f.endswith(SUFFIX))
    if not names:
        raise ValueError("function-map folder holds no function file: %s" % d)
    out = {}
    for n in names:
        with open(os.path.join(d, n + SUFFIX), encoding="utf-8") as fh:
            out[n] = json.load(fh)
    return out


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "--count":
        print("FUNCTION-MAP functions=%d folder=%s" % (len(load_all()), folder()))
        sys.exit(0)
    print("usage: opal_lambda_map.py --count")
    sys.exit(2)
