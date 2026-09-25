# NFRA_OPALAI task order -- `OA-t-4` -- HOP 4: a Teams watch that sees on its own token, and reads

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~4</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the watch is the product's existing detector, moved and repaired; no new cron, alarm or monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: READ-ONLY HTTPS GET to https://mcp.opalinvest.dev/.well-known/oauth-authorization-server (Opal's own gateway). No login, no registration, no token grant.
</preflight>

## 1. THE CELL -- `OA-t-4` (round 1, decomposition s.2/s.3)

`.claude/skills/teams-assist/teams-watch.py` (653 lines) is the Analyst's Teams detector: it polls the gateway for new
messages and emits one line per message. Measured by the Analyst on 2026-09-24
(`org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-09-24/teams_watch_two_blockers_and_a_dark_owner_1145-1315Z.md:18-59`):
- **Blocker 1.** The watch reads Claude Code's own gateway token out of `~/.claude/.credentials.json` and never
  refreshes it (`teams-watch.py:36-38`). The token lives 15 minutes and is re-minted only when the agent itself calls the
  gateway, so the watch goes blind whenever the agent idles.
- **Blocker 2.** 33 of 33 reads failed with a LIVE token. The cause is an untested HYPOTHESIS: an MCP-audience token
  presented straight to `graph.microsoft.com`.

Build the Analyst's watch at `opal_ai/opal/agent/teams_watch/teams-watch.py`, starting from the workspace file's
content, and change it so the items below hold. **AMENDED (CTO ruling I-3, `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/ROUND1_ANALYSIS_INPUTS.md` @`c1717499bf`):
the workspace `.claude/skills/teams-assist/teams-watch.py` STAYS, byte-unchanged, as the OPERATOR plane's tool.** It reads
the operator's Claude credentials for the D7 intake runner (`integrations/ticketing/intake/runner.py:69`, `:107-123`) and
Andrew's `/teams-assist`, which the runtime must never do. The two are different programs on different credential planes,
so C1 holds; only the Analyst's USE of the workspace file ends, at cutover:

1. **It holds its OWN gateway OAuth refresh family.** The gateway's OAuth server already supports this, so carry it and
   do not build one: `infra/aws/ec2/opal-gateway/app/oauth_as.py` has `GRANT_TYPES` incl. `refresh_token` (`:99`),
   dynamic client registration (`:558-579`), and per-family rotation with reuse revocation (`:835-876`). The live
   metadata (`https://mcp.opalinvest.dev/.well-known/oauth-authorization-server`) advertises
   `registration_endpoint` `https://mcp.opalinvest.dev/register` and `token_endpoint` `https://mcp.opalinvest.dev/token`.
   The watch:
   - registers its own client once;
   - keeps its refresh token (rotated on every use) and its cursors in a STATE DIR it is given (a `--state-dir` flag,
     or `state_dir` from the config named by `OPAL_RUNTIME_CONFIG`);
   - refreshes before expiry on its own clock;
   - NEVER opens `~/.claude/.credentials.json`.
   The first authorization (MFA to Andrew's phone) is a login act at close, not yours. Provide an `--authorize` mode
   that prints the authorization URL and exits, plus `--discover-auth <base-url>`. `--discover-auth` reads the live
   metadata and prints exactly `AUTH: refresh_token=<yes|no> registration=<registration_endpoint>`.
2. **Its reads work.** Diagnose blocker 2 from the code path, not from the hypothesis alone. Every read goes through the
   gateway's own tools (`read_chat_messages` / `poll_addressed_teams_messages` over its MCP endpoint), never a token
   presented to Graph directly. Write the diagnosis (what the read path did, what it does now, the evidence) to your
   deliverables folder as `READ_FAILURE_DIAGNOSIS.md`. The live read is proven at the round's close run.
3. **Tests**: `opal_ai/opal/agent/teams_watch/test_teams_watch_lineage.py`, stdlib + pytest only, NO network. A local
   stub stands in for the token endpoint. Name exactly these three tests:
   - `test_refresh_on_expiry`: an expired access token triggers ONE `refresh_token` grant, and the new token is used;
   - `test_never_reads_claude_credentials`: trap `open` and assert the credentials path is never opened;
   - `test_refresh_family_in_state_dir`: the rotated refresh token lands under the state dir only.
4. The cursor discipline (`:26-34`, retry-not-drop, per-channel cursor files), the emit format and the identity pin are
   UNCHANGED, except that the cursor files move under the state dir.
5. **(AMENDED, dropped.)** The operator's `.claude/skills/teams-assist/SKILL.md` and `teams-watch.py` stay byte-unchanged.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on branch `<your worktree branch>-opal_ai`. It has no
   hooks yet. Commit your nested files with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~4
   <0.9.0_WK_NFRA_OPALAI~4@opal.agent>" -F <msgfile> -- <nested paths>`, where the msgfile is written with the Write
   tool. Parent files go through `safe-commit.sh`. No parent-side removal: the workspace watch stays.
2. **No login, no client registration, no token grant against the live gateway, and do not read
   `~/.claude/.credentials.json`.** Your only live call is AC2's metadata GET.
3. `.claude/skills/teams-assist/channels.json` is not yours and stays in place.
4. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/agent/teams_watch/teams-watch.py
opal_ai/opal/agent/teams_watch/test_teams_watch_lineage.py
.claude/skills/teams-assist/teams-watch.py
.claude/skills/teams-assist/SKILL.md
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~4/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/opal-gateway/app/oauth_as.py`, `infra/aws/ec2/opal-gateway/app/server.py`, the
Analyst log named above.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W4-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after both repos are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t4.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t4.AC2.sh; echo "exit=$?"</invocation><expect>direct: refresh_token=yes registration=https://mcp.opalinvest.dev/register; watch: the same string -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t4.AC3.sh; echo "exit=$?"</invocation><expect>moved watch committed in opal_ai=yes; operator teams-watch.py byte-equal to the cut=yes; operator /teams-assist SKILL.md byte-equal to the cut=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~4/NFRA_OPALAI.TO-OA-t-4.teams-watch-sees.proof_of_spec.json`. Report once: what you changed and where, the commit hashes in BOTH repos, the read-failure diagnosis in two lines, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** hop 4, S8 minimum. hostedContents (FWD-2) is enrichment. The watch's first authorization is G-AUTH at
close, and the live read proves blocker 2's fix.

<status>complete</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
