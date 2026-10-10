# TO COMM_ASSIST.TO-CA-e-2 -- round 13 CA-e-2: pin firm_domains() to C-MAIL's five parties

<to_id>COMM_ASSIST.TO-CA-e-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~6</issued_to>
<issued_by>2.0.0_SA_COO~ZZ</issued_by>
<issued_date>2026-10-10</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>

**Directive:** D9 | **Fabric:** site-z | **Decomp cell:** `CA-e-2` (`decompositions/COMM_ASSIST_DECOMP.round13.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-e-2`. Andrew's assistant considers an email only when the sender's domain belongs to one of FIVE named parties:
Cottonwood, Inflection, 49 Financial, Alongside, and Opal (internal). The function that supplies those domains,
`firm_domains()` in `data/transcripts/scripts/teams_chat/mail_requests.py` (read lines 1-95), builds its map from (1) EVERY
client firm in the registry that has a tenant `email_domain` and (2) the mail-parties record. So a sixth client firm added to
the registry tomorrow would silently be admitted. Pin it to the five.

The five, by PARTY KEY (the keys the function already returns): `cottonwood`, `inflection`, `49financial`, `alongside`, `opal`.
Today the function returns four of them; `alongside` has no measured domain yet and stays absent.

### BUILD

1. In `mail_requests.py` only:
   - add a module constant naming the five party keys (a tuple), with a one-line comment citing C-MAIL clause 9, and keep it
     consistent with the existing `FIRMS_NAMED = 5`;
   - `firm_domains()` returns only entries whose key is one of the five; everything else about it is unchanged (where the
     domains are read from, the `considered`/`measured` filtering, the shape `{party: [domains]}`);
   - update its docstring in one sentence.
2. Party keys are NOT domains. Never type a domain string anywhere: C-MAIL requires every domain to be read from the estate's
   records. The existing test `data/transcripts/scripts/tests/test_inbound_mail_poll.py` has an arm (`domains_not_typed`) that
   checks this; it must stay green.

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. No AWS call, no deploy, no network.
- No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAe2-AC1" cell_refs="CA-e-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r13/checks/check_e2_five_pinned.py"</invocation><expect>E2-FIVE ok=True</expect></criterion>
`CAe2-AC1` -- the issuer's check (read it; do not edit it): a synthetic registry with the five plus a sixth client firm returns exactly the five; the live registry's keys are a subset of the five. It prints ok=False at the base.

<criterion id="CAe2-AC2" cell_refs="CA-e-2"><invocation>python data/transcripts/scripts/tests/test_inbound_mail_poll.py</invocation><expect>MAIL-POLL ok=True arms=8/8</expect></criterion>
`CAe2-AC2` -- the bound: the mail poller's existing eight arms, including `domains_not_typed`, still pass.
</proof_of_spec>

<expected_criteria>CAe2-AC1,CAe2-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~6/COMM_ASSIST.TO-CA-e-2.pin-five-parties.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAe2-AC1,CAe2-AC2`, and flip `<status>` to `complete` only
when both criteria pass and the instance is VALID. Your surprise rows are `COMM_ASSIST-W6-S<k>`; append only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round13.md</decomp_doc>
<owned_cells>CA-e-2</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-e-2.pin-five-parties.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~6/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; local code only.
comp-adversary: RUN -- a typed domain string (refused; party keys only, and AC2's domains_not_typed arm stays green); a pin that drops a live party (refused: AC1's live-subset arm reads the four live keys); a pin that changes the domain filtering (refused: BUILD 1).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `a89f5575b1`: CAe2-AC1 base: FAIL as expected (sixthfirm present); CAe2-AC2 base: PASS as expected (8/8).
Source: CTO round-12 analysis `ledger/ROUND_ANALYSIS.round12.md` @82f10ddf63 E2 (carried from CTO msg 32638); PRD v0.3 C-MAIL.
