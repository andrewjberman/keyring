"""O1 resolver prototype -- executes the pre-registered deriving rules of
O1_RESOLVES_VIA_SPEC_20260819.md (@5ecb069af3) and emits durable per-term results.

READS pinned sources + two comp-kuzu capture files. EDITS NOTHING -- the runner is
structurally incapable of chasing; edits are human acts bound by the chase-audit.
Declared values below are the SPEC's pre-registered table (registry prose pinned
@7241d0dfd7), encoded verbatim -- the runner implements the spec, it does not re-read
the registry for declarations (source independence of the two legs).

Output: O1_RESOLVES_VIA_RESULTS_20260819.jsonl (one row per term) + summary to stdout.
Plain ASCII. Run from the workspace root.
"""
from __future__ import annotations

import ast
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import yaml  # noqa: E402

ROOT = Path(".")
OUT = ROOT / "org/tier1_exec/4.0.0_SA_CRO/deliverables/O1_RESOLVES_VIA_RESULTS_20260819.jsonl"
SCRATCH = Path(sys.argv[1]) if len(sys.argv) > 1 else None  # dir holding the kuzu captures

PINS = {
    "registry": "7241d0dfd7",
    "canonical": "27f941ede5",
    "bank": "2f8c55f192",
    "anchor_catalog": "c7048f4846",
    "coverage_resolver": "97dc3e07b6",
}

RUN_TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
ROWS: list[dict] = []


def row(term, cls, declared, declared_src, derived, instrument, verdict, notes="",
        independent=True):
    ROWS.append({
        "term": term, "class": cls, "declared": declared,
        "declared_source": declared_src, "derived": derived, "instrument": instrument,
        "verdict": verdict, "derivation_independent": independent,
        "notes": notes, "run_ts": RUN_TS, "spec": "@5ecb069af3", "pins": PINS,
    })


def parse_kuzu_table(path: Path) -> dict[str, int]:
    """Parse the two-column layer/cnt table from the capture file."""
    vals: dict[str, int] = {}
    in_table = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^-+\s+-+\s*$", line):
            in_table = True
            continue
        if in_table:
            m = re.match(r"^(\S+)\s+(\d+)\s*$", line)
            if m:
                vals[m.group(1)] = int(m.group(2))
            elif line.strip().startswith("("):
                break
    return vals


canonical = yaml.safe_load(open("org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml",
                                encoding="utf-8"))
bank = yaml.safe_load(open("org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml",
                           encoding="utf-8"))

# --- 1/2 Substrate + Estate (comp-kuzu capture) --------------------------------
DECL_SUBSTRATE = ["aws", "portal", "codebase", "ms"]
sub_live = parse_kuzu_table(SCRATCH / "o1_kuzu_substrate.txt")
missing = sorted(set(DECL_SUBSTRATE) - set(sub_live))
extra = sorted(set(sub_live) - set(DECL_SUBSTRATE))
verdict = "AGREES" if not missing and not extra else "FAILS-b"
row("Substrate", "W-I", DECL_SUBSTRATE, "registry prose v1.9 re-ruling",
    {"values": sub_live}, "comp-kuzu MATCH (n) RETURN n.layer, count(*)",
    verdict,
    f"declared-but-absent={missing}; materialized-but-undeclared={extra} "
    f"(pipeline retired v1.9, semctl dropped 07-20 -- the S0 half-landing, live)")
row("Estate", "W-I", "union of Substrate", "registry (degenerate whole)",
    {"total_nodes": sum(sub_live.values())}, "inherits Substrate",
    verdict, "inherits Substrate's verdict by construction")

# --- 3/4/5 Subject, Function, C4 grid ------------------------------------------
grid = canonical["c4_subject_function_grid"]
subj = list(grid["subject"]["values"].keys())
DECL_SUBJECT = ["client", "market", "estate"]
row("Subject", "W-I", DECL_SUBJECT, "registry prose v2.1",
    subj, "canonical c4_subject_function_grid.subject.values keys",
    "AGREES" if subj == DECL_SUBJECT else "FAILS-b")

func_raw = grid["function"]["values"]
func_all = list(func_raw.keys())
TOMBSTONE = re.compile(r"^\s*(COLLAPSED|RETIRED|DEPRECATED)\b")
func_live = [k for k, v in func_raw.items()
             if not (isinstance(v, str) and TOMBSTONE.match(v))]
DECL_FUNCTION = ["acquisition", "analysis", "serving", "experience"]
row("Function", "W-I", DECL_FUNCTION, "registry prose v3.1 (build collapsed)",
    {"raw_keys": func_all, "after_tombstone_filter": func_live},
    "canonical function.values keys, tombstone-filtered (leading COLLAPSED/RETIRED/"
    "DEPRECATED on a string value)",
    "AGREES" if func_live == DECL_FUNCTION else "FAILS-b",
    "FINDING regardless of verdict: the build tombstone is PROSE-MARKED, not "
    "field-marked -- a naive key-count derivation gets 5; the deriving rule must lean "
    "on a leading keyword. Recommend a structured status marker at the (c) design.")

