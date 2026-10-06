# MDPF_SECCLASS -- one canonical security classification -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Contract `org/standards/MDPF_SECCLASS_CONTRACT.json`. Reviewer `3.0.0_SA_CVO` (not
seated at the boundary; a CVO deliverable appeared on CLOUD at ~06:2xZ). As of 2026-10-01T06:5xZ.

Mode: FAST. Lease `MDPF_SECCLASS`, `org/mcp/drive-mode.log` line 36, until 2026-10-01T13:39Z, on 1.0.0_SA_CTO
DECISION 103498 (a) under Andrew-direct 2026-10-01 ~04:2xZ (record @c48af273cc). No round-6 analysis is written; the
round-7 list is built directly. FULL -> FAST boundary: no worker was running; nothing was cut; one order stays
`parked` (TO-SC-e12); round 6's drain-end packet is
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/2.0.0_SA_COO~M/DRAIN_END_R6_20260930.md` @2744a9fc57.

Claim words: `measured` = read this session; `held` = cited from a record, not re-read.

## Pins

| What | Value | Claim |
|---|---|---|
| Working branch / worktree | `coo-m-r30` at `../coo_m_r30` (shared with IRPT_BCKEND~M; disjoint files) | measured |
| Live table `etf-classifications` | 2,309 ticker rows + 348 `CUSIP:` rows | held (session log @9f8fd81494) |
| BD thread code live on `s3://opal-data-bd/code/` | the rolled-back, pre-window versions; C_06, D_03, D_04 read STALE against CLOUD (`comp-pipescript deployed --firm bd`, 05:2xZ) | measured |
| BD_THREAD_R3 half | COO + CTO SIGNED @8769ffe8d5; the nine candidate files' md5 at HEAD equal the signed values; the act's inputs are unchanged since the CTO's signing HEAD 53f971d7a6 | measured 05:4xZ |
| Silver document `opal-bd-asset-dim-download` | the bytes to publish: sha256 d3a38c7b...d3f407, 10,840 bytes (`git show HEAD:`) | measured |
| W12-S1 fix | 9053ffba73: `seed-etf-classifications.py` `merge_item` drops the two model-only fields; `MDPF_SECCLASS_M/R7_CHECKS/test_seed_model_correction.py` 4 passed | measured |
| Lane grant | `.owned-paths.yaml` @b73706a584 (CTO 103507): this seat on exactly the lease's six code files; code only, no deploy grant | held |

## Live thread

FWD-1 (one security reads one class from the canonical table, to the page): LIVE for Investor Reporting Holdings since
2026-09-30 (narrowed release); NOT LIVE for the Black Diamond pages (the thread code is rolled back). First failing
hop: the BD gold scripts on the runner, which the BD_THREAD_R3 window redeploys.

## Write claims

None open (W12-S1 landed @9053ffba73).

## Next proof

BD_THREAD_R3: C_06, D_03 and D_04 import and run on the real runner from `code/gold/lib/_shared/`, then the first
scheduled gold fire and the first 22:10Z silver fire accept it, then the page read for relationship `z08327149`.

## Next-list, in order

1. **BD_THREAD_R3 window: IN FLIGHT.** Ledger `secclass-bd-thread-r3-m-20261001` (opened 06:09Z @8fc4150c9f).
   Legs P, S1, L0 CLOSED @4f10007bde: the six thread files and three shared modules are on
   `s3://opal-data-bd/code/` (ETag equals the signed md5 on 9 of 9, deployed 06:11-06:13Z) and silver document
   version 5 is live (06:16Z). Leg X: the exercise run was fired 06:33:00Z through `bd-gold-trigger`
   (`mode incremental`); it reaches C_06 about 70 minutes in and ends about 08:40Z. Restore targets:
   `MDPF_SECCLASS_M/BD_THREAD_R3_PRIOR_VERSIONS_20261001.json.gz` @c6c769bb3d (53,927 keys) and the six code
   VersionIds in leg P. If C_06, D_03 or D_04 refuses at import, the code rollback runs in the same gap. Then
   A2 (22:10Z silver fire), A1 (23:00Z gold fire), B4 (the page read for z08327149).
