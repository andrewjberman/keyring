# TO NFRA_CTLPLN.TO-CT-i-11 -- workstream INBOUND round 6 CT-i-11: the gateway reads Andrew's teams, their channels, and a channel's posts with replies and mentions

<to_id>NFRA_CTLPLN.TO-CT-i-11</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~39</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-11` (`decompositions/NFRA_CTLPLN_DECOMP.inbound6.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-11`. The Opal gateway (`infra/aws/ec2/opal-gateway/app/`, a Starlette app) serves Andrew's Teams assistant under
`/hx/teams` in `app/teams_route.py`: `/me`, `/chats`, `/chats/{chat_id}/messages` (GET and POST), and one channel thread's
`/channels/{team_id}/{channel_id}/messages/{message_id}/replies` (GET and POST). Every Graph call goes through `_graph()`, which
refuses any path not on the verb's allowlist (`_GET_ALLOWED`, `_POST_ALLOWED`) before a token is fetched. The assistant cannot
see a channel post or reply that @mentions Andrew, because no route reads a channel's messages. This cell adds three READ routes,
and the mentions on every projected message. The routes are mounted in `app/server.py` (~line 1096, the `Route(teams_route...)`
lines).

**The contract** (another cell of this round builds the assistant's side against exactly this; do not change it):

```
GET /hx/teams/teams                                     -> {"rows": [{"team_id", "display_name"}], "count", "next_page_token"}
GET /hx/teams/teams/{team_id}/channels                  -> {"rows": [{"channel_id", "display_name", "membership_type"}], "count", "next_page_token"}
GET /hx/teams/channels/{team_id}/{channel_id}/messages  -> {"rows": [MSG + {"replies": [MSG, ...]}], "count", "next_page_token"}
MSG (every route that projects a message, chats included) gains "mentions": [{"user_id", "name"}]  (a user mention only)
```

Graph paths: `/me/joinedTeams`; `/teams/{team_id}/channels`; `/teams/{team_id}/channels/{channel_id}/messages` with
`$expand=replies`. Same bearer check, same `page_size` (1 to 50) and opaque `page_token` rules as the existing routes (`_page`,
`_mint_token`, `_read_token`, `_continuation`). In Graph a mention is `{"id", "mentionText", "mentioned": {"user": {"id",
"displayName"}} | {"conversation": {...}} | {"application": {...}}}`; only a `user` mention is projected.

### BUILD, IN THIS ORDER

1. **Measure first**, in your deliverables folder, `CHANNEL_READ_SCOPES_MEASURED.md`: the Microsoft Graph delegated scopes the
   gateway's token for `MS_INGEST_IDENTITY` is requested with (read `app/token_broker.py` and `app/config.py`; quote file and
   line), and for each of the three Graph paths the scope Microsoft documents as needed (Team.ReadBasic.All,
   Channel.ReadBasic.All, ChannelMessage.Read.All, or as you find in the code's own comments; say where each claim comes from).
   State plainly which needed scopes the requested list does not carry. You cannot read the live consent; say so.
2. `app/teams_route.py`: three route constants, three GET allowlist entries with the existing strict id patterns (`_TEAM`,
   `_CHANNEL`), a `project_team`, a `project_channel`, `mentions` added to `project_message`, the three kinds in `_handle`, and
   three endpoint functions. The audit line carries ids and counts only, never a name or text (the existing tests assert this).
   No POST is added.
3. `app/server.py`: mount the three routes beside the existing `teams_route` lines, GET only.
4. `tests/test_teams_route.py`: add cases in the file's own style (Graph and the token broker stubbed): each new route returns
   the contract's shape; an invalid team or channel id is 400 and calls no Graph; a page token minted for one channel is refused
   on another; a mention of a user is projected and a `conversation` mention is not; a chat message now carries `mentions`; a
   Graph path off the allowlist (for example `/teams/{id}/members`) is still refused; the audit carries no display name.

### RULES FOR THIS CELL

- **Deploy nothing.** No `terraform`, `safe-apply`, `aws` call, SSH, SSM or restart of any gateway. Nothing leaves this machine.
- Edit nothing but the files in `<paths>`. Change no existing route's behaviour beyond the additive `mentions` key.
- No real chat, team, channel, message, person's or firm's name in any file you write; synthetic labels only, as the test file
  already does. No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi11-AC1" cell_refs="CT-i-11"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/ec2/opal-gateway/tests/test_teams_route.py && echo ROUTE-SUITE ok=True</invocation><expect>ROUTE-SUITE ok=True</expect></criterion>
`CTi11-AC1` -- the built behaviour and its bound in one run: the new cases (shapes, refusals, mentions, no names in the audit) and the 14 existing cases (14 passed at the base, issuer's dry run) all pass.

<criterion id="CTi11-AC2" cell_refs="CT-i-11"><invocation>python "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_ct_i_11_contract.py"</invocation><expect>CONTRACT-CT-i-11 ok=True</expect></criterion>
`CTi11-AC2` -- the issuer's contract check (read it; do not edit it): the allowlist admits the three new GET paths, refuses a neighbour path and any new POST, and the app mounts the three contract routes GET-only. It fails at the base.

<criterion id="CTi11-AC3" cell_refs="CT-i-11" judgment="true"/>
`CTi11-AC3` -- JUDGMENT, never self-graded: `CHANNEL_READ_SCOPES_MEASURED.md` names, from the code, the scopes requested and the scopes the three paths need, and which are missing.
</proof_of_spec>

<expected_criteria>CTi11-AC1,CTi11-AC2,CTi11-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Record `CTi11-AC3` in the instance with NO verdict (status
`UNVERIFIABLE-BY-INSTRUMENT`, the reason naming `3.0.0_SA_CVO` as its grader). Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~39/NFRA_CTLPLN.TO-CT-i-11.gateway-channel-read-routes.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi11-AC1,CTi11-AC2,CTi11-AC3`, and flip `<status>` to
`complete` only when both mechanical criteria pass and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W39-S<k>`;
append lines only to the investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound6.md</decomp_doc>
<owned_cells>CT-i-11</owned_cells>
</decomp_ref>

<paths>
infra/aws/ec2/opal-gateway/app/teams_route.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_teams_route.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 AWS policies; the cell touches Microsoft Graph delegated scopes, which no AWS lens reads, and it MEASURES them (AC3) rather than changing them. BLIND: the live consent on the tenant; a missing scope is a consent act after the drain.
comp-adversary: RUN -- a route that widens Graph reach past reading (no POST added; AC2 refuses a new POST path); an id pattern loose enough to reach another Graph path (strict `_TEAM`/`_CHANNEL`, neighbour path refused in AC2); names leaking into the audit (a test asserts none); a page token replayed across channels (a test); a deploy by a build cell (forbidden). BLIND: Graph's real response shape for `$expand=replies` is read from documentation and stubs, not a live call; the seam is probed at the drain.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20; `1.0.0_SA_CTO` direction msg 107165 item (2).
