#!/usr/bin/env python3
"""deploy_ledger.py -- the deploy-completion ledger contract (TO #5).

ADVI_INFETL.BRONZE-FIX structural #5: every multi-leg deploy OPENS a
change_management ledger entry at deploy-START declaring its COMPLETE
manifest, CLOSES only when every leg carries verification proof, and an
entry left OPEN past its window BLARES (RED inbox delivery to COO).
Enforcement rides COO /drive + fabric-check chaining `check --red` each
cycle -- a half-finished deploy cannot slip past a /drive tick.

NEVER-law anchor: CLAUDE.md "NEVER leave a confirmed deploy half-landed"
(e38cc2b16, Andrew-direct 2026-06-12 after the inf-ADVI P0: one cutover
bundle stranded THREE legs + an invisible FATAL with no structural signal).

Leg kinds (AE 0.6 amendment 2 included):
  git             commit/tag pushed              proof: hash / tag name
  s3-prefix       code landed on a code prefix   proof: the TOOL-03 output
                  line (`comp-pipescript deployed` MATCH row -- machine-
                  greppable, carries bucket attribution; NOT a bare ETag)
  activation      container rebuild / task-def / trigger arm
  ec2-baked-asset on-instance baked copy         proof: SSM cat/md5 of the
                  RUNNING path (S3 ETag is NOT valid proof -- the S3 copy
                  can be current while the baked copy is stale)
  verify          post-deploy live-state check (0-diff plan, smoke, served
                  artifact read)

Usage:
  deploy_ledger.py open  --slug mdpf-vintage --title "..." --author 0.7.0_AE_CloudOps \
      --leg "L1|git|CLOUD commit|hash pushed" --leg "L2|s3-prefix|opal-data-mdpf code/gold|TOOL-03 MATCH line" \
      [--pipeline inf]            # adds the canonical PIPELINE_MAP x VALID_LAYERS
                                  # + AUX_CODE_PREFIXES legs for that firm
      [--window-hours 4]
  deploy_ledger.py close-leg --slug mdpf-vintage --leg-id L2 --proof "<evidence>"
  deploy_ledger.py close     --slug mdpf-vintage        # refuses if any leg unproven
  deploy_ledger.py check [--red] [--window-hours N]     # exit 1 if any entry OPEN
                                  # ALSO sweeps change_management/*.md for an
                                  # OPEN/non-terminal ledger with NO sentinel
                                  # (the false-clean gate-bypass class) -> BYPASS
                                  # line + (--red) RED-to-COO.
  deploy_ledger.py list

CORRELATION-ID TOKEN FORMAT (pinned with DS for BRONZE-FIX #7 interop,
2026-06-12): embed `ssm:<command_id>` and `lock:<run_id>` tokens in --proof
strings when they exist. The #7 FATAL SNS payload carries the SAME tokens, so
a FATAL alert grep-joins to its open ledger entry mechanically.

v1.1 RATCHET LIST (DS contract review 225806Z, non-blocking):
  R1. per-kind proof-shape validation -- s3-prefix proof must match a TOOL-03
      MATCH-line regex; ec2-baked-asset proof must carry an ssm:/md5 token
      (proof quality must not ride culture; this tool exists because culture
      fails).
  R2. AUX['inf'] None-home prefixes (runner/exporter/cleanup) render
      UNCOVERED -- the residual stranded-deploy surface; map repo homes or
      retire the prefixes (small follow-on, AE 0.6 lane interface).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# STOP: THIS TOOL READS FILES OTHER SEATS WROTE, AND 167 OF 644 LEDGER SURFACES CARRY NON-ASCII.
# On Windows with PYTHONIOENCODING/PYTHONUTF8 unset, stdout is cp1252 and printing one of those
# bytes raises UnicodeEncodeError MID-SWEEP. Measured by 3.0.0_SA_CVO (ESTATE_GOVERNANCE-S3) and
# reproduced here: `check --red` died after 16 stdout lines on U+26D4 with rc=1.
# THE DANGEROUS PART IS NOT THE CRASH, IT IS THE EXIT CODE. rc=1 is also this command's HONEST
# verdict for "red entries exist", so a caller -- /drive chains `check --red` every tick -- cannot
# tell a verdict from a traceback, and the sweep it thinks completed was TRUNCATED at the first
# non-ASCII surface. A partial sweep reporting a plausible failure is worse than a loud one.
# The tool must not die on data it exists to read; this does NOT license new non-ASCII in output
# (CLAUDE.md still binds -- use OK:/WARN:/ERROR:/SKIP:/BLOCKED:).
# FOLD-IN from the site-Z rendering of this same fix (0.0.0_AB_MSTR~Z @cecfb9e081), which LOST
# the pick and is discarded except for these two facts, neither of which is in the text above.
# (1) THE DIAGNOSIS: this file reads authored ledgers with errors="replace" in EIGHT places -- it
#     already knew hand-written content carries characters it did not choose -- and guarded its
#     OUTPUT nowhere. Input hardened, output bare. That asymmetry is why the defect existed.
# (2) WHY THE STREAM AND NOT THE CALL SITE: the offending character arrives from AUTHORED text and
#     can surface in ANY print in this 1300-line file, so repairing the one line that happened to
#     fire would leave the identical landmine in every other one. Do not "fix" a future instance
#     locally; it is already fixed here.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001 -- older Python, or a stream that cannot be reconfigured
        pass

WORKSPACE = Path(__file__).resolve().parent.parent
CM_DIR = WORKSPACE / "org" / "critical_paths" / "change_management"
STATE_DIR = WORKSPACE / "org" / "critical_paths" / ".open_deploys"
COO_INBOX = WORKSPACE / "org" / "mcp" / "inbox" / "2.0.0_SA_COO"
LEG_KINDS = {"git", "s3-prefix", "activation", "ec2-baked-asset", "verify", "tf-lambda"}
DEFAULT_WINDOW_HOURS = 4.0

# HELD / SOVEREIGN-GATED state. PROVENANCE, TWO FIELDS ON PURPOSE -- designed by 1.0.0_SA_CTO,
# AUTHORED by 2.0.0_SA_COO~B @f6f0a543aa3 (2026-07-09), clause (d)+HELD-PAST-REREAD extended by
# 0.8.0_AE_CloudComp @6fc0b41fb0 (2026-08-26). This line used to read only "CTO-designed 2026-07-09"
# and that is TRUE-BUT-INCOMPLETE IN A WAY THAT READS AS COMPLETE: 2026-08-26, a seat sourced
# provenance from it, propagated it into a message CORRECTING an attribution, and dropped the
# author -- with `git blame` one command away, unrun, BECAUSE THE COMMENT AGREED WITH WHAT THEY
# ALREADY BELIEVED. A line that confirms you does not feel like a claim under test; it feels like a
# citation. DESIGNER and AUTHOR are DIFFERENT FIELDS and a record carrying one cannot tell them
# apart -- CLAUDE.md: a value must carry its claim in a field a consumer can reject on, never in a
# comment. Amend this block when a name changes; do not let it collapse back to one name.
# The dormant-sovereign-hold doctrine is encoded
# into the never-half-land gate. An APPLY/DEPLOY leg is any leg whose work MUTATES state (git push,
# code landed, TF apply, activation, baked asset); a VERIFY leg is a post-deploy live-state check. The
# distinction is load-bearing: HELD requires EVERY apply leg proven + ONLY verify legs open, so a real
# half-landed strand (an open apply leg) can NEVER claim HELD to escape the RED. See _qualifies_as_held.
APPLY_LEG_KINDS = LEG_KINDS - {"verify"}
GATE_TYPES = {"sovereign", "external"}          # (c) the structured gate class -- NOT free prose
DEFAULT_HELD_STALE_DAYS = 4.0                    # a HELD hold older than this escalates to HELD-STALE
HELD_STATUS = "HELD-SOVEREIGN-GATED"
HELD_NUDGE_SUPPRESS_HOURS = 24.0                # re-nudge a HELD-STALE hold at most once/day

# ---------------------------------------------------------------------------
# NFRA_DEPLOYLEDGER.HELD-STATE (Andrew-approved 2026-08-18 ~1537Z; CTO gates the schema act).
#
# THE DEFECT THIS CLOSES, in one line: A HELD DECLARED WHEN TO LOOK AGAIN, AND NOTHING CARRIED IT.
# `gate.ref` already had to NAME a specific dependency, so the hold-REASON half was real. But the
# RE-READ half lived in DEFAULT_HELD_STALE_DAYS -- a GLOBAL CONVENTION, identical for every hold --
# so no consumer could branch on THIS hold's own stated condition. A value and a guess shared one
# type: "4 days old" and "past the moment its owner said to look again" rendered the same.
#
# RULE 24, stated because a schema act requires it (HS-3 also states it in the deliverable):
#   AXIS + INTENT  -- ONE axis: the ledger's LIFECYCLE state. It does NOT encode disposition,
#                     severity, or ownership; those are separate axes and mixing them here would
#                     break the schema foundationally (24-iii).
#   DOMAIN         -- every sentinel ledger in STATE_DIR.
#   VALUES (MECE)  -- OPEN (work outstanding) | HELD (deliberate, gated, well-formed) | terminal
#                     (CLOSED/ROLLBACK/etc). Exhaustive over the domain and mutually exclusive: a
#                     ledger is in exactly one, and HELD is reachable ONLY through the structural
#                     guardrails, never by asserting a status string.
#   SAME GRAIN     -- all three are LEDGER-level. HELD-PAST-REREAD and HELD-STALE are NOT values on
#                     this axis: they are RE-SURFACE CONDITIONS *of* HELD, reported as their own
#                     finding classes. Putting them on the lifecycle axis would mix a state with a
#                     staleness observation -- two grains, one enum (24-ii).
#   STATE COHERENCE (24-iv) -- the three values move under DIFFERENT remedies and that is the whole
#                     point: OPEN closes by DOING THE WORK; HELD clears by the NAMED GATE MOVING,
#                     which is by construction not the ledger owner's act; terminal moves under
#                     nothing. WARNING: ONE REMEDY DOES NOT MOVE THEM TOGETHER, which is exactly why a
#                     detector that cannot tell a hold from neglect manufactures the wrong reflex.
#
# WARNING: THE EASIEST-PASS ROUTE IS REFUSED BY CONSTRUCTION: labelling neglect "HELD" with no reason and
# no re-read condition is the cheapest possible escape, so a hold missing EITHER is NOT a valid HELD
# and stays RED. A state anyone can claim for free is not a state, it is a label.
REREAD_KINDS = {"date", "event"}   # (d) WHEN to look again: a real date, or a NAMED event
# An EVENT-gated hold cannot go "past" a date, so it is never HELD-PAST-REREAD; it re-surfaces on the
# age cadence instead, with its named event printed. Encoded so the two are not silently conflated.
DRIFT_WARN_SUPPRESS_HOURS = 24.0                # re-warn an entry-vs-sentinel DRIFT at most once/day

# Gate-bypass scan (false-clean hardening 2026-06-17, CTO-author / AE-review /
# COO-track). The sentinel-only `check --red` enumerates ONLY .open_deploys/*.json,
# so a HAND-AUTHORED markdown deploy-completion ledger (no sentinel) is structurally
# INVISIBLE to the gate + auto-RED + COO alert -- the false-clean class (anchor: the
# 2026-06-16 causality teardown ledger was content-complete but unindexed). cmd_check
# now ALSO sweeps the rendered change_management/*.md ledgers for an OPEN/non-terminal
# status carrying NO matching sentinel. A ledger status that LEADS with one of these
# tokens is a terminal (nothing-stranded) state and is skipped.
TERMINAL_STATUS_TOKENS = (
    "CLOSED", "COMPLETE", "DONE", "ROLLBACK", "ROLLED",
    "CANCEL", "SUPERSEDED", "ABANDONED", "RESOLVED", "VOID",
)
# Re-alert suppression for unindexed ledgers (they have no sentinel to carry
# last_red_at). Leading-dot name -> excluded from the STATE_DIR.glob("*.json")
# sentinel enumeration (pathlib `*` skips dotfiles; cmd_check also guards).
UNINDEXED_RED_STATE = STATE_DIR / ".unindexed_red_state.json"


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _ts(dt: datetime | None = None) -> str:
    return (dt or _now()).strftime("%Y%m%dT%H%M%SZ")


def _state_path(slug: str) -> Path:
    return STATE_DIR / f"{slug}.json"


def _load(slug: str) -> dict:
    p = _state_path(slug)
    if not p.exists():
        sys.exit(f"ERROR: no open deploy ledger for slug '{slug}' ({p})")
    return json.loads(p.read_text(encoding="utf-8"))


def _save(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    _state_path(state["slug"]).write_text(
        json.dumps(state, indent=2), encoding="utf-8")


def _stage_open_artifacts(state: dict) -> list:
    """NFRA_CLDGRPH-S34 (2026-09-04; 2.0.0_SA_COO~A 94170, disarm owner 1.0.0_SA_CTO). THE SENTINEL DIED WITH THE
    WORKTREE. Under spine v3 a WORKER opens its deploy inside its own worktree; `open` writes the sentinel as a
    side-effect file that no commit pathspec necessarily names (the worker commits the change_management/*.md, which
    :726 itself calls a RENDERING of the sentinel); the drain then runs `git worktree remove` and the sentinel is gone.
    Round 4 lost 2 of 3 that way -- the gate's ONLY input destroyed, leaving the *.md rendering as an UNINDEXED OPEN
    LEDGER that `check --red`'s sentinel-only scan cannot see (:900 exists to catch exactly that, and did).

    WHAT STAGING BUYS, MEASURED AND NOT OVERSTATED (probe worktree, 2026-09-04): with the sentinel staged,
    `git worktree remove` REFUSES -- "contains modified or untracked files, use --force to delete it", rc 128 -- and
    `git worktree remove --force` returns 0 and deletes it anyway. An UNCOMMITTED sentinel already made the worktree
    dirty before this change, so the round-4 removals that destroyed one were FORCED; staging does not stop a forced
    removal and this docstring does not claim it does. What it buys is that the sentinel sits in the INDEX rather than
    among untracked files, so the worker composing its commit and the drain reading `git status` both see it as an
    added path, and an unforced removal refuses.

    THE HALF THAT ACTUALLY SURVIVES A FORCED REMOVAL is committing the sentinel, and the receipt below names it as a
    REQUIRED commit pathspec because a worker committing with `--only -- <paths>` takes its pathspec from the ORDER,
    not from the index -- so the L6 cut naming org/critical_paths/.open_deploys/<slug>.json in the order's <paths>
    block is the other carrier (2.0.0_SA_COO~A's, offered in 94170 and taken).

    NOT DONE HERE, deliberately: writing the sentinel to the MAIN worktree root (the fix @6bfaa233ed used for the
    gitignored override-audit log). The sentinel is a TRACKED path, so that would have a worker dirtying the shared
    tree -- the one thing v3's worktree isolation exists to prevent.

    Best-effort and LOUD: git failing here never fails the open (the ledger's own state is already on disk), but the
    WARN says so, because a silent staging failure would restore the class this closes. Returns the staged rel paths."""
    import subprocess
    rels = [str(_state_path(state["slug"]).relative_to(WORKSPACE)).replace("\\", "/"), state["entry_path"]]
    try:
        r = subprocess.run(["git", "add", "--"] + rels, cwd=str(WORKSPACE), capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=30)
    except Exception as exc:  # noqa: BLE001
        print(f"WARN: could not stage the ledger artifacts ({type(exc).__name__}: {exc}) -- commit them by hand: "
              f"{' '.join(rels)}", file=sys.stderr)
        return rels
    if r.returncode != 0:
        print(f"WARN: git add returned {r.returncode} for the ledger artifacts ({r.stderr.strip()[:160]}) -- "
              f"commit them by hand: {' '.join(rels)}", file=sys.stderr)
    return rels


def _render_entry(state: dict) -> str:
    """The human-readable s10.6 change_management entry, regenerated from state on every
    mutation THAT GOES THROUGH THIS TOOL.

    GUARANTEES: `open` / `close-leg` / `close` / `hold` re-render the entry from the sentinel,
    so a TOOL-driven mutation cannot leave the two inconsistent.

    DOES NOT GUARANTEE that they agree. A HAND-EDIT of the .md is outside this tool's world:
    it updates nothing the gate reads (the sentinel is the gate's only input), and `close`
    unlinks the sentinel -- so a LIVE sentinel whose entry reads CLOSED means the entry was
    hand-edited and the tool never ran. The previous wording here claimed the two "can never
    drift". That was a FALSE INVARIANT asserted in a docstring: anyone reading the source
    concluded drift was impossible by construction, and ledger
    advi-breaks-to3-49f-431167-unrealized-facts-restore sat falsely RED for 214h behind exactly
    that belief. A comment that over-claims an invariant is a detector that lies to its reader.
    Layer 3 (_entry_prose_drift) DETECTS the drift this function cannot prevent.
    Never hand-edit an entry -- except its `## Sign-off` section, which _write_entry carries through every
    re-render (LGIC_ENFORCE-W1-S17).
    """
    lines = [
        "# Deploy Completion Record",
        f"**Date opened:** {state['opened_at']}",
        f"**Status:** {state['status']}"
        + (f" -- closed {state.get('closed_at')}" if state.get("closed_at") else "")
        + (f" -- gate: {state['gate'].get('type')} / {state['gate'].get('ref')}"
           f" (held since {state.get('held_at')})" if state.get("gate") else ""),
        f"**Deploy:** {state['title']}",
        f"**Authored by:** {state['author']}",
        "**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)",
        f"**Window:** {state['window_hours']}h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)",
        "",
        "---",
        "",
        "## Manifest (every leg must carry proof before CLOSE)",
        "",
        "| leg | kind | target | proof required | proof | state |",
        "|---|---|---|---|---|---|",
    ]
    for leg in state["legs"]:
        proof = (leg.get("proof") or "").replace("|", "\\|")
        st = "CLOSED " + (leg.get("closed_at") or "") if leg.get("proof") else "OPEN"
        lines.append(
            f"| {leg['id']} | {leg['kind']} | {leg['target'].replace('|', chr(92) + '|')} "
            f"| {leg['proof_required'].replace('|', chr(92) + '|')} | {proof} | {st} |")
    lines += ["", "## Log", ""]
    for ev in state.get("log", []):
        lines.append(f"- {ev}")
    lines.append("")
    return "\n".join(lines)


_SIGNOFF_HEAD_RE = re.compile(r"^## Sign-?off\b.*$", re.M | re.I)


def _carried_signoff(old_text: str) -> str:
    """The entry's `## Sign-off` section, verbatim, from its heading to the next `## ` heading or the end; "" if none.

    THE ONE HAND-WRITTEN SECTION A RE-RENDER KEEPS (LGIC_ENFORCE-W1-S17). A never-widen sign-off is written on the
    entry by its signers, and every `close-leg` re-rendered the entry from the sentinel and erased it -- so the step
    that records an apply erased the record that authorized it, and the reader of those lines found zero."""
    m = _SIGNOFF_HEAD_RE.search(old_text or "")
    if not m:
        return ""
    nxt = re.search(r"^## ", old_text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(old_text)
    return old_text[m.start():end].rstrip("\n") + "\n"


def _write_entry(state: dict) -> None:
    path = Path(WORKSPACE / state["entry_path"])
    try:
        old = path.read_text(encoding="utf-8")
    except OSError:
        old = ""
    body = _render_entry(state)
    keep = _carried_signoff(old)
    if keep:
        body = body.rstrip("\n") + "\n\n" + keep
    path.write_text(body, encoding="utf-8", newline="\n")


def _canonical_pipeline_legs(pipeline_dir: str) -> list[dict]:
    """Standard legs from the BRONZE-FIX #1 canonical map (safe_deploy_core:
    PIPELINE_MAP x VALID_LAYERS + AUX_CODE_PREFIXES). ad1f03b7f interface."""
    sys.path.insert(0, str(WORKSPACE / ".tools"))
    import safe_deploy_core as core
    if pipeline_dir not in core.PIPELINE_MAP:
        sys.exit(f"ERROR: unknown pipeline dir '{pipeline_dir}' "
                 f"(known: {sorted(core.PIPELINE_MAP)})")
    bucket, firm = core.PIPELINE_MAP[pipeline_dir]
    legs = []
    # Per-TREE layers (tree_layers), not PIPELINE_MAP x VALID_LAYERS: the union
    # vocabulary mints phantom (tree, layer) pairs once trees stop sharing one
    # layer set (the 2026-08-04 mdpf flip added backfill/feeders/assets_gold to
    # the union; bd has no backfill, and mdpf's s3 prefix is code/scripts/<l>/,
    # not code/<l>/). The tree's own (repo_home, s3_prefix) pairs are the truth.
    # bd/inf/cot legs are byte-identical to the old cross-product.
    for layer, (_repo_home, s3_prefix) in sorted(core.tree_layers(pipeline_dir).items()):
        legs.append({
            "id": f"{firm}-{layer}",
            "kind": "s3-prefix",
            "target": f"s3://{bucket}/{s3_prefix}",
            "proof_required": f"comp-pipescript deployed --pipeline {firm}-{layer} MATCH line",
            "proof": None, "closed_at": None,
        })
    for prefix, home in (core.AUX_CODE_PREFIXES.get(firm) or {}).items():
        legs.append({
            "id": f"{firm}-aux-{prefix}",
            "kind": "s3-prefix",
            "target": f"s3://{bucket}/code/{prefix}/ (aux; repo home: {home or 'NONE -- UNCOVERED'})",
            "proof_required": f"comp-pipescript deployed [aux:{prefix}] MATCH line",
            "proof": None, "closed_at": None,
        })
    return legs


def _lambda_leg(function_name: str) -> dict:
    """A single first-class leg for a single-Lambda TF deploy. THE FIX for the
    --pipeline phantom-leg expansion: a single-lambda TF apply must NOT open the
    full PIPELINE_MAP x VALID_LAYERS S3-code legs (none of which it touches ->
    false 'unproven leg / half-landed' on close). Resolves the function's
    tf_resource from lambda-source-map.json for the leg target."""
    smap = WORKSPACE / "infra" / "aws" / "lambda" / "ci" / "lambda-source-map.json"
    target = function_name
    try:
        data = json.loads(smap.read_text(encoding="utf-8", errors="replace"))
        entry = (data.get(function_name)
                 or (data.get("functions") or {}).get(function_name)
                 or (data.get("lambdas") or {}).get(function_name))
        if entry and entry.get("tf_resource"):
            target = entry["tf_resource"]
    except (OSError, ValueError, AttributeError):
        pass  # source-map unreadable -> fall back to the bare function name as target
    return {
        "id": function_name,
        "kind": "tf-lambda",
        "target": target,
        "proof_required": ("TF apply (0 destroy) + 0-diff replan + deployed "
                           "source_code_hash matches uploaded sha + verify-on-served"),
        "proof": None, "closed_at": None,
    }


def cmd_open(args) -> int:
    if _state_path(args.slug).exists():
        sys.exit(f"ERROR: deploy ledger '{args.slug}' is already OPEN -- "
                 "close it or pick a new slug")
    legs: list[dict] = []
    for spec in args.leg or []:
        parts = [p.strip() for p in spec.split("|")]
        if len(parts) != 4:
            sys.exit(f"ERROR: --leg must be 'id|kind|target|proof_required', got: {spec}")
        lid, kind, target, proof_req = parts
        if kind not in LEG_KINDS:
            sys.exit(f"ERROR: leg kind '{kind}' not in {sorted(LEG_KINDS)}")
        legs.append({"id": lid, "kind": kind, "target": target,
                     "proof_required": proof_req, "proof": None, "closed_at": None})
    for fn in (getattr(args, "lambda_fn", None) or []):
        legs.append(_lambda_leg(fn))
    if args.pipeline:
        legs.extend(_canonical_pipeline_legs(args.pipeline))
    if not legs:
        sys.exit("ERROR: a deploy ledger needs at least one leg "
                 "(--leg, --lambda, and/or --pipeline)")
    ids = [leg["id"] for leg in legs]
    if len(ids) != len(set(ids)):
        sys.exit(f"ERROR: duplicate leg ids: {ids}")
    opened = _now()
    safe_slug = re.sub(r"[^A-Za-z0-9_-]", "-", args.slug)
    entry_rel = (f"org/critical_paths/change_management/"
                 f"{opened.strftime('%Y%m%dT%H%M')}Z_{safe_slug}_deploy_completion.md")
    state = {
        "slug": args.slug,
        "title": args.title,
        "author": args.author,
        "status": "OPEN",
        "opened_at": opened.isoformat(),
        "window_hours": args.window_hours,
        "entry_path": entry_rel,
        "legs": legs,
        "log": [f"{_ts(opened)} OPENED by {args.author} with {len(legs)} leg(s)"],
        "last_red_at": None,
    }
    _save(state)
    _write_entry(state)
    staged = _stage_open_artifacts(state)
    print(f"OK: OPENED deploy ledger '{args.slug}' ({len(legs)} legs) -> {entry_rel}")
    for leg in legs:
        print(f"  OPEN {leg['id']} [{leg['kind']}] {leg['target']}")
    # S34: the sentinel is the gate's ONLY input and dies with a worktree that never commits it.
    print("  REQUIRED COMMIT PATHSPEC (both, in the same commit -- the sentinel is the gate's only input and\n"
          "  a worktree removed without it destroys the OPEN state, leaving the .md as an unindexed open ledger):")
    for s in staged:
        print(f"    {s}")
    print("  (both are STAGED, so an UNFORCED `git worktree remove` refuses; a FORCED one still deletes them --\n"
          "   committing them is what survives the drain)")
    return 0


def cmd_close_leg(args) -> int:
    state = _load(args.slug)
    for leg in state["legs"]:
        if leg["id"] == args.leg_id:
            leg["proof"] = args.proof
            leg["closed_at"] = _ts()
            state.setdefault("log", []).append(f"{_ts()} LEG {args.leg_id} closed: {args.proof[:120]}")
            _save(state)
            _write_entry(state)
            open_left = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
            print(f"OK: leg {args.leg_id} closed. Remaining open: {open_left or 'NONE'}")
            return 0
    sys.exit(f"ERROR: leg '{args.leg_id}' not in ledger '{args.slug}' "
             f"(legs: {[leg['id'] for leg in state['legs']]})")


def cmd_close(args) -> int:
    state = _load(args.slug)
    unproven = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
    if unproven:
        print(f"REFUSED: ledger '{args.slug}' has unproven leg(s): {unproven}")
        print("A leg without proof = the deploy is NOT complete. Close every "
              "leg with evidence, or the entry stays OPEN and blares.")
        return 2
    state["status"] = "CLOSED -- nothing stranded"
    state["closed_at"] = _ts()
    state.setdefault("log", []).append(f"{_ts()} CLOSED -- all {len(state['legs'])} legs proven")
    _write_entry(state)
    _state_path(args.slug).unlink()
    print(f"OK: CLOSED deploy ledger '{args.slug}' -- all {len(state['legs'])} "
          f"legs proven; sentinel removed; entry: {state['entry_path']}")
    return 0


def cmd_hold(args) -> int:
    """Mark a ledger HELD / SOVEREIGN-GATED (or --release it). Encodes the dormant-sovereign-hold
    doctrine: a deploy whose apply legs are all proven but whose post-deploy VERIFY legs are blocked
    on a named sovereign/external gate is NOT half-landed -- it should not cry-wolf RED. The hold is
    granted ONLY on the structural guardrails (_qualifies_as_held); a half-landed strand is refused."""
    state = _load(args.slug)
    if args.release:
        had_gate = bool(state.pop("gate", None))
        state.pop("held_at", None)
        state.pop("last_held_nudge_at", None)
        state["status"] = "OPEN"
        state.setdefault("log", []).append(f"{_ts()} HOLD RELEASED -> OPEN" + ("" if had_gate else " (was not held)"))
        _save(state)
        _write_entry(state)
        print(f"OK: HOLD released on '{args.slug}' -> status OPEN "
              "(verify legs must still close before CLOSE).")
        return 0
    if not args.gate_type or not args.gate_ref:
        sys.exit("ERROR: setting a hold requires --gate-type {sovereign|external} and --gate-ref "
                 "'<specific dependency>' (or use --release).")
    if args.gate_type not in GATE_TYPES:
        sys.exit(f"ERROR: --gate-type must be one of {sorted(GATE_TYPES)}")
    if not args.gate_ref.strip():
        sys.exit("ERROR: --gate-ref must NAME the specific dependency (e.g. 'Andrew cross-region PAT'), "
                 "not prose -- a vague 'waiting on something' is refused.")
    # HS-1: the re-read condition is REQUIRED and EXCLUSIVE -- exactly one of date|event. Refused at
    # set-time as well as at check-time, so the easiest-pass route never reaches the sentinel at all.
    if bool(args.reread_date) == bool(args.reread_event):
        sys.exit("ERROR: setting a hold requires EXACTLY ONE of --reread-date YYYY-MM-DD or "
                 "--reread-event '<named event>'.\n"
                 "A hold must say WHEN to look at it again. Without that the only answer available is "
                 "a global default identical for every hold -- a convention, not THIS hold's claim, "
                 "and neglect labelled HELD is indistinguishable from a deliberate one.")
    if args.reread_date:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.reread_date.strip()):
            sys.exit("ERROR: --reread-date must be YYYY-MM-DD (got %r)" % args.reread_date)
        reread = {"kind": "date", "value": args.reread_date.strip()}
    else:
        if not args.reread_event.strip():
            sys.exit("ERROR: --reread-event must NAME the awaited event, not prose.")
        reread = {"kind": "event", "value": args.reread_event.strip()}
    # Provisionally attach the gate, THEN verify the conjunction -- REFUSE if an apply leg is open
    # (the anti-escape-hatch, enforced at set-time as well as at check-time).
    trial = dict(state)
    trial["gate"] = {"type": args.gate_type, "ref": args.gate_ref.strip(), "reread": reread}
    ok, reason = _qualifies_as_held(trial)
    if not ok:
        sys.exit(f"REFUSED: cannot HELD '{args.slug}' -- {reason}.\n"
                 "A HELD/SOVEREIGN-GATED state requires ALL apply/deploy legs closed-with-proof and "
                 "ONLY verify legs open. A half-landed deploy stays RED -- close or roll back the open "
                 "apply leg first.")
    state["gate"] = trial["gate"]
    state.setdefault("held_at", _now().isoformat())    # preserve the original hold-start on a re-hold
    state["status"] = HELD_STATUS
    state.setdefault("log", []).append(f"{_ts()} HELD-SOVEREIGN-GATED gate={args.gate_type}/{args.gate_ref.strip()[:80]}")
    _save(state)
    _write_entry(state)
    print(f"OK: '{args.slug}' -> {HELD_STATUS} (gate={args.gate_type}/{args.gate_ref.strip()}).\n"
          "Reads KNOWN-HELD (no half-landed RED) but stays VISIBLE + tracked in `check`; escalates to "
          f"HELD-STALE after {DEFAULT_HELD_STALE_DAYS}d (tunable via `check --held-stale-days`).\n"
          f"Release with `deploy_ledger.py hold --slug {args.slug} --release`.")
    return 0


def _held_nudge_alert(state: dict, held_days: float) -> None:
    """A HELD-STALE NUDGE -- DISTINCT from the half-landed _red_alert. A legitimate sovereign/external
    -gated hold that has sat past the staleness threshold: not a stranded deploy, but it needs a human
    to nudge the gate or reconsider. Alert-not-block; softer, clearly-labelled subject."""
    COO_INBOX.mkdir(parents=True, exist_ok=True)
    gate = state.get("gate") or {}
    open_verify = [lg["id"] for lg in state["legs"] if not lg.get("proof")]
    subject = f"HELD-STALE__sovereign-gated_hold__{state['slug']}"
    fname = f"{_ts()}_deploy-ledger_{subject}.md"
    body = (
        f"# Message from deploy_ledger.py (HELD-STALE nudge, on behalf of {state['author']})\n"
        f"**To:** 2.0.0_SA_COO\n**Date:** {_ts()}\n"
        f"**Subject:** HELD-STALE: sovereign/external-gated deploy hold '{state['slug']}' held "
        f"{held_days:.1f}d -- NUDGE THE GATE OR RECONSIDER (NOT a half-landed deploy)\n\n"
        f"Deploy: {state['title']}\nAuthor: {state['author']}\n"
        f"Gate: {gate.get('type')} / {gate.get('ref')}\n"
        f"Held since: {state.get('held_at')} ({held_days:.1f} days)\n"
        f"Open (verify-only) legs: {', '.join(open_verify)}\n"
        f"Entry: {state['entry_path']}\n\n"
        "This is a LEGITIMATE hold (all apply/deploy legs proven; only post-deploy verify pends) -- NOT "
        "a stranded/half-landed deploy, so it is not a half-landed RED. But it has now sat past the "
        "staleness threshold: nudge the named gate so the verify legs can close, or reconsider whether "
        f"the hold still applies. Release with `deploy_ledger.py hold --slug {state['slug']} --release`.\n")
    (COO_INBOX / fname).write_text(body, encoding="utf-8", newline="\n")
    print(f"HELD-STALE: nudge delivered to COO inbox: {fname}")


def _red_alert(state: dict, age_h: float) -> None:
    """RED delivery: write the alert file directly into the COO inbox dir --
    the COO's persistent inbox Monitor streams it as an [INBOX] event. RED is
    alert-not-block (HALTGT [STOP]/[HALT] reserved for deploy-blocking)."""
    COO_INBOX.mkdir(parents=True, exist_ok=True)
    open_legs = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
    subject = f"RED__deploy_ledger_OPEN_past_window__{state['slug']}"
    fname = f"{_ts()}_deploy-ledger_{subject}.md"
    body = (
        f"# Message from deploy_ledger.py (on behalf of {state['author']})\n"
        f"**To:** 2.0.0_SA_COO\n**Date:** {_ts()}\n"
        f"**Subject:** RED: deploy-completion ledger '{state['slug']}' OPEN "
        f"{age_h:.1f}h (window {state['window_hours']}h) -- POSSIBLE HALF-LANDED DEPLOY\n\n"
        f"Deploy: {state['title']}\nAuthor: {state['author']}\n"
        f"Opened: {state['opened_at']}\n"
        f"Stranded leg(s): {', '.join(open_legs)}\n"
        f"Entry: {state['entry_path']}\n\n"
        "NEVER-law e38cc2b16: a begun deploy FINISHES in-session or rolls back "
        "+ escalates loud. Route to the author or escalate.\n")
    (COO_INBOX / fname).write_text(body, encoding="utf-8", newline="\n")
    print(f"RED: alert delivered to COO inbox: {fname}")


# THE READER ACCEPTS EVERY MARKDOWN SPELLING OF A STATUS LINE (CTO ruling amendment 213157Z, on DT's
# reproduce-then-kill grounding 212934Z). The original regex required the bold span to CLOSE immediately
# after the colon (`**Status:** X`), so two perfectly ordinary hand-authored forms were UNREADABLE and
# their files flagged as "no terminal Status" -- when every one of them said CLOSED on line 3:
#     **Status: CLOSED - all legs proven**     <- colon INSIDE the bold span
#     ## Status: CLOSED                        <- heading form
# That is the instrument mis-reading, not the record missing: the dispatch premise ("files lacking a
# terminal Status line") was FALSE, and a fix built to it would have duplicated Status lines into files
# that already carried one. Loosening the READER retires the whole class with ZERO file edits.
# ORDER IS LOAD-BEARING: strict first, because the colon-inside pattern would capture an EMPTY value
# from the canonical `**Status:** X` form (non-greedy `(.*?)` matches nothing before the closing `**`).
_STATUS_LINE_PATTERNS = (
    # 1. STRICT canonical -- what _render_entry emits:            **Status:** VALUE
    re.compile(r"^\s*(?:[-*+>]\s+)?\*\*status:\*\*\s*(.*)$", re.IGNORECASE),
    # 2. COLON INSIDE THE BOLD SPAN (the hand-author majority):   **Status: VALUE**
    re.compile(r"^\s*(?:[-*+>]\s+)?\*\*status:\s*(.*?)\*\*", re.IGNORECASE),
    # 3. HEADING form:                                            ## Status: VALUE
    re.compile(r"^\s*#{1,6}\s*status:\s*(.*)$", re.IGNORECASE),
    # 4. UNTERMINATED bold span (LAST -- it is the loosest, and order is load-bearing:
    #    patterns 1-3 must get first refusal or this one would swallow their values).
    #    A hand-authored `**Status: CLOSED ... ` whose bold span runs on for several
    #    LINES never closes on its own line, so pattern 2's non-greedy `(.*?)\*\*`
    #    finds no terminator and the whole file reads as having NO status -- measured
    #    2026-08-26 on a ledger that says CLOSED in its third line and had been
    #    unreadable for 41 days. Structural, not another enumerated spelling: the value
    #    is simply "the rest of the line" when the span does not terminate on it.
    re.compile(r"^\s*(?:[-*+>]\s+)?\*\*status:\s*(?!.*\*\*)(.*)$", re.IGNORECASE),
    # 5. TABLE-ROW form (STRUCTURAL, 1.0.0_SA_CTO~Z 2026-09-03; 2.0.0_SA_COO~Z 19601 item 3): a
    #    header TABLE whose label cell is the bold word and whose VALUE is the NEXT cell --
    #        | **State** | CLOSED -- COMPLETE 2026-09-01T15:31Z |
    #    The segmenter splits this line at `|` into a label fragment and a value fragment, so no
    #    single-segment pattern can ever see both; this one reads the WHOLE line (the first yield of
    #    _status_segments). It accepts the label words Status and State -- two 2026-09-01 entries
    #    (0.7.0_AE_CloudOps~Z, portal-auth) wrote State and read as UNINDEXED OPEN for 41 h while
    #    saying CLOSED in their own header. Safety unchanged: the label must be the bold word ALONE
    #    in the first cell, so a prose mention of "state" in a cell matches nothing.
    re.compile(r"^\s*\|\s*\*\*(?:status|state)\*\*\s*\|\s*(.*?)\s*\|?\s*$", re.IGNORECASE),
)

# ===========================================================================================
# COMPOUND-FIELD SEGMENTATION -- THE STRUCTURAL FIX (CTO 2026-08-11, COO's FOURTH-VARIANT find).
# The three patterns above are ANCHORED at line start, so a Status carried as the SECOND field of
# a compound header line is unreadable:
#     **Opened:** 2026-08-05T23:05Z by 0.7.0_AE_CloudOps · **Status:** CLOSED 2026-08-05T23:40Z
# Measured over the full corpus (386 files): 340 line-start, 10 COMPOUND-INLINE, 36 genuinely
# absent -- and every one of the 10 was reporting a FALSE RED on the NO-HALF-DEPLOYS gate.
#
# >> WHY A SEGMENTER AND NOT A FOURTH PATTERN: the three fixes before this one each ENUMERATED
# the spelling its author had just seen (colon-inside-span, heading form, doubly-bolded value).
# An enumerated-spellings reader's coverage is exactly its author's sample -- it passes on every
# file that taught it and fails on the next hand-authored one, which is why there was a second,
# a third, and now a fourth variant. This parses the STRUCTURE instead: a markdown header line is
# a sequence of FIELDS separated by `·`/`•`/`|`/`;`/spaced dashes, so the reader tests each FIELD,
# not just the first. New separators extend coverage; new VALUE spellings are already covered by
# the strip("*_") normalization. <<
#
# SAFETY (why this is not over-permissive): a segment still has to satisfy one of the ANCHORED
# patterns above -- it must literally begin with `**status:` / `## status:`. A prose fragment
# that merely mentions the word cannot match (the LD-0274 mention-is-not-a-marker discipline),
# and a separator that splits a date or a sentence just yields fragments that match nothing.
# Adding separators therefore only ever ADDS coverage; it cannot manufacture a false terminal.
# ===========================================================================================
_COMPOUND_FIELD_SEP = re.compile(r"\s*[·•|;]\s*|\s+[-–—]{1,2}\s+")


def _split_fields(line: str) -> list[str]:
    """Split a compound header line at field separators, SKIPPING any separator candidate
    that falls INSIDE an open bold span -- a dash (or dot) inside `**...**` is VALUE content,
    not a field boundary. (Defect B, 2026-08-18, MSTR F-1 / LD-0420: `_COMPOUND_FIELD_SEP.split`
    cut `**STATUS: CLOSED ... -- ALL LEGS COMPLETE...**` before its closing `**`, yielding
    fragments that match no anchored pattern -- so the segmenter's "cannot manufacture a false
    terminal" note stayed true while the INVERSE harm was live: a false OPEN on a CLOSED ledger.
    Measured on 20260729T0135Z_bd49f-etf-ownership-revival line 3.) The guard is structural
    (markdown bold parity before the split point), not an enumerated spelling."""
    parts: list[str] = []
    last = 0
    for m_ in _COMPOUND_FIELD_SEP.finditer(line):
        if line.count("**", 0, m_.start()) % 2:  # inside an open ** span -> value content
            continue
        parts.append(line[last:m_.start()])
        last = m_.end()
    parts.append(line[last:])
    return parts


def _status_segments(line: str):
    """The line itself, then each of its compound-field segments (document order preserved).
    First-status semantics are unchanged: callers stop at the first segment that yields a value.
    Splitting is bold-span-aware via _split_fields (defect B fix); a truncated fragment can still
    only ever match nothing, so segmentation remains additive-coverage-only."""
    yield line
    segs = _split_fields(line)
    if len(segs) > 1:
        for seg in segs:
            if seg and seg != line:
                yield seg


def _md_status(md_path: Path) -> str | None:
    """First Status value in a change_management ledger, in ANY of its markdown spellings
    (canonical `**Status:** X`, colon-inside-span `**Status: X**`, or `## Status: X` heading),
    case-insensitive and tolerant of a leading bullet / blockquote marker.
    None ONLY when the file genuinely carries no status line -- never merely because the author
    closed the bold span in a different place."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in text.splitlines():
        for seg in _status_segments(line):
            for pat in _STATUS_LINE_PATTERNS:
                m = pat.match(seg)
                if m:
                    val = m.group(1).strip().strip("*_").strip()
                    if val:                  # an empty capture is not a status -- keep looking
                        return val
    return None


# `**Opened/closed:** <start>-<end>` is the single-leg in-session hand-authored form: it
# states the close IN THE SAME FIELD as the open, so neither the status patterns nor the
# close-marker pattern could see it. 8 such ledgers were unreportable (measured 2026-08-26).
_CLOSE_MARKER_PAT = re.compile(
    r"^\s*(?:[-*+>]\s+)?\*\*(?:date\s+closed|opened\s*/\s*closed|closed):\*\*\s*\S",
    re.IGNORECASE)


