# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` armed 2026-10-01T04:33Z until 12:33Z on Andrew's word
(record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`,
CTO 103441). Loop `/canonical-drive IRPT_BCKEND` 10m (LIVE_ARMS RELAUNCH row). Way forward: CTO rulings batch 61
@8dcf5bbe7a, ruled on the trace `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md`.
Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-01T05:2xZ. The version before FAST is at @5c19dcc1fe
(rounds 19 to 29, windows 22 and 24, the served-artifact map).

## Pins

| What | Value |
|---|---|
| Worktree | branch `coo-y-r30` at `C:/Users/AndrewBerman/Desktop/coo-y-r30` |
| Item 1, permanent authority refusal ends the job (S231) | candidate `62535e0fdc`, on CLOUD by merge `f1c8ade8b4` |
| Item 2, certification handed the chosen comparisons (S194, S213) | candidate `b75e571a74`, on CLOUD by merge `1ee1c56e9b` plus re-land `3a16cc442b` |
| Item 3, generate tests green; routes.json consumer notes (W94-S2, W91-S1) | candidate `ec4dddd69b`, on CLOUD by re-land `3a16cc442b` |
| Item 4, etf-classifications reader (W88-S2) | candidate `0ad0e6867d`, on CLOUD by merge `ca9d060bb2` |
| Item 5, catalogue list serves named rows only (batch 61) | candidate `efde229443`, on CLOUD by merge `53dcb65acd` |
| Deployed | NOTHING of items 1 to 5. Resident root `/opt/irpt-resident/fe64236bbb-st5`; generate `inrij6hL..`; status `ZYr+IDMp..` |
| Push state | LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read 05:2xZ). CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread

NOT LIVE. The thread is the upload lane (batch 61 item 1): one Cottonwood CSV upload, an Overview, a READY report read
on the page. First failing hop: 7, the YCharts session (the last 3 of 3 jobs that reached the vendor died there). The
thread also crosses three deployed units that are behind CLOUD, so one build window comes first.

## Next, in the order batch 61 ruled

1. **(b) `irpt-status` and `irpt-ycharts-generate` at CLOUD HEAD as WHOLE bundles** -- this seat's packet, both halves:
   member census against the live zip, pending members shipped not pinned, one invoke per function that reaches the
   changed path, same-window rollback. Waits on (a), `2.0.0_SA_COO~P`'s IB-pr-275 (CTO half signed @d9972c6eb4).
2. **(c) The resident at CLOUD HEAD under a ledger** -- this seat's. It picks up IB-yr-293, item 1, item 2 and
   IB-yr-291. Read-back: the digest of `ycharts/generate/current_authority.py` on the host (row S244's disarm).
   Then redrive the two dead-lettered messages on purpose (below); each ends by name.
3. **The hop-7 diagnostic: ONE solo Cottonwood Overview job on a cold resident**, ledgered, under Andrew's standing word
   at this seat for Analysis attempts; read the verdict journal. It produces a report or names the session verdict
   (this names row S230's cause and amends 103150's first condition). Not W27.
4. **S238's two controls after the window:** the directory negative control refused at the API (`svc_principal.py
   negcontrol`, after `~P`'s second packet), and one foreign-firm job refused in the resident's own journal. Then W27.
5. After the thread: one job per remaining arm (Multi-Comp, Target Weight, 49 Financial, Inflection), the catalogue
   route served first; the resolve concurrency fix; the vendor PDF link; the Analysis export; the email lane.

## Reads reconciled (batch 61 item 7), measured 2026-10-01 05:1xZ

- **The resident is ACTIVE, not stopped.** Journal: stopped 2026-09-30T03:50:15Z, started 05:13:31Z under this seat's
  ledger `irpt-resident-restart-3variant-20260930` (leg D1 closed 05:15:33Z), 0 restarts since. Row S229's "the
  resident is stopped" describes the 83 minutes before that start.
- **The dead-letter queue's two messages are named.** `irpt-generation` 0 visible, 0 in flight; `irpt-generation-dlq` 2,
  peeked at visibility 0, nothing deleted: `REQ-3a1b73a8dead02a17a09043b` (sent 2026-09-27T00:12:06Z, the baseline one)
  and `REQ-86f1ce7062356bc5c109ce12` (sent 2026-09-30T03:36:09Z, the added one). The second was received five times
  (03:36, 05:13, 05:28, 05:43, 05:58Z; the last four each `CurrentAuthorityRefused ACTOR_NOT_FOUND`), which is the
  queue's maxReceiveCount.
- **The two SUBMITTING job rows are those same two jobs.** Both carry `intent_session_refresh`, detail
  `{"operation":"session_refresh"}`, no lease. Neither can become terminal on served code. After (c), a redrive ends
  each by name: `REQ-86f1ce70` reads ACTOR_NOT_FOUND (item 1); `REQ-3a1b73a8` reads ACTOR_NOT_FOUND or
  SESSION_REFRESH_ALREADY_USED, whichever its actor's row decides.
- `irpt-jobs` is 17 rows: READY 5, ATTENTION 8, SUBMITTING 2, and 2 rows that are not jobs (tenant `_opal`: the
  session lease row, released, owner `irpt-ycharts-runner/312680`, fence 19; and one PROVIDER_OPERATION row).
- **Row S230, as far as the journal goes:** 03:36:10Z `IRPT_RESIDENT_EVICTION verdict=EVICTED job=REQ-86f1ce70`, then
  03:36:28Z `retained_for_retry class=OperationRefused code=CAPTURE_FAILED:AUTH_FAILED`. The first vendor operation was
  evicted and the one admitted refresh failed inside the capture 18 s later. Why the capture failed is not in the
  resident's journal; item 3 above names it.

## Rows this lane holds

| Row | State |
|---|---|
| S231 | code landed (item 1); disarms when the resident carrying it ends `REQ-86f1ce70` by name |
| S229 | conditions: cause named (item 3 above), retained message handled (the redrive), restart under a ledger (done 09-30) |
| S244 | ARMED; disarms on the resident build's read-back (next 2) |
| W88-S2 | reader landed and inert; the grant and the wiring are an exact patch for `2.0.0_SA_COO~P`: `deliverables/2.0.0_SA_COO~Y/R30_PATCH_FOR_P_W88_S2_20261001.md` |
| W94-S2, W91-S1 | repaired by item 3; for the CVO to close |
| W91-S2 | NOT repaired: `_contracts/tests/test_seam_paired.py` is held by the open order IRPT_DASHBD TO-DB-b-4. Ready check `R30_checks/check_303_seam_handlers.py` (FAIL at HEAD: 4 no-handler lines, 8 of 12). Owner of the file's grant: that order's issuer; un-parks when the order is terminal |
| W92-S1 | READ: the portal never rendered a finding's `actions`. `tabs/analysis/ProspectComposer.tsx:309-319` (portal @7c354824) prints `result.reason`, a fixed sentence and each finding's `code`; `InputReview.tsx:30-41` keys its control on `reasonCode`. So the vocabulary change removed no rendered action. For the CVO to close |
| W92-S4 | waits on `irpt-status` served at CLOUD HEAD (next 1), then one read of `RPT-2e21b52e` sections expecting NOT_READY |

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/ec2/investor-reporting-ycharts/**`;
`docs/contracts/investor-reporting/v1/routes.json`; this file; `deliverables/2.0.0_SA_COO~Y/**`;
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`. NOT this seat's, measured by refusal:
`infra/aws/terraform/investor-reporting/ycharts/generate.tf` (lane IRPT_COMPLETION_P), `reports/**` (`~P`'s lease),
`_contracts/tests/**` (the open IRPT_DASHBD order).

## Parked, each with its owner and the condition that un-parks it

- The upload-resolution path still retries a permanent authority refusal: ending it needs a finding code, a contract
  vocabulary edit. Owner this seat; after the thread.
- `ProspectComposer.tsx:311` tells the user to correct the file for every NEEDS_CORRECTION upload, including
  RESOLVE_RETRY_EXHAUSTED, which rows S206 and S215 measured is not the file's fault. Owner `2.0.0_SA_COO~D`; un-parks
  with the corrected words served on the upload answer.
- `pytest _contracts _authz/tests` in one process reads 7 failed, 329 passed in the main tree (row W98-S1 names the
  census half; the rest is a `transport` module-name collision). Owner `2.0.0_SA_COO~P`.
- The FAST notice to `3.0.0_SA_CVO` ("FAST from 04:33Z; pins graded after the fact") is not sent: no CVO seat is live.
  Un-parks when one registers; this file is its carrier until then.

## Limits

Nothing here is served. Items 1 to 5 are proven offline and by read-only real runs (the retained vendor PDF of
REQ-7ea49c2d for item 2; the live classifications table for items 4 and 5). Item 1's real run is the redrive after (c).

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` explicitly in a worktree.
- Before any irpt-status or generate apply: the four gates on the BUILT artifact (zip_module_census with `--expect`,
  zip_cold_start_smoke `--owner-refusal`, status_role_sim, offline_submit_proof `--live-env`).
- A password is read BY NAME from its store into memory and never printed.
- Vendor egress is on Andrew's standing word at this seat for Analysis attempts, ledgered; a served move needs both
  never-widen halves. "Nobody runs AC8 again"; do not remove the `wk-nfra-oplgtw-og-v-4-p1` worktree.
- Read safe-merge's exit code and its "tree check" line on every merge (merge `1ee1c56e9b` dropped 14 of 15 files at
  exit 0; `0.0.0_AB_MSTR` fixed the tool @380ebf5954).