Items 2-8 are in the order of 1.0.0_SA_CTO's round-6 answer
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_6_20261001.md` @453c6430ec, section 3),
on 3.0.0_SA_CVO's review `org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md`.

2. **W12-S2: DONE on CLOUD @a96e00c279.** `ETFClassifier.classify_holdings` no longer raises KeyError on a class
   beyond the four it seeds (the client and its two copies; 7 tests). The Black Diamond copy trails CLOUD by this one
   line in a method with no caller; it catches up at item 4's deploy.
3. **Ruling 5, row W10-S3: MEASURED.** `.tools/test_safe_deploy.py` reads 7 failed, 7 passed at SC-e13's parent
   and at HEAD, the same seven tests: SC-e13 caused 0 of 7. All seven come from the 2026-08-30 index-blob change
   (`3d9eb2931d`); owner the deploy tool's lane (`0.7.0_AE_CloudOps`, dark). Record:
   `MDPF_SECCLASS_M/RULING7_STALE_ROWS_REMEASURE_20261001.md`.
4. **E_18's trigger (row W10-S2): DEPLOYED 08:41:28Z, acceptance OPEN.** `s3://opal-data-bd/code/gold/gold_dispatch.sh`
   serves commit 6f4bde6b6a (ETag `d6ab7998...b171`, VersionId `VikjYXAE...`; prior `Ar2kBAqt...` is the rollback
   target): E_18 runs between B_01b and B_02 (`PHASE_B3b`, non-fatal) and the calendar guard sits behind
   `GOLD_CALGUARD_ENABLE`, unset. Both halves signed @985bae1fee. Ledger `secclass-e18-trigger-dispatcher-m-20261001`:
   P and D closed, A open. Acceptance, read from the log of the 23:00Z fire (and every proceeding fire until the round
   closes): `E_18 done (rc=0)`, `PHASE_B3b complete`, 0 `CALGUARD` lines, chain exit 0, written / refused equal to
   the table's gain. A stop between PHASE_B3b and PHASE_B4 rolls this back first; the first row E_18 writes is
   compared with the fallback's class. Black Diamond only (Cottonwood's dispatcher and an Inflection caller: row S2).
5. **Ruling 3: DONE on this branch @1617619a6a.** The census prints, and writes only with `--write <path>`.
6. **A canonical row for `CEMIX`: WRITTEN 09:17:42Z; the served read is at 14:15Z.** Both halves signed @37ac46eed2.
   Ledger `secclass-cemix-canonical-row-m-20261001`: W closed (1 row written, table 2,657 to 2,658, second dry run
   0 of 139) and R closed (a local Cottonwood build after the row: 97 of 97 CEMIX nodes equity / EM, 0 of 1,508
   other symbol groups changed); S open -- at the 14:15Z `irpt-holdings-snapshot` publication one Cottonwood
   selection reads CEMIX under Equity and the class totals tie. The rule behind the wrong class is row S7.
7. **Ruling 7: DONE.** The six stale rows are re-measured in
   `MDPF_SECCLASS_M/RULING7_STALE_ROWS_REMEASURE_20261001.md`: four recommended closed (S1, W2-S3, W5-S2, and W3-S3
   once leg A1 passes), two stay open with an owner and a condition (S2 narrowed to this seat's trigger cell plus an
   Inflection caller; W6-S2 on the parked AE order).
8. **Ruling 6, row W11-S1: DONE @d67a10fc01.** `_shared/tests/test_classified_by_v2.py` pins contract 0.3.0 and the
   five `classified_by` values exactly (17 passed; on a 0.4.0 contract with a sixth value the two pinned tests fail).
9. **MODEL_ROWS: 13 rows WRITTEN 11:05Z; two served reads open.** Both halves signed (CTO for 13 rows, CAIBX
   excluded, @000b55fc4b). Ledger `secclass-model-rows-m-20261001`: P closed (census `MODEL-READER-TOLERATED`,
   readers=36; dry run 13 of 13) and W closed (13 of 13 written; table 2,671; each row carries both model fields;
   second dry run `plan=0 already_present=13`). Open: H, the next Holdings publication serves the moves of addendum
   2 (set b moves a class on 706,570.47 USD at Inflection; set a moves the sub class on 5,801,070.93 USD), and G,
   the next Black Diamond gold fire reads six held tickers (57 lots, 518,062.80 USD) with a class. The thirteen
   withheld tickers (eleven low-confidence, O, CAIBX) each need a seed row under its own half or stay on the
   fallback; O is served a wrong class today (fixed_income for a REIT stock, at all three firms), and PCOFX is served
   correctly -- it was the model's answer for it that was wrong, and withheld. REET against VNQ is row S8.

