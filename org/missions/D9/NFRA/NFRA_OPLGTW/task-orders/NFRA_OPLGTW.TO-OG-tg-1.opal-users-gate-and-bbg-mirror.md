# NFRA_OPLGTW task order -- `OG-tg-1` -- the Bloomberg concierge mirrors Andrew's identity, behind an Opal-users-only Teams gate; sender identity on Teams reads for every caller (PRD v2.3 item 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tg-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-tg-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~44</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; Graph is faked in the tests.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is PRD v2.3 item 4 (org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @4fb7326f67) on Andrew-direct ~03:2xZ and ~03:3xZ (records org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md and ANDREW_DIRECT_20261009_033xZ_BBG_CONCIERGE_OPAL_USERS_ONLY_GATE.md), CTO msgs 32320, 32327, 32339.
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-tg-1` (decomposition addendum R3-T.30, workstream GATE-R30; ships in r30, after r29)

Andrew, verbatim, ~03:2xZ: *"opal-gateway-bbg should be an exact copy of opal-gateway for now, just make it mirror
whatever is on opalgateway for consistency, eventually we will make rules but not yet."* And ~03:3xZ (via the CTO): the
mirror ships ONLY together with an Opal-users-only gate on that principal's Teams traffic, "same release or neither".
The Bloomberg concierge principal is the identity `opalbloomberg@opalinvest.com` (the code calls it the scoped concierge
identity; do not print the address in logs or records).

Do, in `infra/aws/ec2/opal-gateway/` (read `app/tools.py` lines ~1030-1220 first: `read_chat_messages`,
`send_chat_message`, `read_channel_messages`, `send_channel_message`, `poll_addressed_impl`,
`poll_addressed_teams_messages`; and `app/identity_scope.py`):
1. **Sender identity on reads, for EVERY caller (ships first; it unblocks the concierge by itself, CTO msg 32339).**
   `poll_addressed_teams_messages` and `read_chat_messages` (and `read_channel_messages` if it shares the shaping) return,
   per message, the sender's Entra UPN and tenant id taken from Graph's `from.user` (the fields Graph returns there; if the
   UPN needs a second Graph read, do it per distinct sender, bounded, and name the call), beside today's fields. A sender
   whose identity cannot be read gets both fields `null`. Never derive identity from a display name.
2. **The gate, for the concierge principal ONLY.** (a) Teams reads (poll, chat, channel) DROP any message whose sender UPN
   is not `@opalinvest.com`, and any whose identity is unreadable (unreadable = external); count the drops in the audit
   record (counts only). (b) `send_chat_message` and `send_channel_message` REFUSE a chat or channel that has ANY member
   whose UPN is not `@opalinvest.com` or is unreadable (read the membership from Graph; a structured refusal with a code,
   audited), and admit one whose members are all `@opalinvest.com`. Every other principal is untouched.
3. **The mirror (code half).** Remove the concierge from `_SEED` in `app/identity_scope.py`, and its two rows from
   `identity_tool_allowlist.txt` (`opal_data_refresh_upload client=...`, `opal_data_refresh_status`), so it is UNSCOPED
   like Andrew's identity; a comment at each change cites the ~03:2xZ record. The client-qualified upload row's purpose
   (the concierge's upload limited to the operator's client) is then gone: state that in your report as a consequence,
   not a choice. The data-grant half of the mirror (the concierge's grants set to Andrew's width) is a release-time
   operator write, NOT yours.
4. **Tests**, offline, new file `infra/aws/ec2/opal-gateway/tests/test_opal_users_gate.py`, named EXACTLY
   `test_ogtg1_ac01` .. `test_ogtg1_ac06` as the header of
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tg1.AC1.sh` lists them; reuse the Graph fakes of
   `tests/test_teams_route.py` and `tests/test_teams_reader_fallback.py`. Use made-up tenants and `.example` addresses for
   the external arms; never a real person's address.
