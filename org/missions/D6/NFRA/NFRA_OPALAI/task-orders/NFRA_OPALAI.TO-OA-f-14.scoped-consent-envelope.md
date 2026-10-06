# NFRA_OPALAI task order -- `OA-f-14` -- DIRECT ACT, ADDENDUM R2-A12: a scoped identity's /login consent asks only for the Graph scopes its allowlisted tools need

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~29</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the tests run offline with fakes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the change NARROWS one identity's consent request; the unscoped arm is the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-14` (decomposition ADDENDUM R2-A12; `1.0.0_SA_CTO~O` ruling R25.3)

The gateway (`infra/aws/ec2/opal-gateway/`) has one scoped service identity, the Teams concierge
`opalbloomberg@opalinvest.com`. `app/identity_scope.py` holds its tool allowlist (`_SEED`, plus the tracked overlay
`identity_tool_allowlist.txt`), enforced at dispatch. Its `/login` sign-in is admitted, but the consent it is sent to
asks Microsoft for the FULL delegated envelope, `config.GRAPH_SCOPES` (17 scopes, mail and calendar included):
- `app/token_broker.py` `build_consent_url(state)` builds the URL with `list(_cfg.GRAPH_SCOPES)`;
- `app/token_broker.py` `redeem_consent(email, code, state)` redeems the code with `list(_cfg.GRAPH_SCOPES)`;
- `app/token_broker.py` `get_token(email)` then acquires silently with `_scopes_for_tier(tier)`, which for this
  identity's tier is again the full envelope;
- `app/server.py` `login()` calls `build_consent_url(state)` with the state made from the caller's email.

The ruling: a scoped identity's `/login` consent requests only the Graph scopes its allowlisted tools need, from a scope
map per tool. An UNSCOPED identity is untouched.

Do:
1. **The scope map.** New file `app/graph_scope_map.py` with one constant, `TOOL_GRAPH_SCOPES: dict[str, frozenset[str]]`,
   and no logic beyond a lookup helper. It carries one entry per tool that any scoped identity may call (the seed and
   the tracked overlay, client-qualified rows included). The issuer's proposed entries are below. VERIFY each one
   against the Graph paths the tool's own code calls (`app/tools.py`, `app/integrations/`), and cite `file:line` in a
   comment beside the entry. Where the code shows a different need, the code wins: correct the entry and say so in
   your report.

   | tool | proposed Graph scopes |
   |---|---|
   | `whoami` | `User.Read` |
   | `poll_addressed_teams_messages`, `list_chats`, `read_chat_messages`, `read_chat_message_images` | `Chat.ReadWrite` |
   | `send_chat_message` | `Chat.ReadWrite`, `ChatMessage.Send` |
   | `list_teams` | `Team.ReadBasic.All` |
   | `list_channels` | `Channel.ReadBasic.All` |
   | `read_channel_messages` | `ChannelMessage.Read.All` |
   | `send_channel_message` | `ChannelMessage.Send` |
   | `opal_asker_query` | MEASURE: the Graph calls made on its path (`app/asker_scope.py`) |
   | `opal_data_refresh_upload` | MEASURE: the Graph calls made with `user_token` (`app/integrations/opal_portal/integration.py`) |

   A tool that makes no Graph call maps to an empty frozenset, with a comment saying so. Every scope string in the map
   is a member of the default `config.GRAPH_SCOPES`; never introduce a scope that list does not carry.
2. **One function decides.** In `app/identity_scope.py` add `consent_scopes(email) -> "list[str] | None"`:
   - an UNSCOPED identity returns `None`;
   - a SCOPED identity returns the sorted union of `TOOL_GRAPH_SCOPES` over every tool on its allowlist (unqualified
     and client-qualified), always including `User.Read`;
   - an allowlisted tool with NO map entry contributes nothing (least privilege), and test 1 below makes that state
     unreachable for the tracked rows.
3. **Both consent legs use it.** `build_consent_url` and `redeem_consent` ask for `consent_scopes(<the state's email>)`
   when it is not `None`, else exactly `list(_cfg.GRAPH_SCOPES)` as today. Both legs key on the SAME email, the one the
   state carries, so the scope list sent at the redirect equals the one sent at the redemption. `login()` passes what
   `build_consent_url` needs; the admit decision, the audit record and every refusal path are not edited.
4. **The silent acquire stays inside the consent.** In `get_token`, when the token owner is a scoped identity, the
   scopes requested are the tier's scopes INTERSECTED with `consent_scopes(...)`. So a token minted after a narrow
   consent never asks for a scope that consent did not carry, and a `NeedsLogin` sent to `/login` cannot loop. An
   unscoped owner's request is byte-for-byte today's.

