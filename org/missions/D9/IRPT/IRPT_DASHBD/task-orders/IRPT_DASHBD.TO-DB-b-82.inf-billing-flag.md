# TO IRPT_DASHBD.TO-DB-b-82 -- E3: a readable billed/unbilled flag for Inflection's fee slices where a source exists -- round 37 read Orion's Asset.IncludedInBilling, unreadable for 526 of 562 sample accounts (W53-S2); find a source that reads more, or show by search that none does

<to_id>IRPT_DASHBD.TO-DB-b-82</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~59</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-38 ADDENDUM 7 (on ADJUDICATION_v23 @ab9ad6b27a), enrichment item E3 | **Decomp cell:** `DB-b-82` (decomposition section 41) | **outcome_ref:** FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-59`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~59/`.

**The cell (`DB-b-82`).** Inflection's billed/unbilled fee slices are PARTIAL at 36 of 562 sample accounts
(`deliverables/0.9.0_WK_IRPT_DASHBD~58/INF_FEE_SLICES_R38.json`). Orion's `Asset.IncludedInBilling` reads `"Error:Not supported"` for 526 of
them, and 2,882 of 3,129 database-wide (row D2-W53-S2; `data/inf/manual_api/PATH_DISCOVERY.md:158`). The CTO's ADDENDUM 7 item 3 asks for a
readable billing flag where a source exists.

1. **Search landed sources first** (S3 reads only; the Orion token expired 2026-10-09T07:02Z, row W57-S1):
   - `silver/api_dims/billing/` (built by `data/inf/scripts/silver/build_billing_dim.py` from `data/inf/manual_api/orion_billing_dim.py`'s
     pulls);
   - the `Billing.*` paths at `PATH_DISCOVERY.md:160-175`, where a non-zero `Billing.FeeAmount` or a `FeeScheduleName` for the account and
     window marks it billed;
   - the fee-classification home `data/inf/scripts/gold/lib/fee_classification.py` (its custody-ledger basis).

   Record every place searched as `searched` [{where, result}].
2. **Choose the source** that reads a billed/unbilled state for the most of the 562 sample accounts (round 37's sample, in
   `deliverables/0.9.0_WK_IRPT_DASHBD~53/`). Record:
   - `source`;
   - `denominator` (562);
   - `readable`;
   - `baseline_readable` (36);
   - `gained` (`readable - 36`).

   If nothing reads more than 36, say so: `source` names the best and `gained` is 0.
3. **Re-derive the slices** `billed`, `unbilled` and `billing_total` from round 37's fee figures (Activity, `activityOptionId` 11) under the
   chosen flag, each as {value, readable, denominator, status}, with status PARTIAL iff readable < denominator.

Record `INF_BILLING_FLAG.json`. Use hashed account keys only.

<criterion id="DB39-1-AC1" cell_refs="DB-b-82"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r39/p39_round39.py" . DB39-1-AC1</invocation><expect>DB39-1-AC1 PASS</expect></criterion>
`DB39-1-AC1` -- the billing-flag source named with every place searched and its readable count against the 36 baseline. Base: FAIL.

<criterion id="DB39-1-AC2" cell_refs="DB-b-82"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r39/p39_round39.py" . DB39-1-AC2</invocation><expect>DB39-1-AC2 PASS</expect></criterion>
`DB39-1-AC2` -- billed, unbilled and billing_total re-derived under that flag with readable-of-denominator and a status by rule. Base: FAIL.

<expected_criteria>DB39-1-AC1,DB39-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~59/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-82.inf-billing-flag.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 41 (round 39), cell `DB-b-82`.
<owned_cells>DB-b-82</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB39-1-AC1, DB39-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~59/IRPT_DASHBD.TO-DB-b-82.inf-billing-flag.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB39-1-AC1,DB39-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the source, readable of 562, what was searched, the three slices, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: offline records in the worker folder; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB39-1-AC1/AC2 FAIL at base (no record). Row D2-W53-S2; CTO ADDENDUM 7 item 3.
lane: the <paths> block IS the grant.
</preflight>
