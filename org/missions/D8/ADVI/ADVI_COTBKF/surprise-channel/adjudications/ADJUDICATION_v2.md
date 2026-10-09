# ADVI_COTBKF: CVO adjudication, rounds 2 and 3

<sweep_watermark>2026-10-07T02:21Z</sweep_watermark>

Rounds 2-3 L8 compile and L9 adjudication by `3.0.0_SA_CVO`, 2026-10-07 ~03:4xZ. Channel read at 63fe6e1aa8: 24 rows, 5 dispositioned in
ADJUDICATION_v1.md, 19 here (3 ARMED), in rows C-S3 to C-S9. All eight round-2 and round-3 orders read `complete`. Judgment criteria: CB2b3-AC3 NOT MET,
CB3c3-AC3 MET, CB3c4-AC3 MET; the grade file is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md`.
Graduated rows are in `remediations/REMEDIATION_v1.md`. After this document 0 rows are undispositioned and 0 are ARMED.

```json
[
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S3",
    "one_line": "ROUNDS 2-3 L9: CB2b3-AC3 is NOT MET -- the price-store census missed a CUSIP-keyed daily closing-price store; W6-S2 GRADUATED with that finding and its open cross-firm question.",
    "spec_asserts": "CB2b3-AC3: every Opal store that holds a daily price series was checked and named with its verdict, so an UNPRICED security is unpriced by Opal. W6-S2: the stores found are the bd, inf and cot canonical and historical price files, and whether a Cottonwood-tenant read may use them was not resolved.",
    "world_is": "The census names 22 stores in 10 of the account's 40 buckets. This seat listed the other 30: none holds a standalone ticker-keyed price file, but opal-data-49financial gold/advi/canonical/canonical_positions holds cusip and closing_price for 565 daily partitions (2024-07-08 to 2026-10-05) and is not named. Its 2026-10-05 partition alone prices 912 of the 4,634 Commonwealth CUSIPs by CUSIP (Equity 572, ETF 193, Mutual Fund 137, Closed End 6, Fixed Income 3, Alternative 1); the census matched 0 securities by CUSIP in its five large stores and 0 Fixed Income. Four more position-level stores are named DERIVED_NOT_READ without a read. So 3,128 unpriced is unpriced by the stores read, not by Opal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-buckets (this seat, 2026-10-07 03:0xZ): 40 buckets; 10 named in PRICE_COVERAGE_20261006.json; full key listing of opal-data-49financial (49,949 keys), opal-data-cottonwood (732), opal-data-inflection (5,543), opal-data-irpt (478), opal-data-pm (102), opal-data-portfolio (9)",
        "s3api get-object opal-data-49financial gold/advi/canonical/canonical_positions/date=2026-10-05/data.parquet: 108,185 rows, columns include cusip, closing_price, business_date; 2,468 distinct priced CUSIPs; 912 in .scratch/price_cache/universe.json (4,634 rows)",
        "python data/assets/scripts/analysis/commonwealth_price_coverage.py (this seat): PRICE-COVERAGE universe=4634 stores_checked=22 stores_with_prices=7 priced_any=1506, rc 0 in 9.7 s",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W6-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S4",
    "one_line": "ROUNDS 2-3 L9: the three cache hazards (W6-S4, W10-S3, W11-S3) are DISARMED and closed -- each criterion re-ran inside its bound in the shared tree at this seat; S4, S5 and S6 are their disarm evidence.",
    "spec_asserts": "Each order bounds its real-data criterion at 120 seconds; each ARMED row says the bound holds only against a cache in a worker's worktree that was about to be removed.",
    "world_is": "The three caches now sit in the shared tree's .scratch/. This seat ran all three criteria there: CB2b3-AC2 9.7 s, CB3c3-AC2 6.4 s, CB3c4-AC2 3.1 s, each rc 0 with the expected line. Each order told the worker to cache under .scratch/, so the cache is the spec, and the hazard was only its location. A clean tree on another device still needs one cold run first (5 to 19 minutes for the price read).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's runs, 2026-10-07 02:4xZ to 03:3xZ: CROSSWALK commonwealth_accounts=1533 every_account_listed=True matched=439 (6.4 s); ACCOUNT-LINKS old_accounts=459 every_old_account_listed=True linked=180 (3.1 s); PRICE-COVERAGE universe=4634 (9.7 s)",
        "investigation rows ADVI_COTBKF-S4, -S5, -S6 (2.0.0_SA_COO~C): the copy acts and their own re-runs",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W6-S4",
      "ADVI_COTBKF-W10-S3",
      "ADVI_COTBKF-W11-S3"
    ],
    "disposition": "GRADUATED"
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S5",
    "one_line": "ROUNDS 2-3 L9: two scripts read legacy S3 locations from a record file under org/ because the naming gate refused the typed addresses (W6-S5, W10-S5) -- GRADUATED for a ruling under rule 30.",
    "spec_asserts": "CLAUDE.md rule 30: every S3 address is address() output, and a builder refusal is a missing registry row to add, never a hand-typed workaround.",
    "world_is": "commonwealth_price_coverage.py reads 22 store locations from PRICE_COVERAGE_STORES_20261006.json, and commonwealth_crosswalk.py reads three from CURRENT_SIDE_LOCATIONS.json. Both files sit under org/, which the naming gate does not grade. No registry row was added and no override was used. The addresses are existing pre-LGIC stores that the builders do not emit, so rule 30's non-application for existing pipelines may cover the READ; nobody has ruled it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-W6-S5 and -W10-S5; org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~10/CURRENT_SIDE_LOCATIONS.json (767 bytes, read at this compile)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W6-S5"
    ],
    "disposition": "GRADUATED"
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S6",
    "one_line": "ROUNDS 2-3 L9: CB3c3-AC3 is MET; W10-S4 GRADUATED for one in-kind exit the date cutoff never scored and 17 near-matches left for a person.",
    "spec_asserts": "CB3c3-AC3: a sample of MATCHED rows is right on its printed evidence, and no NOT_MATCHED reason hides a match the evidence shows.",
    "world_is": "All 439 matches are R2. This seat recomputed the 9 positions-basis matches with its own code: 9 of 9 hold. For the 430 rebuilt matches the current account's first holdings fall 0 to 10 days after the in-kind exit date, 430 of 430, and no current account is matched twice. No NOT_MATCHED row scores 0.8 or more; 17 score 0.65 to 0.8 and are listed with their candidate. One gap: of the 758 CLOSED_BEFORE_CURRENT_HISTORY rows, 11 end in 2026, and acct#a2618be7 left in kind on 2026-04-07 (SCHF 245, IWM 28.809, VADFX 204.943, IBIT 131, FDRXX); the cutoff of 2026-04-22 kept it from being scored. Three current accounts hold the same quantity of 3 of its CUSIPs, which is below the 80% bar, so no match is hidden at the rule.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's recompute over .scratch/advi_cotbkf/cache (positions 469 rows, holdings 1,452,421 rows, transactions 1,416,497 rows) and crosswalk.parquet (1,533 rows), 2026-10-07 03:1xZ",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W10-S4"
    ],
    "disposition": "GRADUATED"
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S7",
    "one_line": "ROUNDS 2-3 L9: CB3c4-AC3 is MET; W11-S2 GRADUATED because a client's line stops at an account that itself ended before the delivery's end.",
    "spec_asserts": "CB3c4-AC3: one client read as one line across an account change is right on its printed evidence, and a sample of LINKED rows holds. FWD-9: the history reads as one line from the oldest account to the newest.",
    "world_is": "This seat checked every evidence item of all 180 links against the raw transactions: 2,652 of 2,652 items have the exit row on the old account and the receipt (one row, or the same-day sum of li rows) on the new one. 175 of 180 share the advisor. The line cvacct#e3f1271c -> acct#e3f1271c -> acct#1b9c5f5a reads as one client across two changes. The limit is W11-S2's: rows exist only for the 459 accounts that ended before 2018, and 46 of the 148 non-old targets stopped trading before 2026, so those lines may not reach the newest account.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's check over .scratch/advi_cotbkf/account_links/account_links.parquet (459 rows, 180 LINKED) and the cached transactions, 2026-10-07 03:3xZ",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W11-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S8",
    "one_line": "ROUNDS 2-3 L9: eight rows are RECORDS needing no remedy -- order premises the data corrected, and rule readings the two judgment grades found sound.",
    "spec_asserts": "W6-S1: security_market holds about 730 days. W6-S3: the order does not say whether a reused-symbol match counts. W9-S1: listings may miss PDFs. W10-S1, W10-S2, W11-S1: the orders' literal holdings rules. W7-S1: the worker expected its names to commit as written. W8-S1: reads finish inside 120 seconds.",
    "world_is": "W6-S1: 4 partitions, 0 needed days, measured and printed. W6-S3: reused-symbol matches are not credited and the amount left out is printed per store, so coverage is a stated floor. W9-S1: the 51 listings cover all 11,119 PDFs; the unlisted branches are fixture-tested and no real row exercises them. W10-S1, W10-S2 and W11-S1: the literal rules return almost nothing (the literal link rule gives 0 links); the applied readings are printed in each output and hold under this seat's recomputes (rows C-S6 and C-S7). W7-S1: two name-shape false positives of the commit gates, renamed around. W8-S1: the read passes at 78 s with parallel fetches.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows named in adjudicates, read at this compile",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W7-S1",
      "ADVI_COTBKF-W6-S1",
      "ADVI_COTBKF-W6-S3",
      "ADVI_COTBKF-W8-S1",
      "ADVI_COTBKF-W9-S1",
      "ADVI_COTBKF-W10-S1",
      "ADVI_COTBKF-W10-S2",
      "ADVI_COTBKF-W11-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row records a premise the data corrected or a reading the worker printed and this seat verified; no outcome changed and no act is owed. The gate false positives in W7-S1 are precision notes for the gates' owner, carried in the grade file."
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T03:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S9",
    "one_line": "ROUNDS 2-3 L9: four rows are carried by another row and need none of their own -- S4, S5 and S6 are the disarm evidence of W6-S4, W10-S3 and W11-S3, and W10-S5 is the same finding as W6-S5.",
    "spec_asserts": "S4, S5, S6: each records the issuer's disarm act for one ARMED cache row. W10-S5: the naming gate refused three typed locations, as in W6-S5.",
    "world_is": "The three disarm acts are verified by this seat's re-runs and their clocks are written on the ARMED rows' own remediation rows (row C-S4). W10-S5's finding and remedy are W6-S5's remediation row (row C-S5), which names both scripts.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v1.md rows ADVI_COTBKF-W6-S4, -W10-S3, -W11-S3 and -W6-S5 (co-committed)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md (co-committed)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-S4",
      "ADVI_COTBKF-S5",
      "ADVI_COTBKF-S6",
      "ADVI_COTBKF-W10-S5"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is evidence for, or a duplicate of, a row that carries the clock and the remedy; a second row would count one item twice."
  }
]
```
