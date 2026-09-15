# POSN_ASTTAX -- L5 DECOMPOSITION (round 7) -- DRAFT, NOT CUT (the cut follows the 13:00Z promote, per the CTO's L10)

**archetype:** IMPLEMENT (one cell: the seeder guard's owned fields reconciled with the retag's write surface, by measurement and exercise)
**Owner (L5-L6):** `2.0.0_SA_COO~Z` - **Date:** 2026-09-15 ~10:2xZ - **Directive:** D4 - **Macro:** POSN - **Fabric:** site-z
**PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.11** @`ab2ee8052a` (ADMITTED; both halves SIGNED by the ~Z lanes; NO addendum for this round --
C-RETAG-SAFETY / C-RETAG-SET already bind the guard to the retag's writes). **Answers:** `1.0.0_SA_CTO~Z`'s round-6 analysis
`ledger/ROUND_ANALYSIS.round6.md` @`e60bf6dca1` (msg 23119), which answers `3.0.0_SA_CVO~Z`'s round-6 slug `REMEDIATION_v6.Z.md`
@`895a87921f` (L9 `ADJUDICATION_v8.Z.md`: V3-AC7 FAIL -> `C-S177` DECOMP_INVALIDATING, ARMED, owner `1.0.0_SA_CTO~Z`).
**The CTO's cell text:** *"The cell adds management_style to the owned tuple (or states, measured, why a reseed cannot write it) and a
criterion that runs the guard against a reseed changing ONLY VNQ's management_style and reads the refusal."*

> **STATUS OF THIS FILE: ONE CELL, DRAFTED; the ONE issuance (`TO-X1-1`) is cut AFTER the 13:00Z portal promote (the CTO's word in
> 23119: "ONE-cell recut C-S177 after the 13:00Z promote"). Nothing in it gates the promote.

---

## 0. WHY THIS ROUND EXISTS -- the subtraction

```
DENOMINATOR   31 task orders under POSN_ASTTAX (27 complete, 2 superseded, 2 cancelled, 0 open)   -- the CTO's s.1
DECLARED       7 (FWD-1..FWD-7)      COVERED 7      UNCOVERED {}
OPEN ITEM      C-S177 (FWD-5): the guard-owned tuple vs the retag's write surface -- a DECOMP_INVALIDATING row, not an outcome gap
```

## 1. THE PREMISE, MEASURED AT HEAD (this seat, ~10:2xZ) -- and why the CTO's parenthesis is the branch the bytes take

`data/black_diamond/scripts/classification/seed_canonical_securities.py` (351 lines):
- `YANG_OWNED_FIELDS = ('asset_class', 'sub_asset_class', 'name')` :210; `_yang_conflicts()` :213-231 compares exactly those fields
  against the live row and returns the disagreements; `seed()` :234-336 REFUSES (rc 1, `[PRESERVED] ... table wins`) on any conflict
  unless `--force`.
- **The seeder's ENTIRE write to the Yang table** is `yang_table.update_item(... UpdateExpression='SET asset_class = :ac,
  sub_asset_class = :sac, #n = :n, last_updated = :ts, updated_by = :ub' ...)` :303-315 -- an UPDATE, never a put; it SETS three
  owned fields plus two audit fields and touches NOTHING else. The module docstring :14 says so in prose ("every field it does not own
  (rationale, firm_origin, management_style, ...) is preserved").
- The seeder's records (:46-206) carry `ticker, asset_class, sub_asset_class, name` -- **no record carries `management_style`**, and
  **VNQ is not a seeder record** (0 occurrences).

So: (a) a reseed CANNOT write, clear or revert `management_style` -- the field is outside the seeder's SET clause; (b) a reseed cannot
touch VNQ at all; (c) `YANG_OWNED_FIELDS` equals the seeder's SET surface exactly (3 of 3) -- the guard owns what the seeder writes.
The CVO's C-S177 reads the tuple against R1's write surface (`asset_class, sub_asset_class, management_style` + `name` on the dict);
the reconciliation the row asks for is that the two surfaces be STATED and PROVED against each other: the guard must own every field
the SEEDER writes (it does), and R1's `management_style` write is outside the seeder's reach (it is). Adding `management_style` to the
tuple would make `_yang_conflicts` raise `KeyError` on `sec['management_style']` for every record (no record carries it) or, guarded
with `.get`, compare a live value against nothing -- a vacuous check that reads as protection. **The honest cell is the CTO's
parenthesis: state it, measured, and EXERCISE it** -- a reseed on a scratch copy against a row carrying `management_style 'active'`
leaves that field byte-identical whether the reseed writes (classes agree) or refuses (classes disagree), and a scratch VNQ row is
untouched in both arms.

## 2. THE CELL

### `AT7-s-1` -- the seeder guard reconciled with the retag's write surface: stated in the file, proved by exercise (C-S177)

**Write surface:** `data/black_diamond/scripts/classification/seed_canonical_securities.py` -- a COMMENT-ONLY change at :206-210 stating
the measured write surface (the SET clause's fields == `YANG_OWNED_FIELDS`; `management_style` and every other field outside the clause
are never written, cleared or compared; VNQ is not a record) and, beside `YANG_OWNED_FIELDS`, an ASSERTION that fails loudly if the two
surfaces ever diverge (a module-level check that the SET clause's owned fields equal the tuple -- read from the expression string, so a
future edit to one without the other trips it at import); the worker's deliverables `~27/`; the channel. No served output moves; the
live table is never opened for write (`--upload` never passed; the scratch harness of V3, `v3_mutant_control_re.py`, replaces boto3
before any seeder byte runs). never-widen: NON-APPLICATION (no served key; a comment and an import-time assertion).

**Bar:** (1) the write-surface proof -- the SET clause's field names read from the file equal `YANG_OWNED_FIELDS` 3 of 3 and
`management_style` appears in neither (printed); (2) the exercise on V3's scratch harness: a scratch Yang row `{QBER: asset_class
structured, sub_asset_class Hedge, management_style active}` with the seeder asserting `fixed_income / Volatility` -> REFUSED, the
row byte-identical after (management_style `active`); a scratch row whose classes AGREE with the seeder -> WRITTEN (last_updated
moved) and `management_style` byte-identical after; a scratch VNQ row `{alternatives, Real Estate, passive}` -> not in the seeder's
records, untouched in both arms (its bytes before == after); the negative control: the harness with the SET clause mutated to include
`management_style = :ms` moves the field -- the instrument can see a write it would have caught; (3) the assertion trips on a mutated
tuple (import fails) and passes on HEAD's; (4) commit-gate clean, ASCII 0; (5) the live table's VNQ/QBER rows identical before and
after (a point read, not a scan); (6) JUDGMENT for L9: whether "the guard owns exactly what the seeder writes" is the reconciliation
C-S177 asked for, or whether R1's `management_style` write wants a guard of its own in the retag script (`r1_rollback.py`'s sibling),
which no seeder can defend. Slot `~27`, wave 1, the only cell. `fanout: 1 of 1 chains, cap 8`.

## 3. WHAT THIS ROUND DOES NOT CUT

The cosmetic and tooling rows the CTO carries (Z-S146, Z-S169, Z-S172, Z-S154, Z-S163, Z-S151, Z-S143/S145, Z-S148/S150/S156/S162,
Z-S158, Z-S173/S174, Z-S137) -- "the next Positioning frontend cut when Andrew calls one" and their named owners. Any promote, push or
gitlink move (the MSTR's on Andrew's word). The third driven characteristics run and the 12:30Z organic read (round 6's arms, this
seat's).

## 4. THE BATTERY

| lens | disposition | denominator / blindness |
|---|---|---|
| `comp-schedule --drift` | DECLARED-NOT-APPLICABLE at L5, RUN at the cut | no deploy, no schedule; the open ledger of interest is B6's L8 (the 12:30Z fire) |
| `comp-iam` | DECLARED-NOT-APPLICABLE | no role or policy; the live table is read by point reads under the operator identity, written by nothing |
| `comp-adversary compose <this file>` | RUN at the cut | the cone recipe (Z-S148) and the base-anchored bars (the memory) applied |

## 5. Four-postulate record (Rule 24)

(i) MECE over the domain {C-S177}: one cell consumes it. (ii) SAME GRAIN: one file, one guard. (iii) INTENT: "the guard owns what the
seeder writes, proved". (iv) STATE: what does not move -- the live tables, every served key, the retag script, the seeder's records.
