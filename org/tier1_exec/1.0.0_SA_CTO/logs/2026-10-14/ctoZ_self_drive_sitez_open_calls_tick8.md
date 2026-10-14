# self-drive sitez open calls -- ticks 7-8 (2026-10-14 02:51Z and 03:51Z), `1.0.0_SA_CTO~Z`

arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md` @ce0ba39d90
state: ARMED   cadence: 60m (cron :41)   ticks covered: 7 (quiet, line carried from `org/mcp/drive_ticks/`) and 8

## Measurements (03:51Z)

- inbox: 0 unread.
- open calls on sitez: 44 rows, 10 OPEN, all `act`, unchanged since tick 4.
- sequence-check: no DRIFT and no OUT-OF-SEQUENCE.

## Calls ruled since tick 6

| call | ruling | carrier |
|---|---|---|
| r30 C3 re-sign (O 33901) | RE-SIGNED at 92698aea8c on live b0c75d24f1; patch-id eac7550c45 = v1 | @1003665c3d |
| call a63a: R20 for 6 hyphenated harvest tables | NOT R20. Six legacy_addresses.json READ rows (lib/opal_naming.py:794; ADVI_COTBKF precedent) | @d5e0b1a0b6 |
| the naming gate does not read legacy_addresses (MI 33935) | NFRA_MCPINDEX lands one judge() branch (LGIC_ENFORCE CLOSED). Laptop CTO: no objection, 3 conditions. dell1: none by ~03:40Z, so the window lapsed and the merge may proceed | msgs to COO~MI |
| YCharts WAF (dell1, 33907) | site Z pause on ycharts_* until the probe; recovery = a person's human-verification pass, then an OPLGTW secret write. Self-recovered 02:23Z; pause lifted (33921) | msg to MSTR~Z |
| OG-mg-1: Andrew's profile ends his BD-fee access (O 33940) | (a): tier admission holds on the profiled branch too; a one-line cell after r30, before OG-mg-1 Phase B | msg to COO~O |
| MC Portal C17 round-2 slug (CVO 33944) | C17 REALIZED (1.3 s); Z-C-S31 three-state display; PRD v0.8 adds FWD-21 (control and depth per person) and FWD-22 (Claude account + 5h/weekly usage per box); C18: one grant writer, deploy files as floor. ADMITTED (CVO ce592cd443f6) | @d0dd3f0964 |
| MX-r-12 CTO half (MI 33948) | SIGNED; MC Portal's breakdown-reader change named, bound by equal link counts | @0312862e0f |
| C18's gateway side (CVO 33950) | NFRA_OPLGTW v2.9 C-PERSON: decide() reads the per-person record; OPLGTW cuts the reader; MC Portal F2 waits on it | @e5e2ce91ec |
| C-PERSON summary vs text (CVO 33957) | the text governs: a record may widen a person to a floor-listed tool; F2 exercises one narrowing and one widening; COOs corrected | msgs 33958/33959 |

## ACTS ONLY ANDREW (OR A PERSON) CAN DO -- 10 OPEN rows, unchanged (see tick 6)

The most time-bound: row 6c9f, the R2/R3 hold-lift yes or no. R2 is reverted at 10:30Z with no answer.

## Completion test

NOT DONE. Stop: Andrew's stand-down.

## Compiler Tools

`check_inbox`, `.tools/open-calls.py list|close|publish`, `.tools/sequence-check.py`, `.tools/prd-signoff.py status`
(NFRA_OPLGTW, NFRA_MCPORTAL, NFRA_MCPINDEX), `git patch-id --stable` (r30 v1 vs v2), the blob-equality check per file
(MX-r-12), `comp-find` (the legacy_addresses readers), `s3api head-object` (live-base agreement). Gap: one Bash read stalled
past 120 s (the open-calls list plus `ls -t` on the read dir) and finished in the background with full output; no data lost.