def _has_close_marker(md_path: Path) -> bool:
    """True if the ledger carries an explicit, non-empty close-date marker
    ('**Date closed:**' / '**Closed:**' / '**closed:**'). Hand-authored ledgers
    that omit a **Status:** line (globgrph-style) signal a terminal state this way
    instead -- without this check they false-trip as 'no status line'.
    Segment-aware since 2026-08-18 (defect A, MSTR F-1 / LD-0420): the 08-11
    compound-field segmentation reached _md_status and _has_terminal_status_anywhere
    but not this reader, so `**Ledger opened:** X · **Closed:** Y` was unreadable --
    the marker sat mid-line and the anchored pattern never saw it. Same anchored
    pattern, now tested per FIELD via _status_segments (mention-is-not-a-marker
    discipline unchanged: prose cannot match the bold anchored form)."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    for line in text.splitlines():
        for seg in _status_segments(line):
            if _CLOSE_MARKER_PAT.match(seg):
                return True
    return False


def _has_terminal_status_anywhere(md_path: Path) -> bool:
    """True if ANY status-grammar line in the doc leads with a terminal token --
    the CLOSE-BLOCK-at-foot shape (CTO GO 144651Z fix b): a doc that closes itself
    in a '## CLOSE BLOCK' while the header Status line still reads OPEN fired a
    false gate-bypass RED every cycle (the a2-egress instance, header never
    flipped). Matches the SAME _STATUS_LINE_PATTERNS grammar as _md_status --
    NEVER bare prose containing the word CLOSED (the LD-0274 matcher class; a
    mention is not a status). Used ONLY by the unindexed scanner, whose stated
    bias is toward terminal; _md_status keeps first-line semantics everywhere
    else (drift detection wants the DECLARED state, not the best one)."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    for line in text.splitlines():
        for seg in _status_segments(line):
            for pat in _STATUS_LINE_PATTERNS:
                m = pat.match(seg)
                if m:
                    val = m.group(1).strip().strip("*_").strip()
                    if val and _is_terminal_status(val):
                        return True
    return False


