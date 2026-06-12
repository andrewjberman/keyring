# Session log — 0.4.0_DS_ClientPlatform — 2026-06-12 (~1330Z–1350Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform (Tier-2 worker, event-driven)
**Drivers/gates:** 2.0.0_SA_COO (GO + RAVC2 close); 1.0.0_SA_CTO (arch-ruling 230400Z + CENSUS-XT adjudication 0e745d9ed convergence oracle); 0.6.0_AE_PartnerETL (sibling CENSUS-XT detector — hit-list convergence).
**Theme:** Built the ADHC_GLDINC.AST-DEDUP CLASS-N detector (the commit-time net for the A_01/A_04 nondeterministic-survivor class), validated to the hard bar, and converged its Phase-3 hit-list against AE's CENSUS-XT + CTO's adjudication.

---

## 1. Startup + reachability
Fresh session: re-registered LIVE (PID 13428), armed persistent inbox Monitor (task b5vnj9r47). org/XXX.md setup (session-serial file, owned-paths hook present, headmove guard, comp-graph context). Read prior log (1930Z 2026-06-11), prompt, the GO + TO. Inbox: 1 GO (COO, AST-DEDUP). Checked in w/ COO (ACK'd).

## 2. ADHC_GLDINC.AST-DEDUP — CLASS-N detector (COMPLETE, ab0cd8ba0)
New `check_completion_order_dedup()` in `.tools/ds-precommit-check.py`. Per-function-scope, fires ONLY on the 3-part CONJUNCTION (the parallel-load ASSEMBLY shape per CTO 230400Z, not the dedup):
1. a list `.append()/.extend()`'d inside `for x in as_completed(...)`/`imap_unordered` loop;
2. that container `pd.concat()/pd.DataFrame()`'d into a frame — **the data-flow link** (load-bearing);
3. that frame `.drop_duplicates()` order-sensitively (keep last/first or default) NOT chained off `.sort_values()`.
Index-slot (`results[i]=...`) + sort-guarded dedup stay silent.

**The data-flow link was the key design iteration.** A first predicate (same-function conjunction, no data-flow) fired 3 FPs on the live bd gold tree — C_02 `load_tax_status_split`/`load_holdings_counts` (dedup on an UNRELATED `accts` lookup dim) + C_01 `main` (dedup textually BEFORE the build). Requiring the dedup'd frame to derive (via concat) from the completion-order container eliminated all 3 with no loss of fixture coverage.

**SEVERITY = WARN-first** (advisory, rc-neutral; one-line `_ASTDEDUP_SEVERITY` ramp knob). Documented in commit + the config comment. Rationale: fabric-shared checker + new heuristic; 0-FP on live bd gold BUT genuine unfixed CLASS-N findings exist (below) → ERROR now would freeze those lanes before adjudication. Promote to ERROR after findings fixed + cross-tree 0-FP re-confirmed. Mirrors the D6 comp-manifest-check advisory→blocking ramp. Path-scoped to `data/*/scripts/{gold,silver,bronze}/*.py`.

**Durable regression:** `test_ds_precommit_check.py` +4 cases (1 FIRE + 3 SILENT: index-slot, sort-guarded, unrelated-dedup) over 4 new fixtures in `test_fixtures/ds-precommit-check/`. Full suite 7/7 PASS.

## 3. Phase-3 cross-tree sweep + convergence (211 files, 0 FP, 3 CLASS-N)
Swept bd/cot/inf × gold/silver/bronze. Findings: **cot A_01, cot A_04, bd silver compact-realized** (0 bd-gold FP).

Reconciled vs AE CENSUS-XT (315c8fab6, CLASS-N=4: cot A_01/A_02/A_04 + inf D_06) and CTO adjudication (0e745d9ed: 2 FIX cot A_01/A_04, 2 BENIGN cot A_02-conditional/inf D_06). **CTO's convergence oracle PASSES exactly:**
- 2 FIX (cot A_01 @L192, cot A_04 @L120) → my rule FIRES both. ✓
- bd A_01/A_04 post-fix → my rule SILENT (CTO "must NOT flag"). ✓
- cot A_02 → SILENT, AGREES w/ BENIGN. Reason encodes the discriminator: append in `load_*()` (concat returned undeduped) vs keep='last' dedup in a DIFFERENT function, `sort_values('trade_date')`-guarded, on a per-account arg → fails same-scope + data-flow + sort-guard. More precise than the whole-file shape census.
- inf D_06 → SILENT, AGREES w/ BENIGN. The L383 dedup is on a LIST-LITERAL frame with the payload in the dedup key (byte-identical dups); the as_completed concat is aggregated not dedup'd.
- **NET-NEW: bd silver compact-realized:94** — genuine same-function unguarded CLASS-N, outside the census scope (inf+cot gold + bd C/D; didn't scan silver). Routed to CTO for ruling.

**Known precision boundaries (flagged to CTO):** (1) cot A_02 reopen-condition (differing-payload same-day fee ties) is a DATA-level check my static AST rule cannot evaluate — needs an empirical pass; (2) `pool.add_done_callback` append not detected (no live instance found).

---

## Compiler Tools
| Tool / run | Where | Result |
|---|---|---|
| custom detector harness (`.runtmp/astdedup_fixtures/detector.py`) | iterate predicate vs fixtures + full bd tree | calibrated the data-flow link to kill 3 same-function-conjunction FPs (C_02 x2, C_01) while keeping 2/2 fixtures. |
| `python ds-precommit-check.py` (integrated) | 2 fixtures (scope-hint) | 2/2 FIRE (A_01 L192, A_04 L120). PASS. |
| `python ds-precommit-check.py` | live bd gold (67) | 0 AST-DEDUP findings. 0 FP. PASS. |
| `python ds-precommit-check.py` | bd/cot/inf gold+silver+bronze (211) | 3 CLASS-N (cot A_01, cot A_04, bd silver compact-realized); rc=1 on cot/some-bd from PRE-EXISTING future-annot gate (ADHC_DSFLOW.004), NOT AST-DEDUP — confirmed AST-DEDUP is WARN/rc-neutral. |
| `test_ds_precommit_check.py` | 7 cases | 7/7 PASS (incl. 4 new AST-DEDUP cases). |
| `ds-commit-gate.sh` | 6 changed files | rc=0 (py_compile + AST undefined-name + ruff py39 + manifest-check advisory). |
| `safe-deploy` (pre-push) | push | "no deploy-scope script files" — tooling-only, correct no-op. |

## Commits this session
`ab0cd8ba0` — AST-DEDUP rule + test runner +4 fixtures (6 files, pushed CLOUD). Plus TO status flip + this log.

## Open / event-driven (none DS-committable now)
- **CTO:** benign/non-benign ruling on the net-new bd silver compact-realized CLASS-N; consolidated fix-decomp for the 2 FIX (cot A_01/A_04) + compact-realized.
- **AST-DEDUP ERROR-promotion:** gated on the live findings being fixed + a cross-tree 0-FP re-confirm (one-line `_ASTDEDUP_SEVERITY` flip).
- **D6 advisory→blocking ramp:** event-driven, CTO calls it (~10 clean tally commits + joint B/C precision review).
- **GLDINC cutovers:** AM scorecard review → per-script cutover on clean-nights + Andrew nod (COO attests night-1 ALL-GREEN).
