# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FULL: the FAST lease was ended at the 2026-10-05 ~16:2xZ wind-down (device wind-down, Andrew's word); the loop cron is closed.
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` and the fold-in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6, Y-H); run order
CTO 104634 ("Y-3 READY, then Y-5 V1, then Y-4 V1, one at a time and spaced"; then Y-2 and Y-6). Reviewer `3.0.0_SA_CVO`
(grades pins after the fact). As of 2026-10-05T16:2xZ (wind-down). Restart from `logs/2026-10-05/session_close_0000-1630Z.md`.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | IRPT_YCDGEN round 5 drained and closed, L8 packet `043a6cc2d1`; CRO handoff `d87bed6db6`. Branch `y-release-390` @f1e101d19c holds the 390 s release (unmerged; it deploys after Y-6). No worktree held by this seat |
| SERVED: `irpt-ycharts-generate` | `uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ=` (Y5D). Source map recorded at 3a14a49f48, parity (S320 `40417a1b8c`) |
| SERVED: the resident | `/opt/irpt-resident/3f29017cfc-st21` since 02:01:04Z 2026-10-04. Rollback root `136ee09e9f-st20` |
| SERVED: `irpt-status` | `jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE=` since 04:18:20Z 2026-10-05 (S326: history newest first; carries S318). Rollback S3 version `jVkDK9v6..` (`XPta1UMJ..`) |
| SERVED: research principal | `irpt-cot-ycharts-research-role` (Put/Get on Cottonwood's two research tables), assumed by the runner role (CTO batch 239) |
| Stored YCharts session | **EVICTED** (14:41Z and 14:56Z 2026-10-05; Opal employees share the account and a new login evicts it -- Andrew via MSTR 105330). The next page job's own re-login revives it; research runs cannot log in. Firewall window (122, 373] s (WAF-PROBE-W330 @bb1b59c3f6) |
| Push state | LOCAL; origin CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6

1. **Y-3 READY** 2026-10-03 17:03:14Z (a CSV upload with ULT + IWM).
2. **Y-5 READY** 2026-10-04 02:28:20Z (REQ-a618aa83; TIMXX named SGOV). Its page row now reads READY with its date basis
   (S318 closed, V1 00:13Z 2026-10-05).
3. **Y-4 READY** 2026-10-04 03:18:02Z (REQ-0d97252f; the typo file; check gate 15.6 s). Ledger closed.
4. **Y-2 READY** 2026-10-05 01:37:07Z (REQ-c1b53772; the easy file, SGOV, Opal Ultra Long-Term; ~D's page run). Its
   row now lists first in the history (S326, served 04:18Z).
5. **Y-6** (~D, 5 cases x 2 from the page, one at a time):
   - run 1 REQ-777d7546 READY 05:18:26Z (page 18.2 min; open to sections 2.0 s);
   - run 2 REQ-14fe69cf READY (page 06:58:51Z, 17.9 min; open to sections 1.4 s);
   - run 3 REQ-724a493e READY 07:38:14Z server-side (18m40s). The page lost the row from 07:27Z on portal 0edab95f;
     server-side the row is position 0 of 33 (page-side miss, ~D reading its screenshot);
   - run 4 REQ-1352d8c1 READY 08:41:43Z; runs 5-6 (Multi-Comp) READY 09:40:23Z and 10:07:22Z, each read-back
     WAF-challenged and absorbed by the release (`Y6/Y6_BACKEND_SUMMARY.md`);
   - run 7 (Dproxy #1) REQ-6eaec4e9 ended ATTENTION 14:56:22Z, SESSION_REFRESH_ALREADY_USED (evicted twice);
   - runs 8-10: ~D's, hold lifted 15:48Z (an eviction mid-run is recorded as a result). This seat records each run's
     backend states (`IRPT_MVP_Y/Y6/`) and writes the Y-6 evidence at the end.

## IRPT_YCDGEN (this seat issues; FULL lease)

- Round 5 is closed on the build side: 5 of 5 orders merged and complete, 12 of 12 checks PASS (135 tests). The L8
  packet @043a6cc2d1 was sent to `3.0.0_SA_CVO` at 16:14Z and is QUEUED, not yet READ (the CVO session is stale). L9
  owes m-5.AC3.
- Close acts:
  - E4 leg 1 is done (YCD-R5-E4-20261005T1215Z). Leg 2 is the same script (`close/ycdgen_r5_e4_host.sh`) after
    today's close reaches YCharts and the session is live.
  - E6 is held. Its bundle `ycdgen-e6-bundle-fb6c0f63feb7` predates the runner fix @05fc7afa6f, so REBUILD the
    bundle before any rerun.
- **Direction (Andrew-direct ~14:3xZ, @a812d50ff1): rebuild the generation in Opal's cloud, YCharts toward zero.**
  - CTO 105307: 4.0.0_SA_CRO's brief addendum first, then PRD v0.2.
  - Handoff @d87bed6db6; a Desktop copy is at `C:/Users/AndrewBerman/Desktop/HANDOFF_TO_CRO_ONPREM_GENERATION_20261005.md`.
  - Sent to 4.0.0_SA_CRO, whose base session was not registered at send.

## Queued work

**PARKED 2026-10-07 ~07:3xZ by `2.0.0_SA_COO~Y2` (dell2 successor of `~Y`)**, on Andrew-direct ~07:2xZ (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_072xZ_Y2_CHECK_IN_WITH_YCDGEN_NO_DUPLICATION.md`
@d9fd724744: the YCharts port is "tenuous on their connection/auth"; build in house). Every item below tunes the YCharts
vendor path, and IRPT_YCDGEN (PRD v0.8, FWD-11) is the in-house build. The served vendor path stays as it is until
FWD-11 retires it.

