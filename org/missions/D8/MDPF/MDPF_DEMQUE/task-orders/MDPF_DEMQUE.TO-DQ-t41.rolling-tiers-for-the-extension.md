# TO MDPF_DEMQUE.TO-DQ-t41 -- round 9 DQ-t-41: the standing extension is TIERED -- daily for the served and held set, a 5-trading-day rolling cycle for IRPT_BCKEND's 782
<to_id>MDPF_DEMQUE.TO-DQ-t41</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~33</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>ROLLTIER</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-41` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 6) |
**outcome_ref:** C-PRICES, C-YAHOO, FWD-8, FWD-9 | **depends_on:** DQ-t-31, DQ-t-36, DQ-t-37 (merged)

---

## WORKER FACE

### THE CELL

`DQ-t-41` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` ADDENDUM 7, read it, with ADDENDUM 6). The vendor
library's batch call sends one HTTP request per symbol (measured in DQ-t-40), so the shared pacer's cap of 400 requests a day stays and the
standing extension is TIERED, not batched: **DAILY (T-1)** the 141 names the price store serves today plus ADVI_COTBKF's 15 funds (156 requests a
day); **ROLLING** IRPT_BCKEND's 782 new names (its 878 minus the 96 already stored) on a cycle of at most **5 trading days**, in FWD-9 rank order.
Every value served from a rolling name carries its own `as_of`, its stored max date, so a consumer reads the lag and never infers freshness.

**Build** (in `data/mdpf/scripts/demque/extend_frontier.py` and a NEW test file; read `extend_frontier.py` as merged at HEAD, `rank.py` and
`lib/trading_calendar.py` first):
1. **The enrolment.** NEW file `org/missions/D8/MDPF/MDPF_DEMQUE/requests/ENROLMENT_TIERS.json`:
   `{"daily_extra": ["ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012"], "rolling": [{"request_id": "IRPT_BCKEND-AS-TRADED-CLOSES-878",
   "cycle_trading_days": 5, "order": "FWD-9"}]}`; each id names a request file in that folder whose `securities` give the names. Read it in
   `plan()`. A request id with no file, or a malformed enrolment, is a loud `SystemExit`.
2. **The tiers in `plan()`.** Over the names `price_store.index` lists (LANDED names only): `rolling` = the securities of each rolling request
   that are NOT already in the index when the rolling request is enrolled (the 96 stored ones stay daily); `daily` = every other indexed name,
   including the `daily_extra` funds once landed. A rolling name that has not landed (not in the index) is excluded and COUNTED in the plan
   (`rolling_not_landed`). Output keys added: `tiers` `{daily: n, rolling: m, rolling_not_landed: k}` and `slice_date`.
3. **The rolling slice.** Order the rolling names ONCE by FWD-9 rank (`rank.rank(...)` with the same inputs `rank.py --probe` reads; if its inputs
   cannot be read, order by symbol and say so in the output as `order: "symbol (rank inputs unavailable)"`). Cut the ordered list into
   `cycle_trading_days` contiguous blocks; the block for a day is `trading_day_ordinal(frontier) mod cycle` (an integer from the trading calendar,
   so it is stateless and a missed day does not shift the others). The day's request holds the `daily` names plus that block. Names outside the
   day's block are NOT in the request and their pacer entries are NOT reset.
4. **The cap is a refusal.** `plan()` raises `SystemExit` when the day's request count would exceed `DAILY_CAP` (400) minus a stated reserve of 20
   for the tier-2 history draws; the message names the count and the cap. No batch is counted as one request.
5. **`--plan-week --from D --days N [--assume-landed REQUEST_ID]`**: print ONE JSON line `{"days": [{"date", "daily", "rolling", "requests"}, ...],
   "max_requests", "max_lag_trading_days", "rolling_names", "assumed_landed"}` over the next N trading days from `D`, computed from the real index
   (S3 read only). `--assume-landed` treats that request's names as landed for PLANNING only and says so (`assumed_landed` the request id,
   else null). `max_lag_trading_days` = the largest gap, in trading days, between two visits of any rolling name across the span (must be <= the
   cycle). Writes nothing.
6. **The freshness entry.** Find where the Yahoo `price_history` store's freshness is or would be declared (`.tools/comp-freshness`,
   `.tools/freshness_manifest_gen.py` and the per-firm `gold_freshness_config.yaml` / `data/served_freshness_config.yaml` it reads) and add ONE
   entry for the store with `freshness_basis: trading-day-frontier` and the lag per tier declared in its note (daily: 0 trading days behind
   the frontier; rolling: at most 5). If no existing config fits, do NOT invent a schema: file a surprise row naming what you read and stop that item.
7. NEW `test_demque_rolling_tiers.py` (pytest; a LOCAL store root under `tmp_path`, a stub enrolment folder, no network, no S3) with exactly
   these names: `test_daily_tier_is_the_stored_names_plus_the_advi_funds_every_trading_day`,
   `test_rolling_names_are_visited_in_rank_blocks_each_within_five_trading_days` (7 consecutive trading days; the first block holds the top-ranked
   names), `test_a_day_never_exceeds_the_cap_and_names_not_yet_landed_are_excluded_and_counted`.
   The three existing extension test files keep passing unedited (they pin the local date).

### ACCEPTANCE

<criterion id="DQ9-t41-AC1" cell_refs="DQ-t-41"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t41_tests.py</invocation><expect>TIER-OK</expect></criterion>
<criterion id="DQ9-t41-AC2" cell_refs="DQ-t-41"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t41_week.py</invocation><expect>TIER-REAL-OK</expect></criterion>
`DQ9-t41-AC1` -- the three named tests. `DQ9-t41-AC2` -- on the REAL served store (S3 read only), a 7-trading-day plan with the 782 assumed landed: every
day at most 400 requests, the daily tier at least 141, 782 rolling names, every one visited within 5 trading days. Report the whole folder
`pytest data/mdpf/scripts/demque` once (136 passed at the t-39 merge, plus t-40's 3).

<expected_criteria>DQ9-t41-AC1,DQ9-t41-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `TIER-BAD no file ...`; `extend_frontier.py: error: one of the arguments --plan --apply is required`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY against S3 and Yahoo: no write to the served store, the real pacer state, the queue or the ledger; no Yahoo or Bloomberg call; no
  AWS write; no deploy.** `--apply` is never run against the real home (the issuer's act under its own pair).
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W33-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_rolling_tiers.py
org/missions/D8/MDPF/MDPF_DEMQUE/requests/ENROLMENT_TIERS.json
data/served_freshness_config.yaml
.tools/freshness_manifest_gen.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit (a different freshness config file than the two above is a
surprise row asking for the grant, not an edit).

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-41`.
<owned_cells>DQ-t-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t41-AC1, DQ9-t41-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~33/MDPF_DEMQUE.TO-DQ-t41.rolling-tiers-for-the-extension.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t41-AC1,DQ9-t41-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the 7-day request table verbatim, the rank order source, the freshness entry (or the row), the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the existing daily draw runs the tiered extension from its next run after the issuer's apply.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder over the existing queue and pacer; the served write is the existing price_store.write.
risk: LOCAL -- code, tests and one config entry. The apply (enrolling 782 new names in the standing extension) is SERVED under its own never-widen pair (CTO ADDENDUM 6/7).
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 ADDENDUM 6, 7 (msgs 4243, 4252); TO-DQ-t40 EQUALITY_REPORT; decomposition round 9.
