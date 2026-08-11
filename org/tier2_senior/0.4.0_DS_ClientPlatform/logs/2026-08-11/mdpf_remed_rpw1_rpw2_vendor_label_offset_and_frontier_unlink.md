# RP-W1 vendor label offset (orion+eclipse) + RP-W2 cross-firm frontier unlink — 0.4.0_DS_ClientPlatform

**Date:** 2026-08-11 (session start 2026-08-10 ~2350Z)
**Task Order:** MDPF_REMED.RP-W1 then MDPF_REMED.RP-W2 (batch GO 2.0.0_SA_COO 233107Z; atomic-deploy re-cut 234440Z)
**Status:** COMPLETE (BUILD+COMMIT scope) — **DEPLOY LEG DELIBERATELY NOT FIRED** (held for the COO-called
atomic window with AE's RP-W3 per Andrew's ~2334Z ruling). **PUSH not fired** (Andrew standing hold).

---

## Objective

Served MDPF numbers are wrong today: orion + eclipse silver partitions are RUN-DATE keyed and carry the
PRIOR NYSE trading day's close, so a served label D contained D-1's data (D-4/D-10), and inflection's
axis frontier was imported from 49F's artifact (D-1 violation). RP-W1 makes a served label mean the day
it claims (orion + eclipse ONLY — schwab/blackdiamond labels are accurate and untouched); RP-W2 severs
the cross-firm FRONTIER link while keeping the shared canonical CALENDAR.

## What changed (all in my Rule-13 lane; committed, NOT deployed, NOT pushed)

1. `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`
   - RP-W1: `_vendor_label_of()` + `_partitions_by_label()` — the T-1 label normalization, wired via
     `prev_trading_day` from `mdpf_calendar_binding` (the canonical `lib/trading_calendar`). **Semantics
     are the sealed `orion_normalize_as_of` (= prior_trading_day, `data/inf/scripts/silver/_orion_vendor_asof.py:128-139
     @e329f0e5ef`) — NOT re-derived**: a cross-tree import of the inf silver module cannot resolve in the
     deployed mdpf-gold package layout (sys.path is the script's own dir + the calendar binding), and the
     canonical pmc calendar supersedes that module's hardcoded 2025-2027 closed-dates table (tie-out n=1096,
     0 in-window disagreements, `MDPF_CALENDAR_TIEOUT_20260806.md`). Wired into
     `load_inflection_custody_history` (orion) + `load_inflection_model_history` (eclipse): an axis LABEL D
     now reads the partition whose run-date normalizes to D.
   - RP-W1: `_model_leg_eclipse` axis=None frontier self-derivation moved to TRUE-LABEL space.
   - RP-W2: `main()` `:2682-2683` — `axis=None` for inflection (self-derived frontier; calendar stays
     shared via `canonical_trading_axis`; `build_global_artifact` date-joins on the UNION axis so
     identical axes are not required).
2. `data/mdpf/scripts/gold/build_mdpf_spine.py` + `data/mdpf/scripts/gold/stage_mdpf_revamp_trio.py` —
   **the RP-W2 call site had MULTIPLIED since the plan** (comp-find found 3 live callers, not 1; the stage
   trio is the deployed-generation route that stages the served artifacts). Both re-grounded and fixed
   with the identical `axis=None` pattern. Surfaced to COO in the BUILD-READY report per the TO's
   mismatch clause — mechanically identical, same lane, so fixed rather than held.
3. `data/mdpf/scripts/gold/gold_validate_config.yaml` — `dim_mdpf_aggregate_aua_timeseries` had
   **NO_CONFIG** (= UNVALIDATED, a phase-2 stop condition). Authored a 6-check entry over the contract
   common to all three scopes; exercised on all three QA artifacts (PASS 6/6 each) AND on a MUTANT
   (source_vintage_last removed + dates truncated → 2 ERROR, BLOCKED — the config discriminates; gate
   accepted on an observed red run, not its authoring commit alone).
4. TO status flips staged→pending (RP-W1, RP-W2).

## Acceptance (EXERCISED, Rule 22a)

