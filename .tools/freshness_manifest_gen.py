#!/usr/bin/env python3
"""NFRA_INFRPT P1 increment-1 -- per-pipeline served-artifact FRESHNESS MANIFEST generator.

The DS producer leg of the NFRA_INFRPT data-freshness section (co-assigned with
0.7.0_AE_CloudOps~B, who renders the manifest in opal-infrastructure-monitor +
emits per-pipeline STATUS at runtime). Contract LOCKED 2026-06-17 (~B 141449Z).

WHAT IT EMITS (the locked data-contract):
  manifest = {
    schema_version, generated_at, source_commit,
    pipelines: [ { pipeline, served_artifacts: [ {
        bucket, key, label, cadence, warn_age_hours, fail_age_hours,
        severity, freshness_basis, coverage, note, pointer
    } ] } ]
  }

WHY IT CANNOT DRIFT (the SmartX-section lesson): the manifest is DETERMINISTICALLY
DERIVED from the canonical sources, never hand-authored -- it carries the artifact
SET + cadence/threshold/basis; the Lambda head-objects each artifact at runtime,
ages it, and computes STATUS. Sources:
  - org/modules/graph/estate-coverage-resolver.json  (pipescript's served lists)
  - data/black_diamond/scripts/gold/gold_freshness_config.yaml  (bd cadences)
  - data/inf/scripts/gold/gold_freshness_config.yaml  (inf cadences)

COVERAGE STATES (per served_artifact, the false-clean discipline on the freshness layer):
  - "comp-freshness"    -- artifact matches a canonical freshness-config entry (cadence/thresholds known)
  - "pipescript-derived"-- cadence assigned from pipeline schedule without a full config entry
  - "GAP-no-config"     -- no cadence determinable -> ~B renders WATCH+reason, NEVER silently omitted

INCREMENT-1a (this): bd/inf COVERED (comp-freshness); the 5 gaps
(cot/mdpf/model-portfolios/news/nna) emitted GAP-no-config.
INCREMENT-1b: author the 5 gap freshness configs -> GAP flips to comp-freshness.

freshness_basis is a pure function of cadence (business-daily|vendor-daily ->
serving-day / market-calendar-aware; daily|weekly|on-demand -> wall-clock+grace),
so neither side hardcodes a per-pipeline map (locked DELTA 4).
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOLVER = os.path.join(ROOT, "org", "modules", "graph", "estate-coverage-resolver.json")

# Pipelines that have a canonical freshness config today -> drive off the config
# (coverage=comp-freshness). The config IS a canonical, ~D-maintained source
# (comp-freshness reads it); driving off it is not "hardcoding paths in the report".
CONFIG_FILES = {
    "bd-gold": "data/black_diamond/scripts/gold/gold_freshness_config.yaml",
    "inf": "data/inf/scripts/gold/gold_freshness_config.yaml",
    "cot": "data/cot/scripts/gold/gold_freshness_config.yaml",
}

# Consolidated served-layer config for pipelines without a per-pipeline gold tree.
# Each entry carries a `pipeline:` field; the generator groups by it.
SERVED_CONFIG = "data/served_freshness_config.yaml"

# pipeline -> estate-resolver named_thread(s) (the pipescript served-list source).
PIPELINE_THREADS = {
    "bd-gold": ["advi-bd"],
    "inf": ["advi-inf"],
    "cot": ["advi-cot"],
    "mdpf": ["mdpf"],
    "model-portfolios": ["model-portfolios"],
    "news": ["news"],
    "nna": ["partners"],
}

SCHEMA_VERSION = "1.0"

# s3://<bucket>/<key>. Bucket: lowercase alnum + dots/hyphens (validated again below
# to drop template-y captures like "opal-data-{bd|inf}").
_S3_RE = re.compile(r"s3://([a-z0-9][a-z0-9.\-]*)/([^\s)]*)")
_GLOB = re.compile(r"[{*]")  # first glob/template marker in a key


def _basis(cadence: str | None) -> str | None:
    if cadence is None:
        return None
    if cadence in ("business-daily", "vendor-daily"):
        return "serving-day"  # market-calendar-aware (weekend/holiday tolerant)
    return "wall-clock"  # daily | weekly | on-demand | deprecated -> wall-clock + grace


def _valid_bucket(b: str) -> bool:
    return bool(b) and 3 <= len(b) <= 63 and not (b.endswith("-") or b.endswith("."))


def _git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unknown"


def _load_yaml_list(rel_path: str) -> list:
    path = os.path.join(ROOT, rel_path)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or []
    return [e for e in data if isinstance(e, dict)]


def _load_resolver() -> list:
    with open(RESOLVER, encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("threads", []) if isinstance(data, dict) else data


def _label_from_key(key: str) -> str:
    stripped = key.rstrip("/")
    return stripped.rsplit("/", 1)[-1] or stripped or "(root)"


def _config_record(entry: dict, pointer: str) -> dict:
    prefix = entry.get("s3_key_prefix", "") or ""
    m = _S3_RE.match(prefix)
    bucket, key = (m.group(1), m.group(2)) if m else ("", prefix)
    cadence = entry.get("cadence", "daily")
    note = (entry.get("notes", "") or "").strip().replace("\n", " ")
    if cadence in ("on-demand", "deprecated"):
        note = f"[{cadence}] {note}".strip()
    # explicit freshness_basis (e.g. BD-source-bound) overrides the cadence-derived default
    basis = entry.get("freshness_basis") or _basis(cadence)
    # YAML auto-parses an unquoted ISO date to a datetime.date -> coerce to str for JSON
    baseline = entry.get("baseline_as_of")
    if isinstance(baseline, (datetime.date, datetime.datetime)):
        baseline = baseline.isoformat()
    return {
        "bucket": bucket,
        "key": key,
        "label": entry.get("artifact_id", _label_from_key(key)),
        "cadence": cadence,
        "warn_age_hours": entry.get("warn_age_hours"),
        "fail_age_hours": entry.get("fail_age_hours"),
        "severity": (entry.get("severity") or "ERROR").upper(),
        "freshness_basis": basis,
        "as_of_source": entry.get("as_of_source"),
        "baseline_as_of": baseline,
        "coverage": "comp-freshness",
        "note": note,
        "pointer": pointer,
    }


def _extract_note(served_str: str) -> str:
    # the parenthetical annotation in the estate prose, if any (a STALE/FRESH hand-note
    # we deliberately do NOT trust for freshness -- the Lambda computes live age).
    m = re.search(r"\(([^)]*)\)", served_str)
    return (m.group(1).strip() if m else "").replace("\n", " ")


def _gap_records(threads: list, pipeline: str) -> list:
    seen = set()
    out = []
    for t in threads:
        for s in t.get("served_artifacts") or []:
            if not isinstance(s, str):
                continue
            for m in _S3_RE.finditer(s):
                bucket, key = m.group(1), m.group(2)
                if not _valid_bucket(bucket):
                    continue
                cut = _GLOB.search(key)
                prefix = key[: cut.start()] if cut else key
                # head-objectable prefix: keep up to the last '/' when we cut a glob
                if cut and "/" in prefix:
                    prefix = prefix.rsplit("/", 1)[0] + "/"
                if not prefix or prefix in ("/",):
                    continue  # bucket-root / too-broad to be a freshness target
                ident = (bucket, prefix)
                if ident in seen:
                    continue
                seen.add(ident)
                out.append({
                    "bucket": bucket,
                    "key": prefix,
                    "label": _label_from_key(prefix),
                    "cadence": None,
                    "warn_age_hours": None,
                    "fail_age_hours": None,
                    "severity": None,
                    "freshness_basis": None,
                    "as_of_source": None,
                    "baseline_as_of": None,
                    "coverage": "GAP-no-config",
                    "note": _extract_note(s),
                    "pointer": f"pipescript {','.join(PIPELINE_THREADS[pipeline])} (no freshness config -- INCREMENT-1b)",
                })
    return out


def build_manifest() -> dict:
    resolver_threads = _load_resolver()
    by_nt: dict = {}
    for t in resolver_threads:
        by_nt.setdefault(t.get("named_thread"), []).append(t)

    # consolidated served config -> entries grouped by their `pipeline:` field
    served_by_pipeline: dict = {}
    for e in _load_yaml_list(SERVED_CONFIG):
        served_by_pipeline.setdefault(e.get("pipeline"), []).append(e)

    pipelines = []
    for pipeline, nts in PIPELINE_THREADS.items():
        if pipeline in CONFIG_FILES:
            pointer = CONFIG_FILES[pipeline]
            records = [_config_record(e, pointer) for e in _load_yaml_list(pointer)
                       if e.get("s3_key_prefix")]
        elif pipeline in served_by_pipeline:
            records = [_config_record(e, SERVED_CONFIG) for e in served_by_pipeline[pipeline]
                       if e.get("s3_key_prefix")]
        else:
            threads = [t for nt in nts for t in by_nt.get(nt, [])]
            records = _gap_records(threads, pipeline)
        records.sort(key=lambda r: (r["bucket"], r["key"]))
        pipelines.append({"pipeline": pipeline, "served_artifacts": records})

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.datetime.now(tz=datetime.timezone.utc)
        .isoformat(timespec="seconds"),
        "source_commit": _git_head(),
        "generator": ".tools/freshness_manifest_gen.py",
        "pipelines": pipelines,
    }


def _summarize(manifest: dict) -> str:
    lines = []
    for p in manifest["pipelines"]:
        sa = p["served_artifacts"]
        cov = {}
        for r in sa:
            cov[r["coverage"]] = cov.get(r["coverage"], 0) + 1
        covstr = ", ".join(f"{k}={v}" for k, v in sorted(cov.items()))
        lines.append(f"  {p['pipeline']:<18} {len(sa):>3} artifacts  [{covstr or 'none'}]")
    return "\n".join(lines)


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(description="Generate the NFRA_INFRPT freshness manifest.")
    ap.add_argument("-o", "--out", help="write manifest JSON to this path (default: stdout)")
    ap.add_argument("--summary", action="store_true", help="print a per-pipeline coverage summary to stderr")
    args = ap.parse_args(argv)

    manifest = build_manifest()
    out_json = json.dumps(manifest, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(out_json + "\n")
        print(f"OK: wrote {args.out} ({len(manifest['pipelines'])} pipelines)", file=sys.stderr)
    else:
        print(out_json)
    if args.summary:
        print("freshness manifest coverage:", file=sys.stderr)
        print(_summarize(manifest), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
