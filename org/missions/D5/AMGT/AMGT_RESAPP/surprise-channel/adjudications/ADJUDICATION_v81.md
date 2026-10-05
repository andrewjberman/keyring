# AMGT_RESAPP -- ADJUDICATION v81 -- pass-2 reconciliation disposition (12 never-adjudicated ARMED items)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~02:1xZ

Twelve ARMED items had no disposition, so the instrument read them UNDER_INVESTIGATION, and a remediation row alone does not move
that. This carrier GRADUATES them: Z-S62, Z-W60-S2, Z-S63, Z-W42-S2, Z-C-S412, Z-W58-S1, Z-W39-S5, Z-C-S413, Z-W53-S1, Z-W119-S1, Z-W53-S2, Z-W117-S4. Each has a DISARMED, REMEDIATED row in REMEDIATION_v15.

Z-C-S412, the served-output incident, was re-read live on the current build: 12/12 HTTP 200, 210 served, 0 spanless.

## The 26 stale rows advanced in place (clocks only); their evidence

| row | file | disarm at | evidence |
|---|---|---|---|
| `Z-C-S49` | REMEDIATION_v5.md | 2026-09-15T02:37Z | bc577af946 (ancestor of HEAD, 2026-09-15T02:37Z): ri-2 ledger CLOSE, 4 of 4 legs proven, the producer writes again ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-2.the-producer-consolidated-and-repointed.md last <status> complete |
| `Z-S10` | REMEDIATION_v5.md | 2026-09-15T01:29Z | infra/aws/terraform/harvest/dynamodb.tf:111-112 declares harvest_security_metrics (opal-harvest-security-metrics) in the one harvest root ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-2.the-producer-consolidated-and-repointed.md last <status> complete |
| `Z-S23` | REMEDIATION_v6.md | 2026-09-15T21:51Z | org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-3.the-exact-input-exercise.md and AMGT-re-1 last <status> complete ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.md: the real print route invoked for 5 names expecting 200, with a mixed-key regression arm; last <status> complete |
| `Z-S96` | REMEDIATION_v10.md | 2026-09-15T20:32Z | 0c4650dc1c (ancestor of HEAD, 2026-09-15T20:32Z): rj-10 drain, order COMPLETE 12 of 12 PASS-by-output ; HEAD reads: lib/research/metrics/chatter_axis.py:108 imports lib.research.coverage.pool_reader; scoped_amgt.py read_coverage_set reads pool_reader.coverage_items (the articles table retired); infra/aws/terraform/harvest/chatter-axis-schedule.tf:77-97,128-141 grant the pool prefixes |
| `Z-W34-S1` | REMEDIATION_v13.md | 2026-09-19T02:28Z | org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-59.plan-tolerates-absent-zip.md last <status> complete ; 6fdfe5b25e (ancestor of HEAD): the chatter function now deploys through modules/yang-lambda from a versioned S3 object (chatter-axis-schedule.tf:43-55); git grep finds no filebase64sha256( call and no .build/ path in any harvest .tf at HEAD 090ba579d3 |
| `Z-C-S50` | REMEDIATION_v5.md | 2026-09-11T22:24Z | org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-8.lead-panel-and-three-tabs.md last <status> superseded; TO-AMGT-re-1.lead-panel-recut.md last <status> complete (8d6c289dc8) ; The route evidence followed: org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-4.the-mount-deployed.md complete at 62d6daf36c (2026-09-15T04:07Z) |
| `Z-S5` | REMEDIATION_v4.md | 2026-09-11T20:46Z | COO half: aef0f33605 (2026-09-11T20:46Z, ancestor of HEAD) row Z-S20 discharges the cut-time live re-read (identity, access, configuration of the renamed opal-data-harvest bucket, old-name 404 control) ; adjudications/ADJUDICATION_v5.md (row adjudicating Z-S20) accepts the scoped S5 read obligation after renaming |
| `Z-W10-S1` | REMEDIATION_v6.md | 2026-09-12T00:41Z | org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-1.the-cross-at-the-producer.md:137 AC3 copies the file to a scratch snapshot before the mutant, and the rule requires restoring from it with byte identity proven by cmp ; The index-restore shape survives only in terminal round-6 re-1 AC3 (TO-AMGT-re-1.lead-panel-recut.md:139, last <status> complete) |
| `Z-S102` | REMEDIATION_v11.md | 2026-09-15T07:40Z | 0801a7d48c (2026-09-15T07:40Z, ancestor of HEAD): the notifier prints a failed re-offer; .tools/prd-header-notify.py:793-798 'RE-OFFER FAILED ... last_error' cites this row; :685-688 prints SEND FAILED on a first-send error ; Residual, not a refusal path: status() (:807-812) still prints UNSENT without last_error |
| `Z-W34-S2` | REMEDIATION_v13.md | 2026-09-19T02:15Z | org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-58.direct-act-minted-order.md last <status> complete ; .claude/skills/dispatch/SKILL.md:274-279 at HEAD: a co-signed DIRECT act is spawned with an order minted by .tools/direct-act-order.py from the signed pair, or not spawned; the minted order is the grant |
| `Z-C-S61` | REMEDIATION_v6.md | 2026-09-12T22:30Z | lib/research/api/tests/test_fiscal_scope_contract.py:180-182 at HEAD: the wrong string 'fiscal_year' must still match nothing ; Task orders TO-AMGT-rf-3, rg-1, rg-2, rg-3: last <status> complete |
| `Z-W2-S6` | REMEDIATION_v5.md | 2026-09-15T09:19Z | lib/research/metrics/chatter_axis.py:46-51, :161-166 and :274-300 at HEAD: POOL_UNIVERSE_PREFIX universe/v1/ is primary; DEFAULT_UNIVERSE_PATH is the fallback and its use sets source and fallback_reason on the provenance ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-5.one-store-the-two-readers-on-the-pool.md: last <status> complete |
| `Z-W10-S3` | REMEDIATION_v6.md | 2026-09-15T04:07Z | 50064d78f5 (ancestor of HEAD): ri-4 drain, 11 /api/scoped/amgt/* routes on 7k3ed8px20 (85 -> 96) ; Task orders TO-AMGT-ri-1..ri-4: last <status> complete; ledger 20260915T0345Z_amgt-scoped-api-mount_deploy_completion.md closed at bd5bad4156 |
| `Z-S67` | REMEDIATION_v9.md | 2026-09-14T15:10Z | org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round10.md:31 at HEAD: 'NEGATIVE CONTROLS, run time: FWD-99 -> 0 FWD-0 -> 0 FWD-42 -> 0' ; 008ca40b6c (ancestor of HEAD): disarm row for Z-S67 by 1.0.0_SA_CTO~W, condition met at two rounds |
| `Z-C-S62` | REMEDIATION_v6.md | 2026-09-12T23:09Z | lib/research/api/scoped_amgt.py:1749 read_model_block returns _apply_corrected_overlay(block, security_key) (:1802, :1879) at HEAD; thesis/print readers call read_model_block (:2866, :3078) ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-4.the-corrected-overlay-bypass.md last <status>complete</status> (8ec7756a49) |
| `Z-S9` | REMEDIATION_v5.md | 2026-09-15T01:29Z | git ls-files infra/aws/terraform/amgt-resapp returns 0 files at HEAD; infra/aws/terraform/harvest/main.tf:46 terraform{} (:49 required_providers, :56 backend s3) and :63 provider aws are the only such blocks across the root's .tf files (Grep over harvest/*.tf) ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-2.the-producer-consolidated-and-repointed.md last <status>complete</s |
| `Z-W2-S7` | REMEDIATION_v5.md | 2026-09-24T05:17Z | 6fdfe5b25e (ancestor of HEAD, 2026-09-24T05:17Z): chatter-axis Lambda moved to modules/yang-lambda; the artifact of record is a versioned S3 object carrying content-sha256 metadata read as source_code_hash ; infra/aws/terraform/harvest/chatter-axis-schedule.tf:43-55 at HEAD: build_zip.py builds, build-and-upload-chatter-axis.sh uploads, BUILD AND UPLOAD FIRST, THEN PLAN; prior versions stay in the |
| `Z-S27` | REMEDIATION_v6.md | 2026-09-12T22:48Z | 62d6daf36c (ancestor of HEAD): AMGT-ri-4 deployed the mount, 19 added 0 changed 0 destroyed; infra/aws/terraform/harvest/scoped-amgt-api.tf:265-267 grants dynamodb Query/GetItem/BatchGetItem ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-2.the-mount-and-its-iam.md last <status>complete</status> |
| `Z-S70` | REMEDIATION_v9.md | 2026-09-23T04:36Z | portal: refs/drains/rg-1-portal 83995ea977 and rg-2-portal a845a8be75 are BOTH ancestors of origin/DEV (2e7c5cdb) and origin/PROD (c69b4747) and of the CLOUD gitlink ec65c5d637 (merge-base --is-ancestor; positive control origin/DEV on itself YES) ; portal 1193bed8 (2026-09-23T04:36Z) is the oldest origin/DEV first-parent commit containing both drain refs |
| `Z-W27-S10` | REMEDIATION_v13.md | 2026-09-19T09:20Z | lib/research/api/scoped_amgt.py:5824-5838 at HEAD: len(rest) >= 3 and requested = _route_security_key(rest[1:-1]) ; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-61 complete at 6a3d2bb4ff; ADJUDICATION_v14 commit 913a02de36 ratifies rk-61 AC2 |
| `Z-C-S7` | REMEDIATION_v1.md | 2026-09-11T10:42Z | adjudications/ADJUDICATION_v3.md#AMGT_RESAPP-Z-C-S18 (13ae38f3f8): L9 grades AMGTrb10-AC5 PASS ('[WARN] 12345 [PROVISIONAL]', status before the number) and AMGTrb15-AC4 PASS (16 of 16 combinations match the co-occurrence contract) ; the round-2 attempts r-10/r-15 had FAILed at L9 (adjudications/ADJUDICATION_v2.md#AMGT_RESAPP-Z-C-S11); the rb- recut is the fix that passed |
| `Z-W1-S7` | REMEDIATION_v5.md | 2026-10-01T09:39Z | 842a3fcdb2 (ancestor of HEAD): .tools/halt-gate-check.sh:73-89 at HEAD resolves the serial from (1) the tree's own session file, (2) OPAL_AGENT_SERIAL in the environment, (3) the shared checkout's session file -- a worker can declare identity without any write ; task-orders/AMGT_RESAPP.TO-AMGT-rd-1.article-store-table.md last <status> complete |
| `Z-S21` | REMEDIATION_v5.md | 2026-09-12T21:43Z | git -C portal ls-tree -r --name-only 83cc87f29d -- src/pages/SecurityAnalysis / wc -l -> 18; at the HEAD gitlink ec65c5d637 -> 77 ; portal: e6057f26 is an ancestor of origin/DEV and origin/PROD (read 2026-10-04) |
| `Z-W11-S1` | REMEDIATION_v7.md | 2026-09-12T21:43Z | bb9009c924 (ancestor of HEAD) drain(AMGT-rf-6): the gitlink moved to 83cc87f29d, which contains c67281460a ; the row's own disarm read: git -C portal ls-tree -r --name-only 83cc87f29d -- src/pages/SecurityAnalysis / wc -l -> 18 (not 0); at the HEAD gitlink ec65c5d637 -> 77 |
| `Z-S72` | REMEDIATION_v9.md | 2026-09-15T01:51Z | investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S94: populated list of 10 tickers, BABA_US_Equity thesis with 183 fiscal figures and 40 PROVISIONAL markers, empty-state string absent on that arm ; the navigation half (ranked-row click landing on an UNRESOLVED identity) was carried by Z-S95, remediations/REMEDIATION_v10.md#AMGT_RESAPP-Z-S95 DISARMED by 5d3a04cab6 |
| `Z-S169` | REMEDIATION_v13.md | 2026-09-19T02:57Z | .tools/surprise-row-gate.py:1294-1305 and :2532-2542 at HEAD: beside the open-order census, the slug-time note prints 'ACCEPTANCE (round N): PASS / FAIL / UNVERIFIABLE of N' per criterion ; task-orders/AMGT_RESAPP.TO-AMGT-rk-57.acceptance-read-at-l10.md last <status> complete |

## Notes

- `Z-S230` (REMEDIATION_v14): CTO ruling AMENDMENT 1 @1696185649 corrects the premise. The pre-fix fingerprint printed username, pw_len and a 48-bit unsalted sha256 verifier, so rotation IS owed. It is carded to Andrew, and the row stays ARMED until the rotated secret passes a daily fire.
- **Three rows the instrument cannot move, all disarmed in fact:**
  - `Z-C-S412` and `Z-C-S413` are CVO adjudication rows. `comp-surprise.py:228` reads such a row by its own disposition only.
  - `Z-S11`'s remediation row was written INERT, with no disarm block, for an ARMED item.
  - Named for the tool's owner.

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S456",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-05T02:10:00Z",
  "one_line": "Pass-2 reconciliation disposition: the twelve ARMED items that were never adjudicated are GRADUATED; each carries a DISARMED, REMEDIATED row in REMEDIATION_v15 on a named commit or read. Z-C-S412 (the 179 spanless sentences incident) re-read on the current deployed build: 210 served, 0 spanless.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "remediations/REMEDIATION_v15.md rows for each id adjudicated here",
    "lambda:Invoke opal-amgt-scoped-api GET /security/<12 names>/thesis 2026-10-05: 210 served, 0 spanless"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_RESAPP-Z-S62",
   "AMGT_RESAPP-Z-W60-S2",
   "AMGT_RESAPP-Z-S63",
   "AMGT_RESAPP-Z-W42-S2",
   "AMGT_RESAPP-Z-C-S412",
   "AMGT_RESAPP-Z-W58-S1",
   "AMGT_RESAPP-Z-W39-S5",
   "AMGT_RESAPP-Z-C-S413",
   "AMGT_RESAPP-Z-W53-S1",
   "AMGT_RESAPP-Z-W119-S1",
   "AMGT_RESAPP-Z-W53-S2",
   "AMGT_RESAPP-Z-W117-S4"
  ],
  "spec_asserts": "L10: every BLOCKING or ARMED row is dispositioned.",
  "world_is": "The twelve were armed with no disposition; each now graduates onto a remediation row that reads DISARMED.",
  "notes": "Carrier only; the remediation evidence is in REMEDIATION_v15."
 }
]
```

-- 3.0.0_SA_CVO~Z