1. **A served point labelled D contains D's close, tied out against the vendor artifact for D:**
   - orion label 2026-08-07: POST artifact `partner_custody_total` = **$209,373,343.50** == direct pandas
     sum of `orion/inflection/silver/fact_assets/date=2026-08-10` (the run-date partition for Friday's
     close). PRE artifact wrongly had $208,325,960.35 (= 08-06's close) at that label.
   - orion label 2026-08-04: POST = **$209,431,383.43** == partition date=2026-08-05 sum — **this is
     Andrew's D-4 MEASURED anchor**: the value served-mislabeled Wednesday 08-05 now sits at its true
     Tuesday 08-04. PRE had it at label 08-05.
   - eclipse label 2026-08-07: POST `model_aua` = **$145,329,103.38** == Opal-crosswalk sum of
     `eclipse/inflection/silver/fact_portfolios_full/date=2026-08-10`. PRE wrongly had $144,545,199.97.
2. **lag_vs_as_of_days asserts nonzero when lag exists (exercised run):**
   `build_source_vintage_revamp` with tonight's REAL leg vintages (both 2026-08-07) against frontier
   2026-08-10 → `lag_vs_as_of_days=3, status=BEHIND, tdb=2` (nonzero: PASS). The full-build variant of
   that shape is refused by the limb-(v) cross-axis gate before emission (count-without-value at the
   extended frontier) — that is the D-19 guard working, observed firing in this QA. In the emitted
   standalone artifact lag=0 is now TRUTHFUL (overall==frontier==2026-08-07 in true-label space).
3. **NEGATIVE CONTROL — schwab + blackdiamond UNCHANGED pre/post** (pre = clean HEAD @a7281ae8e0 in a
   scratch worktree, post = this change; both `--firm all` full builds against live S3):
   - schwab/49F: `dates` (n=441, frontier 2026-08-07), `partner_custody_total` (frontier
     $1,735,211,819.45), `model_aua` — **all byte-identical pre/post**.
   - blackdiamond/cottonwood (global fold): per-date `as_of_by_partner.cottonwood` vector (n=450,
     frontier row ('2026-08-07','2026-08-06')) **identical pre/post**; `cottonwood_carry` meta identical
     except the `roster` LOCAL PATH string (pre ran from the scratch worktree — environment artifact,
     not behavior).
4. **RP-W2: standalone inflection axis == consolidated axis:** both n=441, frontier 2026-08-07,
   list-identical (IDENTICAL=True).
5. **RP-W2: NO smartx/** read in an inflection build — EXERCISED via instrumented boto3 client:**
   TRACE DENOMINATOR 987 S3 read calls recorded in the standalone build; **smartx keys touched = 0**.
   Distinct read targets: eclipse/inflection/silver, orion/inflection/silver, and inflection's own
   account_distribution.json only. (Also the decisive read for "frontier moves independently of 49F
   content": the derivation reads zero 49F bytes, so it structurally cannot depend on them.)
6. **Frontier under self-derivation = 2026-08-07** — exactly D-19's prediction (eclipse HAS 08-07);
   the orion named gap correctly lands at TRUE label 2026-08-05 (the vendor's skipped 08-06 run).

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | `comp-pipescript io dim_mdpf_aggregate_aua_timeseries.py --pipeline mdpf` | PASS | reads = gold/mdpf_revamp/* + the 5 monolith silver fact_* exactly as the TO expects; no unexpected leg; WRITES none (consolidator uploads) |
| comp-find | `comp-find "orion_normalize_as_of" data` | PASS | DENOMINATOR 21 hits/960 files: DEF=1 (`_orion_vendor_asof.py:128`), 0 call sites in the mdpf gold builder — sealed-never-called premise re-confirmed at HEAD before edit |
| comp-find | `comp-find "build_inflection_artifact" data/mdpf` | PASS (premise moved, surfaced) | DENOMINATOR 7 hits/57 files: call site had MULTIPLIED to 3 (main + build_mdpf_spine:104 + stage_mdpf_revamp_trio:65). Re-grounded, all 3 fixed, surfaced to COO |
| comp-blast | `comp-blast build_inflection_artifact` | WARN | NOT-FOUND with printed denominator (20,615 nodes) — function not a graph node; the TO's anticipated fallback; comp-find census above is the consumer roster |
| comp-validate | `comp-validate dim_mdpf_aggregate_aua_timeseries --artifact <post/{firm}> --config data/mdpf/scripts/gold/gold_validate_config.yaml` | PASS | was NO_CONFIG (stop condition) → authored the entry in-lane; PASS 6/6 on all 3 scopes; MUTANT control fires (2 ERROR, BLOCKED) |
| commit-gate | via safe-commit (`.tools/commit-gate.sh`) | PASS | py_compile + ruff + `from __future__ import annotations` present (see commit) |
| comp-pipescript deployed | `comp-pipescript deployed dim_mdpf_aggregate_aua_timeseries.py` | SKIPPED | deploy leg HELD for the COO atomic window (234440Z) — phase 3 runs at the window. R-33: tool false-STALEs on CRLF; do not read STALE as a deploy gap |

**What worked:** comp-find's band separation caught the multiplied call site the plan's "two lines" missed —
the exact class the mandate exists for. The pre/post scratch-worktree comparison made the negative controls
one command each.
**What failed:** comp-blast cannot resolve a function-grain node (honest NOT-FOUND with denominator);
comp-validate had no config for the spine producer (now closed in-lane).
**Gap found:** `dim_mdpf_account_distribution.py` + `data/mdpf/scripts/feeders/wsc_inflection_held_etf.py`
also read eclipse/orion silver with run-date keys — the label offset does NOT cover them (out of this TO's
named scope; surfaced to COO). ROW11 already logs the visible symptom (frontier-stamp STALE, inflection:
stamp 08-07 vs count 08-04).

## Banked findings (surfaced to COO in the BUILD-READY report, not held)

1. RP-W2 call site multiplied to 3; all fixed (above).
2. Sibling consumers of eclipse/orion run-date partitions not covered by this TO (above).
3. 3 PRE-EXISTING test failures in `tests/test_global_fold_flag2.py` (carry family) — fail identically at
   clean HEAD @a7281ae8e0 and post-change (63 pass both sides; zero regression from this change). They
   assert the superseded windowed-carry behavior; Andrew's roll-forward ruling (033107Z) changed the code,
   nobody re-cut the tests.
4. Eclipse crosswalk WARN: eclipse_id=31 '90/10 Opal Intermediate/Ultra Short Term' recurring
   candidate-NEW-Opal on 8 dates (folded to non_model per F5) — crosswalk review owed.
5. `expected_last_trading_day(2026-08-11T00:08Z) = 2026-08-11` (canonical calendar) → tonight's artifacts
   read status=BEHIND tdb=2 at a Friday frontier on Monday evening. Canonical convention, unchanged by me;
   noted so the window-night reader does not mistake it for a defect.

## QA artifacts

Scratchpad (session-local): `pre/` + `post/` full-build artifact trios (pre = clean HEAD worktree),
`inflection_standalone_traced.json`, `qa_rpw12_traced_inflection.py`, `qa_rpw12_compare.py`,
`mutant_inflection.json`. Nothing written to S3; builds write LOCAL --out-dir only.
