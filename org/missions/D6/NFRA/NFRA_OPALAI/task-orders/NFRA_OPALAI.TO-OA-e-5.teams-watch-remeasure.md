# NFRA_OPALAI task order -- `OA-e-5` -- ROUND 2, E5: re-measure the Teams watch's reads after the gap-B fix (MEASURE ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~14</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one bounded measurement run; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- one read-only SSM md5 read on the existing host; no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- a measurement; nothing is changed.
EGRESS CLASS, declared: reads on Opal's own plane only (the gateway, one SSM read).
</preflight>

## 1. THE CELL -- `OA-e-5` (round 2, decomposition section R2.1)

The Opal Analyst's Teams watch was blind on 2026-09-24 for two independent reasons (the Analyst's log
`org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-09-24/teams_watch_two_blockers_and_a_dark_owner_1145-1315Z.md`):
- **blocker (1):** the gateway token in `~/.claude/.credentials.json` lives 15 minutes and is re-minted only when the
  seat itself calls the gateway;
- **blocker (2):** reads FAILED even with a LIVE token. 33 of 33 `read failed ... cursor HELD` lines appeared across
  all four chats, with zero successful reads. The cause was a hypothesis only.

Since then, the gateway's Teams reader retries a Graph 500 page without `$select` and projects the fields client-side
(the laptop's "gap B": `_get_messages` in `infra/aws/ec2/opal-gateway/app/tools.py`, which marks such a page
`select_fallback: true`). **The served gateway carries it BY CONTENT:** at this cut the host serves `fe94911257`, whose
`app/tools.py` holds that retry. The laptop commit `678891171b` is NOT an ancestor of `fe94911257`, because the release
carried the fix on a release branch. So establish gap B by content, never by ancestry.

**Your job is to MEASURE ONLY: do reads through the watch's own read path now succeed with a live token?** Change nothing.
1. **Resolve the served commit BY CONTENT.** Over SSM on `i-07dccb1615503ac99`, read `md5sum /opt/opal-gateway/app/tools.py`
   with `.tools/aws ssm send-command` (read-only, `AWS-RunShellScript`). Match it against
   `git show <c>:infra/aws/ec2/opal-gateway/app/tools.py | md5sum` for `fe94911257` first. If that does not match, try the
   most recent commits touching that file on any `rel-*` branch or CLOUD. Record the match, and whether that commit's
   `tools.py` contains `select_fallback`.
2. **Write a measurement script** at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/e5_remeasure.py`.
   It imports the parent watch `.claude/skills/teams-assist/teams-watch.py` BY PATH (`importlib.util.spec_from_file_location`,
   the same way `integrations/ticketing/intake/runner.py` does) and uses the watch's own `read_token()`, `poll()` and
   `read_chat()`.
   - That file is LIVE PRODUCTION: the D7 intake runner imports it every 5 minutes from this working tree. NEVER edit,
     copy or re-save it. Never call its `main()`, and never write its cursor files. Its import does no IO.
   - Pin the Analyst's identity: set `sys.argv` before the import so the watch's `--server` pin selects the
     `opal-gateway-bbg` record (the Opal Bloomberg sign-in). Print record NAMES only, never a token.
   - `poll(tok, <now minus 7 days>)` gives the touched chat ids. `read_chat(tok, cid)` runs on each, bounded to 10 chats.
   - Classify every read: `OK`; `FAILED`, with a signature (exception class plus HTTP status or Graph error code, and
     never message text); or `TOKEN-EXPIRED`, when the token's `expiresAt` had passed at that read.
3. **The token is warmed by the issuer** (one gateway call) just before your spawn, so it is live for about 15 minutes.
   Run the reads at once. If no read runs on a live token, the verdict is `INCONCLUSIVE`, and you say so. Never mint or
   refresh a token yourself.
4. **Write** `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/E5_TEAMS_WATCH_REMEASURE.json`,
   with exactly these keys:
   - `measured_at` (UTC ISO);
   - `served_commit` (the commit that matched in step 1);
   - `gap_b_in_served` (true/false, by content);
   - `identity` (the watch's `self_id` of the token used);
   - `chats` (distinct chats read);
   - `reads_attempted`, `reads_ok`, `reads_failed`, `reads_token_expired`;
   - `failure_signatures` (`{signature: count}`);
   - `verdict`: `CLEARED` when failed = 0 and ok >= 1; `NOT-CLEARED` when failed > 0; `INCONCLUSIVE` when no read ran on
     a live token;
   - `next`: one sentence. If CLEARED, the watch's remaining work is blocker (1), the token refresh the watch should own
     (PRD C8). If NOT-CLEARED, name the dominant signature.
   Persist no message text and no token.

## 2. BOUNDS

1. Read-only everywhere: no edit to any watch, runner or gateway file; no deploy; no SSM command other than the one
   `md5sum`.
2. Standing: no push, no install. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `.claude/skills/teams-assist/teams-watch.py`, `integrations/ticketing/intake/runner.py`,
`infra/aws/ec2/opal-gateway/app/tools.py`, the Analyst's log above.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W14-S<k>`
(next free k for W14).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the measurement file is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-5"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e5.AC1.sh; echo "exit=$?"</invocation><expect>reads attempted>=1 = ok+failed+token_expired (sum ok=True); signatures sum = failed; chats>=1; identity set=yes; verdict equals implied -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-5"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e5.AC2.sh; echo "exit=$?"</invocation><expect>live md5 of /opt/opal-gateway/app/tools.py = served_commit's md5 (ssm status Success); gap-B in served (content) measured = file -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/NFRA_OPALAI.TO-OA-e-5.teams-watch-remeasure.proof_of_spec.json`.
Report once: the served commit and its md5 pair, the counts, the signature distribution, the verdict, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E5 (I-5 gap B; blocker (2)). Before any further ruling on blocker (2), it is re-read after gap B.
Measured at the cut: `fe94911257`'s `app/tools.py` carries `_get_messages` / `select_fallback`, and `678891171b` is NOT
its ancestor. A check that tested ancestry would read gap B as absent from a gateway that serves it. e5.AC2 therefore
reads by content.

**Dry-run at base** (main tree, CLOUD `7cb7c7f33d`):
- e5.AC1 base: FAIL as expected (the file is absent).
- e5.AC2 base: FAIL as expected (the file is absent).

Checker arms were exercised with a synthetic file, then removed:
- GREEN: AC1 PASS on consistent counts. AC2 PASS: the live SSM md5 `6c888e51...` equals `fe94911257`'s, and gap B is
  in the served commit by content.
- RED: AC1 FAIL on a verdict the counts do not imply.

**SPAWN:** at the cut. Immediately before the spawn, the issuer makes one gateway MCP call as Opal Bloomberg (for
example `whoami` on `opal-gateway-bbg`) so the watch's token is live for the measurement window. The slot continues
with OA-e-6 after Part A.

<status>pending</status>
<round>2</round>
<slot>~14</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
