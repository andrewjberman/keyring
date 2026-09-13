# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 41

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T02:24:07Z**
Tick 40's log is `@5495d05415`. **The POSN obligation carried since tick 39 is DISCHARGED, and the
count collapses: twenty-six ids are NINE obligations.**

---

## 1. THE NINE READ TO A CONDITION EACH -- `Z-S39` `@8efaf17312`

Two of the nine are acts this seat can take and nobody is blocked on either:

- **`Z-W10-S1`** -- its own text: *"ARMED rather than INERT for one reason only: the mis-stated
  mechanism lives in the PRD."* **The POSN PRD is this seat's file at L4** -- one sentence, no other
  seat, not done.
- **`Z-C-S55`** -- *"The CTO must settle this existing owning surface coverage at the project
  boundary."* A SCOPE decision, which is why it sits here and not in a cell.

The other seven are tooling/gate observations correctly parked on the gate owner. Two are real gate
weaknesses and are **parked, not dismissed**: `Z-C-S10` (`SURPRISE_ROW_OVERRIDE` is a **commit-wide
boolean** -- one reason suppressed six violations) and `Z-C-S24` (the `PROOF_OF_SPEC` kind enum has
no DynamoDB item kind, so an instance substitutes `s3_object` and the checker skips it -- **VALID
does not make the datastore checked**).

⚠ **A NEAR-MISS THE CONTROL CAUGHT BEFORE IT WAS WRITTEN.** Five of the nine appeared to carry no
remedy line, which read as a defect in those five rows. **Zero of 64 rows in this project's
adjudication documents carry a `remedy` field at all** -- it is the document's SCHEMA, and the
condition lives in `world_is`. *"Five rows have no remedy"* would have been literally true and
materially misleading.

## 2. THE EIGHT PAIRS READ, AND THE COUNT COLLAPSES -- `Z-S40` `@0a4af820b8`

Read from the rows' own **`adjudicates`** field rather than a token screen:
`Z-W2-S3`→`Z-C-S7`, `Z-W2-S4`→`Z-C-S8`, `Z-S1`→`Z-C-S10`, `Z-W8-S2`→`Z-C-S21`+`Z-C-S33`,
`Z-W8-S4`→`Z-C-S23`, `Z-W8-S5`→`Z-C-S24`, `Z-S7`→`Z-C-S38`. **Every target but one is among the nine
already read.** The eighth, `Z-C-S21`, is superseded by `Z-C-S33` on that row's own words, under
Andrew's call-1 YES. Positive control: 54 of 134 rows carry the field, so it discriminates.

```
 8 INERT at surfacing + 9 armed adjudication-plane obligations
+7 investigation-plane ORIGINALS of those same nine + 1 superseded + 2 of this seat's meta-rows = 26
```
⭐ **THE HONEST OBLIGATION COUNT IS NINE.** `4.0.0_SA_CRO~Z`'s line, now measured on a second
project: **the id is the item, the plane is a facet, and a row count is not an obligation count.**
Every armed count published tonight -- nine, thirty, fifty-three, five, 104, 149 -- is a FACET count
and none of us said so at the time. This is the first converted.
⭐ **And the conversion instrument is STRUCTURAL, not a screen.** This seat's DISARM-token screen
produced a false close twice tonight; the `adjudicates` field produced none.

## 3. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED · NO PITCH (unchanged; CVO-confirmed at tick 31)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  1 OPEN of 46 -- round 8, rg-2 remaining
  POSN_ASTTAX  active/EXECUTING  REACHABLE  4 OPEN of 15 -- round 4 not cut; L10 held on Andrew
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
**Both channel obligations this seat carried are now discharged** -- AMGT's at `Z-S59`, POSN's at
`Z-S39`/`Z-S40`. The two remaining POSN acts are scheduled to the moments they belong to rather than
forced now: the PRD sentence at POSN's L10 when that file is legitimately open, and the boundary
decision in the round-3 L10 analysis where scope questions are answered. **Opening a PRD mid-round
to fix a sentence is the disruption Andrew's ruling names.**

⚠ **A TYPED STAMP CAUGHT AND REPLACED BEFORE COMMIT:** `Z-S40`'s `surfaced_at` was typed from a read
taken 90 seconds earlier rather than measured at the write. Replaced with `date -u`. Small, and the
same class as the placeholder the gate refused at `Z-S36`.

**Push state:** `origin/SITEZ 8efaf17312`; local ahead 2. `HEAD:portal e85f6eb84f`, unmoved. No TO
cut, no dispatch, no apply, no merge, no promote.

## Compiler Tools

The fence-line reader admitting BOTH bracket and brace blocks, with files / blocks
present-admitted-skipped / rows / unparseable / read time · the rows' own `adjudicates` field as the
plane-link instrument, with a 54-of-134 positive control · a `remedy`-field census over 64
adjudication rows as the control that killed a false finding · `_open_tos_for_project` with
`ZZZZ_NOSUCH` · `git status --porcelain` on the channel path before each append · a post-write
verify admitting both block shapes with a `Z-S99` negative control · `date -u` at the write, not
before it · `safe-commit.sh -F`.
