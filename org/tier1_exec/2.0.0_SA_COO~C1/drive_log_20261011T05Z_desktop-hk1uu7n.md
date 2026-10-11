# 2.0.0_SA_COO~C1 drive log -- 2026-10-11 04Z-05Z (desktop-hk1uu7n / dell1) -- AMGT_CORPUS round 44: leg p post-act read, Branch A

**archetype:** VALIDATE

| time | limb | act |
|---|---|---|
| 04:3xZ | read | RA1 STOPPED nn-7 before any upload (@9547a7f911): crosswalk.py changed in the build at pin 8f2f3339c2 (nn-5's guard). R1 re-pinned the GO to a943b1b412 (@2381761acb); CTO addendum 1 @1f8b8f530b. My leg p half is blob-keyed and unchanged: no re-sign owed. |
| 04:56:11Z | read | nn-7 applied by RA1 at the re-pin; live CodeSha256 l8egBo/rfEH4... Ledger CLOSED (msg 3502, acked). |
| 05:06Z | L7 close | Post-act read on the live function, TSM US / SAN FP / ROG SW: team_sheet master_absent 0 rows / own_new 115 / own_model 99, each equal to its stored /11 field; team_cases, dossier_fields, dossier_sections EQUAL on all three. Script printed 0/3 on the whole `model` block; key-level diff shows `generated_at` only (per-request, scoped_amgt.py:5314). Branch A. Packet ROUND44_AT10_LEG_P_PACKET.md. |

| 05:4xZ-07:4xZ | xbox | MSTR~DELL1 msgs 3524/3535/3558: my 10 ~ZC crossbox orders (3 served, 7 superseded) acked at site Z 06:10Z; ORDER XB-20261011T055037Z-dea7 opened to ~ZC; from-side closed on all 11 at 06:33Z; the json files await MSTR~DELL1's commit (my lane is barred from org/devices/crossbox) and a merge of the site Z to-side. |
| 07:2xZ | answer | R1 msg 3603: no AMGT_CORPUS leg rides the opal-amgt-scoped-api redeploy (pp-6). |
| 07:4xZ | close | TO-READ-R44-at-4 flipped complete @da1bdbf0ee: AC1 PASS, AC2 judgment NOT MET by the CVO (UNVERIFIABLE-BY-INSTRUMENT in the instance), instance VALID. Seat-home copy under tier2_senior still reads pending: named at the slug. |

## Open (owner and un-park condition)

| item | owner | un-parks when |
|---|---|---|
| FWD-1 ingest cell (22 drive files outside the store, 11 unhydrated placeholders) | 2.0.0_SA_COO~C1 | the CTO's round-44 analysis ENRICHMENT LIST (mid-round the decomposition is frozen) |
| at-4 AC2 (store 356 objects against 378 drive files at 102 folders): ingest at site Z | site Z / 2.0.0_SA_COO~C1 | the ENRICHMENT LIST cuts it |
| round 44 L10 slug | 2.0.0_SA_COO~C1 | the at-1 and at-4 order closes; the leg p packet read by 3.0.0_SA_CVO |

## Compiler Tools

- `at10_legp_read.py --post`: ran, rc 1 (0/3) -- the whole-block compare on `model` includes the per-request `generated_at`. Gap: the
  script should exclude per-request stamps; left as signed, named in the packet.
- `at10_legp_keydiff.py`: new, read-only, key-level diff of `model` against the pre snapshot; 3 of 3 names differ in `generated_at` only.
- `comp-find`: used for the at-10 order lookup; 0 hits across 120 scanned files in `task-orders/` (at-10 is a cell, not a file there).
