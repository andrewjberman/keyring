# CERTIFICATION — `MDPF_COTREMEDIATION` STAGE-3 ATOM DECOMP v1 (D8)

**Certifier:** `3.0.0_SA_CVO~Z` · 2026-08-27 ~18:4xZ
**Instance (certified object):** `workflows/atom_decomposition/runs/mdpf-cotremediation/20260827T162936Z/DECOMP.md`
@`69cb3eb580` (author `2.0.0_SA_COO~Z`), read at `origin/SITEZ`
**Cert commit:** resolve with `git log --diff-filter=A -- <this file>`
⛔ **The hash on a certification's face names the object certified, never the certificate.**

---

## VERDICT: **CERTIFIED WITH FINDINGS.** Two findings, neither blocking. No TO-mint block.

---

## 1. VINTAGE GUARD

```
69cb3eb580                         ANCESTOR of origin/SITEZ      (the artifact)
6dcd789490                         ANCESTOR of origin/SITEZ      (the round-1 sibling)
origin/CLOUD head                  NOT ancestor   <== THE CONTROL
git diff origin/SITEZ -- <run dir> EMPTY          (tree copies identical to remote)
```

## 2. MECHANICAL CENSUS

Word-boundary, case-insensitive id census over the file bytes, counting DISTINCT ids:

| section | a | b | c | d | e | inv | **total** |
|---|---|---|---|---|---|---|---|
| `COT-*` | 5 | 3 | 2 | 3 | 1 | 4 | **18** |

**14 cells + 4 invariants = 18 distinct ids** (33 raw occurrences). The decomp states no numeric
denominator on its own face — see F2.

## 3. THE LOAD-BEARING CLAIM, VERIFIED AT THREE INDEPENDENT POINTS

§4a.3 is the highest-stakes passage: it asserts the AC7 negative fixture survives only as a
noncurrent S3 version on a 14-day lease. **Verified, not accepted:**

```
CONTENT   fixtures/cottonwood_..._FROZEN_2026-08-19.json  ->  as_of_last=2026-08-19 · 458 dates · 0 nulls
S3        version fZkuD1PfuPSSUhw07IznTFKJvLiT8IoD        ->  2026-08-25T13:50:50Z · 115,177 B · IsLatest=False
LIFECYCLE get-bucket-lifecycle-configuration              ->  expire-noncurrent-versions-14d · Enabled · 14 · Prefix ""
```

**Every figure in §4a.3 reproduces exactly**, including the byte count. The lease claim is real and
the whole-bucket scope (`Filter.Prefix = ""`) is confirmed.

⭐ **AND THE DECOMP'S BEST PASSAGE IS THE ONE WHERE IT REFUSES ITS OWN MOST ATTRACTIVE FINDING.**
§4a.2 brackets the freeze onset to a 24-hour window and observes the suspected commit falls inside
it — then immediately applies its own `COT-inv-3`: *"ANY change landing in that 24-hour window
produces exactly this boundary. The version history NARROWS the search; it does not single out that
commit."* **It converts a would-be root cause into a reusable refutation filter instead.** That is
the reserved-word discipline (`COT-a-1`) applied by the author against the author.

---

## 4. FINDINGS

### F1 (P1) — **THE DECOMP'S ONE ARMED, DEADLINE-BEARING ITEM IS ALREADY DISARMED, AND THE ARTIFACT DOES NOT KNOW IT**

§4a.3 closes: *"**ARMED**, class BLOCKING-adjacent … **Not disarmed by me** … **DISARM BY:
2026-09-09.**"*

**Measured:**
```
decomp §4a written    69cb3eb580   2026-08-27T12:34:57-04:00
fixture CAPTURED      bc570d9e0d   2026-08-27T12:39:29-04:00   0.0.0_AB_MSTR~Z
                      -> 4 minutes 32 seconds later, INTO THIS DECOMP'S OWN RUN DIRECTORY
```

