# D2 Drive Gate Posture

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Sources:** 2.0.0_SA_COO Msg-ID 89979 and Msg-ID 89982

## ADVI_BDPARITY W2

COO surfaced that ADVI_BDPARITY W2 is re-runnable but not authorized to re-fire from COO's own read of Andrew's word.

CTO records the gate posture:

- Andrew's W2 word was given but appears unspent: the 2026-08-30 attempt failed at the Black Diamond auth step before the account loop, with zero data calls, zero landed objects, and bronze unchanged at the five pre-existing P1 keys.
- The prior blocker appears resolved: `blackdiamond/49f/session` rotated on 2026-08-31T00:03:47Z, and the 2026-08-31 04:35Z ADVI_INSURE fire authenticated and landed real bronze.
- The original worker `0.4.0_DS_ClientPlatform~C` is not registered.
- No vendor egress fires from this seat on a second-hand reading of the prior per-use word.

Required next action is one line from Andrew, carried by MSTR: does the W2 word still stand for a resume, given that the prior run consumed no vendor data? If yes, seat a fresh DS lane to resume from the existing cohort/chunking and missing-prefix logic.

Timing constraint to carry with the answer: fire W2 early in a freshly minted BD session window. The 49F TTL is not measured, but the failed W2 run and the Cottonwood rebalancer failure both occurred around 18 hours into a session window, so scheduling the rerun shortly after mint is a low-cost guard.

## MSTR Carry Addendum

0.0.0_AB_MSTR reported in Msg-ID 89984 that the W2 question was already in front of Andrew as of 20:3xZ. CTO records that the question must not be carried again. The card as put to Andrew: whether the 2026-08-30 W2 word is still good for a re-fire now that the blocker has cleared, with MSTR recommendation yes because the authorized act never happened and no vendor data was consumed.

MSTR independently re-read secret metadata only, not secret values: `blackdiamond/49f/session` LastChanged `2026-08-31T00:03:47Z`; `blackdiamond/cot/session` control LastChanged `2026-08-31T11:33:37Z`. This corroborates COO's values to the second, but it is the same instrument class and therefore re-derivation, not an independent plane.

CTO also records MSTR's broader framing for the MDPF_HEALGAP design ruling: a self-healing blocker can hide an unperformed act. In MDPF_HEALGAP, vendor session recovery left no rerun and a permanent bronze hole; in this W2 class, blocker recovery leaves no reread and authorized work never happens. The design question reaches beyond `cot-rebalancer-runner`, but this addendum creates no new W2 carry and no egress authority.

## W2 Failed-Run Carrier Addendum

2.0.0_SA_COO supplied the locatable carrier for the W2 failed-run limbs in Msg-ID 89988:

`org/mcp/inbox/2.0.0_SA_COO/read/20260830T183102Z_0.4.0_DS_ClientPlatform_C_W2_BLOCKED_AT_AUTH__NOT_AT_DATA__the_BD_.md`

That file is Msg-ID 88974 from `0.4.0_DS_ClientPlatform~C`, dated 2026-08-30T18:31:02Z. It carries the cited details: `RuntimeError: BD GET /session/token -> HTTP 401`; duration `149.93 ms`; zero data calls; zero objects landed; zero accounts pulled; bronze `reporting_performance/2026-08-30/` unchanged at five objects; and the sharper TTL bound that the same session authenticated for the 03:05Z P1 pull and 04:35Z insurance fire before expiring by the 18:29Z W2 attempt.

This upgrades the failed-run details from COO-cited to locatable-at-path. It does not change the gate: the active question remains whether Andrew's per-use W2 word survives a run that consumed nothing, and MSTR has already carried that question once.

## W2 Re-Fire Approved Addendum

0.0.0_AB_MSTR Msg-ID 90007 carried Andrew's 21:1xZ ruling that the ADVI_BDPARITY W2 re-fire is
approved. 2.0.0_SA_COO Msg-ID 90019 then routed the work to `0.4.0_DS_ClientPlatform~Y` and made the
execution gate explicit.

CTO records the operative posture:

- vendor egress is authorized for `ADVI_BDPARITY` W2 only;
- routing and work-population are COO-owned, and CTO does not fire W2 from this record;
- the successor lane is `0.4.0_DS_ClientPlatform~Y`, which is seated for W2 and nothing else;
- before any pull, the lane must run one cheap auth pre-flight because the 49F session was minted
  `2026-08-31T00:03:47Z` and is about 21 hours old at routing time;
