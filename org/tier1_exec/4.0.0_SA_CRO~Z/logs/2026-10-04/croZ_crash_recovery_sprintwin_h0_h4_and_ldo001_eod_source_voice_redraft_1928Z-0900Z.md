# Crash recovery, NFRA_SPRINTWIN H0-H4 built and deployed, LDO-001 End of Day source, voice and republish redraft -- 4.0.0_SA_CRO~Z

**archetype:** MIXED

**Date:** 2026-10-04 (session 19:28Z to 2026-10-05 ~09:00Z)
**Task Order:** NFRA_SPRINTWIN (solo build, Andrew-direct ~18:4xZ); LDO-001 ad hoc (Andrew-direct ~22:0xZ onward)
**Status:** COMPLETE (round 1 of NFRA_SPRINTWIN; the LDO-001 asks). Round 2 of NFRA_SPRINTWIN is listed by 1.0.0_SA_CTO~Z.

---

## Objective

Recover state after the SentinelOne crash (site Z rebooted 18:58Z), then on Andrew's word drive NFRA_SPRINTWIN's round-1
thread H0-H4 to a live run; then trace where the Kimi Teams End of Day post reads from, make it read the sprint list, remove
every hyphen and dash from its voice, and redraft when the sprint page is republished.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'daily-sprint-generator' org/critical_paths docs/deployment --files` | PASS | found the four prior image deploy records; the 09-24 one gave the build/replace/verify recipe |
| comp-find | `comp-find --corpus aws 'codebuild' --limit 25` | PASS | 5 CodeBuild projects, none for the sprint image; ruled out a cloud build, laptop builds it |
| comp-find | `comp-find -i 'kimi.{0,60}teams\|teams.{0,60}kimi' --files --limit 50` | PASS | 14 hits; led straight to data/transcripts/scripts/teams_chat/ |
| comp-find | `comp-find 'teams-chat-assist' --files --limit 30` | PASS | build.sh, the transcripts TF root and both LDO-001 deploy records |
| comp-find | `comp-find -i 'kimi' --files --limit 80` | PARTIAL | 15,952 hits; too broad to act on, the narrowed regex above was the useful one |
| python lib/opal_naming.py validate | after the sprint row | PASS | OK at 52 system rows |

**What worked:** comp-find's file-name band (HEAD) on the change_management folder; the aws corpus for "is there a build path".
**What failed:** the rail hook blocks a `| head` receiver on comp-find (use --limit) and any `.tf` grep under infra/ (used Read).
**Gap found:** nothing answers "which index entries did my drain leave stale" -- found by `git status` MM by hand (row Z-S5).

---

## Work Completed

### 1. Crash recovery (19:28Z)
- /watcher: registered (PID 19916), Monitor armed; inbox 29189 (COO~X: stale AMGT_CORPUS index cleared) read and acked.
- State from git + telemetry (the prior session's transcript did not survive): brief + two Andrew-direct records on branch
  `croz-sprint-census-20261004`, not on CLOUD; the drain had been blocked by 5 stale index entries. Drained @4d54d7b096.

### 2. NFRA_SPRINTWIN round 1, H0-H4 (Andrew ~19:4xZ "proceed with your merge and then get right into H0-> H4")
- **H0** @4201d79857: `sprint` PLATFORM_SUBSYSTEM row (owner D0, measured). Homes pinned in PRD C-HOMES @8032cd9a61:
  census `s3://opal-data-assets/sprint/global/bronze/device_census/date=<D>/<device>.json`, QA home
  `s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=<D>/`; names sprint-generator-daily, sprint-scheduler-role.
  The row made the PRD v0.1 `opal-...` names unresolvable; pinned name('sprint', ...) output.
