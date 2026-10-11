# TO ADVI_COTBKF.TO-CB-bb-1.hex-digest-false-positive -- round 54 CB-bb-1: the shape check must not match inside a sha256 digest; restore the mint manifest

<to_id>ADVI_COTBKF.TO-CB-bb-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~81</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>54</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bb-1` (`decompositions/ADVI_COTBKF_DECOMP.round54.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** That includes
code, tests, fixtures, your report, commit messages and rows. Counts, sha256 and reason codes only. Every id in a test you write is
SYNTHETIC (invented digits; never copied from a file or from the account set).

**The problem (row ADVI_COTBKF-D2-S80).** The round-53 re-sweep replaced digit runs INSIDE sha256 digests in the tracked mint manifest
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`.
- 431 hash values on 431 lines were rewritten, 440 tokens in all. Every old value was 64 lower-case hex characters. The file no longer
  works as a hash manifest.
- Cause: `data/assets/scripts/silver/tests/_cotbkf_acct_check.py` `scan_text` reports a shape match wherever the boundary guards of
  the caller allow. The guards refuse a capital or a digit on the left, so a digit run after a lower-case hex letter matches.

**Your item.** No S3 write and no deploy.

1. **Test alone first.** Add `data/assets/scripts/silver/tests/test_cotbkf_acct_check_hex.py`. It calls `scan_text` with patterns
   from `shape_patterns(r"(?<![A-Z0-9])", r"(?!\d)")` and an EMPTY account set, on synthetic strings, and asserts:
   - a run of exactly 64 characters of `[0-9a-f]` that contains an 11-digit run, with no letter or digit on either side of the run
     (for example inside JSON double quotes): 0 shape hits;
   - the same 11-digit run standing alone between spaces: 1 shape hit;
   - the same 11-digit run inside a run of 63 hex characters, and inside a run of 65: at least 1 shape hit each;
   - the same 11-digit run inside 64 hex characters where one letter is upper case: at least 1 shape hit.

   Commit this file ALONE first. The first assertion must fail at that commit; say so in the report with the pytest line.
2. **Fix, in one place.** In `scan_text`, skip a shape match whose span lies wholly inside a maximal run of EXACTLY 64 characters of
   `[0-9a-f]` that has no letter or digit immediately before or after it. Change nothing else: not `SHAPES`, not the guards, not
   `set_spans`, not the exception list of either id test.
3. **Restore the manifest.** Run `git checkout 82049024b3~1 -- "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json"`. That returns the bytes round 52 graded. Do not edit,
   re-sort or re-serialize the file.
4. **Run** the two acceptance invocations below and the silver suite (`python -m pytest data/assets/scripts/silver/tests -q`).

### ACCEPTANCE

<criterion id="CB54bb1-AC1" cell_refs="CB-bb-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_acct_check_hex.py data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py data/assets/scripts/silver/tests/test_cotbkf_code_no_account_ids.py -q</invocation><expect>passed</expect></criterion>
`CB54bb1-AC1` -- all three test files pass, 0 failed, with the denominators of the two id tests printed and 0 hits in both scopes.

<criterion id="CB54bb1-AC2" cell_refs="CB-bb-1"><invocation>python -c "import hashlib;print(hashlib.sha256(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json','rb').read()).hexdigest())"</invocation><expect>924987f6369300d530ddc9fa5793befa4c4edc291c5e83a99c5288a36811c1cb</expect></criterion>
`CB54bb1-AC2` -- the bytes of the manifest are the round-52 bytes.

<expected_criteria>CB54bb1-AC1,CB54bb1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** any other test, the exception list of either id test, `surprise-channel/` except your own NEW row, any task order
  other than this one.
- **No S3 write.** History is not rewritten.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W81-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken a test.

<paths>
data/assets/scripts/silver/tests/_cotbkf_acct_check.py
data/assets/scripts/silver/tests/test_cotbkf_acct_check_hex.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round54.md</decomp_doc> (round 54), cell `CB-bb-1`.
<owned_cells>CB-bb-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB54bb1-AC1, CB54bb1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~81/ADVI_COTBKF.TO-CB-bb-1.hex-digest-false-positive.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB54bb1-AC1,CB54bb1-AC2` BEFORE the flip. Both are mechanical.
</proof_of_spec>

**REPORT (counts only):**
- the pytest line of the test-alone commit (red), and the pytest line of CB54bb1-AC1 after the fix, with denominators;
- the silver suite line;
- the sha256 of the manifest after the restore, and its count of `acct#` tokens;
- commits, with the test-alone commit first;
- every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE local tests and one tracked manifest; nothing scheduled reads them.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the new test alone first, red at the base; the exclusion is exactly a 64-character lower-case hex run bounded on both sides, with four negative arms (standalone, 63, 65, one capital); the manifest is restored by checkout to a named blob and proven by its sha256; BLIND: an account id written as 64 lower-case hex characters (the set holds members of 6 to 12 characters only).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: row ADVI_COTBKF-D2-S80 (issuer); round 53 drain @2306e6d28a; redaction @82049024b3; round-52 manifest blob at 82049024b3~1.
