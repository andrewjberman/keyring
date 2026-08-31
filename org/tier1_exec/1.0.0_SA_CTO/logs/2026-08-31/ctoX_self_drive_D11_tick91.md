# /self-drive D11 -- tick 91 (measured 00:43Z, written 00:5xZ)

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

- seat: `1.0.0_SA_CTO~X` (design lane) -- cron **31950a5f**, 60m at :11; paired with `/drive D11 @ 2.0.0_SA_COO~X`
  (+15m). ticks covered: **91**. state: **ARMED**.

## Steps

- **Step 0** register: **12 live directives**; D11 device LAPTOP, `open_tos` 2, flags `[]`; members
  `NFRA_SUBSTRATECARDING` + `NFRA_C3MATERIALIZE`, both `active`. Claims scan **342 project JSONs, 0
  unreadable, 1 PRD-path claim** (`NFRA_SUBSTRATECARDING` -> `docs/architecture/D11_SUBSTRATE_ANALYSIS_PRD.md`,
  already a member -- the overlap is correct, not an error). **2 of 2 REACHABLE.**
- **Step 1** `/open-calls` scoped D11: **0 adjudicable, 2 CARRIED at Andrew, 0 BLOCKING** -- unchanged. The
  all-RESERVED tell did NOT fire (nothing was classified RESERVED this tick; the 2 CARRIED cards are a
  standing render, not a new classification).
- **Step 2** no pitch -- **zero calls in scope, so no empty packet was sent to `3.0.0_SA_CVO~X`.**
- **Step 3** one verdict landed and one ruling issued; **ledger row 22** appended.
- **Step 4** completion test READ from `org/projects/*.json`: **NOT DONE -- 0 of 2** `complete`.

## Delta since tick 90

1. ⭐ **RULE 3 INDEPENDENTLY VERIFIED AND PASSED BY `3.0.0_SA_CVO~X` (004334Z), BY ITS OWN ENUMERATION.**
   Operative: *"Independent exact-pin verification PASSES Addendum 1v / Rule 3 at `510a84ab23`."* It
   reproduced **116 card JSONs at pin `47954ef3de`, 116 parsed, 102 with `basis_by_field`, exactly 12 fields
   on the stated 12 cards**, pytest 7/7, all four controls clean, worktree blobs equal to the pin, ancestry
   fresh -> LOCAL. **A different enumeration reaching the same 12 is corroboration; had it re-run my script
   it would have been repetition.** It also restated the non-application clauses back correctly -- explicit
   null token only, Class B stays human, no assessment of measurement quality, prospective-only.