**Tests.** A NEW file `infra/aws/ec2/opal-gateway/tests/test_scoped_consent_r253.py`, offline, fakes only (the pattern of
`tests/test_login_admit_r24.py`: `MOCK_GRAPH`, stubbed upstream, no network, no real token). EXACTLY these six names:
- `test_r253_map_covers_every_scoped_tool`: every tool on every scoped identity's allowlist, read from `_SEED` AND the
  tracked `identity_tool_allowlist.txt` (qualified rows included), has an entry in `TOOL_GRAPH_SCOPES`;
- `test_r253_map_scopes_are_consented`: every scope in the map is in the default `GRAPH_SCOPES`;
- `test_r253_concierge_consent_is_narrow`: `consent_scopes("opalbloomberg@opalinvest.com")` equals the union of its
  tools' entries plus `User.Read`, is a STRICT subset of `GRAPH_SCOPES`, and holds no scope beginning `Mail.`,
  `Calendars.`, `Notes.` or `OnlineMeetings.`;
- `test_r253_unscoped_consent_unchanged`: the POSITIVE control. For an unscoped email, the scope list that reaches the
  authorization-URL builder and the one that reaches the code exchange are each exactly `list(GRAPH_SCOPES)`;
- `test_r253_both_legs_same_scopes`: for the concierge email, the list captured at the redirect leg equals the list
  captured at the redemption leg, and equals `consent_scopes(...)`;
- `test_r253_silent_acquire_within_consent`: for the concierge as token owner, the scopes `get_token` passes to
  `acquire_token_silent` are a subset of `consent_scopes(...)` and are not empty.

## 1a. AMENDMENT A1 (2026-10-06 ~22:0xZ; `1.0.0_SA_CTO~O` ruling msg 30365 on row `NFRA_OPALAI-Z-S57`)

Step 4 bounds `get_token` by the token OWNER, but the map names TOOLS. A gateway route that is not a tool and mints a
scoped identity's token (for example `app/taxsma_workbook.py:317`) is narrowed with no entry of its own. Add:
1. **A second table** in `app/graph_scope_map.py`, `CALLER_GRAPH_SCOPES`, for every NON-TOOL caller of
   `token_broker.get_token`: the caller's name (its module), the `config` key that names the identity it mints under,
   and its MEASURED Graph scopes with `file:line` beside each entry. Every scope is in the default `GRAPH_SCOPES`.
2. **`consent_scopes` unions a caller's scopes** when that caller's configured identity IS the scoped identity:
   - a key whose value is an email: when it equals the scoped email (case-insensitive);
   - a key whose value is set but is not an email (a `<tid>/<oid>` binding): the caller's scopes ARE unioned, because
     the match cannot be decided from configuration and the ruling forbids a dead end;
   - a key that is unset or empty: not unioned.
3. **One more test**, `test_r253_every_get_token_caller_is_mapped`: it enumerates every `get_token(` call site under
   `app/` outside `app/tools.py` and `app/token_broker.py` by reading the source files, PRINTS the denominator
   (`get_token callers outside tools.py: <n>`), and fails on a call site whose module has no `CALLER_GRAPH_SCOPES`
   entry. A call site that is on a TOOL's path (it serves a tool already in `TOOL_GRAPH_SCOPES`) is entered in the
   caller table with that tool named, never skipped.
4. `test_r253_concierge_consent_is_narrow` now computes its expected union with the caller table included, under the
   test's own configuration; its STRICT-subset and no-`Mail.`/`Calendars.`/`Notes.`/`OnlineMeetings.` assertions hold
   for a configuration in which no mail-reading caller is bound to the concierge.
5. Do NOT edit `app/taxsma_workbook.py`, `app/mail_route.py`, `app/teams_route.py`, `app/transcript_route.py`,
   `app/ms_ingest.py`, `app/otp.py` or `app/config.py`. Read them; change only the files in `<paths>`.

AC1 now reads seven named arms. AC2 and AC3 are unchanged.

## 2. BOUNDS

1. Only the five gateway files in `<paths>` change. `config.py`, `tier.py`, `tools.py`, `context.py`,
   `identity_tool_allowlist.txt` and every existing test file are NOT edited. No allowlist row is added or removed.
2. Nothing is deployed and nothing is released: the live gateway does not move in this order. No push, no vendor call,
   no sign-in, no call to Microsoft.
3. The gateway suite may append to the tracked `infra/aws/ec2/opal-gateway/audit.jsonl`. Restore it
   (`git checkout -- infra/aws/ec2/opal-gateway/audit.jsonl`) before every commit.