def _is_terminal_status(status: str) -> bool:
    """True if a ledger status LEADS with a terminal-state token (CLOSED /
    COMPLETE / ROLLBACK / ...) -- i.e. the deploy is not still open. Match on the
    leading word only, so a mid-string token (e.g. 'OPEN -- issue RESOLVED') does
    not false-terminal an open ledger. lstrip covers whitespace AND markdown
    emphasis wrappers (*/_): a doubly-bolded '**Status:** **CLOSED ...' captures
    a value leading with '**', and .lstrip() alone (whitespace-only) left it
    unreadable -- the THIRD spelling variant of the :424 class (COO source-read
    2026-08-11, 4 false REDs); the reader loosens, the records stay untouched."""
    # STRIP LEADING NON-ALPHANUMERICS, not an enumerated set: a status written
    # `**Status: [GREEN-CIRCLE] CLOSED ...**` defeated .lstrip("*_ \t") because the
    # emoji is none of those characters, so a genuinely CLOSED ledger read NON-TERMINAL
    # and sat unreportable (measured 2026-08-26: GLDRNS_B1_AOR_RELEASE_WINDOW_20260715,
    # closed 07-16, invisible for 41 days). Enumerating emojis would be the
    # enumerated-spellings mistake this module already retired once for status lines --
    # every terminal token begins with a LETTER, so stripping to the first alphanumeric
    # is structural and cannot manufacture a false terminal from punctuation.
    head = re.sub(r"^[^0-9A-Z]+", "", status.upper())
    return any(head.startswith(tok) for tok in TERMINAL_STATUS_TOKENS)


