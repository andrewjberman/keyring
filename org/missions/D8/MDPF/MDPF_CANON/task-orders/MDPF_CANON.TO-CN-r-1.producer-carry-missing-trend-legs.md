# MDPF_CANON task order -- `CN-r-1` -- THE GLOBAL TREND GROUPS CARRY A MISSING DIVIDEND, GROWTH OR SMA-ADDITIVE LEG AT ITS LAST KNOWN VALUE WHERE THE SERVED TOTAL STILL PARTITIONS (PRODUCER; FWD-9)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~29</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell changes how one existing function fills a gap in a field the scheduled run already writes.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read, no new key; the code reads the same Global fields (it now also reads the existing `model_aua`) and the same SMArtX partition as CN-p-1. No IAM change is made.
comp-adversary: RUN by the issuer on DELL1 at box/dell1 -- r10_cn_r_1.py pure 6 of 11 (M0, P0 controls; R2, R5, R7, R9 guards the base already meets), seams 2 of 4 (S0, S3 controls), oracle 10 of 11 (only the planted-gap arm O9 is red) at base; a scratch reference tree reads 11 of 11, 4 of 4, 11 of 11 (the arms can pass) and CN-p-1's own `r9_cn_p_1.py oracle` reads 7 of 7 on it; ten planted defects (no carry, carry before the first value, the Global All Equity TR leg carried, the carried date not recorded, the memory reset at the 2026-05-18 boundary, the input mutated, an UNCONDITIONAL carry, a refused leg recorded as carried, a row with no model_aua carried, all legs of a row decided together) each turn the named arm red; `r10_cn_r_1.py selftest` prints `CN-R-1 SELFTEST: OK`.
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-r-1` (round 10)

**The rule (PRD v2.22, overrides (c) and (d); you do not need to read it).** `compute_trend_groups(g, smartx)` in the gold consolidator builds three group arrays for the portal's Global AUA Trend. Today, on a row that has a total, a Dividend, Growth or `sma_additive_aua` value that is MISSING (None or NaN) reads as zero, so the groups dip by the whole leg on that day. The rule changes to ONE statement: **on a total-bearing row, a missing leg carries its last known value ONLY IF the carried row still partitions the SERVED Total**, i.e. `total - model_aua - (Client Supervised + ETF + ALT) - gaetr` is within `TREND_IDENTITY_TOL` (0.011), where `gaetr` is the row's Global All Equity TR allowance (the SMArtX leg on a date before 2026-05-18, else 0.0). The Total is READ, never recomposed. Where the Total does not contain the leg the leg stays ABSENT (reads 0.0, as today): that is the truth of the served Total. Each leg is decided ALONE on its row (the other legs of the row at their own value, or 0.0 when absent).

- **Forward only**: a leg that has never had a value contributes 0.0 and is never carried. A value of 0.0 is a value, not a gap.
- **The date joins `carried_dates` ONLY when a leg actually carried.** A refused leg adds no date.
- **A row with no `model_aua` cannot be shown to partition: nothing carries (fail closed).**
- One memory per leg runs across the 2026-05-18 boundary. A pre-boundary date with no SMArtX row is skipped as today. The Global All Equity TR leg (`gaetr`) is NEVER carried (a missing one reads 0.0).
- Why the test is per leg and mostly bites the sleeve: Dividend and Growth cancel between Client Supervised (`- div - growth`) and ETF (`+ div + growth`), so the partition test passes for them whenever the sleeve is right (the rule guards the future); the sleeve (`sma_additive_aua`) is what the test decides. On the served 2026-10-14 object the 7 dated rows 2026-08-31..2026-09-09 have no sleeve in the Total, so the sleeve stays absent there and nothing in the served output changes today.
- Nothing else moves: rows with no total keep today's group-level roll-forward; ALT is unchanged; no key is added; no existing key moves.

**The code (statement-level edits, in this order). File: `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (CRLF: keep its line endings; use the Edit tool).** The checks grade BEHAVIOUR by calling `compute_trend_groups` and the three helpers, so a different but equivalent body is acceptable; the names, signatures and return shapes are the contract.

1. Directly BELOW the line `SMARTX_LOOKBACK_DAYS = 10` add:

