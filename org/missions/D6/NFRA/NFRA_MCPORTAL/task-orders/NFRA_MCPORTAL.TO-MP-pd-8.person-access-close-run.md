# NFRA_MCPORTAL task order -- `MP-pd-8` -- WORKSTREAM PC ROUND 2: the F2 close run -- one test principal switched off and back on, stopped and restored, read back from the store (FWD-21 DONE WHEN, the write half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-8</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-8</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~30</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time close run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only: the grant store through the existing operator read, the change history, and the served gateway for the test principal's calls. The writes in the run are Andrew's, made from the page.
comp-adversary: DECLARED-NOT-APPLICABLE -- each step is read against a source other than the page: the grant store itself, the change history, and a real call by the test principal.
EGRESS CLASS, declared: AWS reads (DynamoDB read through the operator role, the changes table read, S3 where the run needs it) and the test principal's own gateway calls; no write by this cell.
</preflight>

## 1. THE CELL -- `MP-pd-8` (workstream PC round 2, decomposition sections PD.1, PD.2 and PD.6)

**Do not start before the issuer's GO message.** The GO carries, from its ISSUER LINE: the TEST PRINCIPAL (`tid`, `oid`, and the identity
you may call the gateway as), the window `t0`..`t1` (ISO Z) in which Andrew, signed in as the owner on `https://mcp.opalinvest.dev/people`,
made the six changes in this order on that principal's row, and Andrew's own words about the sitting (to be put VERBATIM into a file).
Writes are Andrew's only: the writer verifies the owner's signed header, and you hold none, so you cannot make a change yourself and you must
not try. This cell READS what his six changes did.

The six ops, in order, as Andrew made them from the page: (1) `channel_off`: one channel added to the person's `channels_deny`; (2) `channel_on`:
that channel removed; (3) `tool_off`: one tool added to `tools_deny`; (4) `tool_on`: removed; (5) `stop`: `stopped` set true; (6) `restore`:
`stopped` set false. The GO names the channel and the tool.

Do these:
1. **The store, read under the OPERATOR role.** Assume `arn:aws:iam::313476888478:role/opal-gateway-access-admin` through `.tools/aws sts assume-role`
   (session name starting `mp-pd-8`; keep the credentials in process environment variables only and never print or commit them), and read the person's
   `person_access` record: `Query` or `GetItem` on table `gateway-access-state-table` (us-east-1), pk `POLICY#<tid>#<oid>`, sk `person_access`. The
   operator role is denied `Scan`. You see only the FINAL state of the record, so the six intermediate states come from step 2.
2. **The change history.** Read the changes table's entries for the principal (`GET /api/admin/changes?tid=&oid=` is owner-gated, so read the table
   directly: the table name is `lib/opal_naming.py name('mcportal', None, 'grant-changes', 'table')`; read it with the operator or your own identity
   as the table allows, read-only). Select the entries whose `action` is `set_person_access` and whose `when` is inside `[t0, t1]`. There must be six,
   in order. Each holds `before` and `after` (JSON strings of the record body). For step i, `store_after` is the entry's `after`; `before` must equal
   the previous step's `after` (the first step's `before` is the record before Andrew's sitting: null or the state the GO names).
3. **The effect on a real call.** For each of the six states, the test principal makes ONE real gateway call to a tool of the named channel and one
   to the named tool, and you record admitted or denied, the denial code, and the time. The GO names how the principal calls (its identity, the
   client) and the exact tool calls. If the GO says the effect arm cannot be made (no calling identity), record every `effect_ok` as false with that
   reason: do not substitute a call by another identity. Expected: after `channel_off` and `tool_off` and `stop` the call is denied with code
   `person_record_denied`; after `channel_on`, `tool_on` and `restore` it is admitted (or denied only by a reason that is not this person's record,
   which you name).
4. **Andrew's words.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~30/pd8_andrew_read.md` containing the window and his
   words as the GO quotes them, VERBATIM. Do not paraphrase and do not add a verdict. A judgment criterion is graded on that file.
5. **Run file** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~30/pd8_run.json`: `{"principal": {"tid", "oid"}, "t0", "t1", "steps": [
   {"op", "store_after", "history_row", "store_after_matches": <bool>, "history_before_after": <bool>, "effect": {"call", "admitted", "code", "at"},
   "effect_ok": <bool>}, ... six ...], "final_record": <the store read in step 1>}`. `store_after_matches` is true when the step's history `after` equals the
   intended change (the op's field changed as named, the other fields as before); `history_before_after` is true when the entry exists with `before`
   equal to the previous `after`. Commit it (no credential value in any file), then run AC1.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no store write, no record write, no change of any grant, no deploy.
2. The assumed credentials never leave the process environment of your commands.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a). If you cannot meet a
   criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~30/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/**`, `lib/opal_naming.py`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W30-S<k>` (the next free k for W30). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-8"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd8.AC1.sh; echo "exit=$?"</invocation><expect>run=read ops=ordered store_after_matches=6 of 6 history_before_after=6 of 6 effect_ok=6 of 6 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pd-8" judgment="true"/>
</proof_of_spec>

AC2 is a JUDGMENT criterion, graded by `3.0.0_SA_CVO~Z` at L9 on `pd8_andrew_read.md` and the run file, never by you: did Andrew himself switch a
channel, a tool and the person off and back on from the page, and does his own account say the page showed it? Record it in your instance under
`UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`. Give it no PASS or FAIL.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~30/NFRA_MCPORTAL.TO-MP-pd-8.person-access-close-run.proof_of_spec.json`.
Report once, with: the check output; the commit hash; the six steps (op, the history entry's time, `after` summarized as the changed field, admitted or denied
with the code); `final_record`'s `revision` and `stopped`; the operator-role caller ARN; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PC round-2 issuance (decomposition v10). Gate G-WRITE (PD.6): MP-pd-7 drained, OG-cp-1 live, a test principal
with a real calling identity named by the issuer, and Andrew's sitting on the People page (no seat can produce the owner's signed header). The
sitting is queued as a call when G-REL7 holds. This is the read-and-grade half of FWD-21's DONE WHEN ("on a test principal, one channel switched off
and back on, one tool switched off and back on, and the person stopped and restored, each from the page; each change is read back from the grant
store and honoured on that person's next gateway call"). Check dry-run at base: AC1 FAIL (run file absent); green and red arms exercised with
synthetic files. The test principal is NOT chosen here: it must have a real Entra login to call the gateway.

<status>staged</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~30</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