def _entry_prose_drift(state: dict) -> tuple:
    """DRIFT-A: the rendered entry claims a TERMINAL state while a live sentinel
    still exists for the same slug.

    The .md is a RENDERING of the sentinel (_render_entry/_write_entry) and `close`
    unlinks the sentinel -- so a live sentinel whose entry reads CLOSED means the
    entry was hand-edited and the tool was never run. Layer 1 reads only the
    sentinel; Layer 2 skips sentinel-covered entries. Nothing compared the two, so
    this quadrant was structurally invisible in BOTH directions:

      benign   -- prose CLOSED over a proven-but-unclosed sentinel: a false RED that
                  blares for days while every human reading the repo sees CLOSED
                  (anchor: advi-breaks-to3-49f-431167-unrealized-facts-restore, a
                  hand-edit swept into unrelated commit 149fd762b -- 60 files, 0
                  sentinels -- and left the gate crying wolf for 214h).
      dangerous -- prose CLOSED over a GENUINELY UNPROVEN leg: the operator reads
                  "nothing stranded" while a leg never carried proof at all.

    Returns (is_drift, md_status, unproven_leg_ids).
    """
    try:
        md = (WORKSPACE / state["entry_path"]).resolve()
    except (KeyError, OSError):
        return (False, None, [])
    status = _md_status(md)
    if status is None or not _is_terminal_status(status):
        return (False, status, [])
    unproven = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
    return (True, status, unproven)


