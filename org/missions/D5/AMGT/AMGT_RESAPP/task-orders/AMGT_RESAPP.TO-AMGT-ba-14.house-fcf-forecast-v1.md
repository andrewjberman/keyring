# AMGT_RESAPP task order -- `AMGT-ba-14` -- FWD-20: THE HOUSE FREE-CASH-FLOW FORECAST, TRAILING-TREND v1, WITH THE sd(D) GATE AND A REPORTED CORRELATION TO CONSENSUS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~280</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a pure module, its tests and a dry-run of the existing producer.
comp-iam: DECLARED-NOT-APPLICABLE -- the producer reads the same pool objects it reads today (crosswalk/v1, derived/model_block, peers/v1); no new read path, no write in this cell.
comp-adversary: RUN by the issuer at the cut -- r77_ba14 AC1 and AC2 FAIL at the base (no lib.research.scores.house_fcf); AC3 PASSES (the adapter's five names and the ABSENT default hold). Measured on BA_US_Equity's newest model block (20261007T001051Z): 10 fiscal years of SALES_REV_TURN and CF_FREE_CASH_FLOW, BEST_ESTIMATE_FCF for FY1-FY3, and NO dispersion statistic (none of BEST_CPS_STANDARD_DEV, BEST_CPS_AVG, BEST_CPS_NUMEST or the EPS three) among its 24 header and 12 forecast mnemonics.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; landed pool objects only, read-only.
</preflight>

**Your worktree:** `C:/tmp/r77-280` (branch `wk-AMGT_RESAPP-280`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-280`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-14` (round 77, decomposition s.85)

The CTO's ruling (round-75 analysis ADDENDUM 1 @68c5b56369, FWD-20; ADDENDUM 2 says it is not held), in its words:

1. The model: per name, annual, FY1-FY3, FCF = revenue x FCF margin.
   - Revenue grows at the median of the name's last 3-5 annual changes.
   - The margin is the trailing median of FCF / revenue.
   - Both come from the model block's reported history.
   - No consensus field is read by the producer.
2. D runs through the existing `divergence.py` against `BEST_ESTIMATE_FCF` FY1.
   - The sd(D) >= 0.25 gate runs before anything is served. A name short of history is ABSENT with its reason.
   - Added: the producer also prints the cross-sectional correlation of house FCF to consensus FCF, as a reported figure
     beside the gate, not a gate.
3. The filing-reference gap: option (a) for v1. A driver's reference is the Bloomberg reported fiscal period plus its
   announcement date. It is stored under a field that names it as that (`source: bloomberg_reported_period`), never
   labelled as a filing id, so a consumer can reject it.

**Build, with these names (the checks call them):**

1. **`lib/research/scores/house_fcf.py`, new, pure.**
   - `forecast(model_block) -> dict`. It reads ONLY figures with `scope == "fiscal_year_line_item"` and mnemonic
     `SALES_REV_TURN` or `CF_FREE_CASH_FLOW`, plus the header figure `ERN_ANN_DT_AND_PER` for the reference. It never reads
     a figure whose scope is `forecast` or whose mnemonic starts `BEST_`.
   - Growth is the median of the last FIVE year-over-year revenue changes where the history holds them, and of never fewer
     than three. The margin is the median of FCF / revenue over the last five reported years, and of never fewer than
     three. FY2 and FY3 compound the same growth at the same margin.
   - It returns `state` (`MEASURED`, or `ABSENT_SOURCE` with a plain `absent_reason` when the history is short or a
     revenue is zero or missing), `fy1` / `fy2` / `fy3` each `{fiscal_year, revenue, fcf_margin, fcf}`,
     `revenue_growth_median`, `fcf_margin_median`, the counts it used, and
     `reference: {source: "bloomberg_reported_period", fiscal_year: <the latest reported year>, announcement_date: <the
     date of that year's annual row in ERN_ANN_DT_AND_PER (period "<year>:A"), or null with announcement_date_reason>}`.
   - `universe_summary(records) -> dict` over `[{security_key, house_fcf, consensus_fcf, D}]`: `sd_D`, `n`, `degenerate`
     and `served` from `divergence.check_degeneracy` (served only when sd(D) is 0.25 or more over two or more measured
     values; otherwise `served: False` with a plain `reason`), plus `correlation_house_vs_consensus` (Pearson, over the
     names carrying both) and `n_correlation`. The correlation is reported; it never gates.
2. **`lib/research/scores/run_scores.py`.** For each keyed name the producer builds the house forecast from the model
   block it already reads, takes consensus as the `BEST_ESTIMATE_FCF` figure with `fiscal_period == "FY1"` (read HERE, in
   the producer, never inside `house_fcf.forecast`), and calls `divergence.score_divergence(row, model_fcf, consensus_fcf)`.
   The divergence record gains `house_forecast` (the `forecast` output) beside its existing keys. The universe summary is
   computed over all names BEFORE any record is written: when it reads `served: False`, every name's D, U and Delta are
   written ABSENT with the summary's reason, and the summary itself is written into each record as `universe_gate`.
3. **The dispersion gap, stated and not worked around.** `score_divergence` needs the CFPS or EPS dispersion statistics.
   The landed model block carries none (measured on BA, above). Where they are missing, D is ABSENT through the module's
   own existing guard, on every name. Do NOT pull them, do NOT substitute another denominator, and do NOT serve U or
   Delta in D's place. Print how many of the keyed names carry them.
   **AMENDMENT 1 (issuer, on the CTO's round-76 ADDENDUM 1 @a7b2c3e0ba, before the spawn):** where the dispersion
   statistics are missing, D is ABSENT with exactly the reason `consensus dispersion is not yet pulled`. The record still
   serves the house forecast, and it gains `gap_vs_consensus_pct`: the plain percent gap of the house FY1 FCF against the
   consensus FY1 FCF (`(house - consensus) / abs(consensus) * 100`, null with a plain reason when either is missing or
   consensus is zero), with `gap_label` exactly `house FCF against consensus FY1, percent`. It is a labelled plain gap,
   never D, U or Delta. File NO row for the missing fields: they ride AMGT_CORPUS's scheduled pull (its round 40). Add
   plant tests for the gap (a positive gap, a negative consensus, a zero consensus, a missing side).
4. **Plant tests** in `lib/research/scores/tests/test_house_fcf.py`: the median rule at three, four and five changes; a
   negative-FCF history; a zero revenue; the consensus-blind control; the reference with and without an annual row; the
   gate at 0.24 and 0.25.
5. **One dry run of the producer** (`python -m lib.research.scores.run_scores --dry-run`), read-only on the pool. Save
   its printed summary to your deliverables as `DRY_RUN.md`: names keyed, forecasts MEASURED and ABSENT with the reasons
   grouped, names with a consensus FY1 figure, names with dispersion statistics, `sd_D`, the correlation and its n.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W280-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No pool write: the producer runs with `--dry-run` only. No deploy, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `divergence.score_divergence()` with no house forecast stays ABSENT with `NO_HOUSE_FORECAST_REASON`. Keep these names: `divergence.NO_HOUSE_FORECAST_REASON`, `divergence.LEGACY_NO_HOUSE_FORECAST_REASON`, `divergence.DEGENERACY_FLOOR` (0.25). The serving adapter reads them.
3. Every existing key of the scores record stays; you only add keys. The served route passes the record through as it is stored, so no adapter edit is needed and none is yours.
4. `lib/research/scores/peers_v.py` is another cell's file this round (AMGT-ba-16). Do not edit it.
5. Any reason you write is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/scores/house_fcf.py
lib/research/scores/run_scores.py
lib/research/scores/divergence.py
lib/research/scores/tests/test_house_fcf.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~280/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-14"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba14.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>C0-C6 PASS: the median rule on revenue and margin, FY3 compounding, the consensus-blind control EQUAL, the reference labelled bloomberg_reported_period, a short history ABSENT with its reason; R77 BA14 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-14"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba14.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>C0-C4 PASS: the gate serves at sd(D) 0.25 or more, refuses a near-zero spread and fewer than two values with a reason, and the correlation is reported with its n; R77 BA14 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-14"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba14.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>C1-C3 PASS (the control): the no-forecast default is still ABSENT with the plain reason, the adapter's five names exist, the floor is 0.25; R77 BA14 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~280 <0.9.0_WK_AMGT_RESAPP~280@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~280/AMGT_RESAPP.TO-AMGT-ba-14.house-fcf-forecast-v1.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the dry run's counts: forecasts MEASURED and ABSENT, names with consensus FY1, names with dispersion statistics, sd(D), the correlation and its n;
- any existing test you changed and why;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Z):** ROUND_ANALYSIS.round76.md @c8bbeeac10 section 4 item 9; ruling text ROUND_ANALYSIS.round75.md ADDENDUM 1 @68c5b56369. Decomposition s.85. Chain `~280`, wave 0, no inbound edge. Checks dry-run at the base: ba-14 AC1 base: FAIL as expected; ba-14 AC2 base: FAIL as expected; ba-14 AC3 base: PASS as expected. No adapter hookup: `scoped_amgt._plain_score_record` passes the stored record through. OPEN FOR THE CTO, carried in the packet: the model block carries no dispersion statistics, so D stays ABSENT on every name and the sd(D) gate cannot serve until those fields are pulled (Andrew's word). The real producer run (a pool write) is NOT in this cell.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~280</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @0f83652b8b; proof VALID (worktree checker); house FCF forecast v1 with the sd(D) gate, the reported correlation and the labelled plain gap (AMENDMENT 1); dry run: 237 keyed, 92 forecasts MEASURED, 0 names with dispersion, correlation 0.943 over 84; AC1 7 of 7, AC2 5 of 5, AC3 3 of 3; rows Z-W280-S1 (issuer ruling: the worker's reading stands -- the gate overwrites only a MEASURED D), Z-W280-S2</status>
