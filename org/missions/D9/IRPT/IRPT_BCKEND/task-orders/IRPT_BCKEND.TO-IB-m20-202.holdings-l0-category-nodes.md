# TO IRPT_BCKEND.TO-IB-m20-202 -- Holdings L0 CATEGORY nodes (Models / SMAs / Client) per account, producer-served

<to_id>IRPT_BCKEND.TO-IB-m20-202</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~44</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-202`
(`decompositions/IRPT_BCKEND_DECOMP_R20_M.md`) | **outcome_ref:** FWD-5 (AD-01/02) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-202` -- the portal's Holdings card (AD-01, owner 2.0.0_SA_COO~D) drills L-1 accounts -> L0 Models / SMAs /
Client -> L1 contents, and the CTO ruled (msg 102475) that the PRODUCER serves every total: "one L0 node per account
per category (Models, SMAs, Client) carrying its own amount, and the L-1 account total ... the page never sums". Today
`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` builds, per account:
- COT: ACCOUNT -> L1 MODEL_WRAPPER (the Rebalancer strategy, `holdings_snapshot.py:1810`, built near :1920) -> L2
  MODEL_LEAF / SLEEVE Client (the plug) -> L3 SECURITY (read the docstring at :1800-1830 whole);
- 49F and INF: read the builders (`holdings_49f.py`, `holdings_inf.py`) and state their current account subtree in the
  profile of your change.
Each MODEL_LEAF already carries a `hierarchy_path` from the MDPF registry rule ("Models > Primary", "Models > Custom",
"SMA"); the Client sleeve is the plug.

**Build:** a shape change only -- no amount, classification or membership rule moves.
1. Under every ACCOUNT, emit one CATEGORY node per category present, named exactly `Models`, `SMAs` or `Client`, each
   carrying the sum of its children's amounts; the leaves attach under their category by `hierarchy_path` first segment
   (Models > ... -> Models; SMA -> SMAs; the Client sleeve and anything else -> Client). The ACCOUNT keeps its total.
2. Remove COT's MODEL_WRAPPER strategy node; its children attach to the category nodes. The strategy name, if kept,
   is a field on the account, never a node.
3. Keep the contract valid: extend `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` with the new
   node kind only if it rejects one (read it first), and keep the difference control (`redistribute_holdouts`) passing.
4. Tests: add `data/assets/scripts/gold/investor_reporting/tests/test_l0_categories.py` -- fixtures for all three firm
   shapes asserting ACCOUNT -> CATEGORY-only children, L0 sum == account total, no MODEL_WRAPPER, and leaf amounts
   unchanged. Run the investor_reporting suite and report its summary line (7 failed / 7 errors on `lib.silver_ids`
   are pre-existing at CLOUD, row W42-S3; report any other).
5. Real local builds, no upload: for each firm run `holdings_snapshot.run_firm(<firm>, s3, qa=True, upload=False,
   local_out=<scratch>)` before and after the change and write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_L0_SHAPE_SUMMARY_20260929.json`:
   `{"firms": [{"firm", "accounts", "accounts_with_non_category_child", "accounts_l0_sum_mismatch",
   "model_wrapper_nodes", "category_names", "security_amount_total_before", "security_amount_total_after",
   "candidate_sha256"}]}`.
6. Write the never-widen half request (COO half to be signed by the issuer; CTO half owed)
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md`:
   `## The act` (re-mint the three Holdings packages from the merged code under a ledger; the next scheduled
   publication serves the new shape), `## Blast radius` (the served node shape per firm, from your local candidate diff:
   nodes added / removed by kind, amounts unchanged, the consumer 2.0.0_SA_COO~D's AD-01 card and any other reader of
   node_kind -- census them), and `Rollback per key` (re-put the prior package versions; repoint the served index).
7. Do NOT re-mint, upload, publish or merge. The schedule is live after IB-mr-201, so a re-mint moves the served
   publication; that act waits for the half's signatures and ~D.

### ACCEPTANCE

<criterion id="IBM20-202-AC1" cell_refs="IB-mr-202"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_l0_categories.py -q -p no:cacheprovider</invocation><expect>a summary line with N passed and no failed or error</expect></criterion>
`IBM20-202-AC1` -- the built behaviour on fixtures of all three firm shapes.

<criterion id="IBM20-202-AC2" cell_refs="IB-mr-202"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_m202_l0_shape.py</invocation><expect>L0-SHAPED followed by 49financial, inflection and cottonwood each with its account count</expect></criterion>
`IBM20-202-AC2` -- the shape holds on a real local build at every firm, with no dollars created or lost.

<criterion id="IBM20-202-AC3" cell_refs="IB-mr-202"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md</invocation><expect>HALF-READY NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md</expect></criterion>
`IBM20-202-AC3` -- the half request is written for the issuer to sign and send.

<expected_criteria>IBM20-202-AC1,IBM20-202-AC2,IBM20-202-AC3</expected_criteria>

Dry-run at the base 2026-09-29 01:0xZ: AC1 "no tests ran" (file absent), AC2 NOT-SHAPED (summary absent), AC3
NOT-READY (half absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** Real local builds read S3 (read-only). No upload, no mint, no served write, no Terraform.
  `holdings_snapshot.py` is a member of the directory bundle `investor-reporting.tar.gz` (MSTR skips it at push).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W44-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_L0_SHAPE_SUMMARY_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R20_M.md</decomp_doc> (round 20, workstream ~M), cell `IB-mr-202`.
<owned_cells>IB-mr-202</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM20-202-AC1, IBM20-202-AC2, IBM20-202-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~44/IRPT_BCKEND.TO-IB-m20-202.holdings-l0-category-nodes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM20-202-AC1,IBM20-202-AC2,IBM20-202-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the change (files, node kinds added/removed), each firm's before/after subtree, the
summary JSON's counts, the pytest lines, the half's path, commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger change; the served move is a later act under the half.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; local builds read with the operator's credentials, no writes.
comp-adversary: RUN -- 1 file read at the cut (holdings_snapshot.py:1800-1830, the COT tree docstring, and the MODEL_WRAPPER sites :717, :1810, :1920); BLIND: holdings_49f.py and holdings_inf.py account subtrees were not read (the cell states them); the check compares security-amount totals before and after on real builds, so a shape change that creates or loses dollars cannot pass.
lane: the <paths> block IS the grant; ~M owns the gold holdings snapshot (contract writer table).
</preflight>

Source: `STATUS~M.md` @dc913869d8 next-list item 3; CTO rulings 102475 (AD-01/02) and 102516.
