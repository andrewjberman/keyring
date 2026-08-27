# POSN_TENANCY — STAGE-3 DECOMP CERTIFICATION

**Certifier:** `3.0.0_SA_CVO~Z` · **2026-08-27 ~20:2xZ**
**Certified object:** `workflows/atom_decomposition/runs/posn-tenancy/20260827T200734Z/DECOMP.md` @`07de844b12`
**Author:** `2.0.0_SA_COO~Z` · **Project:** `POSN_TENANCY` @`4bbfda8ff8` · **PRD** @`a7ba82d253`

## VERDICT: **CERTIFIED WITH FINDINGS (5).** No cell invalidated. No TO blocked.

The artifact is sound. Every cell is scoped, carries a named oracle and a lane, and is born UNMEASURED.
The four-postulate record is present with an **honestly open CE**, the reduced cohort is disclosed, and
§5 states what the author is **not** asserting. Three of the five findings below were **named by the
author as their own most-likely errors** — one is upheld, one is confirmed and sharpened, one is where
they were right to be worried.

---

## 1. VINTAGE GUARD, AND THE HALF-LIFE THE AUTHOR FLAGGED

`07de844b12` (2026-08-27T16:09:17-04:00, `2.0.0_SA_COO~Z`). **WORKTREE == PIN for this file** — the
certified object did not move under me. `2.0.0_SA_COO~Z` held the artifact still while it was under
certification (msg 9910: *"a moving artifact is the thing a certifier cannot certify"*), which is what
made a pinned certification possible at all.

**THEIR CHECK-HARD #1 — "re-derive the bucket state at YOUR seat; do not accept mine." DONE, live API,
my own instrument, with a negative control:**

```
  EXISTS  opal-data-49financial      <- confirms theirs
  ABSENT  opal-data-inflection       <- confirms theirs
  ABSENT  opal-data-cottonwood       <- confirms theirs
  EXISTS  opal-data-bd / -cot / -inf <- MY ADDITION: all three still live
  EXISTS  opal-data-assets
  ABSENT  opal-data-qqq-no-such-bucket-4417   (negative control passes)
```

**The extension matters and it is not a quibble.** Both name-sets are live **simultaneously**. The
transitional shape the author flagged in `R-pt1(i)` as *"open by measurement"* is not a future
condition to plan for — **it is today's condition**, and Finding 4 shows it already has a hole in it.

---

## 2. THE OTHER TWO CHECK-HARDS, ANSWERED

**#2 — `R-pt1`'s open CE. THE AUTHOR'S CALL IS UPHELD.** They asked whether *"some firms migrated,
some not"* must be a **VALUE** rather than a disclosure. **It must not**, and postulate (iv) is the
discriminator: a value earns its place by having a remedy that does not move the others. The
transitional state's only remedy is **completing the migration** — which is precisely moving members
from value 1 to value 2. **A state whose sole remedy is the transition between two values is the
interval, not a third value.** Disclosing it was correct. *But see Finding 3: being right about the
axis left the interval with no criterion.*

**#3 — "if any criterion I wrote can be satisfied by a rendering check, it is broken." IT CAN. SEE
FINDING 2.** They were right to be worried, and right about which invariant would be the one to trip on.

---

## 3. FINDINGS

### F1 — §4's ARITHMETIC DOES NOT CLOSE, AND ITS OWN PARTITION IS NOT MECE *(clerical)*

§4 reads **"Cells: 16 — (a) 3 · (b) 3 · (c) 2 · (d) 3 · (e) 2 · (inv) 6 → 13 criterion-bearing + 3
that are decisions."** Mechanical census at the pin: **19 unique `PT-` ids** (a3 b3 c2 d3 e2 = 13, plus
inv 6). The enumeration sums to **19**, not 16; **13** is the (a)–(e) subtotal wearing the
"criterion-bearing" label; and the 3 named decisions (`PT-c-1`, `PT-e-2`, `PT-b-2`) are all **inside**
(a)–(e).

⛔ **AND THE PARTITION ITSELF FAILS POSTULATE (i) — over the decomp's own declared set.** `PT-b-2` is
listed as a decision *"(PT-b-2's shape selection)"* while also carrying an exercisable criterion
(*"each shape's deny arm EXERCISED"*). **It is in both classes**, so {criterion-bearing, decisions} is
not MECE and no single reading of "16" can be recovered. This is Rule 24 applied to the decomp's own
denominator section — the same postulate it applies correctly to `R-pt1` two sections earlier.

>> **WHY A CLERICAL FINDING IS WORTH A ROW: the wrong number for "cells" is very close to a right
   number for "criterion-bearing."** A downstream reader counting criterion-bearing items lands near 16,
   **agrees with the stated total, and never looks again.** A denominator that is wrong for its label
   and right for a neighbouring question is the hardest kind to catch. <<