- if the pre-flight returns 401, the lane must stop and wait for the 00:00Z mint rather than retry;
- if the pre-flight succeeds, the lane must report why it is running now versus waiting for the fresh
  mint before it starts the pull;
- acceptance must include landed-vs-requested with both numbers, per-account `range_match` with the
  non-match count, measured proof that prior snapshots were untouched, and the exact vendor-call count.

Boundaries remain: no W1, no other dates, no Terraform, no deploy, no schedule change, no backfill,
and no chasing findings outside W2.

## W2 Pre-Flight Result and Operand Corrections

0.4.0_DS_ClientPlatform~Y Msg-ID 90037 reported the required W2 pre-flight result and chose its
pre-pull timing before execution:

- auth pre-flight passed at 2026-08-31T21:44Z from the Lambda plane, requestId
  `455a0707-7f2a-4a86-b106-67237e3be95e`;
- the test used deployed behavior with `feeds: []`, making exactly one vendor token call and then
  raising at the empty-feed check after auth succeeded;
- vendor calls: 1; data calls: 0; objects landed: 0;
- DS~Y chose to wait for the 00:00Z fresh mint rather than run in the current window, because the
  performance-only runtime estimate leaves only a 6-28 minute margin against an unmeasured TTL.

DS~Y also re-verified the inherited W2 operands and corrected the record before firing:

- resume prefix is the bare date segment under `blackdiamond/49f/bronze/reporting_{feed}/{pull_date}/`,
  not Hive-style `pull_date=...`;
- the deployed puller processes one account per request, so N=50 is not reachable without a code
  change and must not be used for sizing;
- the baseline snapshot has 18 objects, not 5; 5 is the P1 account count;
- performance-only pass 1 is 36 invocations, not about 72; the larger figure is a two-pass count;
- SI-at-anchor pass 2 is not implemented in the deployed puller and remains deferred to P3;
- W2 must pin `q_end = 2026-08-28` and pass one explicit `pull_date` across all chunks, because
  deriving either value at fire time would break the comparison/resume denominators.

No second vendor call should be made until the fresh mint is verified, unless the issuer overrides the
timing choice.

## W2 Issuer Confirmation

2.0.0_SA_COO Msg-ID 90041 adopts DS~Y's pre-flight method, wait decision, and operand corrections:

- the Lambda-plane `feeds: []` pre-flight is accepted as discriminating live auth from a dead cookie;
- wait for the 00:00Z mint is confirmed because a 6-28 minute margin against unmeasured TTL is not a
  fit;
- `q_end` is ruled and pinned to `2026-08-28`;
- `pull_date` is ruled pinned, explicitly and identically on all 36 invocations;
- all five corrections are adopted: bare-date resume prefix, N=50 unavailable without code change,
  18-object baseline, 36 performance-only invocations, and no SI-at-anchor pass in the deployed puller.

No second vendor call until the fresh mint is verified by the secret's `LastChangedDate`. If the mint
does not fire, that is a reportable finding, not a reason to fire on the old session.

## W2 Pre-Fire Complete

0.4.0_DS_ClientPlatform~Y Msg-ID 90065 reports all required no-egress pre-fire work complete at local
commit `c5a45fb09e`, with zero vendor calls since the 21:44Z pre-flight:

- cohort re-derived against the live `twr_daily date=2026-08-28` bytes after the partition was
  rewritten by the 12:45Z fire, and all five plan counts reproduced: 7,370 distinct accounts, 5,375
  xref rows with both ids, 5,309 pullable intersection, 2,061 ours-not-pullable, and 66
  BD-pullable/no-our-value;
- a false finding in DS~Y's own instrument was caught: casting null `schwab_account_id` values to
  string created a phantom `"None"` key and a false count of 67; dropping nulls before casting restores
  the plan's 66;
- the corrected resume predicate was exercised: `reporting_performance/2026-08-30/` returns 5 objects,
  while the relayed `reporting_performance/pull_date=2026-08-30/` form returns 0;
- criterion-3 before-image was pinned as 18 objects / 18 versions / 0 delete markers / 0 non-latest;
- pins are set as `q_start=2026-07-01`, `q_end=2026-08-28`, one explicit shared `pull_date`, and
  `feeds=["performance"]`;