2. **ADDENDUM 1w RULED -- the design ruling `3.0.0_SA_CVO~X` asked for at 002908Z, on `2.0.0_SA_COO~X` 89651.**
   That issuer did the thing only the issuer could: **read BOTH faces and see that its own extraction defect
   and `0.7.0_AE_CloudOps~X`'s four-instance shape are ONE failure** -- *a set that shrinks silently because
   the thing that enumerates it and the thing that checks it share an author and a blind spot.*
   **RULED (i):** the conservation shape **GOVERNS** multi-carrier claim repairs -- scope the repair to THE
   CLAIM, DERIVE its carrier set, and require each returned carrier **MOVED or DECLINED BY NAME**. It is
   **indifferent to direction**, which is exactly the property the four instances defeat.
   ⛔ **RULED (ii), the open half:** **prose discovery is bounded by its FAILURE DIRECTION, never by its
   completeness.** Requiring "every sentence asserting the claim" is unsolved -- and the hazard is not that
   it stays unsolved, it is that **an unsatisfiable rule gets discharged by an approximation that LOOKS
   complete**, which is the chosen-set-reported-as-corpus defect this record already carries against ME at
   1s Amendment 1. So the sweep is mechanical and **LEXICALLY OVER-INCLUSIVE**: under-inclusion fails
   **silently and byte-identically to a clean repair**; over-inclusion fails **loudly**, costing one
   declining line.
   **MEASURED rather than argued** (card 7's cadence claim at pin `47954ef3de`): **77 string leaves, sweep
   returns 14 for disposition, true carriers ~4** -- so the required direction costs ten extra lines read
   once. ⭐ **And the sweep returns `/verdict/why`, the DOWNSTREAM carrier the producer had to remember
   separately** (*"The verdict limb is re-worded to match"*) -- the mechanical procedure surfaces the carrier
   the remembered enumeration reached only by luck.
   **RESIDUAL DECLARED, NOT SOLVED:** a paraphrase carrier sharing no signature token is unreachable by any
   lexical sweep, so the denominator reads **"carriers reachable by the declared signature"** -- the same
   scoping `0.7.0_AE_CloudOps~X` adopted hours earlier for the trigger name-plane.
   ⛔ **NOTHING ARMED: no gate, no checker rule, no card change** -- and the rule does NOT bind a
   single-carrier fix or the FIRST authoring of a claim, only a repair across carriers.
   **WHAT IT DOES NOT FIX:** conservation proves every carrier MOVED, never that they moved to the RIGHT
   value. All four instances would have been caught; **a fifth where every carrier is updated consistently
   to a WRONG value passes completely** -- that stays a certifier's read of the merits.
3. **NEITHER SEAT PROPOSED A FIFTH ARM AND BOTH WERE RIGHT NOT TO.** `0.7.0_AE_CloudOps~X` refused on the
   ground that an arm shaped to its four instances would be shaped to the last defect class again, citing
   this lane's own 89083 back at it; `2.0.0_SA_COO~X` refused and pointed at the already-ruled general
   remedy instead. **The ruling adds a shape, not an arm.**

## Scope state (denominators printed)

| project | status | dep_stage | open TOs | reachable |
|---|---|---|---|---|
| NFRA_C3MATERIALIZE | active | EXECUTING | 1 (7A CERTIFIED + DELIVERED; determination typed B; edge-vocabulary finding CLOSED @`e6a6e781ed`; gate `after-bridge-declared` STAYS OPEN -- only OUTCOME_A discharges it) | YES |
| NFRA_SUBSTRATECARDING | active | EXECUTING | 1 of 9 open; **6 of 7** cards closed; card 7 on its **THIRD** successor `47954ef3de` with its certifiers; face proof owed by the producer and not started | YES |

Completion test: **NOT DONE, 0 of 2**. RESERVED cards at Andrew: 2, CARRIED, neither blocking.
**Owed by this seat (DERIVED):** nothing unblocked. The W4-COX face design read lands if a certifier stops
the next successor; the 1u-conformant re-declaration lands if the issuer amends the margin procedure; RULE 3
binds at the next card cut. **HALTGT is DISARMED by assignment and queued behind the W4-COX face per
`2.0.0_SA_COO~X`'s shape-(a) call -- this lane holds the design ruling, not the repair.**

## Push state (measured 00:5xZ)

`origin/CLOUD` = **`ea912ac001`** (ls-remote). `e6a6e781ed` **ON ORIGIN**; `510a84ab23` (RULE 3 + 1v),
`47954ef3de` and this commit **LOCAL** -- ⛔ **push on `CLOUD` is INTEGRATOR-ONLY and the gate refused this
seat by name**, so these ride the next integration window; that is the correct terminal state for this lane,
not a failure. Null control `ffffffffff` ABSENT. **Perishable -- re-derive.**

## Compiler Tools

| tool | result |
|---|---|
| `python .tools/directives-check.py --json` | 12 live; D11 LAPTOP, 2 members, open TOs 2, flags [] |
| `org/projects/*.json` claims scan (both `prds[]` shapes) | 342 scanned, 0 unreadable, 1 PRD-path claim |
| lexical carrier sweep over card 7 at pin `47954ef3de` | 77 string leaves -> 14 returned for disposition, ~4 true carriers, `/verdict/why` surfaced |
| `git ls-tree` + `git show` per file at the pin (RULE 3 census) | reproduced independently by `3.0.0_SA_CVO~X`: same 116/116/102 and the same 12 |
| `git ls-remote` + `merge-base --is-ancestor` + `cat-file -e` (3-state) | placements as stated, null control ABSENT |
