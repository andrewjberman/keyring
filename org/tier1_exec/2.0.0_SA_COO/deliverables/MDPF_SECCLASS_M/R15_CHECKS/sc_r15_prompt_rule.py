"""sc_r15_prompt_rule.py -- MDPF_SECCLASS round 15 cell SC-e-78 check: the AI classifier's prompt states Andrew's alternatives rule.

READ-ONLY, no AWS, no model call. Andrew-direct 2026-10-08 ~19:0xZ (record
org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_190xZ_HEDGE_PRIVATE_REAL_ESTATE_FUNDS_ARE_ALTERNATIVES.md):
"Hedge funds, private funds, real estate funds, all of this falls to Alternatives."
build_prompt()'s instruction text (before the trailing data object) must name hedge funds, private funds and real estate funds, and
name alternatives as their class; the name and ticker must still sit only in the trailing data object (the injection rule).
Run from the repo root you are grading.
Prints  PROMPT-RULE ok=<bool> hedge=<b> private=<b> real_estate=<b> alternatives=<b> data_only=<b>
"""
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "infra/aws/lambda/v2_portal/_shared"))


def main():
    from etf_classification_model import build_prompt
    probe_name, probe_ticker = "ZZPROBE NAME FUND", "ZZPRB"
    text = build_prompt(probe_name, probe_ticker, {})  # empty vocabulary: no sub-class text can satisfy a check
    instruction, _, data = text.rpartition("\n")
    low = instruction.lower()
    checks = {
        "hedge": "hedge fund" in low,
        "private": "private fund" in low,
        "real_estate": "real estate fund" in low,
        "alternatives": "alternatives" in low,
        "data_only": probe_name not in instruction and probe_ticker not in instruction
        and json.loads(data) == {"name": probe_name, "ticker": probe_ticker},
    }
    ok = all(checks.values())
    print("PROMPT-RULE ok=%s %s" % (ok, " ".join("%s=%s" % (k, v) for k, v in checks.items())))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