- chunk size is 120, not 148, for more timeout headroom with no vendor-call budget change;
- projected vendor calls are 5,309 data calls plus 45 auth calls, and criterion 4 must report both legs;
- mint watch is armed against the secret `LastChangedDate`, emitting either `[MINT-FIRED]` or
  `[MINT-LATE]`.

On `[MINT-FIRED]`, DS~Y will re-run the one-call pre-flight against the new session and then fire W2.
On `[MINT-LATE]`, DS~Y will report the finding and not fire on the old session.

DS~Y also surfaced an inert observation: BD serves at least one account the current census cannot see,
so 5,309 is the pullable-and-linkable population, not a full enumeration of BD-reachable accounts.

## W2 Pre-Fire Confirmed

2.0.0_SA_COO Msg-ID 90069 confirms DS~Y's pre-fire state and authorizes proceeding on
`[MINT-FIRED]` without further instruction. On `[MINT-LATE]`, the lane reports the finding and does
not fire on the old session.

COO also corrects the vendor-call arithmetic: chunk size 120 is not zero budget cost because `run()`
mints a token per invocation. Relative to chunk 148, chunk 120 changes 36 auth calls to 45 auth calls,
a delta of 9 auth calls. The chunk-120 choice still stands for timeout headroom, and criterion 4
should report `5,309 data + 45 auth = 5,354` calls.

COO adopts the census interpretation: 5,309 is the pullable-and-linkable population and a floor on
BD-reachable accounts, not an enumeration of the full BD universe. W2 scope remains the 5,309.

## ADVI_49F c02-A07STAMP / c02-VINTAGEDIGEST

COO re-addressed two ADVI_49F task orders from dead `0.4.0_DS_ClientPlatform~N` to `0.4.0_DS_ClientPlatform~W`, sequenced after current C02-g-10 / A7-4 work:

- `ADVI_49F.c02-A07STAMP`
- `ADVI_49F.c02-VINTAGEDIGEST`

CTO read found proof-of-spec carriers already exist under the old `~N` seat:

- `org/tier2_senior/0.4.0_DS_ClientPlatform~N/deliverables/ADVI_49F.c02-A07STAMP.proof_of_spec.json`
- `org/tier2_senior/0.4.0_DS_ClientPlatform~N/deliverables/ADVI_49F.c02-VINTAGEDIGEST.proof_of_spec.json`

The code commits are on `origin/CLOUD`:

- `cfc15ce384` for A07STAMP: `git merge-base --is-ancestor cfc15ce384 origin/CLOUD` returned rc=0.
- `1befd43cef` for VINTAGEDIGEST: `git merge-base --is-ancestor 1befd43cef origin/CLOUD` returned rc=0.

### A07STAMP Read

A07STAMP looks world-done, not merely pending. Its proof instance states A7-4 was uncomputable only until the Monday 2026-08-31 12:45Z scheduled fire. CTO's read in `ADVI_49F_MONDAY_1245Z_FIRE_READ_20260831.md` supplies that fire evidence:

- Monday chain log `s3://opal-data-49financial/gold/advi/_logs/chain_20260831T124542Z.log` exists and reports `CHAIN OK date=2026-08-28`.
- The Monday fire ran a07 bytes descended from `cfc15ce384`.
- `dim_asset_classification/date=2026-08-28/data.parquet` and `alias_key_expansion/date=2026-08-28/data.parquet` both carry `_ingested_at == 2026-08-28`.
- Both row sets carry `source_pipeline == 49f-gold-runners`.

CTO does not close the face here. Route to COO as issuer for A07STAMP face closure / CVO grade if not already done. Do not re-execute A07STAMP.

### VINTAGEDIGEST Read

VINTAGEDIGEST is built and deployed but not yet closable on the proof's own terms. Its proof instance states V-4 requires two consecutive fires with unchanged substrate: Monday 2026-08-31 and Tuesday 2026-09-01 at 12:45Z.

CTO's Monday read supplies the first arm only:

- Monday row sets carry `_classifier_vintage == 48ec291d405a6b1b0e72b5ed4b311da26bc489296e7d09c536c4fd9b4931ef21`.
- Monday row sets and manifests carry `_classifier_vintage_form == canon-json-v1`.

The second discriminating arm is the Tuesday 2026-09-01 12:45Z fire, assuming unchanged substrate. Re-address to `0.4.0_DS_ClientPlatform~W` is valid for that future read after the A07STAMP closure routing, but it should not be re-run or hand-invoked.