row("C4", "W-I", 12, "registry prose (3x4 cells)",
    len(subj) * len(func_live),
    "product of the two axis derivations (tombstone-filtered)",
    "AGREES" if len(subj) * len(func_live) == 12 else "FAILS-b")

# --- 6 Segment (BOTH candidate blocks) ------------------------------------------
DECL_SEGMENT = ["partner-data", "market-intelligence", "interactive-products",
                "access-delivery", "andrew-infrastructure"]
seg_a = sorted(canonical["c4_segments"].keys())
seg_b = sorted(k for k in grid["segment_definitions"].keys() if k != "note")
agree_a = sorted(DECL_SEGMENT) == seg_a
agree_b = sorted(DECL_SEGMENT) == seg_b
row("Segment", "W-I", DECL_SEGMENT, "registry prose v2.1 (rename act)",
    {"c4_segments_keys": seg_a, "segment_definitions_keys": seg_b},
    "canonical -- BOTH blocks, per spec",
    "SPLIT" if agree_a != agree_b else ("AGREES" if agree_a else "FAILS-b"),
    "INTRA-FILE TWO-HOMES: the same authority file carries the roster twice and the "
    "blocks disagree on one member name (c4_segments still spells "
    "estate-infrastructure; segment_definitions spells andrew-infrastructure). A "
    "resolves_via naming 'the canonical' without naming the BLOCK is underspecified "
    "by construction. Known pre-run (F1 both-truths amendment); now measured at "
    "resolver grain.")

# --- 7 Domain -------------------------------------------------------------------
DECL_DOMAIN = ["object-data", "compute-orchestration", "pipeline", "table-data",
               "identity", "api-serving", "artifact-serving", "observability",
               "ui-dataflow"]
src = open("org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/"
           "NFRA_MOTIF_P1_canonical_ab_catalog.py", encoding="utf-8").read()
cat = None
for node in ast.walk(ast.parse(src)):
    if isinstance(node, ast.Assign) and any(
            getattr(t, "id", "") == "ANCHOR_CATALOG" for t in node.targets):
        cat = ast.literal_eval(node.value)
        break
dom = sorted(cat.keys())
d_missing = sorted(set(DECL_DOMAIN) - set(dom))
row("Domain", "W-I", DECL_DOMAIN, "registry prose (9 values in-definition)",
    dom, "ANCHOR_CATALOG keys (@c7048f4846, ast-parsed)",
    "AGREES" if not d_missing and len(dom) == len(DECL_DOMAIN) else "FAILS-b",
    f"declared-but-not-materialized={d_missing} -- the four 08-11-ratified values "
    "(extension spec) were never landed in the deriving instrument; the registry's "
    "authority line cites catalog AND extension spec, and only the catalog is code. "
    "ALSO: the P0 census A1a row hand-wrote 'Domain (4 values)' -- three sources, "
    "three numbers (9 declared / 5 materialized / 4 in the census row); the census "
    "row is itself a specimen of the class O1 measures.")

# --- 8/9 Role, Relation ---------------------------------------------------------
roles = list(bank["roles"].keys())
row("Role", "W-I", 14, "registry prose ('closed set of 14')",
    {"count": len(roles), "members": roles}, "bank roles keys",
    "AGREES" if len(roles) == 14 else "FAILS-b")
rels = list(bank["relations"].keys())
row("Relation", "W-I", 10, "registry prose ('closed set of 10')",
    {"count": len(rels), "members": rels}, "bank relations keys",
    "AGREES" if len(rels) == 10 else "FAILS-b")

# --- 10/11 C2 + Motif -----------------------------------------------------------
fams = list(canonical["c2_motif_families"].keys())
c2_verdict = "AGREES" if len(fams) == 12 else "FAILS-b"
row("C2", "W-I", 12, "registry prose ('12 canonical agnostic families')",
    {"count": len(fams), "members": fams}, "canonical c2_motif_families keys",
    c2_verdict)
row("Motif", "W-I", "same universe as C2", "registry (unit term)",
    {"count": len(fams)}, "same resolver as C2", c2_verdict,
    "unit term over the C2 universe; one resolver, two terms")

# --- 12 Contract_Record ---------------------------------------------------------
cr = bank["dynamic_rails"]["D3_contract_obligation"]["contract_record"]
DECL_REQ = ["intent_source", "obligation", "lifecycle_class", "revalidate_by",
            "locality"]
DECL_OPT = ["successor", "expiry_condition", "cadence", "vintage_probe"]
req_ok = list(cr["required"]) == DECL_REQ
opt_delta = sorted(set(cr["optional"]) ^ set(DECL_OPT))
row("Contract_Record", "W-I",
    {"required": DECL_REQ, "optional": DECL_OPT}, "registry prose (in-definition)",
    {"required": cr["required"], "optional": cr["optional"]},
    "bank contract_record.required/.optional lists",
    "AGREES" if req_ok and not opt_delta else "FAILS-b",
    f"required {'agrees 5/5' if req_ok else 'DISAGREES'}; optional symmetric-delta="
    f"{opt_delta} (bank carries 'describes', registry's declared optional list "
    "omits it -- one-field member-grain drift between two live canon homes)")

