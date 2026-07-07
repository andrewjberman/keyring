"""
ses-sender-lint -- enforce CLAUDE.md Rule 23: every SES send must use an opalinvest.dev sender.

THE BUG CLASS IT CATCHES: a `ses.send_email`/`send_raw_email` call (or the `EMAIL_FROM`/
`SES_SENDER` env var it reads its Source= from) hardcoded to a non-opalinvest.dev address.
opalinvest.com is address-verified only (DKIM NOT_STARTED, SPF excludes SES) -- EOP
quarantines it NONDETERMINISTICALLY (a silent coin-flip, not a clean fail). opalcapital.com
is unverified entirely. Only opalinvest.dev is DKIM-signed + DMARC-aligned and delivers
clean (Andrew-direct 2026-07-07, after `infrastructure_monitor`'s hardcoded
andrew@opalinvest.com caused the partner-etl-ops-alerts P1 quarantine incident).

Two scan surfaces (CLAUDE.md Rule 23's own two clauses):
  1. Python: an `X.send_email(...)`/`X.send_raw_email(...)` call whose `Source=` keyword is a
     STRING LITERAL not on opalinvest.dev; OR a module-level `NAME = os.environ.get(ENV,
     'default@domain')` binding whose name looks like an email-sender constant (EMAIL_FROM /
     SES_SENDER / *_SENDER / *_EMAIL_FROM) with a literal default not on opalinvest.dev --
     this is the exact shape of the incident (a hardcoded fallback that fires the moment the
     env var is unset, silently).
  2. Terraform: a literal `EMAIL_FROM = "..."` / `SES_SENDER = "..."` Lambda environment-
     variable assignment not on opalinvest.dev.

Non-literal Source= (a bare variable/expression) is NOT flagged here -- it traces back to
whatever env var/constant sets it, which IS covered by surface 1's env-default check, so
double-flagging the same root cause at two sites would just be noise.

Invoke:
  python org/modules/graph/ses_sender_lint_cli.py <file.py|file.tf> [...]   # exit 1 if any finding
  python org/modules/graph/ses_sender_lint_cli.py --self-test

Author: 0.7.0_AE_CloudOps~B (ses-sender-lint TO, CLAUDE.md Rule 23, 2026-07-07).
"""
from __future__ import annotations

import argparse
import ast
import re
import sys

ALLOWED_DOMAIN = "opalinvest.dev"
_SES_SEND_METHODS = {"send_email", "send_raw_email"}
_SENDER_NAME_RE = re.compile(r"(?i)(^|_)(email_from|ses_sender|sender)($|_)")
_EMAIL_LITERAL_RE = re.compile(r"^[^\s@]+@([^\s@]+)$")


def _domain_of(value: str) -> str | None:
    m = _EMAIL_LITERAL_RE.match(value.strip())
    return m.group(1).lower() if m else None


def _is_allowed(value: str) -> bool:
    domain = _domain_of(value)
    return domain is None or domain == ALLOWED_DOMAIN


def _is_send_call(node: ast.Call) -> bool:
    return isinstance(node.func, ast.Attribute) and node.func.attr in _SES_SEND_METHODS


def _source_kwarg(node: ast.Call) -> ast.AST | None:
    for kw in node.keywords:
        if kw.arg == "Source":
            return kw.value
    return None


def _env_default(node: ast.Call) -> ast.AST | None:
    """If node is os.environ.get(name, default), return the default node."""
    func = node.func
    is_env_get = (
        isinstance(func, ast.Attribute) and func.attr == "get"
        and isinstance(func.value, ast.Attribute) and func.value.attr == "environ"
        and isinstance(func.value.value, ast.Name) and func.value.value.id == "os"
    )
    if not is_env_get or len(node.args) < 2:
        return None
    return node.args[1]


def check_python_source(src: str, filename: str = "<src>") -> list[dict]:
    """Return one finding dict per offending sender: {file, line, kind, value}."""
    try:
        tree = ast.parse(src, filename=filename)
    except SyntaxError:
        return []  # not this lint's job -- py_compile/ds-precommit-check already own syntax
    out: list[dict] = []
    # surface 1a: ses.send_email(..., Source="literal@bad-domain", ...)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _is_send_call(node):
            src_node = _source_kwarg(node)
            if isinstance(src_node, ast.Constant) and isinstance(src_node.value, str):
                if not _is_allowed(src_node.value):
                    out.append({
                        "file": filename, "line": getattr(node, "lineno", 0),
                        "kind": "send-call-literal", "value": src_node.value,
                    })
    # surface 1b: NAME = os.environ.get(ENV, 'default@bad-domain') where NAME/ENV looks like
    # a sender constant. Assign-based (not a bare Call walk) so the target NAME is available
    # in the same pass as the RHS call.
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        default_node = None
        if isinstance(node.value, ast.Call):
            default_node = _env_default(node.value)
        if default_node is None:
            continue
        if not (isinstance(default_node, ast.Constant) and isinstance(default_node.value, str)):
            continue
        if _is_allowed(default_node.value):
            continue
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        env_arg = node.value.args[0] if node.value.args else None
        env_name = env_arg.value if isinstance(env_arg, ast.Constant) and isinstance(env_arg.value, str) else ""
        if any(_SENDER_NAME_RE.search(n) for n in names) or _SENDER_NAME_RE.search(env_name):
            out.append({
                "file": filename, "line": node.lineno,
                "kind": "env-default-literal", "value": default_node.value,
            })
    return out


