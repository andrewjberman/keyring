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

---

# AMENDMENT 1 — ~20:3xZ — THE `49f` / `49financial` ALIAS IS LIVE ON BOTH SIDES

**Verdict unchanged (CERTIFIED WITH FINDINGS).** This amends the substrate facts under F3 and
`PT-b-2`, and resolves a direct contradiction between two seats that arrived while the certification
was being written.

**THE CONTRADICTION.** `0.4.0_DS_ClientPlatform~Z` (9949): *"BOTH ARE LIVE — 285 vs 8,862 objects."*
`2.0.0_SA_COO~Z` (9951, downgrading their own earlier hazard): *"`49f/` IS A DEAD PROBE PREFIX —
ONLY `_ops/probe` objects. Nothing since 2026-07-14. SIX WEEKS COLD."*

**MEASURED AT THIS SEAT**, `opal-data-assets`, client-side counts, negative control passed:

```
blackdiamond/49f/           285 objects   _ops/ bronze/ gold/ meta/ silver/   NEWEST 2026-08-25T07:06:47Z
blackdiamond/49financial/  8862 objects   bronze/ bronze_legacy/ silver/ silver_legacy/
                                                                             NEWEST 2026-08-27T18:31:25Z
gold/ under 49f/  -> 1        gold/ under 49financial/ -> 0
control blackdiamond/49f/nonexistent-qqq4417/ -> 0
```

`0.4.0_DS_ClientPlatform~Z`'s figures reproduce **exactly** on a third instrument.

⛔ **THE DOWNGRADE IS A HEAD-OF-LISTING ARTIFACT, AND IT IS MECHANICAL.** The two probe files quoted
as proof of death are **keys #1 and #2 in lexicographic order** under that prefix — `_` is 0x5F and
sorts before `b`, `g`, `m`, `s`, so **`_ops/` is structurally first and a truncated read cannot
return anything else.** I ran the head-of-listing read and got the identical pair.

>> **THE PREFIX THAT LOOKS DEADEST FROM THE TOP OF THE LISTING IS THE ONE WHOSE LIVE TIERS SORT
   LAST.** An IAM condition on `49financial/` alone misses **285 objects refreshed two days ago**,
   including **the only `gold/` tier that exists on either side.** *(One object. The tier's size is
   not the point; its existence under the OTHER token is.)* <<

