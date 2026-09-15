# PARKED at the managed winddown -- POSN_AGGFIX round 1: where it stands, what this seat owes, and every measurement its L10 needs

**Owner:** `1.0.0_SA_CTO~Z`. **Parked:** 2026-09-15 ~23:5xZ, on the Andrew-direct winddown relayed by `0.0.0_AB_MSTR~Z` (msg 23297).
**Carrier:** this file. Everything below was in this seat's session only; it is committed so a successor needs no context from it.
**Push state:** LOCAL (site-Z push hold).

## The word

Andrew-direct ~23:5xZ at the `0.0.0_AB_MSTR~Z` terminal, VERBATIM AND ENTIRE: "huntress is blowing up again we need managed winddown".
Read by the relaying seat as: stop starting, let in-flight finish, park durably, report, do not self-kill. Neither POSN_AGGFIX nor AMGT is
cancelled.

## Round 1 state at the park (measured 23:52Z)

- SIX orders COMPLETE and drained: TO-A1-1, TO-A2-1, TO-A3-1, TO-B1-1, TO-B2-1, TO-C1-1.
- TO-B3-1: the worker's proof instance is filed VALID rc=0 with 6 of 6 criteria recorded (`ece511ae97`); B3-AC4 PASSES on the printed rows
  under AMENDMENT 1. It is STAGED pending `2.0.0_SA_COO~Z`'s drain. dep_stage EXECUTING.
- LIVE IN PRODUCTION ALREADY: the producer deploy (Branch A) and the edge gate (auth-validator-edge v20 on 25 of 25 associations).
- NOT YET ON PROD: the portal UI, 5 files, on `refs/drains/aggfix-1-portal` = `3ec1f83cab`, also on origin as `sitez/aggfix-1-portal`.

## What this seat owes next, in order

1. On the CVO's round-1 slug: `ledger/ROUND_ANALYSIS.round1.md` and `ledger/COMPLETION_GRADES.round1.json` (graded_by binds to this seat).
   Grade FWD-4, FWD-6, FWD-7 and FWD-8 REALIZED on the evidence below; FWD-1, FWD-2, FWD-3 and FWD-9 are page-side and are graded AFTER the
   promote, per the goal record @`15827b3991`.
2. Then send `0.0.0_AB_MSTR~Z` a message beginning exactly "POSN_AGGFIX step 2 due", naming every order terminal, the slug, the L10 grades,
   and the exact portal ref and head. That message, and only that message, starts the DEV merge (contract acked in msgs 23262, 23263, 23296).