**REMEDY (one line, in the same commit as the first TO, per §4's own instruction):** state the total as
**19**, and split the classes so nothing is in both — `PT-b-2` is criterion-bearing **and contains** a
decision.

### F2 — `PT-d-1`'s ORACLE IS WRITTEN IN THE EXACT VOCABULARY `PT-inv-1` FORBIDS

They asked for this one. It is `PT-d-1`:

```
PT-d-1  oracle:  "each firm renders; denominator printed"
PT-inv-1        "Discrimination is proven by what a firm can FETCH, never by what its UI shows.
                 A green render is NOT evidence."
```

**`PT-d-1` is not wrong to care about rendering** — its subject is *"or the other three LOSE THE
PAGE"*, and for **availability** a render genuinely is the thing. **The defect is that one oracle is
carrying two claims.** *"Each firm renders"* discharges availability and says **nothing** about whether
that firm received **its own** bytes — and a page rendering firm B's data renders perfectly.

**REMEDY:** `PT-d-1` needs **both arms named**: the page renders (availability) **AND** the bytes it
rendered are that firm's (discrimination, per `PT-inv-1`). As written, the first arm alone reads as
discharge.

**Same shape, weaker, `PT-c-2`:** *"a missing key and an empty artifact must be distinguishable **at
the consumer**."* "At the consumer" admits a client-side reading. Per `PT-inv-1` this belongs in the
**response** — a 404 and a 200-with-empty-artifact are distinguishable **on the wire**, which is where
the criterion should sit.

### F3 — THE INTERVAL HAS NO CRITERION *(the substantive one)*

`PT-b-2` requires isolation **SPECIFIED for both shapes**. Measured §1: **both shapes are live at the
same time, right now.** Specification is not simultaneity — **no cell requires that both mechanisms be
correct AT ONCE during the migration**, which is the only state the estate is actually in today.

`R-pt1` is right that the interval is not a value on the isolation-shape axis. **But a design authored
against two end-states, in an estate that is in neither, has no cell that owns the state it is in.**
`PT-e-1` covers *"no firm loses the page mid-flight"* — availability during the interval. **Nothing
covers ISOLATION during the interval.** Finding 4 is that gap, already open, measured.

**REMEDY:** either extend `PT-b-2` to require both mechanisms simultaneously live and exercised while
both name-sets exist, or add a cell that owns it. **A decomp input, not a defect in the axis.**

### F4 — ⛔ `PT-inv-6` IS CONFIRMED, AND MY OWN `POSN_TENANCY-S1` WAS TOO STRONG. CORRECTING MINE.

`CLAUDE.md:133` names **two** mechanisms: *"commit-gated **+** IAM Deny."* I filed S1 saying *"either
way the rule stops binding."* **Measured, that is overstated — and what is actually true is worse in
one limb and better in the other:**

| limb | state | evidence |
|---|---|---|
| **IAM Deny** | **SURVIVES the rename** | `infra/aws/terraform/shared-infra/s3-49financial.tf:50-56` @`07de844b12` — the resource policy on `opal-data-49financial` **deliberately catches cot-\* and inf-\* principals** and exempts bd-\* because *"opal-data-49financial IS the bd/49F firm's client bucket"* |
| **Commit gate** | ⛔ **STALE — hole open today** | `.tools/ds-precommit-check.py:61` — `_CROSS_FIRM_FOREIGN_BUCKETS`, **read via AST, not searched**: `data/cot/` bans `('opal-data-bd','opal-data-inf')`; `data/black_diamond/` bans `('opal-data-cot',)`. **Union of banned literals = 3. `49financial` in any ban tuple: False.** |

**So a script under `data/cot/` that references `opal-data-49financial` — the bd firm's client bucket,
which EXISTS — is not caught by the cross-firm commit gate.** Defense-in-depth went from two layers to
one, **silently, with nothing edited and nothing failing.** The surviving layer is the stronger one,
which is why this is a finding and not a fire.

⭐ **AND THE DIVERGENCE IS VISIBLE IN-TREE, WHICH IS WHAT MAKES IT A CLASS AND NOT A TYPO.**
`.tools/comp-secrets:58` carries `49financial` **inside its `bd` firm pattern**. **Two carriers of one
firm-to-token map, in the same directory: one was updated at the rename, the other was not.** Nothing
compares them.

⛔ **AND THE IRONY IS THE POINT, NOT A FLOURISH: the stale artifact IS A FIRM ENUMERATION MISSING A
FIRM** — the exact `MDPF_3FIRMS` defect class `1.0.0_SA_CTO~Z` cited in 9896, sitting inside the gate
that exists to catch cross-firm errors.

**BOUNDS — what I did NOT do.** I **read the ban list**; I did **not exercise the gate.** I am not
claiming a commit has passed through this hole — only that the enumeration lacks the token. Exercising
it means authoring a `data/cot/` file referencing `49financial` and committing it, on a gate every
seat's every commit runs through, mid-certification. **I am not doing that; I am naming it as the
unrun rung.** Per Rule 22a this claim sits at **APPLIED, not EXERCISED**, and I use neither "proof"
nor "root cause".

**INSTRUMENT NOTE, against myself.** My first pass at this was a **rail-nudged raw grep**. Andrew-direct
at `1.0.0_SA_CTO~Z`'s terminal (~20:1xZ, relayed in 9915): *"You should not be grepping, you should be
using comp-find."* I re-derived with `comp-find -i opal-data-49financial --files --all` (**182 files**;
the only `.tools/` member is `safe_deploy_core.py`, not the gate). **I am applying Rule 21 because it is
standing law that binds me, NOT widening a word he spoke to another seat.** The core claim rests on the
**AST read of the value set**, not on any sweep — banked: *a token census cannot see a value set.*

