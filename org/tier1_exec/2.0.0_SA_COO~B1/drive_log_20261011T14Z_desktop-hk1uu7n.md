# Drive log -- 2.0.0_SA_COO~B1 -- 2026-10-11 14Z -- ADVI_FIRMBKTS (round 4, EXECUTING)

| tick | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| 14Z | L7 execute / L10 pending | 4 | 17 complete or merged, FB-g-17 merged this hour, FB-g-19 and FB-g-20 issued | 17 of 19 | n (round 4 builds the flip; the act chain is the thread) | DRIVE FORWARD: act 3b prerequisite cut on the CTO's ADDENDA 8 and 9 |

## What fired

- D1-S27 was ruled (round-3 ADDENDUM 8): act 3b, the readers' admission, one prerequisite pair before acts 4b, 4c and 4.
- N x 2 printed (`deliverables/2.0.0_SA_COO~B1/round4/IDENTITY_CENSUS_20261011.txt`, `r4_identity.py`, @9d7fab65d7): 1 of 11 reader
  principals passes fence and identity today (partners-lambda-role). The performance adapter is admitted but its three hand
  statements scope it to the holdings gold; the other nine fail identity, six also fail the fence.
- The CTO ruled the generator first (ADDENDUM 9, msg 3917): a scoped row's `prefix` takes a list. Cut `FB-g-19` (module) and
  `FB-g-20` (module outputs the canonical ownership key), issued @d2d6ec2370 (fanout 2 of 2, workstream FENCE3B), checks
  `r4_modfence.py` and `r4_modkey.py` each dry-run at base (3 of 4 and 3 of 5 as expected). Decomposition amended 7: cells 19.
- FB-g-17 merged @dab8535aef; `r4_canonlist.py` 4 of 4, `r4_validator.py` 4 of 4, `r4_flip.py` 4 of 4 at the merged head.
- Census read, not assumed: the canonical bucket's ownership directory holds exactly one object (the 474,726-byte map), so a
  directory-grain scoped row is the key in effect today.
- One ask out (msg after 3917): a generated bucket-policy Allow beside each scoped Deny row instead of nine identity applies.

## Open and parked

- Exec-summary generator's PutObject (`platinum/advisors/*/exec_summary.json`) cannot be a scoped row (Get/List only): a call for
  the CTO at 4b, not yet put.
- Act 3b COO half, the staged act order and the executor's PutBucketPolicy authority read follow the CTO's answer.
- FB-g-15, FB-g-16, FB-g-17 instances and flips at the next drain (override `TREE_COO`).
- Andrew-only: FWD-7 and FWD-8 (DEC-13); the SEV1 text; the AWS Support case if it did not arrive.
- Push state: LOCAL on `box/dell1`.

## 14:30Z to 16:30Z (appended)

| tick | limb | round | act fired |
|---|---|---|---|
| 15Z | L7 / pre-window | 4 | DRIVE FORWARD x many: act 3b built, applied and read; delete grant ruled, built, applied; act 3c and 4b policy applied |
| 16Z | pre-window | 4 | the window runbook, the four staged acts re-homed, the act-4 addenda 1 and 2 (re-pins) |

- **Act 3b:** `FB-g-19` to `FB-g-23` merged and graded; `FB-f-14` APPLIED (4 to 29 statements, FB1); `FB-f-15` close simulation:
  ~FBL read 9 of 9 allowed and 2 of 2 negatives `explicitDeny` from a scratch copy of `r4_sim.py` (three defects of mine, fixed
  @408768aae2; the committed-script re-run is crossbox b717).
- **Row D1-S29** (act-0 grant lacks Delete; D_02 and D_04 never read `Errors`): the CTO ruled both; `FB-g-24`, `-25`, `-26`
  merged; `FB-f-16` APPLIED (three Sids); act-2 ADDENDUM 3 and act-0 ADDENDUM 1 signed.
- **Act 3c and 4b's policy:** `FB-g-27`, `-28` merged; `FB-f-17` (29 to 34 statements) and `FB-f-18` (1 policy) APPLIED by FB1.
- **FB-g-29** census merged: 8 of 9 side-effect free; the performance adapter writes one evidence artifact; the validator needs
  a signed JWT; the exec-summary has no event. The CTO accepted the three reads (ADDENDUM 4).
- **Window:** the runbook (`ledger/WINDOW_RUNBOOK_ROUND4.md`) fixes the order; act 4 is timed inside US trading hours (CTO
  ADDENDUM 3). `r4_oai.py` reads 3 of 3 on the simulated flip; `r4_flipcommit.py` reads 4 of 4 in a scratch worktree.
