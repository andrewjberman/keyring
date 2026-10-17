"""RCG estate name lexicon: canonical identifiers tagged LIVE / RETIRED / status, per scan.

Feeds reference_lexical features and mark.py's lexical-citation edges (PRD s.6). The
RETIRED tags are MEASURED where possible (a tool registered in a registry but absent from
.tools/ is retired-by-evidence, never by recollection).

BOUNDARY DECLARATION (printed every run):
  address_space      four channels: .tools basenames | org/projects codes+status |
                     SYSTEM_DEFINITIONS term keys+status | function-map names.
  traversal_residue  agent serials (runtime liveness, not lexicon-stable), S3 bucket/key
                     grammars, portal identifiers, file basenames at large -- all OUT of
                     v1, declared. A mention of an out-channel identifier scores nothing.
  presentation       full lexicon at scans/<vintage>/lexicon.json; the print is counts.
  failure_direction  UNDER-enumeration (a channel misparse drops tokens LOUDLY via its
                     printed denominator, never silently).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

WS = Path(__file__).resolve().parents[2]
_LIB = WS / "lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))
from opal_lambda_map import load_all  # noqa: E402  (the one reader of the function-map folder)


def channel_tools() -> list[dict]:
    """.tools/ basenames = LIVE; registry-only names = RETIRED-by-evidence."""
    live = {p.name for p in (WS / ".tools").iterdir()
            if p.is_file() and not p.name.endswith((".md", ".txt", ".log"))}
    entries = [{"token": t, "kind": "tool", "status": "LIVE", "source": ".tools/"}
               for t in sorted(live)]
    registry_names: set = set()
    for reg in ("org/modules/graph/graph-call-manifest.yaml",
                "org/modules/graph/comp-tools.yaml",
                "org/modules/graph/TOOL_MASTER.yaml"):
        path = WS / reg
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        registry_names |= set(re.findall(r"\b(comp-[a-z0-9-]+)\b", text))
    ghosts = sorted(t for t in registry_names
                    if t not in live and not any(t.startswith(x + "-") for x in live))
    entries += [{"token": t, "kind": "tool", "status": "RETIRED",
                 "source": "registry-only (absent from .tools/ -- retired-by-evidence)"}
                for t in ghosts]
    return entries


def channel_projects() -> list[dict]:
    out = []
    for p in sorted((WS / "org" / "projects").glob("*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            out.append({"token": p.stem, "kind": "project", "status": "UNPARSEABLE",
                        "source": str(p.relative_to(WS))})
            continue
        status = str(d.get("status", "unknown")).lower()
        live = "LIVE" if status in ("active", "on-hold", "on_hold") else "RETIRED"
        out.append({"token": d.get("project_code", p.stem), "kind": "project",
                    "status": live, "detail": status, "source": str(p.relative_to(WS))})
    return out


def channel_terms() -> list[dict]:
    path = WS / "infra" / "system" / "ontology" / "SYSTEM_DEFINITIONS.yaml"
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    out = []
    for term, body in spec.get("terms", {}).items():
        status = body.get("status", "unknown")
        live = "LIVE" if status == "reserved_ratified" else (
            "RETIRED" if status == "deprecated" else "CONTESTED")
        out.append({"token": term, "kind": "term", "status": live, "detail": status,
                    "source": "SYSTEM_DEFINITIONS.yaml"})
    return out


def channel_canon_nonconform() -> list[dict]:
    """Naming-act violations, MECHANICALLY generated from the canon's own keys (R-0013:
    concretely resolvable end-to-end, zero prose parsing, zero curation).

    For each SYSTEM_DEFINITIONS term key: the dashed variant (v1.6 underscore act) and the
    Capitalized_Segments variant (R-0004/R-0014 lowercase act) are NONCONFORMING usages --
    EXCEPT variants that collide with a real on-disk path component (e.g. the
    estate-contracts DIRECTORY is legal on disk; only the definition-key usage is bound).
    """
    path = WS / "infra" / "system" / "ontology" / "SYSTEM_DEFINITIONS.yaml"
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    out_p = subprocess.run(["git", "ls-files"], cwd=WS, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
    components: set = set()
    for line in out_p.stdout.splitlines():
        for comp in line.split("/"):
            components.add(comp)
            components.add(comp.rsplit(".", 1)[0])
    entries = []
    excluded = 0
    for term in spec.get("terms", {}):
        variants = set()
        if "_" in term:
            variants.add(term.replace("_", "-"))
            variants.add("_".join(seg.capitalize() for seg in term.split("_")))
        elif term != term.lower():
            variants.add(term)  # a capitalized single-word key is itself nonconforming
        for v in variants:
            if v == term:
                continue
            if v in components:
                excluded += 1
                continue
            entries.append({"token": v, "kind": "canon_nonconform", "status": "NONCONFORM",
                            "source": f"generated from canon key '{term}' (naming acts)"})
    entries.append({"token": "__meta_excluded_path_collisions__", "kind": "canon_nonconform_meta",
                    "status": "META", "source": f"{excluded} variant(s) excluded as real path components"})
    return entries


def channel_lambdas() -> list[dict]:
    # One file per function under infra/aws/lambda/ci/function-map/ (round 30). The folder holds no
    # metadata keys, so every file is a function. load_all raises on an absent or empty folder: no silent empty channel.
    functions = load_all(str(WS))
    return [{"token": n, "kind": "lambda", "status": "LIVE",
             "source": "function-map/%s.json" % n} for n in sorted(functions)]


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    scans = sorted((WS / "rcg" / "scans").iterdir()) if (WS / "rcg" / "scans").exists() else []
    out_dir = scans[-1] if scans else (WS / "rcg" / "scans" / f"{stamp}_lexonly")
    out_dir.mkdir(parents=True, exist_ok=True)

    channels = {"tools": channel_tools(), "projects": channel_projects(),
                "terms": channel_terms(), "lambdas": channel_lambdas(),
                "canon_nonconform": channel_canon_nonconform()}
    lexicon = [e for entries in channels.values() for e in entries]
    (out_dir / "lexicon.json").write_text(
        json.dumps({"built": stamp, "entries": lexicon}, indent=1), encoding="utf-8")

    print(f"[lexicon] {len(lexicon)} identifiers -> {out_dir.relative_to(WS)}/lexicon.json")
    for name, entries in channels.items():
        by = {}
        for e in entries:
            by[e["status"]] = by.get(e["status"], 0) + 1
        print(f"  {name:<10} {len(entries):>4}  {by}")
    ghosts = [e["token"] for e in channels["tools"] if e["status"] == "RETIRED"]
    if ghosts:
        print(f"  [finding] registry-only tool names (retired-by-evidence): {ghosts}")
    print("[boundary] " + __doc__.split("BOUNDARY DECLARATION", 1)[1].strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
