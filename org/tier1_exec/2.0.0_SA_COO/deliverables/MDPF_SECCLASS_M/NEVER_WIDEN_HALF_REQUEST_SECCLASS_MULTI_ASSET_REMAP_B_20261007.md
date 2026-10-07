# Never-widen half, MDPF_SECCLASS -- the 33 `multi_asset` rows remapped into the six classes (Andrew-direct 2026-10-07: no multi-asset class; "I like B")

**Author:** `2.0.0_SA_COO~M`, 2026-10-07 ~02:0xZ. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half SIGNED; CTO half UNSIGNED. Nothing is written.**
Records: `ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`, `ANDREW_DIRECT_20261007_00xxZ_RULE_B_CATEGORY_RULE_FOR_MULTI_ASSET_FUNDS.md`; CTO msgs 105871, 105888.
Ledger `secclass-multi-asset-remap-b-m-20261007` (legs S, H, G).

## The act

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/remap_multi_asset_rows_b.py --write --half <this file> --snapshot <rollback.json>`, by the issuer, after both halves sign.
- **The set:** `R9_CHECKS/MULTI_ASSET_REMAP_B_SET_20261007.tsv`, 33 rows: **25 to equity, 8 to fixed_income**. 28 are placed by rule B's own category words in the fund's name
  (target-date, balanced, allocation -> equity; income-oriented -> fixed_income). **5 rows are this seat's call** (below).
- **Each row** is ONE conditional `UpdateItem` (compare-and-set): it lands only if the row still reads `multi_asset` / the recorded sub-class / the recorded `classified_by`. It sets `asset_class`, `updated_by = mdpf-secclass-remap-b`,
  `last_updated`; the sub-class is RESTORED on the five rows that read the same class before batch 183 (ABALX, AOR, VTHRX, VWELX, VWENX: the sub-class they carried) and otherwise REMOVED with `low_confidence = true` (28 rows;
  the old `Target Date` / `Fixed Mix` / `Flexible` are not equity or fixed-income sub-classes, and none is invented). Nothing else on the row changes; no row is created or deleted.
- **The writer** (dry run by default, read this session): `plan: MOVE 33, ALREADY 0, REFUSED 0`; `--write` refuses without `--snapshot` and without both halves reading SIGNED (a withdrawn or unsigned half refuses), writes the full pre-state of all 33 rows
  to the snapshot first, and a condition failure on one row is reported while the rest continue.

## The five rows that are this seat's call (rule B is "for example"; Andrew's B covers the other 28)

| fund | rows | proposed | why it is a call | held today (served, 10-05) |
|---|---|---|---|---|
| First Eagle Global | SGIIX, CUSIP:32008F606 | equity | sub-class Flexible; no category word in the name | cottonwood $160,910.85 (5 nodes), 49 Financial $75,599.41 (3), inflection $15,241.00 (4) |
| Vanguard Wellington | VWELX, VWENX | equity | a balanced fund by category; "balanced" is not in the name | 49 Financial $999,360.14 (2 nodes, VWENX), inflection $0 (4 nodes) |
| Vanguard LifeStrategy Moderate Growth | VSMGX | equity | an allocation family by category; "allocation" is not in the name | not held |

These are about $1.25 M of the $2.72 M that moves. The other call worth his eye under the rule itself: Income Fund of America, Capital Income Builder and Franklin Income are placed in fixed_income because their names say "income"
(rule B's wording); their actual equity and bond split is not in our data, and some of them may be equity-majority.

## What changes in the served output (named from the producers' rules)

Every producer reads a table row's `asset_class` verbatim (Holdings producer `classify_security` canonical-first; the gold scripts through `ETFClassifier`). After the act no row reads `multi_asset`, so no served node, mix or composition carries it.

**Holdings (the three firms, latest read 2026-10-05; `R9_CHECKS/MULTI_ASSET_REMAP_B_HELD_20261007.json`)**
| firm | held in `multi_asset` today | after: equity | after: fixed_income |
|---|---|---|---|
| Cottonwood | $160,910.85 (5 nodes) | $160,910.85 | -- |
| 49 Financial | $2,515,601.18 (35 nodes) | $1,971,366.25 (23) | $544,234.93 (12) |
| Inflection | $40,812.89 (20 nodes) | $15,241.00 (13) | $25,571.89 (7) |
| total | $2,717,324.92 | $2,147,518.10 | $569,806.82 |
The move lands at each firm's next Holdings build. The Holdings contract's `multi_asset` enum value stays valid and unused.

**Cottonwood gold (`opal-data-cot`)** (the code is the pre-S29 code, restored and read: S3 equals the repo): the four clients that hold SGIIX gain its dollars in `equity`, and their mixes sum to 1 again:
z09305578 equity .463922 -> .500560; z09305621 .432149 -> .528068; z09305679 .463970 -> .506724; z09305703 .778890 -> .805543 (the other shares unchanged; each sum 0.904-0.973 today -> 1.000).
`gold/views/firm_composition.json`: total $546,489,758.16, class sum $546,223,106.49, gap $266,651.67 today -> the gap closes, the $266,651.67 in `equity`. `platinum/firm/mix_summary.json`: pct sum 0.999524 -> 1.

**Black Diamond gold (`opal-data-bd`, 49 Financial)**: `gold/views/firm_composition.json` gap $5,438,537.08 today (total $1,994,163,246.13) -> closes. The $5.44 M lands in equity and fixed_income by this split of the ungated 2026-10-02 holdings-lots read
(`R9_CHECKS/MULTI_ASSET_REMAP_B_BD_LOTS_20261007.json`, each lot counted once): equity $4,629,737.04, fixed_income $904,855.88, total $5,534,592.92. That total is $96,055.85 above the served $5.44 M because it has no AP or ghost gate; the served split is not measured.
The client mixes: the holders of these funds read their class from the table at the next run; their per-holder shares are not computed here (the served files predate these rows, last run 2026-10-04); read at acceptance.

## Blast radius

`etf-classifications`: 33 existing keys change `asset_class` (and the sub-class as above); nothing is created or deleted. The table counted 3,507 rows at the 00:41Z scan and counts the same after, plus any put-on-absence rows other writers add in between. The keys are read by: the Holdings producers of the three firms; the Cottonwood and Black Diamond gold chains
(`C_06`, `D_03`, `D_04`; the other gold lists graded HOLDS-NONE in `COT_FIRM_CLASS_LIST_TRIAGE_20261006.md` T07-T22); the portal through those artifacts.

## Writers counted (`etf-classifications`), both branches

N = 7: the seed path; E_18 `detect_new_securities`; the CUSIP rows writer; `write-model-rows.py`; the FWD-9 writer; the FWD-10 producer; this remap writer. All but this one and the seed path put on absence and never touch these keys.
**The seed path is the one that bites:** 20 of the 33 rows were written by it (`updated_by seed-script`), and its source module `infra/aws/lambda/v2_portal/_shared/etf_classification.py` still says `multi_asset` for them; its merge rule returns CONFLICT where table and module disagree and its caller refuses. **The seed script is not run until the module carries the six-class values** (follow-up below).
- **Branch A, every compare-and-set lands:** 33 of 33 written.
- **Branch B, a row changed since the plan's consistent get:** `ConditionalCheckFailedException`, that row is left exactly as it was and reported; the rest continue.

## Rollback

The snapshot holds each row's full pre-state; `remap_multi_asset_rows_b.py --rollback <snapshot> --write` puts each back, only where it still reads as remapped by this writer (`updated_by mdpf-secclass-remap-b`). A rollback restores `multi_asset` rows, contrary to Andrew's word, so it is for a failed act only.

## Acceptance

1. Immediately after: consistent get-item of all 33 rows reads the set's class and sub-class, `updated_by mdpf-secclass-remap-b`, `classified_by` unchanged; a full table scan reads zero `multi_asset` rows and the same row count as before the act.
2. The next Holdings build of each firm: its remapped nodes read `equity` / `fixed_income` (counts and dollars per the table above); no node reads `multi_asset`.
3. The next Cottonwood gold run: the four clients sum to 1 within 0.001 with the equity shares above; `firm_composition` gap 0. The next Black Diamond run: `firm_composition` total equals its class sum within $0.01.

## Follow-ups (not part of this act; routed to the CTO)

The seed module and the table's vocabulary (so the seed script and the AI classifier cannot write `multi_asset` again); the Holdings contract enum, producer, reader and the portal class lists and legends; PRD wording of batch 164.

## COO half -- SIGNED

`2.0.0_SA_COO~M`, 2026-10-07 ~02:0xZ, after reading the set, the writer (dry run 33 MOVE / 0 REFUSED, the refusal without a signed half), the served dollars above, and the restored gold code (S3 equals the repo, 7 of 8; `B_01b` is not served output).
- **Blast radius:** the 33 keys above; the served effects named per firm. **Writers counted:** N = 7, both branches above. **Rollback per key:** the snapshot and `--rollback`.
- **Not signed here:** the five rows' placement beyond what Andrew's B states (they are marked for his or the CTO's overrule), and the follow-ups.

## CTO half -- UNSIGNED

Awaiting `1.0.0_SA_CTO`.
