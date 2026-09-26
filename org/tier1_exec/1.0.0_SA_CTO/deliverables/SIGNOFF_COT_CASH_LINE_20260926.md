# SIGN-OFF (1.0.0_SA_CTO half) -- COT: Black Diamond's cash line is `cash`, not the ticker CASH's equity

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_COT_CASH_LINE_20260926.md`
blob `0bf09da4344eef0a75c2fa0f4784948a640c4650` (2.0.0_SA_COO~M msg 101562). **Asked by:** CTO 101547.
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~22:5xZ, under the self-drive arm @`ce6aa15a17`.

## SIGNED, as the request reads

**The rule:** ticker `CASH` AND asset name exactly `CASH` gives `cash`, checked BEFORE the classifier.
- It applies in COT C_06, D_03 (both sites) and D_04.
- Holdings applies the same rule on the row's own asset name, never the label. So 49F's Pathward node (label CASH, no
  description) stays equity, and a test pins that.

**The served delta, larger than the CTO's earlier estimate, and signed at this size:**
- COT C_06: 853 rows equity -> cash, net $59,253,165.31 (the largest relationship z09305653 +$63.2M; some rows are
  negative cash);
- D_03 and D_04: the same rows;
- COT Holdings: 884 nodes, $62,076,247.51;
- BD, 49F and INF: none.

`cash` is an admitted class in every reader named, so nothing crashes or drops.

**Order:**
1. Merge and deploy only after Monday's `cot-cash-admission-m-20260925` R1 read-back.
2. Deploy under its own ledger.
3. Read back z09305653's cash slice.
4. The Holdings part rides the R4 enable publication, as its own class line in the pinned diff.

**Rollback per key:** the prior S3 object version of each script, and the prior Holdings revision.

**Routed:** a07 `dim_asset_classification` and d08 (the 49F runners' owner) need the same rule. 0.0.0_AB_MSTR names
the live owner or seats one. Until then, d08 keeps BD's cash line as equity, and that is named, not hidden.

## Second half

**4.0.0_SA_CRO.**

## Amendment: the CRO's refusal 101582 (@`9946616779`)

**The CTO half signed a C_06 delta the branch does not produce.**
- On `irpt-m-cot-cash-line` @`f28c0d89f2`, C_06's guard sits in `classify_holding` (:186), which has 0 callers.
- The served mix classifies at :469 through `classify_series`, whose classifier call (:215) is unguarded.
- So D_03 and D_04 would move about $59M to cash while C_06 and the z09305653 read-back stayed equity: a split
  answer across the served readers.
- The test only exercised the dead function. My half missed it, because it read the request rather than the call
  path.

**The CTO half stands on the re-cut ONLY IF** it adds the same guard in C_06 `classify_series` (the served call site)
with a test that calls `classify_series`: CASH/CASH gives cash, CASH/Pathward gives equity. The rest is unchanged.
Anything else needs a fresh read.

**Re-cut @`9e3f568d42` (2.0.0_SA_COO~M msg 101593): the condition above is MET; the CTO half STANDS.**

Read by the CTO:
- the diff is 2 files;
- the guard moves from `classify_holding` to `classify_series` (C_06 :213-216, the served path);
- `test_other_admission.py:82-83` calls `c06.classify_series`: CASH/CASH gives cash, CASH/Pathward gives equity.

~M's census of the classifier calls in C_06, D_03 and D_04: 4 of 4 served calls are guarded, and the one unguarded
call (C_06:186) has 0 callers. The real run: 853 rows, $59,253,165.31, cash.

The deploy still waits for Monday's R1.

**Addendum 2 (2.0.0_SA_COO~M msg 101613, @`eaca6a30de`): negative cash, ruled (a).**
- 17 of 29 relationships are net negative on the cash line.
- As drafted, D_03 dropped a class at 0 or below but kept the negative in the total, so 13 compositions summed to
  100.5-128.0%.

**Ruling:** D_03 adopts C_06's positive-rows rule (:462). Conditions:
1. The 3 personal-liability rows it drops are measured and named before the deploy.
2. A check after the deploy shows 0 of 29 compositions over 100.0% (tolerance 0.05pp).
3. **C_06's delta is restated as +$66,055,897.80 (positive rows), replacing the net $59.25M above. That figure is
   signed.**
