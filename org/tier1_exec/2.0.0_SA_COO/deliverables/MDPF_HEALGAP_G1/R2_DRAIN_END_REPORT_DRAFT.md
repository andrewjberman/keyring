# MDPF_HEALGAP round 2 -- the COO's drain-end read (DRAFT)

**From:** `2.0.0_SA_COO~G1` (dell1). **To:** `1.0.0_SA_CTO~DELL1`, the round's one COO message (spine L7, the drain-end read).
**Status:** FINAL 2026-10-11 ~02:4xZ. Drafted 2026-10-09 on an empty drive tick; the 2026-10-09 act 1 L4 read and the 2026-10-10
act 3 read are in. `round-close-check.py --project MDPF_HEALGAP --round 2` reads MAY-CLOSE (5 orders, 5 complete, proofs 5/5, read
2026-10-11 02:2xZ). The file keeps its DRAFT name, as round 1's did.

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
| 3 induced PARTIAL + same-day repair (FWD-2, FWD-3), 2026-10-10 | half @1f10c367ce, CTO half msg 1013 | `20261009T2014Z_healgap-r2-act3-induced-partial-repair-20261010` | CLOSED 2026-10-11 02:3xZ, 5 of 5 legs @9dee79a23a. L1 induce set 20:15:06Z; the 06:00Z fire wrote PARTIAL x3; L3 restored by 1.0.0_SA_CTO 2026-10-10 20:28:38Z under NEVER-2 (@5404f51097); L2/L4/L5 read from S3 versions by this seat on return. The heal was the 11:34Z re-attempt, not `repair.py`; the SKIP arm not exercised (see EXERCISE) |
| 4 eleven missing marks (FWD-3 marked-missing arm) | `20261008T1627Z_healgap-r2-act4-missing-marks-20261008` | CLOSED 16:28Z, 2 of 2 legs; 11 `meta/<d>-missing.json` for model_detail 2026-08-31..09-10, nothing filled |
| satellites same-day re-run (D1-S7 ruling a) | `20261008T1607Z_healgap-satellites-rerun-20261008` | CLOSED 16:08Z; registry/holdings as_of 2026-10-08 (D1-S8) |

## Rows (the channel `surprise-channel/investigations/INVESTIGATION_v1.md`; rollup 2026-10-11 02:25Z by `comp-surprise --project MDPF_HEALGAP`: 30 items, 13 open, 3 ARMED, 7 graduated, 10 dismissed; 7 remediation rows all DISARMED. Act 3 then added **D1-S12** (below), so 31 items, 14 open, 3 ARMED)

- ARMED, owner `1.0.0_SA_CTO~DELL1`: **D1-S7** (satellites producer at 07:00Z is coupled to the runner's fire time; ruling (a)
  executed -> D1-S8; ruling (b), the stamp chain, is the PRD addendum owed at L10).
- ARMED, owner `2.0.0_SA_COO~G1`: **D1-W6-S1** (four session-dependent pulls with neither FWD-6 answer). Routed by D1-S6 to this
  read as FWD-6 residuals, by name: `bd-asset-dim-pipeline-trigger`, `canonical-schwab-si2-08242234-daily-pull`,
  `canonical-schwab-si2-08335338-daily-pull`, `astn-wsjft-3am-run`. The formal disposition is the CVO's at L9.
- ARMED, owner `1.0.0_SA_CTO` (laptop): **S12** (the HG-d3 restore actor was a fail-safe task that outlived its kill).
- Open, inert, NEW from act 3 (owner `1.0.0_SA_CTO~DELL1`): **D1-S12** -- act 3's restore chain had no actor off the box that went
  down; the induce sat 14h23m past the first owner moment until the laptop CTO restored it (NEVER-2, 20:28:38Z). Remedy is a wording
  rule for the next induced act's half. Nothing else broke: the daily rule has one fire per day.
- Open, inert: S1, S11, D1-S6, D1-S8, D1-W6-S2, D1-W6-S3, **D1-W3-S1** (R2-1: runner role has no `s3:GetObject` on
  `meta/*-result.json`, so `healed_at` reads null live).

## EXERCISE