```
# MDPF_CANON CN-r-1 (PRD v2.22, override (c) and (d)): the legs whose MISSING value on a total-bearing row carries the
# leg's last known value ONLY IF the carried row still partitions the served Total (forward only, never before the
# leg's first value). The Global All Equity TR leg is a terminated SMArtX-only model and is not in this tuple.
TREND_CARRY_LEGS = ("div", "growth", "sma")
TREND_IDENTITY_TOL = 0.011   # the readback's IDENTITY_TOL: three 2-decimal roundings
```

2. Directly ABOVE `def compute_trend_groups(` add these three functions (copy them):

```
def _leg_present(x) -> bool:
    """A leg value is PRESENT when it is a number (0.0 is a value); None and NaN are absence."""
    return x is not None and x == x


def _partitions(row: dict, key: str, cand: float) -> bool:
    """True when the row, with leg `key` at `cand` and every other leg at its own value (0.0 when absent), still partitions the
    SERVED Total (PRD override (d)): total - model_aua - (Client Supervised + ETF + ALT) - the Global All Equity TR allowance
    is within TREND_IDENTITY_TOL. The Total is read, never recomposed. A row with no model_aua cannot be shown to partition."""
    if row["model"] is None:
        return False
    v = dict(row["vals"])
    v[key] = cand
    cs = round(row["nm"] - v["div"] - v["growth"] - row["gaetr"], 2)
    etf = round(v["div"] + v["growth"] + v["sma"], 2)
    alt = 0.0 if row["tax"] is None else round(row["tax"], 2)
    return abs(row["total"] - row["model"] - cs - etf - alt - row["gaetr"]) <= TREND_IDENTITY_TOL


def _leg_carry(last: dict, key: str, raw, row: dict) -> tuple:
    """(value, carried). The leg's own value when present (and it becomes the leg's last known value); else, for a leg named in
    TREND_CARRY_LEGS that has had a value, its last known value ONLY IF the carried row still partitions the served Total
    (carried=True); else 0.0 (absent: the leg has never had a value, or the Total does not contain it)."""
    if _leg_present(raw):
        last[key] = float(raw)
        return float(raw), False
    if key in TREND_CARRY_LEGS and key in last and _partitions(row, key, last[key]):
        return last[key], True
    return 0.0, False
```

3. Inside `compute_trend_groups` change exactly these statements and no others (the docstring gains the sentence "A Dividend, Growth or sma_additive_aua leg that is missing on a TOTAL-BEARING row carries its last known value when the carried row still partitions the served Total (CN-r-1; PRD override (c) and (d)); the date joins carried_dates only when a leg actually carried. The Global All Equity TR leg is never carried."):
   - Directly BELOW the `total, nm = ...` line add `model = _col(g.get("model_aua"))`.
   - Directly BELOW `raw = {k: [None] * n for k in TREND_GROUP_KEYS}` add `last: dict = {}` and `leg_carried: set = set()`.
   - Replace the whole `if d < TREND_SMARTX_UNTIL:` / `else:` block (the two `div, growth, gaetr = ...` assignments) with:

```
        if d < TREND_SMARTX_UNTIL:
            leg = smartx.get(d)
            if leg is None:
                continue
            legs_raw = {"div": leg.get("div"), "growth": leg.get("growth"), "sma": sma[i]}
            gaetr = leg.get("gaetr") if _leg_present(leg.get("gaetr")) else 0.0
        else:
            legs_raw = {"div": div_g[i], "growth": growth_g[i], "sma": sma[i]}
            gaetr = 0.0
        row = {"total": total[i], "model": model[i], "nm": nm[i], "tax": tax[i], "gaetr": gaetr,
               "vals": {k: (float(v) if _leg_present(v) else 0.0) for k, v in legs_raw.items()}}
        got = {k: _leg_carry(last, k, v, row) for k, v in legs_raw.items()}
        div, growth, sma_v = (got[k][0] for k in ("div", "growth", "sma"))
        if any(c for _, c in got.values()):
            leg_carried.add(d)
```

   - `raw["etf_strategies_aua"][i] = round(div + growth + (sma[i] or 0.0), 2)` becomes `round(div + growth + sma_v, 2)`. The client-supervised and ALT lines do not change.
   - `carried: set = set()` becomes `carried: set = set(leg_carried)`. In the group roll-forward loop rename the local `last` to `last_v` (it would shadow the new dict). Nothing else in the function changes.

