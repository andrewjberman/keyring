# TO IRPT_DASHBD.TO-DB-b-81 -- E4: Inflection's six fee slices re-printed with readable-of-denominator and a COMPLETE/PARTIAL status, so no slice is shown complete where the source cannot read it (W53-S2, CTO Decision 3)

<to_id>IRPT_DASHBD.TO-DB-b-81</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~58</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-37 ADDENDUM 6 @fb5579ddfc (on ADJUDICATION_v22 @153e101791), enrichment item E4 | **Decomp cell:** `DB-b-81` (decomposition section 40) | **outcome_ref:** FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-58`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~58/`.

**The cell (`DB-b-81`).** Round 37's fee slices (`deliverables/0.9.0_WK_IRPT_DASHBD~53/INF_GROSS_FEE_TIEOUT.json`, row D2-W53-S2):
- supervised/unsupervised came from the account-level managed flag in `silver/api_dims/accounts_v2`, an inference; 68 accounts are missing
  from that snapshot;
- billed/unbilled cover only 36 accounts, because `Asset.IncludedInBilling` is unreadable for 526 of 562.

The CTO ruled (Decision 3) that a slice is never shown as complete.

1. Re-derive the six slices (`supervised`, `unsupervised`, `supervision_total`, `billed`, `unbilled`, `billing_total`) from round 37's inputs,
   copied into your folder. Each slice is {value, readable, denominator, status}, where `readable` is the accounts whose flag the source
   could read and `denominator` is the sample's accounts.
2. `status` is "PARTIAL" if readable < denominator, else "COMPLETE".
3. For each PARTIAL slice, write a one-line `statement` naming readable of denominator and why (for example "billed: 36 of 562 accounts --
   IncludedInBilling unreadable for 526").

Record `INF_FEE_SLICES_R38.json`.

<criterion id="DB38-4-AC1" cell_refs="DB-b-81"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-4-AC1</invocation><expect>DB38-4-AC1 PASS</expect></criterion>
`DB38-4-AC1` -- six slices, each with value, readable, denominator, and a status that follows the rule. Base: FAIL.

<criterion id="DB38-4-AC2" cell_refs="DB-b-81"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-4-AC2</invocation><expect>DB38-4-AC2 PASS</expect></criterion>
`DB38-4-AC2` -- every PARTIAL slice stated with readable of denominator. Base: FAIL.

<expected_criteria>DB38-4-AC1,DB38-4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~58/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-81.fee-slices-partial.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 40 (round 38), cell `DB-b-81`.
<owned_cells>DB-b-81</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB38-4-AC1, DB38-4-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~58/IRPT_DASHBD.TO-DB-b-81.fee-slices-partial.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB38-4-AC1,DB38-4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the six slices with status, and the statements, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: offline records and code in the worker folder; nothing served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB38-4-AC1/AC2 FAIL at base (no record). Row D2-W53-S2; CTO ADDENDUM 6 Decision 3.
lane: the <paths> block IS the grant.
</preflight>
