# Session Log: 2026-04-10 — ADVI_PROFIL.004a + .004c + incidents

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-10 (session stretched into early 2026-04-11 UTC)
**Projects:** ADVI_PROFIL
**Coordinators:** 0.4.0_DT_ClientPlatform (primary), 2.0.0_SA_COO, 1.0.0_SA_CTO
**Related logs (deep dives):**
- `advi_profil_004a_scoping.md` — .004a Phase 1 audit, architectural correction, deploy, curl + CloudWatch validation
- `advi_profil_004c_prep_notes.md` — .004c SDK/IAM/cache design notes + implementation details

---

## TL;DR

Shipped two Lambda@Edge enforcement waves for ADVI_PROFIL in one session:

- **`.004a` (advisor-id scoping)** — `portal-auth-v1.11.8` + `v1.11.9`, end-to-end validated via DT's curl matrix + CloudWatch structured denial events
- **`.004c` (account/relationship scoping)** — `portal-auth-v1.11.10` + `v1.11.11`, live on `auth-validator-edge:12`, pending DT curl matrix verification (ownership_map.json landed during Group D run at 10:14 PM EDT, CF propagation ~5-15 min from 10:44 PM EDT)

Both waves corrected the original TO target from `shared-advisor-router` to `auth-validator-edge` after Phase 1 `comp-routes` audit revealed shared-advisor-router is origin-request on the S3 behavior only and cannot see `/api/scoped/partners/*`. CTO PRD was corrected in commit `9fa1d073` to match.