**RULED 2026-10-07 ~07:5xZ by `1.0.0_SA_CTO~DELL2` (msgs 91 and 93):**
1. Two lanes stay, with ONE WRITER. `2.0.0_SA_COO~G2` alone writes and releases `ycharts/generate/resident_worker.py`,
   `upload_suggestions.py`, `security_resolution.py` and the resident host. This seat asks for a change to any of them
   as a named cell. The rest of `ycharts/**` that is Y's stays with this seat.
2. The 390 s release is UN-PARKED. It rides `~G2`'s next resident build, after M1. This seat supplied it:
   `deliverables/2.0.0_SA_COO~Y2/release390/` (the patch onto `aaea945582`, the test run still owed on a host with
   PyMuPDF, and the never-widen pair text).
3. STOPPED: Y-6 runs 8-10. No new work on the YCharts session, lease or firewall; only breaks that users see are
   repaired. CORRECTED by msg 104 (08:03Z): Y-5 packet 2 (the K3 swap call in `intake/resolution_kimi.py`) is chassis,
   not the YCharts producer, so it is NOT stopped. It is back to HELD under CTO batch 218, and the CTO re-rules it when
   4.0.0_SA_CRO's research on the check and swap operations lands (Andrew-direct ~08:0xZ, @1ea0796be2). Any live Kimi
   call still needs Andrew's per-use vendor word.
   **SUPERSEDED by msg 120 (08:15Z, `1.0.0_SA_CTO~DELL2`, on the brief
   `docs/briefs/irpt-check-swap-ai-autosuggest-ux-brief-20261007.md` @3d0ecacb0b section 4.1):** Y-5 packet 2 is
   superseded by IRPT_YCDGEN S32 (FWD-16). There, the candidates come from etf-classifications, and the model ranks or
   words them but never invents one. The check and swap UI changes R1-R9 go to IRPT_YCDGEN as a PRD addendum, not to
   this workstream.
4. Y stays open until IRPT_YCDGEN FWD-11, then closes with the removal of the YCharts path.

**Round 61 (~Y) CLOSED 2026-10-07 ~09:0xZ:** E-Y1 @ad59d08617 (row S353), E-Y2 drained @1ade2e9989 (owner table: 14 fixtures/har
REMOVE, templates.json KEEP, lane IRPT_COMPLETION_Y), E-Y3 = the release390 hand-over. S339 disarmed (row S351).

