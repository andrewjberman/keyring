"""
comp-dispatch -- the gold-dispatch ORCHESTRATION-DAG tool (NFRA_COMPROUTE Stage-1 #1).

Fronts the one thing no comp-tool answered: the gold-dispatch orchestration layer -- which scripts a
`gold_dispatch.sh` runs, in what ORDER (per chain), under which GROUP/flag, past which conditional
GATE. It is the ORCHESTRATION grain (chain/DAG) sibling to comp-pipescript's PER-SCRIPT grain (io /
deployed) -- distinct one-home node (CTO ruling 2026-07-01: different grain + concern -> sibling, not
a `comp-pipescript dag` subcommand). They COMPOSE: comp-dispatch shows the chain -> drill into
comp-pipescript for a script in it.

Grounded on the #1 gap_heat build-next: gold_dispatch.sh (bd 1419 lines, 7 rail-escapes/heat 0.89;
cot 6/0.66) -- every escape asked "what scripts / in what order / conditional skips". This is a
DETERMINISTIC DECLARED-BLOCK PARSE (the CATALOG heredoc + the CHAIN_*/GROUP_* ordered-ID vars + the
named gate functions/flags) -- it NEVER executes the bash. Read-only, firm-parameterized (bd + cot
share the structure), no AWS, no LLM.

Usage:
    comp-dispatch <firm|path>                 # the full dispatch map
    comp-dispatch <firm> --chain <name>       # one chain expanded to its ordered script list
    comp-dispatch <firm> --script <ID>        # reverse: which chains/groups include a script
    comp-dispatch <firm> --gates              # the conditional skips + how to override
    comp-dispatch <firm> --undispatched       # gold-dir scripts NOT in the catalog (standalone diagnostics)
    comp-dispatch --list                      # firms with a parseable gold_dispatch.sh
    [--json]                                  # machine-readable

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE Stage-1). 2026-07-01. Spec:
org/projects/NFRA_COMPLEARN/comp_dispatch_spec_v1.md. CTO-ratified 012043Z.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

# firm alias -> the data/<dir>/ segment. A bare dir name or a direct .sh path also work.
FIRM_DIRS = {
    "bd": "black_diamond", "black_diamond": "black_diamond",
    "cot": "cot", "cottonwood": "cot",
    "inf": "inf", "inflection": "inf",
}

# Known dispatch gates: (detector regex, label, description, override). Presence-detected in the .sh
# so the tool degrades gracefully (a gate not found is simply not reported, never a crash).
_GATES = [
    (re.compile(r"\bcheck_freshness\b"), "freshness",
     "SKIP the run if the latest silver input has not advanced past the last gold data_as_of "
     "(silver/allocations date vs gold header_metrics.json data_as_of).", "--force"),
    (re.compile(r"GOLD_RESUME|_checkpoint_done|\.checkpoints/"), "resume-skip",
     "Per-script `.done` checkpoint markers under gold/.checkpoints/<run_date>/: with GOLD_RESUME=1 "
     "a script already completed for this run_date is skipped; a fresh run never skips (re-runs).",
     "GOLD_RESUME unset (default fresh)"),
    (re.compile(r"--incremental"), "incremental",
     "Scripts passed --incremental skip already-processed dates (per-script incremental logic).",
     "omit --incremental"),
    (re.compile(r'!=\s*"bcd"|_par_mode\s*=\s*"bcd"|mode[^\n]*"bcd"'), "mode-skip",
     "A dispatch MODE conditionally skips whole phases: cot's run_chain_parallel `if [ \"$mode\" != "
     "\"bcd\" ]` skips PHASE_A (the A_* dimension scripts) when the A dimension is already done "
     "(reached via `--chain bcd`). Grounded on the cot source; the shared bd structure was NOT read "
     "(sovereign-held) -- verify there if/when in scope.", "run the full chain (omit the bcd mode)"),
]

# gate detection is a CLOSED, presence-matched allowlist (the patterns above), NOT derived from the
# source's control flow. A conditional skip built from a construct outside these patterns is NOT
# surfaced -- so --gates DISCLOSES its own boundary (mirroring --undispatched's honest gap-disclosure),
# rather than presenting the matched set as exhaustive. This is the completeness-honesty the tool
# already applies to undispatched scripts, now applied to gates.
_GATE_LABELS = ", ".join(label for _rx, label, _d, _o in _GATES)


# --------------------------------------------------------------------------------------------
def find_dispatch(firm_or_path: str) -> tuple[str | None, str | None]:
    """Resolve a firm alias / dir name / direct path -> (dispatch_path, firm_label)."""
    if firm_or_path.endswith(".sh"):
        p = firm_or_path if os.path.isabs(firm_or_path) else os.path.join(_WS, firm_or_path)
        return (p, os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(p))))) if os.path.exists(p) else (None, None)
    seg = FIRM_DIRS.get(firm_or_path, firm_or_path)
    p = os.path.join(_WS, "data", seg, "scripts", "gold", "gold_dispatch.sh")
    return (p, seg) if os.path.exists(p) else (None, None)


def list_firms() -> list[tuple[str, str]]:
    """(firm_dir, path) for every data/*/scripts/gold/gold_dispatch.sh."""
    out = []
    for p in sorted(glob.glob(os.path.join(_WS, "data", "*", "scripts", "gold", "gold_dispatch.sh"))):
        firm = p.replace("\\", "/").split("/data/")[1].split("/")[0]
        out.append((firm, p))
    return out


# --------------------------------------------------------------------------------------------
def parse_catalog(text: str) -> dict:
    """Parse the `CATALOG << 'MARKER' ... MARKER` heredoc -> {ID: {file, flags}}."""
    m = re.search(r"CATALOG\s*<<\s*'?(\w+)'?.*?\n(.*?)\n\1", text, re.DOTALL)
    catalog: dict = {}
    if not m:
        return catalog
    for ln in m.group(2).splitlines():
        s = ln.strip()
        if not s or s.startswith("#") or "|" not in s:
            continue
        parts = [p.strip() for p in s.split("|")]
        if parts[0]:
            catalog[parts[0]] = {"file": parts[1] if len(parts) > 1 else "",
                                 "flags": parts[2] if len(parts) > 2 else ""}
    return catalog


def parse_vars(text: str, prefix: str) -> dict:
    """Parse `PREFIX_NAME="..."` assignments -> {NAME: raw_value}."""
    return {m.group(1): m.group(2)
            for m in re.finditer(rf'^{prefix}_(\w+)="([^"]*)"', text, re.MULTILINE)}


def resolve_ids(raw: str, chains: dict, _seen: set | None = None) -> list[str]:
    """Expand a chain value to an ordered ID list, resolving nested $CHAIN_X references (de-cycled)."""
    _seen = _seen or set()
    ids: list[str] = []
    for tok in raw.split():
        if tok.startswith("$CHAIN_"):
            ref = tok[len("$CHAIN_"):]
            if ref not in _seen and ref in chains:
                ids.extend(resolve_ids(chains[ref], chains, _seen | {ref}))
        elif not tok.startswith("$"):
            ids.append(tok)
    return ids


def parse_gates(text: str) -> list[dict]:
    return [{"gate": label, "description": desc, "override": override}
            for rx, label, desc, override in _GATES if rx.search(text)]


def undispatched(dispatch_path: str, catalog: dict) -> list[str]:
    """gold-dir *.py NOT in the CATALOG (by filename) -- standalone diagnostics (the E_* class)."""
    gold_dir = os.path.dirname(dispatch_path)
    cat_files = {v["file"] for v in catalog.values()}
    out = []
    for p in sorted(glob.glob(os.path.join(gold_dir, "*.py"))):
        fn = os.path.basename(p)
        if fn not in cat_files:
            out.append(fn)
    return out


def analyze(firm_or_path: str) -> dict:
    path, firm = find_dispatch(firm_or_path)
    if not path:
        return {"error": f"no gold_dispatch.sh for '{firm_or_path}' "
                         f"(known firms: {sorted(set(FIRM_DIRS))}; or pass a path)"}
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    catalog = parse_catalog(text)
    chains_raw = parse_vars(text, "CHAIN")
    groups_raw = parse_vars(text, "GROUP")
    chains_all = {name: resolve_ids(raw, chains_raw) for name, raw in chains_raw.items()}
    # a REAL chain runs catalog scripts; drop label/scalar CHAIN_* vars (e.g. CHAIN_LABEL, a logging
    # string) that resolve to no catalog-member IDs.
    chains = {n: ids for n, ids in chains_all.items() if any(i in catalog for i in ids)}
    chains_raw = {n: chains_raw[n] for n in chains}
    groups = {name: raw.split() for name, raw in groups_raw.items()}
    return {
        "firm": firm, "path": os.path.relpath(path, _WS).replace(os.sep, "/"),
        "catalog": catalog, "chains": chains, "chains_raw": chains_raw, "groups": groups,
        "gates": parse_gates(text),
        "gates_detection": "bounded-allowlist",  # NOT exhaustive: a gate outside _GATES is not surfaced
        "gates_known_patterns": [label for _rx, label, _d, _o in _GATES],
        "undispatched": undispatched(path, catalog),
    }


# --------------------------------------------------------------------------------------------
def _annot(ids: list[str], catalog: dict) -> list[str]:
    out = []
    for i in ids:
        c = catalog.get(i, {})
        f = c.get("file", "?")
        fl = c.get("flags", "")
        out.append(f"    {i:8s} {f}" + (f"   [{fl}]" if fl else ""))
    return out


def render(a: dict, args) -> str:
    if a.get("error"):
        return f"comp-dispatch: {a['error']}"
    L = [f"=== comp-dispatch: {a['firm']}  ({a['path']}) ==="]
    if args.chain:
        ids = a["chains"].get(args.chain) or a["chains"].get(args.chain.upper())
        if ids is None:
            return "\n".join(L + [f"  no chain '{args.chain}'. chains: {sorted(a['chains'])}"])
        L.append(f"\nCHAIN {args.chain} ({len(ids)} scripts, in order):")
        L += _annot(ids, a["catalog"])
        return "\n".join(L)
    if args.script:
        sid = args.script
        c = a["catalog"].get(sid)
        L.append(f"\nSCRIPT {sid}: " + (f"{c['file']}  [{c['flags']}]" if c else "NOT in the catalog"))
        inchains = [(n, ids.index(sid) + 1) for n, ids in a["chains"].items() if sid in ids]
        L.append("  in chains: " + (", ".join(f"{n}(pos {p})" for n, p in inchains) or "none"))
        L.append("  in groups: " + (", ".join(n for n, ids in a["groups"].items() if sid in ids) or "none"))
        if not c and sid in a["undispatched"]:
            L.append("  -> UNDISPATCHED (standalone diagnostic; not run by any chain)")
        return "\n".join(L)
    if args.gates:
        L.append(f"\nCONDITIONAL GATES ({len(a['gates'])} of the known-pattern set matched -- what skips a run/script):")
        for g in a["gates"]:
            L.append(f"  {g['gate']:12s} {g['description']}\n               override: {g['override']}")
        L.append(f"\n  NOTE: gate detection is a fixed presence-matched pattern-set ({_GATE_LABELS}); a "
                 "conditional skip built from a construct OUTSIDE these patterns is NOT surfaced. This "
                 "is a bounded detector, not an exhaustive read of the bash control flow -- cross-check "
                 "the source for a novel gate (as --undispatched discloses its own gap).")
        return "\n".join(L)
    if args.undispatched:
        L.append(f"\nUNDISPATCHED ({len(a['undispatched'])} gold-dir scripts NOT in any chain -- standalone):")
        L += [f"    {f}" for f in a["undispatched"]]
        return "\n".join(L)
    # default: the full map
    L.append(f"\nCHAINS ({len(a['chains'])}):")
    for n, ids in a["chains"].items():
        L.append(f"  {n:14s} ({len(ids)}): {' '.join(ids)}")
    L.append(f"\nGROUPS ({len(a['groups'])}):")
    for n, ids in a["groups"].items():
        L.append(f"  {n:14s} {' '.join(ids)}")
    L.append(f"\nCATALOG ({len(a['catalog'])} scripts): ID -> file [default_flags]")
    L += _annot(list(a["catalog"]), a["catalog"])
    if a["gates"]:
        L.append(f"\nGATES ({len(a['gates'])} of a known-pattern set): " + ", ".join(g["gate"] for g in a["gates"])
                 + "   (comp-dispatch <firm> --gates for detail + the detector-boundary note)")
    if a["undispatched"]:
        L.append(f"\nUNDISPATCHED ({len(a['undispatched'])}): " + ", ".join(a["undispatched"])
                 + "   (standalone diagnostics, not in any chain)")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-dispatch -- the gold-dispatch orchestration-DAG tool")
    ap.add_argument("firm", nargs="?", help="firm alias (bd|cot|...) | dir | path to gold_dispatch.sh")
    ap.add_argument("--chain", help="expand one chain to its ordered script list")
    ap.add_argument("--script", help="reverse-lookup: which chains/groups include this script ID")
    ap.add_argument("--gates", action="store_true", help="the conditional skips + overrides")
    ap.add_argument("--undispatched", action="store_true", help="gold-dir scripts not in the catalog")
    ap.add_argument("--list", action="store_true", dest="do_list", help="firms with a gold_dispatch.sh")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if args.do_list or not args.firm:
        firms = list_firms()
        if args.json:
            print(json.dumps([{"firm": f, "path": os.path.relpath(p, _WS).replace(os.sep, "/")} for f, p in firms], indent=2))
        else:
            print("comp-dispatch -- firms with a parseable gold_dispatch.sh:")
            for f, p in firms:
                print(f"  {f:16s} {os.path.relpath(p, _WS)}")
            if not args.firm:
                print("\n  usage: comp-dispatch <firm> [--chain N | --script ID | --gates | --undispatched | --json]")
        return 0

    a = analyze(args.firm)
    if args.json:
        print(json.dumps(a, indent=2))
        return 0 if not a.get("error") else 1
    print(render(a, args))
    return 1 if a.get("error") else 0


if __name__ == "__main__":
    sys.exit(main())