10. **MDPF_HEALGAP cell 1 (CTO 103641; rulings batch 72 and batch 75): built, half signed by this seat, CTO half owed.**
    Not this project. Its state is `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_M/STATUS~M.md`: the
    catch-up module and 16 tests are on CLOUD and wired nowhere; the live read-only plan is the ruling's five dates;
    the call line and the Lambda package row are `4.0.0_SA_CRO`'s.

11. **The Cottonwood thread (row IRPT_BCKEND-S173; CTO rulings batch 86 items 5-8): IN HAND.** Ruled (a): Cottonwood
    gold classes from the canonical table only, no name pattern, no ticker shape; what the table lacks reads
    unclassified. Done: the library `data/cot/scripts/gold/lib/etf_classifier.py` @398a0ce84c (serve-held, 7 tests);
    the measurement `MDPF_SECCLASS_M/COT_THREAD_UNCLASSIFIED_MEASURE_20261001.md` -- of 554.6 million USD, 205.1
    million (37.0%) would read unclassified: 101.3 million with no ticker (held-away and manual assets) and 103.8
    million in 271 tickers the table lacks, the top 25 carrying 84.3%. Next, in order: (i) rows for the top tickers
    FIRST, each a seed row with its ground or a model row with a seed peer, under its own half (item 6);
    (ii) the three callers' rule for an unknown ticker and for a holding with no ticker (C_06, D_03, D_04);
    (iii) the host role's read on `etf-classifications` only and the shipped-artifacts entry -- two exact-file
    grants asked 12:55Z; (iv) the half for the re-point, naming the residue; (v) Cottonwood's scheduled E_18
    step, under its own half (item 7). It disposes the two ledger entries held since 2026-09-25/26.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| The exercise run ends | the run fired 06:33:00Z | EC2 state of `i-01003b035d2988dfb` and its log on `s3://opal-data-bd/logs/gold-layer/` | AWAITED: a watch is armed |
| Andrew's call: may a per-firm value FILL an absent `instrument_kind` on an existing row | Andrew (CTO 103218 routed it) | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_192xZ_INSTRUMENT_KIND_NO_FIRM_FILL_AI_CLASSIFIER_FILLS.md` @b9e5d795c8 | CLOSED 2026-10-06 ~19:2xZ, Andrew: no. A firm's own label never fills `instrument_kind`; only the AI classifier fills a blank one (it lands without review and is listed in the AI-landed index). Relayed by 1.0.0_SA_CTO msg 105702. |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| "FAST from 2026-10-01T05:39Z; pins graded after the fact" (the boundary's one line to the CVO); round 6's three issuer-amendment deviations are in the drain-end packet | `3.0.0_SA_CVO` | a CVO is seated; it reads this row |
| TO-SC-e12, the shared-infra bd-securities grant narrowing | `0.7.0_AE_CloudOps` | that seat is live (CTO 103327) |
| `.tools/test_safe_deploy.py` fails 7 of 14 before and after round 6 (row W10-S3) | owner of `.tools/safe_deploy_core.py` | its next change |
| `test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged` fails on CLOUD's unmodified script (row W11-S2) | owner of `seed-etf-constituents.py` | its next change |
| The live bytes of the `bd-asset-dim-trigger` Lambda are unread (the half is sound under either reading) | `2.0.0_SA_COO~M` | item 1's ledger reads them |

## Limits

Item 1 is a served move and is not run. The W12-S1 fix is a local script change: no table row is written by it, and
no live row carries the defect (0 model rows in the table, held). No product ID is PASS until the CVO grades a
pinned candidate. No S3 delete runs under the BD_THREAD_R3 half (CTO condition 3).
