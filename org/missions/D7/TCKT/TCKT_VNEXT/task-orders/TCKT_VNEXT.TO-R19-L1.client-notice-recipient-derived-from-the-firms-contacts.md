# TO TCKT_VNEXT.TO-R19-L1 -- BUILD the client notice's recipient as derived from the ticket firm's configured contacts, never from the request body (row S134 item 1; source and tests only)

<to_id>TCKT_VNEXT.TO-R19-L1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~45</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda source path; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R19-nr-1` (`decompositions/TCKT_VNEXT_DECOMP_R19.md`) | **outcome_ref:** row `IRPT_ANLREQ-D2-S134` item 1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~45`.
- **Worktree:** `C:/dev/wk-tckt-vnext-45` (branch `wk-TCKT_VNEXT-45`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~45 <0.9.0_WK_TCKT_VNEXT~45@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `TCKT_VNEXT-D2-W45-S<k>` (take the next free `<k>`). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before
  its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call of any kind: no AWS, no network, no
  mail, no deploy, no apply, no Terraform (`tests/conftest.py` refuses a real call). **Run NO test file by path (`python <file>`): pytest only, with `-p no:cacheprovider`** (a by-path run bypasses the SES guard). Scratch outside the product tree.

### WHY

Row `IRPT_ANLREQ-D2-S134`: the ticket service lets the request body choose where a client notice goes (CTO ruling ADDENDUM 7, item 1). The contract every cell obeys is
`org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md`, section CONTRACT; its item 1 is this cell's.

### THE CELL (`R19-nr-1`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

In `infra/aws/lambda/ticket_center/lambda_function.py` (read first: `_client_recipients` about line 1182, `_recipient_digest`, `notify_client` and `notify_client_isolated` about lines 1204-1252, `create_ticket` about 1324 where `requester.email` is taken from the body about 1373):

1. **The config.** A module-level reader of the env var `CLIENT_NOTICE_CONTACT_MAP`, JSON `{"<firm id>": ["<address>", ...]}`, read at CALL time (so a test sets it with monkeypatch). Unset, empty, malformed JSON, a non-object, or a value that is not a list of strings gives `{}` for that firm; a malformed document also logs one line `WE_CLIENT_CONTACT_MAP_MALFORMED` (never its text).
2. **The derivation.** Rewrite `_client_recipients(item)`: `firm` = `item.requester.firm`; `contacts` = the map's list for that firm (each stripped, empty strings dropped). No firm or no contacts: log `WE_CLIENT_NO_CONTACT firm=<f>` and return `[]` (the existing single-recipient guard in `notify_client` then refuses, as it does for any non-single set). Otherwise `stored` = `item.requester.email` stripped and lower-cased: if it equals (lower-cased) one of the contacts return `[that contact]`; else return `[contacts[0]]` and log `WE_CLIENT_RECIPIENT_IGNORED firm=<f> to_digest=<_recipient_digest(stored)>` (the digest only, never the address). The result is always a list of at most ONE address.
3. **Not changed:** `requester.email` is still STORED from the body exactly as today (display only). The DL notice path (`notify_dl*`, `resolve_recipients`) is a different path and is NOT touched. `submit_form`, `create_ticket` and every route keep their behaviour. `notify_client`'s single-recipient guard and `notify_client_isolated` stay.
4. **Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_notice_recipient_firm.py` (copy the style of `tests/test_client_notify.py`; a fake SES through the module's existing seam, no AWS). One named test per case:
   - the stored requester is a contact of the firm: the notice goes to that address;
   - the stored requester is NOT a contact: the notice goes to the firm's FIRST contact, and the log carries `WE_CLIENT_RECIPIENT_IGNORED` with a digest and no address;
   - the firm has no contacts, or is absent from the map: no SES call, and the log carries `WE_CLIENT_NO_CONTACT`;
   - an unset map and a malformed map send nothing;
   - a body address that is in ANOTHER firm's list is not honoured for this firm;
   - the match is case-insensitive;
   - the recipient set is never more than one;
   - a CREATE with a body `requester_email` of an outside address sends its notice to the firm contact, not the body address;
   - no log line the notice path writes contains a full address.
5. Edit an existing test ONLY where a fixture assumed "the requester's own address receives it" with no map set (likely `tests/test_client_notify.py` and `tests/test_client_mail_digest.py`): give those fixtures a `CLIENT_NOTICE_CONTACT_MAP` listing the same address, so each keeps what it asserts. List each edit with the old and the new fixture line in your record. No existing assertion about another behaviour may change.
6. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~45/mutant_check.py`** (AC2 below) and a short `R19_L1_RECORD.json`: the lines you changed, the test counts, the before-arm (the new tests on the base: every case FAILS), the edited fixtures, `not_read`.

### ACCEPTANCE

<criterion id="R19L1-AC1" cell_refs="R19-nr-1"><invocation>python -m pytest C:/dev/wk-tckt-vnext-45/infra/aws/lambda/ticket_center/tests/test_notice_recipient_firm.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`R19L1-AC1`: the new test file passes with every case of step 4 named in a test, no failures or errors. Also run the whole `infra/aws/lambda/ticket_center/tests/` folder once and record the counts in your record (a drain check; the issuer re-runs it).

<criterion id="R19L1-AC2" cell_refs="R19-nr-1"><invocation>python C:/dev/wk-tckt-vnext-45/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~45/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R19L1-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the product tree with the contact-list restriction removed (the stored requester address is used whatever the firm's list holds), runs the new test file against the copy with pytest, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R19L1-AC3J" cell_refs="R19-nr-1" judgment="true"/>
`R19L1-AC3J` (judgment, graded at L9, never by you): a caller can no longer choose where a firm's notice goes: the recipient is a configured contact of the ticket's own firm, a body address outside the list is ignored and logged by digest only, an absent or malformed config sends nothing, and the single-recipient guard stands.

<expected_criteria>R19L1-AC1 R19L1-AC2 R19L1-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~45/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- **Shared file:** `lambda_function.py` is also edited by `TO-R19-L2` and `TO-R19-L3` (other workers, other slots). Touch ONLY the recipient functions and their config reader, so the three merge cleanly.
- READ only: everything else, including `infra/aws/terraform/` (the environment values are `TO-R19-TR`'s).

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md</decomp_doc>
<owned_cells>R19-nr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~45/TCKT_VNEXT.TO-R19-L1.client-notice-recipient-derived-from-the-firms-contacts.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R19-L1`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R19L1-AC1,R19L1-AC2,R19L1-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source in a worker worktree; nothing is deployed, applied or invoked. The release is `TO-R19-REL`.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler uses the SES permission it already has.
comp-adversary: RUN -- by reading row S134, ruling ADDENDUM 7 item 1 and the contract against this cell; the lens: a body address that reaches another firm's inbox, a log line that prints an address, a notice that goes to nobody without a token, a fixture edit that weakens an assertion. BLIND to: the live firm contacts and the deployed function (denominator: 1 ruling item and 1 contract item read).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ADDENDUM 7 (msg 8833) in round 19; fan-out 4 of 5 chains, cap 4 (dell2 CPU budget). The three lambda cells edit disjoint functions of one file; the issuer merges them. Open input with owner `1.0.0_SA_CTO~DELL2`: the firm contacts (the map ships empty, so no client notice is sent until they are supplied; not release-blocking). Base: `R19L1-AC1` and `R19L1-AC2` FAIL as expected (no test file, no checker file).
