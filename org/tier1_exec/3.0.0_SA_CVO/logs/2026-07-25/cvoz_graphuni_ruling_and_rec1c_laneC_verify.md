# CVO~Z session log — 2026-07-25, GRAPHUNI re-measurement RULING + REC-1c LANE-C verification

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`

---

## 1 · NFRA_GRAPHUNI.P2/D2 fresh re-measurement — verified, then RULED (Andrew-delegated)

`0.8.0_AE_CloudComp~D` delivered the re-measurement I dispatched (`45e6a3548`), using the P0-CVO
fixture's own recipe as instructed. Andrew had delegated the architectural decision to me ("reopen it,
have CVO deal with it").

**CONFIRMED, independently re-derived:** counts re-tallied from the raw `per_target` statuses with my own
parser — comp-blast 11/28, comp-trace 2/8, comp-xref 0/9 = **13/45 (28.9%)**, exact match. Sharp case
`gold:D_01.partner_analytics` script-level reproduces at **13 today vs 216 old** — the regression is LIVE,
not stale, and a month of estate growth did not close it. Function-level
`generate_header_metrics` = 39/39 exact. Mechanism citation real at `comp_marker_read.py:230`. Method
sound (drove real `cli.main()` rather than reimplementing answer logic; id-canonicalization precondition
applied).

**REFINEMENT 1 — the discriminator is RADIUS, not grain.** ~D reported "function-grain clean, script-grain
broken." I classified all 28 blast targets myself: script **0/6**, s3-artifact **0/6**, function **11/16**
— so 5 function-level targets fail, and the s3-artifact bucket isn't script-grain-rollup output at all.
Sorting by old radius gives a perfect separation instead: **every target with `old_n <= 52` MATCHES
(12/12); every target with `old_n >= 76` MISMATCHES (15/15).** The single sub-76 exception
(`s3:silver/allocations`, old=31 new=48) is the only zero-missing/pure-growth row, so not a counterexample.
Grain and radius are confounded in this sample — the script targets happen to be the big ones.

*(Retrieval note: `missing_from_new` reads exactly 20 on every mismatch row — that is list TRUNCATION in
the JSON, not a real count. I reasoned from `old_n`/`new_n` and `extra_in_new` instead. Reporting
"20 missing" as a finding would have been a truncation artifact dressed as data.)*

**REFINEMENT 2 — the decision-changing one: the rollup CANNOT close this gap even if perfectly repaired.**
Counted the pre-delta fixture's own s3 edge population (`graph.json.pinned_predelta`, read-only) by grain
AND direction. Both of the docstring's figures confirm exactly (445 script-touching / 131
function-touching). Decomposed:
- `WRITES_S3` script->s3 = 139; function->s3 = 131 → rollup input exists, ~1:1. Plausible.
- `READS_S3` s3->script = 306; s3->function = **0**.

**There are ZERO function-grain READS_S3 edges.** The rollup only rolls up edges that exist, so it must
synthesize 306 script-side READS from 0 inputs — structurally impossible, not a logic bug. And READS is
precisely what drives inbound cross-script reachability, which is *why* large radii collapse and small ones
don't: my radius finding and ~D's grain finding converge on one root, but the **fix layer** differs.

**RULING (recorded; Andrew-delegated):**
- **Option 3 (re-baseline the fixture): REJECTED** — papers over a live, reproducible loss.
- **Option 4 (~D's targeted script-grain rollup repair): REJECTED on measurement** — repairs a mitigation,
  not the defect. Would land as a partial fix that re-fails on the next traversal: the same shape as the
  `DescribeTable`-vs-whole-policy trap in *today's own* `BoundedDeriveReadOnly` commit. Same trap, same
  session.
- **This CONFIRMS the original 2026-07-01 deferral VERBATIM** — *"NOT closeable at the read-handle (the
  edges aren't there to canonicalize)."* A month later, on fresh data, that call was right. It does not
  need relitigating.
- **Fix layer = the COMPUTE POPULATION** (options 1/2 territory): the producer must emit `READS_S3` edges,
  which it currently does not at any grain the projection can consume.
- **Deliberately NOT ruled: option 1 vs option 2.** I have not grounded either one's feasibility, and
  picking blind is how a plausible-but-wrong architecture call gets ratified. The bounded discriminator I
  named and routed: *can the GRAPHUNI Phase-A/B compute producer emit `READS_S3` at function grain (option 1
  viable), or does that relationship only exist in `build_graph`'s AST pass (option 2 forced)?* Source
  question, no measurement needed. Routed to CTO~Z to dispatch; told ~D not to start it off my message.

## 2 · REC-1c LANE-C (`0.8.0_AE_CloudComp~C`) — verified clean

First of five parallel batches. **Counts:** re-tallied raw sidecar rows myself — 10 MATCH / 4 MISMATCH /
2 UNKNOWN = 16, exact, 0 skipped, UNKNOWNs properly first-class rather than counted as passes.

**All 4 MISMATCHes re-derived** (own probe strings, rc captured directly, not through a pipe):
comp-registry rc=1 LOUD (louder than declared); comp-tool-health rc=0 plain not-found string;
comp-tool-health-gate rc=0; comp-coverage rc=0 with a well-formed 0.0% report. All confirmed.

**Both mechanism claims source-confirmed:** `_render_tool` returns a bare f-string on not-found with no
raise/exit; `load_effective_feed`'s docstring says verbatim *"a missing/unreadable file returns {} … never
a crash"* with matching code. ~C correctly characterized the gate as by-design rather than a defect.

**My refinement, on the candidate L0b ABSENT axis CTO~Z asked about — bank it, but the 5 instances are NOT
homogeneous.** They share `rc=0`; they do NOT share silence:
- **Disclosed degrade (4 of 5):** the gate printed *"no feed (EFFECTIVE pending) -- STALE"* as line 1;
  comp-surface-check `scan` printed the ADVISORY skip; comp-freshness printed *"Prefix not found"*;
  comp-tool-health printed a plain not-found string.
- **Undisclosed (1 of 5) — the dangerous one: comp-coverage.** It printed a real corpus
  ("1,127 TO IDs / 1,757 TO files") then "Total TOs: 0 / Raw coverage: 0.0%" with **no** signal that the
  nonexistent pipeline filter was the cause. A reader cannot distinguish that 0.0% from a real finding.

So the axis to bank is not *"goes silent on absent input"* but **"rc-silent on absent input, with stdout
disclosure varying independently"** — load-bearing because automation gates on `rc` (all 5 fail uniformly)
while humans read stdout (only comp-coverage genuinely misleads). A single collapsed ABSENT value would
lose that. Also noted: the gate emits a confident commission table (FIX 8 / RETIRE 4, named tools +
ratifiers) on a nonexistent feed — honest header, confident body, its own readable-past hazard.

**Queue disclosed, not assumed:** `REC1C_E` and `REC1C_base` were already on disk unverified when I
reported; flagged to CTO~Z rather than letting coverage be presumed.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| Python (own parsers) over `REASSERT_20260725_result.json` | PASS | independent count re-tally + my own grain/radius classification |
| Python (own parser) over `graph.json.pinned_predelta` | PASS — **decisive finding** | s3 edge population by grain AND direction; found the 306-vs-0 READS asymmetry that refuted option 4 |
| `sed`/`grep` over `comp_marker_read.py` | PASS | mechanism confirmed at source (`:230` rollup), and read the implementation to assess fix-layer |
| Python (own tally) over `REC1C_C.sidecar.json` | PASS | 10/4/2 = 16 independently confirmed |
| `comp-registry` / `comp-tool-health` / `comp-tool-health-gate` / `comp-coverage` (4 separate invocations) | PASS | all 4 lane-C mismatches independently reproduced, own probe strings |
| `sed` over `comp_tool_health.py` | PASS | both mechanism claims source-confirmed verbatim |

**Retrieval traps hit and avoided this pass (both recorded rather than quietly corrected):** a redirect to
an unwritable `/tmp` returned `rc=1` that was the *redirect* failing, not the tool — caught because I
captured rc directly, and because ~C had disclosed the identical piped-`head` trap in their own delivery.
And `missing_from_new` truncation at 20 would have been reportable as a false count.
