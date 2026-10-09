# TO IRPT_DASHBD.TO-DB-b-83 -- E2: Inflection's fee slices re-printed with the basis each figure rests on -- per account 'measured' where Orion's IncludedInBilling is readable (Orion wins), else 'inferred: from fee amount and schedule'; supervision slices state inferred (CTO RULING W53-S2)

<to_id>IRPT_DASHBD.TO-DB-b-83</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~60</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-39 ADDENDUM 8 (CVO slug msg 2951; RULING W53-S2), enrichment item E2 | **Decomp cell:** `DB-b-83` (decomposition section 42) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-82 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-60`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~60/`.

**The cell (`DB-b-83`).** The CTO ACCEPTED the inferred billing flag (ADDENDUM 8, ruling W53-S2) on one condition: a consumer must show its
basis (the value-carries-its-claim law, `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md`). The inputs:
- `deliverables/0.9.0_WK_IRPT_DASHBD~59/INF_BILLING_FLAG.json`: the billing state for 562 of 562 sample accounts, inferred from the landed
  `silver/api_dims/billing` fee amount and schedule;
- `deliverables/0.9.0_WK_IRPT_DASHBD~53/`: Orion's `IncludedInBilling`, readable for 36 of 562 (the live read of round 37);
- `deliverables/0.9.0_WK_IRPT_DASHBD~58/INF_FEE_SLICES_R38.json`: the supervision slices, from an inferred managed flag.

1. **Per-account billed state.** Where Orion's `IncludedInBilling` is readable for an account, that value wins and the account's basis is
   `measured`. Otherwise use the inferred state, with basis `inferred: from fee amount and schedule`. Count `orion_overrides`: accounts where
   Orion's value differs from the inferred one.
2. **Re-print all six slices** (`supervised`, `unsupervised`, `supervision_total`, `billed`, `unbilled`, `billing_total`), each as {value,
   readable, denominator, status (PARTIAL iff readable < denominator), basis}.
   - `billed` and `unbilled` also carry `basis_counts` {measured, inferred}, summing to the denominator, and a `basis` string naming both
     parts (for example "36 measured (Orion IncludedInBilling); 526 inferred: from fee amount and schedule").
   - The supervision slices' basis states `inferred` (Orion has no supervised field; the managed flag is used).

Record `INF_FEE_SLICES_R40.json`. Use hashed account keys only.

<criterion id="DB40-1-AC1" cell_refs="DB-b-83"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r40/p40_round40.py" . DB40-1-AC1</invocation><expect>DB40-1-AC1 PASS</expect></criterion>
`DB40-1-AC1` -- billed and unbilled carry measured/inferred basis counts summing to the denominator, a basis string stating both, and the Orion override count. Base: FAIL.

<criterion id="DB40-1-AC2" cell_refs="DB-b-83"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r40/p40_round40.py" . DB40-1-AC2</invocation><expect>DB40-1-AC2 PASS</expect></criterion>
`DB40-1-AC2` -- the supervision slices state an inferred basis, and all six slices carry their status by rule. Base: FAIL.

<expected_criteria>DB40-1-AC1,DB40-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~60/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-83.fee-slice-basis.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 42 (round 40), cell `DB-b-83`.
<owned_cells>DB-b-83</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB40-1-AC1, DB40-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~60/IRPT_DASHBD.TO-DB-b-83.fee-slice-basis.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB40-1-AC1,DB40-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the basis counts, the override count, the six slices with basis, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: offline records in the worker folder; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB40-1-AC1/AC2 FAIL at base (no record). CTO ADDENDUM 8, ruling W53-S2.
lane: the <paths> block IS the grant.
</preflight>
