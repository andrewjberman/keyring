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

## Sequencing

Post-fires, ~C's queue AFTER WS1 steps 2-3 (nothing here blocks WS2; this is an independent
hardening of an existing instrument). One rail change at a time still binds. CVO recuses from
build; verifies against this battery.

— 3.0.0_SA_CVO
