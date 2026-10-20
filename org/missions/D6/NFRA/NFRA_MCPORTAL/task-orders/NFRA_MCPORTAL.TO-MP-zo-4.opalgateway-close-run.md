# NFRA_MCPORTAL task order -- `MP-zo-4` -- WORKSTREAM OGW ROUND 2: the close run on /opalgateway -- one test principal switched off and back on, stopped and restored, read three ways (FWD-24, 25, 27, 28, 29)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zo-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zo-4</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~44</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time close run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only: the grant store through the existing operator read, the change history, and the served gateway for the test principal's calls. The writes in the run are Andrew's, made from the page.
comp-adversary: DECLARED-NOT-APPLICABLE -- each step is read against a source other than the page: the grant store itself, the change history, and a real call by the test principal.
EGRESS CLASS, declared: AWS reads (DynamoDB read through the operator role, the changes table read) and the test principal's own gateway calls; no write by this cell.
</preflight>

## 1. THE CELL -- `MP-zo-4` (workstream OGW round 2, decomposition section OGW2.1)

**Do not start before the issuer's GO message.** The GO carries, from its ISSUER LINE: the TEST PRINCIPAL (`tid`, `oid`, and the identity you may call the
gateway as), the channel and the tool to switch, the exact tool calls to make, the window `t0`..`t1` (ISO Z) in which Andrew, signed in as the owner on
`https://mcp.opalinvest.dev/opalgateway`, made the six changes in this order on that principal's row, and Andrew's own words about the sitting (to be put
VERBATIM into a file). Writes are Andrew's only: the writer verifies the owner's signed header, and you hold none, so you cannot make a change yourself and
you must not try. This cell READS what his six changes did.

The six ops, in order: (1) `channel_off`: one channel added to the person's `channels_deny`; (2) `channel_on`: that channel removed; (3) `tool_off`: one tool
added to `tools_deny`; (4) `tool_on`: removed; (5) `stop`: `stopped` set true; (6) `restore`: `stopped` set false.

Do these:
1. **The store, read under the OPERATOR role.** Assume `arn:aws:iam::313476888478:role/opal-gateway-access-admin` through `.tools/aws sts assume-role`
   (session name starting `mp-zo-4`; keep the credentials in process environment variables only and never print or commit them), and read the person's
   `person_access` record: `GetItem` on table `gateway-access-state-table` (us-east-1), pk `POLICY#<tid>#<oid>`, sk `person_access`. The operator role is
   denied `Scan`. You see only the FINAL state of the record, so the six intermediate states come from step 2.
2. **The change history.** Read the changes table's entries for the principal (the table name is `lib/opal_naming.py name('mcportal', None,
   'grant-changes', 'table')`; read it with the operator role or your own identity as the table allows, read-only). Select the entries whose `action` is
   `set_person_access` and whose `when` is inside `[t0, t1]`. There must be six, in order. Each holds `who`, `before` and `after` (JSON strings of the record
   body). For step i, `store_after` is the entry's `after`; `before` must equal the previous step's `after` (the first step's `before` is the record before
   Andrew's sitting: null or the state the GO names). `history_attributed` is true when the entry's `who` is a non-empty string.
3. **The served gateway agrees (FWD-29).** For each of the six states, the test principal makes ONE real gateway call to a tool of the named channel and one to
   the named tool, and you record admitted or denied, the denial code, and the time. The GO names how the principal calls (its identity, the client) and the
   exact tool calls. If the GO says the effect arm cannot be made (no calling identity), record every `effect_ok` as false with that reason: do not
   substitute a call by another identity. Expected: after `channel_off`, `tool_off` and `stop` the call is denied with code `person_record_denied`; after
   `channel_on`, `tool_on` and `restore` it is admitted (or denied only by a reason that is not this person's record, which you name). `effect_ok` is true
   when the call agrees with the switch the store state implies.
4. **Andrew's words.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~44/zo4_andrew_read.md` containing the window and his words
   as the GO quotes them, VERBATIM. Do not paraphrase and do not add a verdict. A judgment criterion is graded on that file.
