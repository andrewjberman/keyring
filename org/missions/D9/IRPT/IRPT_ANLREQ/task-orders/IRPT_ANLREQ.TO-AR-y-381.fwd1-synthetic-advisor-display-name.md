# TO IRPT_ANLREQ.TO-AR-y-381.fwd1-synthetic-advisor-display-name -- the synthetic advisor helper's display name reads exactly SYNTHETIC TEST ADVISOR (users row name and partner row advisorName), with one new offline test; offline, no AWS call

<to_id>IRPT_ANLREQ.TO-AR-y-381</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~173</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ42</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one constant in a deliverable script and its offline tests; nothing is called, minted or filed)
**Decomp cell:** `AR-y-381` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (window 5) | **depends_on:** `AR-y-380` (merged: `fwd1_advisor.py` with 18 offline tests, sha256 `cc8b8bd5f120f3e54bb73b9c82d97ba390207a65e95e769ddf1a2e1706906a34`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~173`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-173` (branch `wk-IRPT_ANLREQ-173`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~173 <0.9.0_WK_IRPT_ANLREQ~173@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (a row id `IRPT_ANLREQ-D2-W173-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). The workspace worktree shows ` M portal`: never commit it. Every `.py` you edit passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, no real boto3 client. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.

### THE CELL (`AR-y-381`, inlined)

*Context. The CTO signed addendum 5 (FWD-1 window 5) with the condition (msg 10001, item 2) that the synthetic partner row's display name reads `SYNTHETIC TEST ADVISOR`, so that no 49financial partner-facing list could mistake it for a real advisor. In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/fwd1_advisor.py` the display name is the constant `NAME = "IRPT_ANLREQ FWD-1 synthetic advisor"` (line about 52), used for the users row `name` (about line 110) and the partner row `advisorName` (about line 126).*

1. **The constant.** Change `NAME` to exactly `SYNTHETIC TEST ADVISOR` (ASCII, upper case) and its comment line; change nothing else in `fwd1_advisor.py` (the address `irpt-w5-advisor-<date>@opal.invalid`, the attribute sets, the conditions and the remove path stay byte-for-byte as they are).
2. **The tests.** In `test_fwd1_advisor.py` (same folder) update any case that pins the old display name, and ADD one case named `the display name of both rows reads SYNTHETIC TEST ADVISOR` asserting that the users item `name` and the partner item `advisorName` equal that string; the file prints `ADVISOR-TESTS-OK <n>` with n at least 19. `check_items.py` still prints `ITEMS-OK users=13 partner=8`; `mutant_check.py` still prints `MUTANT-FIRES` (and its positive control passes).
3. **Record** `r43/ADVISOR_DISPLAY_NAME.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/`: `helper_sha256_before` (reads `cc8b8bd5...`), `helper_sha256_after`, `bytes_after`, `tests_output`, `diff_summary` (the lines that changed, by number), `not_read` (any live mint).

### ACCEPTANCE

<criterion id="AR381-y-AC1" cell_refs="AR-y-381"><invocation>python C:/dev/wk-irpt-anlreq-173/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/test_fwd1_advisor.py</invocation><expect>^ADVISOR-TESTS-OK (19|[2-9][0-9])$</expect></criterion>
`AR381-y-AC1`: the offline tests pass with at least 19 cases (the merged 18 plus the new name case).

<criterion id="AR381-y-AC2" cell_refs="AR-y-381"><invocation>python C:/dev/wk-irpt-anlreq-173/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/name_check.py</invocation><expect>^NAME-OK </expect></criterion>
`AR381-y-AC2`: you write `name_check.py` in your folder: it imports `fwd1_advisor` from the `~172` folder, builds both items for a fixed date, and prints `NAME-OK users.name=<v> partner.advisorName=<v> other attributes unchanged (<n> of <n>)` only when both names equal `SYNTHETIC TEST ADVISOR` and the other attributes of both items equal those of the merged version (compare against the file at `git show HEAD:<path>` taken before your edit, applied to the same fixed date); otherwise `NAME-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR381-y-AC3" cell_refs="AR-y-381"><invocation>python C:/dev/wk-irpt-anlreq-173/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR381-y-AC3`: the existing `mutant_check.py` still prints `MUTANT-FIRES` (the unmutated copy passes, the copy without `allowedFirmIds` fails).

<criterion id="AR381-y-AC4J" cell_refs="AR-y-381" judgment="true"/>
`AR381-y-AC4J` (judgment, graded at L9, never by you): only the display name changed, to exactly the CTO's string, in both rows; nothing else in the helper moved; the record says plainly what it did not read.

<expected_criteria>AR381-y-AC1 AR381-y-AC2 AR381-y-AC3 AR381-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/` and this order's file (status flip only). The files you edit outside your folder are `fwd1_advisor.py` and `test_fwd1_advisor.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/`.
- READ only: everything else. NO run of `mint` or `remove`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/fwd1_advisor.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/test_fwd1_advisor.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-381</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/IRPT_ANLREQ.TO-AR-y-381.fwd1-synthetic-advisor-display-name.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-381`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR381-y-AC1,AR381-y-AC2,AR381-y-AC3,AR381-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one constant in a deliverable script and its offline tests; nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the helper's items and the CTO's condition against the cell; the lens: a wrong or mixed-case string, only one of the two rows renamed, another attribute changed alongside, a test that pins the old name left in place. The cell requires the exact string in both rows, no other attribute changed, one new test and a still-firing mutant. NOT seen (blind): any live mint; denominator: 1 constant, 2 rows, 3 checks, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's condition (2) of the addendum 5 signature, msg 10001. Workstream `ZZ42` of round 43. Base: `AR381-y-AC1` reads `ADVISOR-TESTS-OK 18` (below the 19 needed); `AC2` FAILS as expected (`name_check.py` absent); `AC3` PASSES at base (the existing mutant check) and is a control.
- The new helper sha256 is pinned by an amendment to addendum 5 (the CTO's half).
