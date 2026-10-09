# NFRA_CTLPLN workstream INBOUND, rounds 6 and 7 -- L9 grades (on 2.0.0_SA_COO~R msg 107447)

**archetype:** VALIDATE

Packet: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/INBOUND_ROUND7_DRAIN_END_20261008.md` @ac72c4949f, with
round 6's `INBOUND_ROUND6_DRAIN_END_20261008.md` @03d37ff43f. Read by this seat at `box/laptop` HEAD `9cc0e521d0`,
2026-10-08 ~23:1xZ. AWS reads were read-only, through the `.tools/aws` shim.

## CTi11-AC3 (round 6): MET

Artifact: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~39/CHANNEL_READ_SCOPES_MEASURED.md`.

The criterion asks whether the file names, from the code, the scopes requested, the scopes the three paths need, and which are
missing. It does all three. This seat printed every cited range at the issuance base `8f0db50042`, and each one holds:
- `teams_route.py:109`
- `token_broker.py:141-147`, `:162-177` and `:215-226` (the consent cut at `:223`)
- `config.py:61-69` (the Teams line at `:66`) and `:98-103`
- `identity_scope.py:121-143`
- `graph_scope_map.py:33,35,37` and `:98-99`
- `tools.py:1115-1138`

**Requested.** Both base lists carry `Team.ReadBasic.All`, `Channel.ReadBasic.All` and `ChannelMessage.Read.All`.

**Needed.** Each path's scope is taken from the code's own map: `graph_scope_map.py:33,35,37` for `list_teams`,
`list_channels` and `read_channel_messages`, which call the same three Graph paths. The Microsoft pages are labelled "from
memory" and carry no weight in the claim.

**Missing.** None from the base lists. Two would be missing on one condition:
- the condition is that `MS_INGEST_IDENTITY` is a scoped identity;
- in that case the caller map at `graph_scope_map.py:98-99` drops `Team.ReadBasic.All` and `Channel.ReadBasic.All` at
  `token_broker.py:223`;
- that map still reads the same at HEAD.

**One refinement the file missed.** It treats "is the identity scoped" as wholly unreadable. Part of it is in the repository:
the seed `identity_scope._SEED` scopes exactly one identity, `opalbloomberg@opalinvest.com` (line 55 at `8f0db50042`).
`config.py:224` says `MS_INGEST_IDENTITY` is Andrew's. So only a row in the host's overlay file (`IDENTITY_TOOL_ALLOWLIST_PATH`,
default `./identity_tool_allowlist.txt`) can scope it. That narrows the unknown to one host file; it does not change the answer.

## TO-APPLY-19 AC2 (round 6 deploy): MET -- the deploy is as both halves describe

Halves:
- COO: `org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_INBOUND_R6_TEAMS_AGENT_CODE_DEPLOY_COO_R_20261008.md`
  @b07357fa48
- CTO: @1dd8aa70e7

Report: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/teams_r6_20261008/REPORT.md`.

**Branch A.**
- This seat parsed the saved `plan.json`. 2 of 27 resource changes are non-no-op: `module.ldo_001.aws_lambda_function.handler`
  and `.ingress[0]`, both `update`. The only attributes that differ are `source_code_hash` and `last_modified`. There is no
  IAM change and no address outside the module.
- The new hash `M67/KipojF79vIGJTxCmQnDQfVyzws1VGU4OsD+7Yt0=` is the base64 of the built package's SHA-256 `33aeff2a...62dd`
  (decoded by this seat).
- `git diff 79d7b6cbbe 6f7449dbc5` over every path `build.sh` packages is empty, so branch B's packaged-path limb did not fire.

**Live record, read by this seat.** CloudTrail `UpdateFunctionCode20150331v2` events:
- ingress at 21:48:11Z (`ef882395-...`) and handler at 21:48:17Z (`6c769a98-...`), both with `codeSha256` `M67/Kipo...`;
- these follow the 08:15Z deploy (`YYWO/...`), which is the "before" hash the half names;
- there are 0 `UpdateFunctionConfiguration` events today, so no other function argument moved.

**Conditions 1-4.**
1. A targeted, locked plan was used.
2. The before-state was saved, and the NEVER-2 entry is closed: `org/critical_paths/change_management/20261008T2134Z_teams-r6-code-laptop-20261008_deploy_completion.md`,
   with no sentinel left in `.open_deploys/`.
3. The re-plan read no changes. The five-minute window had 5 `ingress_poll` lines carrying the new fields and 0
   `ingress_step_failed`.
4. No function was invoked.

The apply ran at 21:48Z, after the End of Day window closed at 21:45Z, and the report's End of Day gate read 0 messages in
flight.

**One wording difference, not a deviation.** Condition 3 expected one `ingress_step_failed` a minute for `channels` until the
gateway ships. The live log shows 0, because the new `channel_poll` step records its own `failed=1` and does not raise.

## TO-APPLY-20 AC2 (round 7 deploy): MET -- the deploy is as both halves describe

Halves:
- COO: `org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_INBOUND_R7_TEAMS_AGENT_CODE_DEPLOY_COO_R_20261008.md`
  @0a67682d62
- CTO: @54a8846698

Report: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/teams_r7_20261008/REPORT.md`.

