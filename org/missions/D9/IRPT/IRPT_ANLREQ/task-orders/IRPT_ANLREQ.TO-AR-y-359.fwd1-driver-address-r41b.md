# TO IRPT_ANLREQ.TO-AR-y-359.fwd1-driver-address-r41b -- the FWD-1 driver and mint helper take run 3's synthetic address (fwd1-staff-r41b@opal.invalid) and nothing else changes; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-359</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~156</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ20</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (two script files in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-359` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-352` (merged `e166ac9aed`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~156`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-156` (branch `wk-IRPT_ANLREQ-156`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~156 <0.9.0_WK_IRPT_ANLREQ~156@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W156-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add or edit passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, you never launch a browser and never run the driver except with `--selftest` (offline) and the mint helper only in its offline mode if it has one. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree.

### THE CELL (`AR-y-359`, inlined)

*Context. FWD-1 window 2 filed a ticket and the live intake accepted it, then the resident's packaging step refused (a registry gap, the issuer's source read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/r41/PACKAGE_REFUSAL_READ.json`). The CTO (ruling addendum 2, msg 8567) ruled that run 3 comes after the single resident release `r32`, with a NEW producer address: the issuer chose `fwd1-staff-r41b@opal.invalid` (the name is never reused; `r41a` was used in windows 1 and 2 and leaves the resident's producer list in `r32`). The driver `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs` (sha256 `d29d0afdc4d6f2be4f575aa5d6dae970b625189db1ad1248aef391fbcd45bdcc`, 21287 bytes) holds the address once (`const EMAIL = 'fwd1-staff-r41a@opal.invalid'`, about line 26) and the mint helper `fwd1_mint.py` (sha256 `2a600dcf4001bc432075b5ab2632fe9aa3005fcf656f3c72afeb6466b14a119f`) holds it once (`EMAIL = "fwd1-staff-r41a@opal.invalid"`, about line 22). The driver also carries the title `SYNTHETIC IRPT_ANLREQ FWD-1 run r41, do not action` (about line 28). Nothing else of the two files changes: the route guard stays at its eight shapes, the order-token gate and every other rule stay exactly as they are.*

1. **The change.** In `fwd1_driver.mjs` set `EMAIL` to `fwd1-staff-r41b@opal.invalid` and the title to `SYNTHETIC IRPT_ANLREQ FWD-1 run r41b, do not action`; in `fwd1_mint.py` set `EMAIL` to `fwd1-staff-r41b@opal.invalid`. Search both files for any other occurrence of `r41a` or of the first address (a name search, printed): there must be none left. Self-test cases that name the old address, if any, are re-pinned to the new one, case by case, never deleted; add ONE case that the old address `fwd1-staff-r41a@opal.invalid` is NOT the run's address (the driver refuses to mint it: the mint helper's `mint` refuses a different address on its command line if it takes one; if it takes none, assert the constant).
2. **The record.** Write `r41/ADDRESS_R41B.json` in your deliverable folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~156/`): `base` (your branch's base sha), `driver_sha256_before`, `driver_sha256_after`, `mint_sha256_before`, `mint_sha256_after`, `bytes_after` for both, `occurrences_after` (the printed search result for `r41a`: 0 for each file), `selftest_output` (the printed lines), `selftest_cases_before` (36) and `selftest_cases_after`, and `not_read` (any live run; the resident's producer list, which is the issuer's and `~G2`'s). Then write the checker scripts named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="AR359-y-AC1" cell_refs="AR-y-359"><invocation>node C:/dev/wk-irpt-anlreq-156/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK (3[7-9]|[4-9][0-9]|[1-9][0-9][0-9]) cases$</expect></criterion>
`AR359-y-AC1`: the self-test passes with at least 37 cases (36 before plus the new case).

<criterion id="AR359-y-AC2" cell_refs="AR-y-359"><invocation>python C:/dev/wk-irpt-anlreq-156/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~156/address_check.py</invocation><expect>^ADDRESS-OK </expect></criterion>
`AR359-y-AC2`: you write `address_check.py`: it reads the two amended files and the committed base (`git show <base>:<path>`) and prints `ADDRESS-OK <n> lines changed, r41a gone, r41b present` only when `r41a` occurs in neither file, `fwd1-staff-r41b@opal.invalid` occurs exactly once in each, the route guard's `POST_ALLOWED` list is byte-identical to the base's, and the diff against the base (`git diff <base> -- <both files>`) touches only the address lines, the title line and the self-test cases; otherwise `ADDRESS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR359-y-AC3" cell_refs="AR-y-359"><invocation>python C:/dev/wk-irpt-anlreq-156/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~156/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR359-y-AC3` (the one mutant that fails): you write `mutant_check.py`: it copies the amended driver to a scratch folder OUTSIDE the product tree with `EMAIL` put back to the `r41a` address, runs `node <copy> --selftest`, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR359-y-AC4J" cell_refs="AR-y-359" judgment="true"/>
`AR359-y-AC4J` (judgment, graded at L9, never by you): only the address, the title and the self-test cases changed; the guard and every gate are as signed; the record says plainly what it did not read.

<expected_criteria>AR359-y-AC1 AR359-y-AC2 AR359-y-AC3 AR359-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~156/` and this order's file (status flip only). The two files you edit are `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py`; no other file of that folder.
- READ only: everything else. NO run of the driver except `--selftest`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-359</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~156/IRPT_ANLREQ.TO-AR-y-359.fwd1-driver-address-r41b.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-359`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR359-y-AC1,AR359-y-AC2,AR359-y-AC3,AR359-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two script files edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the signed driver and addendum 2 against the cell; the lens: a guard shape changed alongside the address, an old address left in one of the two files, a self-test that never exercises the new constant, a mint of the old address still possible. The cell requires the byte-identical POST_ALLOWED, exactly one new address per file, none of the old, and a mutant that fails. NOT seen (blind): any live run and the resident's producer list; denominator: 2 files, 3 changed line classes (address, title, self-test), 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (addendum 2, msg 8567) and `~G2`'s acceptance (msg 8569) that run 3's new address rides the single resident release `r32`. Workstream `ZZ20` of round 40. Base: `AR359-y-AC1` reads `SELFTEST-OK 36 cases` (below the 37 the criterion needs), `AC2` and `AC3` FAIL as expected (no checker files).
- A third window needs a new pair addendum (the driver's sha256 changes) and the CTO's half; it opens only after `r32` reads live on the host with `r41b` on the producer list and `r41a` off it.