Also triggered a manual Group-D-only gold run on `bd-gold-layer-runner` (Andrew redirected DS's request from 0.6.0_AE_PartnerETL) to materialize the `.004b` ownership map and D_04 timeseries_overview artifacts without re-running the A/B/C chain. SSM command `e99ecf29-e583-4e5b-a12b-91c69d59d95a` is in progress as of this log write (D_02 currently running, D_03/D_04 still ahead).

One attribution incident self-reported and closed:
- Commit `7ae0ef6b` (my .004a test matrix log) swept two of DS's .004b files (`D_00.portal_aggregates.py` + `lib/s3_layout.py`) from the shared working-tree index. Root cause: bare `git commit -m` commits the whole index, not just the path I `git add`ed. Escalated to COO + DS. Andrew ruled STAND DOWN — no history fix. Accepted cosmetic attribution cost. New memory rule `feedback_commit_only_flag.md` added to prevent recurrence.

---

## Work threads

### Thread 1 — ADVI_PROFIL.004a (advisor-id scoping)

**Start:** 17:32 EDT — DT relayed Andrew's GO (message `20260410T223238Z`) after .002 JWT claim verified end-to-end

**Phase 1 compiler audit:**
- `comp-routes trace getPlatinumAdvisorSummary` → `/api/scoped/partners/*` → APIGateway-portal
- `comp-routes trace getPlatinumAdvisorTimeseries` → `/api/scoped/advisor-intelligence/*.json` → S3-opal-data-bd via `shared-advisor-router`
- `comp-routes trace getPlatinumAdvisorDrilldownSummary` → empty (same URL as summary, one rule covers both wrappers)
- `comp-blast shared-advisor-router` → no downstream consumers (edge terminus)
- Cross-read auth-validator-edge, tier-router-edge, shared-advisor-router, portal-auth/lambda-edge.tf, portal-auth/cloudfront-distribution.tf

**Architectural correction:** TO target `shared-advisor-router` is structurally wrong. It's origin-request on `/api/scoped/advisor-intelligence/*.json` only. Cannot see `/api/scoped/partners/*` which routes to API GW. `auth-validator-edge` (viewer-request, universal) is the true single choke point. Escalated to DT with three options (A=auth-validator-edge, B=extend CF behavior attachment, C=split across two Lambdas). DT concurred with A under coordinator authority (message `20260410T224010Z`). No COO or Andrew gate needed — scope correction, not expansion.

**Semantics pivot mid-session:** DT initially leaned Option 2 (`firmId === 'opal-capital'` bypass). Andrew direct correction via DT message `20260410T224501Z`: quoted Andrew saying *"No travis should be able to click on any advisor card, or their bar in a chart element, or the leaderboard cards, and be taken to that advisors profile with full access. He is an Admin of 49. Chase however cannot do that."* — that authorizes Option 3-simplified (`role === 'admin'` bypass covering Opal staff AND partner-firm admins). Cross-firm containment preserved by existing X-Firm-Id injection + `opal-partners-data.is_authorized()`. Verified via source read of `users/lambda/portal-authorizer/index.mjs:125 computeAllowedFirms` + `opal-partners-data/lambda_function.py:147 is_authorized`. Caught the flip pre-commit.

**Deploy:** two-step pattern because `cloudfront-distribution.tf` hardcodes `auth_validator_edge_arn = "...:9"` in a local (not dynamic like `shared_advisor_router_arn`).
- Step 1 (`portal-auth-v1.11.8`): source + source map + IAM, Lambda function version → v11 (after one failed build attempt due to MSYS_NO_PATHCONV openssl bug — see Gotchas section)
- Step 2 (`portal-auth-v1.11.9`): CF distribution rewired from `auth-validator-edge:9` → `:11` on all 13 viewer-request behaviors

**Validation:** DT ran an 8-row curl matrix (Chase/Travis cross-advisor attempts + admin bypass + no-JWT). I queried CloudWatch `/aws/lambda/us-east-1.auth-validator-edge` via PowerShell wrapper and found 4 `advisor_scoping_denied` structured events matching DT's curls exactly. Travis/admin bypass rows produced zero denial events as designed. Full matrix + log excerpts in `advi_profil_004a_scoping.md`.

**Status:** TO flipped to `complete` in commit `308c2fae`. CTO PRD corrected in commit `9fa1d073` after I flagged the shared-advisor-router error in CTO's spec.

### Thread 2 — ADVI_PROFIL.004c (account/relationship scoping)

**Start:** 19:25 EDT — DT GO after `.004a` closed out (message `20260410T233046Z`)

**Blocker:** `.004c` needs the firm-partitioned `ownership_map.json` artifact from DS's `.004b`. DS committed code but the artifact wasn't live on S3 yet because a runner timing race (DS fired the runner at 19:00 EDT with old D_00, then uploaded new D_00 at 19:18 EDT — 18 min too late).

**Safe prep while blocked:**
- Read DS's new D_00.py + lib/s3_layout.py for schema, slug normalization (`lib.mix_views.advisor_id` canonical form), filename (`ownership_map.json`, NOT `advisor_ownership.json` — DT had it wrong in the GO), sentinel handling
- Verified firm-scoping precondition via computeAllowedFirms + is_authorized source read (Option 3 admin-bypass model is safe because Travis cannot reach cross-firm data even when bypassing .004c)
- Drafted code in working tree (uncommitted): index.mjs +205 lines, package.json +1 dep, iam.tf +1 resource, plus detailed prep notes
- Bundle size sanity: `bun build --minify` → 63.22 KB (+2.9 KB vs .004a v10), 76 modules, syntax clean
- Mental walkthrough of 6 enforcement flows (Chase pass/deny, Travis admin bypass, missing identity, schema mismatch 500, S3 unreachable 503, admin short-circuit no-fetch)

**Unblock sequence:**
1. Andrew ruled STAND DOWN on attribution incident at 22:06 UTC (see Thread 3) — git-side unblocked
2. Andrew redirected DS's gold-run request from 0.6.0 to me — triggered Group-D-only SSM run, ownership_map.json landed at 22:14 UTC (10:14:41 PM EDT)
3. Extracted test IDs from the live map via `jq` — 4 Chase/Travis account/relationship IDs, cross-non-overlap verified
4. Ran `bun install` in auth-validator-edge/ to update lockfile with `@aws-sdk/client-s3`
5. Committed source + IAM + prep notes with **explicit `git commit -- <pathspec>`** form (per the new `feedback_commit_only_flag.md` rule after the .004a sweep incident). Commit `5a202107`, exactly 5 files, no sweeping.
6. `unset MSYS_NO_PATHCONV && bash build-nodejs-lambda.sh portal-auth auth-validator-edge` → Lambda v12 published
7. `terraform plan` → 1 add (IAM policy) + 1 change (Lambda s3_object_version), no CF drift. `apply` clean. 0-diff confirmed.
8. Tag `portal-auth-v1.11.10` on `0a20c3bc`
9. Bumped `auth_validator_edge_arn` local from `:11` to `:12`, committed with explicit pathspec (`00be0440`), plan → 1 change (13 CF behaviors rewired), apply clean, 0-diff confirmed
10. Tag `portal-auth-v1.11.11` on `00be0440`
11. Pushed both tags with `--follow-tags`

**Current .004c state:**
- Lambda@Edge `auth-validator-edge:12` — live, .004c enforcement active
- IAM `lambda-edge-ownership-map-read` — created, grants `s3:GetObject` on `arn:aws:s3:::opal-data-bd/platinum/*/ownership_map.json` (specific key pattern, not wildcard)
- CF distribution `EVTSA9VEHNZVH` — status `Deployed`, all 13 viewer-request behaviors bound to `auth-validator-edge:12`
- Global propagation window: 5-15 min from apply at 22:44 UTC
- Test IDs sent to DT; DT can fire the 8-row curl matrix after propagation settles

### Thread 3 — 7ae0ef6b attribution incident

**Trigger:** DS flagged via MCP at 23:23 UTC (`20260411T022322Z_0.4.0_DS_ClientPlatform_.004b_shipped___ATTRIBUTION_INCIDENT_fla.md`). My commit `7ae0ef6b` ("log(0.7.0_AE): .004a test matrix validated + CloudWatch denial events confirmed") contained two of DS's .004b files (`D_00.portal_aggregates.py` + `lib/s3_layout.py`) attributed to me.

**Root cause diagnosed:**
```bash
git add org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-04-10/advi_profil_004a_scoping.md && \
  git commit --author="0.7.0_AE_CloudOps ..." -m "..."
```
Explicit `git add` on one path. But bare `git commit -m` commits the WHOLE index, not just the path I just added. DS had their two files staged concurrently in the shared working-tree index. Sibling failure mode to the existing `feedback_selective_staging_only.md` "no git add -A" rule, but distinct: even explicit `git add` is unsafe if another agent is staging concurrently and you run bare `git commit -m`.

**Audit scope:** every other commit from this session was clean. Only `7ae0ef6b` had the sweep. Verified via `git log --author="0.7.0_AE_CloudOps" --since="2026-04-10 18:00" --stat`.

**Escalation:** Messaged DS with root cause + apology, escalated to COO with two fix options:
- **Option A** — force-push rewrite of `7ae0ef6b` to correct attribution (required Andrew auth per CLAUDE.md rule 14)
- **Option B** — `git notes` annotation on the commit documenting the mis-attribution (non-destructive)

**Andrew ruling (via COO message `20260411T020651Z`):** *"we're not doing any force pushing that's cosmetic and we hold ourselves to a higher standard."* STAND DOWN on both options. Content is byte-identical-correct. Cosmetic metadata issue. Force-pushing for cosmetic reasons sets a bad precedent. Real audit trail = session logs, not git blame. Incident closed. Cost accepted: D_00 and s3_layout.py show `0.7.0_AE_CloudOps` in `git blame` permanently.

**Durable fix:** COO committed to a worktree-per-task-order protocol as a future addition (not mine, not blocking anything). Architecturally eliminates the shared-index root cause.

**Memory update:** Wrote `feedback_commit_only_flag.md` with the incident details + the rule *"git add stages, git commit commits the index. They are not the same operation. Always constrain commits with pathspec."* Indexed in `MEMORY.md`. Applied on every commit from `.004c` forward (`5a202107`, `a32027e7`, `00be0440`, source-map commits, tag commits — all clean per explicit pathspec).

### Thread 4 — Group-D gold run trigger

**Trigger:** 22:06 UTC — Andrew redirected DS's original AE-request from `0.6.0_AE_PartnerETL` to me, directing me to run Group D only (not full chain A→D) per his explicit "don't waste 30-45 min on positions cube rebuild" rationale.

**Problem:** `bd-gold-layer-runner` (`i-01003b035d2988dfb`, c6i.16xlarge) is a systemd-managed instance. On boot, `gold-layer-runner.service` auto-fires `run-gold-layer.sh`, which calls `run_gold_layer.sh incremental`, which calls `gold_dispatch.sh --chain full --incremental` — full chain A→D. No native way to start the instance and run Group D only without winning a race against systemd.

**Approach:** Start the instance → poll SSM-ready (came online in ~15s) → send SSM command that (1) stops the systemd service, (2) kills any stragglers, (3) re-syncs scripts from `s3://opal-data-bd/code/gold/` (gets DS's new D_00 + D_04), (4) invokes `gold_dispatch.sh --group D --no-shutdown` directly, (5) uploads log to `s3://.../logs/gold-layer/group_d_manual_{timestamp}.log`, (6) `shutdown -h +2` after completion.

**SSM command ID:** `e99ecf29-e583-4e5b-a12b-91c69d59d95a`
**Kicked off:** 21:50 EDT (21:50:xx UTC... actually 01:50 UTC next day)

**D_00 (.004b) completed at 22:14:41 UTC** — `platinum/49financial/ownership_map.json` live, 364 KB, schema_version=1, 162 advisors. Extracted test IDs via `jq` and passed to DT.

**Status at session-log time (22:48 UTC / 10:48 PM EDT):**
- SSM command still `InProgress`
- Probe at 22:31 UTC showed D_02.advisor_client_detail.py running (PID 3801, 120% CPU, 6 GB RAM, 13:29 CPU time)
- D_01 completed per log: 2,808 client detail files in 8.6s, 183 advisor timeseries, relationship timeseries near done (3,000/3,335)
- D_03 and D_04 still ahead
- D_04 timeseries_overview.json still shows old 00:07 UTC timestamp — not yet re-written this run
- ETA for D_04 completion: ~22:50-23:00 UTC (10:50-11:00 PM EDT)
- Scheduled wake-up at 22:48 UTC to re-check

**No impact on .004c deploy:** .004c source was deployed, IAM grant applied, CF rewired to Lambda v12, all BEFORE D_04 completes. Because `.004c` enforcement only touches the ownership_map (which is already live from D_00) and not timeseries_overview (which is D_04's output and doesn't interact with `.004c`), `.004c` is independent of D_04's completion. D_04 is required for DS's other TO (nna-canonical-source) but not mine.

---

## Deployment Tags

| Pipeline | Tag | Commit | What |
|---|---|---|---|
| portal-auth | `portal-auth-v1.11.8` | `9208c784` / `be25dc9b` / `58a62b94` | .004a Lambda@Edge v10 source + IAM + source map |
| portal-auth | `portal-auth-v1.11.9` | `95692b66` / `dfd4f7ca` | .004a CF distribution bound to `auth-validator-edge:11` |
| portal-auth | `portal-auth-v1.11.10` | `5a202107` / `a32027e7` / `0a20c3bc` | .004c Lambda@Edge v11→v12 source + new IAM policy lambda-edge-ownership-map-read + source map |
| portal-auth | `portal-auth-v1.11.11` | `00be0440` / `2ba67e44` | .004c CF distribution bound to `auth-validator-edge:12` |

All commits authored `0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>`. All four tags pushed with `--follow-tags`.

---

## Commits authored this session (in order)

| Hash | Subject |
|---|---|
| `9208c784` | feat(ADVI_PROFIL.004a): advisor-id scoping gate in auth-validator-edge (v10) |
| `be25dc9b` | ci: upload auth-validator-edge .004a artifact [skip ci] |
| `58a62b94` | ci: record deploy portal-auth @ be25dc9b [skip ci] |
| `95692b66` | infra(ADVI_PROFIL.004a): bump CloudFront auth-validator-edge to v11 |
| `dfd4f7ca` | ci: record deploy portal-auth @ f332672b [skip ci] |
| `0160219b` | log(0.7.0_AE): ADVI_PROFIL.004a deploy + compiler log + pipeline_inventory bump |
| `7ae0ef6b` | log(0.7.0_AE): .004a test matrix validated + CloudWatch denial events confirmed ⚠️ **swept 2 DS files — see Thread 3** |
| `308c2fae` | ADVI_PROFIL.004a: flip TO status pending -> complete |
| `765dcae9` | log(0.7.0_AE): .004c prep notes -- SDK/IAM/cache design, blocks on .004b |
| `5a202107` | feat(ADVI_PROFIL.004c): account/relationship scoping gate in auth-validator-edge (v11) |
| `a32027e7` | ci: upload auth-validator-edge .004c artifact [skip ci] |
| `0a20c3bc` | ci: record deploy portal-auth @ a32027e7 [skip ci] |
| `00be0440` | infra(ADVI_PROFIL.004c): bump CloudFront auth-validator-edge to v12 |
| `2ba67e44` | ci: record deploy portal-auth @ 36416c3f [skip ci] |

Every commit from `5a202107` forward used explicit `git commit -- <pathspec>` form per the new `feedback_commit_only_flag.md` rule. Zero subsequent sweeps.

---

## Compiler Tools

| Tool | Invocation | Result | Used for |
|---|---|---|---|
| `comp-build` | force rebuild at session start | 662 nodes, 287 edges (1.4s) | Fresh graph for .004a audit |
| `comp-routes trace` | `getPlatinumAdvisorSummary` | `/api/scoped/partners/*` → APIGateway-portal | .004a path-1 confirm |
| `comp-routes trace` | `getPlatinumAdvisorTimeseries` | `/api/scoped/advisor-intelligence/*.json` → S3-opal-data-bd via shared-advisor-router | .004a path-2 confirm |
| `comp-routes trace` | `getPlatinumAdvisorDrilldownSummary` | empty (same URL as summary) | CTO PARTIAL check — single rule covers both TS wrappers |
| `comp-blast` | `shared-advisor-router` | no downstream consumers | .004a blast radius on original (wrong) TO target |
| Manual read (substitute for comp-* on v10→v11 flow) | `auth-validator-edge/index.mjs`, `tier-router-edge/index.mjs`, `shared-advisor-router/index.mjs`, `portal-auth/lambda-edge.tf`, `portal-auth/cloudfront-distribution.tf`, `users/lambda/portal-authorizer/index.mjs:125`, `opal-partners-data/lambda_function.py:147,1244,1263`, `portal_authorizer/index.mjs:101`, `data/black_diamond/scripts/gold/D_00.portal_aggregates.py`, `data/black_diamond/scripts/gold/lib/s3_layout.py:143` | Verified choke point, firm-scoping end-to-end, ownership_map schema + filename | Architecture verification for both .004a and .004c |

Appended two lines to `org/compiler-tools-log.md`:
- 2026-04-10 .004a Phase 1 entry
- 2026-04-10 .004c prep + Group-D verification entry

Gap: did not run `comp-blast auth-validator-edge` explicitly for .004c Phase 1. Substituted with manual file reads since the downstream topology was already understood from .004a. Would be worth running next session.

---

## Gotchas found this session (added to memory)

### MSYS_NO_PATHCONV breaks openssl in build-nodejs-lambda.sh

`build-nodejs-lambda.sh` creates `/tmp/lambda-artifact-{function}.zip` (Git Bash POSIX path) and runs `openssl dgst -sha256 -binary "$ZIP_PATH"`. With `MSYS_NO_PATHCONV=1` set (which memory says is required for terraform `-chdir=`), openssl cannot resolve the POSIX path and returns empty SHA256. Upload "succeeds" but S3 metadata `content-sha256` is blank AND source map gets a blank hash. Terraform won't detect the artifact change and silently deploys stale code.

**Fix:** `unset MSYS_NO_PATHCONV` before running the build script. Re-export `MSYS_NO_PATHCONV=1` for subsequent terraform calls. Do NOT mix build and terraform in one export scope.

**First caught** during `portal-auth-v1.11.8` deploy (.004a). First build corrupted the artifact metadata; second build without MSYS_NO_PATHCONV succeeded (SHA256 `AsESuygxQAhRzh0eZ0jpoDRGfpO5WdW3DPnLmcZptdk=`). Applied the fix preemptively to `.004c` build.

### CloudWatch Logs CLI log-group-name path conversion

`aws logs filter-log-events --log-group-name /aws/lambda/us-east-1.auth-validator-edge` in Git Bash gets mangled by MSYS to `C:/Program Files/Git/aws/lambda/us-east-1.auth-validator-edge`. Setting `MSYS_NO_PATHCONV=1` instead breaks the path to the `aws` Python script itself. Leading `//` escape is rejected by the API as non-existent log group.

**Fix:** Wrap in PowerShell:
```bash
powershell.exe -NoProfile -Command "\$env:AWS_EC2_METADATA_DISABLED='true'; aws logs filter-log-events --log-group-name '/aws/lambda/us-east-1.auth-validator-edge' --start-time ... --filter-pattern 'advisor_scoping_denied' --region us-east-1"
```
PowerShell doesn't do path conversion. Alternative for discovery queries: use `describe-log-groups --query 'logGroups[?contains(logGroupName, \`substring\`)]'` (log group name inside a JMESPath expression, not a positional arg).

Lambda@Edge log groups are replicated per edge region. Primary log group is `/aws/lambda/us-east-1.<function-name>` (note the `us-east-1.` prefix — this is the replicated format, NOT `/aws/lambda/<function-name>` which is the control-plane placeholder).

**First caught** when verifying .004a structured denial events against DT's curl matrix. Written up in `feedback_msys_pathconv_openssl_logs.md` with both gotchas.

### Bare `git commit -m` commits the whole shared index

Covered in Thread 3. Rule: always use `git commit -- <explicit-pathspec>` or `git commit --only <paths>` in multi-agent sessions. Written up in `feedback_commit_only_flag.md`.

### CloudFront Lambda@Edge version hardcoded local in cloudfront-distribution.tf

`cloudfront-distribution.tf:59`:
```hcl
auth_validator_edge_arn = "${local.edge_arn_prefix}:auth-validator-edge:9"
```
Not dynamic (unlike `shared_advisor_router_arn` which uses `qualified_arn`). Every `auth-validator-edge` deploy requires a **second** terraform apply that bumps the version number in this local. Missed on my first `.004a` deploy — plan showed 0-diff after the Lambda upload but the CF distribution was still pointing at the old version. Had to do a second commit + apply.

Same trap caught me twice this session (.004a and .004c — both two-step deploys). Parked as a follow-up TO — convert this local to dynamic reference like `shared_advisor_router_arn`. Low priority, not blocking anything. Noted in `.004a` and `.004c` session logs.

---

## Coordination thread

Dense coordination across four agents in one session. Message count (approx):

| With | Inbound | Outbound |
|---|---|---|
| 0.4.0_DT_ClientPlatform | ~11 | ~8 |
| 0.4.0_DS_ClientPlatform | ~2 | ~2 |
| 2.0.0_SA_COO | ~1 | ~1 |
| 1.0.0_SA_CTO | ~1 | ~2 |

Notable coordination moments:
- **Three-way crossed wires on .004a semantics** — DT sent Option 2 lean, I agreed, then Andrew corrected to Option 3. Caught mid-session pre-commit and flipped the helper with a one-line edit.
- **DT-inline TO correction block** — DT edited my .004a TO correction block inline (Option 2 → Option 3) while I was still editing the same file. No conflict because the TO file supports multiple section edits.
- **Andrew-directed redirect on .004b gold run** — DS originally messaged 0.6.0_AE_PartnerETL, Andrew redirected to me. Took the baton, executed via SSM.
- **Self-reported attribution incident** — DS flagged `7ae0ef6b`, I self-reported to COO without attempting to rewrite history, Andrew ruled STAND DOWN.

**Protocol adherence notes:**
- Inbox watcher re-launched after every exit (per memory rule)
- Pre-commit pause on every GO signal that landed mid-flight (e.g. "go Option 3, confirmed" before flipping the helper)
- Explicit pathspec discipline applied from `5a202107` forward

---

## Status at session-log time (22:48 UTC / 10:48 PM EDT)

### Complete
- `.004a` shipped, validated, TO flipped to `complete`, CTO PRD corrected
- `.004c` source + IAM + CF bump shipped, CF status `Deployed`, binding `auth-validator-edge:12`
- Attribution incident closed per Andrew ruling
- Memory updated with new gotchas and the commit-pathspec rule

### In progress
- Group D gold run (SSM `e99ecf29-e583-4e5b-a12b-91c69d59d95a`) — D_02 currently running, D_03/D_04 still ahead, ETA 22:50-23:00 UTC
- `.004c` global Lambda@Edge propagation — 5-15 min from 22:44 UTC apply
- DT curl matrix for `.004c` — IDs delivered, DT to fire post-propagation
- Scheduled wake-up at 22:48 UTC to re-probe Group D state and D_04 artifact

### Parked (not blocking)
- Convert `auth_validator_edge_arn` hardcoded TF local → dynamic reference (save the two-step deploy on future `auth-validator-edge` bumps)
- Investigate whether `/auth/*` CloudFront behavior absence is intentional or drift (DT flagged during .004a login flow)
- `.004c` TO file still dirty in working tree (DT-authored architectural-principle block edits I never made) — DT to commit under DT author

### Blockers (none for me)
- `.004c` TO status flip to `complete` blocks only on DT curl matrix results + CloudWatch structured event verification. Both can happen tomorrow morning if DT is offline tonight.

---

## Next steps

1. **When SSM command completes:** Verify `platinum/firm/timeseries_overview.json` LastModified >= 22:14 UTC, spot-check D_04's new `by_geo`/`by_adv` structure via `jq '.nna.quarterly[0].by_geo'`. Confirm runner shut down cleanly. Message DT + DS that both artifacts are live.
2. **When .004c propagation settles (~23:00 UTC):** DT fires 8-row curl matrix. I query CloudWatch for `advisor_scoping_denied rule=004c`, `advisor_not_in_ownership_map rule=004c`, and any `ownership_map_fetch_failed` or `ownership_map_schema_mismatch` events.
3. **Post-validation:** Flip `.004c` TO to `complete`. Bump `pipeline_inventory.xml` auth-validator-edge version from `:11` to `:12`. Append compiler-tools-log entry for `.004c` verification.
4. **Future cleanup (separate TO):** Convert `auth_validator_edge_arn` TF local to dynamic. Small infra cleanup pass, not blocking anything.

---

## Verification

### .004a + .004c live state

```
# Lambda@Edge function versions
$ aws lambda list-versions-by-function --function-name auth-validator-edge --query 'Versions[-3:].Version'
10  11  12

# CloudFront distribution binding
$ aws cloudfront get-distribution-config --id EVTSA9VEHNZVH | grep -oE 'auth-validator-edge:[0-9]+' | sort -u
auth-validator-edge:12

# CloudFront status
$ aws cloudfront get-distribution --id EVTSA9VEHNZVH --query 'Distribution.Status'
Deployed
```

### Ownership map live

```
$ aws s3api head-object --bucket opal-data-bd --key platinum/49financial/ownership_map.json
LastModified: 2026-04-11T02:14:41Z
ContentLength: 372867

$ jq '{schema_version, firm_id, advisor_count: (.advisors | length)}' ownership_map.json
{
  "schema_version": 1,
  "firm_id": "49financial",
  "advisor_count": 162
}
```

### .004a CloudWatch denial events (already captured in advi_profil_004a_scoping.md)

Four `advisor_scoping_denied` events logged during DT's curl matrix, matching timestamps 23:05:34, 23:05:35, 23:06:35, 23:06:35 (UTC), all with full structured payload (userId, jwtAdvisor, jwtFirmId, jwtRole, requestedAdvisor, path, rule="004a"). Travis/admin rows produced zero events as designed.

### Terraform 0-diff

Both `.004a` and `.004c` deploys confirmed `No changes. Infrastructure matches the configuration.` on post-apply plan.
