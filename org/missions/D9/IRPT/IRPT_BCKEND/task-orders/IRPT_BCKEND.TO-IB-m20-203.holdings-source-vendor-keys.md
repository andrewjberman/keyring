# TO IRPT_BCKEND.TO-IB-m20-203 -- Holdings snapshots name their own source vendors (UIC-14)

<to_id>IRPT_BCKEND.TO-IB-m20-203</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~44</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-203`
(`decompositions/IRPT_BCKEND_DECOMP_R20_M.md`) | **outcome_ref:** FWD-5 (UIC-14) | **depends_on:** IB-mr-202 (same file)

---

## WORKER FACE

### THE CELL

`IB-mr-203` -- the CTO ruled UIC-14 (msg 102443): "the Holdings builder writes each snapshot's source vendor keys
(registry vendor keys) into its output, so the portal turns keys into words and no function-name map exists". The
portal side (2.0.0_SA_COO~D) was parked because producer names embed firm tokens and a hand-typed map is refused by
the LGIC naming gate (read `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md`, Parked, UIC-14). Vendor keys come from the
LGIC registry read through `lib/opal_naming.py` (`lookup()`); start from `infra/logic/registry/systems.json` and name
the registry file you used. Never type a vendor key or a firm id (the naming gate, CLAUDE.md rule 30).

**Build (on top of IB-mr-202's change, same worktree):**
1. In `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, each firm's snapshot gains one output field
   carrying the source vendor keys of the data it read (49F: its custodian and model-platform systems; INF: its
   Eclipse/Orion systems; COT: Black Diamond) -- derived from the registry by the sources the build actually opened,
   not from a per-firm constant. Extend the contract schema only if it rejects the field.
2. Tests: add `data/assets/scripts/gold/investor_reporting/tests/test_vendor_keys.py` asserting the field is present,
   non-empty, drawn from the registry, and that an unknown source is refused rather than labelled. Run the suite and
   report its summary line (the `lib.silver_ids` 7F/7E are pre-existing, row W42-S3).
3. Real local builds, no upload, for all three firms; write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_UIC14_VENDOR_KEYS_SUMMARY_20260929.json`:
   `{"registry_source": "<file>", "registry_vendor_keys": [...], "firms": [{"firm", "vendor_keys": [...],
   "output_field": "<json path>"}]}`.
4. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_VENDOR_KEYS_20260929.md`
   (`## The act`, `## Blast radius` with the local candidate diff -- one added field per snapshot, nothing else moves --
   and `Rollback per key`). It may reference IB-mr-202's half; the two ride one re-mint when both are signed.
5. Do NOT re-mint, upload, publish or merge.

### AMENDMENT 1 (2026-09-29 ~03:0xZ, issuer 2.0.0_SA_COO~M, on IB-mr-202's drain read and row W44-S1)

Two repairs ride this cell, batched (same file family, same worktree):
- **R1 -- keep the COT strategy assignment.** IB-mr-202 removed the MODEL_WRAPPER node and with it the only place the
  account's assigned Rebalancer strategy lived (`model_id` {namespace COT_REBALANCER_MODEL, value}, and its name); the
  old assertion on it in `tests/test_holdings_membership.py` went with the node. Put the assignment back as a FIELD on
  the COT ACCOUNT node (never a node): `assigned_strategy: {model_id: {...}, name: ...}` when membership assigns one,
  absent otherwise; extend the contract schema only if it rejects the field; assert it in `test_holdings_membership.py`
  (z091 carries m-lt, z092 carries none).
- **R2 -- re-point the S71 re-arm trigger (row W44-S1).** `tests/test_holdings_rearm_trigger.py` guards the directory
  bundle `investor_reporting` (`investor-reporting.tar.gz`), but the enabled schedule runs the three standalone packages
  the dispatch names in `IRPT_HOLDINGS_BUNDLE_MAP` (read live 03:0xZ: `s3://opal-data-<firm>/irpt/<firm>/code/gold/
  investor-reporting-holdings.tar.gz`, members-sha256 94f2e3433d9e, 41 members, the bundles `irpt_holdings_{49f,inf,cot}`
  in `.tools/safe_deploy_core.py`). Re-point the guard at those three (read the key from the guard's declaration, never
  typed); keep its verdict (FAIL when the schedule is ENABLED while a served package lacks a file the runner opens) and
  its SKIP-is-not-a-pass rule. Run it live: it must PASS now. Record the old and new targets in row W44-S1's resolution.

### ACCEPTANCE

<criterion id="IBM20-203-AC1" cell_refs="IB-mr-203"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_vendor_keys.py -q -p no:cacheprovider</invocation><expect>a summary line with N passed and no failed or error</expect></criterion>
`IBM20-203-AC1` -- the built behaviour, including the refusal of an unknown source.

<criterion id="IBM20-203-AC2" cell_refs="IB-mr-203"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_m203_vendor_keys.py</invocation><expect>VENDOR-KEYED followed by 49financial, inflection and cottonwood each with its registry vendor keys</expect></criterion>
`IBM20-203-AC2` -- every firm's real local candidate carries registry vendor keys.

<criterion id="IBM20-203-AC3" cell_refs="IB-mr-203"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_VENDOR_KEYS_20260929.md</invocation><expect>HALF-READY NEVER_WIDEN_HALF_REQUEST_HOLDINGS_VENDOR_KEYS_20260929.md</expect></criterion>
`IBM20-203-AC3` -- the half request is written for the issuer to sign and send.

<criterion id="IBM20-203-AC4" cell_refs="IB-mr-203"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_rearm_trigger.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_membership.py -q -p no:cacheprovider</invocation><expect>a summary line with N passed and no failed, error or skipped</expect></criterion>
`IBM20-203-AC4` -- the batched repairs R1 and R2 (a fourth criterion: the round's repairs ride this one cell, per the
spine's "repairs batched into ONE cell").

<expected_criteria>IBM20-203-AC1,IBM20-203-AC2,IBM20-203-AC3,IBM20-203-AC4</expected_criteria>

Dry-run at the base 2026-09-29 01:0xZ: AC1 "no tests ran", AC2 NOT-KEYED, AC3 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no served write, no Terraform. `holdings_snapshot.py` is a directory
  bundle member (MSTR skips that bundle at push).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W44-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_UIC14_VENDOR_KEYS_SUMMARY_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_VENDOR_KEYS_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R20_M.md</decomp_doc> (round 20, workstream ~M), cell `IB-mr-203`.
<owned_cells>IB-mr-203</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM20-203-AC1, IBM20-203-AC2, IBM20-203-AC3, IBM20-203-AC4. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~44/IRPT_BCKEND.TO-IB-m20-203.holdings-source-vendor-keys.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM20-203-AC1,IBM20-203-AC2,IBM20-203-AC3,IBM20-203-AC4` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the field and its JSON path, the registry file, each firm's keys, the pytest lines,
the half's path, commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger change.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change.
comp-adversary: RUN -- comp-find vendor_key|"vendors" over infra/logic/registry, lib and data/firm_registry.json: 0 hits across 347 files, and infra/logic/registry holds 7 files; BLIND: the file that carries the vendor keys is not confirmed at the cut (systems.json is the lead; the worker names it); the check requires every key to sit in that registry list, so a typed or function-named key fails.
lane: the <paths> block IS the grant; ~M owns the gold holdings snapshot.
</preflight>

Source: `STATUS~M.md` @dc913869d8 next-list item 4; CTO rulings 102443 (UIC-14) and 102516.
