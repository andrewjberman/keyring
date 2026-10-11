# TO ADVI_COTBKF.TO-CB-ba-1.all-shapes-resweep -- round 53 CB-ba-1: widen the account-id detector, check against the account set, and re-sweep

<to_id>ADVI_COTBKF.TO-CB-ba-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~80</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>53</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ba-1` (`decompositions/ADVI_COTBKF_DECOMP.round53.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** That includes
code, tests, fixtures, your report, commit messages and rows. Counts, sha256 and reason codes only. Never print a matched value to a
tracked file; print counts and paths.

**The problem (row D2-S75; CTO AMENDMENT 3 @4b7dcc5929).** The two id tests below match three shapes only:
- `data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py` (docs: tracked files under `org/missions/D8/ADVI/ADVI_COTBKF/`,
  minus `surprise-channel/`);
- `data/assets/scripts/silver/tests/test_cotbkf_code_no_account_ids.py` (code).

Real Cottonwood account ids also come as one letter + 8 digits, and as 11 digits. Both pass the tests today, so cleartext ids remain
in files the round-51 sweep rewrote.

**Your item.** No S3 write and no deploy.

1. **Account set, outside the repo.**
   - Read the `account` column of the served table
     `s3://opal-data-assets/commonwealth/cottonwood/silver/month_grades/date=2026-06-23/part-00000.parquet` (read-only).
   - Also read the `account` column of every local parquet under `.scratch/advi_cotbkf/` that has one.
   - Write the distinct set to `C:/dev/_cotbkf_private_evidence_20261009/account_set.json`.
   - The repo carries only its sha256 and its count.
2. **Widen both tests.** Add these shapes, with the same boundary guards as the existing three:
   - `[A-Z]\d{8}`
   - `\d{11}`
   - `z0\d{9}`
   - `cv\d{8}`

   Then add a second check to each test:
   - Every token of 6 to 12 letters and digits is checked against the account set.
   - The test reads the set from the env var `COTBKF_ACCOUNT_SET`, with the file above as the default. It FAILS (it does not skip) when
     the set is absent, and it checks the set's sha256 against a constant in the test.
   - A shape match that is not in the account set is allowed only as a named exception with its reason (e.g. a security id).
   - Commit the widened tests ALONE first. They must fail at the base.
3. **Re-sweep.**
   - In-scope tracked files (both tests' scopes): replace every id with `acct#<first 8 hex of sha256("cottonwood:" + id)>`. The key
     never enters the repo.
   - This covers `0.7.0_AE_CloudOps~CB2`'s 4 files (row D2-S75); they go by this sweep, not by hand.
   - Each diff is token substitutions only.
4. **Paths.**
   - `git mv` the 2 tracked paths whose names carry an id to the token form.
   - Make any fixture in the 2 test files that carries a real id synthetic (`SYN_ACCT_<nn>`, consistent within each test).
   - The tests stay green.
5. **Run** both tests, the silver suite (`python -m pytest data/assets/scripts/silver/tests -q`), and `python
   data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --data-dir .scratch/advi_cotbkf/r28 --out
   <scratch>` before and after your sweep. Its LAST line must be identical.

### ACCEPTANCE

<criterion id="CB53ba1-AC1" cell_refs="CB-ba-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py data/assets/scripts/silver/tests/test_cotbkf_code_no_account_ids.py -q</invocation><expect>2 passed</expect></criterion>
`CB53ba1-AC1` -- 0 hits on all seven shapes AND against the account set, in both scopes, with the denominators printed. The widened
tests alone were committed first and failed at the base.

<criterion id="CB53ba1-AC2" cell_refs="CB-ba-1" judgment="true"/>
`CB53ba1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- every redaction diff is token substitutions only;
- the SWEEP-REGRADE line is identical before and after;
- each named exception is a non-account by the account set.

<expected_criteria>CB53ba1-AC1,CB53ba1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `C:/dev/_cotbkf_private_evidence_20261009/` (outside the repo), your deliverables folder
  and this order's file.
- **Do NOT touch:**
  - `surprise-channel/` (the CVO's, append-only). Report its hit count by file; do not edit it.
  - The 7 completed task orders parked under row D2-S74 (`task-orders/` files whose `<status>` reads `complete`, other than CB-az-1 and
    CB-ay-1). Report their hit counts.
- **No S3 write.** History is not rewritten; a purge is Andrew's act.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W80-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken a test.

**AMENDMENT 1 (issuer, 2026-10-11 ~02:5xZ) -- row ADVI_COTBKF-D2-W80-S2 ruled: the grant widens to 5 completed orders; merge the trunk first.**
- Your branch was cut before the 7 parked orders landed redacted on `box/dell2` (@5cda488073, @10f554dde2). Run `git merge box/dell2`
  in your worktree FIRST, then re-run both tests and re-count. The "Do NOT touch" line on the 7 parked orders stands.
- The 5 completed orders the widened account set flags and no one had named (CB-a-2, CB-c-3, CB-c-4, CB-m-1, CB-v-1) are added to the
  `<paths>` block below. Redact them: each diff is token substitutions only, `acct#<sha8("cottonwood:"+id)>`, `<status>` untouched.
  They land through `.tools/to-pipeline-gate.py` path (b) (pure redaction of a completed order, @24bdcd2690).
- If a file outside the `<paths>` block still carries a hit after the merge, stop and report it by file and count; do not edit it.
- `CB53ba1-AC1` is unchanged: 2 pass at your branch HEAD after the merge.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/decompositions/
org/missions/D8/ADVI/ADVI_COTBKF/prd/
data/assets/scripts/silver/
data/cot/scripts/gold/tests/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-a-2.silver-transactions.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-c-3.crosswalk.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-c-4.account-links.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-m-1.one-signing-table.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-v-1.cash-leg-repair.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round53.md</decomp_doc> (round 53), cell `CB-ba-1`.
<owned_cells>CB-ba-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB53ba1-AC1, CB53ba1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~80/ADVI_COTBKF.TO-CB-ba-1.all-shapes-resweep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB53ba1-AC1,CB53ba1-AC2` BEFORE the flip. Mechanical: CB53ba1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT (counts only):**
- the pytest lines (both tests and the silver suite), with denominators;
- the account set's count and sha256;
- the tokens issued and the files redacted, by count;
- the named exceptions, with their reasons;
- the SWEEP-REGRADE line before and after;
- the hit counts left in `surprise-channel/` and in the parked orders, by file;
- commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE local docs and tests; nothing scheduled reads them.
comp-iam: DECLARED-NOT-APPLICABLE one read-only S3 get of a served table this project owns; no write.
comp-adversary: RUN -- the widened tests alone first, failing at the base; the account-set check fails closed and is sha-checked; diffs are token substitutions; the chain output is unchanged; BLIND: ids in shapes outside all seven and absent from the Cottonwood set (other firms' ids; the firm-wide list of record is 2.0.0_SA_COO~P2's).
lane: the <paths> block IS the grant (worker RULING 1); TREE_DELIVERABLES override audited for other workers' folders per the CTO ruling.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` containment AMENDMENT 3 @4b7dcc5929 (msg 3764); row D2-S75 (msg 3762); rows D2-W78-S2 and D2-S73.