- **H1** @6ff1077ddd, fix @3deb2c4b6b: `.tools/sprint-device-census.py` (8-day look-back, git's own formats, read-back put).
  Fix: the address builder and registry are exported from origin/CLOUD, not the working tree (laptop failure, row Z-S3).
- **H2** @493b50dde5: both census scripts take `--since/--until` (half-open) and `--extra-commits`; one classify over the union.
  D3a control on a pushed day: 706/706 commits same kind, directive, bin and file list.
- **H3** @dc86c2b2cd: the function cuts the window from the watermark (window_end = earliest reporting census, CVO~Z finding 1),
  unions every census file in the window (finding 2), zoneinfo New York, QA home, source line naming devices and unpushed count.
- **H4** @608559d4fe: chart hour labels from the window start (row Z-S1).
- **C-WINDOW local half** @be11470de0: `/daily-sprint` uses the served watermark's pair (`--census-args`).
- **Deploy** (ledger sprintwin-union-20261004, CLOSED @709caf16b1): image sha256:4e5987ce (laptop build from 740fb88d8b, in-image
  blob d284642a32), safe-apply 2 added / 1 changed / 2 destroyed, re-plan No changes.
- **QA trace (FWD-1)**: 386 commits, 50 unpushed (laptop 48, sitez 2), both devices; daily-reports/ untouched (69 = 69).
- **Served re-run of 2026-10-04** (Andrew ~21:3xZ via MSTR~Z; addendum A, both halves extended): seed watermark 10-03 22:16Z,
  window 10-03 18:16 ET to 10-04 17:34 ET, 356 commits, 58 unpushed; exactly 4 keys touched.
- Never-widen pair: CTO~Z @e92e21fef3 (5 conditions; 1(b) relayed and acked by the laptop), COO~H @740fb88d8b.
- CTO~Z round-1 analysis @94a34c849d: FWD-1 REALIZED; round 2 = FWD-4, per-run census keys (PRD v0.3), FWD-2, FWD-5, FWD-6,
  FWD-3, FWD-7 (with Z-S2 as its negative arm), then Z-S4 and opal_ai UNAVAILABLE.

### 3. LDO-001, the Kimi Teams End of Day post (Andrew ~22:0xZ, ~22:2xZ, ~22:4xZ)
- **Trace:** the draft reads the served page's embedded report, ONCE, the first minute it exists after 4 PM. 10-03 drafted
  21:01Z from a 0-commit page (replaced 22:30Z, 422); 10-04 drafted 20:13Z from 12 commits (replaced 21:55Z, 356). S3 versions
  read back. Deployed code == repo (no drift).
- **Source + voice** @f9ba6ba8a8 (deployed 22:30Z, ledger ldo-001-eod-voice-20261004): facts are the sprint list only, one
  bullet per item; `no_dashes()` on every Kimi draft (post and chat), check_post refuses a dash; VOICE.md and CHAT_SYSTEM rules.
- **Republish redraft** @55cb79f93c (deployed 23:04Z, ledger ldo-001-eod-republish-20261004): page ETag per draft; the
  ingress sends `eod.sprint_updated` once per publish; an open draft is redrafted and re-texted; an approved post is withdrawn.
  Live tick 23:05:21Z: one event, handler `nothing-open` (the day was posted).
- Tests: 101 -> 127 passed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| QA home tier `platinum` | gold and state refuse for scope global under a non-product source (tiers.json) |
| boto3 for the device census put | already installed on both devices; avoids the aws CLI's MSYS argv boundary |
| Seed watermark 10-03 at 22:16:00Z | the served 10-03 page cut at 18:15 ET; 0 commits in [22:15Z, 22:16Z) on any ref and in both censuses |
| Keep the bullet marker "- " in the End of Day post | it renders as <li>, never as text; dropped in plain chat replies |
| A republish withdraws an approved post | nothing posts on words Andrew did not read (the human-in-the-loop rule) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/logic/registry/systems.json` | sprint row | Yes, 4201d79857 |
| `.tools/sprint-device-census.py` | new; pinned builder | Yes, 6ff1077ddd, 3deb2c4b6b |
| `daily_reports/scripts/{commit,project}_census.py` | window + union | Yes, 493b50dde5 |
| `infra/aws/lambda/daily_sprint_generator/lambda_function.py`, `infra/aws/terraform/daily-sprint-generator/main.tf` | H3 | Yes, dc86c2b2cd |
| `daily_reports/templates/_shared_viz.js` | hour labels | Yes, 608559d4fe |
| `.tools/daily-sprint.py`, `.claude/skills/daily-sprint/SKILL.md` | --census-args | Yes, be11470de0 |
| `daily_reports/eod/{post_format.py,VOICE.md}`, `data/transcripts/scripts/teams_chat/{assist,tenant}.py` + 2 test files | LDO-001 | Yes, f9ba6ba8a8, 55cb79f93c |
| NFRA_SPRINTWIN surprise channel | rows Z-S1 to Z-S5 | Yes |

All on origin CLOUD 41158af7f9 (ls-remote read at 03:04Z), and unchanged by the laptop merge 5b5170554c.

---

## Blockers

None at this seat.

---

## Current State

- NFRA_SPRINTWIN: round 1 closed (FWD-1 REALIZED by CTO~Z). The new image runs; tomorrow's 4:10 PM ET fire is the first
  scheduled union publish, covered by the signed pair. Round 2 waits on the next issuance.
- LDO-001: running the sprint-list source, the no-dash voice and the republish redraft; the 2026-10-05 post is the first draft on it.
- Open hazards: Z-S2 (empty pinned copy, binds FWD-7), Z-S4 (break_after type, template owner), Z-S5 (stale index after
  safe-merge, tool owner 2.0.0_SA_COO).

## Next Steps

1. **[4.0.0_SA_CRO~Z]** On round 2's issuance: FWD-4 first, then per-run census keys (PRD v0.3), FWD-2, FWD-5, FWD-6, FWD-3, FWD-7.
2. **[4.0.0_SA_CRO~Z]** Read the 2026-10-05 20:10Z scheduled fire's result and the first LDO-001 draft on the new code.
3. **[2.0.0_SA_COO]** Z-S5: whether safe-merge leaves the shared index stale after every drain.
