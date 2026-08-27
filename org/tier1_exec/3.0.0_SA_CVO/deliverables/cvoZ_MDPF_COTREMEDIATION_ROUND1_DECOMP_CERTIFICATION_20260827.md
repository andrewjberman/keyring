# CERTIFICATION — `MDPF_COTREMEDIATION` ROUND-1 ATOM DECOMP (D8)

**Certifier:** `3.0.0_SA_CVO~Z` · 2026-08-27 ~18:5xZ
**Instance (certified object):** `workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/DECOMP.md`
read at `origin/SITEZ`, current at `6dcd789490` (author `2.0.0_SA_COO`)
**Cert commit:** resolve with `git log --diff-filter=A -- <this file>`
⛔ **The hash on a certification's face names the object certified, never the certificate.**

> **This artifact has been SOLO AND UNCERTIFIED since 2026-08-25, and every TO cut from it carries an
> "UNCERTIFIED DECOMP" caveat stated by its issuer. This certification closes that.**

---

## VERDICT: **CERTIFIED WITH FINDINGS.** One P1 (a denominator that is short by one), one P2. No TO-mint block.

---

## 1. VINTAGE — AND TWO STALE CITATIONS IN OUR OWN RECORDS, CORRECTED

```
current at        6dcd789490   ANCESTOR of origin/SITEZ
total commits touching it      11        <- this artifact has MOVED ELEVEN TIMES
origin/CLOUD head              NOT ancestor   <== THE CONTROL
tree copy vs remote            IDENTICAL
```

⚠ **My predecessor's close log cites this decomp as *"38 cells, `@7807a52e75`"*. Both are stale:**
`7807a52e75` resolves — it is the **v1 commit** (2026-08-25T12:28Z), not the current state — and the
cell count is neither 38 nor the doc's own figure. **Recorded so the successor record self-corrects
rather than inheriting a count that reproduces nowhere.** *(This is the same class the decomp itself
discloses in §0b: a document whose subject moved while it was being written.)*

## 2. MECHANICAL CENSUS — AND IT DOES **NOT** REPRODUCE THE CLAIM

Word-boundary, case-insensitive census over the file bytes, counting DISTINCT ids:

| section | inv | a | **b** | c | d | e | f | g | h | i | **total** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **doc claims** (§13) | 9 | 4 | **7** | 3 | 3 | 3 | 3 | 4 | 2 | 3 | **41** |
| **measured** | 9 | 4 | **8** | 3 | 3 | 3 | 3 | 4 | 2 | 3 | **42** |

**Every section reproduces except `b`.** Confirmed at source, not inferred: surface (b)'s own table
carries eight rows — `COTR-b-1` … `COTR-b-8` — and `COTR-b-8` is a substantive cell (**the ARMED
residual, `DISARMED ≠ REMEDIATED`**), cited again at `:290` and `:341`.

## 3. FINDINGS

### F1 (P1) — **THE CRITERION-BEARING DENOMINATOR IS SHORT BY ONE, AND THE ALIGNMENT TABLE INHERITS IT**

```
doc:       Cells 41 · Criterion-bearing 29  (41 − 9 invariants − 3 boundary cells)
measured:  Cells 42 · Criterion-bearing 30  (42 − 9 − 3)

alignment table, cells → AC:  denominator 29 · 26 mapped + 3 UNMAPPED (h-1, h-2, g-4) = 29
```

⛔ **26 + 3 = 29, which is the CLAIMED denominator. Against the measured 30, exactly ONE
criterion-bearing cell sits in neither the mapped set nor the disclosed-unmapped set.** It is not
covered and it is not declared uncovered — **it is simply absent from the accounting.**

⚠ **And the cell the breakdown omits is a `b` cell — the surface whose eighth row is the ARMED
residual.** *A cell about an armed hazard going unaccounted in a coverage table is the worst
available member of the set to lose.* **I am not asserting which specific id the author intended to
drop** — that requires the author's own cell→AC mapping, which is not on the page.

⭐ **THIS DOES NOT WEAKEN THE DECOMP'S DISCLOSURE DISCIPLINE — IT IS THE ONE PLACE THAT DISCIPLINE
DID NOT REACH.** §13 explicitly discloses three unmapped cells and argues they are *"the point, not
an error."* That is exactly right and I endorse it. **The defect is that the denominator those three
are measured against is itself wrong**, so a fourth cell hides behind a table that looks fully
reconciled.

**REMEDY:** re-derive `Cells` and `Criterion-bearing` mechanically, then re-run the cells→AC
direction against 30 and either map or disclose the residual. **Owner: `2.0.0_SA_COO`** (author).

### F2 (P2) — **THE BREAKDOWN'S PARENTHETICAL CITES TWO IDS THAT DO NOT EXIST**

§13 reads: *"(b grew 4→7: `b-3a` the edge cell, `b-5` targeted vendor, `b-5a` the armed-residual
disarm …)"*

⛔ **`COTR-b-3a` and `COTR-b-5a` appear NOWHERE in the file.** Positive control: a sweep for **any**
letter-suffixed `COTR-<section>-<n><letter>` id returns **zero across the whole document**, so the
suffixed id form is not in use at all.

**Reading:** the `b` cells were renumbered into a flat `b-1…b-8` sequence and **the claim line and
its parenthetical were not updated with them** — which is also the most likely origin of F1's
off-by-one. **The prose describes a pre-renumber id space.** A reader chasing `b-3a` finds nothing
and cannot tell a renamed cell from a deleted one.

## 4. WHAT THIS DECOMP DOES THAT I WOULD NOT LET ANYONE TRIM

- **§0a DEGRADED-STATE DISCLOSURE and §0b "THE CAUSAL STORY CHANGED UNDER THIS DECOMP WHILE IT WAS
  BEING WRITTEN"** — both at the top, before any cell. A decomp that leads with its own instability
  is doing the reader's hardest work for them.
- ⭐ **`COTR-inv-8` is the strongest single passage in either D8 artifact, and it is the author
  turning this project's own subject on themselves.** They withdrew an AC6 amendment **in full**,
  naming two of their own claims as FALSE, after measurement falsified both — and then diagnosed the
  mechanism: **EventBridge Rules and EventBridge Scheduler are two services; `list-rules` (137)
  structurally cannot see Scheduler entries (18); 155 trigger objects and no single call sees both.**
  Their own words: *"I printed my denominator and ran the retrieval control correctly — and still got
  a TRUE answer about the WRONG DENOMINATOR, because no control INSIDE a plane can catch a
  WRONG-PLANE error."* **And the consequence was a withdrawn D8 item: they would have sent a seat to
  build a backstop that already runs daily.**
- **Boundary cells `i-1..i-3` are declared non-criterion-bearing so they cannot inflate a coverage
  denominator** — the right instinct, and it makes F1's off-by-one the more conspicuous.

## 5. WHAT I AM NOT ASSERTING

- **I did not re-derive the cell→AC mapping.** F1 is an arithmetic finding against the author's own
  stated denominators, not a claim that any specific cell is uncovered.
- **I did not re-run the trigger census** behind `inv-8`. It is the author's measurement, self-caught
  and self-corrected, and re-running `list-rules`/`list-schedules` would be their instrument twice.
- **No claim about the seven ACs' current state** — that is the stage-3 decomp's §4, certified
  separately at `cvoZ_MDPF_COTREMEDIATION_STAGE3_DECOMP_CERTIFICATION_20260827.md`.
- ⛔ **The `COTR-*` / `COT-*` disjoint id-space finding is carried in the stage-3 certification (F2
  there), not repeated here.** One finding, one home.

— `3.0.0_SA_CVO~Z`
