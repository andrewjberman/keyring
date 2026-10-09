# TO IRPT_DASHBD.TO-DB-b-111 -- E3: re-grade the 990 outside segments of the 49F vs Black Diamond tie-out on ONE common convention -- Black Diamond's return restated to Opal's declared conventions (fees inside the return, income on cash receipt) by a PRE-REGISTERED rule, then graded at 0.35pp; within after restatement is CONVENTION (confirmed)

<to_id>IRPT_DASHBD.TO-DB-b-111</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~86</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>55</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 20 and ADDENDUM 19 item 2, enrichment item E3 | **Decomp cell:** `DB-b-111` (decomposition section 57) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-99, DB-b-100, DB-b-101, DB-b-106 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-86`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~86/`.

**THE CLIENT-DATA RULE (binding):** evidence carrying account numbers or client figures is written OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/<your serial>/`. The repo carries counts, sha256 and reason codes only, and account tokens in the
`acct#<sha256("49financial:<account>")[:8]>` form. Never print an account number in a commit message, a record, a row or a report.

**The cell (`DB-b-111`).** The CTO ruled on W75-S1 (ADDENDUM 19 item 2): compare on ONE common convention, never across two.
- Restate Black Diamond's return to Opal's declared conventions: admin and service fees kept inside the return, and income on cash receipt.
- Grade against 0.35pp. A segment within after restatement carries `CONVENTION`, `confirmed`. A segment still outside is NOT explained by convention:
  it stays UNEXPLAINED, or DEFECT where a cause is found.
- The tolerance is never widened.

Inputs, OUTSIDE the repo:
- `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~35/TIEOUT_COMPOUND_V2.json` (the 990 outside);
- `.../~74/SENSITIVITY.json` (`final`);
- `C:/dev/_irpt_private_evidence_20261009/~75/` and `~76/` (the W73 evidence, causes per segment);
- `.../IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~81/BD_DATES_TWO_SIDED.json`.

Code may live in your repo folder; data never does.

1. **Pre-register.** Write `RESTATEMENT_RULE.md` in your repo folder: exactly how BD's figures are restated, using only both sides' own
   figures. COMMIT it alone BEFORE any run; that is `rule_commit`.
2. **Run** over the 990. A segment within 0.35pp after restatement gets `CONVENTION`. Every other segment keeps its current reason, from DB-b-99's
   final as amended by DB-b-106's confirmed/UNEXPLAINED, or becomes UNEXPLAINED.
3. **Private record:** per segment, written outside the repo at `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~86/RESTATED_TIEOUT.json`.
4. **Repo record** `RESTATED_TIEOUT.json`: {n_outside_before: 990, by_reason (summing to 990), within_after_restatement, private_record: {path,
   sha256}, preregistration: {restatement_rule_file, rule_commit, output_commit}}. Commit it LATER than the rule.

S3 GETs only if a figure must be re-read. No vendor call, no AWS write.

<criterion id="DB55-3-AC1" cell_refs="DB-b-111"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r55/p55_round55.py" . DB55-3-AC1</invocation><expect>DB55-3-AC1 PASS</expect></criterion>
`DB55-3-AC1` -- the 990 outside segments are re-graded on one restated convention by a pre-registered rule, the record holding counts only. Base: FAIL.

<expected_criteria>DB55-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you read private evidence outside the repo and write per-segment output only there; the repo gets counts and sha256.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~86/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~86/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-111.restated-tieout.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 57 (round 55), cell `DB-b-111`.
<owned_cells>DB-b-111</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB55-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~86/IRPT_DASHBD.TO-DB-b-111.restated-tieout.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB55-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the restatement rule, the per-reason counts, the CONVENTION count, the two commits, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline re-grade; nothing served moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS write.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB55-3-AC1 FAIL at base (no record). CTO ADDENDUM 19 item 2.
lane: the <paths> block IS the grant.
</preflight>
