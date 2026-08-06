# Session 2020–2135Z — P0-4: H3 source census, calendar tie-out, and four things that fail green

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, VALIDATE, COORDINATE

**Agent:** `0.4.0_DS_ClientPlatform~Z` (site Z, first session on this lane)
**TO:** `MDPF_CANRTE.P0-4` @ebaf5700a · **Commit:** `645a8759e` · **Baseline:** SITEZ `73ca92eb3`

---

## 1. Summary

Stood up on site Z, oriented on MDPF_PROPVALIDATION, delivered a read-only import-surface artifact
that changed three TO scopes, then took P0-4 on GO and closed criteria **5, 6, and 9**. The graph
criterion (1) is correctly **NOT-STARTED-PENDING-CAPTURE**.

The through-line: **four separate constructs in this pipeline degrade silently instead of failing**,
and the one construct that fails loudly is the one a reviewer would be tempted to soften.

---

## 2. Deliverables

| What | Where | State |
|---|---|---|
| Import surface + dependency closure | MCP to COO~Z 203704Z | accepted in full; changed 3 TO scopes |
| H3 source census + provisional disposition | `deliverables/MDPF_H3_SOURCE_CENSUS_20260806.md` | `645a8759e` |
| Calendar tie-out (exercised + mutant) | `deliverables/MDPF_CALENDAR_TIEOUT_20260806.md` | `645a8759e` |
| Cottonwood L2 producer located | MCP 205137Z | criterion 5 CLOSED, accepted |
| `.crosswalk_cache.pkl` disposition | MCP 213150Z | (c) STALE + named falsifier, accepted |
| Roster/Phase-2 conflict | MCP 213220Z → converged 213428Z | routed to CTO~Z, ruling pending |

---

## 3. The fail-green pattern — four instances, one house style

| # | Construct | What absence does | Raises? |
|---|---|---|---|
| 1 | `pandas_market_calendars` under `try/except ImportError` (`_trading_day_calendar.py:37-43`) | falls back to a holiday set ending 2026-12-31; from 2027-01-01 every weekday reads as a trading day | **no** |
| 2 | `partner_held_etf` feeder via `_empty_feeder()` (`mdpf_aggregate_aua.py:217`) | reverts `identity_2` from a measurement to an estimate the docstring records as **~1-3% high** | **no** |
| 3 | `comp-pipescript consumers` on a runtime-composed key | reports "no downstream consumers" for a live, required dependency | **no** |
| 4 | doc 02's prescribed import-health check | passes **because** the fallback engaged | **no** |

**(4) is the sharpest: the prescribed remedy for (1) cannot fail in the state it exists to detect.**
That is an anti-control, not a weak one — the same anti-correlated shape as the orphan-watcher
`REACHABLE` verdict.

**The counterweight, and it matters:** `_load_partner_roster()` (`:1718-1747`) is **fail-closed** —
`SystemExit` naming both candidate paths, and its error message literally says *"Do NOT add another
resolution mechanism here."* The estate is **not** uniformly fail-green. Requested and got this as an
explicit P1-1 `do_not`: **adding a graceful fallback is exactly the change that reads as an
improvement in review.**

*The pattern worth carrying: the fail-green constructs advertise nothing; the fail-closed one shouts
in its error string. The quiet ones are dangerous, and the loud one is the one people soften.*

---

## 4. Findings that changed scope

**Cottonwood is not built in the spine.** `build_mdpf_spine.py:88-112` emits pre-staged S3 **bytes
verbatim**; the real producer is `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:945` — a
**different repo tree**, a family of three, with a real ordering constraint. It was the gating unknown
on P1-1's size.

**The coupling runs both ways, on a private symbol.** `build_cottonwood_mdpf_pair.py:64-65` imports
`_distribution_stats` (private) and `calc_metric`/`quarter_ends` **out of** the MDPF tree. A refactor
there breaks Cottonwood across a tree boundary with no import-side signal in the MDPF tree.

**The closure is 53% larger than the pack scoped** — 14 modules / 9,442 lines over three directories
vs 7 / 6,158, including a **silver**-tier module imported into gold.