# --- 13/14 C0, C1 (UNDECLARED-b) ------------------------------------------------
row("C0", "W-I", None, "NO DECLARED COUNT (graph-derived by nature)",
    {"nodes": sum(sub_live.values())}, "comp-kuzu node count",
    "UNDECLARED-b", "writable, nothing declared to agree with -- a finding of the "
    "UNDECLARED class, not a pass")
edges_txt = (SCRATCH / "o1_kuzu_edges.txt").read_text(encoding="utf-8",
                                                      errors="replace")
m = re.search(r"^(\d+)\s*$", edges_txt, re.M)
edge_count = int(m.group(1)) if m else None
row("C1", "W-I", None, "NO DECLARED COUNT",
    {"edges": edge_count}, "comp-kuzu MATCH ()-[r]->() RETURN count(*)",
    "UNDECLARED-b",
    "capture header states 41331 edges vs query 41310 -- a 21-edge delta between "
    "the DB header and the directed-edge count, recorded not adjudicated")

# --- 15 Estate_Contracts --------------------------------------------------------
store = Path("org/modules/graph/estate-contracts")
files = sorted(store.glob("*.contracts.yaml"))
n_records = 0
per_file = {}
for f in files:
    d = yaml.safe_load(open(f, encoding="utf-8"))
    k = len(d.get("contracts", {}))
    per_file[f.name] = k
    n_records += k
row("Estate_Contracts", "W-I", None, "NO DECLARED COUNT (store of D3 instances)",
    {"files": per_file, "subject_records": n_records},
    "count contracts keys across estate-contracts/*.contracts.yaml",
    "UNDECLARED-b")

# --- 16 Chain (source-degenerate) -----------------------------------------------
cov = json.load(open("org/modules/graph/estate-coverage-resolver.json",
                     encoding="utf-8"))
n_threads = len(cov["threads"])
row("Chain", "W-D", 138, "registry via A10 -- source IS the artifact counted",
    {"threads": n_threads, "named_threads": len(cov["named_threads"])},
    "count threads in estate-coverage-resolver.json @97dc3e07b6 (FROZEN, W-16)",
    "VACUOUS-AGREE" if n_threads == 138 else "FAILS-b",
    "derivation_independent=false: agreement excluded from the agreeing number; the "
    "honest resolves_via names the regen path, which is the W-16 defect",
    independent=False)

# --- 17 Deploy_State (legislated register) --------------------------------------
row("Deploy_State", "L", ["deployed", "undeployed"],
    "naming acts v2.0 + v2.2 (Andrew verbatim)",
    "n/a -- the naming-act register IS the deriving source",
    "registry changelog (the register)",
    "RESOLVES-BY-RULING",
    "hand-RULED membership through a register is the predicate's stated legal form; "
    "single-home, nothing external to diff")

# --- 18-21 not writable tonight -------------------------------------------------
for t in ("D1", "D2", "D3"):
    row(t, "NW", None, "-", None, None, "NOT-WRITABLE",
        "A9-COORDINATE: instance-universe counts are CORE's to declare; census "
        "cites, never re-derives CORE")
row("Name_Variant", "NW", None, "-", None, None, "NOT-WRITABLE",
    "DATA-GRAIN: the a07 alias-surface row count; scores at the instrument pass")

# --- emit -----------------------------------------------------------------------
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    for r in ROWS:
        f.write(json.dumps(r, ensure_ascii=True) + "\n")

attempted = len(ROWS)
writable = sum(1 for r in ROWS if r["verdict"] != "NOT-WRITABLE")
comparable = [r for r in ROWS if r["class"] == "W-I" and r["declared"] is not None]
agreeing = [r for r in comparable if r["verdict"] == "AGREES"]
print("O1 THREE-NUMBER OUTPUT (frame pre-registered @5ecb069af3):")
print(f"  attempted:  {attempted}  (of 26 A1a universes; 5 C3-family HELD for W-15)")
print(f"  writable:   {writable}  ({sum(1 for r in ROWS if r['class']=='W-I')} W-I "
      f"+ {sum(1 for r in ROWS if r['class']=='W-D')} W-D "
      f"+ {sum(1 for r in ROWS if r['class']=='L')} L)")
print(f"  agreeing:   {len(agreeing)} of {len(comparable)} comparable "
      f"(vacuous + UNDECLARED-b excluded by the frame)")
print()
for r in ROWS:
    print(f"  {r['term']:18} {r['class']:3} {r['verdict']}")
print(f"\nresults -> {OUT}  ({attempted} rows, run_ts {RUN_TS})")