def _drift_warn_alert(state: dict, md_status: str, unproven: list) -> None:
    """WARN delivery for a DANGEROUS entry-vs-sentinel drift: the rendered entry claims a
    terminal state while the sentinel still carries an UNPROVEN leg -- a NEVER#6 bypass that
    reads as compliance to anyone reading the repo.

    Loud to a human, INERT to the pipeline (no RED, no exit_flag) -- CTO ruling 20260709T191228Z.
    RED + exit 1 is gated on all three of:
      (1) the detector EXERCISED -- fires on an injected DANGEROUS fixture, silent on an injected
          benign one (both directions; extend the _is_terminal_status mutation to the unproven path);
      (2) a measured 7-day window with ZERO false positives on live boards;
      (3) an audited escape hatch matching `safe-commit --force` / `HALT_OVERRIDE`.
    A hard-fail shipped with no false-positive data is how a gate earns an --no-verify habit.
    """
    COO_INBOX.mkdir(parents=True, exist_ok=True)
    subject = f"WARN__deploy_ledger_ENTRY_SENTINEL_DRIFT__{state['slug']}"
    fname = f"{_ts()}_deploy-ledger_{subject}.md"
    body = (
        f"# Message from deploy_ledger.py (on behalf of {state['author']})\n"
        f"**To:** 2.0.0_SA_COO\n**Date:** {_ts()}\n"
        f"**Subject:** WARN: ledger '{state['slug']}' entry reads TERMINAL while leg(s) "
        f"{', '.join(unproven)} carry NO proof -- the record disagrees with the gate\n\n"
        f"Deploy: {state['title']}\nAuthor: {state['author']}\n"
        f"Entry: {state['entry_path']}\n"
        f"Entry **Status:** {md_status}\n"
        f"Unproven leg(s) in the sentinel: {', '.join(unproven)}\n\n"
        "The change_management/*.md is a RENDERING of the .open_deploys sentinel; the sentinel is\n"
        "the gate's only input, and `close` unlinks it. A live sentinel whose entry reads CLOSED\n"
        "means the entry was hand-edited and the tool was never run. Here the entry ALSO claims a\n"
        "close over leg(s) that never carried proof -- a NEVER#6 bypass wearing a compliance mask.\n\n"
        "Fix: `deploy_ledger.py close-leg --proof ...` then `close`. NEVER hand-edit the entry.\n"
        "WARN, not RED: alert-not-block, pending the CTO promotion gate.\n")
    (COO_INBOX / fname).write_text(body, encoding="utf-8", newline="\n")
    print(f"  WARN: drift alert delivered to COO inbox: {fname}")


def _qualifies_as_held(state: dict) -> tuple:
    """CTO's CONJUNCTIVE guardrails for a HELD / SOVEREIGN-GATED deploy ledger -- ALL required, and
    verified STRUCTURALLY off the legs (NEVER off a status string), so a real half-landed strand can
    NOT claim HELD to escape the RED. Returns (qualifies: bool, reason: str). HELD is NOT terminal
    (unlike CLOSED): a HELD ledger stays visible + tracked, it just is not a stranded-deploy RED.
      (a) every APPLY/DEPLOY leg (kind != 'verify') is CLOSED-WITH-PROOF -- an open apply leg IS a
          genuinely half-landed deploy -> DISQUALIFIED (stays RED). THIS is the anti-escape-hatch.
      (b) at least one leg is open AND every open leg is a 'verify' leg (only post-deploy checks pend;
          a fully-proven ledger must close(), not HELD).
      (c) a NAMED, STRUCTURED gate: state['gate'] = {'type' in GATE_TYPES, 'ref': <non-empty>} -- a
          machine-checkable dependency, NOT prose. A vague 'waiting on something' cannot qualify."""
    legs = state.get("legs") or []
    open_legs = [lg for lg in legs if not lg.get("proof")]
    if not open_legs:
        return False, "no open legs -- close() the ledger, do not HELD it"
    open_apply = [lg["id"] for lg in open_legs if lg.get("kind") != "verify"]
    if open_apply:                                    # (a) + (b): the load-bearing anti-escape-hatch
        return False, ("open APPLY/DEPLOY leg(s) %s -- a half-landed deploy cannot be HELD (stays RED)"
                       % open_apply)
    gate = state.get("gate")                          # (c) structured gate
    if not isinstance(gate, dict):
        return False, "no structured gate (need gate.type + gate.ref -- not prose)"
    if gate.get("type") not in GATE_TYPES:
        return False, "gate.type must be one of %s (got %r)" % (sorted(GATE_TYPES), gate.get("type"))
    if not (gate.get("ref") or "").strip():
        return False, "gate.ref is empty -- name the SPECIFIC dependency, not prose"
    # (d) HS-1: a REQUIRED re-read condition -- WHEN to look at this hold again. Without it the
    # only answer available is a global default identical for every hold, which is a convention,
    # not this hold's claim. A hold that cannot say when to revisit it is indistinguishable from
    # neglect wearing the word HELD, so it does NOT qualify and stays RED.
    rr = gate.get("reread")
    if not isinstance(rr, dict):
        return False, ("no re-read condition (need gate.reread {kind: date|event, value}) -- a hold "
                       "that cannot say WHEN to look again is indistinguishable from neglect")
    if rr.get("kind") not in REREAD_KINDS:
        return False, "gate.reread.kind must be one of %s (got %r)" % (sorted(REREAD_KINDS), rr.get("kind"))
    rv = (rr.get("value") or "").strip()
    if not rv:
        return False, "gate.reread.value is empty -- give a real date or NAME the awaited event"
    if rr["kind"] == "date" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", rv):
        return False, "gate.reread.value must be YYYY-MM-DD for kind=date (got %r)" % rv
    return True, ("all apply legs proven; only verify open; structured %s gate (%s); re-read %s=%s"
                  % (gate["type"], gate["ref"], rr["kind"], rv))


