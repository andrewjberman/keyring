# TO IRPT_ANLREQ.TO-AR-y-373.fwd1-mint-allowed-firm-ids -- the FWD-1 synthetic staff row carries allowedFirmIds as a list holding the ONE firm the run files under (49financial), and the read-back checks that exact list and prints the scope; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-373</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~167</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ34</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one script file in a deliverable folder; nothing is called, minted or filed)
**Decomp cell:** `AR-y-373` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (the helper is unchanged since worker 149)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~167`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-167` (branch `wk-IRPT_ANLREQ-167`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~167 <0.9.0_WK_IRPT_ANLREQ~167@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (a row id `IRPT_ANLREQ-D2-W167-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). The workspace worktree shows ` M portal`: never commit it. No non-ASCII in what you add. Every `.py` you add or edit passes `bash .tools/commit-gate.sh <file>`.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, no boto3 call (the helper imports boto3 only inside its functions; your tests never reach them). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.

### THE CELL (`AR-y-373`, inlined)

*Context. The helper `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py` writes ONE `opal-users-v2` row (key `USER#fwd1-staff-r41b@opal.invalid` / `PROFILE`, `firmId` `opal-capital`, `status` active, `role` user) and its read-back REFUSES a row that carries `allowedFirmIds` (line about 100). The CTO's ruling (msg 9670, relayed by `2.0.0_SA_COO~V2` msg 9705): after the combined ticket-service release, an internal caller's PROFILE row with neither `allowedFirmIds` nor the global marker is refused 403 "firm scope not configured". The reader is `_profile_scope` in `infra/aws/lambda/ticket_center/lambda_function.py` (read it, lines about 395 to 440): `allowedFirmIds` must be a LIST (DynamoDB `L`) of non-empty strings, never together with `scope_all_firms`; a string, an empty list, a NULL or a non-string member is refused 403 "firm scope malformed" or "not configured". The synthetic staff row therefore carries `allowedFirmIds` = a list holding exactly the ONE firm the run files under, `49financial`, and never `scope_all_firms`.*

Edit the ONE file `fwd1_mint.py` named above (in place; the issuer pins the new sha256 in the next addendum):

1. **The row.** Add a module constant `RUN_FIRM = "49financial"` and, in `item_for`, the attribute `"allowedFirmIds": {"L": [{"S": RUN_FIRM}]}`. Every other attribute, the key, the `exp` and the conditional write stay exactly as they are.
2. **The read-back as a pure function.** Extract the read-back test into `readback_ok(row)` (no AWS): True only when `status` is exactly `active`, `firmId` is exactly `opal-capital`, `passwordHash` is present, `allowedFirmIds` equals exactly `[{"S": "49financial"}]` (a list of one string member), and none of `mfaEnabled`, `mfaChannel`, `scope_all_firms` is present. `cmd_mint` calls it and prints, as today, ONE first line `MINT-OK READBACK-OK` (or `MINT-OK READBACK-BAD shape`); on success it then prints ONE second line `SCOPE allowedFirmIds=49financial scope_all_firms=absent mfa=absent` (the values read from the row, never the hash). Before editing, READ how `fwd1_driver.mjs` (same folder; READ only, another worker edits it) takes the mint output; if it requires the output to equal exactly `MINT-OK READBACK-OK`, file a BLOCKING surprise row naming the line and print the second line to stderr instead.
3. **Offline tests.** Write `test_fwd1_mint.py` in YOUR folder: at least 8 cases over `item_for` and `readback_ok`: the new row carries the list; the row keeps every attribute it had; a good read-back row passes; a row with no `allowedFirmIds` fails; `allowedFirmIds` with two firms fails; `allowedFirmIds` as a string `"49financial"` fails; a row with `scope_all_firms` fails; a row with `mfaEnabled` fails. It prints `MINT-TESTS-OK <n>` at the end and exits 0, otherwise `MINT-TESTS-BAD <why>`, exit 1.
4. **The item check.** Write `check_item.py` in YOUR folder: it imports `fwd1_mint` from the helper's folder, calls `item_for("x")`, and prints `ITEM-OK <n> attributes` only when the item has exactly the attributes of the base version (read the base with `git show HEAD~0:<path>` is NOT needed: list them from the base file in the task's RECORD FACE: PK, SK, email, passwordHash, status, firmId, role, userType, name, exp) PLUS `allowedFirmIds` and nothing else; otherwise `ITEM-BAD <why>`, exit 1. It prints the denominator.
5. **Record** `r43/MINT_ALLOWED_FIRM_IDS.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/`: `base` (your branch's base sha), `mint_sha256_before` (the merged helper's, which reads `04e4ba64...`), `mint_sha256_after`, `bytes_after`, `tests_output`, `driver_reads_mint_output_as` (what you read in the driver), `not_read` (any live mint; the combined release's own code live; how the pre-release authorizer reads `allowedFirmIds`, since the new code is at HEAD but the release is not yet applied).

### ACCEPTANCE

<criterion id="AR373-y-AC1" cell_refs="AR-y-373"><invocation>python C:/dev/wk-irpt-anlreq-167/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/test_fwd1_mint.py</invocation><expect>^MINT-TESTS-OK (8|9|[1-9][0-9]+)$</expect></criterion>
`AR373-y-AC1`: your offline tests pass with at least 8 cases.

<criterion id="AR373-y-AC2" cell_refs="AR-y-373"><invocation>python C:/dev/wk-irpt-anlreq-167/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/check_item.py</invocation><expect>^ITEM-OK 11 attributes$</expect></criterion>
`AR373-y-AC2`: the item has the ten base attributes plus `allowedFirmIds` and nothing else.

<criterion id="AR373-y-AC3" cell_refs="AR-y-373"><invocation>python C:/dev/wk-irpt-anlreq-167/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR373-y-AC3` (the one mutant that fails): your `mutant_check.py` copies the edited helper to a scratch folder OUTSIDE the product tree with `readback_ok` loosened to accept a row with no `allowedFirmIds`, runs your tests against the copy and prints `MUTANT-FIRES` only when the tests FAIL (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR373-y-AC4J" cell_refs="AR-y-373" judgment="true"/>
`AR373-y-AC4J` (judgment, graded at L9, never by you): the helper writes the one-firm list the ruling names and nothing wider, refuses a read-back of any other scope shape, prints the scope without the hash, leaves the removal and the password handling as signed, and the record says plainly what it did not read.

<expected_criteria>AR373-y-AC1 AR373-y-AC2 AR373-y-AC3 AR373-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/` and this order's file (status flip only). The ONE file you edit outside your folder is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py`; the driver and other workers' folders are READ only.
- READ only: everything else. NO run of the helper's `mint` or `remove`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-373</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/IRPT_ANLREQ.TO-AR-y-373.fwd1-mint-allowed-firm-ids.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-373`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR373-y-AC1,AR373-y-AC2,AR373-y-AC3,AR373-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one script file edited in a deliverable folder; nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading `_profile_scope` (lines about 395 to 440 of the ticket Lambda) and the helper against the cell; the lens: a string where the reader needs a list, two firms where the ruling names one, the global marker written, a read-back that still refuses the new attribute, the hash printed, a driver that cannot read the second output line, the removal path altered. The cell requires the one-firm list, the exact read-back, no marker, no hash in any output, and a mutant that fails. NOT seen (blind): any live mint; the pre-release authorizer's reading of the list; denominator: 1 attribute, 1 predicate, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling msg 9670 (relayed by `2.0.0_SA_COO~V2` msg 9705, the combined ticket-service release goes first). Workstream `ZZ34` of round 43. Base attributes of `item_for`: PK, SK, email, passwordHash, status, firmId, role, userType, name, exp (ten). Base: `AR373-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker or test files in this folder).
- The new helper sha256 is pinned by the window-4 addendum (a new pair, the CTO's half).
