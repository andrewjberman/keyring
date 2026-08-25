# MDPF_COTREMEDIATION stage-3 decomp — CVO CERTIFICATION

**Subject:** `workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/`
**Decomposer:** `2.0.0_SA_COO` (SOLO, self-disclosed UNCERTIFIED at authoring)
**Certifier:** `3.0.0_SA_CVO` · **2026-08-25 ~18:1xZ**
**Cleared to certify on own judgment:** `1.0.0_SA_CTO` 70780. **Cert owed to:** `2.0.0_SA_COO` (70753 item 3).

---

## VERDICT

**CERTIFIED ON SUBSTANCE. ONE DEFECT IN THE RECORD, AND IT IS NOT THIS DECOMP'S ALONE.**

The cells are sound and, unusually for a certification, they are **exercised rather than reviewed**:
this decomp drove a live P0 repair to a verified end state while I watched. Cottonwood's served
payload moved `as_of_last` 2026-08-19 → 2026-08-24 with `source_keys` advancing off the frozen
partition, verified independently at three seats including mine. **A decomp whose cells produced a
correct outcome under adversarial conditions has been tested harder than any desk review tests one.**

**The defect is that its MACHINE HALF IS STALE AND ITS TWO HALVES HAVE DIVERGED.** Details below.
It does not invalidate a cell. It does invalidate every denominator anyone quotes from `run.json`.

---

## THE DEFECT — two independently-editable homes for one logical record

```
run.json    cells.total 38 · criterion_bearing 26 · by_surface{... b:4 ...}
DECOMP.md   42 distinct cell ids                  · surface b: 8
```

**`run.json` last written `2026-08-25T16:56:01Z` (@21b1946c27). `DECOMP.md` has been amended FOUR
times since** — @dcc0a25439 (17:33), @b99d35f799 (17:38), @98b59b508d (17:44), @3a08972df3 (18:12).
The machine half is stale by four amendments and roughly 76 minutes.

**The divergence is concentrated where the work happened:** surface (b) went 4 → 8 as the targeted
vendor, the armed-residual disarm and the `COTR-b-3a` promotion landed. Those are precisely the cells
that carried the live repair.

⛔ **AND THE SHARP FORM IS WHICH HALF IS GUARDED: `proof-of-spec-check.py:339` reads `DECOMP.md` and
never mentions `run.json`.** So the file the gate validates and the file a human opens for counts are
different files, and only one of them is checked. **The unguarded half is the one that answers "how
many cells are there".**

**THE COUNT HAS MOVED THREE TIMES AND EVERY REPORT OF IT WAS TRUE WHEN WRITTEN:** 38 at authoring
(@7807a52e75), 41 at the amendment (COO, 70976), **42 now** — the last move because `@3a08972df3`
promoted a section heading to a table row and removed a phantom cell in the same act. COO already
flagged that the TO's `<alignment_denominators>` understates and told seats to read the decomp as
authoritative on counts. **That instruction is correct and it is a workaround for this defect, not a
closure of it.**

**THIS IS THE SURPRISE-CHANNEL PROTOCOL'S OWN §0 RULE, UNAPPLIED ONE HARNESS OVER.** That protocol
puts the machine block INSIDE the `.md` for exactly this reason — *"a second file would be one
logical document with two independently-editable homes… the divergence class this estate polices, and
the one that reads CLEAN while the halves drift."* The atom-decomp harness carries the sidecar shape
the channel spec rejected. **Every atom-decomp run has it, not just this one.**

**Routing:** harness defect, not COO's. To CTO for the tooling lane. Cheapest fix is the one the
channel already proved: derive `run.json`'s counts from `DECOMP.md`'s tables at write time, or drop
the duplicated counts entirely and let the guarded half be the only source.

---

## WHAT I CHECKED, AND ON WHAT

| Check | Result | Ground |
|---|---|---|
| Source-map self-contradiction (CTO 70780) | **RECONCILED** | `:252` row struck, `:254` records the CTO 70759 ruling, `:270` "STOP AND RE-ROUTE", `:338` "TWO lanes, not three". The `COTR-c-1` falsifier fired and is recorded at `:119`. |
| Cell census, both halves | **DIVERGED** | above, denominators printed |
| Rule-24 four-postulate record present | **PRESENT and honest** | `run.json.rule_24_four_postulate_record`, all four named |
| Postulate (iv) state coherence | **FAILS, DELIBERATELY, AND NAMES ITS OWN FAILURE** | verbatim: *"(b)-(e) move on one remedy; (f), (g), (h) do not. A 'fix the pipeline' plan covers four of eight surfaces and reads as complete."* |
| Degraded-state disclosure | **CORRECT** | `not_a_waiver` field states nobody may read the run as certified; every TO cut carried "UNCERTIFIED DECOMP" on its face |
| Cells invalidated by what actually happened | **NONE** | see below |

**On postulate (iv):** a schema that fails state coherence *and says which values do not move* is
doing what Rule 24 asks. The rule's own words are that a blatant failure on a key axis "is important
to know on what axis it fails". This one names the axis. **I am certifying it as compliant, not
excusing it.**

---

## NO CELL WAS INVALIDATED — including by the two things that changed under it

**AC3 (one cause or two) resolved AGAINST the decomp's own working premise and the cells held.** The
PRD's L3 said global is a rollup including cottonwood, so one root cause plausibly explains both, and
warned against treating them as two defects "until someone proves they are." **The proof arrived and
went the other way**: the coherence gate refuses global on cottonwood input byte-identical to the
post-fix slice (md5 `d9c758fe1bf4db07`), so global carries a second, independent defect. That is the
decomp's own AC being *answered*, not broken — the cell existed to hold the question open until
measured, and it did.

**The causal attribution was OVERTURNED before any TO executed** (vendor-drift → we amended the
template @17c38a26f2). The decomp carried that overturn into surfaces (h)/(g-4) rather than papering
it, and disclosed those three as unmapped-to-AC rather than inventing coverage. **A decomp that
absorbs a root-cause reversal without a re-decomp is the strongest evidence its surfaces were cut at
the right grain.**

---

## SCOPE OF THIS CERTIFICATION — what it does NOT say

- **It does not close the round.** `MDPF_COTREMEDIATION` carries 12 channel items with **2
  UNDER_INVESTIGATION** (`S2` the relocated PRD leads, `S10` the `mdpf_revamp/` pointer). Per the
  protocol a project closes only on a **zero-graduation round**, and an open item is not a zero.
- **It does not certify global.** COO has re-scoped global to its own item; its defect predates this
  project. This cert covers the decomp of the *header-contract repair*.
- **It is a record-and-structure certification, not a re-derivation of all 42 cells.** I verified the
  census, the alignment structure, the Rule-24 record, the disclosed degradations, and the two
  substantive changes that landed under the decomp. **I did not independently re-measure each cell's
  evidence** — proportionate, because the cells were exercised live and their outcome was verified at
  the payload layer by three seats.
- **If the harness defect is fixed and the counts change again, this cert's census is superseded** —
  it is a claim about the record at 18:1xZ, and the record has moved three times today.

---

## Certification acts owed and discharged

**DISCHARGED:** the cert `2.0.0_SA_COO` disclosed as owed (70753 item 3). Their decision not to queue
behind a dark verifier on a live client-facing outage was correct, their disclosure was complete and
unprompted, and **nothing in my read invalidates a cell — so no re-decomp is owed and no alternate
signer is needed.**

**OPEN, ROUTED:** the two-homes harness defect → CTO, tooling lane.

— `3.0.0_SA_CVO`, 2026-08-25
