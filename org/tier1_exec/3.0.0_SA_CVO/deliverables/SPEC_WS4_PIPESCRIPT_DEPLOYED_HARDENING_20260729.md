# WS4 SPEC: comp-pipescript deployed — two measured failure modes, both indistinguishable from truth

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~17:10Z · **archetype:** IMPLEMENT(spec-only)
**Andrew-direct (my terminal ~17:08Z):** *"comp-pipescript deployed is unreliable as I used it: a
bare basename silently defaults to the wrong tree and returns a clean-looking zero, and the
full-path form false-positives STALE on CRLF. Both failure modes are indistinguishable from truth
without an independent content diff. Filed as a tool gap."* COO's 165733Z #4 carries the same
first fixture independently. **Owner: 1.0.0_SA_CTO~C (WS4).**

## Mechanisms, source-confirmed (`org/modules/graph/pipeline_cli.py`)

- **D-1 wrong-tree default:** `pipeline="bd-gold"` is the documented "backward-compatible default"
  (:221). Full paths auto-detect their tree (:1316-1332); a BARE BASENAME does not and falls into
  the bd graph → `0 MATCH, 0 STALE, 0 UNCOVERED`, rc=0 — **byte-identical to a genuine clean
  sweep, on the wrong population, with the population unnamed.** Three states (did-not-look /
  looked-clean / looked-BROKEN) collapse to one glyph.
- **D-2 CRLF false-STALE:** `cmd_deployed` (:1804) compares `hashlib.md5(local_path.read_bytes())`
  — WORKING-TREE bytes — against the S3 ETag (:1825, :1890). A CRLF working copy vs an LF-uploaded
  artifact reads STALE with zero content difference. (Today's CRLF class, surfacing inside a
  verification instrument — the instrument inherits the estate's line-ending nondeterminism.)
- **D-3 latent, declare while in there:** ETag == MD5 only for single-part uploads (standing law:
  "multipart ETags are not MD5s"). Scripts are small today; the boundary goes undeclared.

## The fix, three parts

1. **D-1 → REFUSE-OR-RESOLVE, never default:** bare basename with no `--pipeline` searches ALL
   PIPELINE_MAP trees: unique hit → proceed with the tree NAMED in output ("resolved to inf-gold");
   ambiguous → rc=2 listing candidates; zero hits → rc=2 "not in any tree" (the comp-grep
   failed-retrieval convention). The bd-gold default dies. **Every output names the tree(s)
   searched — a population, not just a denominator** (COO requirement #3).
2. **D-2 → three-tier verdict:** `MATCH` (raw md5 == ETag) / **`EOL-DRIFT`** (raw differs,
   LF-normalized md5 matches — never reported as STALE; one-line remediation hint pointing at the
   F-2/F-3 renormalization work) / `STALE` (normalized content genuinely differs). Comparison basis
   printed per file.
3. **rc REFLECTS THE VERDICT** (COO fixture: today it exits rc=0 on a real STALE, so rc-derived
   PASS columns cannot record failure): rc=0 all-MATCH/EOL-DRIFT · rc=1 any STALE/MISSING · rc=2
   failed retrieval/ambiguity. Plus the O2 footer (examined-N-of-M per tree) and D-3's boundary
   declared (multipart ETag → fall back to size + ranged-GET content hash, stated in output).

## Acceptance battery (pre-stated)

1. COO's fixture: a bare mdpf-script basename must refuse-or-resolve — never a silent bd-tree zero.
2. A file differing ONLY in line endings vs its deployed copy reads EOL-DRIFT, not STALE (construct
   by CRLF-flipping a known-MATCH file locally).
3. Mutant: a genuinely-edited file reads STALE with rc=1 (proving the normalized comparison still
   catches real drift — the EOL fix must not create a false-MATCH class).
4. Positive control per tree: one known-deployed script per PIPELINE_MAP tree resolves and MATCHes.
5. Output-not-rc: verdicts scored from printed text in all four cases (harness-rc corruption law).

## MECHANISM AUDIT (Andrew-ordered deep dive, ~17:50Z — five measured facts)

1. **The hand-synced PIPELINE_MAP fallback is byte-equal today AND DORMANT** — `pipeline_cli.py:34-35`
   puts `.tools` on sys.path, so the real map imports under real invocation (probe-verified; my
   first cd-based probe was a harness artifact, self-corrected). Latent hazard only: the fallback
   fires on an undeclared "some invocation contexts" condition with nothing marking the switch.
   WS4 add: log which map branch loaded, one line.
2. **The bd-gold default is DOUBLE:** the documented bare-id fallthrough (:1841-1845 "backward
   compatible") AND `_PIPELINE_SILVER_DIRS.get(pipeline, <bd silver dir>)` — an unmapped pipeline's
   silver comparisons silently read BLACK_DIAMOND's silver tree. Both die in refuse-or-resolve.
3. **The sovereign-hold skip is CORRECT behavior with a STALE comment** — measured:
   `SOVEREIGN_HELD_BUCKETS = ()` ("Retracted 2026-07-14 → always False by design"); the retraction
   propagated to the enforcing copy. The :1890-vicinity comment still describes the hold as live;
   fix the comment, not the code. (Hypothesis that 15 days of bd checks were no-ops: REFUTED.)
4. **THE REAL HAND-WRITTEN-NOT-CURRENT DEFECT: the mdpf layer tuple.** `build_mdpf_dag`
   (`extract_pipeline.py:1331`) globs `("gold","backfill","feeders","bronze")` — live bucket census
   (36 objects `code/scripts/<layer>/`, written TODAY) shows **`assets_gold` and `silver` layers
   the tuple omits**: `code/scripts/assets_gold/build_cottonwood_mdpf_{pair,slice}.py` (deployed
   05:09Z today) and `code/scripts/silver/rebalancer_schemas.py` are INVISIBLE to the mdpf DAG,
   the deployed sweep, io, and postdeps. **And the assets_gold scripts' repo home is
   `data/assets/scripts/gold/` — the ASSETS tree — a CROSS-TREE deploy the per-tree glob model
   structurally cannot represent** (assets is not a comp-pipescript tree at all). The scope with
   no coverage is COTTONWOOD's — the known problem child. WS4 add: derive mdpf layers from the
   LIVE `code/scripts/` listing (or a declared manifest), never a hand tuple; cross-tree script
   homes need an explicit (repo-home → deploy-prefix) mapping entry, C-3 style.
5. **Dual-layout residue quantified:** 36 `code/scripts/<layer>/` vs 2 legacy `code/<layer>/` + 3
   loose `code/<file>` — the tool's chosen layout is the right dominant one; the 5 stragglers are
   teardown-wave rows, not tool logic.

## Sequencing

Post-fires, ~C's queue AFTER WS1 steps 2-3 (nothing here blocks WS2; this is an independent
hardening of an existing instrument). One rail change at a time still binds. CVO recuses from
build; verifies against this battery.

— 3.0.0_SA_CVO
