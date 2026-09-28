# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE), `/canonical-drive 10m` (cron 34a39a73; LIVE_ARMS RELAUNCH row). Workstream scope:
shared auth, routes, IaC and packaging, plus Performance/Reporting. Also issuer of workstream ~E (CTO ruling 102461).
As of 2026-09-28T23:2xZ. The A2 freeze of this file is @025cef10fd; earlier forms are in git.

## Standing Andrew words that govern this workstream (read first)

- **~22:2xZ call 3** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md`):
  performance is end-of-day holdings only -- the weight-pro-rated daily price return of the securities held, no
  inflow/outflow logic.
- **~22:4xZ** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`):
  every firm (49F, INF, COT) moves to that basis, in ONE consolidated gold shape the page reads, run daily, verified at
  the vendors' official periods. Sequence: CRO L1 inventory brief -> CTO L4 addendum (an ENDPOINT change; CVO
  re-signs) -> COO decomposition. Cottonwood per-use vendor plans are no longer the path.

## Served function -> deployed artifact -> source commit (live CodeSha256 read at each move)

| Function | Live CodeSha256 | Applied (Z) | Source | Ledger |
|---|---|---|---|---|
| irpt-performance-adapter | `hcZpXDDofuUX2YImni0nsCDyLOxHl2Mxc1IvEBwG0+0=` (S3 wVW7wVQw) | 09-28 22:02:49 | entry.py + f49_engine.py @57a58117fb (NEW-01 guard); other 67 pins as F0bYtOfB | irpt-adapter-implausible-guard-20260928 (U1 closed; D1 OPEN) -- rollback G4UtfeeR |
| irpt-export-render | `BORQ2shbblG4OIG387kkAKTxUUtbPhw6LoLVx0mqGM4=` | 09-28 12:51:49 | export/entry.py @5c0185fee2 | irpt-export-receipt-running-20260928 |
| irpt-ycharts-generate | `AdE17rT6f3IZKuh/VWMLTB+HuCZql50ZJzZXUYs90e8=` | 09-28 13:11:54 | generate_installed @2e3d50caac, publication @c1fd6c5e52, maintained_sources @15b9f85eb3, templates @6096ee740b | irpt-generate-resident-grant-20260928 CLOSED |
| Resident (i-0167fd745ad906a66) | root `/opt/irpt-resident/fe64236bbb-st2` | 09-28 13:17:56 | as generate | same, CLOSED |
| irpt-status | `ZYr+IDMpN0vtwnpxz+kOXKDMcjNpLrbbHdRm4TZerkY=` | 09-28 14:04:55 | publish @6389be7a9b; IAM @75df934b23 | irpt-status-dates-rebuild3-20260928 |
| irpt-directory-search | `o1TXq5PH1+/VVff+hf4U+b+H6Kf1VCJkUJJjAaN+y7Q=` | 09-26 22:54:06 | @49b935c213 | irpt-uir07-search-rank-20260926 CLOSED |

All source commits are on CLOUD (MSTR act-4 drain @c161a2faca; B3 row S178). Nothing here is pushed.

## Open ledger entries (CLOUD `org/critical_paths/.open_deploys/`)

| Entry | Open leg | What closes it |
|---|---|---|
| irpt-adapter-implausible-guard-20260928 | D1, A1 | CRO D1 NOT MET @5f82151a2e: the page reopens RETAINED reports, so NEW-01 1Y still reads -100%. Closes after IB-pr-194 (the reopen guard) is served and a walk shows the named refusal |
| irpt-adapter-render-grant-kms-20260927 | A1 | the render's Performance read succeeds, READY %PDF |
| irpt-adapter-render-selection-20260927 | A1 | the same read answers (no SelectionRefused) |
| irpt-export-async-submit-20260927 | A1 | one POST QUEUED -> READY %PDF or a named FAILED |
| irpt-export-receipt-running-20260928 | A1 | a pending receipt reads RUNNING and the page polls to READY |
| irpt-export-reopen-rule-20260927 | A1 | a second in-scope principal exports READY; a principal missing one account is refused |
| irpt-status-dates-rebuild3-20260928 | A1 | the page reads REQ-67e12718 READY PER_SECTION |

## Round 19 (workstream ~P; decomposition section 13, 13.1)