**THE TIER SPLIT, now measured rather than suggested:** `gold/` exists **only** under `49f/`;
`bronze_legacy/` and `silver_legacy/` exist **only** under `49financial/`. **The correct prefix
depends on which tier you are reading** (`0.4.0_DS_ClientPlatform~Z`'s formulation, confirmed here) —
so a condition keyed on either token is correct about one tier and silently wrong about another.

**BEARING ON THE DECOMP.** This is **F3 with a name**: the interval is not hypothetical, and the
alias is one of its concrete hazards. `2.0.0_SA_COO~Z`'s *surviving* `PT-b-2` defect is
**independent and untouched** — `smartx/` has no firm level at all, so a key-prefix condition has no
prefix to condition on. **The send-back list is three items, not two.**

**STILL OPEN, qualifier kept rather than spent:** that the two prefixes belong to the SAME FIRM.
Naming and the legacy suffixes suggest it; **no object was opened.**

⛔ **AND MY OWN INSTRUMENT FAILED IN THE SAME CLASS ONE MINUTE EARLIER.** My first `gold/` test
reported `49financial/gold/ -> 1`. It is **0**: `--output text` prints the literal `None` for an
empty result and my `grep -c .` counted it as a line. **A failed retrieval returned a VALUE, and the
value was a plausible small number.** I caught it only because the CommonPrefixes listing contradicted
it — *not* because the count looked wrong. **Same class as the artifact I am correcting: an instrument
answering a question I did not ask, in the vocabulary of the one I did.**

---

# AMENDMENT 2 — ~20:4xZ — THE RULING `2.0.0_SA_COO~Z` ASKED FOR

They routed two material inputs mid-certification (9919, 9926), declined to amend under
certification, and put the call here: *certify with these marked CORRECTED-IN-FLIGHT, or send back
for v1.3.* **Their recommendation was SEND BACK.** I measured both rather than adjudicating between
them, and they do not have the same answer.

## RULING — PARTIAL. The send-back is ADOPTED and SCOPED BY MEASUREMENT.

```
CERTIFIED WITH FINDINGS   18 of 19 cells + all 6 invariants
NOT CERTIFIED             PT-b-2  (the cell)  and  R-pt1  (the Rule 24 record)
```
**TOs may be cut against the certified cells. None may be cut against `PT-b-2`.**

### INPUT 1 — `PT-inv-7`'s 12× SCOPE ERROR: **NOT GROUNDS.** It is not in the certified object.

9919 says the understatement is *"IN THE ARTIFACT YOU ARE CERTIFYING."* **Measured at the pin:**

```
PT-inv- ids at 07de844b12:  PT-inv-1 2 3 4 5 6      'inv-7' occurrences: 0
positive control PT-inv-6:  found                    (so the reader is not the thing failing)
```

**`PT-inv-7` does not exist at `07de844b12`.** It was routed as certification *input* — `2.0.0_SA_COO~Z`'s
own 9910 says *"NOT an amendment."* And **F5 never cited the 2-file figure**: it rests on the dispatch
list, the extractor's own docstring, and the two seats' **first-party** session counts (10 commits/24
files; 6 commits), all of which stand. **A correction to a cell that is not in the artifact cannot
invalidate the artifact.**

⛔ **WHAT IT DOES BIND — and F5 already carries it, now with the denominator explicit:** when
`PT-inv-7` is authored into v1.3 it carries **~25**, not 2. **With `1.0.0_SA_CTO~Z`'s own bound kept
rather than spent:** 25 is frontend-language files containing **one** token (`cottonwood`); **firm
enumerations are a SUBSET of that**, other firms would add files this sweep did not ask for, and per
Rule 21 the denominator certifies **the sweep, not the pattern.**

### INPUT 2 — `PT-b-2` / `R-pt1`: **UPHELD, MEASURED, AND IT IS POSTULATE-LEVEL.**

`2.0.0_SA_COO~Z` said they were *"not asserting"* it, only that `PT-b-2` rests on an unchecked
premise. **I checked it.** `opal-data-assets`, CommonPrefixes at depth 1:

```
smartx/        account/  allocation/  model/  platform/     <- NO FIRM LEVEL
blackdiamond/  49f/  49financial/  cottonwood/              <- FIRM LEVEL
eclipse/       inflection/                                  <- FIRM LEVEL
orion/         inflection/                                  <- FIRM LEVEL
```

**Andrew's map puts 49 Financial's Models AND SMAs on SmartX.** `PT-b-2` specifies shared-substrate
isolation as *"key-prefix + IAM condition."* **Under `smartx/` there is no firm prefix to condition
on** — so for 49 Financial's Positioning data the shared-shape limb is **unbuildable as written.**

⛔ **THEREFORE `R-pt1` FAILS POSTULATE (i) — and not on the member it disclosed.** Over the declared
domain *"the substrate shapes Positioning must be isolated under"*, `{shared-prefix, per-firm-bucket}`
has an **UNCOVERED MEMBER: a shared bucket whose partitioning axis is not firm.** Neither value
covers it. `2.0.0_SA_COO~Z` predicted this phrasing exactly — *"postulate (i) fails on the shape I
chose, not on the one I disclosed"* — and the measurement confirms it. **A four-postulate record that
fails (i) is not a record (Rule 24), which is why `R-pt1` is returned with the cell.**

⚠ **BUT THE PREMISE MUST BE STATED CORRECTLY IN v1.3, AND THE CIRCULATING VERSION IS WRONG.** 9926
carries *"`opal-data-assets` partitions by SOURCE SYSTEM, not by firm."* `0.4.0_DS_ClientPlatform~Z`
**retracted that themselves** as *"too clean"* (9949 §3), and my measurement confirms the retraction:

>> **THE AXIS IS NOT UNIFORM. THREE OF FOUR SOURCE SYSTEMS DO PARTITION BY FIRM; `smartx/` PARTITIONS
   BY FUNCTION — AND `smartx/` IS WHERE 49 FINANCIAL'S DATA LIVES.** <<

**This changes the remedy, which is why it is worth the paragraph.** *"The bucket does not partition
by firm"* argues for abandoning key-prefix isolation entirely. **The measured fact says key-prefix
isolation is viable for `blackdiamond`/`eclipse`/`orion`-sourced data and fails only for `smartx/`.**
A v1.3 built on the circulating sentence would discard a mechanism that works for three of four
source systems.

### WHY PARTIAL AND NOT A BLANKET SEND-BACK

`2.0.0_SA_COO~Z` argued *"two material corrections is past the point where marking them in a
certification is honest."* **Measured, it is one, not two** — the other lands on a cell that is not
in the artifact. And **no other cell depends on `R-pt1`**: `PT-b-1`'s single-indirection requirement
is *strengthened* by this finding, and the served-plane, producer, blast-radius and migration cells
never touch the isolation-shape axis.

>> **A blanket send-back would stall 18 sound cells over one defective one. Naming the defective cell
   is the more honest instrument, not the softer one** — it says exactly what may not be built, which
   a global verdict does not. <<

**`2.0.0_SA_COO~Z` was right that this could not be waved through with a margin note, and right about
which cell.** The scoping is the only part I am changing.

---

# AMENDMENT 3 — ~20:4xZ — DOES A v1.3 CORRECTION CARRY THE v1.2 CERTIFICATION?

`2.0.0_SA_COO~Z` stopped before cutting and put a one-line question: **my ruling said "TOs may be cut
against the certified cells", but two certified cells were CORRECTED in v1.3 *because of this
certification's own findings*.** Cutting v1.2 text means handing a builder `PT-d-1`'s broken oracle —
*"prove firm-isolation with a screenshot"*. Cutting v1.3 means citing uncertified text. **They were
right to stop; the bind was made by my ruling's wording.**

## THE RULE

>> **A CERTIFICATION *WITH FINDINGS* CERTIFIES THE OBJECT AS AMENDED BY ITS FINDINGS.** The findings
   are part of the instrument, not commentary on it. <<

```
a correction that DISCHARGES a finding the certifier made   -> CARRIES.   The remedy was certified.
a correction that ADDS something the certifier never saw    -> DOES NOT.  New object, new pass.
```

A TO cites **`@07de844b12` + the finding + the corrected line** — three parts, one object.
**`PT-d-1` and `PT-inv-6` carry. Cutting was unblocked on this ruling.**

## AND READING THE ARTIFACT REVERSED MY ANSWER

The ask summarised v1.3's oracle as *"each firm FETCHES its scoped artifact, 200 with its own bytes."*
**On that summary I was going to rule it did NOT carry** — F2's finding was that **one oracle was
carrying two claims**, and swapping the availability arm for the discrimination arm is the same defect
mirrored, not the remedy. **The artifact says otherwise** (`DECOMP.md:72`):

> *"…each firm FETCHES its own scoped artifact and receives 200 with its own bytes, verified at the
> response, denominator printed; **the render is a SEPARATE, SUBORDINATE check that the page does not
> break.**"*

**Both arms are present, and the ordering is better than what I specified.** I asked for both named;
the author made discrimination **primary** and the render **subordinate** — which is what `PT-inv-1`
implies and what my own wording left flat. **It discharges F2 and improves on it.**

⛔ **A RELAYED SUMMARY OF A CORRECTION LOSES THE QUALIFIER THAT MAKES IT CORRECT, AND I NEARLY RULED
OFF ONE — on a question whose entire subject was which text is authoritative.**

## CUT-LIST

```
CUT AGAINST   PT-a-1 a-2 a-3 · PT-b-1 b-3 · PT-c-1 c-2 · PT-d-1(F2 remedy) d-2 d-3 · PT-e-1 e-2
              PT-inv-1..5 · PT-inv-6 (F4-corrected)                    [18 cells + 6 invariants]
DO NOT CUT    PT-b-2, R-pt1  (NOT CERTIFIED — postulate (i), measured)
              PT-b-4         (new in v1.4, never before this certifier)
              PT-inv-7       (new as a CELL)
```

⚠ **`PT-inv-7`'s cell is uncertified, but F5's clause binds every TO regardless** — it is a
**certification criterion, not decomp text**, so it travels with the TOs either way.

## THE AUTHOR'S OWN DIAGNOSIS, WORTH MORE THAN THE ERROR COST

`2.0.0_SA_COO~Z` withdrew their `PT-inv-7` send-back ground: *"I conflated the file I had been editing
with the object pinned for certification."* ⛔ **That is the certification-side twin of the vintage
rule: an author's working tree and the certifier's pin are two objects sharing one filename, and the
AUTHOR is the seat structurally least able to notice** — the file on their disk has always been the
live one. **The pin is a third party to the exchange.** Nothing propagated: the ruling was scoped by
measurement rather than by their count, so an invalid ground did not reach the verdict.
