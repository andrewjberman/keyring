#!/usr/bin/env python3
"""sc_e31_vocab_bound.py -- MDPF_SECCLASS round 8, cell SC-e-31 (FWD-11): the issuer's bound check on the AI classifier's
class vocabulary. The worker does not edit this file.

Andrew-direct 2026-10-07 ~00:4xZ ("there should be no multi-asset class. There are 6 classes: cash, fixed income, equity,
structured, alternatives, commodities.", record MDPF_SECCLASS_M/ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md)
and 1.0.0_SA_CTO's remap half condition 1 (the AI classifier's vocabulary carries the six-class values).

PASS only if, in infra/aws/lambda/v2_portal/_shared/etf_classification_model.py:
  - ASSET_CLASS_VOCAB is exactly the six values;
  - build_prompt() text names each of the six and never 'multi_asset' / 'multi-asset' / 'multi asset';
  - a stubbed reply naming 'multi_asset' is refused to null (no network: send is injected).
Prints VOCAB-BOUND ok=True|False and the failing limb(s).
"""
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(_REPO / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))

SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}


def main():
    import etf_classification_model as m

    fails = []
    vocab = set(getattr(m, "ASSET_CLASS_VOCAB", set()))
    if vocab != SIX:
        fails.append(f"vocab={sorted(vocab)}")
    subs = {"equity": ["US Large Cap"], "fixed_income": ["Intermediate"]}
    prompt = m.build_prompt("ACME TARGET 2030 FUND", "ACMEX", subs)
    low = prompt.lower()
    missing = sorted(c for c in SIX if c not in low)
    if missing:
        fails.append(f"prompt_missing={missing}")
    if any(t in low for t in ("multi_asset", "multi-asset", "multi asset")):
        fails.append("prompt_names_multi_asset")

    def _send(payload, **_kw):
        content = '{"asset_class": "multi_asset", "sub_asset_class": null, "confidence": 0.95, "reason": "stub"}'
        return {"choices": [{"message": {"content": content}, "finish_reason": "stop"}]}

    try:
        r = m.classify_one("ACME TARGET 2030 FUND", "ACMEX", subs, send=_send, api_key="stub")
        if r.get("asset_class") is not None:
            fails.append("multi_asset_reply_not_refused={!r}".format(r.get("asset_class")))
    except TypeError as exc:
        fails.append(f"classify_one_signature={exc}")
    print("VOCAB-BOUND ok={}{}".format(not fails, "" if not fails else " fails=" + ";".join(fails)))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