5. **Run file** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~44/zo4_run.json`: `{"principal": {"tid", "oid"}, "t0", "t1", "steps": [
   {"op", "store_after", "history_row", "store_after_matches": <bool>, "history_before_after": <bool>, "history_attributed": <bool>, "effect": {"call",
   "admitted", "code", "at"}, "effect_ok": <bool>}, ... six ...], "final_record": <the store read in step 1>}`. `store_after_matches` is true when the step's
   history `after` equals the intended change (the op's field changed as named, the other fields as before); `history_before_after` is true when the entry
   exists with `before` equal to the previous `after`. Commit it (no credential value in any file), then run AC1.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no store write, no record write, no change of any grant, no deploy.
2. The assumed credentials never leave the process environment of your commands.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a). If you cannot meet a criterion as
   written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~44/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/**`, `lib/opal_naming.py`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W44-S<k>` (the next free k for W44).
APPEND ONLY: add your row after the last one and leave every earlier byte untouched. `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is
`2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zo-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)run=read ops=ordered store_after_matches=6 of 6 history_before_after=6 of 6 history_attributed=6 of 6 effect_ok=6 of 6.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-zo-4" judgment="true"/>
  <criterion id="AC3" cell_refs="MP-zo-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo4.AC3.sh; echo "exit=$?"</invocation><expect>(?s)deployed_commit=\S+; admin_people_access.py at it: yes; mounted in admin_api.py=[1-9]\d*; @owner_only decorators=([2-9]|\d{2,}).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

AC3 reads git at the live release's commit: the gateway mounts the people-access routes and both handlers sit behind `owner_only` (the CVO's W1' note, gateway side; the writer side is `MP-zo-3`'s fifth test, already drained).

AC2 is a JUDGMENT criterion, graded by `3.0.0_SA_CVO~Z` at L9 on `zo4_andrew_read.md` and the run file, never by you: did Andrew himself switch a channel, a tool and the
person off and back on from `/opalgateway`, and does his own account say the page showed it, with the audit list listing the six? Record it in your instance under
`UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`. Give it no PASS or FAIL.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~44/NFRA_MCPORTAL.TO-MP-zo-4.opalgateway-close-run.proof_of_spec.json`.
Report once, with: the check output; the commit hash; the six steps (op, the history entry's time, `after` summarized as the changed field, admitted or denied with
the code); `final_record`'s `revision` and `stopped`; the operator-role caller ARN; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** issued in OGW round 2 (decomposition OGW2.1), the CTO's ROUND_ANALYSIS.ogw-round1.md item 1 and 2; it was drafted in round 1 and refused as a second round-1 issuance. Gate G-OGW-CLOSE: the mount `OG-mp-1`
(`2.0.0_SA_COO~O` batch17 `OG-rl-18`, not before 2026-10-22T06:00Z) and the bundle at mcportal f90f03a live on the host; the writer is already live (`MP-pd-7`);
Andrew has named a test principal with a real calling identity and the sitting is queued as ONE call at the cut (no seat can produce the owner's signed header).
Supersedes `MP-pd-8` (same six ops and run-file schema; adds the `who` read and the served-agreement framing; the page is `/opalgateway`, not `/people`); `MP-pd-8`
is cancelled in place when this order is issued. The unattributed arm (a store-direct write in a test tree) is proven by `MP-zo-2`'s test and is not repeated served.
Check `zo4.AC1.sh` dry-run at base: FAIL (run file absent); green and red arms exercised with synthetic files (see the staging commit).

**GO OWED (issuer):** GO owed: issued when batch17 (OG-rl-18, the OG-mp-1 mount) has closed and the bundle at f90f03a is live, and Andrew has named the test principal (open call sitez-20261020T212417Z-ee12). No worker is spawned until the GO file is written.

<status>pending</status>
<round>2</round>
<workstream>OGW</workstream>
<slot>~44</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
