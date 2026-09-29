# TO IRPT_BCKEND.TO-IB-pr-231 -- The lambda-tree DirectoryEntry contract carries AD-10's account_masks

<to_id>IRPT_BCKEND.TO-IB-pr-231</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~79</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 2.0.0_SA_COO~M 102754/102775 (TO-IB-m22-221 release order
step 1; row IRPT_BCKEND-W75-S1) | **Decomp cell:** `IB-pr-231` (decomposition section 20) | **outcome_ref:** FWD-5
(Holdings/Directory) | **depends_on:** none

---

## WORKER FACE

**The cell.** 2.0.0_SA_COO~M's round 22 adds an OPTIONAL `account_masks` array to the Directory entry (brief item AD-10:
each account shows its own tail). ~M committed the docs contract copy
`docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` @4ecbaca410, git blob
`27d9a8f700889f2e234c267faf02d37f6d23d9a4`. That commit sits on a local branch, but the blob is in this repository's
object store.

Your one change: make
`C:/Users/AndrewBerman/Desktop/wk-irpt-p-79/infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json`
byte-equal to that blob. Write it with `git show 27d9a8f700889f2e234c267faf02d37f6d23d9a4 > <that path>` from your
worktree root, with LF line endings. Change nothing else.
- The directory runner validates its entries against this lambda-tree copy.
- The served Lambdas stage the DOCS copy at pinned commits, not this one, so nothing served moves.

<criterion id="P23-1-AC1" cell_refs="IB-pr-231"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r23/p23_1_ac1_directory_contract_masks.py" .</invocation><expect>P23-1-AC1 PASS</expect></criterion>
`P23-1-AC1` -- the file's git blob is 27d9a8f7, it defines `account_masks`, and every property of the HEAD copy is
kept. Base: FAIL (`account_masks defined: False`).

<expected_criteria>P23-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.**
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the check.

<paths>
infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 20 (round 23, workstream ~P), cell `IB-pr-231`.
<owned_cells>IB-pr-231</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P23-1-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~79/IRPT_BCKEND.TO-IB-pr-231.directory-contract-account-masks.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P23-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, and any surprise row id (`IRPT_BCKEND-W79-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo file only; 0 roles touched.
comp-blast: RUN -- source map census: irpt-directory-search and irpt-ycharts-generate stage the DOCS copy (pins 69144433df / 19d8f3038c), not _contracts; the lambda-tree copy's reader is the directory runner (and its tests), which is ~M's step 2.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P23-1-AC1 dry-run at the base: FAIL (account_masks defined: False); positive control on the blob bytes: 27d9a8f700, masks True, kept True.
lane: the <paths> block IS the grant.
</preflight>
