"""LDO-001 mode-default gate (COMM_ASSIST CA-k-2, round 19; a gate, not an alert).

Compares the trunk default of the variable chat_assist_ingress_mark_mode with the live INGRESS_MARK_MODE of the
two Lambda functions of module "ldo_001" (handler and ingress). safe-apply.sh runs this before any apply that
covers module.ldo_001 and refuses the apply on anything but OK.

Usage, from the repository root, by relative path:
    python .tools/ldo001-mode-default-check.py --tf PATH [--live-json PATH]

  --tf PATH          the Terraform file holding the variable and the module. REQUIRED: no path is hand-typed here
                     (the naming gate refuses a literal registry name, and no registry row gives this file's path),
                     so an absent --tf is NO-VERDICT.
  --live-json PATH   the test seam: a JSON dict, or a list of dicts, each shaped like the output of
                     `lambda get-function-configuration`. Without it the live read is that call, read-only,
                     through the .tools/aws shim, once per function.

The function names are lib/opal_naming.py name() output for the module block's system, scope and function with
the kinds handler and ingress, never typed (the same names the module's own name() calls build).

Last stdout line: LDO001-MODE verdict=<OK|REFUSED|NO-VERDICT> default=<v> live=<v>
Exit 0 only for OK; 1 for REFUSED; 2 for NO-VERDICT. Notes go to stderr.
  OK          every live value equals the default.
  REFUSED     a live value differs from the default, or the two functions disagree with each other.
  NO-VERDICT  anything unreadable: the file, the variable, the default (absent or not a mode), the module block
              or its names, the JSON, the key, or the AWS call. NO-VERDICT refuses too.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHIM = ".tools/aws"
VAR = "chat_assist_ingress_mark_mode"
MODULE = "ldo_001"
KEY = "INGRESS_MARK_MODE"
MODES = ("off", "record", "enforce")
KINDS = ("handler", "ingress")


class Unreadable(Exception):
    pass


def block_body(text, head):
    """The body of the first block opened by head (a regex) and closed by a brace at column 0, or None."""
    m = re.search(head + r"\s*\{(.*?)^\}", text, re.S | re.M)
    return m.group(1) if m else None


def tf_default(text):
    body = block_body(text, r'variable\s+"%s"' % VAR)
    if body is None:
        raise Unreadable("variable %s is not declared" % VAR)
    m = re.search(r'^\s*default\s*=\s*"([^"]*)"\s*(#.*)?$', body, re.M)
    if not m:
        raise Unreadable("variable %s has no quoted default" % VAR)
    if m.group(1) not in MODES:
        raise Unreadable("the default %r is not one of %s" % (m.group(1), "/".join(MODES)))
    return m.group(1)


def module_names(text):
    body = block_body(text, r'module\s+"%s"' % MODULE)
    if body is None:
        raise Unreadable("module %s is not declared" % MODULE)
    got = {}
    for key in ("system", "scope", "function"):
        m = re.search(r'^\s*%s\s*=\s*"([^"]+)"' % key, body, re.M)
        if not m:
            raise Unreadable("module %s has no literal %s" % (MODULE, key))
        got[key] = m.group(1)
    sys.path.insert(0, str(ROOT / "lib"))
    from opal_naming import name as opal_name
    return [opal_name(got["system"], got["scope"], got["function"], "lambda", kind) for kind in KINDS]


def aws_configs(names):
    sys.path.insert(0, str(ROOT / ".tools"))
    from git_bash_resolver import git_bash
    bash = git_bash()
    if not bash:
        raise Unreadable("no Git Bash to run the .tools/aws shim")
    out = []
    for fn in names:
        r = subprocess.run([bash, SHIM, "lambda", "get-function-configuration", "--function-name", fn, "--output", "json"],
                           capture_output=True, text=True, encoding="utf-8", timeout=90, cwd=str(ROOT))
        if r.returncode != 0:
            raise Unreadable("aws lambda get-function-configuration %s exited %d" % (fn, r.returncode))
        out.append(json.loads(r.stdout))
    return out


def seam_configs(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list) and data:
        return data
    raise Unreadable("the live JSON is neither a dict nor a non-empty list")


def live_values(configs):
    values = []
    for c in configs:
        env = c.get("Environment") if isinstance(c, dict) else None
        variables = env.get("Variables") if isinstance(env, dict) else None
        val = variables.get(KEY) if isinstance(variables, dict) else None
        if not isinstance(val, str) or not val:
            raise Unreadable("no %s in a live configuration" % KEY)
        values.append(val)
    return values


def check(tf, live_json):
    """Returns (verdict, default, live, rc)."""
    try:
        text = Path(tf).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print("LDO001-MODE note: the .tf file is unreadable (%s)" % exc.__class__.__name__, file=sys.stderr)
        return "NO-VERDICT", "-", "-"
    try:
        default = tf_default(text)
    except Unreadable as exc:
        print("LDO001-MODE note: %s" % exc, file=sys.stderr)
        return "NO-VERDICT", "-", "-"
    try:
        if live_json is not None:
            configs = seam_configs(live_json)
        else:
            configs = aws_configs(module_names(text))
        values = live_values(configs)
    except Exception as exc:  # any failure of the live read is NO-VERDICT, whatever its class
        print("LDO001-MODE note: the live read failed (%s: %s)" % (exc.__class__.__name__, exc), file=sys.stderr)
        return "NO-VERDICT", default, "-"
    live = "+".join(dict.fromkeys(values))
    if all(v == default for v in values):
        return "OK", default, live
    return "REFUSED", default, live


def main(argv):
    tf = None
    live_json = None
    args = list(argv)
    while args:
        a = args.pop(0)
        if a == "--tf" and args:
            tf = args.pop(0)
        elif a == "--live-json" and args:
            live_json = args.pop(0)
        else:
            print("LDO001-MODE note: unknown or incomplete argument %r" % a, file=sys.stderr)
            print("LDO001-MODE verdict=NO-VERDICT default=- live=-")
            return 2
    if tf is None:
        print("LDO001-MODE note: --tf PATH is required", file=sys.stderr)
        print("LDO001-MODE verdict=NO-VERDICT default=- live=-")
        return 2
    verdict, default, live = check(tf, live_json)
    print("LDO001-MODE verdict=%s default=%s live=%s" % (verdict, default, live))
    return {"OK": 0, "REFUSED": 1}.get(verdict, 2)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
