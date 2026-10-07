#!/usr/bin/env python3
"""sc_e61_us_no_subclass_written.py -- MDPF_SECCLASS round 10 SC-e-61 (row W38-S4): the FWD-10 producer's unresolved gate is
not keyed on sub_asset_class.

READ-ONLY, no AWS. Loads new-security-classifier/lambda_function.py and calls is_unresolved_us() on a bare-ticker US item that
the shared module resolved (gics_sector set, no sub_asset_class) and on one it did not (no gics_sector, no sub_asset_class,
low_confidence). ok when the first is NOT unresolved and the second IS (the difference control). Prints SC-E61 ok=<bool>.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
LAMBDA = ROOT / "infra/aws/lambda/mdpf-secclass/new-security-classifier"
for p in (str(ROOT / "infra/aws/lambda/v2_portal/_shared"), str(LAMBDA)):
    if p not in sys.path:
        sys.path.insert(0, p)


def main():
    spec = importlib.util.spec_from_file_location("nsc_e61_check", LAMBDA / "lambda_function.py")
    nsc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nsc)
    resolved = {"identifier_namespace": "TICKER", "asset_class": "equity", "gics_sector": "Information Technology",
                "low_confidence": True}
    unresolved = {"identifier_namespace": "TICKER", "asset_class": "equity", "low_confidence": True}
    a, b = bool(nsc.is_unresolved_us(resolved)), bool(nsc.is_unresolved_us(unresolved))
    ok = (a is False) and (b is True)
    print(f"SC-E61 ok={ok} resolved_is_unresolved={a} unresolved_is_unresolved={b}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
