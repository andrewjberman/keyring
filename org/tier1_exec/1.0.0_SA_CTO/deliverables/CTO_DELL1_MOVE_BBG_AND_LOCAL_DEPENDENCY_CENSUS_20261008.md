# DELL1 move -- step 3: the census of Bloomberg and site-Z-local dependencies of the five projects (2026-10-08 ~23:5xZ)

**Author:** `1.0.0_SA_CTO~Z`. **Under:** `ANDREW_DIRECT_20261008_225xZ_AMGT_DSGN_RIVALS_TO_DELL1_AFTER_ROUND_CLOSE_AND_BBG_CENSUS.md`
@b7361ceb2a, step 3. **Method:** a read-only census run for this seat. It read 12,094 files across the five project homes, line by
line for the 5 PRDs and 5 `project.json`. It also read 17 root scheduled tasks (13 matching, 7 traced), about 20 code files in part,
the 10-07 and 10-08 pull logs, the 10-08 induction log and the live process list. Items marked INFERRED were not read directly.
**DELL1 has no Bloomberg:** measured on dell1 by `0.0.0_AB_MSTR~DELL1` (bus a0f8808e, 23:06:43Z). It found no `C:\blp`, no terminal
process, nothing on 127.0.0.1:8194 and no `blpapi` module (relay `org/tier0_exec/0.0.0_AB_MSTR~Z/relays/RELAY_20261008_230xZ_DELL1_ANSWERS_AMGT_DSGN_RIVALS_MOVE.md`).

## Verdict

**NOT 100% clear.** The agent seats, cloud Lambdas, portal work and every S3/DynamoDB read move to DELL1 as they are. The
Bloomberg pulls do not: the Terminal and its API listen on site Z only. Neither does AMGT_HARVST's publication collector, whose
session files are bound to this box's Windows user. Four of the five projects have a hard site-Z dependency. DSGN_AMGTV1 has none
of its own; it draws AMGT_RESAPP's served output.

## The dependencies

| project | process | needs on site Z | when | DELL1 as-is? | evidence |
|---|---|---|---|---|---|
| ETFS_RIVALS | holdings collector `rivalfunds.collector_bloomberg --mode daily`, a leg of the daily pull | Terminal, Excel with BQL (`C:/blp/API/Office Tools`), pywin32, Python311, the scheduled task | 11:00Z weekdays | NO | `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:422-459`; `collector_bloomberg.py:386-439` |
| ETFS_RIVALS | enrichment `enrichment_bloomberg --mode daily`: corporate actions, `security_market`, names | Terminal API, the same task | 11:00Z | NO | cmd `:473-509`; `enrichment_bloomberg.py:1-80` |
| ETFS_RIVALS | close-price backfill / history-owed (`FWD-24`) | Terminal | ad hoc, after the pull | NO | `enrichment_bloomberg.py:67-80, :902` |
| ETFS_RIVALS, AMGT_CORPUS | Bloomberg budget ledger | `%LOCALAPPDATA%\opal_bbg_budget` | every BBG call | ONLY-IF it stays beside the Terminal | `bbg_budget.py:38-50`; `model_block_pull.py:2201-2228` |
| ETFS_RIVALS | 5 Lambdas, 2 cloud schedules, marker rules | nothing local; fed by the collector's marker and the enrichment's `security_market` | daily | YES (inputs still from Z) | `infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json` |
| AMGT_RESAPP | price leg `price_axis_pull.py` + `price_series_persist.py` into `opal-harvest-security-metrics` | Terminal API, the same task | 11:00Z, when the Terminal is up | NO | cmd `:352-387`; PRD `:1835-1851` |
| AMGT_RESAPP | `pull_consumer.py`, the page-refresh queue consumer | Terminal; the PRD keeps it on the box | on demand | NO | PRD `:1390-1392` |
| AMGT_RESAPP | hand-run pulls (`model_block_pull`, `research_pulls`, `price_history_pull`, `pull_baba_daily_px`, `bloomberg_fallback.py:195`, `scores/robustness.py:465-473`, `filings/battery.py:507-519`) | Terminal | manual | NO | the files named |
| AMGT_RESAPP | `OpalResearch-ExecManagement` / `-FilingsAnalyzer` (both DISABLED) | scheduled task; a Terminal fallback | disabled | ONLY-IF re-created and no Terminal fallback is needed | each task's `run_batch.cmd` |
| AMGT_RESAPP | Seeking Alpha fetch | session/proxy from Secrets Manager; cookie re-mint by browser | per run | YES (INFERRED); a re-mint needs a browser on DELL1 | `integrations/seekingalpha/config.json` |
| AMGT_CORPUS | task `amgt-induction-daily`: `induction_run --fire`, then model-block `admit`/`refresh` | Terminal; the task; pinned checkout `opal-pinned\amgt-induction-daily\6402de513726`; Python311; log under `%LOCALAPPDATA%\opal\amgt-induction-daily` | 13:00Z daily | NO | the task's action; `induction_scheduled.py:10-16, 98-121` |
| AMGT_CORPUS | research library listing | local OneDrive sync of `...\Asset Management\Research` | each induction | ONLY-IF synced on DELL1 (moot while induction stays on Z) | `lib/research/corpus/library.py:41-71` |
| AMGT_HARVST | `backfill_driver` / `lib.opal_data_harvest run` (live now) | DPAPI session files `.runtime/opal-data-harvest*/secrets/*.dpapi` for this Windows user; Chrome profiles; captcha extension; progress DB and checkpoint | running | NO | harvest `README.md:38-46`; `tab_transport.py:38-53`; PRD `:1108` ("Each publisher has ONE persistent browser profile on the site Z box, and it is the only source of that publisher's session.") |
| AMGT_HARVST | `Opal Data Harvest - Local Publications` (DISABLED); `Continuous Cycle` (unregistered) | scheduled task, working-tree path | disabled | ONLY-IF re-created | `install-schedule.ps1`, `install-cycle-schedule.ps1` |
| AMGT_HARVST | `publication_gold build-mention` | repo JSON + S3 | ad hoc | YES (INFERRED) | `lib/research/harvest/` |
| DSGN_AMGTV1 | portal dev server on 5174, `/ui-walk` | bun, a portal checkout, the walker account's AWS credentials | ad hoc | YES, ONLY-IF bun and the credentials are on DELL1 | `.claude/skills/ui-walk/SKILL.md:29-46` |
| CORPUS, RESAPP | `bloomberg` MCP health check before a fire | the local MCP server on the Terminal API | before each fire | NO (`ok:false` on DELL1) | CORPUS `DECOMP.round3.md`; RESAPP `project.json` |
| RIVALS, RESAPP | graders read the pull log `%USERPROFILE%\opal_bbg_logs` | local file | at grading | NO | RIVALS `round27/SERVED_READ_2026-10-08.after_r27.md`; RESAPP `round77/GROUP_E_NOTES.md` |
| all five | the `opal-gateway-bbg` Teams identity | none (0 references) | -- | YES | census |

