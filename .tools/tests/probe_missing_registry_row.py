#!/usr/bin/env python3
"""probe_missing_registry_row.py -- NFRA_CTLPLN round 4 cell CT-d-8: what does the Terraform apply path's naming gate
do with a well-named resource that has NO registry row?

Stand-ins only: no AWS call, no terraform, no backend. Three synthetic `terraform show -json` plans, each ADDING one
aws_lambda_function, are fed to .tools/naming-apply-gate.py exactly as .tools/safe-apply.sh feeds it its rendered
plan (safe-apply.sh lines 181-185): `python .tools/naming-apply-gate.py --plan-json FILE`, no --enforce flag, the
mode read by the gate itself from NAMING_GATE_ENFORCE=1 or the file org/mcp/naming-gate.enforce. A case is
`refused` when the gate exits non-zero AND prints its `NAMING-PLAN: REFUSE` line (what safe-apply.sh turns into
exit 7 in ENFORCE), `admitted` when the gate exits 0 with no REFUSE summary, `error` otherwise.

  (A) registered   : the name of an existing resources.json row (the order's recipe). Measured finding: no row's name
                     is builder-conformant, so this case is a REGISTERED name, not a registered WELL-NAMED one.
  (B) unregistered : a lib/opal_naming.name() output from registry vocabulary, text-counted absent from the registry.
  (C) badly named  : the positive control -- the gate must refuse it, or the gate was not exercised.

LAST line: MISSING-ROW-PROBE registered_wellnamed=.. unregistered_wellnamed=.. badly_named=.. gate_mode=.. ok=..
Standard library only. ASCII only. Edits no gate and no registry file.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
GATE = os.path.join(REPO, ".tools", "naming-apply-gate.py")
REGISTRY_DIR = os.path.join(REPO, "infra", "logic", "registry")
ENFORCE_FILE = os.path.join(REPO, "org", "mcp", "naming-gate.enforce")
TF_TYPE = "aws_lambda_function"   # NAMING_SCHEMA.json tf_type_map: node type LAMBDA, own-name attribute function_name
NODE_TYPE = "LAMBDA"
BAD_NAME = "bd_probe_lambda"       # underscores, a legacy prefix: not a name opal_naming.name() can produce


def load_builder():
    path = os.path.join(REPO, "lib", "opal_naming.py")
    loader = importlib.machinery.SourceFileLoader("opal_naming_probe", path)
    spec = importlib.util.spec_from_loader("opal_naming_probe", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def registry_text():
    out = {}
    for fn in sorted(os.listdir(REGISTRY_DIR)):
        if fn.endswith(".json"):
            with open(os.path.join(REGISTRY_DIR, fn), "rb") as fh:
                out[fn] = fh.read().decode("utf-8")
    return out


def count_in_registry(texts, token):
    needle = '"%s"' % token
    return sum(t.count(needle) for t in texts.values())


def gate_mode():
    if os.environ.get("NAMING_GATE_ENFORCE") == "1" or os.path.exists(ENFORCE_FILE):
        return "ENFORCE"
    return "WARN"


def plan_for(address, name):
    return {"format_version": "1.2", "resource_changes": [{
        "address": address, "mode": "managed", "type": TF_TYPE, "name": address.split(".")[-1],
        "change": {"actions": ["create"], "before": None, "after": {"function_name": name}}}]}


def run_gate(workdir, label, address, name):
    pfile = os.path.join(workdir, label + ".plan.json")
    with open(pfile, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(plan_for(address, name), fh)
    proc = subprocess.run([sys.executable, GATE, "--plan-json", pfile], cwd=REPO, capture_output=True, text=True,
                          timeout=120, check=False)
    out = (proc.stdout or "") + (proc.stderr or "")
    lines = [ln.rstrip() for ln in out.splitlines() if ln.strip()]
    summary = next((ln for ln in lines if ln.startswith("NAMING-PLAN: ")), "")
    if proc.returncode != 0 and "NAMING-PLAN: REFUSE" in summary:
        result = "refused"
    elif proc.returncode == 0 and summary and "NAMING-PLAN: REFUSE" not in summary:
        result = "admitted"
    else:
        result = "error"
    return result, proc.returncode, lines


def main():
    texts = registry_text()
    ob = load_builder()
    rows = json.load(open(os.path.join(REGISTRY_DIR, "resources.json"), encoding="utf-8"))["resources"]
    conformant_rows = sum(1 for r in rows if ob.grade(r["name"], r["type"])[0] == "CONFORMANT")
    print("registry census: resources.json holds %d row(s); %d of %d row name(s) grade CONFORMANT under "
          "lib/opal_naming.grade()" % (len(rows), conformant_rows, len(rows)))
    row_a = next(r for r in rows if r["type"] == NODE_TYPE)
    name_a = row_a["name"]
    name_b = ob.name("blackdiamond", "49financial", "missing-row-probe", "lambda")
    grade_b = ob.grade(name_b, NODE_TYPE)
    count_a = count_in_registry(texts, name_a)
    count_b = count_in_registry(texts, name_b)
    print("A name=%s registry_count=%d own_grade=%s" % (name_a, count_a, ob.grade(name_a, NODE_TYPE)[0]))
    print("B name=%s registry_count=%d own_grade=%s (built by opal_naming.name())" % (name_b, count_b, grade_b[0]))
    print("C name=%s own_grade=%s" % (BAD_NAME, ob.grade(BAD_NAME, NODE_TYPE)[0]))
    mode = gate_mode()
    results = {}
    complete = count_b == 0 and count_a >= 1 and grade_b[0] == "CONFORMANT"
    with tempfile.TemporaryDirectory(dir=os.path.join(REPO, ".scratch") if os.path.isdir(os.path.join(REPO, ".scratch")) else None) as wd:
        for label, addr, nm in (("A", "aws_lambda_function.registered_probe", name_a),
                                ("B", "aws_lambda_function.unregistered_probe", name_b),
                                ("C", "aws_lambda_function.badly_named_probe", BAD_NAME)):
            res, rc, lines = run_gate(wd, label, addr, nm)
            results[label] = res
            print("--- case %s: %s rc=%d" % (label, res, rc))
            for ln in lines:
                print("    gate: " + ln)
    ok = complete and all(v in ("admitted", "refused") for v in results.values()) and results["C"] == "refused"
    print("MISSING-ROW-PROBE registered_wellnamed=%s unregistered_wellnamed=%s badly_named=%s gate_mode=%s ok=%s" % (
        results["A"], results["B"], results["C"], mode, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
