# IRPT P -- STATUS at 2026-09-24 09:4xZ (2.0.0_SA_COO~P)

Goal (Andrew-direct 2026-09-23 ~22:4xZ): Investor Reporting Performance done end to end and linked
up for every firm client at 49 Financial, Inflection and Cottonwood; Cottonwood structurally sound
with its ~May-2026 data window disclosed. Loop: 20 minutes. Every number below is from a receipt in
this directory or a message id.

## Served (each a ledgered act: sentinel -> plan -> safe-apply -> readback -> re-plan -> recorder)

| object | pin / revision | at (Z) | carries | receipt |
|---|---|---|---|---|
| irpt-holdings | kZygK57yXxZBaC3t5Wr+y04tDKx6tDJdjCwPm87kdYE= | 06:00 | B1/B3 loaders + B7 served (05:04); schema copy b3e3bcb044 (`display` + CUSTODY_UNITS) | HOLDINGS_SPEED_APPLY, HOLDINGS_SCHEMA_APPLY |
| irpt-directory-search | o9Qu0Jm7jidtrlBeGWD9d2ZsxROK3NXcQTEOUOMvGus= | 05:16 | listing speed (04:21) + keep-warm rule, three targets, 500 ms hold; three containers seated per tick | DIRECTORY_SPEED_APPLY, DIRECTORY_KEEPWARM_APPLY |
| irpt-performance-adapter | 07lSH03z53irjBk3AkX2upzUuWzVd4QOuPA4JmisLss= | 06:36 | canonical 61-member shape; X10 ACTIVE row; hop 4b MRO walk + named retention codes; hop 3 SELECTION_UNSUPPORTED; hop 12 sink | PERFORMANCE_RECONCILE_APPLY, PERFORMANCE_X10_HOPS_APPLY |
| Holdings, all three firms (M's acts) | COT dec293d6 06:20; 49F 3d59c80b 06:58 + units 5a25ae76 09:0x; INF d03e91a4 07:04 + units d32e50c6 09:04 | | labels on every node the directory knows; CUSTODY_UNITS on every observed row | IRPT_MVP_M receipts |
| portal DEV | 013323f0 | 09:1x (MSTR) | candidates 1-3: consolidation, M's labels, hop 11, "Performance" tab, SELECTION_UNSUPPORTED named, F1 / F5 / F3 | CTO 100359 / 100463; MSTR receipts |
| the resident (this box's act) | package ab2e088b5b on i-0167fd745ad906a66 | 09:39 | irpt-analysis-resident.service ACTIVE, single consumer of irpt-generation, enrolled 1276035, tokenless transport, X10 ACTIVE row, census 44853788fa..; five empty polls, no vendor call | RESIDENT_INSTALL, RESIDENT_CUTOVER_EVIDENCE |
| irpt-ycharts-generate | uHfng41l/agHCG5OHldwqi2r+NUZKfu7DqmWvbqNhTc= | 10:24 | handler generate_installed.lambda_handler (the 8 production ports composed once per container, both branches refuse BY NAME as NOT_READY); sqs:SendMessage on irpt-generation; 0 event source mappings; IRPT_LIVE_YCHARTS_CALL absent; invoke {} -> 200 named refusal; does NOT move hop 2 | GENERATE_INSTALLED_APPLY |
| irpt-status | pfAr3uZEAjWWUNfcukhJYV+bWi1oxPUZzYKUE/NbztY= (was 5E8T+/LV.. 10:53) | 11:46 | handler status_installed.lambda_handler (build_owned_entry over the production readers; 5 operations, the two history routes on the function's own table); +GetObject on the four retained families (12 ARNs); the two table env keys; invoke {} -> CONTRACT_VERSION, unsigned history GET -> NOT_AUTHORIZED by name; routes.json publication is (iii) | STATUS_OWNED_HISTORY_APPLY |
| api root: the two owned-history GET routes | routes 7yo12g5, jjidb6b on 7k3ed8px20 | 11:06 | routes.json DECLARED against irpt-status (16 of 17 declared); apply 2/0/0, replan No changes, get-routes readback; signed-out probe 401 on route AND control (non-discriminating, stated); edge (a) mapped in ops/entry.py @e0f52fa041 -- SERVED 11:46Z by the irpt-status rebuild pfAr3uZE.. (STATUS_EDGE_A_APPLY) | HISTORY_ROUTES_APPLY |
| irpt-ycharts-generate + the upload route | 4fkloyC1HaICo2OboVZgSFSapRJQlM5+ErEKWm0SCnU=; route 0sp6wva | 11:21 | the boundary carries the analysis POST and the upload POST (UploadNotComposed: the real validator, then NOT_READY by name); routes.json 17 of 17 DECLARED; apply 0/1/0 + 1/0/0, replans clean; invoke {} -> CONTRACT_VERSION, unsigned upload -> NOT_AUTHORIZED; S123's positive control fired (the builder's SKIP notice) | UPLOAD_ROUTE_HOST_APPLY |

Directory listing: p50 2308 -> 160 ms, p90 4665 -> 634 ms, p99 6093 -> 972 ms (03:21-04:21 vs 04:21-05:21).

## The Performance thread (the CRO's trace @d8abd7dc65, hop by hop)

Hops 4a (X10 ACTIVE), 4b, 3, 10, 12 CLOSED at the deployed bytes (CRO 100381); 11 on DEV.
The ONE gate left before a number renders: hop 6, the one-use plan for acc_d486fc9455d6b2aa18e13af1
on the default window -- Andrew's per-use word. Then: install the plan, ONE calculation, retained
report, reopen without a vendor call, export.

## D1 -- the YCharts session: CAPTURED

Six credential submissions on 2026-09-24 (03:31, 03:49, 04:35, 05:55, 06:27, 08:56), each bounded to
one by the CTO's word. Run 7 (08:56Z) captured and persisted the bundle: identity from the signed-in
page's own document (user_id 1276035), the template route LIVE from the TOKENLESS Node client, and
the pair 200 (no WAF token) / 405 captcha (token presented) named the WAF token as the cause of runs
5 and 6. ycharts/session/current carries AWSCURRENT 02e53a44 (fence 11; CRO grade PASS 100463). The
stored-bundle probe (09:12Z, no sign-in) reads 200 LIVE with rc 0. Receipts: D1_RUN7_SIXTH_SUBMISSION,
D1_STORED_BUNDLE_PROBE.

Runner @b9d36bc34e (library dfc87d8312c5938c.., wrapper 55ddb8f7 unchanged) deployed. Resident
transport tokenless @8576bec142 (CRO STANDS 100477); the four resident files at Y's 93ec16f4fe.
Y is paused on a safeguards dialog (Andrew's model call); its reads were re-routed to the CRO by the
CTO (100425) and are welcome on return, not owed.

Rows: IRPT_BCKEND-S119 (bundle contract), S120 (Playwright under /root), S121 (the offline suite
reached ycharts.com once unguarded; the suite now refuses to start unguarded).

## Next at P (CTO batch 34 item 5 / batch 28 (i)-(iv))

1. The Analysis backend: (i) DONE 10:24Z (row above; the two revisions are DERIVED from the packaged
   registry and schema directory, not env keys). Hop 2 (the upload composition) is a design cell on
   the CTO's shape (100497 (b)); its two vendor-egress questions are carded to Andrew.
   (ii) DONE 10:53Z. (iii) server side DONE 11:21Z (the two rows above); the client flag is CUT as
   portal candidate 4 @310b83b8 (irpt-dev-candidate-4-20260924 from origin/DEV f7a4e47f; tsc 0,
   eslint 0, 0 suite failures introduced vs the base, 4 fixed; receipt PORTAL_CANDIDATE_4) and sits
   LANDED on DEV 310b83b8 by MSTR 11:44Z (fast-forward; VALGATE PASS). (iv): see the assessment sent 11:5xZ.
   S122 (the builder's silent exit) is REMEDIED on the trunk @bf938bcf39 (row S123).
2. Speed levers F7 / F2: held on a HAR from opalinvest.dev (the 04:32Z HAR was a localhost dev session).
3. Andrew's browser act (G) last.

## Standing constraints

Commits LOCAL (MSTR pushes); no vendor call without Andrew's per-use word; no synthesized trusted
header on a live surface; cookie values and credentials never printed; audited lane overrides only on
the CTO's word; the P/M/Y closer contract and the post-slug HOLD stand.
