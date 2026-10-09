# TO IRPT_CUSTDY.TO-CU-g-2a -- round 7 CU-g-5 (E2a): one real Performance client statement, retained and persisted through the live writer

<to_id>IRPT_CUSTDY.TO-CU-g-2a</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~18</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~K2-E2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-g-5` (`decompositions/IRPT_CUSTDY_DECOMP.round7.addendum2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** irpt-ycharts-generate release 5 (E11) LIVE. The issuer spawns this order only after reading
it live; the spawn is the GO.

---

## WORKER FACE

### THE CELL

`CU-g-5` (E2a): ONE real Performance client statement for ONE real household is retained, and its household document is persisted through
the live writer. "Performance client statement" is the product's name; in code it is `CUSTODY_REPORT`, policy
`irpt-custody-x10-v1`. The live pieces you use (READ the code, never edit it; it is IRPT_BCKEND's):

- **The submission:** `infra/aws/lambda/investor-reporting/ycharts/generate/custody_submission.py`. After release 5 it builds its
  retained repositories under `irpt-custody-x10-v1` (IRPT_BCKEND E11, order `TO-IB-yr-691`). Find how a submission is created and
  retained in the live stack. One submission, one household, one real as-of date: no batch.
- **The writer:** `POST /api/scoped/investor-reporting/custody-report`, operation `custody-report-persist`, behind the CUSTOM portal
  authorizer, and Opal-only.
  - Body: `retained_request` (the submission, by reference) + `document` (the household document) + optional `provenance`.
  - The owner and accounts come from the retained submission. A body carrying owner, principal, account_ids, tenant or firm_id is
    refused by name, so do not send them.
  - Code: `infra/aws/lambda/investor-reporting/export/custody_persist.py`, `custody_write.py`, `entry.py`. Its release record is
    `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_90_92_P_DRAIN_END_20261009.md`.
  - The scoped-route call pattern IRPT_BCKEND's after-reads already use is how you authenticate. Reuse it; do not invent a credential.
- **The household document:** this project's hop 3 producer, `data/assets/scripts/gold/irpt_custody/hop3_real_run.py` +
  `client_report_figures.py`. It carries `as_of_date` (TO-CU-g-4) and is validated by `validate_document`. Pick the household
  by this project's existing pick (`pick_reread.py` / round-1 pick); do not choose a new one.

**Build:** `data/assets/scripts/gold/irpt_custody/e2a_real_statement.py` with three subcommands.
- `run`: retain the submission, then persist the document through the route. Write the refs only to the deliverable
  `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~18/E2A_REFS.json`: the submission ref, the persisted object
  ref, its revision, the policy revision, the as-of date, the household's opaque id and the HTTP status of each call. No figures.
- `verify-submission`: re-read the retained submission LIVE from its store and print
  `SUBMISSION RETAINED policy=<revision> ref=<ref>`.
- `verify-persisted`: re-read the persisted object LIVE from the retained store and print
  `PERSISTED kind=CUSTODY_REPORT revision=<n> ref=<ref>`.

Add an offline test, `data/assets/scripts/gold/irpt_custody/tests/test_e2a_real_statement.py`. It asserts that the persist body
never carries the five refused keys, and that the refs file holds no figure (no number other than the revision and HTTP status).

**Hand-off:** your report gives the two refs. `2.0.0_SA_COO~P2` owes the owner read by reference and the other-firm refusal on them
(not yours).

### ACCEPTANCE

<criterion id="CU21-AC1" cell_refs="CU-g-5"><invocation>python data/assets/scripts/gold/irpt_custody/e2a_real_statement.py verify-submission --refs org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~18/E2A_REFS.json</invocation><expect>SUBMISSION RETAINED policy=irpt-custody-x10-v1</expect></criterion>
`CU21-AC1`: the real submission is retained under the Performance client statement policy, read live.

<criterion id="CU21-AC2" cell_refs="CU-g-5"><invocation>python data/assets/scripts/gold/irpt_custody/e2a_real_statement.py verify-persisted --refs org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~18/E2A_REFS.json</invocation><expect>PERSISTED kind=CUSTODY_REPORT</expect></criterion>
`CU21-AC2`: the household document is persisted through the live writer, read live from the retained store.

<criterion id="CU21-AC3" cell_refs="CU-g-5"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_e2a_real_statement.py</invocation><expect>passed</expect></criterion>
`CU21-AC3`: the persist body never asserts identity, and the refs file carries no figure.

<expected_criteria>CU21-AC1,CU21-AC2,CU21-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block plus this order's file. Scaffolding under `.scratch/`, uncommitted.
- **Writes to AWS: exactly two acts.** The one submission and the one persist, both through the live product path. No other AWS write:
  no apply, no IAM, no direct table or S3 put, no Lambda invoke that bypasses the route. Reads are free.
- **Client data.** Figures stay in the retained store; files and messages carry refs and counts only.
- **Never edit IRPT_BCKEND code.** A refusal from the live path is a finding: write a row with the refusal's name, stop and report.
  Never work around it.
- Commits via `.tools/safe-commit.sh` with your serial as author (on a merge-in-progress refusal, wait and retry). A surprise row is
  committed in the same turn you write it.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason and a row (id `IRPT_CUSTDY-W18-S<k>`;
  `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/e2a_real_statement.py
data/assets/scripts/gold/irpt_custody/tests/test_e2a_real_statement.py
org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~18/E2A_REFS.json
org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~18/IRPT_CUSTDY.TO-CU-g-2a.real-statement-retained-and-persisted.proof_of_spec.json
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round7.addendum2.md</decomp_doc> (round 7, addendum 2), cell `CU-g-5`.
<owned_cells>CU-g-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU21-AC1, CU21-AC2, CU21-AC3. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~18/IRPT_CUSTDY.TO-CU-g-2a.real-statement-retained-and-persisted.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU21-AC1,CU21-AC2,CU21-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the household's opaque id, the submission and persisted refs, the policy revision, each call's status and each
criterion's output. No figure.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-off real run of an already-released product path; no schedule.
comp-iam: RUN -- the live role was widened by IB-pr-373's IAM leg (applied 22:47:14Z, read back live by the laptop issuer, b8d0c40390); the run exercises it, never changes it.
comp-adversary: RUN -- both mechanical criteria re-read the LIVE store, never the run's own stdout; the refused-key and no-figure checks are a test, not a promise; BLIND: the submission's live creation path is discovered by the worker from code, so a mismatch is a row, not a guess.
lane: the <paths> block IS the grant; the two AWS writes are the product path's own, named above.
</preflight>

Source: round-7 ADDENDUM 2 (this issuer, 2026-10-09); IRPT_BCKEND ADDENDA 9-11 (msgs 1475, 1513, CTO 1416); ~P2 packets a59adb446a
(writer) and 18d4c45c1d (live + the owed reads). Gate: release 5 live (issuer reads it before the spawn).

## AMENDMENT 1 (issuer, 2026-10-09 ~03:4xZ) -- HELD: the executor moves to dell2's applier; do NOT spawn this order as written

The worker on this order, `0.9.0_WK_IRPT_CUSTDY~18`, stopped before any AWS write (row W18-S1, @c562748b71), and CTO rulings
2123/2296/2310 change how the cell runs:

- The writes go through ONE named service subject, `svc-custody-statement`. Its firm comes from the token claim (`cottonwood`). It is
  admitted on custody-report-persist, POST /analysis and POST /export by `2.0.0_SA_COO~P2`'s writer cell (ruling (b), msg 2310).
- Its token is minted under the never-widen pair
  `deliverables/2.0.0_SA_COO~K2/NEVER_WIDEN_PAIR_SVC_CUSTODY_STATEMENT_MINT.md` (COO half unsigned until that cell drains). Only
  `0.7.0_AE_CloudOps~DELL2` reads the token.
- So the two writes and the live re-reads (CU21-AC1/AC2) are an APPLY act by `0.7.0_AE_CloudOps~DELL2`. They are cut as an apply order
  in that seat's folder, with a GO, after: (1) irpt-ycharts-generate release 6 is live (TO-APPLY-Y77), (2) ~P2's writer cell drains,
  (3) the mint pair lands.
- CU21-AC3 (the offline no-identity / no-figure test) stays a worker build and is folded into that cut.

**Graded by:** no gate limb. This amendment changes neither `<paths>` nor `<placeholders>`, and to-pipeline-gate grades only on a new
order or a declared placeholder. This order stays `pending` and unspawned until the recut supersedes it.
