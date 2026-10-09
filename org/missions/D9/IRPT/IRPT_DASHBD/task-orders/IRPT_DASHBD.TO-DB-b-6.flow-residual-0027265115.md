# TO IRPT_DASHBD.TO-DB-b-6 -- Name the leg behind the [redacted] USD flow residual on acct#89d0916a from the landed responses (read cell, direct act)

<to_id>IRPT_DASHBD.TO-DB-b-6</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-1 analysis @57304c750b item E3; PRD v0.6 @aabc054e89 ruling 25 |
**Decomp cell:** `DB-b-6` (decomposition section 2) | **outcome_ref:** FWD-8 (enrichment) | **depends_on:** none

---

## WORKER FACE

**The cell.** A READ: on 49 Financial account `acct#89d0916a`, the external flow Opal's gold carries on a day the tie-out could not
reconcile leaves a [redacted] USD residual after the fee leg, which matches to the cent (PRD v0.6 ruling 25). Name the leg that makes
the residual -- one of: an IN-KIND leg valued differently by the two sides (`IN_KIND_VALUED_DIFFERENTLY`), a leg Opal classes
INTERNAL and Black Diamond classes EXTERNAL or the reverse (`INTERNAL_HERE_EXTERNAL_AT_VENDOR`), or `OTHER` with the reason -- from
data ALREADY LANDED. **No vendor call of any kind** (Black Diamond, Schwab or any other API): reads of landed S3 objects only.

**What is known, and how firmly.**
- MEASURED (tie-out record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/tieout/TIEOUT_49F_BLACKDIAMOND_R1.json`,
  `periods[]` for `acct#89d0916a`): `2026-07-07` carries a flow of `[redacted]`, withheld as `FLOW_UNRECONCILED / NOT_GRADED_OUTSIDE_DOMAIN`;
  `2026-03-16` carries `133980.54` (`NOT_MEASURABLE / GUARD_NOT_REACHED`) and `2026-03-27` carries `462984.11`
  (`FLOW_UNRECONCILED / GRADED_DISAGREED`).
- INFERRED by the issuer, NOT measured: the residual is on `2026-07-07` (2,423.40 - [redacted] = 925.02 would be the fee leg). Confirm
  or refute this FIRST from the landed rows; if the residual sits on another day, follow the data and say so in the record.

**Where the landed data is (read only).**
- Schwab silver, declared in `data/assets/scripts/gold/irpt_reporting/sources.json` (entry `schwab_08335338`): bucket
  `opal-data-assets`, prefixes `schwab/08335338/silver/fact_trn/`, `schwab/08335338/silver/dim_position/`,
  `schwab/08335338/silver/dim_balance/`, partitions `date=YYYY-MM-DD/`, account column `account_id` (zero-padded to 10).
- The Schwab transaction-code classes, as DATA: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`;
  how the adapter turns them into `external_flow`: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (read, never edit).
- Opal's served day: gold `account_return_daily` at `lib.opal_naming.address("irpt","49financial","gold","account_return_daily","date=<D>")`
  + `/data.parquet` (columns per `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`: `external_flow`, `fee_amount`,
  `fee_amount_reason`, `day_quality`, ...).
- Black Diamond landed responses: `s3://opal-data-assets/blackdiamond/49f/bronze/` (the tie-out read `reporting_performance/<pull
  date>/reporting_performance_acct#57de9fb9_<period end>.json`, pull dates 2026-07-17, 08-30, 08-31, 09-01; Black Diamond relationship
  `acct#57de9fb9` maps to `acct#89d0916a` in `blackdiamond/49f/_ops/taxsma_roster.json`). List the bronze prefix for any other landed family
  that carries per-transaction or per-day flow detail for that relationship and window; use only what is there.

**What you write.** ONE record, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/FLOW_RESIDUAL_acct#89d0916a_R2.json`:
`{"account": "acct#89d0916a", "flow_date": "<YYYY-MM-DD>", "opal_external_flow_usd": <n>, "fee_leg_usd": <n>, "residual_usd": <n>,
"legs": [{"source": "schwab|blackdiamond|opal_gold", "key": "s3://<bucket>/<key>", "row_ref": "<row or field identity>",
"amount_usd": <n>, "class_opal": "<class or null>", "class_vendor": "<class or null>", "is_residual": true|false}, ...],
"leg_named": "IN_KIND_VALUED_DIFFERENTLY|INTERNAL_HERE_EXTERNAL_AT_VENDOR|OTHER", "leg_explanation": "<two or three sentences>",
"vendor_calls": 0, "measured_at": "<UTC>"}`. Every leg cites the landed object it was read from. The legs flagged `is_residual` sum to
the residual. Plus a one-page `FLOW_RESIDUAL_acct#89d0916a_R2.md` beside it in plain English for the CTO's next ruling.

<criterion id="DB-6-AC1" cell_refs="DB-b-6"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r2/p2_6_ac1_flow_residual_record.py" .</invocation><expect>DB-6-AC1 PASS</expect></criterion>
`DB-6-AC1` -- the record exists for `acct#89d0916a` with `vendor_calls` 0; `residual_usd` is [redacted] within 0.01; `leg_named` is one of the
closed set with an explanation; the `is_residual` legs sum to it; every cited `s3://` key exists. Base: FAIL (no record).

<expected_criteria>DB-6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS:** reads only (`s3 ls`, `get-object`, `head-object`). NO write to any bucket, no Lambda invoke, no vendor call.
- **Refusal clause.** If the landed data cannot place the residual (a leg is not in any landed object), say exactly which object
  family would hold it and stop: that is a row (`IRPT_DASHBD-W1-S<k>`), never a vendor pull and never an estimate.

<paths>
data/assets/scripts/gold/irpt_reporting/
org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/tieout/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `lib/opal_naming.py` and `infra/logic/registry/` (the builder resolving the gold address).

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 2 (round 2, workstream B), cell `DB-b-6`.
<owned_cells>DB-b-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-6-AC1. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-6.flow-residual-acct#89d0916a.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the flow date, the leg named in one sentence, and any
surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a read cell; no schedule, trigger or cron is created or moved.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: reads under the worker's existing session; no role or policy is created or changed.
comp-blast: RUN -- 0 written keys outside the worker's deliverables folder; 0 readers move.
comp-routes: DECLARED-NOT-APPLICABLE -- no route in this cell.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-6-AC1 base FAIL (no record), dry-run at the base 2026-10-02 ~05:0xZ: "FAIL: no record ... DB-6-AC1 FAIL", rc 1.
lane: the <paths> block IS the grant.
</preflight>
