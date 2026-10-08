# TO IRPT_DASHBD.TO-DB-b-54 -- E1 (recast): is the right-half gap the advisory fee? Opal's net-basis gap against an Opal-side fee drag compounded daily; CONFIRMED iff >= 80% within 0.35 pp

<to_id>IRPT_DASHBD.TO-DB-b-54</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~32</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>superseded; IRPT_DASHBD.TO-DB-b-53.fee-census.md (re-cut in place) -- 1.0.0_SA_CTO~DELL2 ruling on row IRPT_DASHBD-S35, msg 1660 (2026-10-08 21:21Z): Opal is gross by design and the gap was the tie-out's additive add-back; worker ~32 stopped by the issuer, its branch wk-IRPT_DASHBD-32 not drained</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-29 analysis @72ae174b3c item
E1, RECAST by msg 1641 (the analysis's E1 was an identity: net gap minus BD's add-back drag IS the recorded gap, max difference 1.8e-12
over 1,527, 0 within 0.35 pp before any work) | **Decomp cell:** `DB-b-54` (decomposition section 32) | **outcome_ref:** FWD-8 |
**depends_on:** DB-b-53 (its `FEE_ROWS_E2.parquet` and census; same worker, next order).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-32`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~32/`. Do this order after DB-b-53 is complete.

**The cell (`DB-b-54`).** Opal's served return is gross of the advisory fee; BD's net return is after it. If the right-half gap is the
fee, then Opal's NET-basis gap equals the fee drag Opal itself measures from its own rows.

**Population:** the same 1,528 as DB-b-53. Use the rows of `deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json` with
`right.tied == false` AND `recompose.within == true`, each with its `right.range`.

1. Per account: `net_gap_pp = (right.opal_return - right.bd_net_return) * 100`, read from the record exactly.
2. Per account, `fee_drag_pp`: the advisory fee's drag compounded daily over the right-half window.
   - The formula is `(1 - prod_t(1 - |fee_t| / V_{t-1})) * 100`.
   - `fee_t` is the sum of that day's `FEE-MANAGEMENT` amounts from your `FEE_ROWS_E2.parquet` (FEE-ADMIN stays out: the producer keeps
     it inside the return).
   - `V_{t-1}` is the account's served `market_value_eod` on the previous served business date, from
     `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`.
   - An account with no fee rows has `fee_drag_pp = 0`. A day with no prior value is skipped and counted in `skipped_days`.
3. `residual_pp = net_gap_pp - fee_drag_pp`. Write `fee_days` (int) per row.
4. `share_within = count(|residual_pp| <= 0.35) / 1,528`. `verdict = CONFIRMED` if `share_within >= 0.80`, else `REFUTED`. The rule is
   stated in the check before the run; the verdict is printed, not graded. Also print the residual's median, p10 and p90.
5. Write `FEE_DRAG_E1.json` (`rows` [{account, net_gap_pp, fee_drag_pp, residual_pp, fee_days, skipped_days}], `share_within`,
   `verdict`, `residual_stats`, `formula`, `files_read`) and `FEE_DRAG_E1.md`, COUNTS AND STATISTICS ONLY (no account number, name or
   balance).

<criterion id="DB30-2-AC1" cell_refs="DB-b-54"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-2-AC1</invocation><expect>DB30-2-AC1 PASS</expect></criterion>
`DB30-2-AC1` -- rows cover exactly the 1,528; the net gap equals the record's; residual = net gap - fee drag on every row; drag >= 0. Base: FAIL.

<criterion id="DB30-2-AC2" cell_refs="DB-b-54"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-2-AC2</invocation><expect>DB30-2-AC2 PASS</expect></criterion>
`DB30-2-AC2` -- the share within 0.35 pp and the verdict follow the stated rule (CONFIRMED iff >= 0.80). Base: FAIL.

<expected_criteria>DB30-2-AC1,DB30-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The producer and earlier rounds' files are read, never edited.
- **AWS:** S3 reads only. No Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, a threshold other than 0.35 pp / 80%, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~32/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-54.fee-drag-test.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 32 (round 30), cell `DB-b-54`.
<owned_cells>DB-b-54</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB30-2-AC1, DB30-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~32/IRPT_DASHBD.TO-DB-b-54.fee-drag-test.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB30-2-AC1,DB30-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the share and verdict, the residual distribution, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only comparison over the landed record, DB-b-53's table and the served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB30-2-AC1 and AC2 base FAIL (no record) at base 74730695dc; positive control on a planted record PASS (1,528 rows; residual arithmetic and the 80% rule both exercised).
lane: the <paths> block IS the grant.
</preflight>
