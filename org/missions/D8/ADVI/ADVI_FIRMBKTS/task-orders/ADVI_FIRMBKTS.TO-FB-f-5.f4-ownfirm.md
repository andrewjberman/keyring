# ADVI_FIRMBKTS task order -- `FB-f-5` -- F4'S OWN-FIRM ADMIT, EXERCISED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~15</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- the same SSM route as round 2 (user -> ssm:SendCommand on i-0167fd745ad906a66 -> the runner's profile assumes irpt-cot-ycharts-research-role): the issuer's own dry run read Status Success, command 0e7afa57-7961-4575-b7cd-becebda020da; the role's policy carries s3:GetObject on irpt/cottonwood/state/ycharts_runs/* and ycharts_responses/*. No grant, role or policy is created.
comp-adversary: RUN by the issuer -- r3_f4.py ownfirm 0 of 4 at base (evidence absent), 4 of 4 on the dry-run record. Blindness: the lens cannot see the fence's behavior for a principal this cell does not assume; the cell exercises one own-firm role, one ungranted own-firm key and one foreign bucket.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-5` (round 3, enrichment item 5; row D1-W7-S1; PRD F4)

Round 2 showed that a `*-cot-*` role is REFUSED by the fence on `opal-data-inflection`, and that the same role's read of
`opal-data-cottonwood` was refused by an identity-side implicit deny, so the fence's ADMIT of its own firm was shown only
by policy text. The CTO's ruling: the admit must be EXERCISED. One read must SUCCEED through the fence, as a named act
printed with the principal's ARN. You make it, with the issuer's sender.

The sender `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f4_send.py` sends ONE SSM
command to the runner `i-0167fd745ad906a66`. The command assumes `irpt-cot-ycharts-research-role` and makes three
read-only calls, each printed with its result or its error text: `OWN` a `GetObject` (ContentLength only) of
`irpt/cottonwood/state/ycharts_runs/index=latest/latest_by_portfolio.json` in `opal-data-cottonwood`; `OUT` a `GetObject`
of a key the role's identity policy does not grant, same bucket; `INF` a `ListObjectsV2` (MaxKeys 1) on
`opal-data-inflection`. It prints no credential and writes nothing.

### 1a. The steps

0. Work in `/c/dev/wk-firmbkts-15`. Begin every shell call with `cd /c/dev/wk-firmbkts-15 &&`.
1. Print the command first: `python <sender> --print` (sends nothing). Read it. If it names anything other than the
   instance, role, buckets and keys above, STOP: a BLOCKING row.
2. Send once: `python <sender> --out "$D/F4_OWNFIRM_EVIDENCE.json" --wait 100`, where
   `D=org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~15`. If the status is not Success, or
   `ssm:SendCommand` is refused, STOP: a BLOCKING row naming the refusal text (never retry around it, never assume another
   role). If the command is still running, `--collect <command id> --out <same file>` fetches it without a second send.
3. Run AC1 and AC2 (section 4).
4. If AC1 fails on arm O3 because the OWN read was refused, that is a FINDING against F4's serving grants, not a pass:
   file it as a row, and report the exact refusal text.

## 2. BOUNDS

1. The only AWS acts are the sender's SSM command (read-only on the runner) and `describe`/`get` reads by the grader.
   No write, delete, policy edit, role creation or configuration change; no second send.
2. Never edit the sender or the grader. Never print or save a credential.
3. Only the files in section 3 change. No non-ASCII; LF line endings.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~15/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the issuer's checks under `deliverables/2.0.0_SA_COO~B1/round3/checks/` and `round2/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~15/ADVI_FIRMBKTS.TO-FB-f-5.f4-ownfirm.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-5"><invocation>cd /c/dev/wk-firmbkts-15 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f4.py --arms ownfirm --evidence org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~15/F4_OWNFIRM_EVIDENCE.json; echo "exit=$?"</invocation><expect>ROUND 3 F4 OWNFIRM: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-5"><invocation>cd /c/dev/wk-firmbkts-15 &amp;&amp; timeout 90 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f4.py --arms positive; echo "exit=$?"</invocation><expect>ROUND 2 F4 POSITIVE: 3 of 3 arms</expect></criterion>
</proof_of_spec>

AC1 is the exercised read through the fence with its two difference controls. AC2 is the standing positive arm, run live
beside it (a control that passes at base by construction).

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-5.f4-ownfirm.proof_of_spec.json`, `D` as above. **Flip this order's `<status>` to
`complete` in the SAME commit as your proof instance and the evidence file**, only when AC1 and AC2 pass. A row id on this
project carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W15-S<k>`, `surfaced_at` from `date -u +%FT%TZ`. Report
once: the command id, the caller ARN, the four result lines (`OWN`, `OUT`, `INF` in full), the output of AC1 and AC2, and
the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the issuer's dry run at the cut is L5 evidence (L5_FACTS section 3), not the order's; this order's
evidence file is the record the CVO grades. `OWN` reads a 431-byte pointer object under the role's `ycharts_runs/`
prefix (its body is never printed). If the evidence reads a different `OWN` key's byte count, the sender was edited:
refuse the instance.

<status>complete</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-5</to_id>
<slot>~15</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
