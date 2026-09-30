# Session 2026-09-29/30 (site Z): ETFS_RIVALS brief to PRD, the IDVZ peer group, AMGT rulings research, HARVST bot operations -- 4.0.0_SA_CRO~Z

**archetype:** MIXED
**secondary_archetypes:** SCRIBE, VALIDATE, DIAGNOSE, EXPLORE

**Date:** 2026-09-30 02:40Z to 21:10Z (Claude Code session a3a51db9; this serial previously ran as a Codex seat).
**Task Order:** ad hoc (Andrew-direct at this terminal), plus research asks from 1.0.0_SA_CTO~Z (msgs 27006, 27101,
27280, 27290).
**Status:** COMPLETE for every act asked. Two calls are open at Andrew (see Next Steps).

## Objective

1. Startup: `/watcher` and the `org/XXX.md` protocol.
2. ETF holdings brief: background, gap pass, Andrew's rulings, registry fix, handoff to the CTO (L1 to L2).
3. Reverse-engineered trade schedule (Andrew's idea), then the IDVZ rival group expansion (Adam Muller's list).
4. CTO research asks: the FWD-7 partial-coverage denominator; the slash security_key; HARVST publisher routes.
5. HARVST production collection: NopeCHA coverage, token and bot-scoring study, live trials, a playbook for COO~H.
6. Site Z crash dumps; the `/next-calls` default (style-read preview).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `lib/opal_naming.py validate / grade / address / name / generate` | PASS | Registry change validated (0 refusals). 12 generated targets content-identical. The `name()` vs `grade()` disagreement came from the CTO. |
| `lib/opal_naming.py census --repo` | FAIL | Stops at a pre-existing RAISE (`F49ServedAndSourceRead`), so it cannot measure a delta. |
| `.tools/aws` s3api / secretsmanager / ec2 / lambda (read) | PASS | Needed a positive control once: `--query KeyCount` printed "None" for populated prefixes, a false absence caught with a JSON listing. |
| Bloomberg Excel BQL census (`bbg_daily_coverage_census_multi.py`) | PASS / FAIL | IDVZ group 501/501 requests. The PFOE run hit `#N/A Connection` on every date (Terminal logged out). |
| `blp_client.reference_data` DVD_HIST_ALL | PASS | 738 securities, 0 security errors. |
| Playwright + curl_cffi trials (`harvest_botops_trial*.py`) | PASS | Four trials, all recorded. |
| native Grep / Glob / Read | PASS | Most searches. The rail refused raw greps twice; switched to native Grep. |

- **What worked:** measuring before claiming: the dividend match, trust-cookie expiry read from bundles (names only),
  and the IP-vs-cookie discriminator (trials 3 and 3b).
- **What failed:** trial 1's outside-client calls degraded this box's IP reputation for bbg/wsj/barrons. The finding
  was real, and it cost the rest of the day's testing.
- **Gap found:** the Bash tool's PATH arrives Windows-formatted on this box, so every bare command returns 127.
  `inbox-watch.sh`'s printed re-arm command does not quote the space in the path. The `/watcher` skill hardcodes
  `/Users/AndrewBerman`.

## Work Completed (commits, all LOCAL at writing)

- **ETFS_RIVALS L1 to PRD:**
  - `091d502fae`, `5c0494860e`: six-step build order and 14 gap-pass rulings.
  - `d451070fb1`: registry change, `etfs` scope to GENERAL tenancy plus system key `rivalfunds`.
  - `1ad807ce0e`: project named ETFS_RIVALS.
  - `2a1f275a78`, `ffc8563ac1`: revision 3, the trade schedule as foundation at the 0.2% floor.
  - `77c891c869`: five open calls answered (DONE WHEN approved; Bloomberg under R-21; no support mail; any signed-in
    viewer; crash dumps).
  - `9d550730e2`: Lambda names corrected to `name()` output.
- **IDVZ group:**
  - `2090f20a8a`, `85557326fe`, `a0ff624dbd`: census, cash-line measurement, dividend match.
  - `a5dde65360`: midstream brief.
  - `2bc18b60a5`: Addendum A DONE WHEN approved, FWD-1 to cover IDVZ and PFOE.
  - The CTO produced PRD v0.3 (`cbf0cfd6b0`, C-GOLD-MODEL).