- **Found, ahead of the window:** the eight IRPT artifacts stage `loaders.py` at a pin, so act 4 needs eight re-pins (COO
  ADDENDUM 2, with eight rehearsal hashes). Asked of the CTO.
- **Rows:** D1-S28 (the standing `check_fence_scoped_rows.py` reads ok=False), D1-S29, ~FBL's S20 (the sim script's defects, fixed).
- **Open for the CTO:** act-4 ADDENDUM 2 of the COO half (re-pins); the c290 SNS routing fix's form (Andrew: the text arrived).
- Push state: box/dell1 is on origin/CLOUD through 57802a7435 (MSTR measured); later commits LOCAL.


## 17:20Z tick (B1)
- FB-g-35 @f55374d418, FB-g-33 @d8fd43457a, FB-g-34 @dd6d2e5df2 merged and graded (r4_modeenv arm E3 relaxed for the merge form: row W57-S1 a check defect, ruled). FB-g-35 order FB-f-20 sent to ~FBL (99a0), acked 17:15:07Z, running.
- d701: ~FBL own line: earliest start Mon 2026-10-12 13:45Z, waits for the GO commit; act 2 condition (ack with time) met.
- FB-f-13 re-faced as acts 4b/4c for ~FB1 (parked); r4_execeq.py built (DIFFER pre act 3: 194 vs 192, expected); FB-g-36 (partners events) worker 58 in flight.
- NEXT: merge worker 58; FB-f-20 close; window GO Monday per runbook (a chain ended, FB-g-36 merged).

## 17:31Z tick (B1)
- FB-g-36 @5e684dc53e merged, VALID, complete; FB-f-13 step 9 amended (real id per entity class, 200 denominator).
- FB-f-20 (c290) done by ~FBL 17:19Z (laptop commit 8e2c4a76e6 on origin/box/laptop, ls-remote read): plan 1 to change, diff default_sms_type alone; AC1 Transactional, AC2 50 0, AC3 No changes; no text sent. Graded from the committed evidence (plan.txt, apply.txt, instance); the dell1 identity cannot read SNS attributes, so no independent live read from this seat. 99a0 from-side closed 17:30:30Z (HALF-CLOSED until the to-side record lands).
- Open: real SEV1 publish (Andrew word, CTO asking); window GO Monday.

## 2026-10-12 06:07Z tick (B1)
- Producers chain still writing the legacy home at 06:05Z (7055 keys since 05:50Z, 397 since 05:52:53Z); window not open. Poll monitor running; GO after 12 quiet minutes and the remaining section-0 conditions.
- FB-f-15 re-run: ~FBL committed d6093ad983 (16:20Z Oct 11), AC1 PASS from the committed r4_sim.py: 9 of 9 allowed, 2 of 2 negatives, OAI ok. Graded from the instance; b717 from-side closed 06:06:52Z (to-side not yet recorded); 5cf5 CLOSED-BOTH.

## 2026-10-12 08:20Z tick (B1)
- Act 2 DONE (FB1): MOVE_TS 2026-10-12T06:22:08Z, AC1 20/20, legacy quiet. Act 3 DONE: DEST-VS-MANIFEST EQUAL 53031/0/0/0, ownership key equal (my re-run 07:38Z). Acts 4b/4c DEPLOYED and complete (FB-f-13 @3e8181a764): exec-summary fdPwod..., partners c9FXD84..., mode canonical, sample 8/8 (one case by content hash, claim replayed-prior-artifact; D1-S36 ruled, AMENDMENT 4).
- FB-g-30 flip commit 69679b90e3 merged @49bff125c6 (verify 4/4); FB-g-31 re-pins e274a0e60c merged @ec099f0623 (repin 3/3). ycharts-generate at HEAD carries 3 unreleased YCDGEN/BCKEND commits; built from pre-state branch scratch/r4-act4-ycharts-pin (c4ca0c9a99), hash NeAB50CN equals the rehearsal. CTO 4312 no objection with two conditions (kept ref; relay to dell2 owners), both done.
- NEXT: laptop integrates box/dell1 to CLOUD (MSTR asked); 13:30Z MDPF fire read; un-park FB-f-11 and FB-f-19 at 13:45Z+ (mk_r4_af.py), then step 5 pre-flip reads, act 4, step 7 reads, close.