The durable fixture exists at
`…/20260827T162936Z/fixtures/cottonwood_aggregate-aua-timeseries_FROZEN_2026-08-19.json`, is
**byte-identical in size (115,177 B)** to the S3 version, and content-matches on all three declared
properties. ⛔ **The 14-day lease no longer bites: the bytes are in git.**

**Consequence:** a successor reads a LIVE 2026-09-09 deadline on an item that is closed, and may
re-capture a fixture sitting in the same directory — or, worse, treat the deadline's passing as a
lost specimen. ⚠ **This is the fourth instance of one class today** (`SAT-inv-2`, the 11 stale
`disarm_owner` rows, `Z-S23`, this): **a record keyed on a state that moved, with no gate firing.**

⭐ **NOT a defect in the reasoning — the opposite.** The decomp said the specimen needed capturing
before it expired, and **it was captured because the decomp said so, within five minutes.** The
finding is a carrier lag, not an error. **REMEDY:** amend §4a.3 to record the capture path and
`bc570d9e0d`, and move the item to disarmed. **Owner: `2.0.0_SA_COO~Z`** (author; I do not edit
another seat's artifact).

### F2 (P2) — **TWO DECOMPS, ONE PROJECT, DISJOINT ID SPACES DIFFERING BY ONE CHARACTER**

```
round-1  20260825T161149Z   prefix COTR-   42 distinct ids (33 cells + 9 invariants)
stage-3  20260827T162936Z   prefix COT-    18 distinct ids (14 cells +  4 invariants)
cross-check: round-1 contains ZERO COT- ids; stage-3 contains ZERO COTR- ids. NO OVERLAP.
```

**Measured consequence, on me:** my first census of the stage-3 decomp used the `COTR-` pattern and
returned **0 ids** — reading as *"a stage-3 atom decomp with no cells at all."* Only a positive
control caught it. **A proof instance's `cell_refs` will resolve against one space and silently miss
the other**, and any "the project's cells" census returns 42 or 18 depending on which prefix is
typed, with both looking complete.

**REMEDY:** state the relationship on both faces — which id space is live, and whether `COTR-*` is
SUPERSEDED by `COT-*` or still binding alongside it. **This is a question, not a correction: I do
not know which is intended and am not guessing.**

---

## 5. WHAT THE DECOMP GETS RIGHT AND SHOULD NOT BE "IMPROVED"

- **§0 discharges NEVER#1 before writing a single cell** and then **refuses its own green reading as
  discharge**, quoting AC5's own prohibition. A decomp that closed on that measurement would have
  closed the one project whose reason for existing is that a green reading was wrong.
- **`COT-b-2` declares itself NOT DISCHARGEABLE by its author's own reading** — *"I measured both
  healthy TODAY, which is consistent with health AND with having been moved. The before-image is
  required and I do not hold one."* **Naming the cell most likely to be waved through is worth more
  than any cell that passes.**
- **`COT-d-3`** rules every `LastModified` / `s3 ls` / `comp-freshness` instrument **mechanically
  ineligible** for all seven ACs, because the objects were rewritten daily throughout the freeze —
  *"every mtime instrument was GREEN AND CORRECT ABOUT THE FILE."*
- **§3 authors no schema, deliberately**, naming that a cell enumerating conformance categories
  *"would have silently begun the census project on the repair's clock."* **The PARKED
  target-architecture constraint is held exactly as carried.**

## 6. WHAT I AM NOT ASSERTING

- ⛔ **THE ROUND-1 DECOMP (`20260825T161149Z`, 42 ids) IS *NOT* CERTIFIED BY THIS DOCUMENT.** I
  censused it and ran its vintage guard; I did not read its 412 lines against its PRD. **It remains
  SOLO AND UNCERTIFIED, and every TO cut from it still carries that caveat.** Named as owed rather
  than quietly folded in.
- **I did not re-run §4a's ten-version history table** — that is the author's instrument, and
  repeating it would be repetition rather than corroboration. I verified the fixture, the S3 version
  and the lifecycle rule instead, which are three different reads.
- **No claim about the upstream BD feed partitions**, which the decomp itself scopes out.

— `3.0.0_SA_CVO~Z`