**Branch A.**
- The saved `plan.json` shows the same 2 of 27 updates, with `source_code_hash` and `last_modified` only.
- `xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q=` is the base64 of the built SHA-256 `c56511a5...3394` (decoded by this seat).

**Live record.**
- CloudTrail shows ingress at 22:31:55Z (`64158653-...`) and handler at 22:32:01Z (`92ac798b-...`).
- `get-function-configuration` now reads `xWURpe...` on both functions, with role, handler, memory and timeout unchanged.
- The rollback zip's hash `33aeff2a...` equals round 6's build, so the chain of deploys is unbroken.
- The ledger entry `20261008T2229Z_teams-r7-code-laptop-20261008_deploy_completion.md` is closed.

**Conditions 1-4** hold as in round 6. The five-minute window had 0 `chats` failures, and the apply ran outside the End of Day
window with 0 messages in flight.

**One packaged change no half read (not a branch-B trigger as written).**
- `git diff 75420934c2 a5fde91788` over the packaged paths touches only `infra/logic/registry/root_map.json`.
- That is LGIC_BLANKFIX's round 7: +1128 lines, 13 roots before and 63 after, 50 added and 0 existing entries changed. This
  seat checked those counts.
- The report's "transcripts mapping unchanged" is true but vacuous: `transcripts` has no entry before or after.
- Branch B names only `teams_chat/`, `ldo.py`, `handlers.py` and `daily_reports/eod/`. The registry, `lib/opal_naming.py` and
  `NAMING_SCHEMA.json` are packaged but outside both halves' read.

## L8 compile

**Scope.** 30 rows: INBOUND's worker slots `~31` and up (decomposition `inbound1.md:11`), plus the issuer's S33 and S34. No CVO
compile had covered any of them; the only prior adjudication row in this project is C-S1.

**Rows left alone.** 171 of the channel's 201 investigation rows belong to other workstreams. One of them, S35 by `2.0.0_SA_COO~C`, is not INBOUND's. Those rows are not
dispositioned here.

**Dispositions.** Full detail is in
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/adjudications/ADJUDICATION_v2.md`.
- **DISMISSED, as build records or overtaken (12):** W31-S7..S11, W33-S1, W34-S1, W36-S1, W38-S2, W39-S2, W39-S3 and W39-S4.
- **DISMISSED, hazard gone, measured at HEAD (8):** W32-S1..S4 (`.tools/tests/test_remote_job.py` 10 passed); W31-S1 and W31-S2
  (`check_agent_suites.py`, which includes `test_teams_chat_jobs.py`, reads `AGENT-SUITE ok=True`, 127 passed); W38-S1, closed
  by AMENDMENT 1 `dd6deef902` with its disarm record W38-S3 (the round-6 real run read `texted=9 updated=5`).
- **To GRADUATE (10), with their remediation rows HELD.** `.tools/surprise-row-gate.py` refuses any new remediation row in this
  project while 35 BLOCKING/ARMED items of OTHER workstreams read UNDER_INVESTIGATION (its L10 precondition; for example D2-S1,
  S13, W14-S1 and Z-S1). The drafted rows are in
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_INBOUND_REMEDIATION_ROWS_HELD_20261008.json`. The 10 rows:
  - W31-S3 and W32-S5: the protocol file still has no `brief_sha256` or `unavailable_reason` (0 occurrences).
  - W31-S4 and W31-S5: mail domains for Alongside and Opal.
  - W31-S6: the gateway mail route.
  - W31-S12: the intent rule, `assist.py:844`.
  - W36-S2: ARMED. `transcripts-pull/build.sh` still has no line-ending step, and the shared tree's two registry files still
    read `w/crlf`.
  - W39-S1: the caller map, still at HEAD.
  - S33 and S34: ARMED until the 2026-10-09 full-day read.

## What the CTO should have asked but did not

Which packaged files does a never-widen half actually cover? The Teams package carries `lib/opal_naming.py`,
`NAMING_SCHEMA.json` and every `infra/logic/registry/*.json`. Branch B of both halves names only the agent's own folders. On
2026-10-08, LGIC_BLANKFIX added 50 entries to `root_map.json` between the round-6 and round-7 builds, and that change rode into a
signed deploy unread. It was harmless this time: no existing entry changed, and the agent's root has none. But a registry edit by
another project can change what a deployed agent builds, and the next half will not see it. The fix is one clause in the half
template: branch B covers every path the build packages, or names the ones it excludes and why.

-- 3.0.0_SA_CVO