5. **Pinned tests.** `tests/test_identity_scope.py`, `tests/test_identity_scope_status_row.py`,
   `tests/test_scoped_consent_r253.py` (and any other that fails ONLY because the concierge's seed or rows are gone):
   change ONLY the pinned expectation, name each line in your report. Delete or rename no test.
6. Run, each in its own process, and state totals: the new file, the three Teams suites, the three identity-scope suites,
   `tests/test_tool_classification_composition.py`.

**AMENDMENT A1 (issuer, 2026-10-09 ~05:1xZ; your rows Z-W44-S1 and S3).** Three more tests pin the concierge as scoped
and are now in `<paths>`: `tests/test_teams_reader_fallback.py` (line 75 reads `_SEED[...]`), `tests/test_transcript_tools.py`
(`test_scoped_and_restricted_principals_denied`) and `tests/test_login_admit_r24.py` (`test_oglg1_ac05`). Move ONLY the
pinned expectation in each, the same way you moved the identity-scope suites (a fixture address carrying the old seed
where the test's subject is "a scoped identity"; the real concierge where its subject is the concierge); name each line;
delete or rename no test. Then re-run both criteria and every suite you ran. The fail-closed channel path for the
concierge (no `User.ReadBasic.All`, no `ChannelMember.Read.All` consented) and the re-consent are ACCEPTED as written;
they go into r30's halves, not this cell.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~44/`.

## 2. BOUNDS

- No release, no deploy, no host act, no grant write, no AWS call. BUILT and HELD on your branch for r30.
- No other principal's behaviour changes; no new tool, route or bearer.
- Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/identity_scope.py
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt
infra/aws/ec2/opal-gateway/tests/test_opal_users_gate.py
infra/aws/ec2/opal-gateway/tests/test_identity_scope.py
infra/aws/ec2/opal-gateway/tests/test_identity_scope_status_row.py
infra/aws/ec2/opal-gateway/tests/test_scoped_consent_r253.py
infra/aws/ec2/opal-gateway/tests/test_teams_reader_fallback.py
infra/aws/ec2/opal-gateway/tests/test_transcript_tools.py
infra/aws/ec2/opal-gateway/tests/test_login_admit_r24.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~44/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W44-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tg1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 6 of 6; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tg1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_teams_format\.py: pytest rc=0 .*removed or renamed 0.*test_teams_reader_fallback\.py: pytest rc=0 .*removed or renamed 0.*test_teams_route\.py: pytest rc=0 .*removed or renamed 0.*test_identity_scope\.py: pytest rc=0.*test_identity_scope_status_row\.py: pytest rc=0.*test_scoped_consent_r253\.py: pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: identity fields for everyone; the gate's two arms for the concierge only; the concierge unscoped.
- `AC2`: the Teams suites pass whole and lost no test; the identity-scope suites pass with only pinned expectations moved.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-tg-1.opal-users-gate-and-bbg-mirror.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the diff of every app file; how sender identity is read (which Graph field or call);
   each pinned expectation you moved, with its line; every test file run with its totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32, workstream GATE-R30: the issuer held Andrew's Bloomberg mirror out of r29 (OG-rl-15 A6 @38f240bdab) because
  it must ship WITH this gate ("same release or neither"); this cell builds both for r30, cut right after r29 drains.
- The data-grant half of the mirror is a release-time operator write under r30's halves.
- A1 (2026-10-09): three seed-pinning tests added to <paths> (rows Z-W44-S1, S3); channel fail-closed and re-consent
  carried to r30's halves. Graded by no gate limb as a modification.
- Pre-cut: tg1.AC1 base FAIL as expected (test file absent); tg1.AC2 base PASS as expected (teams_format 35, reader_fallback
  5, route 21, none removed; identity_scope 10, status_row 4, scoped_consent 7 rc 0).

<status>pending</status>
<round>32</round>
<workstream>GATE-R30</workstream>
<slot>~44</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