**"Firm-parameterized" is false in the incumbent** (three shapes; inflection consumes 49f's axis) and
**channel independence does not hold** (`build_global_artifact(arts["49financial"], …)` is a direct
subscript). Both are work to ADD — so equivalence-vs-incumbent and channel-independence are
**opposite** batteries and cannot be one suite.

**A measured flat-zip break.** `build_dim_model_portfolio.py:66` derives a sibling dir by splitting
its own `__file__` on `"scripts"`; at `/var/task` there is no such segment, `sys.path.insert` does not
raise, and via the slice the import is function-scoped (`:350`) — so it waits for the Cottonwood leg.
Mine to fix in P1-1.

---

## 5. Two instrument corrections I made to my own work

- **pyarrow.** I reported "zero direct imports" — true of the MDPF tree, which was my closure at the
  time; false once Cottonwood was in it (`slice:81`, `build_dim_model_portfolio:43-44`). Restated scoped.
- **`rebalancer_schemas`.** My own closure tool called it third-party purely because it sat outside
  the two directories searched. It is local. **A closure tool reports "third-party" for anything it
  cannot find, so an unresolved LOCAL module and a real pip package produce identical output.**

And one correction I **accepted** from AE~Z: I framed *"NEVER a vendored copy"* as categorical, which
would condemn the current production path — the same docstring sanctions the runner's synced copy two
lines earlier. Their **drift-capable vs tied** distinction makes the docstring internally consistent;
mine did not. Conclusion unchanged, basis now sound.

---

## 6. Compiler Tools

**Every row carries its denominator. A retrieval that returned zero carries its positive control.**

| Tool | Result | Denominator / control |
|---|---|---|
| `comp-which "what reads the mdpf feeder outputs…"` | near-tie, 3 candidates surfaced | 75 tools ranked; routed correctly, no silent guess |
| `comp-glob **/build_mdpf_spine.py` etc. | located spine + aggregate modules | 1 file each, systems-context printed |
| `comp-glob **/rebalancer_schemas.py` | 2 hits → resolved LOCAL | corrected a third-party misclassification |
| `comp-grep "mdpf_revamp/cottonwood"` | located the L2 producer family | multi-file, tool printed scan scope |
| `comp-grep "crosswalk_cache"` | 24 matches / 15 files, **all logs or TOs, zero executable refs** | **21,247 of 22,979 files scanned** |
| `comp-grep "pandas-market-calendars"` | 0 hits | 21,226 of 22,958 scanned; tool printed its own "NOT a confirmation of absence" caveat |
| `comp-pipescript consumers wsb_49f_smartx_model_aua --pipeline mdpf` | **"no downstream consumers" — FALSE ZERO** | contradicted by `mdpf_aggregate_aua.py:239-268`; mechanism established |
| `comp-pipescript consumers <artifact key>` | **rc=2 REFUSED** | verb takes a SCRIPT name, not a key — mandate/interface gap, reported |
| AST import closure (own, scratchpad) | 14 modules, **0 unresolved** | 10 entrypoints, 14 files parsed, 124 edges |
| calendar tie-out (own, scratchpad) | in-window equal; falsifier fired; 2027 divergent | **1096 dates** / 0 diffs · mutant → 1 diff localized · **365 dates** / 10 diffs |
| literal-key control | reader has **0** occurrences of the composite key | **control: `FEEDER_PREFIX` = 3** in the same file, same command |
| `git log` on the pickle path | empty (never tracked) | **control: same form on `mdpf_revamp_model_crosswalk.py` returned history** |
| basename collision check | 0 duplicates | **45 files**; control fed a synthetic duplicate and it printed |
| `safe-commit.sh` | PASS, risk-reflex CLEAN | **3 files vs 1662 danger nodes**, map 6.4h old |
| `.tools/to-check.py --all --assignee` | 0 active TOs at start | workspace-wide scope |

**What worked:** forcing `_USE_PMC=False` before comparing calendars. Asking *"could this test have
failed?"* found that on any machine with pmc installed it structurally could not — both modules would
defer to pmc and agree for a reason unrelated to the sets the ruling turns on.

**What failed:** `comp-pipescript consumers` returned a false zero on two live producers.
**Mechanism established** (not merely observed): both sides compose the S3 key by f-string from a dict
key, so no literal exists for a static extractor. **For this pipeline a zero-consumer result is the
expected output for a whole class of real dependency.**

**Gaps found + routed:** (i) mandate says `consumers <artifact key>`, the verb takes a script name;
(ii) `build_mdpf_etf_ownership_timeseries.py` docstring `:21` names `opal-data-portal-v2` while its
constant `:75` says `opal-data-assets` — the constant executes, and the Aug-6 live failure corroborates.

---

## 7. Scope held

H10 **not** closed — every absence says *"no source-visible reader"*, no reserved word on any absence
claim. Other pipelines' vendored calendar copies untouched. Nothing deleted. Criterion 1 **not**
claimed from repo source. Two questions routed rather than adjudicated (calendar scope over the
Cottonwood family; roster read vs CTO 230319Z).

## 8. Next

- **Blocked-by-design:** criterion 1 graph → AE~Z's P0-7 enumeration at the chain's own ~09:00 ET
  start. Will triangulate repo-closure vs captured-closure vs CVO~Z's declared 33.
- **Blocked on ruling:** P1-1 → CTO~Z on the roster read (the choice sits inside the module I refactor).
- **Owed on capture:** the `.crosswalk_cache.pkl` falsifier — AE~Z reports the outcome against my reason.
- **Mine in P1-1:** the `build_dim_model_portfolio.py:66` path-split break.
