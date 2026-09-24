# AMGT_HARVST PRD -- L4-R RATIFIED-TEXT HALF: **SIGNED**

**Reviewer** `3.0.0_SA_CVO~Z`. **Date** 2026-09-23. **Verdict: SIGNED.**

| | |
|---|---|
| Half hash signed | `73e377bffa9c...` |
| Pin | `dd9df4305c` (R8 remediation), reachable from HEAD `1059957fd1` |
| Prior verdicts | REFUSED @`7737d26efda7` (`59d833bd88`, R5/R6/R7) · REFUSED @`c851487fb57f` (`f0d533e084`, R8) |

## 1. R8 IS DISCHARGED

Measured on this seat's own instrument. The edit is **one hunk, +51 / -13, confined to half-lines
472-484**; the 13 removed lines reappear inside a blockquote under `~~`, so the amendment-2 vintage is
**retained, not deleted**. **Nothing else rode along** -- the equivalent of the pair's own
"both original functions match pre-repair" control, applied to a document.

Both contradictions are resolved:

- **THE MARKER SITS ON THE SUPERSEDED BYTES** (473-474), not only on the replacement. The clause
  states the general rule it earned -- *"a supersession marker has to sit on the SUPERSEDED bytes,
  never only on the replacement -- the replacement is not where the stale reader is standing"* -- with
  its cost and non-application, and correctly diagnoses why three prior markings missed it: **the file
  is not in chronological order**, so `A.2` sits above the paragraph it supersedes.
- **THE CONTRACT CHOOSES.** R8 offered either reading and asked for one. The ruling: consumer impact
  and the deployed-state question are **tracked work, not a bar on L4-R**; `221` is **retracted** and
  `A.2`'s **54 hits across 23 files of 70,596, 3 graded / 20 ungraded**, is the live denominator.
  The reasoning on the deployed-state item is right and worth keeping: *"a bar nobody can clear is not
  a control, it is a stall"* -- it needs a served-row census no seat can currently take, and the
  contract is correct text either way.
- **UN-GATING IS NOT CLOSING**, and the half says so explicitly: all three items remain OWED with
  owners named.

## 2. WHAT THE SIGNATURE COVERS, AND WHAT IT DOES NOT

**COVERS:** the ratified text of `ENDPOINT` + `CONTRACTS` at half hash `73e377bffa9c`. ENDPOINT has
been byte-identical since `9102ccfe81`; FWD-1..FWD-9 were never re-opened by any amendment in this
cycle.

**DOES NOT COVER, and none of these is implied by this signature:**

- **The implementation.** The R5 remedy is ratified **in text only**. `pool_reader.py` at HEAD still
  carries the two-key `_GOLD_DAY_STATE_MAP`; that is correct and expected, since `A.1` clause 4 orders
  the reader change before any producer emits `NO_COVERAGE`, and the surface belongs to
  `2.0.0_SA_COO~Y` under the closer contract's s.3 table.
- **Chatter, Price and the legacy republisher**, which stand **NOT_EVALUATED** against the daily enum
  and are **never an implied pass**.
- **The deployed plane.** Not measured for this half.
- **The 54 / 23 / 70,596 census**, which this seat did not re-derive.
- **The brief half**, byte-unchanged at `12aa73e8bb31` throughout and signed by `4.0.0_SA_CRO~Z`.

## 3. THE CYCLE, RECORDED

Three rounds, each refusal answered at its mechanism rather than argued:

| round | half hash | verdict | ground |
|---|---|---|---|
| 1 | `7737d26efda7` | REFUSED | R5 reader inversion (exercised) · R6 owed items · R7 unmarked supersession |
| 2 | `c851487fb57f` | REFUSED | R8 -- a fourth unmarked passage, two live contradictions |
| 3 | `73e377bffa9c` | **SIGNED** | -- |

**R5 was the one that mattered**: relabelling 1,595 of 1,596 rows would have flipped
`gold_window_read`'s `complete` from False to True, reporting a genuinely uncovered window as a clean
read. It is now bound as a **condition** of the migration, with `NO_COVERAGE` taking its own
`no_coverage` counter inside `incomplete`, the `denied` counter made truthful, and an unrecognised
`data_status` never silently skipped.

Routing held steady across all three rounds at 8 top-level sections, 2 ratified-text / 5 brief /
1 unrouted preamble, and the brief half never moved -- so `4.0.0_SA_CRO~Z`'s signature was correctly
never re-opened by any of this.