def _held_age_days(state: dict, now: datetime) -> float | None:
    """Days since the ledger entered HELD (state['held_at']); None if unknown/unparseable."""
    ha = state.get("held_at")
    if not ha:
        return None
    try:
        return (now - datetime.fromisoformat(ha)).total_seconds() / 86400.0
    except (ValueError, TypeError):
        return None


# ==========================================================================================
# HELD-VERIFY-PENDING -- THE THIRD LIFECYCLE STATE (COO ruling @be7d73eb2a, dispatch 72668).
#
# THE STATE THE AXIS COULD NOT EXPRESS: apply COMPLETE, but a VERIFY leg pending on a NAMED
# FUTURE EVENT under a DIFFERENT OWNER. None of the ten TERMINAL_STATUS_TOKENS can say that, so
# authors reached for prose and each reached for DIFFERENT prose -- the estate carries SIX
# independent one-off coinages for this one state (HELD-SOVEREIGN-GATED, DEFERRED-TO-POST-
# CONSOLIDATION, RESOLVED-PARKED, plus three prose forms), each used exactly once. An n=1 value
# is the signature of a MISSING VOCABULARY, not a careless author.
#
# WHY THIS IS NOT THE ENUMERATED-SPELLINGS TREADMILL THIS MODULE ALREADY RETIRED: the treadmill
# adds SPELLINGS for a state the axis HAS. This adds the STATE.
#
# WHY THE TOKEN IS NOT THE OBVIOUS BARE `HELD`: bare HELD has ZERO status-line occupancy (0 of
# 468) and would be perfectly safe for this status-line-anchored reader -- and that is the trap.
# It occupies 102 of 551 files as ORDINARY PROSE ("held behind", "held before"), so any future
# free-text grep or comp-find census over the token returns a confident, well-formed count of
# something else. THE READER IS NOT THE ONLY CONSUMER OF A STATUS VALUE; THE NEXT AGENT WITH A
# QUESTION IS. HELD-VERIFY-PENDING has zero occupancy on every probe and composes into the
# HELD-* family the corpus already started.
#
# ⛔ THE CONSUMING HALF IS THE WHOLE MECHANISM -- CLAUDE.md "A VALUE MUST CARRY ITS CLAIM".
# _qualified_held_verify_pending REFUSES a value that does not carry BOTH an OWNER and a NAMED
# RE-READ EVENT, and the caller then reports it as OPEN. Without that refusal this becomes the
# most attractive place in the estate to park anything inconvenient and drifts to unpopulated
# exactly as `closure_reason` did at 0 of 333 project JSONs. A hold with no named owner and no
# named event is indistinguishable from an ABANDONMENT and is MORE dangerous than an OPEN,
# because it reads as deliberate.
#
# ⛔ THE UNCOVERED MEMBER, NAMED SO IT IS NOT DISCOVERED LATER AS A GAP: apply-complete with a
# verify pending on NO NAMED EVENT is NOT this value and stays OPEN. An unnamed re-read event is
# precisely how a hold becomes permanent.
#
# GRAMMAR (both fields REQUIRED, and required IN THE STATUS VALUE ITSELF, not merely somewhere in
# the file -- a file-wide scan would let an unrelated "owner:" elsewhere qualify a bare hold, and
# the failure direction of a loose parser here is INVISIBLE PARKING):
#     **Status:** HELD-VERIFY-PENDING -- owner: <serial> -- re-read: <named event>
# Field labels accepted: owner|author for the owner; re-read|reread|re-read-event|event for the
# event. Separator-liberal, field-strict.
# ==========================================================================================
HELD_VERIFY_PENDING_TOKEN = "HELD-VERIFY-PENDING"
_HVP_OWNER_PAT = re.compile(r"\b(?:owner|author)\s*[:=]\s*([^\n]+?)(?=\s+(?:--|\u00b7|\||;)\s+|$)",
                            re.IGNORECASE)
_HVP_EVENT_PAT = re.compile(
    r"\b(?:re-?read(?:-event)?|event)\s*[:=]\s*([^\n]+?)(?=\s+(?:--|\u00b7|\||;)\s+|$)",
    re.IGNORECASE)


def _is_held_verify_pending(status: str) -> bool:
    """True if the status value LEADS with the HELD-VERIFY-PENDING token. Leading-token match
    only, mirroring _is_terminal_status, so a mid-string mention cannot claim the state."""
    if not status:
        return False
    head = re.sub(r"^[^0-9A-Z]+", "", status.upper())
    return head.startswith(HELD_VERIFY_PENDING_TOKEN)


def _qualified_held_verify_pending(status: str) -> tuple:
    """(is_qualified, owner, event) for a HELD-VERIFY-PENDING status.

    REFUSES -- returns is_qualified False -- unless BOTH an owner and a named re-read event are
    carried in the value. The caller MUST then treat the entry as OPEN. This refusal is half (b)
    of the ruling and the half that keeps the value honest."""
    if not _is_held_verify_pending(status):
        return (False, None, None)
    o = _HVP_OWNER_PAT.search(status)
    e = _HVP_EVENT_PAT.search(status)
    owner = o.group(1).strip().strip("*_ ") if o else None
    event = e.group(1).strip().strip("*_ ") if e else None
    return (bool(owner and event), owner or None, event or None)


_LEG_TABLE_PAT = re.compile(r"^\|\s*(?:leg|L\d+|id)\s*\|", re.M | re.I)
_LEDGER_CLASS_PAT = re.compile(r"\*\*Class:\*\*\s*deploy-completion", re.I)
_MANIFEST_HEAD_PAT = re.compile(r"^#{1,6}\s*Manifest\b", re.M | re.I)
# A doc whose OWN H1 calls it a deploy(-)completion ledger is one, even when it renders
# its evidence as free-form tables rather than the canonical `| leg |` manifest. Without
# this the shape filter silently drops hand-authored ledgers -- trading the filename
# blind spot for a layout blind spot, which is the same defect one axis over.
_LEDGER_TITLE_PAT = re.compile(r"^#{1,6}\s*DEPLOY[\s-]*(?:COMPLETION|LEDGER)", re.M | re.I)


def _is_deploy_ledger_shaped(md: Path) -> bool:
    """Is this .md a DEPLOY LEDGER, decided on CONTENT rather than on its filename?

    WHY THIS EXISTS: the scanner used to glob `*_deploy_completion.md`, so its population
    was a NAMING CONVENTION. Measured 2026-08-26: 122 of 551 entries sat outside that glob
    and 74 of them were non-terminal, while `check` reported 1 -- and SEVEN differed by a
    single character (`-deploy_completion.md`, hyphen where the glob wanted an underscore).
    A detector built to catch false-clean gate-bypasses had one of its own: it printed an
    honest denominator that certified the SWEEP and never the QUESTION.

    WHY NOT JUST WIDEN THE GLOB: the directory also holds ~51 approval records, plans,
    scan-findings and event logs that carry no status line and never had legs. Reporting
    those as "open or malformed" would trade a silent miss for a 51-entry false RED -- the
    over-reaping inversion. So the population is widened and the FILTER moves to content:
    a deploy ledger declares its class, renders a leg manifest, or heads a Manifest block.
    """
    try:
        text = md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return bool(_LEDGER_CLASS_PAT.search(text)
                or _LEG_TABLE_PAT.search(text)
                or _MANIFEST_HEAD_PAT.search(text)
                or _LEDGER_TITLE_PAT.search(text))


def _unindexed_open_ledgers(covered: set) -> list:
    """change_management/*_deploy_completion.md ledgers that represent an OPEN
    (non-terminal) deploy yet carry NO matching .open_deploys sentinel -- the
    false-clean gate-bypass class. `covered` = resolved .md paths already tracked
    by a live sentinel (reported via the sentinel scan). A ledger is treated as
    TERMINAL (skipped) when EITHER a **Status:** line leads with a terminal token
    OR an explicit close-date marker is present -- biased toward terminal so the
    loud RED never false-fires on the many CLOSED hand-authored ledgers. Returns
    [(path, reason, age_h), ...]."""
    out: list = []
    if not CM_DIR.is_dir():
        return out
    now = _now()
    for md in sorted(CM_DIR.glob("*.md")):
        if not _is_deploy_ledger_shaped(md):
            continue  # an approval record / plan / event log is not a deploy ledger
        try:
            if md.resolve() in covered:
                continue  # tracked by a live sentinel -- already reported above
        except OSError:
            pass
        status = _md_status(md)
        if status is not None and _is_terminal_status(status):
            continue  # CLOSED / COMPLETE / ROLLED-BACK status -- nothing stranded
        if _has_close_marker(md):
            continue  # explicit close-date marker (globgrph-style hand ledger)
        if _has_terminal_status_anywhere(md):
            continue  # CLOSE-BLOCK-at-foot shape: a terminal status line ANYWHERE
            #           in the doc's own status grammar (fix b, CTO GO 144651Z)
        # HELD-VERIFY-PENDING -- the third lifecycle state. A QUALIFIED one (owner + named
        # re-read event) is neither terminal nor open: --red must neither fire on it nor
        # swallow it, so it is skipped here. An UNQUALIFIED one is REFUSED and falls through
        # to be reported as OPEN, naming the missing field -- half (b) of ruling be7d73eb2a.
        if status is not None and _is_held_verify_pending(status):
            ok, owner, event = _qualified_held_verify_pending(status)
            if ok:
                continue
            missing = " and ".join(
                m for m, v in (("an owner", owner), ("a named re-read event", event)) if not v)
            reason = (f"REFUSED HELD-VERIFY-PENDING (missing {missing}) -- read as OPEN: "
                      "a hold without both is indistinguishable from an abandonment")
            try:
                mtime = datetime.fromtimestamp(md.stat().st_mtime, timezone.utc)
                age_h = (now - mtime).total_seconds() / 3600.0
            except OSError:
                age_h = -1.0
            out.append((md, reason, age_h))
            continue
        if status is None:
            reason = "no **Status:** and no close-date marker (open or malformed)"
        else:
            reason = f"status='{status[:60]}' (not a terminal/closed state)"
        try:
            mtime = datetime.fromtimestamp(md.stat().st_mtime, timezone.utc)
            age_h = (now - mtime).total_seconds() / 3600.0
        except OSError:
            age_h = -1.0
        out.append((md, reason, age_h))
    return out