4. Standing: REFUSE a criterion you cannot meet as written, and report the refusal with its measurement. Never repair a
   criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/graph_scope_map.py
infra/aws/ec2/opal-gateway/app/identity_scope.py
infra/aws/ec2/opal-gateway/app/token_broker.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_scoped_consent_r253.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~29/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W29-S<k>` (none exist at the cut; the first is S1), with an exact `HH:MMZ` `surfaced_at`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-14"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f14.AC1.sh; echo "exit=$?"</invocation><expect>named arms passed 7 of 7; failed/errored tests 0; get_token callers outside tools.py: a printed count >= 1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-14"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f14.AC2.sh; echo "exit=$?"</invocation><expect>passed >= 36 (base 36); failed=[] (base []) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-f-14"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f14.AC3.sh; echo "exit=$?"</invocation><expect>gateway files changed >= 1; outside the order: 0; scope map file changed: 1; audit.jsonl changed: 0; allowlist overlay changed: 0; uncommitted gateway paths: 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~29/NFRA_OPALAI.TO-OA-f-14.scoped-consent-envelope.proof_of_spec.json`.
Report once:
- the final scope map as a table, with the `file:line` behind each entry and every entry that differs from the proposal;
- the concierge's resulting consent list, and the scopes of `GRAPH_SCOPES` it no longer asks for;
- the changed regions with `file:line`, and the commit hash(es);
- the three criterion lines, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on `1.0.0_SA_CTO~O` msg 30323 (2026-10-06 ~21:2xZ), under the Andrew-direct record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_211xZ_NFRA_OPEN_CALLS_ALYSSA_NOT_NOW_COO_AI_IF_WORK_G2ND_ANY_TIME.md`
@9480178371. The ruling is R25.3, `org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round19.md:100`, carried to
this project by NFRA_OPLGTW's round-20 analysis (`ROUND_ANALYSIS.round20.md:72`) and its decomposition (`:1545`). No
`<round>` (the R2-A1 precedent).

ONE DECOMPOSITION JUDGMENT, the issuer's: step 4 (the silent acquire). R25.3's sentence names the `/login` consent
only. `get_token` asks for the tier's full envelope, so after a narrow consent the first silent acquire would ask for
scopes that consent never carried. Where the tenant grant covers them it succeeds and the narrowing changes nothing a
token holds; where it does not, the acquire fails into `NeedsLogin`, back to the same narrow `/login`: the dead end
R25.1 forbids. Bounding the acquire by the same function closes both. The CTO reads this at the analysis.

KNOWN RESIDUAL, not in this cell: both legs key on the STATE's email. Row W3-S22 (the account picker lets the signed-in
account differ from the declared one) means an unscoped declared email that signs in as the concierge still redeems the
full envelope. The second deny check in `redeem_consent` runs after the exchange. Narrowing on the VALIDATED principal
would need a second exchange; left for the analysis.

WRITE-SURFACE OVERLAP, placed: NFRA_OPLGTW's OG-rl-9 (`2.0.0_SA_COO~O`, pending) names the whole
`infra/aws/ec2/opal-gateway/` for its release. This cell builds on a worker branch and reaches no host. Its drain to
CLOUD waits until OG-rl-9 is terminal, so r23 ships the bytes it was cut on. The release of this cell is a later order
with CTO+COO+CVO halves.

Risk: gateway code under infra/, WORLD floor (the OA-f-1 and OA-f-7 precedent); nothing deploys here. Three mechanical
criteria; the live proof (the concierge's real consent screen and a Teams read after it) belongs to the release order.

SPAWN ONLY WHEN: at the cut. Slot `~29`, sparse worktree from the issuance commit.

Dry-run at base (821fca2410, ~21:5xZ):
- f14.AC1 base: FAIL as expected (`tests/test_scoped_consent_r253.py absent`).
- f14.AC2 base: PASS as expected (the control: passed 36, failed []).
- f14.AC3 base: FAIL as expected (gateway files changed 0; scope map file changed 0).

fanout: 1 of 1 chains, cap 8.

AMENDMENT A1 (issuer, 2026-10-06 ~22:0xZ): on `1.0.0_SA_CTO~O` ruling msg 30365 (a) on row Z-S57. First build: worker
~29 @95028d4d69, issuer re-grade AC1 6 of 6, AC2 36 / [], AC3 4 files / 0 outside. A1 adds the caller table, the union
rule and a seventh arm; items (4) and (5) of the ruling are bound 5 above and the later release order. The non-email
binding rule (union when set) is the issuer's reading of "without a dead end". Gate limb that graded this
modification: stated in the amendment commit. Z-S57 stays ARMED until the seventh arm passes.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
