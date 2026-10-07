#!/usr/bin/env python3
"""issuer_check_sc_e27.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-27 (the contract's next version).

Reads org/standards/MDPF_SECCLASS_CONTRACT.json and the two measured inputs (SC-e-25's values JSON, SC-e-26's key-form
proposal) and prints SC-E27-CONTRACT ok=True|False. It passes only when:
  - contract_version is above 0.4.0;
  - exactly two NEW fields (not present in 0.4.0's seven) carry closed `values`, one whose values equal SC-e-25's measured
    characteristics sector set and one whose values equal its industry-group set, each with a `rule24_record`;
  - neither new field is named `sector` or `sub_asset_class` (C-SECTOR: the legacy `sector` keeps its bytes);
  - the contract text carries the PROPOSED KEY FORM from SC-e-26's newest KEY_FORM_PROPOSAL_*.md, verbatim;
  - the seven 0.4.0 fields are all still present.
Run from the repo root.
"""
import glob
import json
import os
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
CONTRACT = os.path.join("org", "standards", "MDPF_SECCLASS_CONTRACT.json")
V040_FIELDS = {"instrument_kind", "identifier_namespace", "classified_by", "classification_confidence",
               "low_confidence", "security_bloomberg", "listing_country"}


def newest(pattern):
    hits = sorted(glob.glob(os.path.join(M, pattern)))
    return hits[-1] if hits else None


def vtuple(v):
    return tuple(int(x) for x in str(v).split("."))


def check():
    with open(CONTRACT, encoding="utf-8") as fh:
        raw = fh.read()
    c = json.loads(raw)
    if vtuple(c.get("contract_version", "0.0.0")) <= (0, 4, 0):
        return False, "contract_version {} not above 0.4.0".format(c.get("contract_version"))
    fields = c.get("fields", {})
    if not V040_FIELDS.issubset(fields):
        return False, f"0.4.0 fields missing: {sorted(V040_FIELDS - set(fields))}"
    new = {k: v for k, v in fields.items() if k not in V040_FIELDS}
    if len(new) != 2:
        return False, f"expected 2 new fields, found {len(new)}: {sorted(new)!s}"
    if {"sector", "sub_asset_class"} & set(new):
        return False, "a new field reuses the legacy name sector or sub_asset_class"
    vpath = newest("SECTOR_INDUSTRY_GROUP_VALUES_*.json")
    kpath = newest("KEY_FORM_PROPOSAL_*.md")
    if not vpath or not kpath:
        return False, "inputs absent (SC-e-25 values JSON or SC-e-26 key-form proposal)"
    with open(vpath, encoding="utf-8") as fh:
        ch = json.load(fh)["sources"]["characteristics"]
    want = [sorted(ch["sector_values"]), sorted(ch["industry_group_values"])]
    got = []
    for k, v in new.items():
        if not isinstance(v.get("values"), list) or not v.get("rule24_record"):
            return False, f"new field {k} lacks closed values or rule24_record"
        got.append(sorted(v["values"]))
    if sorted(got) != sorted(want):
        return False, "new fields' values do not equal the measured sector and industry-group sets"
    with open(kpath, encoding="utf-8") as fh:
        line = next(ln for ln in fh.read().splitlines() if "PROPOSED KEY FORM:" in ln)
    form = line.split("PROPOSED KEY FORM:", 1)[1].strip().strip("`")
    if not form or form not in raw:
        return False, f"the proposed key form {form!r} is not in the contract"
    return True, "version={} new_fields={} key_form={}".format(c["contract_version"], ",".join(sorted(new)), form)


def main():
    ok, why = check()
    print(f"SC-E27-CONTRACT ok={ok} {why}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
