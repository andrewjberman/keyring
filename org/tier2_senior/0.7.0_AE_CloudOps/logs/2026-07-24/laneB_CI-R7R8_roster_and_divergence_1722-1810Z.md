# 0.7.0_AE_CloudOps~B — CI-R7R8 rows 7+8: the partner roster + normalised divergence

**archetype:** IMPLEMENT

**Session:** 2026-07-24 17:22Z–18:10Z · lane `~B` (fresh) · TO `MDPF_CHANNEL_INDEPENDENCE.CI-R7R8`
**Authorization:** Andrew-direct ~1720Z *"Go now, this is P0."* via COO GO @174109Z.
**Landed:** `fd6e92faa` — committed, **NOT pushed** (Tier-1 push only, Andrew ~1600Z; COO is push operator).

---

## What was delivered

| Artifact | Purpose |
|---|---|
| `data/mdpf/config/partner_roster.json` | THE declared data — partners, legs, per-quantity effective windows, per-feed cadences, feed locations, aliases, axes |
| `infra/aws/lambda/mdpf-pipeline/_shared/mdpf_roster.py` | reader + normalised divergence (row 8) |
| `infra/aws/lambda/mdpf-pipeline/_shared/tests/test_mdpf_roster.py` | 17 tests, **17/17**, mutation-verified |

**Row 7 acceptance — the partner-#4 test — was RUN, not asserted.** A synthetic fourth partner (`northgate`,
channel D, own per-quantity dates, own T-1 cadence) is added as a pure data row and drives the **unmodified**
production module: expectations, composition, cadence, frontier, divergence and the alias crosswalk all
follow. No subclass, no monkeypatch, no branch, no registration call. Offboarding tested via `effective_to`.

**Row 8 — live estate reads 0/0/0**, spread 0, signal false. Measured 2026-07-24T17:38Z, **denominator 7 of 7
feeds across 3 partners, 0 inferred.**

---

## The three things I would want a successor to read

**1. I refused to guess an effective date, and it turned out the PRD was wrong.**
PRD §2.6 recorded inflection as effective-from "existing" (inception). The producer said
`INFLECTION_MODEL_LAUNCH = "2026-05-15"` with **Andrew-direct 07-21 verbatim at :1045 — *"it was 0, 5-15 was
the beginning."*** I routed it to CTO rather than picking one, on the reasoning he then asked to be quoted
back: **an effective date is SILENT when wrong — there is no failing test, the alarm simply never fires.**
CTO ruled the producer wins, amended the PRD (`f642948889`), and accepted the structural half: the roster key
became **(firm, LEG, quantity)** because inflection's custody and model legs do not share a start.
*Cost of surfacing at minute 15: one message. Cost of being wrong: an alarm that never fires.*

**2. CTO left one cell as ESTABLISH and forbade assuming inception. I measured it instead.**
`orion/inflection/silver/fact_assets` first partition is **`date=2020-04-28`** — 4.5 years before the
2024-11-01 series floor — so custody genuinely covers the served window and **the floor binds, not the feed.**
Recorded on the artifact face as `established_by: MEASUREMENT` so no successor re-reads it as the assumption.
Separately, `eclipse/inflection/silver/fact_portfolios_full` first partition is **`date=2026-05-15`** — the
**data independently corroborates the ruling**, so that cell no longer rests on a self-report at all
(PRD §3.1 rule 1: derive from partition identity).

**3. I reported a stale-record finding I was not asked for, and it was promoted to a row-8 prerequisite.**
`lib/trading_calendar.py`'s docstring claims it converged 5+ inline copies **and names `mdpf-daily-trigger`
as one of them** — while that Lambda still carries its own inline calendar at `:96-137`, and
`data/mdpf/scripts/gold/_trading_day_calendar.py` is a third. **The record says converged; the estate has
three copies**, and the trigger that deferred today's build computed its trading-day arithmetic with its own.
CTO took it as its own item. **My module imports the canonical lib and RAISES rather than falling back** — a
convenient private fallback would have been a fourth implementation, and a normalised metric anchored to one
of three competing calendars is a rigorous instrument on the wrong axis. **Row 8's estate-wide
one-definition premise is not yet satisfied; I said so rather than picking a calendar.**

---

## Errors I made

- **I asserted `expected_partners("2026-01-15","value") == ["49financial"]` and my own test failed me.**
  Inflection is EXPECTED from 2024-11-01 at **firm** level; only its MODEL leg starts 2026-05-15. The module
  was right, my expectation was wrong. Flagged explicitly to DS~A because a consumer asking the firm question
  while meaning the model question would read inflection as missing for ~380 dates.
- **I asserted the raw counterfactual spread as 2; it is 1 at partner level and 2 at feed level.** Corrected
  to state both rather than the convenient one.
- **My CWD lingered in `org/mcp/inbox/.../read/` after a `cd`**, so `ls`/`sed`/`grep` reported "No such file"
  for a TO that existed — a **broken retrieval rendering a clean ABSENT**, the exact class CLAUDE.md names
  (control the retrieval, not the pattern). Caught because `comp-glob` and `Read` disagreed with bash. XXX.md
  §1a calls a lingering CWD a defect in itself; it is.

---

## Verification — what I did beyond a green suite

**Mutation-tested, because a suite never mutated has never been tested.** Five mutants of the module, all
caught, then restored:

| Mutant | Result |
|---|---|
| collapse the 3rd state into NOT_YET_ONBOARDED (the `NEVER` defect shape) | 14/17 |
| ignore cadence — raw day counting | 11/17 |
| unknown lag renders as 0 instead of None | 15/17 |
| divergence signal hardwired False | 15/17 |
| partner frontier uses MAX (fastest feed) not MIN | 16/17 |
| restored | **17/17** |

**The metric can fail:** cottonwood D+2 → D+4 moves lag 0→2, spread 0→2, signal false→**true**, while the
other two channels stay byte-identical. **It is a watch, not a gate:** severing channel A leaves B and C
byte-identical. **Unknown is None, never 0** — an unknown rendered as 0 is what lets a frozen channel read
healthy. **The rising-lag limb reports `null` when `prior_lags` is absent** — a check that could not run is
not a check that passed.

**The counterfactual is asserted, not claimed:** on the same live data a raw day-count reads spread 1
(partner) / 2 (feed) — non-zero on a perfectly healthy estate, i.e. the permanently-red signal nobody reads.

---

## Boundaries held

- **Did not touch `data/mdpf/scripts/gold/*`** (Rule 13, DS~A's lane, pre-push enforced). Verified the roster
  JSON is out of Rule-13 scope at source: `safe_deploy_core.file_to_s3_target` requires
  `data/<pipeline>/scripts/<layer>/*.py`.
- **Did not commit to `lib/`** (lane BASE_EXEC). Surfaced at minute 15; CTO ruled option (a) — he does the
  `git mv`. Module written with no path-dependent imports so relocation is pure.
- **Did not push.** **Did not touch CI.** Build-and-verify only.
- **Schema agreed in writing with DS~A before either side built** (their 172911Z ask → my 173252Z contract).

---

## Compiler Tools

| Tool | Command | Result | Value |
|---|---|---|---|
| `comp-which` | `"where is the partner roster with expected cadences..."` | near-tie, routed to `comp-grep` | Correctly declined to guess; surfaced that **"roster" is overloaded** — the hits were SmartX's `fact_model_allocation_roster`, not a partner roster |
| `comp-grep` | `PARTNER_ROSTER\|roster` in `data/mdpf`; `cottonwood`; `trading_calendar` across `data/ infra/ .tools/` | 3–30 hits, denominators printed | Found the literal `partners = {"49financial": bd}` gate **and** the three live trading-day implementations (the promoted finding) |
| `comp-glob` | `**/*roster*`, `**/mdpf*trigger*/**`, `**/*CI-R7R8*` | 1–11 files | Located the TO when bash reported it absent — **the disagreement is what exposed my lingering-CWD defect** |
| `comp-to` | `comp-to MDPF_CHANNEL_INDEPENDENCE.CI-R7R8` | OK | Race-free per-session TO id; every subsequent comp run auto-logged under it |
| `comp-surface-check` | auto via `safe-commit` | PASS — 4 files, no critical surface | Workspace-side advisory; no portal surface touched |
| `comp-pulse` (risk reflex) | auto via `safe-commit` | REFLEX CLEAN | **denominator stated: 4 files vs 1511 danger nodes**, map 5.1h old |
| `.tools/commit-gate.sh` | 2 `.py` files | All checks passed | Rule 14 |
| `.tools/safe-commit.sh` | `-F` body file, `~B` author | `fd6e92faa` | Rule 14a + the `-F`-not-`-m` execution-vector rule |

**`comp-iam` not run:** no new boto3 call is deployed by this commit. `Roster.from_s3` imports boto3 lazily
and is not yet wired into any Lambda; `comp-iam service` + a per-ARN
`simulate-principal-policy` on `s3://opal-data-mdpf/config/partner_roster.json` are owed **at the wiring
commit, not this one** (and per Rule 22a `comp-iam` alone would be insufficient there — it models `(action)`,
never `(action, resource)`).

---

## Open at others

1. **[2.0.0_SA_COO]** push `fd6e92faa`.
2. **[1.0.0_SA_CTO]** gate rows 7+8; `git mv` the module to `lib/mdpf_roster.py`; the trading-calendar
   convergence item (**row 8 prerequisite**); decide whether to build the pluggable layout resolver that would
   upgrade the partner-#4 claim from "any enumerated layout" to unqualified.
3. **[0.4.0_DS_ClientPlatform~A]** consumption path against the landed API; redlines welcome while it is
   committed-not-pushed and a shape change is still cheap.

## Surfaced, not adjudicated

- MEMORY.md records cot `allocations` as having no new data since 07-17. **Measured today:
  `blackdiamond/cottonwood/silver/fact_allocations_s2` is at `date=2026-07-22`** (holdings_s2 likewise).
  Different lane; not chased.
- SmartX feeds (`fact_model_aum_daily`, `fact_model_allocation_roster`) only go back to **2026-07-14** — a
  recent re-source, not the served window. Recorded in the roster's evidence blocks.
- `mdpf-daily-trigger` reads Schwab RPS at `opal-data-bd/schwab/silver/rps` (`date=YYYYMMDD`), while the gold
  producer reads `opal-data-assets/schwab/08242234/silver/fact_rps_s2` (`date=YYYY-MM-DD`). **Two different
  locations and two different layouts for the same nominal feed.** Not investigated — flagging only.
