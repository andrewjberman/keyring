# NFRA_TOOLUNIFY REC-1c Lane-A: 18-tool live-AWS exercise batch + 24-residual-dir closure — 0.8.0_AE_CloudComp~A

**archetype:** VALIDATE
**secondary_archetypes:** TRACE

## Objective

Fresh session start (~A was previously live earlier today per prior commits in this log directory, but was
NOT registered at this session's start — re-registered from scratch). CTO~Z dispatched REC-1c Lane-A the
moment registration completed: behaviorally exercise 18 named comp-tools (live-AWS-plane affinity) against
D.md's register, per the REC-1/REC-1b method (mismatched/stale/empty/nonexistent input, OBSERVED vs
DECLARED `failure_mode`), plus close a carried-over secondary item: 24 Lambda source-directories A.md had
left "genuinely undetermined."

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-lambdamap check` | `bash .tools/comp-lambdamap check` | rc=1, DRIFT report | reverse-direction mismatch vs declared FAIL-OPEN |
| `comp-routes trace` | `bash .tools/comp-routes trace <nonexistent>` | rc=0, FAIL-OPEN | mismatch vs declared LOUD |
| `comp-iam-usage reach-check` | `bash .tools/comp-iam-usage reach-check <nonexistent role/action/arn>` | rc=0, JSON verdict:UNKNOWN | by-design mismatch at exit-code layer |
| `comp-deadgrant`(`.py`) | `--self-test`; `--account 000000000000 --limit 1` | self-test PASS; account probe inconclusive (UNKNOWN) | account-dependent branch never reached at this sample size |
| `comp-denytest`(`.py`) | missing-arg + full-arg nonexistent-principal probes | rc=1 both, explicit FAIL | MATCH |
| `comp-tagauthz`(`.py`) `check` | missing `--default-tags-tree` | rc=1, explicit fail-closed error | MATCH |
| `comp-secrets get` | `python3 .tools/comp-secrets get <nonexistent>` | rc=1, explicit not-found | MATCH (after self-caught idiom-mismatch retry) |
| `comp-pii scan` | `<nonexistent component>` | rc=1, explicit not-found | MATCH |
| `comp-keys exists` | `<nonexistent prefix>` | rc=0, ABSENT labels | by-design mismatch at exit-code layer |
| `comp-clobber` | `--live <nonexistent bucket> <key>` | rc=1, unhandled botocore traceback | MATCH-but-flagged (crash, not designed error) |
| `comp-debris` | `--self-test`; `--types <bad>` | self-test PASS; bad-type FAIL-OPEN | mismatch on `--types` |
| `comp-dups` | `--class <bad enum>` | rc=0, silent full unfiltered scan | mismatch, most severe (SILENT-EMPTY as to the mutation) |
| `comp-drift` | `<nonexistent target>`, 150s budget | timeout-bounded partial | UNKNOWN, flagged not adjudicated |
| `comp-firmsep-sweep`(`.py`) | `--secret <nonexistent>` | rc=1, explicit ResourceNotFoundException | MATCH |

**What worked:** the REC-1/1b dispatch-idiom map (bash-wrapper vs python-shebang-direct) held for 17 of 18
tools on first try; `--self-test` flags on `comp-deadgrant`/`comp-debris` gave cheap, safe, offline positive
controls without a separate acceptance-gate re-run (the gate itself, `comp-manifest-check`/
`comp-stitch-refresh`, is inherited CLOSED from REC-1, not re-verified this pass).
**What failed:** first `comp-secrets` invocation used `bash` instead of `python3` (idiom-2 tool) — mis-
dispatched into bash trying to parse Python source, produced a nonsense unrelated error; caught before
recording a verdict, logged not discarded (repeats REC-1 §6's exact class).
**Gap found:** the register's `failure_mode` column is per-tool, and this pass's `comp-lambdamap` result is
the first case where the declared value undershoots the observed loudness (opposite direction of every
prior mismatch) — flagged as a candidate for subcommand-granularity register work, not resolved here.

## Work Completed

### 1. 18-tool live-AWS-plane exercise batch (REC1C_A.md + REC1C_A.sidecar.json)

18/18 dispatched tools exercised, 0 skipped, read-only throughout (no `--write`/`--write-only`/apply/commit
calls). Per-tool verdict: 8 MATCH, 6 MISMATCH, 1 MATCH-but-flagged, 3 UNKNOWN (first-class per CTO~Z's
addendum, not forced). Mutation types labeled EMPTY/NONEXISTENT/MALFORMED/STALE with the provisional-
pending-L0b caveat verbatim in the deliverable header, per CTO~Z's mid-batch addendum.

Headline: a cross-batch pattern (declared-LOUD tools reading FAIL-OPEN-or-worse on invalid/absent input) is
now 7 confirmed instances across three exercise passes (5 new this pass: `comp-routes trace`,
`comp-iam-usage reach-check`, `comp-keys exists`, `comp-debris --types`, `comp-dups --class`; 2 banked from
REC-1/1b: `comp-freshness`, `comp-surface-check scan`).

### 2. 24-residual-Lambda-dir closure (REC1C_A.md §7)

CVO~Z's A.md ADDENDUM 2 had already split the 24 into GROUP1 (11, deployed-under-another-name, closed) /
GROUP2 (9, no-live-counterpart, unsplit) / GROUP3 (4, genuinely uncertain). This session closed the
remaining 13: GROUP2 split into 6 DECOMMISSIONED-LEFTOVER (each with a matching deploy-commit + CTO-GO
teardown-commit citation) vs 3 NEVER-DEPLOYED (zero TF trace, current or historical, no teardown commit);
GROUP3 resolved fully (1 new DEPLOYED-UNDER-ANOTHER-NAME via a live TF citation — `data_refresh` ->
`opal-data-refresh-api`; 3 NEVER-DEPLOYED, one via an explicit author-stated "NOT deployed" commit message).
0 of 24 remain unresolved. Grounding method: current `infra/aws/terraform/**` grep + full-history
`git log -S<name>` per name (13 names checked); `# rail-checked` marker used per CLAUDE.md Rule 21 (a
historical TF-string search is not answerable by `comp-aws`/`comp-iam`).

## Decisions Made

None sovereign or architectural this session — this is an exercise/inventory lane, findings routed to
CTO~Z/CVO~Z for disposition, not adjudicated here (per this lane's explicit read-only scope in both
dispatches).

## Files Modified

| File | Change |
|---|---|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1C_A.md` | new — primary deliverable |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1C_A.sidecar.json` | new — raw per-invocation record |

Both written to disk, NOT committed by this lane — CTO~Z's BASE_EXEC lane owns the commit per the
established REC-1/1b convention (owned-paths gates that tree to CTO~Z).

## Blockers

None. MCP traffic this window: 5 messages (1 dispatch, 1 addendum, 1 ack sent, 2 delivery reports sent to
CTO~Z + CVO~Z) — all handled inline, no RAVC loop left open.

## Current State

Fresh `0.8.0_AE_CloudComp~A` session: registered live, persistent inbox Monitor armed (`bash
/cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh 0.8.0_AE_CloudComp~A stream` —
note: this session's shell is Cygwin, not MSYS/Git-Bash, so the watcher command needed the `/cygdrive/c/...`
path form, not SKILL.md's default `/c/...` form; the first arm attempt exit-127'd on the wrong path form
before the corrected re-arm succeeded), session-serial file written, owned-paths hook confirmed wired,
`.comp-graph/.agent_context` set. REC1C_A.md + REC1C_A.sidecar.json are on disk, delivered to CTO~Z and
CVO~Z via MCP, awaiting CTO~Z's commit and CVO~Z's independent verification pass. No standing crons armed
(event-driven per launcher instructions — AE_CloudComp lane arms zero crons).

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit `REC1C_A.md` + sidecar; decide whether §4a's reverse-direction
   `comp-lambdamap` mismatch and §5's now-7-instance cross-batch pattern become their own follow-up items or
   fold into REC-1/1b's existing handoff queue.
2. **[3.0.0_SA_CVO~Z]** Independent verification pass — every row is re-derivable from the sidecar's
   verbatim commands; flagged two items worth particular attention (comp-lambdamap subcommand-attribution
   question; comp-drift's un-chased CLEAN/MATCH-on-nonexistent-target partial result).
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by for the next dispatched batch.
