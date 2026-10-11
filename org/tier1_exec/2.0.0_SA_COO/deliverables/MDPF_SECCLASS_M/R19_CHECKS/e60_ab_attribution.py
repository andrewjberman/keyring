#!/usr/bin/env python3
"""e60_ab_attribution.py -- MDPF_SECCLASS SC-e-60 arm 2 attribution (CTO ruling @c224f368e3, item 2), COMPUTE-ONLY.

Runs the OLD D_04 (the served code before the e60 ship, S3 VersionId Mu1tZXWFwKEKDLBkmRcfhBq04GXNoAVh, ETag 816a77e9) and the NEW
D_04 (the repo bytes, md5 23d2f2ae) through `build_firm_mix_summary` on ONE captured set of inputs (the three served JSONs, read
once). Each module's S3 reader is replaced with that capture and its writer with an in-memory sink, so NOTHING is written to any
key, scratch or served. Never production evidence.

Prints the field-by-field diff of the two summaries with its denominator, the top-level `Unclassified` and
`composition.mix.unclassified` under both codes, then one verdict line:
  E60-AB ok=<bool> leaves=<n> differing=<k> outside_mix=<m> old_mix_keys=[..] new_mix_keys=[..] old_uncov=<mv> new_Unclassified=<mv>
ok is True when the two summaries differ ONLY under the top-level `mix` key (outside_mix == 0), which makes any change in
`composition`, `concentration`, `mix_periods` or `data_as_of` between two served versions an INPUT change, not e60's.
Run from the repo root.
"""
import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

import boto3

ROOT = Path.cwd()
GOLD = ROOT / "data/black_diamond/scripts/gold"
NEW_FILE = GOLD / "D_04.client_portal_summary.py"
BUCKET = "opal-data-bd"
OLD_KEY = "code/gold/D_04.client_portal_summary.py"
OLD_VERSION = "Mu1tZXWFwKEKDLBkmRcfhBq04GXNoAVh"
OLD_MD5, NEW_MD5 = "816a77e9", "23d2f2ae"


def _load(path, name):
    sys.path.insert(0, str(GOLD))
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _leaves(obj, prefix=""):
    if isinstance(obj, dict):
        for k in sorted(obj):
            yield from _leaves(obj[k], f"{prefix}.{k}" if prefix else str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _leaves(v, f"{prefix}[{i}]")
    else:
        yield prefix, obj


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    new_md5 = hashlib.md5(NEW_FILE.read_bytes()).hexdigest()
    old_body = s3.get_object(Bucket=BUCKET, Key=OLD_KEY, VersionId=OLD_VERSION)["Body"].read()
    old_md5 = hashlib.md5(old_body).hexdigest()
    if not (old_md5.startswith(OLD_MD5) and new_md5.startswith(NEW_MD5)):
        print(f"E60-AB ok=False error=code-bytes old_md5={old_md5} new_md5={new_md5}")
        return 1

    with tempfile.TemporaryDirectory() as td:
        old_path = Path(td) / "D_04_old.py"
        old_path.write_bytes(old_body)
        old, new = _load(old_path, "d04_old"), _load(NEW_FILE, "d04_new")

        keys = (new.MIX_DAILY_SUMMARY, new.FIRM_MIX_VIEWS, new.FIRM_COMPOSITION)
        captured = {}
        for k in keys:
            o = s3.get_object(Bucket=BUCKET, Key=k)
            captured[k] = (json.loads(o["Body"].read()), o["VersionId"])
        print("INPUTS (read once, shared by both codes):")
        for k, (_, v) in captured.items():
            print(f"  s3://{BUCKET}/{k}  VersionId={v}")

        out = {}
        for label, mod in (("old", old), ("new", new)):
            sink = []
            mod._read_json = lambda key, _c=captured: copy.deepcopy(_c[key][0]) if key in _c else None
            mod._write_batch = lambda items, upload, label="", _s=sink: _s.extend(items) or len(items)
            mod._now_str = lambda: "FIXED"
            mod.build_firm_mix_summary(False)
            assert len(sink) == 1 and sink[0][1] == "platinum/firm/mix_summary.json", [k for _, k in sink]
            out[label] = json.loads(json.dumps(sink[0][0], default=str))

    lo, ln = dict(_leaves(out["old"])), dict(_leaves(out["new"]))
    paths = sorted(set(lo) | set(ln))
    differing = [p for p in paths if lo.get(p, "<absent>") != ln.get(p, "<absent>")]
    outside = [p for p in differing if not p.startswith("mix.") and p != "mix"]
    print(f"DIFF: {len(paths)} leaf fields compared (union of both summaries); {len(differing)} differ; {len(outside)} outside top-level mix")
    for p in differing:
        print(f"  {p}: old={lo.get(p, '<absent>')!r} new={ln.get(p, '<absent>')!r}")

    om, nm = out["old"].get("mix", {}), out["new"].get("mix", {})
    def mv(d, k):
        return d[k].get("market_value", 0.0) if isinstance(d.get(k), dict) else 0.0

    old_uncov = mv(om, "unclassified") + mv(om, "other")
    new_unc = mv(nm, "Unclassified")
    def comp_unc_of(s):
        return {c.get("asset_class"): c.get("market_value") for c in s.get("composition", {}).get("mix", [])}.get("unclassified")

    print(f"OLD top-level: unclassified={mv(om, 'unclassified'):,.2f} other={mv(om, 'other'):,.2f}  "
          f"composition.mix.unclassified={comp_unc_of(out['old'])}")
    print(f"NEW top-level: Unclassified={new_unc:,.2f}  composition.mix.unclassified={comp_unc_of(out['new'])}")
    ok = not outside and bool(differing)
    print(f"E60-AB ok={ok} leaves={len(paths)} differing={len(differing)} outside_mix={len(outside)} "
          f"old_mix_keys={sorted(om)} new_mix_keys={sorted(nm)} old_uncov={old_uncov:,.2f} new_Unclassified={new_unc:,.2f}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