**Next Y cell, ruled by `1.0.0_SA_CTO~DELL2` msg 233, PARKED:** drop the 14 `fixtures/har/*` from `irpt-ycharts-generate`'s
`files[]`. Its criteria:
(1) an import/open trace over the package at the pin shows no runtime reader;
(2) the built package has no fixtures/har member, and the tests that read them still pass from the repo;
(3) a planted runtime open is caught by the trace.
It rides the function's next release (if that is `~G2`'s resident build, it rides `~G2`'s).
Owner: this seat. It un-parks when that next release is scheduled AND a host with PyMuPDF (`fitz`) can run criterion (2)'s tests.
dell2 has no `fitz`, so an order cut now would carry a criterion no dell2 worker can meet.

- Y-5 packet 2 (the Kimi swap): HELD by CTO batch 218.
- **Submit-to-READY is mostly a fixed wait.**
  - Y-6 runs 1-3 each spend 15m07s in `READ_BACK_LEASE_TTL_S = 900` (`ycharts/generate/recipe.py:688`, CTO batch 97
    item 4) after one `calculating` read-back.
  - Window measured (122, 373] s. CTO batch 262 YES: the release goes to 390 s. It is built on branch `y-release-390`
    @f1e101d19c (generate 403 passed, offline suite 0).
  - Deploy after Y-6 ends, under a never-widen packet with the CTO's half and a resident build (st22). After-read: the
    first two live jobs show no firewall challenge on either read-back; a challenge reverts to 900 s in the same
    session.

## Rows this lane holds

| Row | State |
|---|---|
| S318 / S321 | DISARMED by S325 (irpt-status serves the pinned-boilerplate proof) |
| S326 | CLOSED (V1 by ~D's page check); disarmed by S329 |
| S284 | DISARMED by S327 (the user-named proxy proven by Y-5 and Y-2; the entitlement stays Andrew's vendor call) |
| S320 | closed (recorder run, parity) |
| S288 | DISARMED by S306 |
| S296, S286, S230, S282 | unchanged (see their rows) |
| S263, S253, S261, S231, W94-S2, W91-S1, W92-S1, W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

None open. Closed: `irpt-s326-history-20261005`, `irpt-y4-20261003`,
`irpt-ycdgen-grant-20261004` (V1 superseded), `irpt-ycdgen-principal-20261004`, `irpt-s318-boilerplate-20261004`.

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/lambda/investor-reporting/intake/{security_resolution,portfolio,resolution_broker}.py`
and their tests; `infra/aws/lambda/investor-reporting/ops/{owned_requests,prospect_dates}.py` and their tests;
`infra/aws/ec2/investor-reporting-ycharts/**`; `infra/aws/terraform/investor-reporting/ycharts/resident.tf`;
`docs/contracts/investor-reporting/v1/routes.json`; the rows of `irpt-status` and `irpt-ycharts-generate` in
`infra/aws/lambda/ci/lambda-source-map.json`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; this file.

## Parked, each with its owner and the condition that un-parks it

- C: is full (1.7 GB free at 10:5xZ). Twelve merged worktrees of ~P and ~M hold ~30 GB. Owner 0.0.0_AB_MSTR (asked
  10:34Z); un-parks when space returns. Until then this seat's workers use sparse worktrees.

- Login and session secret ARNs keep `-*` in the runner role. Owner this seat; un-parks on a CTO ruling.
- The recorder's CHANGELOG entries for irpt-ycharts-generate (S320) and irpt-status (S318) are `2.0.0_SA_COO~P`'s lane,
  handed over as patches. The S320 entry was committed by ~P; S318's un-parks when ~P commits it.
- An uncommitted `irpt-holdings` artifact_sha256 edit in the shared source map is another seat's. It was left untouched.
- Andrew's HAR file `C:\Users\AndrewBerman\Downloads\ycharts.comalyss.har` (outside the repo): its deletion is Andrew's
  (asked); recorded by sha256 and size only.
- The worktree `C:/Users/AndrewBerman/Desktop/wk-ycdgen-2` (round-1 slot ~2; branch merged) holds an untracked `.scratch/`.
  Owner this seat; un-parks on a look at its contents.
- A deterministic ROWS_UNVERIFIED is still retried four times at 60 s. Owner this seat; un-parks if a stray-row refusal
  recurs.
