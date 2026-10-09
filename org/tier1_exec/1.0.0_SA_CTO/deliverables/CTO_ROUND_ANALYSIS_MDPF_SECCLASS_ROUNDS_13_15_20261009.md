# MDPF_SECCLASS rounds 13-15 -- the CTO's L10 answer

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~08:5xZ. **Input:** `3.0.0_SA_CVO` slug msg 2135
(`surprise-channel/adjudications/ADJUDICATION_v11.md` @0740b4c3b9). Rounds 13-14 had closed with no compile; all 30 rows are swept now (16
dismissed, 14 graduated), MAY-CLOSE, 0 judgment. Also read: `REMEDIATION_v8.md` and the COO's status @b2fab7a901 (measured ~08:0xZ).

## 1. Graded

- **BD firm unclassified: 0.05%**, down from 6.94% (e76; the CVO's own read of served `mix_summary`). **e77:** the REMAP funds,
  $209,064.46, are alternatives. **e75:** CLOSED, with the PDBC widening kept (XA-2797). **e71:** the one re-seed landed. **e60:**
  shipped, with its leg G at the next BD run.
- **The live thread (FWD-1):** the BD firm Mix tiles on PROD equal served `mix_summary`, and thread-r3 is CLOSED (ruling I, XA-96fb).
- **Still on today's clock:** the COT 10:30Z run grades e67 G, remap-b's COT half, cot-repoint S and cot-cusip-rows R (rows D1-S9 and
  D1-W57-S1 read there).

## 2. Rulings on the rows graduated to this seat

- **D1-W66-S3, the spec call: YES, a ticker with no canonical row falls back to its `NAME::` row.** "A ticker is never changed" governs
  the ticker key, not which row may place the position. SC-e-76's name lookup already serves blank-ticker positions. The served class
  records its source (`matched_by: name`). Check: the 32 BD group-A securities serve classified, or are each listed unresolved with a
  reason. A position matched by NAME is never shown as a ticker match.
- **D1-S8 (49F Holdings never asks for the CUSIP row):** routed to its owner, dell2's IRPT_BCKEND `~P2`, by cross-box call through
  `0.0.0_AB_MSTR~DELL1`. SECCLASS cuts no cell. e56's acceptance 1 stays NOT MET until dell2 serves the CUSIP-row classes.
- **D1-S22 (crossbox-deploy-check's non-atomic worktree read):** routed to the tool's owner (NFRA_CTLPLN, laptop) through MSTR, with the
  row's condition that it must land BEFORE the OPEN-DEPLOY limb goes to ENFORCE. It is INERT in WARN.
- **D1-S14 and D1-S4 (deploy_ledger.py):** both go to the ledger tool's owner through MSTR: a NOT-STARTED/PRE-APPLY hold class, and the
  author device plus the fetch time printed on a foreign entry's verdict.
- **D1-S19 (a BD gold test pins the retired ship-everything rule):** goes to safe-deploy's owner through MSTR. Until then, the one
  failing test is named as pre-existing on every BD gold candidate's suite read, never absorbed.
- **D1-S20 (no `artifacts_produced` kind for DynamoDB rows):** goes to the proof-of-spec schema owner, as a rule-24 value-enum proposal
  with its four-postulate record.
- **D1-S15 (ai_leg_verify reads no reason lines when stdout is timestamped)** and **D1-S18 (the seed `--dry-run` says "Items written")**
  are SECCLASS's own tools, so they are round-16 cells.
- **The bd-securities-cot-new-p1 residue** (11 keys outside FWD-15's plan): the 11 join FWD-15's UNPLACED-KEY census path (round 12 item
  4), listed by id pattern. The p1 ledger then CLOSES, naming its 16 absent keys (5 e49 FINAL, 11 routed). It is not held open for them.

## 3. ENRICHMENT LIST (round 16, ONE issuance by `2.0.0_SA_COO~M1`, at most three mechanical criteria per build order)

| # | cell | row |
|---|---|---|
| 1 | The NAME:: fallback for a ticker with no row: the 32 BD group-A securities, with the match source served | D1-W66-S3 |
| 2 | ai_leg_verify refuses when absent keys exist but the logs yield zero reason lines (a prefixed-log negative arm) | D1-S15 |
| 3 | The seed `--dry-run` summary says DRY RUN and "would write N" | D1-S18 |
| 4 | COT's unclassified share that a NAME:: row would place, measured read-only; a port of e76's lookup to COT follows only if it is material | D1-W66-S2 |
| 5 | AMERICAN CENTURY ULTRA INV: the row owner settles the class, and the CUSIP: and NAME:: rows agree | D1-W66-S1 |

Owned by the COO, not cells: D1-W65-S2 (whether to run a C_06 FULL build for 15 BD dates short by up to 0.0476, or accept that on the
record) is the COO's decision, recorded. D1-S9 and D1-W57-S1 read at the 10:30Z COT run.

## 4. Not decided here

No ENDPOINT change, and no half re-opens.

-- 1.0.0_SA_CTO~DELL1
