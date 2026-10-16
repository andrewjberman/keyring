# AMGT_RESAPP task order -- `AMGT-gy-1` -- THE PRODUCER STAMPS A PASS BLOCK CLEARED AT WRITE WHEN NO HOLD APPLIES (FWD-41 ROUND 113, CTO C-1 OF THE cc02 PAIR; A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gy-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~487</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gy-1.the-producer-stamps-a-pass-block-cleared-at-write-when-no-hold-applies</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; one library function, one command-line flag and a test file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only, with a fake S3 client.
comp-adversary: RUN at the cut -- `check_gy1_stamp_at_write.py` is a prepared acceptance check (12 arms: nine for the change, three controls); at the base it reads `AIFILL GY-1 ARMS: NO (3 of 12)`, the build check failing as expected, and the issuer's reference edit in a scratch copy of lib reads `YES (12 of 12)` with the existing aifill suite at 866 passed, the same count as the base.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks; no model call; no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-487` (branch `wk-AMGT_RESAPP-487`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-487`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gy-1` (round 113, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

Every stored AI-fill block carries a `validation` dict: `{version, state, verdict, contract, checked_at}`. `state` is `HELD` or `CLEARED`. The CTO ruled what they mean (and wrote it beside `VALIDATION_STATES` in `lib/research/aifill/contract.py`): `CLEARED` = the block passed the producer's grounding contract (its `verdict` is `PASS`) and no hold applies to serving it; `HELD` = a hold applies, or the block is not validated. It is a mechanical claim, never a reader's grade.

Today `lib/research/aifill/run.py` (`main`) builds a document, checks `contract.validate_document`, and then writes it (to `--out` and/or S3 with `--to-s3 --confirm-write`) with NO `validation` key at all: the only stamping function, `lib/research/aifill/validation.py` `stamp_validation(doc, now, state="HELD")`, has no production caller. You make the producer stamp at write.

### The change (two source files and one new test file)
1. In `lib/research/aifill/validation.py` add `stamp_for_write(doc, now, hold=False)`. It returns a deep copy of the document in which every block carries the five-key `validation` dict, computed by the producer's own rule (`stamp_validation` already computes the verdict: PASS when `contract.validate_block` finds no problem on the block without its validation key, else REFUSED). A block whose verdict is PASS has `state` `CLEARED`, unless `hold` is true; a block whose verdict is REFUSED stays `HELD` with verdict `REFUSED`; with `hold=True` every block is `HELD`. It NEVER raises on a REFUSED block (unlike `stamp_validation(..., state="CLEARED")`, which keeps raising and which you do not change). The input document is never mutated. Build it on `stamp_validation(doc, now, state="HELD")` then promote the PASS blocks; do not copy its rule.
2. In `lib/research/aifill/run.py` add the flag `--hold` (`action="store_true"`, help: stamp every block HELD instead of CLEARED, a hold applies to serving). In `main`, after the document has passed `contract.validate_document` and before anything is printed or written, replace `doc` with `validation.stamp_for_write(doc, <now>, hold=args.hold)` where `<now>` is `datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)` (add the imports `datetime` and `validation`). Every later step (`_print_blocks`, the `--out` file, the S3 write) then uses the stamped document. A document that fails validation still returns 1 before it is stamped, as today.
3. Add `lib/research/aifill/tests/test_gy1_stamp_at_write.py` (pytest, no network, no model, the time passed in): at least six tests, including these named ones: `test_a_planted_pass_block_is_cleared` (a good document: every block `CLEARED` and `PASS`, the NONE block too), `test_a_planted_refused_block_stays_held` (set `doc["blocks"]["mgmt_bio"]["citations"] = []` on a good document: that block is `HELD` with verdict `REFUSED`, the other four `CLEARED`, nothing raises), `test_hold_stamps_every_block_held`, `test_the_input_is_not_mutated`, `test_run_main_writes_a_cleared_file` (run `run.main(["--key", "ASML_NA_Equity", "--inputs-file", <the fixture>, "--no-model", "--out", <tmp dir>])` and read the file back: every block `CLEARED`/`PASS`) and `test_run_main_hold_writes_a_held_file` (the same with `--hold`: every block `HELD`). Build the good document the way `lib/research/aifill/tests/test_validation.py` does (`good_doc`, `grounded_block`) and use the fixture `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/fixtures/served_inputs_ASML_NA_Equity.json` as `lib/research/aifill/tests/test_store_run.py` does (read it first).
4. Change nothing else: not `stamp_validation`, not the contract, not the grounding or block modules, not any existing test (the issuer measured that the existing aifill suite passes unchanged with the change, 866 passed). All three files stay ASCII.
5. Run the commit gate on each `.py` you touch, and commit in your worktree with `.tools/safe-commit.sh` as `worker.md` says.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W487-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Local Python in the worktree only; no AWS call, no network, no model call, no store write; no `bun install`.
2. Edit exactly the three files named in `<paths>`; the instance and the investigation file are the only other things you write. Never touch another order's files or a stored document.

## 3. SURFACES

<paths>
lib/research/aifill/validation.py
lib/research/aifill/run.py
lib/research/aifill/tests/test_gy1_stamp_at_write.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~487/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gy-1"><invocation>cd C:/dev/wk-resapp-487 &amp;&amp; PYTHONPATH=C:/dev/wk-resapp-487 timeout 110 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round113_aifill_prep/checks/check_gy1_stamp_at_write.py" "C:/dev/wk-resapp-487" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GY-1 ARMS: YES (N of N)` with N equal to 12, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gy-1"><invocation>cd C:/dev/wk-resapp-487 &amp;&amp; PYTHONPATH=C:/dev/wk-resapp-487 timeout 110 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_gy1_stamp_at_write.py | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>a pytest summary line of the form `N passed` with N at least 6 and no `failed` or `error`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~487 <0.9.0_WK_AMGT_RESAPP~487@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~487/AMGT_RESAPP.TO-AMGT-gy-1.the-producer-stamps-a-pass-block-cleared-at-write-when-no-hold-applies.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters. Model the instance's shape on an existing `*.proof_of_spec.json` under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~485/` if it is present in your worktree.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and AC2's pytest summary line;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, about 20 product lines plus tests, LOCAL; no L2, L4-R or L8-L10. Source: the CTO's C-1 of the cc02 pair (msg 6904): until this lands no new AI-fill document is stored. The close is the issuer's: the aifill suite plus `lib/research/api/tests/test_ai_fill_serve.py` at the merged head, the commit gate, the check (12 of 12), and a byte-compare of the worker's `validation.py` and `run.py` against the issuer's reference edit (saved as `gy1_reference.diff` in the session scratchpad; the issuer's reference tree is `C:/dev/scratch-gy1`). Not a store write: nothing is re-stamped here.

<status>pending</status>
<round>113</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~487</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
