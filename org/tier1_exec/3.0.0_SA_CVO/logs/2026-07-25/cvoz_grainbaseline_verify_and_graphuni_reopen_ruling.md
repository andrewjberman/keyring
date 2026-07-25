# CVO~Z session log — 2026-07-25, grain_baseline recert verify + GRAPHUNI reopen ruling

**archetype:** MIXED (VALIDATE + COORDINATE)
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`

---

## 1 · grain_baseline.json EXTERNAL_ENDPOINT recertification — independently verified

`0.8.0_AE_CloudComp~D` drafted a recertification of `grain_baseline.json`'s `per_class.EXTERNAL_ENDPOINT`
(3 -> 0), citing: commit `9a70418a7b` (a deliberate 2026-06-26 Andrew-direct drop of the EXTERNAL_ENDPOINT
node type from the canonical graph, not a bug) and `grain_sentinel.py`'s `check_magnitude` skip-on-`base<=0`
mechanism. ~D was `ANY_EXEC`-locked out of committing it; `1.0.0_SA_CTO~Z` landed it (`0e97e0350f`) after
its own verification and asked me to independently re-derive rather than trust either read.

**Independently re-derived, own commands:**
- `git log -1`/`git show` on `9a70418a7b`: verbatim matches the quoted rationale — deliberate,
  Andrew-direct, CTO-arch-gated, CVO-signed taxonomy simplification; source-read the actual diff
  (`DROP_NODE_TYPES` frozenset + `drop_node_types()`).
- `grain_baseline.json`'s own `certified` field: `"2026-06-11 post-pagination-fix complete graph"` —
  confirmed, predates the drop by 15 days (the entire premise of the recert).
- `grain_sentinel.py:128`: `if base <= 0: continue` — confirmed exact mechanism; recertifying to 0 makes
  the sentinel permanently skip this class.
- **Live mutant re-run**, own shell, post-fix: `derive_stitch.py` now reports `GRAIN-SENTINEL: FAIL (5
  violation group(s))` — EXTERNAL_ENDPOINT specifically absent from the list (was 6 groups before). All
  three legs hold; nothing further needed.

## 2 · NFRA_GRAPHUNI.P2/D2 reopen — Andrew-direct, ruled

Andrew-direct (relayed via CTO~Z, verbatim): *"reopen it, have CVO deal with it."* Routed to me (not base
CVO) since I hold context on the thread and the original escalation target (`CVO~B`) isn't a live lane.

Context: `comp_marker_read.py` (built 2026-07-01, this same `~D` lane, NFRA_GRAPHUNI.P2/D2) is the
already-built re-point infrastructure CANON2's Leg B needs. Its wiring into `cli.py`/`platinum_cli.py` was
deliberately deferred (`42b7f3c48a`, 2026-07-01) after a real coverage regression: marker-head projection
2040n/2353e vs pre-delta `build_graph`'s 2152n/2772e; one script's blast radius came back 13 vs expected
216. Escalated to `COO~B`/`CVO~B`/`CTO` a month ago, never resolved.

**Independently verified before ruling, own commands (did not act on ~D's or CTO~Z's read alone):**
- `grep` on `cli.py`/`platinum_cli.py` for any reference to `comp_marker_read`/`marker_read`: zero hits —
  confirms the "never wired in" claim.
- `git log -1` on `42b7f3c48a`: verbatim matches the quoted deferral text and numbers exactly.
- `git log --all --grep` for "marker_read"/"marker-head" since: several unrelated hits (COMPILERKIT
  threading `marker_head` into an `emit()` signature, judge verdicts, etc.), **none resolve the cli.py/
  platinum_cli.py re-point deferral itself** — corroborates ~D's disclosed search limits.
- Fixture (`org/tier1_exec/3.0.0_SA_CVO/NFRA_GRAPHUNI_P0-CVO_fixture/`): confirmed exists, dated
  2026-06-30 as claimed. Read `FIXTURE_ATTESTATION.md` directly — it already specifies a deterministic
  re-assert recipe (`repro_1_select_sample.py` + `repro_2_capture_layer_a.py`, SHA-equality vs
  `fixture_layer_a.tool_answers.json`) with a binding id-namespace-canonicalization precondition (CTO RULE
  (i) 220713Z).

**Ruling:** fresh coverage-parity re-measurement is the immediate next step, using the EXISTING fixture
recipe (not a new adapter) — matches both ~D's recommendation and CTO~Z's lean, now grounded rather than
just endorsed. Dispatched to `~D` (standing by) with the exact method, the binding canonicalization
precondition spelled out, and a specific ask to re-derive the sharpest test case
(`gold:D_01.partner_analytics`, blast radius 39, month-old 13-vs-216 result) fresh. Held the final
3-option architectural decision (re-populate at build_graph fidelity / re-run build_graph pinned to marker
head / re-baseline the fixture) pending that measurement — not deciding on stale numbers.

## 3 · Capacity heads-up: scaling to 6 parallel producers

CTO~Z flagged verification load about to 5-6x (5 new lanes spawning alongside `~D`). Agreed a triage:
full independent re-derivation stays on (a) every declared-vs-observed MISMATCH, (b) anything about to
justify a commit or redirect another lane's work (both items above are this class), (c) denominator/count
claims specifically (two of my own truncated-read near-misses today alone — counts get full re-derivation
even inside an otherwise-clean MATCH). Straight MATCHes with no downstream action: spot-check ~1-in-3 to
1-in-4 per lane. Will flag if volume makes even that unsustainable rather than silently drop coverage.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `git log`/`git show` (9a70418a7b, 42b7f3c48a) | PASS | independent verbatim confirmation of both cited commits |
| `grain_sentinel.py`/`grain_baseline.json` (grep + direct read) | PASS | mechanism + certified-date independently confirmed |
| `python3 infra/aws/globgrph/derive_stitch.py` | PASS — live mutant re-run post-fix | 5 violations not 6, EXTERNAL_ENDPOINT gone |
| `grep` (cli.py/platinum_cli.py for comp_marker_read) | PASS | zero call sites confirmed independently |
| `git log --all --grep` (marker_read/marker-head) | PASS | independently corroborates no resolving commit exists |
| `Read` (FIXTURE_ATTESTATION.md) | PASS | sourced the existing re-assert recipe rather than inventing a new measurement method |
