# NFRA_GRAPHUNI EMISSION-FILTER TRACE — per-member attribution + predict-then-measure control

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T070827Z
(supersedes 070657Z RESIDUAL-SWEEP per CVO~Z's 070754Z ruling) · **reports to:** `1.0.0_SA_CTO~Z` +
`3.0.0_SA_CVO~Z` ONLY · **boundary observed:** measurement only, ingestion hard-gated.

**Note on the crossed dispatch:** the 17-target sweep (070657Z) had already been run before the 070827Z
supersession arrived — its coverage-per-target result (58.2%–100%, NOT clustered near 91%) is real data
and included in the sidecar for completeness, but it is not this memo's primary content per the
supersession.

---

## Concede-or-contest, closed: 7-vs-12 CONCEDED — 2-vs-17 carried forward

CVO~Z's arithmetic (14 `WRITES_S3`-carrying members cannot fit in a 12-member in-scope set, since
`WRITES_S3` is explicitly in `extract_gold_compute.py`'s own `coverage.slices_scanned`) is correct and my
original 7/12 split is wrong — I counted "carries `TRIGGERS`/`FETCHES` *at all*" instead of "carries
*only* out-of-scope classes." **Conceded.** Restated under the strict predicate, matching CVO~Z's
re-partition exactly:
- **2 out-of-scope** (carry *only* `TRIGGERS`/`FETCHES`, no in-scope class): `gold:gold_dispatch`,
  `gold:orion-gold-dispatch`.
- **17 in-scope**, node-type partition (independently re-derived from my own sidecar, matches CVO~Z's
  handed-over 8/2/7 exactly): **8 `gold:` · 2 `lambda:` · 7 `s3:`.**

## Predicted predicates — confirmed/refuted per member, at source

| Prediction | Verdict | Evidence |
|---|---|---|
| `:94`'s GOLD_SCRIPT-only slice explains the 2 `lambda:` members | **CONFIRMED** | `lambda:bd-price-update`, `lambda:opal-partners-data` are `GENUINELY-ABSENT` — zero producer edges reference either canonicalized id under ANY form. Structurally consistent with `:94` (`fn_firm` only populated from `GOLD_SCRIPT` nodes) **compounded by** the `READS_S3`/`WRITES_S3` handlers' own `key.startswith("s3:")` requirement (`:185`) — a lambda-typed endpoint can satisfy neither the `CALLS` branch (needs both ends in `fn_firm`) nor the S3-typed-key requirement of the other two branches. No code path in this producer can ever emit an edge to a `lambda:` id. |
| Key-form canonicalization (bucketless vs. bucket-qualified) explains the 7 `s3:` members | **REFUTED for 5 of 7.** | Directly checked: `s3:config/ticker_lookup.json`, `s3:gold/meta/positions_cube_incr_watermark.json`, `s3:silver/historical_prices.parquet`, `s3:silver/realized/bd_realized_agg.parquet`, `s3:gold/account_gains/{*}.parquet` all have **correctly bucket-qualified edges present** in the producer's raw JSON (my `un_s3_id()` strip-the-firm-prefix reconstruction recovers the exact expected id — no map/expansion needed, unlike the earlier live-kuzu comparison). These 5 are `PRESENT-UNREACHABLE` — see the new finding below, not a form issue. **Holds for the other 2** (`s3:silver/accounts_dim/latest.parquet`, `s3:silver/interpolated_prices.parquet`) only in the weak sense that they're genuinely absent — but zero producer edges exist under ANY form, so this isn't a form-mismatch either; it's a source-extraction gap (see below). |
| `8 gold:` members fall to `:160` (read-only-writers) or `:175`/`:185` (fn-attribution) | **REFUTED, all 8.** | Every one of the 8 `gold:` members has its own edges present in the producer's raw output, correctly attributed and firm-qualified. None were dropped by an attribution predicate — they are `PRESENT-UNREACHABLE`. |

## The actual dominant finding, not predicted by any of the three: REACHABILITY, not emission filtering

Classified all 17 in-scope missing members by checking, for each: does a correctly-canonicalized edge
referencing this id exist ANYWHERE in the producer's raw output (any direction, any form)? If yes but the
member still isn't in this seed's BFS radius, it's **`PRESENT-UNREACHABLE`** — the member's own connecting
edge is fine; something *between* the seed and that member is broken. If no edge exists under any form,
it's **`GENUINELY-ABSENT`** — a real emission gap.

```
CLASSIFICATION COUNTS: PRESENT-UNREACHABLE: 13/17 (76%)   GENUINELY-ABSENT: 4/17 (24%)
```
Zero `REACHABLE-BUT-MISSED` self-check failures (a member classified reachable that was also in the
missing set — a logical impossibility if the trace script were wrong) — the classification is internally
consistent.

**This means: three-quarters of the sharp case's real residual is not a filter/predicate question at
all.** The predicted predicates (`:94`, `:160`, `:175`/`:185`, key-form) are all per-EDGE emission
questions — "does this producer choose to emit this specific relationship." The dominant cause instead is
that the **path** from the seed to these 13 members — some intermediate `CALLS`/`READS_S3`/`WRITES_S3`
hop — doesn't exist or doesn't connect in the reconstructed graph, even though the terminal edges
individually are present and correctly formed. **Not traced further this pass** (a proper trace of *which*
intermediate hop is missing, per member, is real follow-on work — flagged, not attempted, given this
dispatch's scope was attribution + the control, not a second-order investigation).

**The 4 `GENUINELY-ABSENT` members**: 2 `lambda:` (see confirmed prediction above — structurally
impossible for this producer to emit, a **DELIBERATE-SCOPE-BOUNDARY** by construction, not a bug), and 2
`s3:` (`accounts_dim/latest.parquet`, `interpolated_prices.parquet`) whose cause is genuinely unresolved
this pass — zero producer edges under any form means the underlying `_extract_s3_reads()`/
`_extract_functions_with_s3()` regex passes in `extract_s3.py` never found the read/write pattern in
whatever source file references these keys. **Classified as an open question, not assumed either
DELIBERATE or UNINTENDED** — would need a source read of the specific gold script(s) that the fixture says
touch these keys, not attempted this pass.

## Disposition column (per the dispatch's ask) — reframed by the finding, not skipped

| Predicate / cause | Members | Disposition |
|---|---|---|
| `:94` GOLD_SCRIPT-only slice (lambda targets) | 2 (`lambda:*`) | **DELIBERATE-SCOPE-BOUNDARY** — this producer's own docstring names its scope as gold-compute only; a lambda-target relationship is a different producer's job (comp-aws/comp-lambdamap territory), sourcing it here would be scope creep, not a fix |
| Unresolved source-extraction gap (2 `s3:` keys) | 2 | **UNDETERMINED** — genuinely open, not attempted to disposition without reading the specific source first |
| Reachability gap (intermediate hop missing) | 13 (8 `gold:` + 5 `s3:`) | **UNDETERMINED, DIFFERENT REMEDIATION CLASS** — not an emission-filter fix at all; would require tracing which specific intermediate `CALLS`/`READS_S3` edge is absent from the *chain*, a distinct follow-on investigation from what "fix the dropping predicate" implies |
| Genuinely out-of-scope (2 members) | 2 (`gold:gold_dispatch`, `gold:orion-gold-dispatch`) | **DELIBERATE-SCOPE-BOUNDARY** (confirmed prior pass — `TRIGGERS`/`FETCHES`-only, a different extraction pass's job entirely) |

**Net: of 19 total missing members, at most 4 (2 lambda + the 2 out-of-scope) have a clean
DELIBERATE-SCOPE-BOUNDARY disposition today. The remaining 15 (13 reachability + 2 unresolved) need
further investigation before either disposition can be assigned — reporting this honestly rather than
forcing a premature UNINTENDED-FILTER label onto a cause (reachability) that isn't actually a filter.**

## Predict-then-measure control

**PREDICTION, written down before running** (verbatim from `emission_trace_control.py`'s own docstring,
committed to the script file before execution — not reconstructed after the fact): *"held-out target
`s3:gold/timeseries/client_performance.parquet`. Model built from the sharp case: 13/17 (76%)
PRESENT-UNREACHABLE, 4/17 (24%) GENUINELY-ABSENT (both lambda: members + 2 s3: members). Prediction: the
majority of this target's missing members will classify PRESENT-UNREACHABLE; any GENUINELY-ABSENT members
will skew toward non-GOLD_SCRIPT node types (lambda:) rather than gold:/s3: members."*

**MEASURED** (run after the prediction was committed):
```
old_n=168 new_n=120 missing_n=54
CLASSIFICATION COUNTS: PRESENT-UNREACHABLE: 47/54 (87%)   GENUINELY-ABSENT: 7/54 (13%)
genuinely-absent node-type prefixes: gold, gold, lambda, lambda, lambda, lambda, s3
```

**Verdict: the dominant-mechanism prediction HOLDS — PRESENT-UNREACHABLE is again the large majority
(87%, vs. the predicted "majority").** This is the part that matters: it forecasts, not just retrodicts —
the reachability-dominant pattern generalizes to a target this pass never fitted anything on.

**The composition prediction was only partially right, stated plainly, not smoothed over:** 4 of the 7
genuinely-absent members ARE `lambda:` (matches the "skew toward lambda" prediction), but **2 are `gold:`
and 1 is `s3:`** — the sharp case's model showed ZERO genuinely-absent `gold:` members, so this specific
detail was not forecast correctly. **The mechanism (reachability-dominant) is a real, confirmed forecasting
result; the exact genuinely-absent composition varies by target and is not yet captured by a single rule.**

## Function-level controls — extended, still clean

Ran 2 more function-level targets beyond `generate_header_metrics` (which has now been clean on 4+
independent measurement paths across this session): `gold:D_02.advisor_client_detail:main` and
`gold:INF_D_02.advisor_client_detail:build_advisor_books`. **Both 0 missing, 0 extra, exact.** Function
grain remains the trustworthy comparator — the method itself is not in question; the estate's script-grain
reachability is.

## What this lane did NOT do

Did not trace which specific intermediate hop breaks reachability for the 13 `PRESENT-UNREACHABLE`
members (real follow-on work, out of this dispatch's scope). Did not read source for the 2 unresolved
`s3:` genuinely-absent keys. Did not run the 17-target sweep's classification (only the sharp case + the
one held-out control target were classified member-by-member, per the dispatch's revised scope — the
sweep's coverage-per-target numbers from before the supersession are in the sidecar as supplementary data,
not re-analyzed for edge class). Did not wire anything into live ingestion.

## Files

| File | Role |
|---|---|
| `deliverables/NFRA_GRAPHUNI_REASSERT/emission_trace.py` | sharp-case per-member classification script |
| `deliverables/NFRA_GRAPHUNI_REASSERT/EMISSION_TRACE_result.json` | sharp-case full per-member result |
| `deliverables/NFRA_GRAPHUNI_REASSERT/emission_trace_control.py` | predict-then-measure control (prediction in its own docstring, committed pre-run) |
| `deliverables/NFRA_GRAPHUNI_REASSERT/EMISSION_TRACE_CONTROL_result.json` | control measurement result |
| `deliverables/NFRA_GRAPHUNI_REASSERT/residual_sweep.py` + `RESIDUAL_SWEEP_result.json` | the pre-supersession 17-target sweep (supplementary, not this memo's core) |