**Code delivery to site Z.** The daily pull runs site Z's WORKING TREE (`scheduled_daily_pull.cmd:37`), and the `Opal box-sync` task
moves `origin/CLOUD` into that tree every 30 minutes (INFERRED from `box-sync.sh`'s header). So a DELL1 merge to CLOUD that touches
a producer path above runs on site Z within the hour: **it is a site-Z deploy**. The induction task runs a pinned commit instead and
moves only on a re-register (`schedule_induction.ps1 -Register -Commit <sha>`).

**Latest runs:** 10-07, every leg landed (price leg rc 0, rivals 90/94). 10-08, rc 50 with the Terminal signed out, so the price leg was
skipped and the rivals legs wrote nothing (93/97). Induction 10-08 rc 0.

## The bridge (this seat's recommendation; it is CTO~DELL1's term (2) and MDPF_DEMQUE's C-SITES split)

1. **Named site-Z producers stay on site Z under their present tasks:** the rivals collector, enrichment and backfill; the RESAPP
   price leg, `pull_consumer` and hand-run pulls; CORPUS induction; the HARVST collector; the budget ledger beside the Terminal.
   DELL1 reads their outputs from S3 and DynamoDB, which it can already reach.
2. **One site-Z owner runs them on DELL1's asks.** A DELL1 seat that needs a hand-run pull asks that owner; no DELL1 agent can run
   one. The owner also relays the pull log and the MCP health read, which DELL1 graders cannot open; alternatively graders read
   the S3 markers instead.
3. **A DELL1 change to a producer path is a site-Z deploy.** It carries a never-widen pair that names site Z as the act's box, and
   for induction the site-Z re-register.
4. **AMGT_HARVST's collector stays on site Z** unless Andrew chooses to redo every publisher sign-in on DELL1. That needs new
   session files, browser profiles and the captcha extension, plus a PRD amendment, because FWD-10/13 and `:1108` name site Z. The
   sign-ins are his act (his login).
5. **Disabled tasks** are re-created on DELL1 only if they are re-enabled. The CORPUS library sync on DELL1 is not needed while
   induction stays on Z.

-- 1.0.0_SA_CTO~Z
