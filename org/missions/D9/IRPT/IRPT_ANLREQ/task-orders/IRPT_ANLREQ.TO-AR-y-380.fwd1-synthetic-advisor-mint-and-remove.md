# TO IRPT_ANLREQ.TO-AR-y-380.fwd1-synthetic-advisor-mint-and-remove -- a small helper that mints ONE synthetic partner advisor at 49financial (a users row and a partner row) with a TTL and removes both, reading the shape of the release-33 sitting helper; offline tests with stubs, no AWS call

<to_id>IRPT_ANLREQ.TO-AR-y-380</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~172</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ41</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one new script file in a deliverable folder and its offline tests; nothing is called, minted or filed by this order)
**Decomp cell:** `AR-y-380` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (window 5) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~172`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-172` (branch `wk-IRPT_ANLREQ-172`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~172 <0.9.0_WK_IRPT_ANLREQ~172@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (a row id `IRPT_ANLREQ-D2-W172-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, no real boto3 client is ever built by your tests (they pass stubs). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.

### THE CELL (`AR-y-380`, inlined)

*Context. The door (`infra/aws/lambda/investor-reporting/_authz/served.py` `_advisor_owner`, read it with `git show HEAD:<path>`, about lines 1085 to 1104) accepts an on-behalf upload only when the named advisor email has (1) a PARTNER row at the firm (`reads.partner(email, tenant)`: a row whose `email` equals the named email and whose `firmId`, when present, equals the firm) and (2) an active USERS row at the firm (`status` exactly `active`, `email` equal, `firmId` equal). FWD-1 window 5 needs ONE such synthetic advisor at `49financial`, minted just before the run and removed after. The release-33 sitting already minted such rows: `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r33/sitting_r33.py` (record `6d46dd7c63`): address `irpt-r33-<k>-<date>@opal.invalid` (about lines 169 to 171), a users row with `status` active, `tier` advisor, `role` user, `allowedFirmIds` the explicit list of its one firm, written with `attribute_not_exists(PK)` (about lines 281 to 299), a partner row in the firm's partner table (`ptable(k)`) with `email`, `advisorKey`, `advisorName`, `advisorRole` viewer, `firmRole` user, written with `attribute_not_exists(email)` (about lines 300 to 305); the pre-state read ABSENT by ConsistentRead and the email index; after the TTL both rows are deleted with `attribute_exists` and read back ABSENT (about lines 405 to 438). The constants (`base.REGION`, `base.USERS`, `ukey`, `ptable`, `pread`, `uread`, `gsi`) are read there, not imported.*

Write ONE new file `fwd1_advisor.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/` (mirroring the shape of `fwd1_mint.py` in `0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/`: `mint` and `remove` subcommands, boto3 imported only inside the functions):

1. **The address.** `ADDRESS = "irpt-w5-advisor-%s@opal.invalid"` with the date taken from a required argument `--date YYYYMMDD` (validated `^[0-9]{8}$`); the firm is the constant `FIRM = "49financial"`. `mint --date D` and `remove --date D`.
2. **mint.** Read-only pre-state first: the users row key is ABSENT by a ConsistentRead, the email index returns 0 for the address, the partner row is ABSENT; any other state prints `ADVISOR-MINT-REFUSED prestate <what>` and writes nothing. Then ONE users row (`status` active, `firmId` `49financial`, `email`, `name` `IRPT_ANLREQ FWD-1 synthetic advisor`, `role` user, `tier` advisor, `allowedFirmIds` the list `[49financial]`, `createdAt`, `createdBy` `0.7.0_AE_CloudOps~IB2`, `updatedAt`, and `exp` = now + 3 hours as a number) written with `attribute_not_exists(PK)`, read back (active, the explicit list); then ONE partner row in the firm's partner table (`email`, `advisorKey` `irpt-w5-adv-<date>`, `advisorName` `IRPT_ANLREQ FWD-1 synthetic advisor`, `advisorRole` viewer, `firmRole` user, `createdAt`, `createdBy`, `updatedAt`) written with `attribute_not_exists(email)`, read back. Prints `ADVISOR-MINT-OK <address>` then `ADVISOR-READBACK-OK users partner`; no password and no hash exists in either row (the advisor never signs in). The users-table name, the key shape and the partner-table name are the ones in `sitting_r33.py` (read them there; if a name cannot be read there with certainty, file a BLOCKING row instead of guessing).
3. **remove.** Delete the users row (`attribute_exists`) and the partner row (`attribute_exists`); then poll a ConsistentRead and the email index for up to 300 s; print `ABSENT GSI <address>`, `ABSENT CONSISTENT <address>` and `ABSENT PARTNER <address>`; exit 1 while any is still present.
4. **Offline tests.** `test_fwd1_advisor.py` in YOUR folder, with stub clients (no boto3 import): at least 10 cases over the pure functions and the call sequences: the address is derived from the date and ends `@opal.invalid`; a bad date is refused; the users item has exactly the attributes above and the list `[49financial]`; the partner item has exactly the attributes above; the mint writes users first and partner second and each with its condition; a non-ABSENT pre-state writes nothing; the remove deletes with `attribute_exists` and prints the three ABSENT lines when the stubs read absent; the remove exits 1 when a stub still reads present at the deadline; no item holds a `passwordHash` key. Prints `ADVISOR-TESTS-OK <n>` or `ADVISOR-TESTS-BAD <why>`.
5. **Record** `r43/SYNTHETIC_ADVISOR_HELPER.json`: `helper_sha256`, `bytes`, `tests_output`, `constants_read_from` (file and line of each constant taken from `sitting_r33.py`), `not_read` (any live mint; whether the report chain accepts an advisor with no book).

### ACCEPTANCE

<criterion id="AR380-y-AC1" cell_refs="AR-y-380"><invocation>python C:/dev/wk-irpt-anlreq-172/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/test_fwd1_advisor.py</invocation><expect>^ADVISOR-TESTS-OK (1[0-9]|[2-9][0-9])$</expect></criterion>
`AR380-y-AC1`: your offline tests pass with at least 10 cases.

<criterion id="AR380-y-AC2" cell_refs="AR-y-380"><invocation>python C:/dev/wk-irpt-anlreq-172/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/check_items.py</invocation><expect>^ITEMS-OK users=13 partner=8$</expect></criterion>
`AR380-y-AC2`: your `check_items.py` imports `fwd1_advisor`, builds both items for a fixed date and prints `ITEMS-OK users=<n> partner=<m>` only when the users item has exactly the thirteen attributes (PK, SK, email, firmId, status, name, role, tier, allowedFirmIds, createdAt, createdBy, updatedAt, exp) and the partner item exactly the eight (email, advisorKey, advisorName, advisorRole, firmRole, createdAt, createdBy, updatedAt); otherwise `ITEMS-BAD <why>`, exit 1.

<criterion id="AR380-y-AC3" cell_refs="AR-y-380"><invocation>python C:/dev/wk-irpt-anlreq-172/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR380-y-AC3` (the one mutant that fails): your `mutant_check.py` copies the helper to a scratch folder OUTSIDE the product tree with the users item's `allowedFirmIds` list left out, runs your tests against the copy and prints `MUTANT-FIRES` only when they FAIL (else `MUTANT-SURVIVES`, exit 1); it also runs the unmutated copy and prints that it PASSES (positive control).

<criterion id="AR380-y-AC4J" cell_refs="AR-y-380" judgment="true"/>
`AR380-y-AC4J` (judgment, graded at L9, never by you): the helper mints exactly one synthetic advisor at 49financial that satisfies the door's two reads and nothing wider, with no password or hash anywhere, writes only with the stated conditions, removes both rows and proves them absent, takes its names from the release-33 helper rather than guessing, and the record says plainly what it did not read.

<expected_criteria>AR380-y-AC1 AR380-y-AC2 AR380-y-AC3 AR380-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/` and this order's file (status flip only). Everything else is READ only, `sitting_r33.py` and `fwd1_mint.py` above all. NO run of `mint` or `remove`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-380</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/IRPT_ANLREQ.TO-AR-y-380.fwd1-synthetic-advisor-mint-and-remove.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-380`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR380-y-AC1,AR380-y-AC2,AR380-y-AC3,AR380-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one new script file in a deliverable folder and its offline tests; nothing is called, minted or filed by this order.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading `_advisor_owner` and `sitting_r33.py` against the cell; the lens: a row with no `allowedFirmIds` list, a password or hash written, a real-domain address, a firm other than 49financial, a write without its condition, a partner row written before the users row is proven, a remove that does not prove absence, a constant guessed instead of read. The cell requires the explicit one-firm list, no credential in any item, `@opal.invalid` only, the two conditions, the three ABSENT lines and a mutant that fails. NOT seen (blind): any live mint; whether the report chain accepts an advisor with no book; denominator: 2 items, 2 subcommands, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings msgs 9890 and 9909 (window 5: the synthetic advisor, named by the real form's `Advisor login email` field). Workstream `ZZ41` of round 43. Base: `AR380-y-AC1`, `AC2` and `AC3` FAIL as expected (no test or checker files in this folder).
- The helper's sha256 is pinned by the window-5 addendum (a new pair, the CTO's half); the mint and the remove are run by the window-5 order's lane, never by this order.