| Order | Cell(s) | State |
|---|---|---|
| TO-IB-pr-191 | IB-pr-191 (NEW-01 guard on compute) + IB-pr-194 (the retained reopen guard) | REOPENED @b6e0525927 to slot ~63; 191 served as hcZpXDDo; 194 built @90c4b596f3, proof pending |
| TO-IB-pr-192 | IB-pr-192 (Since inception from the first data point) | pending on slot ~61's branch; AC1 PASS, AC2 FAIL live (row W61-S2); now governed by the consolidated-gold sequence |
| TO-IB-pr-193 | IB-pr-193 (async export log REFUSED) | complete, merged @b02d1e9097 |
| TO-IB-s158 | IB-sr-1 (COT BD session auto-login) | complete |
| TO-IB-er-191 (workstream ~E) | IB-er-191 (holdings-based 49F engine) | CANCELLED @06d66b5893 by Andrew-direct ~22:4xZ; 0.4.0_DS_ClientPlatform~E halted, nothing written (102466) |

## Acceptance (goal done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | Performance: no firm has a complete report on the page (CRO walk 17:49Z; AD-14). 49F NEW-01 still -100% on retained reports (D1 open). Analysis READY once -- cottonwood, REQ-67e12718 (corrected by ~Y 102408; previously written here as 49F). Export reaches the render; READY needs the K8 window |
| 2 | Every active account resolvable | MEASURED 09-28 AM: COT 843/843, INF 878/878, 49F 6698/7497 |
| 3 | COT structurally sound, window disclosed | MET on RPT-12b885b8 (actual 07-21..09-21) |

## Named dependencies (AD-14)

- **COT** (row S185): every fresh Cottonwood window needs a server-approved one-use Black Diamond plan; none is armed,
  so the adapter refuses VendorEgressRefused before any vendor call (154 refusals 13:30-22:30Z). Superseded as a fix
  path by the ~22:4xZ Andrew-direct (holdings basis for all firms).
- **INF**: InflectionMappingRefused, "account not individually addressable: its Orion household holds 4 accounts" (49).
- **49F**: WindowNotRuled for 3Y / Since inception (36); NEW-01 on two retained reports.

## Next-list, in priority order

1. **IB-pr-194 served move:** drain slot ~63; packet (both readers of the served figure counted: compute AND reopen);
   both halves; apply; CRO walk shows NEW-01 1Y and YTD as a named refusal. Closes ledger D1.
2. **Consolidated holdings gold:** the ~P share of the COO decomposition once the CRO brief and CTO L4 addendum land;
   ~E's 49F slice is re-cut then (DS~E's facts are with the CRO: 99.2% priceable, prices in canonical_positions,
   W61-S2's cause is a calendar gap).
3. **The live window packet** (one principal, both halves): K4 window 15 Dollars CSV; K5 one Comparison
   (opal_long_term); K8 export (closes the five export/adapter A1 legs); K10 the page reads REQ-67 READY; ~Y's arms
   (Y2 XLSX, Y2 Target Weight, one INF Overview, one 49F Overview, a deliberate mid-job credoff revocation).
   Precondition: the next resident + generate build carries ~Y's recipe.py + resident_worker.py @ec8f69f718.
4. **Branded Analysis export** (~Y R19_Y AMENDMENT 2; ~Y supplies the AnalysisReport schema and owner shape).
5. **Hygiene:** W62-S1 (export suite red `test_the_marked_event_builds_and_the_handle_reaches_the_receipt`,
   pre-existing); the tree-order template's short proof_of_spec name (W61-S1); build-and-upload deleting tracked
   performance/*.py; the directory Terraform root predating ~M's holdings resources.

## Andrew acts in flight

None at this lane. No one-use plan is armed on the adapter.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| Kept test inputs and reports from windows 1-6 in cottonwood, RPT-b683f188, spent claims PERFORMANCE_USE#63cf95e9 / #b20d69b2 | the release cutter | the route opens to firm users |
| Row S175: MaintainedSourceRefused maps to UNEXPECTED | 2.0.0_SA_COO~M | the next maintained_sources.py change |
| Row S184: 2 near-miss invested accounts (-0.9996, -0.99996) keep ~-100% | the consolidated-gold decomposition | the holdings basis replaces the flow engine |

## Gates in force

- Every served zip: flat_zip_module_census + ~Y zip_module_census + a cold-start smoke (with /var/task mapped on this
  host; the ~Y smoke is non-discriminating here) BEFORE apply.
- A before/after read that DISCRIMINATES on the served surface, counting every reader of the served figure (compute
  and retained reopen); a refusal-only read does not count.
- Served moves need both never-widen halves at HEAD naming the packet blob.
