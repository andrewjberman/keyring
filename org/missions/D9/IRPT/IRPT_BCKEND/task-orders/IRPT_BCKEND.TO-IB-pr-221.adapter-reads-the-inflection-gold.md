# TO IRPT_BCKEND.TO-IB-pr-221 -- The Performance adapter reads Inflection from its holdings gold, both readers (PRD v0.19 rulings 10-12)

<to_id>IRPT_BCKEND.TO-IB-pr-221</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~74</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~P</workstream>

**AMENDMENT 1 (2026-09-29 ~08:5xZ, issuer, row S197):** slot ~73 -> ~74 before any spawn; ~Y's TO-IB-yr-221 (@52e63f09ee) also holds ~73.

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-19 ANALYSIS section 6 item 1 ("then Inflection
and Cottonwood on the holdings gold, in that order (ruling 11)"); PRD ADDENDUM v0.19 rulings 10-12, v0.20 rulings 13-17 |
**Decomp cell:** `IB-pr-221` (decomposition section 19) | **outcome_ref:** FWD-3 (INF) | **depends_on:** ~E round 3
(TO-IB-er-301, complete: INF gold for 960 accounts, 2020-04-27..2026-09-25, manifests complete)

---

## WORKER FACE

### THE CELL

`IB-pr-221` -- The 49F adapter switch is built (`holdings_gold.py`, `retained.py`, `installed.py` under
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/performance/`). Inflection is the
next firm. Its gold is at
`lib/opal_naming.address("irpt", "inflection", "gold", "holdings_performance_daily", "date=...")` (today
`s3://opal-data-inflection/irpt/inflection/gold/...`), keyed by the raw Orion `accountId` as `account_id`, with the
same columns as 49F. INF is served today through the Orion path: `retained.py`'s `_provider` -> `orion_selected`,
composed by `inf_mapping_loader`. Ruling 12 retires that read for INF in the same act; nothing runs alongside.

**Build:**
1. `holdings_gold.calculate` answers for ANY firm whose gold the caller's source reads.
   - Today it refuses everything but 49F at `holdings_gold.py:165-166`, and binds the currency with
     `bind_report_currency(tenants._CANONICAL_49F)` at `:228`. Take the firm from the verified scope and bind the
     currency for THAT firm.
   - The account mapping keeps `f49_engine.map_account`'s rule: the canonical id is `ids.opaque_account(<firm>, raw)`.
   - 49F behaviour is unchanged.
2. `RetainedPerformance` gains `holdings_sources`, a dict from canonical firm id to `HoldingsGoldSource`. The existing
   `holdings_source=` stays accepted as the 49F entry, so round 20's callers and checks keep working.
   - A firm present in `holdings_sources` is computed from its gold, on the fresh path, with the same guards as 49F:
     `implausible_engine_series` (IB-pr-214) and the separate accepted-key namespace (`accepted_key["basis"]`), so a
     pre-switch pointer at the old key is never found or reopened.
   - For INF this REPLACES the Orion path; COT is untouched.
3. `installed.py` composes `holdings_sources` for 49F and INF from the builder addresses, never typed. A registry
   refusal leaves that firm on its current path, the way `_holdings_source` does for 49F today.
4. Tests beside the existing ones in `performance/tests/`.

### ACCEPTANCE (run each from your worktree root)

<criterion id="P22-1-AC1" cell_refs="IB-pr-221"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r22/p22_1_ac1_inf_gold_fixture.py" .</invocation><expect>P22-1-AC1 PASS</expect></criterion>
`P22-1-AC1` -- in-memory gold: an INF YTD answers the chain as OPAL_HOLDINGS (arm A); 49F unchanged (arm B, control);
an uncovered INF account refuses (arm C, control). Base: FAIL (arm A refused "49 Financial holdings calculation only").

<criterion id="P22-1-AC2" cell_refs="IB-pr-221"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r22/p22_1_ac2_inf_gold_live.py" .</invocation><expect>P22-1-AC2 PASS</expect></criterion>
`P22-1-AC2` -- the seam probe against the REAL INF gold, read-only: account 998's YTD equals the independent chain of
its 180 OK days (0.057245053463) within 1e-12. Base: FAIL (refused).

<criterion id="P22-2-AC1" cell_refs="IB-pr-221"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r22/p22_2_ac1_inf_retained_switch.py" .</invocation><expect>P22-2-AC1 PASS</expect></criterion>
`P22-2-AC1` -- the RETAINED reader, through `RetainedPerformance(holdings_sources={INF: ...})`:
- a pre-switch pointer planted at the old key is never consulted, and the answer is OPAL_HOLDINGS at the chain;
- asking again reopens it with no second gold read.

Base: FAIL (`holdings_sources` does not exist).

<expected_criteria>P22-1-AC1,P22-1-AC2,P22-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.** AC2 reads S3 only. The served move (code + the adapter role's read on the INF gold +
  the INF bucket's firm fence) is the issuer's, under both never-widen halves.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken a check to pass.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/retained.py
infra/aws/lambda/investor-reporting/performance/installed.py
infra/aws/lambda/investor-reporting/performance/tests/test_holdings_gold.py
infra/aws/lambda/investor-reporting/performance/tests/test_retained_performance.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 19 (round 22, workstream ~P), cell `IB-pr-221`.
<owned_cells>IB-pr-221</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P22-1-AC1, P22-1-AC2, P22-2-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~74/IRPT_BCKEND.TO-IB-pr-221.adapter-reads-the-inflection-gold.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P22-1-AC1,P22-1-AC2,P22-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, and any surprise row id (`IRPT_BCKEND-W74-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- code only here; the adapter role's INF gold read and the INF bucket fence are the issuer's served act (census at that act).
comp-blast: RUN -- both readers of the INF served figure are in the criteria (fresh: P22-1-AC1/AC2; retained: P22-2-AC1); COT untouched; 49F guarded by arm B.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- dry-run at the base: P22-1-AC1 FAIL (arm A refused, arms B and C controls PASS); P22-1-AC2 FAIL (refused; independent chain 0.057245053463 over 180 days); P22-2-AC1 FAIL (TypeError: holdings_sources).
lane: the <paths> block IS the grant.
</preflight>
