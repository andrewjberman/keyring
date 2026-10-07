# TO IRPT_BCKEND.TO-IB-pr-344 -- back-fill covered_account_ids into existing export receipts from their bundles: the tool and a DRY-RUN census (PRD v0.30 item 35)

<to_id>IRPT_BCKEND.TO-IB-pr-344</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~145</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 PRIORITY msg 439, PRD v0.30 item 35, item (2) | **Decomp cell:** `IB-pr-344`
(decomposition section 58) | **outcome_ref:** FWD-2 (existing receipts stop failing open once back-filled) | **depends_on:** IB-pr-343 (same slot, the field and its derivation).

---

## WORKER FACE

**The task (PRD v0.30 item 35).** Receipts written before IB-pr-343 carry no `covered_account_ids`, so after the fix they are
REFUSED on read (correct, fail closed) until back-filled. Each receipt lives at `firms/{firm}/generations/{export_id}/receipt.json` in the
firm's evidence bucket (`infra/aws/lambda/investor-reporting/export/entry.py` :64-78, `handler.py` :144 `_keys.s3_evidence_key`), beside the bundle it was frozen from.

**What you build** (same worktree `C:/dev/wk-irpt-bckend-145`; you continue from IB-pr-343's commits):

1. `infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py` (new): for every existing receipt, read its bundle, derive `covered_account_ids` with the SAME
   function IB-pr-343 uses at freeze (import it; do not copy it), and classify the receipt FILLED (a non-empty list derived) or
   UNFILLABLE (no bundle, or the bundle names no account; it stays refused). `--dry-run` is the default and writes NOTHING; an
   `--apply` mode exists but you never run it (the apply is the issuer's, under a never-widen pair).
2. Tests `infra/aws/lambda/investor-reporting/export/tests/test_backfill_covered_account_ids.py` (new, offline, fixture receipts + bundles): filled, unfillable, and that
   dry-run writes nothing.
3. Run the dry run READ-ONLY against the real evidence buckets this box can read (the firms' registry buckets; a denied bucket is
   recorded, never widened, and filed as a row) and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~145/IB65-2_backfill_census.json`:
   `{"read": N, "filled": F, "unfillable": U, "wrote": 0, "sources": {...}, "per_firm": {...}}` with read = filled + unfillable.

<criterion id="IB65-2-AC1" cell_refs="IB-pr-344"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-2-AC1</invocation><expect>IB65-2-AC1 PASS</expect></criterion>
`IB65-2-AC1` -- the back-fill tests pass and the dry-run census reconciles read = filled + unfillable, sources named, nothing written. Base: FAIL.

<criterion id="IB65-G-145" cell_refs="IB-pr-344"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-G-145</invocation><expect>IB65-G-145 PASS</expect></criterion>
`IB65-G-145` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB65-2-AC1,IB65-G-145</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Running --apply, any S3 write, or widening a fence is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py
infra/aws/lambda/investor-reporting/export/tests/test_backfill_covered_account_ids.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~145/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-344.backfill-covered-accounts-dry-run.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 58 (round 65, workstream ~P), cell `IB-pr-344`.
<owned_cells>IB-pr-344</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB65-2-AC1, IB65-G-145. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~145/IRPT_BCKEND.TO-IB-pr-344.backfill-covered-accounts-dry-run.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB65-2-AC1,IB65-G-145` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 31b26bff2d 2026-10-07 ~11:5xZ: build checks FAIL, guards PASS (p65_cells.py).
lane: the <paths> block IS the grant.
</preflight>
