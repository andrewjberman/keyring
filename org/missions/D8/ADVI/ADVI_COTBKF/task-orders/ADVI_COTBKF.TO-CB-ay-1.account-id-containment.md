# TO ADVI_COTBKF.TO-CB-ay-1.account-id-containment -- round 51 CB-ay-1: move evidence and redact docs that carry client account ids

<to_id>ADVI_COTBKF.TO-CB-ay-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~78</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>51</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ay-1` (`decompositions/ADVI_COTBKF_DECOMP.round51.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow may be written into any tracked file.**
The repo carries counts, sha256 and reason codes only. This applies to everything you write, including your report, your commit
messages and any surprise row.

ADVI_COTBKF's tracked files carry Cottonwood/Commonwealth client account numbers. Their shapes are 9 characters: 3 alphanumerics then
6 digits, e.g. `[A-Z0-9]{2}[A-Z]\d{6}`, `\d[A-Z]{2}\d{6}` or `[A-Z]{3}\d{6}`. The issuer's census of every file at HEAD
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACCOUNT_ID_CENSUS_HEAD_20261009.md`, @3b0dda2cb0) lists each hit
file with its class. This cell handles two classes:
- **`evidence` (80 files: JSON, CSV, TXT, LOG, parquet sidecars): MOVE.**
- **`doc` and `doc:lane` (82 `.md` files: reports, packets, task orders, decompositions): REDACT in place.**

The `channel` class (11 files) is the CVO's and is out of scope. The `code` class (6 files) is the next issuance's cell and is out of
scope.

**Your item.**

1. **MOVE each `evidence` file.**
   - Byte-copy it FIRST to `C:/dev/_cotbkf_private_evidence_20261009/<its repo path>`, outside the repo, and verify the copy's sha256.
   - Then untrack and delete it from the repo.
   - Write the path list with each sha256 to `C:/dev/_cotbkf_private_evidence_20261009/MOVED_20261009.json`, outside the repo.
   - In the repo, add ONE file per affected folder, `MOVED_ACCOUNT_DATA.md`, listing each moved file's name, sha256 and byte size only.
2. **REDACT each `doc` / `doc:lane` file in place.**
   - Replace every account-number match with `acct#<first 8 hex of sha256("cottonwood:" + account)>`. The same account always gets
     the same token, so cross-references survive.
   - Keep the token -> account key ONLY outside the repo, at `C:/dev/_cotbkf_private_evidence_20261009/TOKEN_KEY.json`.
   - Change nothing else in the files. The diff shows only token substitutions.
3. **Re-census.** Write `data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py`. It scans every tracked file under
   `org/missions/D8/ADVI/ADVI_COTBKF/` EXCEPT `surprise-channel/` (the CVO's), with the same patterns, prints the denominator, and
   expects 0 hits.
   - Commit the test ALONE first; it must fail at the base.
   - Beware false positives: CUSIPs are 9 characters too (e.g. `05613L3H2`, all-digit `464287614`). The patterns above are
     account-shaped (3 alnum + 6 digits). If a CUSIP matches, list it in the test as a named exception with its reason.
4. **Commits.** These touch other workers' deliverables folders, so commit under the audited override
   `GIT_COMMIT_AUTHOR_OVERRIDE=TREE_DELIVERABLES`, with the reason in the message. The message carries counts only.

### ACCEPTANCE

<criterion id="CB51ay1-AC1" cell_refs="CB-ay-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q</invocation><expect>passed</expect></criterion>
`CB51ay1-AC1` -- 0 account ids across every non-channel ADVI_COTBKF file at HEAD. The test alone was committed first and failed at the
base.

<criterion id="CB51ay1-AC2" cell_refs="CB-ay-1" judgment="true"/>
`CB51ay1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- every moved file was byte-copied outside the repo before it was untracked;
- each redaction diff is token substitutions only;
- the token key and the moved bytes are outside the repo.

<expected_criteria>CB51ay1-AC1,CB51ay1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `C:/dev/_cotbkf_private_evidence_20261009/` (outside the repo), plus your deliverables
  folder and this order's file.
- **Do NOT touch** `surprise-channel/` (the CVO's) or any `.py` file outside the new test. No S3 act.
- **History is not rewritten.** A purge is Andrew's act.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise
  row (id `ADVI_COTBKF-D2-W78-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken the test.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/
org/missions/D8/ADVI/ADVI_COTBKF/decompositions/
data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round51.md</decomp_doc> (round 51), cell `CB-ay-1`.
<owned_cells>CB-ay-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB51ay1-AC1, CB51ay1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~78/ADVI_COTBKF.TO-CB-ay-1.account-id-containment.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB51ay1-AC1,CB51ay1-AC2` BEFORE the flip. Mechanical: CB51ay1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT (counts only):** files moved and redacted; tokens issued; CUSIP exceptions; the test denominator; commits, with the
test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a repo-only containment act.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- byte-copy before untrack; the token key kept outside the repo; the test alone first; CUSIP false positives named; BLIND: history on origin (Andrew's purge), and the channel rows (the CVO's).
lane: the <paths> block IS the grant (worker RULING 1); TREE_DELIVERABLES override audited for other workers' folders per the CTO ruling.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` containment ruling @0e8209c33c (msg 3645); census @3b0dda2cb0.