3. Then this seat runs `/prod-deploy` (Andrew's word, record @`15827b3991`), reading BOTH copies of `promote-to-prod.yml` first and naming
   which one governs a PROD push (DEV's copy differs; PROD's copy runs).
4. Then grade the four page outcomes on the served page, and `0.0.0_AB_MSTR~Z` makes ONE gitlink commit to the PROD that contains the
   aggregate.

## Andrew's local build, already fixed by this seat (do not redo)

- The workspace `portal` checkout was moved from `e85f6eb84f` (2026-09-10, 212 commits behind) to `origin/PROD` `edf85ce503`. The gitlink is
  deliberately NOT committed; the workspace shows ` M portal` and `0.0.0_AB_MSTR~Z` owns that one commit after the promote.
- `portal/.env.local` and `/c/tmp/portal-aggfix-view/.env.local` (both gitignored) set `VITE_AUTH_API_URL=` and `VITE_PORTAL_API_URL=` empty,
  so auth is same-origin through the dev proxy into CloudFront. Without it the hardcoded API Gateway fallbacks
  (`src/api/api-client.ts:17`, `src/contexts/AuthContext.tsx:76`) get 403 from the authorizer, which is what he hit.
- `/c/tmp/portal-aggfix-view` is a portal worktree at `3ec1f83cab` (PROD + the two AGGFIX commits) for previewing the aggregate before the
  promote. It is this seat's and can be removed by anyone after the promote.

## Un-parks when

The CVO's round-1 slug lands, or Andrew re-sequences. A successor resumes at step 1 above with nothing but this file.

---

# THE L10 CARRY LIST AND EVERY MEASUREMENT (verbatim from this seat's working notes)

# POSN_AGGFIX round 1 -- L10 carry list (working notes, not a record)

Seat: 1.0.0_SA_CTO~Z. Started 2026-09-15 ~20:2xZ while round 1 executes. Every item re-reads its row or artifact at L10; nothing here
is graded from memory.

## Rows the analysis must answer (read each at HEAD at L10; the channel may have grown)

| row | class / standing at 20:1xZ | what L10 decides |
|---|---|---|
| POSN_AGGFIX-Z-S1 | OBSERVATION INERT | PRD touch to C-NO-SILENT-EMPTY: name both arms of the books' failure fallback (a wholly failed read writes no current_holdings; a partial read writes aum 0). A brief-half-only edit, so only the brief half re-signs. |
| POSN_AGGFIX-Z-S2 | OBSERVATION INERT (arms at TO-A3-1 Branch A) | restore writers by prefix (yang-time-machine, rollback-protocol.sh) re-serve AGG and July aum after a pre-change restore; plus W1-S4's CLI --upload path as a fourth write site. Decide: a cell (restore set handling for json/positioning/, or an operating rule) or an accepted, disclosed residual. |
| POSN_AGGFIX-Z-W1-S1 | OBSERVATION ARMED | gap 8,324,465.16 = opal_fixed_income, a cohort-model key the fold counts in model_aua that dim_mdpf_aum_metrics.py's fixed MODEL_ORDER never rows. Owner of the defect 0.4.0_DS_ClientPlatform (gate 1.0.0_SA_CTO). FWD-6 "explained" branch satisfied by AF1_S1_GAP_EXPLANATION.md; Andrew ~19:0xZ "no Opal Fixed Income" keeps it outside the aggregate. Route the producer defect outside this project, not a POSN cell. |
| POSN_AGGFIX-Z-W1-S2 | BLOCKING INERT | issuer cut defect in A1-AC6 (IAM simulate query); the COO's re-run. Confirm resolved at the slug. |
| POSN_AGGFIX-Z-W1-S3 | OBSERVATION INERT | yang-pipeline-lambda-role's bucket-wide S3ReadWrite also allows PutObject on platinum/mdpf/global/aum-metrics.json. Pre-existing breadth, not a widening by this project; PRD S9 "no IAM edit" stands. Decide whether to route a least-privilege note to the IAM owner. |
| POSN_AGGFIX-Z-W1-S4 | BLOCKING INERT | two write sites in the producer file (handler :2623-2630, main() --upload :2501-2508). Issuer cut defect in A1-AC2's expected count; also feeds Z-S2. |
| POSN_AGGFIX-Z-W1-S5 | OBSERVATION INERT | order text said all served objects are gzip; only positioning_data.json is. Cut wording; no outcome effect. |
| POSN_AGGFIX-Z-W2-S1, Z-W2-S2 | (worker ~2's rows, unread by this seat at 20:1xZ) | read at L10. W2-S1 one_line begins "no client class in the signer's tier space" -- check against C1-AC13's client-class token. |

## Standard and PRD items not carried by a row

1. `org/standards/POSN_AGGREGATE_MODEL_SET.json` v1.0:
   - ST INT blend `claim` inferred -> held on Andrew's word ~19:1xZ ("50/50 ST INT would be 50% into ST and 50% into INT", COO record @fc8cdf1a1e). Deferred from mid-round.
   - INT LTC blend stays inferred until AF1-s-17's verify.
   - `measured_against.rows_outside_the_rule: 0` is scoped to the seven served rows; it cannot see opal_fixed_income (W1-S1). Add the scope sentence and the out-of-row key.
2. PRD v0.2 C-MEMBERS: Andrew's "no Opal Fixed Income" and the split rule are consistent with the text; cite both records in s.6 at the next bump.

## Grading reminders for the close

- Page outcomes FWD-1, FWD-2, FWD-3, FWD-9 are read on the served page after /prod-deploy (Andrew-direct ~19:2xZ order, record @15827b3991).
- FWD-7: live refusal for advisor and client on both URL forms and the encoded variants (edge half conditions, TO-C1-1 AMENDMENT 1 @b62ea1caa3).
- FWD-8: five books' non-aum identity and each aum equal to its own current row; S16 before/after screens.
- The goal's step 2: name refs/drains/aggfix-1-portal and its base PROD edf85ce503 to 0.0.0_AB_MSTR~Z for the portal /integrate.

## Added ~20:3xZ

- **Z-W2-S1** (OBSERVATION INERT): the live signer mints only tier internal (firmId opal-capital) or advisor; no real client-class
  token exists. The worker built a synthetic client (tier client, firmId 49financial, no advisor identity). The gate reads only
  firmId and userType, so the synthetic class still exercises it; the advisor class is the real outside tier. L10: note that FWD-2
  and FWD-7's "client" arm is exercised on a synthetic token, and name the auth-handler source (jwt.ts :168) as the evidence.
- **Z-W2-S2** (OBSERVATION INERT): /api/general/positioning/model.json does NOT refuse a client token live (C1-AC3, 19:41:33Z). The
  proxy docstring (portal-proxy.ts :1419-1426) describes a check that is not on the path; inert only while json/positioning/model.json
  is absent. Not this project's surface: route to the portal-proxy / edge owner at L10 (corroborates PRD s.7 S4's finding).
- **COO amendment 48a00724ca**: TO-A1-1 re-cuts A1-AC2 and A1-AC6 on the worker's refusals; TO-A2-1 takes the CLI --upload write path
  (answers W1-S4 inside the round). Re-read at L10 that the --upload path no longer writes AGG into the shared file.

## Added ~21:2xZ -- the edge gate (TO-C1-1), live evidence for FWD-2 / FWD-7 grading

- LIVE (read by 1.0.0_SA_CTO~Z, AWS read-only ~21:0xZ and ~21:14Z): auth-validator-edge version 20, CodeSha256
  fekWqHP2cWuewpfFOnlxa2S5jBhxmKKs8eB4/QccRxs=, published 2026-09-15T21:00:57Z; artifact latest VersionId NQpc4Vgyg.NyZLUn078xzAc5Ly8NkPlM.
- Worker ~2 scratch (/c/tmp/wk-aggfix-1-2/.scratch): C1-AC18 25 of 25 at v19 BEFORE the apply (20:42:04Z); C1-AC12 25 of 25 at v20 AFTER,
  0 other (21:06:51Z); C1-AC20 WAF RULES UNCHANGED 6 of 6; C1-AC13 30 of 30 MATCH (advisor + client 401 on both URL forms and on
  %5F / %5f / json-form %5F / ?v=1; double-slash 403 S3 absent key; control positioning_data.json 200 for all four classes; FAMILIES
  UNMOVED 6 of 6). At the L10 read, re-read from the DRAINED proof instance, not this scratch.
- The client arm is a synthetic token (row Z-W2-S1): the signer mints only internal or advisor.
- OPERATING FACT for other seats: every plan of infra/aws/terraform/portal-auth now re-proposes the WebACL's three managed rule version
  leaves '' -> null (state "" vs AWS absent). Inside both halves' AMENDMENT 2; TO-C1-1 AMENDMENT 3 @b2628856f5 accepts it on re-plan.
  L10: decide whether to route a one-line fix (lifecycle ignore_changes on that attribute, or state normalisation) to the portal-auth
  owner so the next seat's plan is clean -- not a POSN cell.
- FWD-7 still needs: the Opal-only key WRITTEN by the producer (TO-A3-1) and the live refusal re-read on the served bytes (TO-B3-1 /
  AF1-s-16); today Opal staff get S3's absent-key answer.

## Added ~21:3xZ -- TO-A2-1 rows W1-S6..W1-S9 (partial drain 75775c954a)

- W1-S6 (BLOCKING): main() --upload builds a different payload from the handler (no ETF returns; data_date YYYY-MM-DD vs YYYYMMDD);
  true at 605c03f81f too. Feeds Z-S2: a local CLI upload would serve a shared file WITHOUT per-holding returns (an FWD-8 hazard, not only
  an AGG one). COO re-cut; L10 decides whether the CLI write path stays at all.
- W1-S7 (OBSERVATION): the shared file is not byte-stable across processes (portfolios.<code>.benchmark.spread.segment key order follows
  set iteration under hash randomization). Any byte/hash compare of two served files sees a change that is not one. BEARS ON TO-A3-1's
  Branch B trigger under both producer halves -- flagged to the COO before the deploy (see CTO half addendum).
- W1-S8 (OBSERVATION): aggregate weights are served rounded to 4 decimals; FWD-4 grading compares at 4.
- W1-S9 (BLOCKING): A2-AC11's anchor 605c03f81f counts other orders' infra files after the SITEZ fast-forward; the order's own commit
  touches exactly one infra file. COO re-cut.

## Added ~21:5xZ -- the portal drain ref, for goal step 2 (MSTR~Z portal /integrate)

- refs/drains/aggfix-1-portal = 3ec1f83cab (read ~21:5xZ); base portal PROD edf85ce503 is an ancestor.
- Commits above PROD, 2: 63edeeeb51 (TO-B1-1, the Opal-only aggregate fetch gated to the page predicate) and 3ec1f83cab (TO-B2-1, the
  Holdings tab restores the aggregate book for Opal viewers).
- Files vs PROD, 5: src/api/portal-proxy.ts (+59), src/pages/Positioning/Positioning.tsx (+32/-), src/pages/Positioning/README.md (+11),
  src/pages/Positioning/shared/bookSet.ts (+162/-), src/pages/Positioning/tabs/HoldingsTab.tsx (+150/-). 370 insertions, 44 deletions.
- TO-B3-1 (the five model views and the aggregate on live bytes) may add more; re-read the ref at the close before naming it to
  0.0.0_AB_MSTR~Z. Nothing moves the gitlink; the promote is step 3, /prod-deploy, after the integrate.

## Added ~21:4xZ -- TO-C1-1 drained (70e74a93bb); an attribution fault in worker merges

- TO-C1-1 COMPLETE: the edge gate live, auth-validator-edge v20 on 25 of 25; rows W2-S5 (halt gate rooted at the worktree), W2-S6 (the WAF
  normalization re-plans after the apply), and more in 2fbcd7f228 -- read all W2 rows at L10.
- ATTRIBUTION FAULT (tooling, not a POSN defect): e88029a8c0 "Merge branch 'SITEZ' into wk-posn_aggfix-1-2" is authored by
  0.0.0_AB_MSTR, the machine's git identity, because the worker's first act runs a bare `git merge --no-edit SITEZ` (the order text) with no
  --author and no GIT_AUTHOR_* in the environment. A worker's merge therefore lands in the record under the integrator's serial. L10: route a
  one-line fix to the order template (merge with the worker's author identity, e.g. `git -c user.name=<serial> -c user.email=<serial>@opal.agent
  merge --no-edit SITEZ`), not a POSN cell. Check the other slots' merges for the same shape.

## Added ~22:1xZ -- goal step 2 groundwork by 0.0.0_AB_MSTR~Z (msg 23261)

- Portal branch sitez/aggfix-1-portal is ON ORIGIN @3ec1f83cab (ls-remote), equal to refs/drains/aggfix-1-portal. Base origin/PROD edf85ce503
  verified as merge-base and ancestor. Merge into origin/DEV: overlap 0 of 7 files; merge-tree rc=0; result tree de013cf176 differs from
  origin/DEV by exactly the 5 Positioning files (+370/-44), with a negative control. The integrator is HOLDING the DEV merge.
- AGREED sequence (this seat's reply): (a) this seat sends "POSN_AGGFIX step 2 due" -- every order terminal in every round, slug landed,
  L10 graded REALIZED on every pre-promote outcome, the exact ref and head named; (b) ONE MSTR merges the RE-READ drain ref into DEV and
  pushes; (c) this seat runs /prod-deploy; the page outcomes FWD-1/2/3/9 are graded after (c).
- FOR /prod-deploy: promote-to-prod.yml differs between DEV (acdb02e9, 1.0.0_SA_CTO~A) and PROD. A PROD push runs PROD's copy. Read both
  copies before running the skill; name which runs.

## Added ~22:2xZ -- TO-A3-1 producer deploy, Branch A (worker ~1 change record, read by this seat at 22:22Z)

- L3 plan -target=module.generate_positioning 0/1/0 (s3_object_version, source_code_hash); L4 safe-apply 22:08:5xZ 0/1/0 (halt gate
  scanned the issuer; tagauthz and tombstone gates passed); L5 re-plan No changes, CodeSha256 riByGXEf... == artifact, LastModified
  22:09:30Z.
- L6 driven run 22:12:11Z on execution 20260914_v1-9dbd2129: generator once, no FunctionError; invalidation once, no FunctionError.
  positioning_data.json VersionId aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou -> dFjRdciig4Y.4DBiK_F... (read the full id at L10).
- L7 compare 22:13:45Z, parsed JSON, key order ignored: AGG removed; BOOK NON-AUM IDENTICAL 5 of 5; book aum EQUAL to its own platinum row
  at OVcFBOpgjFywfYJGYjowX2VSVwLdiyez 5 of 5; top-level identical; opal_aggregate.json status OK, weights sum 1.0, max |w - members/sum| 0;
  served delta 7 paths all permitted, 0 other. BRANCH A. No restore path invoked (CTO half condition held).
- L8 record commit 04ee6921d8 (lambda-source-map.json, 3 of 2418 leaves).
- FWD evidence this feeds: FWD-4 (current mix), FWD-6 (primary + blends, reconciliation block), FWD-8 (five books' non-aum identity on
  the served file). FWD-7's served-bytes refusal is TO-B3-1's live read now that the key exists.
- NOT POSN, route at L10: yang-invalidate-cloudfront answered E2LPCXXBLDGWXY NoSuchDistribution -- a stale distribution id, likely in the
  same DISTRIBUTION_IDS list yang-time-machine carries at :44 (read both at L10). The CHANGELOG helper failed again (SyntaxError, the
  POSN_ASTTAX W23-S4 recorder defect, owner 0.7.0_AE_CloudOps); entry written by hand.

## Added ~23:3xZ -- THIS SEAT'S OWN SERVED READS for grading (not from any report)

Instrument: .tools/aws s3api get-object + local gzip/json parse, run by 1.0.0_SA_CTO~Z at ~23:2xZ.

- s3://opal-data-portal-v2/json/positioning/positioning_data.json VersionId dFjRdciig4Y.4DBiK_F0eyHtn1.YBCOC, LastModified
  2026-09-15T22:12:23Z, gzip, 7150 B stored / 67273 B decoded; generated_at 2026-09-15T22:12:22Z; data_as_of 2026-09-14.
  current_holdings keys ['INT','LT','ST','ULT','UST']; AGG PRESENT = False.
- Each book's aum EQUAL to its own by_model row of platinum/mdpf/global/aum-metrics.json (VersionId OVcFBOpgjFywfYJGYjowX2VSVwLdiyez,
  period 2026-09-14): UST 65,550,660.50; ST 133,205,460.44; INT 456,971,348.29; LT 883,977,496.68; ULT 209,446,529.75. 5 of 5.
- s3://opal-data-portal-v2/json/positioning/opal_aggregate.json VersionId M8FOApCmYnAQB_3946XGOHSeqEzcL2j., gzip, 14410 B decoded:
  status OK, reason null, data_as_of 2026-09-14; 30 holdings; total_aum 1,792,113,521.90.
  weights UST .0366 ST .0763 INT .2670 LT .5032 ULT .1169, sum exactly 1.0; weight == members[code]/members_sum for all five.
  weights_source key platinum/mdpf/global/aum-metrics.json, period 2026-09-14, version OVcFBOpgjFywfYJG...
  members: five primary + 2 blends; reconciliation five_primary_sum 1,749,151,495.66, members_sum 1,792,113,521.90,
  file_total_model_aum 1,800,437,987.06, gap 8,324,465.16.
- GRADES THIS SUPPORTS (pre-promote): FWD-4 (current mix, EXERCISED), FWD-6 (members + blends + reconciliation, EXERCISED),
  FWD-8 data half (five books present, non-aum identity from B3-AC2's 10 of 10 render compare), FWD-7 data half (no AGG in the shared
  file every viewer receives; the live refusal is B3-AC4's 24 of 24 and B3-AC6's session read).
- STILL PAGE-SIDE, graded after /prod-deploy: FWD-1, FWD-2, FWD-3, FWD-9.

## Added ~23:4xZ -- TO-B3-1's last two criteria (read by this seat from slot ~3's outputs, 23:42Z)

- B3-AC4 re-run (b3_ac4_rerun.out, after AMENDMENT 1 @b2901f56c6): TABLE ROWS 24; MATCH 24 of 24. Advisor and client 401
  "Opal-only resource" on both URL forms and on %5F / %5f / json-form %5F / ?v=1; the double-slash form 403 (S3 absent-key answer, not
  the aggregate); the control /api/general/positioning/positioning_data.json 200 len 67273 sha256 86314ec65f3877e6 for BOTH classes.
  The FAMILIES line still reports slot ~2's baseline ABSENT; AMENDMENT 1 grades the printed rows, not the rc, so this is expected.
- B3-AC6 (new, b3_ac6.out): TABLE ROWS 8; MATCH 8 of 8.
  advisor + client on the shared file: 200, current_holdings [UST ST INT LT ULT], AGG=ABSENT.
  advisor + client on the aggregate, both URL forms: 401.
  opal + dev on the aggregate: 200, len 14410, body.status OK, current_holdings [AGG], AGG=PRESENT.
  POSITIVE CONTROL: the same parser against TO-A3-1's PRIOR shared-file version reports AGG PRESENT -- the check CAN fail.
- GRADES THIS COMPLETES (pre-promote): FWD-7 EXERCISED (nothing outside Opal receives the aggregate, on the served bytes, with a firing
  control) and the served half of FWD-8 (the shared file an advisor/client receives still carries the five books).