### F5 — `PT-inv-7` IS ADOPTED AS A **REQUIRED** CELL, NOT AN OPTIONAL ONE

`2.0.0_SA_COO~Z` routed it as certification input with *"fold it in or reject it; the call is yours."*
**Folded in, and required.** `1.0.0_SA_CTO~Z` (9896/9915) measured that the Rule 14 gate dispatches on
`.py`/`.sh`/`.tf`/`org/projects/*.json` only, **prints `OK: pre-commit gate clean for 0 file(s)` and
returns rc=0** on frontend artifacts — and this project's firm enumerations live in `.ts` and `.mjs`.
Two seats then measured **their own** sessions inside it (`0.4.0_DE_ClientPlatform~Y`: 10 commits, 24
files, zero checked; `2.0.0_SA_COO~Z`: 6 commits, all zero, *"I read every one as a pass"*).

⛔ **BINDING ON EVERY POSN_TENANCY CRITERION:** no criterion may be discharged by *"the commit gate
passed"* where the artifact is `.ts`/`.tsx`/`.mjs`/`.js`. On those suffixes the gate is **not an
instrument**. **I extend it by one clause on the strength of F4:** nor by *"the cross-firm gate
passed"* for any **newly-named** bucket. **Same class, one layer apart** — an enumeration-driven guard
is blind to whatever its enumeration omits, whether the omission is a **language** or a **name**.

>> `2.0.0_SA_COO~Z`'s formulation is adopted verbatim and it corrects a rule I have applied all
   session: **A DENOMINATOR PRINTED BUT NOT READ IS EXACTLY AS USELESS AS ONE NOT PRINTED.** I have
   been treating *print the denominator* as the remedy. Here it was printed, on screen, sixteen times
   across two seats who hunt this exact shape, and changed nothing. **The remedy is formatting a
   zero-denominator result so it cannot read as a pass.** <<

---

## 4. WHAT I DID NOT MEASURE

- **I did not exercise any cell.** Every cell is UNMEASURED by design; certification is of the
  **decomp**, not of the world it describes.
- **I did not re-derive `ADVI_FIRMSEP`'s state.** §5 already declines to rest on it; I inherit that
  bound rather than resolving it.
- **I did not verify the IAM Deny is APPLIED in the account.** I read the Terraform — **DESIRED state.
  `.tf` is a declaration, not an apply.** F4's IAM row is therefore **DESIRED, not APPLIED**, and I say
  so rather than letting the table imply otherwise. *This is the same plane error the S1 certifier's
  note names — a code literal is not infrastructure state — and it applies to me here.*
- **I did not count firm enumerations missing a firm today.** `1.0.0_SA_CTO~Z` declined that by
  inference from the 07-22 census and was right to; it needs a real instrument and it is decomp work.

## 5. STANDING CRITERIA FOR ROUND 1, STATED NOW SO THEY COST NOTHING TO MEET

1. **`modesFor`'s four-postulate record must be RE-AUTHORED against an ACCESS domain, not re-cited.**
   The existing record is scoped to a **PRESENTATION** domain. A record still declaring "present" would
   **pass its own test and answer the wrong question.**
2. **§4's denominator is amended in the same commit as the first TO** (F1) — §4's own instruction.
3. **No criterion discharged by a gate blind to the artifact's language or name** (F5).
4. **No cell's oracle may resolve a bucket, prefix, or firm location from SOURCE TEXT** — live API
   only. Carried from `POSN_TENANCY-S1`.

**Author did not certify their own work.** Reduced cohort disclosed by the author; certifier is this
seat, alternate `1.0.0_SA_CTO~Z`.
