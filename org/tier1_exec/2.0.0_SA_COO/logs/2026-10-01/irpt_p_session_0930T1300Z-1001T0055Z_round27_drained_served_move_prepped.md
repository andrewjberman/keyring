# IRPT_BCKEND ~P post-crash relaunch to now: rounds 26 and 27 drained, the wrong 49F return found served, the service-principal served move prepped but not built -- 2.0.0_SA_COO~P

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, DIAGNOSE, VALIDATE
**Date:** 2026-10-01 (window 2026-09-30 ~13:00Z to 2026-10-01 ~00:55Z)
**Task Order:** IRPT_BCKEND rounds 26 and 27 workstream ~P (TO-IB-pr-261, pr-263, pr-271, pr-272, pr-273, pr-274; cell IB-pr-275 is the issuer's); IRPT_DASHBD workstream B round 1 (TO-DB-b-1 to b-4)
**Status:** IN PROGRESS -- interrupted by Andrew for this log part-way through cell IB-pr-275
**Push state:** origin CLOUD read at 85a765dbcd (ls-remote, 2026-10-01 00:5xZ). 995f0a53ac is on origin; 22b99e32fd, cc20caf7b8 and abc3f0991c are LOCAL. This seat does not push.

---

## Objective

Relaunch after the 07:52Z reboot, assess state from commits, and continue `/canonical-drive` on IRPT_BCKEND workstream ~P under the
LIVE_ARMS directed row. Also: issue IRPT_DASHBD workstream B on the seating Andrew gave ("COO~P on the backend and bucketing").

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | several content and --files censuses (shared-advisor-router, opal-users-v2, token minters) | PASS | denominators printed; one census ran past 180 s and finished in the background |
| comp-routes | `trace --json` on the perfrp leaf URL | PASS | RESOLVED through shared-advisor-router; source plane only, so the access logs were the oracle |
| comp-which | "authenticated read-only request to a portal /api/scoped route" | PARTIAL | no tool mints a user token; that is correct, and it steered me off scripting one |
| to-pipeline-gate / proof-of-spec-check | on both issuances and three drains | PASS | preflight lines refused once for missing denominators, rewritten |
| safe-merge.sh | three round-27 drains, each with a channel conflict | PASS | union resolution verified by id census (538+2, 540+4, 544+2) |
| commit-gate / naming-gate | every commit | PASS | ruff refused the scan script on style once; the naming gate graded 5 new policy names CONFORMANT |
| iam simulate-principal-policy | 7 roles x 2 actions on opal-users-v2 | PASS | positive control irpt-ycharts-generate-role allowed; 6 implicitDeny |

**What worked:** the access-log scan answered an exposure question no source-plane tool could.
**What failed:** nothing structural. Merges and staged sets by other seats in the shared tree cost about 25 minutes of waiting before the first drain.
**Gap found:** `build-and-upload.sh` has no build-only mode, and it stages a pinned member INTO the source folder and deletes it afterwards. A pin on a file that is committed at its packaged path therefore deletes a tracked file. The build for IB-pr-275 must run in a private worktree.

---

## Work Completed

### 1. Round 26 closed (IRPT_BCKEND ~P)

Issuance f54e17e4c6. TO-IB-pr-261 drained at 18518f52d4 (lib/silver_ids.py shipped where the INF gold chain imports it). TO-IB-pr-263
superseded at ed0be5b557 (row S236: the two twr_daily gap partitions are non-performance days). The pr-242 served move (the
inf-ec2-launch-monitor empty-reason line) applied under packet e0a2f524e4 with the CTO half at 0386ab930c; its A1 observation leg is HELD
in ledger `inf-launch-monitor-empty-reason-a1-observation-20260930` (5449e4ffcf). Drain-end record 6bd17a7d15, merged 299d57ca4d. The CTO
round-26 analysis is `org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round26P.md` @7c9ed807bb.

### 2. Round 27 issued and drained (IRPT_BCKEND ~P)

Decomposition section 25; issuance 22b99e32fd; slots 98, 99, 100.

| order | result | drain |
|---|---|---|
| TO-IB-pr-271 | the served boundary refuses a SERVICE subject selecting a firm outside its allowedFirmIds; a subject with no profile row is refused (amendment 1, c31230ea02); reader closure in all 7 bundles. P27-1-AC1 PASS (2 controls, 7 arms), P27-1-AC2 PASS (7 of 7) | cc20caf7b8 |
| TO-IB-pr-272 | NNA 09-24 rows are Branch A (one client, household 63; Orion re-typed four transaction ids to internal journals). The silver stall is upstream of both Lambdas (no 09-28/09-29 raw; the 09-30 raw landed after the 13:05Z mirror fire). Orion positions accept an as-of date (documentation only, 0 calls) | 690409234b |
| TO-IB-pr-273 | S237 verdict PROPAGATES, but NOT through the IRPT adapter (it reads the holdings gold only); through the ADVI perfrp leaf | 934c157f17 |
| TO-IB-pr-274 | PARKED on `0.6.2_AE_PartnerETL~C` (dark) | -- |

All six criteria and three proofs re-ran PASS / VALID on CLOUD after the drains. The three worker worktrees and branches are removed.

### 3. The wrong 49F return is served (row IRPT_BCKEND-W100-S2)

`s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json` (as_of 2026-09-01, one version) carries the S237
skipped-day error: 0093614544 reads +69.81% (corrected +8.47%), 0027256463 reads -83.34% (corrected +28.47%). The CTO placed the remedy on
ADVI_PERFRP (msg 103403) and asked for one exposure read. Measured on the access logs of the portal distribution
(`s3://opal-data-security/waf-logs/cloudfront-access/`, 4,149 objects, 152,160 request lines, 2026-09-03 to 09-30): the leaf returned HTTP
200 three times (09-26 20:03Z, 09-28 17:58Z, 09-30 18:15Z), two distinct clients, referer /advisor-intelligence. Record and script at
abc3f0991c. NOT measured: who the viewers were, and whether an affected account was selected. No scripted authenticated request was made,
because it would mean minting a user credential. The CTO was told (decision message 00:09Z); Andrew was notified at the terminal.

### 4. IRPT_DASHBD workstream B round 1 issued

Decomposition b6cfb3316e; issuance 51c05d1530 (TO-DB-b-1 to b-4); amendments b5ef7317a3, 995f0a53ac, 2fde2edae3, b116670d7c. The
account_return_daily contract landed for the DS seat at 10939bbfa4. `0.4.0_DS_ClientPlatform~S` holds the DB-b-1 emit: its log c7a1058593
records the outside methodology review Andrew ran, and a defect in MY face (TO-DB-b-1 line 62 makes a matched inter-account cash leg
INTERNAL and so drops it from the account-level flow term; the PRD C-METHOD row does not say that, and `c02_twr_engine.py:84-98` admits
such legs at account grain). Nothing is in S3 under the new gold prefixes.

### 5. Cell IB-pr-275 (the served move of pr-271): measured and prepped, NOT built

Measured on the seven live zips (all CodeSha256 equal the artifact_sha256 in the source map):
- The seven functions run FIVE versions of served.py. A plain build at HEAD would also ship eight pending members of other cells
  (ycharts-generate 4, export-render 1, status 3) and an undeployed candidate on irpt-narrative.
- The live irpt-narrative boundary has no tenant selection (0 lines), so the S238 hole is absent there. It is excluded from the move.
- Six of seven roles cannot read opal-users-v2. Without a grant the boundary fails closed and refuses every service principal, its
  allowed firm included.
- The candidate shape "live bundle + served.py at HEAD + reader closure" imports cold, returns the same three refusal envelopes as live,
  and passes the 7 arms inside each of six bundle layouts. The real reader returns `['cottonwood']` for svc-irpt-analysis.

Prepped at b217896d65 on branch `coo-p-pr275` (worktree DIR `C:\Users\AndrewBerman\Desktop\coo-p-pr275`, LOCAL, NOT merged): served.py
re-pinned to f6c6b56f40 in seven map rows; eight members pinned to their live bytes; `service_profile_read.tf` in the performance,
directory, export, holdings and ops roots (plan-first, not applied).

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Use the access logs, not a scripted request, for the exposure read | A human token is RS256-signed by the login service; scripting one is minting a credential. The logs are the real viewers and their real requests. |
| Ship only the boundary and reader closure in IB-pr-275 | Never-widen: pending members belong to the windows of their own cells. Pinned by content to live bytes. |
| Exclude irpt-narrative | No selection branch on its live boundary; its candidate is another deploy. Its map row is re-pinned so the candidate cannot arrive without the refusal. |
| Build in a private worktree | The builder deletes pinned files it staged; unsafe in the shared tree. |
| Do not lift the hold the DS seat set | The method is under direct review by Andrew; only the wrong flow-term reading in the face is the issuer's to correct. |

---

## Files Modified

See commit messages: 22b99e32fd, c31230ea02, 934c157f17, 690409234b, cc20caf7b8, abc3f0991c (IRPT_BCKEND); b6cfb3316e, 51c05d1530,
b5ef7317a3, 995f0a53ac, 2fde2edae3, b116670d7c, 10939bbfa4 (IRPT_DASHBD); b217896d65 (worktree branch only).

---

## MCP traffic

About 30 messages in the window. Significant: CTO 103318 (S238 ruling), CTO 103370 (deployed-layout issuer rule), CTO 103403 (S237 remedy
placed on ADVI_PERFRP, exposure read ordered), my decision reply at 2026-10-01 00:09Z (200, served); DS~S 103401 (vendor overlap 1 pair).

---

## Blockers

- **BLOCKED on Andrew:** the remedy for the served perfrp figure sits behind the D2 hold he set on ADVI_PERFRP (CTO 103403). Evidence: record at abc3f0991c.
- **BLOCKED on Andrew:** the DB-b-1 emit, held by `0.4.0_DS_ClientPlatform~S` pending his method review (log c7a1058593).
- **GATED:** any apply for IB-pr-275 needs the packet and both halves; the packet is not yet written.

---

## Current State

- CLOUD carries rounds 26 and 27 of workstream ~P fully drained. Round 27 is NOT closed: IB-pr-275 is open, TO-IB-pr-274 is parked, and no
  drain-end record or L10 slug exists for round 27.
- ARMED rows owned by this lane: W100-S2 (served perfrp figure; remedy placed, the hold is with Andrew), W99-S3 (the daily eclipse-prefix
  raise in the mirror would hide a real orion-row failure; routing to the CTO not yet sent), S238 (disarms on the served move plus the
  negative control ~Y runs), S216 (fact_positions stalled at 09-27), W86-S2 (launch-monitor observation).
- IB-pr-275: branch `coo-p-pr275` @b217896d65 is unmerged. NOTHING is built, uploaded or applied. No ledger is open for it. The live
  functions are unchanged (CodeSha256: adapter `+h/AH/RY..`, directory `s0riHZ9h..`, ycharts-generate `inrij6hL..`, export-render
  `BORQ2shb..`, holdings `U4/P5Bh3..`, status `ZYr+IDMp..`, narrative `es/S9azu..`).
- NNA Branch A: the excusal packet (accounts 866, 769, 1096, partition 2026-09-24) is NOT written. `nna_coverage_excusals.json` is
  unchanged (7 accounts; the deployed copy is identical).
- Held ledger `inf-launch-monitor-empty-reason-a1-observation-20260930`: record the first stop log line after 2026-09-30T16:19:48Z by
  2026-10-01 11:20Z, then close.
- Scratch outside the repo, for a human to delete: DIR `C:\r27c`, DIR `C:\r27d` (extracted live zips), and the `cflogs` DIR in the session
  scratchpad (access logs with client addresses).
- The inbox watcher Monitor is armed (re-arm on each expiry notice).

---

## Next Steps

1. **[`2.0.0_SA_COO~P`]** IB-pr-275: open a ledger; merge `coo-p-pr275`; build and upload the six artifacts from the private worktree and
   restore the eight files the builder deletes; member-equal census against live; fresh plans for five roots; write the packet (six
   functions, five grants, narrative excluded, the three functions whose boundary catches up several commits named); ask both halves.
2. **[`2.0.0_SA_COO~P`]** Amend the TO-DB-b-1 flow term at account grain (EXTERNAL plus inter-account legs with pair-match or
   text-counterpart provenance) and file the row in the IRPT_DASHBD channel; tell `0.4.0_DS_ClientPlatform~S`.
3. **[`2.0.0_SA_COO~P`]** Write the NNA Branch A never-widen packet (three literal keys) for the CTO to sign on read.
4. **[`2.0.0_SA_COO~P`]** Route W99-S3 (eclipse-prefix class) and the mirror re-time question to `1.0.0_SA_CTO` as one decision.
5. **[`1.0.0_SA_CTO`]** Confirm the ADVI_PERFRP remedy cell is cut by base `2.0.0_SA_COO` once Andrew lifts the hold (asked 00:09Z).
6. **[`2.0.0_SA_COO~Y`]** W27 stays gated on IB-pr-275. The live pins on ycharts-generate and status are for that lane to drop when it
   ships the pending members.
7. **[Andrew]** Word on the D2 hold (ADVI_PERFRP) and on the DB-b-1 method.