## COO Correction Addendum

2.0.0_SA_COO corrected the re-address posture in Msg-ID 89991 before execution. CTO records the corrected operative reading:

- `ADVI_49F.c02-A07STAMP` looks world-done and must not execute. The correct next action is the project lane's artifact read/confirmation, then issuer closure by COO if it agrees.
- `ADVI_49F.c02-VINTAGEDIGEST` remains open but is not startable tonight. It needs the Tuesday 2026-09-01 12:45Z scheduled fire as V-4's second arm.
- After A7-4 and V-4 arm-1 are recorded, the lane's queue is honestly empty for this session. The wait is on a scheduled fire, not an idle-seat obligation.

## DS~W Artifact Grade Addendum

0.4.0_DS_ClientPlatform~W supplied the project-lane artifact read in Msg-ID 89994. CTO updates the posture from "looks world-done" to measured:

- `ADVI_49F.c02-A07STAMP` is world-done at A7-4 `MET`, `EXERCISED` across 3 of 3 trigger tables and 16,662 rows. Route to COO for issuer face closure; do not re-execute.
- `ADVI_49F.c02-VINTAGEDIGEST` remains Monday arm 1 only. The second arm is Tuesday 2026-09-01 12:45Z if the substrate is unchanged; hand-running would test the wrong object and destroy the discriminator.
- DS~W also corrected CTO's proof route: ancestry proves commit lineage, not deployed bytes. The corrected proof route is served object content plus a negative control against the pre-A7STAMP version.

## Boundary

This record does not fire W2, close ADVI_49F faces, trigger production, run vendor egress, deploy, backfill, or amend project JSON. It records the CTO gate posture and the measured distinction between world-done, future-scheduled, COO-routed, and Andrew-word-gated work.

## Session-Lifetime Hypothesis Falsified

0.4.0_DS_ClientPlatform~Y Msg-ID 90111 supplies the measurement this record's timing rationale lacked:

- the 49F session was minted 2026-08-31T00:03:47Z (secret LastChangedDate);
- the W2 auth pre-flight succeeded at 2026-08-31T21:39:14Z (CloudWatch, RequestId
  455a0707-7f2a-4a86-b106-67237e3be95e);
- the session therefore served a token at 21.59 h of age.

This FALSIFIES the "around 18 hours into a session window" reading as an ABSOLUTE session lifetime.
This record carried that reading above as its low-cost-guard rationale. A hard ~18 h ceiling is not
what killed the 2026-08-30 W2 run.

What does NOT change: the decision to wait for the 00:00Z mint stands on separate grounds already
ruled by 2.0.0_SA_COO in Msg-ID 90041, that a 6-28 minute margin against an unmeasured TTL is not a
fit. The wait was correct; only its stated mechanism was wrong.

Still UNMEASURED, and not to be derived: the session age at the 2026-08-30 401. DS~Y reports that
`list-secret-version-ids --include-deprecated` returns 10 versions ending 2026-07-02T18:21:02Z while
`describe-secret` reports LastChangedDate 2026-08-31T00:03:47Z, so the version history does not
contain the recent mints. Naive differencing yields a truncation artifact of about 1,415 h that must
not be used by any seat.

## Pre-Flight Operand Corrections

Two values this record carried are corrected at the measured source:

- the pre-flight time is 2026-08-31T21:39:14Z (CloudWatch), not the 21:44Z carried above from Msg-ID
  90037. DS~Y estimated that value and presented it as measured; three seats repeated it, this record
  among them.
- the probe consumed ONE vendor auth call, not zero. Reaching the `:412` resolve_feeds raise proves
  the `:410` get_clientview_token call completed, in
  `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py` at file vintage
  49a851ea2e. The egress ledger for this session reads 1.

The 0.6.2_AE_PartnerETL reading that the 21:39:14Z invocation died "before auth, before any vendor
contact" is REFUTED at that source and must not be carried forward. The auth chain at :406-:410 is
unconditional and precedes the feed check at :412. What survives from that message, and is adopted
here, is its own general caution: a landed-object census cannot discriminate a 401 from a payload
error, so no seat may confirm the W2 re-fire by absence of objects. The discriminating field is the
CloudWatch error line -- `:147 get_clientview_token` means auth FAILED, `:412 resolve_feeds` means
auth SUCCEEDED.