- **CTO research (all ruled the same tick):**
  - `784068f4c0`: FWD-7 denominator (ruled `ddcc71fd2d`).
  - `c5ebbb2356`: slash security_key, option (c) (ruled `c9081e03d6`).
  - `c7e4748a07`: HARVST publisher routes.
- **HARVST:**
  - `9473d06426`: cloud design, with Andrew's answers recorded (Bright Data residential IP on EC2 OK; no unlocker;
    consolidation last resort; no licensed feeds; local job on site Z until mature).
  - `f5c3b0dbc7`: bot-ops study.
  - `ca0eab4933`, `7bcc258369`: live trials 1-3b and the playbook for 2.0.0_SA_COO~H.
- **Style read:** `9fc7430875`, the G9 recurrence gate proposal.
- **Crash dumps:** `17c1886b55`. MEMORY.DMP removed (18.7 GB). The dedicated dump settings were removed and
  `C:\dedicateddump.sys` is scheduled for deletion at reboot. The Sentinel dump is protected by SentinelOne.

## Decisions Made

1. A registry scope's bucket must be `opal-data-{scope}`. On Andrew's word the product uses scope `etfs` (moved to
   GENERAL tenancy) and a `rivalfunds` system key.
2. Trade detection excludes cash and currency lines and applies DVD_HIST_ALL corporate actions. Scrip was measured
   immaterial for the IDVZ group.
3. HARVST: volume is not the cause. Cold starts, outside-client refusals and retry loops degrade the IP. Stop at the
   first challenge.

## Blockers

- **BLOCKED (Bloomberg):** blpapi session to 127.0.0.1:8194 failed at ~21:0xZ ("is the Terminal running + logged in?").
  No bbcomm process was listed. The PFOE census returned `#N/A Connection`. Tomorrow's 08:03 ET morning run needs the
  Terminal logged in (Andrew).
- **HARVST IP flag:** as of 19:44Z an anonymous fresh browser on this box was challenged by bbg (PerimeterX) and wsj
  (DataDome). No traffic sent to them after 19:45Z. Recovery is unmeasured until the 05:00 ET first-light test.

## Current State

- **ETFS_RIVALS:** PRD v0.3 at `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`; round 2 at 2.0.0_SA_COO~RV. Round 1's
  BASG thread is live in `opal-data-etfs` (`issuer-site/etfs/bronze/...`, `rivalfunds/etfs/gold/{canonical_shape,
  trade_schedule}/`, page `rivalfunds/etfs/platinum/page/date=2026-09-30/`).
- Evidence folder: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/`, containing
  `IDVZ_GROUP_SOURCE_CENSUS.md`, `TRADE_INFERENCE_FEASIBILITY.md`, `STYLE_READ_PREVIEW_20260930.md` and `scripts/`.
  Raw data under `.runtime/etfs-rivals-idvz-20260930/`, `.runtime/amgt-reconn-daily-census-20260929/`.
- **HARVST:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_{CLOUD_COLLECTION_DESIGN,BOT_OPS_STUDY,BOT_OPS_PLAYBOOK}_20260930.md`;
  trial logs `.runtime/harvest-botops-trial-20260930/`.
- **Registry:** `infra/logic/registry/{scopes,systems}.json` @`d451070fb1`. Generated targets not re-stamped
  (content-identical).
- **Box:** the Excel process pid 35956 (hidden, since 2026-09-29 16:35) was left untouched because its owner is
  unknown.

## Next Steps

- [Andrew] CALL 1: a one-time Windows scheduled task for the 05:00 ET HARVST first-light test (REC yes). CALL 2: the
  Sentinel dump (REC leave). Log the Bloomberg Terminal back in before 08:03 ET.
- [2.0.0_SA_COO~H] Follow `HARVST_BOT_OPS_PLAYBOOK_20260930.md`. No bbg/wsj/barrons traffic from this box before the
  first-light test.
- [2.0.0_SA_COO~RV] Round 2 from C-GOLD-MODEL; the home-producer measurement first (PFOE is not on Bloomberg while the
  Terminal is down).
- [1.0.0_SA_CTO~Z] G9 recurrence gate (`STYLE_READ_PREVIEW_20260930.md` section 3) for the PRD.
- [0.0.0_AB_MSTR~Z] `inbox-watch.sh` re-arm line quoting; `/watcher` skill hardcoded path.
