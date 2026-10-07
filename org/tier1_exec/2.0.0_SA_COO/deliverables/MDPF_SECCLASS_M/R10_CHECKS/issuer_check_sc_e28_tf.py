#!/usr/bin/env python3
"""issuer_check_sc_e28_tf.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-28: the declared root is named and registered.

AMENDMENT 2 (2.0.0_SA_COO~M1, rulings on rows W24-S5 and W24-S8):
- REGISTERED, per the registry's own rule: every `aws_*` resource the root declares (log groups excluded), mapped to its node type by
  org/standards/NAMING_SCHEMA.json `tf_type_map` and read from that map's `name_attribute`, must grade CONFORMANT through
  lib/opal_naming.py grade() (the registry resolves it from its own tokens, which is why the registry refuses a redundant row for it),
  or, where grade() cannot resolve it, carry a row in infra/logic/registry/resources.json. At least one name must be found.
- FORMATTED: `terraform fmt -check -recursive` on the root (no provider and no network needed).
- NOT HERE: `terraform validate`. It needs the AWS provider, which no cache on dell1 holds and no seat may download; it runs in the
  issuer's safe-apply plan when the root is applied.
Never inits, plans or applies. Prints SC-E28-TF ok=True|False with the denominator. Run from the repo root.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.join("infra", "aws", "terraform", "mdpf-secclass", "sector-writer")
BLOCK = re.compile(r'^resource\s+"(aws_[a-z0-9_]+)"\s+"[^"]+"\s*\{(.*?)^\}', re.MULTILINE | re.DOTALL)


def main():
    if not os.path.isdir(ROOT):
        print(f"SC-E28-TF ok=False no root {ROOT}")
        return 1
    tf = shutil.which("terraform")
    if not tf:
        print("SC-E28-TF ok=False terraform not on PATH")
        return 1
    fmt = subprocess.run([tf, "-chdir=" + ROOT, "fmt", "-check", "-recursive", "-no-color"], capture_output=True, text=True,
                         timeout=30, check=False)
    if fmt.returncode != 0:
        print(f"SC-E28-TF ok=False fmt rc={int(fmt.returncode)} files={fmt.stdout.split()}")
        return 1
    sys.path.insert(0, "lib")
    import opal_naming
    with open(os.path.join("org", "standards", "NAMING_SCHEMA.json"), encoding="utf-8") as fh:
        tmap = json.load(fh)["tf_type_map"]
    with open(os.path.join("infra", "logic", "registry", "resources.json"), encoding="utf-8") as fh:
        reg = json.load(fh)
    rows = reg.get("resources", reg) if isinstance(reg, dict) else reg
    known = {str(r.get("name", "")) for r in rows if isinstance(r, dict)}
    names, bad = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, "*.tf"))):
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for kind, body in BLOCK.findall(text):
            if kind == "aws_cloudwatch_log_group" or kind not in tmap:
                continue
            attr, node = tmap[kind]["name_attribute"], tmap[kind]["node_type"]
            m = re.search(r'^\s*' + re.escape(attr) + r'\s*=\s*"([^"$]+)"', body, re.MULTILINE)
            if not m:
                continue
            nm = m.group(1)
            names.append(nm)
            try:
                verdict = opal_naming.grade(nm, node)[0]
            except Exception as exc:  # noqa: BLE001 -- the builder raises its own defect classes for an unresolvable name
                verdict = "UNRESOLVED:" + str(exc)[:60]
            if verdict != "CONFORMANT" and nm not in known:
                bad.append(f"{nm}={verdict}")
    ok = bool(names) and not bad
    print(f"SC-E28-TF ok={ok} fmt=clean names={len(names)} registered={len(names) - len(bad)} unregistered={bad} validate=deferred-to-safe-apply")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