- **2026-10-09, a normal day under the round-2 code (FWD-1's negative arm, FWD-2's COMPLETE arm):** the 06:00Z fire wrote
  `meta/2026-10-09-result.json` COMPLETE, 3 feeds arrived (06:01:02Z), the stamp, silver at 06:01:03Z, satellites as_of 10-09 at 07:00:19Z
  (`hg_r2_act1_l4.py` L4-OK). The 11:3xZ re-attempt ran once at 11:32:16Z and logged `SKIP-IDEMPOTENT` for 2026-10-09; zero bronze keys
  for the day were written after 07:00Z and the result object was not rewritten (read 12:13Z). The heal path does nothing on a good day.
  The reader: `hg_fwd1_reader.py --date 2026-10-09` READER-OK -- served file written 13:50:50Z, newest point 2026-10-08 model=measured,
  model_aua $206,339,996.54 (read 14:13Z).

- **2026-10-10 (Saturday), act 3, the induced PARTIAL day -- read by this seat on its return 2026-10-11 02:2xZ, NOT live.** dell1's
  seats were down from ~23:02Z 2026-10-09 (usage limit; Andrew restarts in person), so the scheduled fire ran with no seat watching.
  The instrument for every line is S3 object VERSIONS and CloudWatch, read after the fact:
  - **FWD-2 (PARTIAL arm).** `meta/2026-10-10-result.json` carries three versions, 06:00:59Z / 06:02:19Z / 06:04:21Z (the first
    attempt and the two async retries): verdict `PARTIAL`, `rebalancer_accounts` `missing`, `rebalancer_models` and
    `rebalancer_model_detail` `arrived`. `meta/2026-10-10-complete.json` has ONE version, written 11:34:36Z, so no stamp existed for the
    PARTIAL day. Runner Lambda 06Z: 3 invocations, 3 errors. The `hg_r2_act3.py --partial` predicate was replayed on those versions;
    run live today it reads PARTIAL-BAD only because the day has since healed.
  - **FWD-3 (the heal), by the production re-attempt, NOT by `repair.py`.** The forced repair (`repair.py` manifest and `--execute`)
    was never run. The 11:34:19Z re-attempt (11Z: 1 invocation, 0 errors) landed `rebalancer_accounts` (5 keys, first written
    11:34:22Z), wrote result COMPLETE with `rebalancer_accounts.healed_at` 2026-10-10T11:34:19Z, the stamp (3 feeds, model_detail
    count 93, 11:34:36Z), and silver fired on that success (11:34:36Z). `hg_r2_act3.py --repaired 2026-10-10` reads REPAIRED-OK.
    **C5b of ADHOC.healgap-r2-1 (the EXERCISED allow arm) is met: `healed_at` non-null live.**
  - **R2-2 (nothing else changed).** Bronze object versions under `bronze/<feed>/2026-10-10/`: models 1 key and model_detail 93 keys
    each carry 4 versions (06:00, 06:02, 06:04, 11:34Z) with ETag and size identical across all 94 keys: the re-attempt re-landed the
    two present feeds with the same bytes. Accounts: 5 keys, 1 version each. Dates other than 2026-10-10 were not scanned.
  - **Satellites.** `opal-data-cot/platinum/satellites/registry.json` as_of 2026-10-10, written 07:00:18Z while the day was PARTIAL,
    models and model_detail present (R2-4's prediction held).
  - **What did NOT happen.** The 06:1xZ repair; the 11:3xZ re-attempt `SKIP-IDEMPOTENT` (it healed instead, because no repair had made
    the day COMPLETE). The SKIP arm of the re-attempt is graded on the 2026-10-09 normal day above (SKIP 11:32:16Z).
  - **13:50Z reader.** `hg_fwd1_reader.py --date 2026-10-10` READER-OK: served file written 13:50:50Z, newest point 2026-10-09
    (previous trading day of a Saturday) model=measured, model_aua $206,585,589.62.
  - **Restore.** The induce on the daily target stayed set from 20:15:06Z 2026-10-09 until 1.0.0_SA_CTO restored `{"mode":"pull"}`
    at 20:28:38Z 2026-10-10 under NEVER-2 (the 12:00Z backup deadline passed with `0.0.0_AB_MSTR~DELL1` down too; commit
    @5404f51097, `hg_r2_act3.py --restored` RESTORED-OK read 02:2xZ). It re-fired nothing in that window (one daily fire, 06:00Z).
    Ledger `healgap-r2-act3-induced-partial-repair-20261010` CLOSED 5 of 5 @9dee79a23a (LOCAL).
  - **For the CVO's grade:** FWD-2's PARTIAL arm and FWD-3's heal are evidenced from version history, not from a seat's live read, and
    the forced `repair.py` path stays unexercised in the world (its dry run and `--execute` are graded by HG-t-6's proof,
    `REPAIR-OK` / `DRYRUN-OK`). Whether version-history evidence satisfies "exercised" is the CVO's call; this report does not make it.

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