4. Tests: in `data/mdpf/tests/canon/test_global_trend_groups.py` keep all eight existing tests unedited and ADD at least five (synthetic data, `copy.deepcopy` the input and assert it unchanged): (a) a planted gap in each leg on a post-boundary fixture where the Total contains it (model_aua = total - non_model - the sleeve) - Client Supervised constant, ETF constant after the sleeve's first value, `carried_dates` exactly the gap dates; (b) the sleeve missing on rows where the Total EXCLUDES it (model_aua = total - non_model) stays absent and those dates are NOT in `carried_dates`; (c) a row where Dividend AND the sleeve are both missing, the Total containing the Dividend and excluding the sleeve: Dividend carries, the sleeve does not; (d) a leg is never carried before its first value; (e) the memory crosses 2026-05-18, `gaetr` missing reads 0.0 and is not carried, and a fixture with no `model_aua` carries nothing.

The issuer's check `round10/checks/r10_cn_r_1.py` (read it; never edit it) holds the exact fixtures `FIX_R`, `FIX_X`, `FIX_M`, `FIX_N`, `FIX_S`, `FIX_Z` and the expected arrays your tests may reuse.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no `safe-deploy`. Read-only `get`/`list`/`describe` is allowed (criterion AC3 reads one served Global object, one 49 Financial object and one SMArtX partition). No install, no push. REFUSE, do not rescue. The deploy of this code is CloudOps's, in its own window, after a never-widen pair; none of it is yours.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Everything else is read-only; in particular `apply_global_trend_groups`, `load_smartx_sma_legs`, `build_all`, the registry rows and `lib/`.
3. **No existing key moves.** Do not change any key name, `point_class`, `opal_aggregate_aua`, `by_model`, `model_aua`, any existing `meta` key, or `R2_RULED_EXTRAS`. Do not carry `gaetr`. Do not carry across a row with no total (the group-level roll-forward already handles those). Do not recompose the Total or `model_aua`: they are read.
4. **CLIENT DATA:** never print an account id or a firm level (print dates, counts and differences). No non-ASCII in any text you add. Keep each file's line endings as you find them (read them first). Use the Edit tool.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/tests/canon/test_global_trend_groups.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-r-1.producer-carry-missing-trend-legs.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~29/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/` (`r10_cn_r_1.py`) and `round9/checks/r9_cn_p_1.py` (its `pure`, `seams` and `oracle` modes must all stay 7 of 7).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_1.py" pure; echo "exit=$?"</invocation><expect>CN-R-1 PURE: 11 of 11 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_1.py" seams; echo "exit=$?"</invocation><expect>CN-R-1 SEAMS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_1.py" oracle; echo "exit=$?"</invocation><expect>CN-R-1 ORACLE: 11 of 11 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-r-1" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT, graded at the round close (never self-graded): `/seams` on the producer-to-served seam, grounded on the objects after the first scheduled run that carries the code, and the first-fire readback `r9_trend_groups_readback.py` (amended R11 in `round10/checks/`) - MECHANICAL (the four keys stay aligned to `dates[]`; every pre-existing key is equal to the prior day's rule; `carried_dates` equals the no-total dates plus the dates on which a leg actually carried; the partition identity R4 and the oracle R3 hold), DECLARATIVE (`meta.trend_groups` unchanged), SEMANTIC (the served output is unchanged on today's data, since the only gap, the sleeve on 2026-08-31..09-09, is not in the Total; the rule's effect is on a future gap where the Total contains the leg).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~29/MDPF_CANON.TO-CN-r-1.producer-carry-missing-trend-legs.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC4 UNVERIFIABLE-BY-INSTRUMENT and status_reason
"graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes. Commit through `.tools/safe-commit.sh` with a message file written by the Write tool; the commit gate (py_compile, ds-precommit, ruff py39) must pass -- if it refuses anything this order did not foresee, file a row and stop.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W29-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 10, issuer 2.0.0_SA_COO~D1, on the CTO's round-9 analysis `ledger/ROUND_ANALYSIS.round9.md` section 4 item 1 and section 3 (a) and (c), PRD v2.22 override (c), and the CTO's ruling on the issuer's contradiction (msg 6047: one generalized rule, the carry only where the carried row still partitions the served Total). Drafted by a one-shot fork; nothing committed.
- **Decisions the drafter took inside the ruling (the issuer may overrule):** (1) `carried_dates` gains a date ONLY when a leg actually carried; the 7 sleeve-less dates 2026-08-31..09-09 stay out (so `carried_dates` stays at the 9 no-total dates today and CN-p-1's oracle O4 stays green). (2) The test is per leg, not per row: Dividend and Growth cancel in the identity, so a row-level test would refuse a Dividend carry because of a sleeve gap on the same row (mutant `row-level` proves the arm R8 catches it). (3) The tolerance is 0.011 (the readback's `IDENTITY_TOL`), not 0.010: three 2-decimal roundings can differ by 0.015, and R4 already uses 0.011. (4) The Global All Equity TR allowance is the row's own SMArtX leg, which is exact; the readback's R4 allows up to `GAETR_MAX` before 2025-03-27. (5) A row with no `model_aua` carries nothing (fail closed).
- **Measured read-only (served 2026-10-14 Global object, SMArtX partition 2026-10-15):** the sleeve has its first value 2026-08-26 and is missing on 7 total-bearing dates (2026-08-31..09-09), where the Total excludes it: the new rule leaves them absent, so the tree's three arrays are identical to today's on all 497 dates (O1 0 differing cells), `carried_dates` is the 9 no-total dates, the nine period ends equal the amended oracle (max diff 0.00M), the identity holds on all 488 dated rows (max |residual| 0.0000), the readback R11 reads PASS on the newest row, and CN-p-1's `r9_cn_p_1.py oracle` reads 7 of 7 on the reference tree. Dividend and Growth have no gaps today; a planted Dividend deletion on a real row (O9) carries and moves only that row.
- **Honest limit of the rule:** the partition test is blind to Dividend and Growth (they cancel), so for them it is a no-op guard; and for the sleeve it passes only when the carried value is within 0.011 of the true value on that row, so a gap on a day when the sleeve moved is refused, not carried. Both follow from the ruling as worded.
- **Amendments owed to the round-9 checks in the SAME issuance:** none to `r9_cn_p_1.py`. `r9_trend_groups_readback.py` is replaced by the amended copy in `round10/checks/` (R11 extracted to `r11_check(g)`; a leg absent on the newest date but present before is Branch B unless that date is in `carried_dates`, then PASS "CARRIED by the producer"). R3, R4 and R6 are untouched.
- **Never-widen pair (COO half and CTO half; WORLD):** a scheduled gold fire writes the Global `aggregate-aua-timeseries` leaf (and the 4-scope parquet). On today's data the rule moves NO served cell (O1), so the pair may state DELTA=0 on the first fire; it must still count the writers of each moved leaf (N printed, not predicted from this draft) and state BOTH branches: (a) a gap where the Total contains the leg (carried; groups computed from the carried leg; the date named), (b) a gap where it does not (absent; the date not named), plus the SMArtX-absent branch (pre-boundary legs skipped). Rollback per key: the prior VersionId of the Global leaf. Headline `opal_aggregate_aua`, `by_model` and `model_aua` byte-equal. A same-`as_of` re-run records `conflict` (A8).
- **Risk and class:** WORLD (a producer change to a served object). `worker` class; about 45 product lines plus five tests. Slot ~29. Fanout: one cell, one chain, base box/dell1; independent of the other round-10 cells.
- **Not in this cell:** the portal (`trendGrouping.ts` already rolls a null forward on `carried_dates`; the issuer confirms at the render); the publisher IAM (item 2); the readback print (done, 48c40b2375); the Cottonwood Trend; the deploy; the pair.
- **UNVERIFIED by the drafter:** the lambda runtime (pure Python, no new import; ruff py39 clean); the actual N and blast radius; `build_all`'s whole-run behaviour on the reference tree (only the pure function and `apply_global_trend_groups` were run); whether the 497-date object is the one the first fire will see.

<status>complete</status>
<round>10</round>
<to_id>MDPF_CANON.TO-CN-r-1</to_id>
<slot>~29</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
