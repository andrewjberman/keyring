# MDPF_HEALGAP round 2 -- the COO's drain-end read (DRAFT)

**From:** `2.0.0_SA_COO~G1` (dell1). **To:** `1.0.0_SA_CTO~DELL1`, the round's one COO message (spine L7, the drain-end read).
**Status:** DRAFT 2026-10-09 ~01:3xZ, written on an empty drive tick (`/next-calls MDPF_HEALGAP --drive`) ahead of the two
event-gated reads. Sections marked `PENDING` fill from the 2026-10-09 06:00Z fire (act 1 L4) and the 2026-10-10 act 3. Not sent.
Before FINAL: `round-close-check.py --project MDPF_HEALGAP --round 2` must read MAY-CLOSE.

## The round

- Cut on PRD v0.2; decomposition `decompositions/MDPF_HEALGAP_DECOMP.md` ROUND 2. Drain plan and issuer rulings R2-1..R2-4:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_DRAIN_PLAN.md`.

| order | what | risk | state |
|---|---|---|---|
| HG-t-3 | per-feed run result + `PartialDay` (FWD-2) | WORLD | complete, drained @c468b71b6d |
| HG-t-4 | retry settings made true (FWD-4) | WORLD | complete, drained @672800c42a |
| HG-t-5 | daily fire after the session refresh (FWD-5) | WORLD | complete, drained @672800c42a; NOT APPLIED -- HELD on D1-S7 (CTO 51c9c0e64a 3b); live rule stays `cron(0 6 * * ? *)` (CTO msg 1154: intended) |
| HG-t-6 | repair act + missing mark (FWD-3) | WORLD | complete, drained @7ede39f044 |
| HG-t-7 | session-dependent pulls census (FWD-6) | LOCAL | complete, drained @a0ee7928f1 |

## Drain acts (each under its own never-widen pair and change-management entry)

| act | entry | state |
|---|---|---|
| 1 runner code (HG-t-3 + `induce` drop-feed) | `20261008T1618Z_healgap-r2-act1-runner-code-20261008` | CLOSED 2026-10-09 07:1xZ, 4 of 4 legs. L4 (`R2_CHECKS/hg_r2_act1_l4.py --date 2026-10-09`): L4-OK -- result COMPLETE, 3 feeds arrived (the first result object written live); stamp 3 feeds, model_detail 93; silver first event 06:01:03Z; satellites as_of 2026-10-09 at 07:00:19Z. Controls: 10-08 L4-BAD; 10-07 SILVER/STAMP ok. Act 3 precondition (branch A) MET |
| 2a event age 900 (HG-t-4) | `20261008T1611Z_healgap-r2-act2a-event-age-20261008` | CLOSED 16:13Z |
| 2b fire time (HG-t-5) | -- | HELD, not applied (above) |
| 3 induced PARTIAL + same-day repair (FWD-2, FWD-3), 2026-10-10 | half @1f10c367ce, CTO half msg 1013 | `PENDING`. Precondition: act 1 L4 reads branch A. Step 1 ~2026-10-09 20:00Z (announce to `0.0.0_AB_MSTR~DELL1`, `PutTargets` drop-feed:rebalancer_accounts). Staged read 2026-10-09 01:2xZ: daily rule has 1 target, input `{"mode":"pull"}` |
| 4 eleven missing marks (FWD-3 marked-missing arm) | `20261008T1627Z_healgap-r2-act4-missing-marks-20261008` | CLOSED 16:28Z, 2 of 2 legs; 11 `meta/<d>-missing.json` for model_detail 2026-08-31..09-10, nothing filled |
| satellites same-day re-run (D1-S7 ruling a) | `20261008T1607Z_healgap-satellites-rerun-20261008` | CLOSED 16:08Z; registry/holdings as_of 2026-10-08 (D1-S8) |

## Rows (the channel `surprise-channel/investigations/INVESTIGATION_v1.md`; rollup 2026-10-09 01:14Z: 27 items, 10 open, 3 ARMED)

- ARMED, owner `1.0.0_SA_CTO~DELL1`: **D1-S7** (satellites producer at 07:00Z is coupled to the runner's fire time; ruling (a)
  executed -> D1-S8; ruling (b), the stamp chain, is the PRD addendum owed at L10).
- ARMED, owner `2.0.0_SA_COO~G1`: **D1-W6-S1** (four session-dependent pulls with neither FWD-6 answer). Routed by D1-S6 to this
  read as FWD-6 residuals, by name: `bd-asset-dim-pipeline-trigger`, `canonical-schwab-si2-08242234-daily-pull`,
  `canonical-schwab-si2-08335338-daily-pull`, `astn-wsjft-3am-run`. The formal disposition is the CVO's at L9.
- ARMED, owner `1.0.0_SA_CTO` (laptop): **S12** (the HG-d3 restore actor was a fail-safe task that outlived its kill).
- Open, inert: S1, S11, D1-S6, D1-S8, D1-W6-S2, D1-W6-S3, **D1-W3-S1** (R2-1: runner role has no `s3:GetObject` on
  `meta/*-result.json`, so `healed_at` reads null live).

## EXERCISE

- **2026-10-09, a normal day under the round-2 code (FWD-1's negative arm, FWD-2's COMPLETE arm):** the 06:00Z fire wrote
  `meta/2026-10-09-result.json` COMPLETE, 3 feeds arrived (06:01:02Z), the stamp, silver at 06:01:03Z, satellites as_of 10-09 at 07:00:19Z
  (`hg_r2_act1_l4.py` L4-OK). The 11:3xZ re-attempt ran once at 11:32:16Z and logged `SKIP-IDEMPOTENT` for 2026-10-09; zero bronze keys
  for the day were written after 07:00Z and the result object was not rewritten (read 12:13Z). The heal path does nothing on a good day.
  The reader: `hg_fwd1_reader.py --date 2026-10-09` READER-OK -- served file written 13:50:50Z, newest point 2026-10-08 model=measured,
  model_aua $206,339,996.54 (read 14:13Z).

`PENDING` -- act 1 L4 (2026-10-09 06:00Z/07:00Z) and act 3 (2026-10-10): FWD-2 read of the PARTIAL result object, FWD-3 repair
read (COMPLETE, R2-2 before/after key sets of the two present feeds), the 11:3xZ SKIP, the 13:30Z floor and 13:50Z reader.

## For the round-2 analysis (enrichment list, three items already ruled ahead of the slug)

- **R2-1 (D1-W3-S1) -- PULLED FORWARD, not round 3:** decomposition round 2 amendment A1 (cell HG-t-8), carried by
  `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/ADHOC.healgap-r2-1-runner-reads-own-result.md` @15091a3a96 (operator's word at
  this terminal ~05:3xZ; the round-2 issuance was closed to new files). LANDED 2026-10-09 ~07:4xZ (edit ba88934f7b, close 74b0ca41c8):
  live `cot-rebalancer-runner-write-cot` 4 statements, `ReadOwnRunResult` s3:GetObject on `.../cottonwood/meta/*-result.json` (firm read via
  `one(local.monolith_source_scopes.blackdiamond)`, CTO ruling H, after the naming limb refused the typed firm -- row D1-S9). Issuer
  validated: live policy read, `hg_t8_iam.py` IAM-OK, proof-of-spec C1-C8 VALID rc=0. C5a over all five identity carriers (allow /
  implicitDeny x2 / explicitDeny). C5b, the EXERCISED allow arm, is act 3's `--repaired` read (healed_at non-null). Rows D1-S10, D1-S11:
  iam:SimulatePrincipalPolicy is denied to the dell1 principal.
- **D1-S7 (b) -- RULED** (CTO batch @6c538a0bfd section D): the satellites producer keeps cron(0 7) and gains ONE scheduled 12:00Z fire
  that reads the runner's completion stamp and rebuilds only when today's bronze has landed (else one log line, nothing served).
  HG-t-5 is freed under it. Round-3 cells: the 12:00Z fire (producer owner 0.6.2_AE_PartnerETL's code; apply by
  0.7.0_AE_CloudOps~DELL1), then HG-t-5's apply. Negative arm: a day the runner lands after 07:00Z serves the fresh registry from 12:00Z.
- **FWD-6 residuals -- RULED** (section E): round-3 heal cells for `bd-asset-dim-pipeline-trigger` and `astn-wsjft-3am-run` (a
  re-attempt after the session mint, FWD-1's pattern); the two `canonical-schwab-si2` pulls are a KNOWN MANUAL EXPOSURE named on FWD-6's
  grade, the person's re-login listed on open-calls when owed, not a cell.
- For the next cut: an order's surprise-row id format names the fabric coordinate (D1-W6-S3); a half counts every reader of the
  runner's same-day bronze (D1-S7: the satellites producer was missed by every round-1 half); a late-round cell cannot be added to a
  closed issuance as a new file (HG-t-8 went by a CloudOps carrier under an audited override).