def _load_unindexed_red_state() -> dict:
    if UNINDEXED_RED_STATE.exists():
        try:
            return json.loads(UNINDEXED_RED_STATE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
    return {}


def _save_unindexed_red_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    UNINDEXED_RED_STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def _red_alert_unindexed(md: Path, reason: str, age_h: float) -> None:
    """RED delivery for an UNINDEXED open ledger -- the gate-bypass that the
    sentinel-only scan was blind to. Same alert-not-block class as _red_alert."""
    COO_INBOX.mkdir(parents=True, exist_ok=True)
    try:
        rel = md.relative_to(WORKSPACE)
    except ValueError:
        rel = md
    subject = f"RED__UNINDEXED_open_deploy_ledger__gate_bypass__{md.stem}"
    fname = f"{_ts()}_deploy-ledger_{subject}.md"
    body = (
        "# Message from deploy_ledger.py (gate-bypass scan)\n"
        "**To:** 2.0.0_SA_COO\n"
        f"**Date:** {_ts()}\n"
        "**Subject:** RED: UNINDEXED open deploy-completion ledger -- gate-bypass "
        "(invisible to the sentinel-only --red scan)\n\n"
        f"Ledger: {rel}\n"
        f"Reason: {reason}\n"
        f"Age (file mtime): {age_h:.1f}h\n\n"
        "This deploy-completion ledger declares an OPEN/non-terminal deploy but has "
        "NO .open_deploys/*.json sentinel, so the sentinel-only `check --red` scan "
        "was structurally blind to it (the false-clean class: a hand-authored "
        "markdown ledger is content-complete but INVISIBLE to the gate).\n\n"
        "NEVER-law e38cc2b16: a begun deploy FINISHES in-session or rolls back + "
        "escalates loud. RESOLVE by either:\n"
        "  (a) closing it -- set the ledger's **Status:** to a terminal state "
        "(CLOSED / COMPLETE / ROLLED BACK) once every leg is proven; or\n"
        "  (b) re-homing it onto the tracked path -- open via `deploy_ledger.py "
        "open ...` so it carries a sentinel the gate can see.\n")
    (COO_INBOX / fname).write_text(body, encoding="utf-8", newline="\n")
    print(f"RED: unindexed-ledger alert delivered to COO inbox: {fname}")


# A sentinel the Layer-1 scan can reason about MUST carry these. They are exactly the keys the scan
# dereferences unguarded (opened_at :664, legs :667, slug in the alert paths) -- the writer (cmd_open)
# always emits them, so a sentinel missing one was NOT writer-produced (it was hand-authored, or a
# foreign-schema record dropped into the state dir).
REQUIRED_SENTINEL_KEYS = ("slug", "opened_at", "legs")


def _read_sentinel(sp):
    """Return the parsed sentinel dict, or a STRING describing why it is unusable.
    Never raises: a sentinel we cannot read is a LOUD verdict for the caller, never a crashed sweep."""
    try:
        state = json.loads(sp.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001 -- unparseable JSON is a finding, not a traceback
        return f"UNPARSEABLE JSON ({type(e).__name__}: {str(e)[:80]})"
    if not isinstance(state, dict):
        return f"not a JSON object (got {type(state).__name__})"
    missing = [k for k in REQUIRED_SENTINEL_KEYS if k not in state]
    if missing:
        return (f"missing required key(s) {missing} -- has {sorted(state)[:8]}; "
                f"not a deploy_ledger sentinel (writer emits slug/opened_at/legs/entry_path/window_hours)")
    if not isinstance(state["legs"], list):
        return f"'legs' is {type(state['legs']).__name__}, expected list"
    try:
        datetime.fromisoformat(state["opened_at"])
    except Exception:  # noqa: BLE001
        return f"'opened_at' unparseable ({state.get('opened_at')!r})"
    return state


def cmd_check(args) -> int:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    now = _now()
    exit_flag = False       # any NON-HELD open ledger / HELD-STALE / bypass -> check exits 1
    held_count = 0          # KNOWN-HELD (sovereign/external-gated, non-stale) -> visible, NOT a RED
    drift_benign = 0        # Layer 3: entry claims terminal, sentinel live, every leg proven
    drift_dangerous = 0     # Layer 3: entry claims terminal over a GENUINELY UNPROVEN leg (WARN)
    covered: set = set()
    stale_days = getattr(args, "held_stale_days", None) or DEFAULT_HELD_STALE_DAYS

    # --- Layer 1: tracked sentinels (the original, sound, in-window scan) ---
    sentinels = [sp for sp in sorted(STATE_DIR.glob("*.json"))
                 if not sp.name.startswith(".")]
    malformed = []          # schema-violating / unparseable sentinels -> LOUD, never a crash, never silent
    scanned = 0
    for sp in sentinels:
        # MALFORMED IS A VERDICT, NOT A CRASH (CTO gate-integrity dispatch 205615Z). A KeyError here
        # aborted the WHOLE sweep, leaving every sentinel AFTER the bad one unscanned -- so the
        # no-half-deploys instrument (NEVER#6) failed WITHOUT rendering a verdict, which is strictly
        # worse than failing loudly: a crashed red-scan cannot assert "0 stranded" but reads like it
        # never got the chance to. Same law as the R1R3 appender: UNKNOWN IS NOT A VERDICT -- an entry
        # we cannot parse has UNKNOWN legs, never "proven", and the scan CONTINUES to completion.
        state = _read_sentinel(sp)
        if isinstance(state, str):          # _read_sentinel returns the failure REASON as a str
            malformed.append((sp.name, state))
            print(f"MALFORMED-ENTRY [LOUD]: {sp.name} -- {state}. NOT SCANNED: this sentinel's legs are "
                  f"UNKNOWN, not proven. A malformed entry cannot assert 'nothing stranded' (NEVER#6). "
                  f"FIX: repair via deploy_ledger.py (open/close-leg/close) -- never hand-author a "
                  f"sentinel; a CLOSED deploy has NO file here (close unlinks it).")
            continue
        scanned += 1
        opened = datetime.fromisoformat(state["opened_at"])
        age_h = (now - opened).total_seconds() / 3600.0
        window = args.window_hours or state.get("window_hours", DEFAULT_WINDOW_HOURS)
        open_legs = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
        try:
            covered.add((WORKSPACE / state["entry_path"]).resolve())
        except (KeyError, OSError):
            pass

        # --- Layer 3: entry-vs-sentinel DRIFT (WARN-class; never a RED, never exit-1) ---
        # Deliberately non-blaring: it reports a RECORD inconsistency, not a stranded deploy,
        # and must not be able to false-alarm the fabric. Escalation to RED is a governance
        # call (COO/CTO), not this tool's to make unilaterally. CTO 20260709T191228Z: DANGEROUS
        # stays WARN until the detector is exercised + has a 7d zero-FP window + an audited
        # bypass -- an unexercised hard-fail is how a gate earns an --no-verify habit.
        drifted, md_status, unproven = _entry_prose_drift(state)
        if drifted:
            if unproven:
                drift_dangerous += 1
                print(f"DRIFT-DANGEROUS [WARN]: {state['slug']} entry reads terminal "
                      f"('{md_status[:38]}') while leg(s) {unproven} carry NO proof -- a NEVER#6 "
                      f"bypass wearing a compliance mask. The record disagrees with the gate. "
                      f"Fix: deploy_ledger.py close-leg/close (never hand-edit the entry).")
                if args.red:
                    last = state.get("last_drift_warn_at")
                    if last and (now - datetime.fromisoformat(last)).total_seconds() < DRIFT_WARN_SUPPRESS_HOURS * 3600:
                        print(f"  (drift WARN suppressed -- last {last}, re-warns each {DRIFT_WARN_SUPPRESS_HOURS}h)")
                    else:
                        _drift_warn_alert(state, md_status, unproven)
                        state["last_drift_warn_at"] = now.isoformat()
                        _save(state)
            else:
                drift_benign += 1
                print(f"DRIFT: {state['slug']} entry reads terminal ('{md_status[:38]}') while its "
                      f"sentinel is LIVE -- benign; every leg is proven, the close was never run "
                      f"through the tool. Fix: deploy_ledger.py close (never hand-edit the entry).")

        # HELD / SOVEREIGN-GATED: structurally verified off the legs (all apply legs proven + only
        # verify open + a named structured gate). A KNOWN-HELD ledger is NOT a half-landed RED -- it
        # stays visible + tracked and only escalates to HELD-STALE past the staleness threshold. The
        # guardrails read the LEGS, so a half-landed strand (an open APPLY leg) can never reach here.
        held_ok, held_reason = _qualifies_as_held(state)
        if held_ok:
            gate = state["gate"]
            held_days = _held_age_days(state, now)
            rr = gate.get("reread") or {}
            # HS-2: a hold past ITS OWN stated re-read date is its own finding class with its own
            # line vocabulary. It is NEVER merged into an aged OPEN (that would call a deliberate
            # hold neglect) and never into HELD-STALE (that is the GLOBAL age cadence, a different
            # claim about a different thing). Checked BEFORE the age cadence so the sharper,
            # owner-stated condition wins when both would fire.
            # WARNING: PRINT-ONLY BY CONSTRUCTION -- no nudge, no alert, no inbox write. The notification
            # moratorium stands and this class deliberately reaches for none: it surfaces in the
            # existing check output and nothing more.
            past_reread = False
            if rr.get("kind") == "date":
                try:
                    past_reread = datetime.strptime(rr["value"], "%Y-%m-%d").replace(
                        tzinfo=timezone.utc) < now
                except (ValueError, KeyError, TypeError):
                    past_reread = False   # a malformed date cannot fire the class; (d) already gates it
            if past_reread:
                exit_flag = True
                hd = f"{held_days:.1f}d" if held_days is not None else "?"
                print(f"HELD-PAST-REREAD: {state['slug']} re-read-due={rr['value']} (stated by the "
                      f"hold itself) held={hd} gate={gate['type']}/{gate['ref']} "
                      f"open-verify={open_legs} author={state['author']} "
                      "-- the hold's OWN re-read date has passed: re-read it, do not treat it as "
                      "neglect and do not treat it as closed")
                continue
            if held_days is not None and held_days > stale_days:
                exit_flag = True    # a legit hold sat too long -> a DISTINCT nudge (not the half-land RED)
                print(f"HELD-STALE: {state['slug']} held={held_days:.1f}d (>{stale_days}d) "
                      f"gate={gate['type']}/{gate['ref']} "
                      f"re-read={rr.get('kind')}={rr.get('value')} open-verify={open_legs} "
                      f"author={state['author']} -- nudge the gate or reconsider")
                if args.red:
                    last = state.get("last_held_nudge_at")
                    if last and (now - datetime.fromisoformat(last)).total_seconds() < HELD_NUDGE_SUPPRESS_HOURS * 3600:
                        print(f"  (HELD-STALE nudge suppressed -- last {last}, re-nudges each {HELD_NUDGE_SUPPRESS_HOURS}h)")
                    else:
                        _held_nudge_alert(state, held_days)
                        state["last_held_nudge_at"] = now.isoformat()
                        _save(state)
            else:
                held_count += 1
                hd = f"{held_days:.1f}d" if held_days is not None else "?"
                print(f"HELD: {state['slug']} [{HELD_STATUS}] held={hd} gate={gate['type']}/{gate['ref']} "
                      f"re-read={rr.get('kind')}={rr.get('value')} "
                      f"open-verify={open_legs} author={state['author']} "
                      "-- apply legs proven, only verify open; tracked-not-stranded")
            continue

        # NOT held -> the original OPEN / stranded logic (preserves the exit-1-on-any-open contract).
        # A ledger that CLAIMS a hold (a gate is set) but does NOT qualify (e.g. an open apply leg) is
        # flagged LOUDLY -- the anti-escape-hatch fired: a half-landed strand can't hide behind a gate.
        exit_flag = True
        gate_note = f" [HELD-CLAIM REJECTED: {held_reason}]" if state.get("gate") else ""
        flag = "PAST-WINDOW" if age_h > window else "in-window"
        print(f"OPEN: {state['slug']} age={age_h:.1f}h window={window}h [{flag}] "
              f"stranded={open_legs} author={state['author']}{gate_note}")
        if args.red and age_h > window:
            last_red = state.get("last_red_at")
            if last_red and (now - datetime.fromisoformat(last_red)).total_seconds() < window * 3600:
                print(f"  (RED suppressed -- last alert {last_red}, re-alerts each {window}h)")
            else:
                _red_alert(state, age_h)
                state["last_red_at"] = now.isoformat()
                _save(state)

    # --- Layer 2: gate-bypass scan -- OPEN markdown ledgers with NO sentinel ---
    # (the false-clean class the sentinel-only scan was structurally blind to).
    bypass = _unindexed_open_ledgers(covered)
    if bypass:
        red_state = _load_unindexed_red_state() if args.red else {}
        changed = False
        for md, reason, age_h in bypass:
            try:
                shown = md.relative_to(WORKSPACE)
            except ValueError:
                shown = md
            print(f"BYPASS: UNINDEXED OPEN LEDGER {shown} age={age_h:.1f}h -- {reason}")
            if args.red:
                key = str(md.resolve())
                last = red_state.get(key)
                # --all: FULL RE-ENUMERATION on demand (CTO extension leg 3). The per-finding
                # suppression below is what keeps a standing backlog from re-flooding COO every
                # sweep (signal-dilution: a backlog that re-fires buries the genuinely NEW bypass).
                # --all deliberately overrides it for a deliberate full census -- an operator asking
                # "show me EVERYTHING right now" must not be answered from a suppression cache.
                if (last and not getattr(args, "all", False)
                        and (now - datetime.fromisoformat(last)).total_seconds() < DEFAULT_WINDOW_HOURS * 3600):
                    print(f"  (RED suppressed -- last alert {last}, re-alerts each {DEFAULT_WINDOW_HOURS}h; "
                          f"--all to force full re-enumeration)")
                else:
                    _red_alert_unindexed(md, reason, age_h)
                    red_state[key] = now.isoformat()
                    changed = True
        if args.red and changed:
            _save_unindexed_red_state(red_state)

    # Layer-3 counter (CTO-specified): a standing, countable signal even when the board is otherwise
    # clean. Never touches exit_flag -- a record inconsistency is not a stranded deploy.
    if drift_benign or drift_dangerous:
        print(f"DRIFT SUMMARY: {drift_dangerous} DANGEROUS (WARN; entry terminal over an unproven leg), "
              f"{drift_benign} benign (nudge; entry terminal, all legs proven). "
              "The .md is a RENDERING of the sentinel -- never hand-edit it.")

    # DENOMINATOR OF THE SWEEP, always printed: a verdict about "nothing stranded" is only as good as
    # the population it actually covered. A malformed entry is EXCLUDED from the scan, so an OK that
    # does not disclose the exclusion is the misleading-PASS class.
    print(f"SCAN DENOMINATOR: {scanned} of {len(sentinels)} sentinel(s) scanned"
          + (f"; {len(malformed)} MALFORMED (unscanned, legs UNKNOWN)" if malformed else ""))
    if malformed:
        print("MALFORMED SUMMARY -- these entries were NOT scanned and their legs are UNKNOWN, "
              "never 'proven':")
        for name, why in malformed:
            print(f"  - {name}: {why}")
        print("  A red-scan that cannot read an entry cannot assert 0-stranded for it. Repair or close "
              "each via deploy_ledger.py; exit is NON-ZERO until they parse.")
        exit_flag = True    # UNKNOWN-is-not-a-verdict: unreadable entries fail the check, loudly

    if not exit_flag and not bypass:
        if held_count:
            print(f"OK: no stranded/open deploys; {held_count} HELD-SOVEREIGN-GATED "
                  "(visible + tracked, apply-proven, NOT half-landed)")
        else:
            print("OK: no open deploy ledgers + no unindexed open ledgers -- nothing half-landed")
        return 0
    return 1


def cmd_list(args) -> int:
    return cmd_check(argparse.Namespace(window_hours=None, red=False,
                                        held_stale_days=DEFAULT_HELD_STALE_DAYS))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("open", help="open a completion ledger at deploy START")
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--author", required=True)
    p.add_argument("--leg", action="append",
                   help="'id|kind|target|proof_required' (repeatable)")
    p.add_argument("--lambda", dest="lambda_fn", action="append",
                   help="single-Lambda TF deploy: add ONE 'tf-lambda' leg for this "
                        "function (tf_resource from lambda-source-map) INSTEAD of the "
                        "--pipeline S3-code expansion. Use this (not --pipeline) for a "
                        "single-function TF apply so close() does not blare on phantom "
                        "S3-code legs the deploy never touched. (repeatable)")
    p.add_argument("--pipeline", help="add canonical legs for this pipeline dir "
                                      "(PIPELINE_MAP x VALID_LAYERS + AUX_CODE_PREFIXES). "
                                      "For a single-lambda TF deploy use --lambda instead.")
    p.add_argument("--window-hours", type=float, default=DEFAULT_WINDOW_HOURS)
    p.set_defaults(fn=cmd_open)

    p = sub.add_parser("close-leg", help="record one leg's verification proof")
    p.add_argument("--slug", required=True)
    p.add_argument("--leg-id", required=True)
    p.add_argument("--proof", required=True)
    p.set_defaults(fn=cmd_close_leg)

    p = sub.add_parser("close", help="close the ledger (refuses if any leg unproven)")
    p.add_argument("--slug", required=True)
    p.set_defaults(fn=cmd_close)

    p = sub.add_parser("hold", help="mark a ledger HELD/SOVEREIGN-GATED (apply legs proven, only verify "
                                    "open, blocked on a NAMED sovereign/external gate) -> stops the "
                                    "half-landed RED cry-wolf but stays visible + tracked; --release to clear")
    p.add_argument("--slug", required=True)
    p.add_argument("--gate-type", choices=sorted(GATE_TYPES),
                   help="the gate class: 'sovereign' (Andrew/human sign-off) or 'external' "
                        "(a third-party / cross-system dependency)")
    p.add_argument("--gate-ref",
                   help="the SPECIFIC named dependency (e.g. 'Andrew cross-region PAT') -- not prose; "
                        "a vague 'waiting on something' is refused")
    p.add_argument("--reread-date", metavar="YYYY-MM-DD",
                   help="REQUIRED (or --reread-event): the date to look at this hold again. Past it, "
                        "the hold re-surfaces as HELD-PAST-REREAD -- its OWN finding class, never an "
                        "aged OPEN")
    p.add_argument("--reread-event", metavar="'<named event>'",
                   help="REQUIRED (or --reread-date): the NAMED event that ends the hold. An "
                        "event-gated hold cannot go past a date, so it re-surfaces on the age cadence "
                        "with its event printed -- never silently conflated with a date-gated one")
    p.add_argument("--release", action="store_true", help="clear the hold -> back to OPEN")
    p.set_defaults(fn=cmd_hold)

    p = sub.add_parser("check", help="report OPEN ledgers; exit 1 if any; --red alerts COO")
    p.add_argument("--red", action="store_true")
    p.add_argument("--all", action="store_true",
                   help="force FULL re-enumeration: ignore per-finding RED suppression "
                        "(a deliberate census must not be answered from a suppression cache)")
    p.add_argument("--window-hours", type=float, default=None)
    p.add_argument("--held-stale-days", type=float, default=DEFAULT_HELD_STALE_DAYS,
                   help="a HELD/SOVEREIGN-GATED ledger older than this escalates to HELD-STALE "
                        "(a distinct nudge, not the half-landed RED); default %(default)s")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("list", help="alias for check (no RED)")
    p.set_defaults(fn=cmd_list)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
