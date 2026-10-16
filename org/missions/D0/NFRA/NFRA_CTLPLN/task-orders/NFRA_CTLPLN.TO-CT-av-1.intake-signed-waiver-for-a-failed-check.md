# TO NFRA_CTLPLN.TO-CT-av-1 -- workstream OUTCOME round 24 (cell CT-av-1): the organic journey, step 4b -- a failed check 3-7 may be carried to release only by a named, reasoned WAIVE line in the CTO's signed check-8 file; check 6 records when it compared across platforms (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-av-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~134</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-av-1` (`decompositions/NFRA_CTLPLN_DECOMP.round27.md`, amendment 5) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** CT-au-1 (blocked at the release of four wheels; this cell removes that block)

---

## WORKER FACE

### THE CELL

The organic journey of dell2's `yfinance==1.2.0` Linux closure. 13 of the 17 wheels are released. Four (curl_cffi, numpy, pandas, websockets) are refused because their check 6 reads FAILED (their `.py` files differ from the laptop's WINDOWS-installed copy) and `intake_check.compute_verdict` (line 826) returns `not_checked` unless every one of checks 1-7 is `passed` or `not_applicable` with a reason: the CTO's signed check 8 cannot carry a failed check. The CTO read every differing file (after CRLF normalisation only the Windows-only delvewheel blocks and numpy's build metadata remain) and RULED a signature waiver: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INTAKE_SIGNED_WAIVER_FOR_A_FAILED_CHECK_20261016.md` (read it whole: its terms 1-5 are this cell). This cell changes the tools; the four lines and the release of the four wheels come AFTER it merges (the CTO adds the lines; a later cell releases). Read first: `org/devices/intake/intake_check.py` (`check_6`, `check_8` lines ~765-825, `compute_verdict` ~826, the release verdict re-derivation ~938-945, the released-only pack rule ~1012), `org/devices/intake/intake_receive.py` (line ~185 record verdict test and `verify`), and both existing test files.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. The CTO's ruling is under `org/tier1_exec/1.0.0_SA_CTO/deliverables/`: add that folder.

### BUILD

1. **The waiver line, in `check_8`.** After the signature file passes its existing rules (under the signer directory, names the batch and THE FILE, carries the CHECK 8 SIGNED marker), parse its lines for the exact form `WAIVE <file name> check <N>: <reason>` (after the same leading markdown-emphasis stripping `has_sign_marker` uses; case-sensitive `WAIVE`; one file name and one check number per line; no wildcard, no batch-wide form; `<reason>` must be non-empty after stripping). Keep only the lines whose `<file name>` equals THIS file's name exactly. Record them in check 8's evidence as `waivers: [{"check": N, "reason": "..."}]` (empty list when none). A waiver line naming check 1 or check 2 for this file is REFUSED: check 8 reads `failed` with a summary that says the check cannot be waived (digest and identity are never waivable); a waiver naming check 8 or a number outside 1-7 is ignored and listed in `ignored_waivers`.
2. **`compute_verdict`.** A failed check N of 3-7 is accepted only when check 8 passed with a signer and path AND its evidence carries a waiver for exactly N with a non-empty reason. A failed check 1 or 2 is never accepted. The overall verdict is `checked` when no waiver was needed, `released-with-waiver` when at least one failed check was carried by a waiver (the record also carries `waived_checks: [N,...]`), and `not_checked` otherwise. The record KEEPS the failed check's own verdict `failed` and its evidence: nothing is edited or rewritten to look passed.
3. **Everything that reads the verdict accepts exactly those two values.** `release` (the re-derivation near line 938), the released-only pack rule (near line 1012) and every other reader in `intake_check.py` accept `checked` or `released-with-waiver` (re-derived by `compute_verdict`, never trusted from the field alone). In `intake_receive.py` the record test near line 185 accepts `checked` or `released-with-waiver`, and `verify` prints one extra line per waived wheel BEFORE its last line: `INTAKE-VERIFY-WAIVED <file> check <N>: <reason>`; the existing `INTAKE-VERIFY pack=... wheels=.. verified=.. checked=.. stray=.. ok=..` last line keeps its exact format (a waived wheel counts in `checked`). Anything else (`not_checked`, a missing waiver, a field that disagrees with the re-derivation) is still refused. List in your report every place you changed and every place that reads the verdict and needed no change.
4. **Check 6 records why it can fail, not gating.** When the installed copy's own WHEEL `Tag:` platform differs from the held wheel's platform tag, check 6's evidence records `compared_across_platforms: true` (and the two platform strings); beside its raw count of differing `.py` files it records `differ_after_crlf_normalisation` (the count after replacing CRLF with LF on both sides before comparing). The verdict of check 6 does NOT change.
5. **The existing check suite is RED at the base and you fix its stale case.** `python org/devices/intake/test_intake_check.py` reads `INTAKE-CHECK-TEST cases=56/57 skipped=0 ok=False` today: `case_check_8_signature_rules` asserts (line ~648) that a signature file that does NOT EXIST reads check 8 `failed`, but the tool since an earlier cell (CT-am-2, row W119-S1) reads it as `awaiting` (a recorded state of its own, never a failed check). Update THAT assertion to the tool's intended behaviour (`awaiting`) and nothing else in that case, and file one OBSERVATION row saying the suite was red at the base and why. Change no other existing case.
6. **Tests.** A NEW test `.tools/tests/test_round27_waiver.py` (standard library plus the two tools; synthetic wheels and a temporary signer directory only, as `test_intake_check.py` builds them; no network; ASCII output) with the CTO's five arms: (a) an unwaived failed check 6 still refuses release; (b) a waiver for a different file, or for a different check, does not carry; (c) a waiver line in a file with no CHECK 8 SIGNED marker does not carry; (d) a waiver of check 1 or of check 2 is refused (check 8 fails); (e) with the four-style lines present (a synthetic failed check 6 and a matching `WAIVE <file> check 6: <reason>` line in a signed file) the file RELEASES and its record reads `released-with-waiver` with `waived_checks: [6]` while check 6 still reads `failed`; plus (f) the pack of that released file verifies in `intake_receive.py verify` with its last line `checked=1 ok=True` and the `INTAKE-VERIFY-WAIVED` line printed, and a pack whose record is `not_checked` is still refused; (g) check 6 across platforms: a synthetic installed copy tagged win_amd64 against a manylinux wheel records `compared_across_platforms: true` and the post-CRLF count (a CRLF-only difference reads raw differ 1, post-CRLF 0). Add control arms that fail the suite if a waiver ever carries a failed check 1, 2 or 8. Last line `WAIVER arms=<k>/<n> ok=<True|False>`.
7. Add to `test_intake_check.py` and `test_intake_receive.py` only the cases for the new behaviour (their counts grow) and the one stale-assertion fix of step 5.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. NO network request of any kind, no `pip`, no install; do NOT run `release`, `pack` or `check` against the real batch `intake-20261016-yfinance-linux` or move any file under `C:/opal-intake/`: the real release of the four wheels is a later cell, after the CTO adds his four lines. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~132/NFRA_CTLPLN.TO-CT-at-1.yfinance-linux-fetch-and-checks-one-to-seven.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W134-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTav1-AC1" cell_refs="CT-av-1"><invocation>python .tools/tests/test_round27_waiver.py</invocation><expect>ok=True</expect></criterion>
`CTav1-AC1` -- a named, reasoned WAIVE line carries a failed check 3-7 to release, an unnamed or misdirected one never does, checks 1 and 2 are never waivable, and check 6 records the cross-platform comparison (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTav1-AC2" cell_refs="CT-av-1"><invocation>python org/devices/intake/test_intake_check.py</invocation><expect>ok=True</expect></criterion>
`CTav1-AC2` -- the check tool's own suite passes, its one stale case fixed (base: `INTAKE-CHECK-TEST cases=56/57 skipped=0 ok=False`, a red base); report the whole last line.

<criterion id="CTav1-AC3" cell_refs="CT-av-1"><invocation>python org/devices/intake/test_intake_receive.py</invocation><expect>ok=True</expect></criterion>
`CTav1-AC3` -- the receiving tool's suite passes with the waived-wheel cases added (base: `INTAKE-RECEIVE-TEST cases=34/34 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTav1-AC1,CTav1-AC2,CTav1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTav1-AC1,CTav1-AC2,CTav1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round27.md</decomp_doc>
<owned_cells>CT-av-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_check.py
org/devices/intake/test_intake_check.py
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_receive.py
.tools/tests/test_round27_waiver.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; synthetic wheels in temporary folders.
comp-adversary: RUN -- a waiver widening into a general pass (arms a-d and the controls: an unnamed failure, a wrong file, a wrong check, no marker, checks 1, 2 and 8 all still refuse); a waiver hiding the failure (the record keeps check 6 `failed` and its evidence, the verdict string differs, `waived_checks` names it, `verify` prints the waived line); the receiving tool refusing a released-with-waiver pack on dell2 (arm f; dell2 gets the tool only through box-sync, so the issuer states in the packet that dell2's `verify` needs this change if the manager runs it); a wildcard or batch-wide waiver (the face allows one file and one check per line); the tool trusting the verdict field alone (release re-derives with `compute_verdict`, as it does today); the real batch's records edited or the real release folder touched (forbidden by the face: the real release is a later cell); BLIND: a waiver is the CTO's judgment written in a text file, so the tool can check its form and its name match, not whether the reason is true; the CTO's four lines do not exist yet.
risk: LOCAL -- changes to the intake check and receive tools and their tests against synthetic wheels in temporary folders; no real file is released, moved or sent.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE); the CTO ruled the design (`CTO_RULING_INTAKE_SIGNED_WAIVER_FOR_A_FAILED_CHECK_20261016.md` @a71c144be8, msg 109650).
</preflight>

Base checks, dry-run by the issuer before the cut: CTav1-AC1 FAIL as expected (the test does not exist, rc=2); CTav1-AC2 FAIL at the base (`INTAKE-CHECK-TEST cases=56/57 skipped=0 ok=False`: the stale `case_check_8_signature_rules` assertion at line ~648; the cell fixes it); CTav1-AC3 PASS as expected (control: `INTAKE-RECEIVE-TEST cases=34/34 ok=True`).
Source: CTO ruling @a71c144be8 terms 1-5; worker row `NFRA_CTLPLN-W133-S2`; FWD-15, FWD-16.
