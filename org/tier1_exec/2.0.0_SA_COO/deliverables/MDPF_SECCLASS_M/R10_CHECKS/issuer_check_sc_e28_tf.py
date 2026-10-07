#!/usr/bin/env python3
"""issuer_check_sc_e28_tf.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-28: the declared Terraform validates.

Runs `terraform init -backend=false` (with `-plugin-dir=<HOME>/.terraform.d/plugin-cache` when that directory exists, so
no registry egress; the home directory is DERIVED, never typed) and then `terraform validate -no-color` in
infra/aws/terraform/mdpf-secclass/sector-writer/. Never plans and never applies. Prints SC-E28-TF ok=True|False.
Run from the repo root; `terraform` must be on PATH.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.join("infra", "aws", "terraform", "mdpf-secclass", "sector-writer")


def main():
    if not os.path.isdir(ROOT):
        print(f"SC-E28-TF ok=False no root {ROOT}")
        return 1
    tf = shutil.which("terraform")
    if not tf:
        print("SC-E28-TF ok=False terraform not on PATH")
        return 1
    init = [tf, "-chdir=" + ROOT, "init", "-backend=false", "-input=false", "-no-color"]
    cache = os.path.join(os.path.expanduser("~"), ".terraform.d", "plugin-cache")
    if os.path.isdir(cache):
        init.append("-plugin-dir=" + cache)
    r = subprocess.run(init, capture_output=True, text=True, timeout=90, check=False)
    if r.returncode != 0:
        print(f"SC-E28-TF ok=False init rc={int(r.returncode)} {(r.stderr or r.stdout).strip().splitlines()[-1:]!s}")
        return 1
    v = subprocess.run([tf, "-chdir=" + ROOT, "validate", "-no-color"], capture_output=True, text=True, timeout=25, check=False)
    ok = v.returncode == 0 and "The configuration is valid" in v.stdout
    print("SC-E28-TF ok={} {}".format(ok, (v.stdout or v.stderr).strip().splitlines()[-1:] if not ok else "The configuration is valid"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