def check_file(path: str) -> list[dict]:
    if path.endswith(".py"):
        with open(path, encoding="utf-8", errors="replace") as fh:
            return check_python_source(fh.read(), filename=path)
    if path.endswith(".tf"):
        return check_tf_file(path)
    return []


_TF_VAR_RE = re.compile(r'\b(EMAIL_FROM|SES_SENDER)\s*=\s*"([^"]*)"')


def check_tf_source(text: str, filename: str = "<src>") -> list[dict]:
    out: list[dict] = []
    for i, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        m = _TF_VAR_RE.search(line)
        if m and not _is_allowed(m.group(2)):
            out.append({
                "file": filename, "line": i,
                "kind": f"tf-env-literal-{m.group(1)}", "value": m.group(2),
            })
    return out


def check_tf_file(path: str) -> list[dict]:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return check_tf_source(fh.read(), filename=path)


def _selftest() -> int:
    # -- Python: send call with a bad literal Source= --
    bad_call = 'import boto3\nses = boto3.client("ses")\nses.send_email(Source="andrew@opalinvest.com", Destination={}, Message={})\n'
    r = check_python_source(bad_call)
    assert r and r[0]["kind"] == "send-call-literal", "literal opalinvest.com Source= must FLAG"

    # -- Python: send call with a good literal --
    good_call = 'import boto3\nses = boto3.client("ses")\nses.send_email(Source="noreply@opalinvest.dev", Destination={}, Message={})\n'
    assert not check_python_source(good_call), "opalinvest.dev Source= must NOT flag"

    # -- Python: send call with a non-literal Source= (variable) -- not flagged here (env-default
    # site owns it, avoids double-report of the same root cause) --
    var_call = 'ses.send_email(Source=SENDER, Destination={}, Message={})\n'
    assert not check_python_source(var_call), "non-literal Source= must NOT flag at the call site"

    # -- Python: EMAIL_FROM env-default on a bad domain (the real 2026-07-07 incident shape) --
    bad_default = "import os\nEMAIL_FROM = os.environ.get('EMAIL_FROM', 'trades@opalcapital.com')\n"
    r = check_python_source(bad_default)
    assert r and r[0]["kind"] == "env-default-literal", "bad-domain EMAIL_FROM default must FLAG"

    # -- Python: EMAIL_FROM env-default on the correct domain --
    good_default = "import os\nEMAIL_FROM = os.environ.get('EMAIL_FROM', 'trades@opalinvest.dev')\n"
    assert not check_python_source(good_default), "opalinvest.dev EMAIL_FROM default must NOT flag"

    # -- Python: an unrelated os.environ.get default must NOT flag (no sender-shaped name) --
    unrelated = "import os\nS3_BUCKET = os.environ.get('S3_BUCKET', 'trades@notasenderdomain.example')\n"
    assert not check_python_source(unrelated), "a non-sender-named constant must NOT flag"

    # -- Terraform: bad EMAIL_FROM --
    bad_tf = '      EMAIL_FROM        = "trades@opalcapital.com"\n'
    r = check_tf_source(bad_tf)
    assert r and r[0]["kind"] == "tf-env-literal-EMAIL_FROM", "bad-domain TF EMAIL_FROM must FLAG"

    # -- Terraform: good EMAIL_FROM --
    good_tf = '      EMAIL_FROM        = "trades@opalinvest.dev"\n'
    assert not check_tf_source(good_tf), "opalinvest.dev TF EMAIL_FROM must NOT flag"

    # -- Terraform: a commented-out line must NOT flag --
    commented_tf = '      # EMAIL_FROM = "trades@opalcapital.com"\n'
    assert not check_tf_source(commented_tf), "a commented TF line must NOT flag"

    print("SELF-TEST PASS: 9/9 (send-call literal bad/good/non-literal, env-default bad/good/"
          "unrelated, TF bad/good/commented)")
    return 0


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="ses-sender-lint",
        description="Flag any SES sender (Python send_email/send_raw_email Source=, or "
                    "Terraform EMAIL_FROM/SES_SENDER) not on the opalinvest.dev domain "
                    "(CLAUDE.md Rule 23).",
    )
    ap.add_argument("files", nargs="*", help="python or terraform files to lint")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return _selftest()
    if not a.files:
        ap.print_help()
        return 0
    total = 0
    for f in a.files:
        try:
            found = check_file(f)
        except OSError as e:
            print(f"SKIP: {f} ({e})", file=sys.stderr)
            continue
        for v in found:
            total += 1
            print(
                f"{v['file']}:{v['line']}  non-opalinvest.dev SES sender ({v['kind']}): "
                f"{v['value']!r}",
                file=sys.stderr,
            )
    if total:
        print(
            f"\nBLOCKED: {total} SES sender(s) not on opalinvest.dev (CLAUDE.md Rule 23) -- "
            f"opalinvest.com is unauthenticated (nondeterministic EOP quarantine risk), "
            f"opalcapital.com is unverified. Use an opalinvest.dev sender (e.g. noreply@opalinvest.dev).",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
