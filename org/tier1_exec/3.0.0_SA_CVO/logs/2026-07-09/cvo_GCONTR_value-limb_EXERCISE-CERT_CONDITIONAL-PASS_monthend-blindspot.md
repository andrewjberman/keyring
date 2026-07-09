# CVO exercise-cert — NFRA_GCONTR value-limb (TO-3 item 3): CONDITIONAL PASS

**archetype:** VALIDATE

**Date:** 2026-07-09 ~18:05-18:35Z · **Agent:** 3.0.0_SA_CVO · **TO:** NFRA_GCONTR.TO-3
**Subject:** the CVO-owned `period_defs` value-check, driven from AUTHORED to EXERCISED.
**Verdict:** **CONDITIONAL PASS.** Logic correct and specific; detection power is as-of dependent and
is ZERO for `1M` and `1Q` at the current served vintage. Value-limb **NOT closeable** until the
check reads honestly at a period-end as-of. (COO ratified this as the acceptance criterion, 182023Z.)

---

## What was exercised

Prior-me committed `contracts/value_check_benchmark_period_defs.py` (`0cbcee240`) and reported it
AUTHORED-pending-exercise. Authored != proven. This is the exercise.

The negative control is the point: inject the actual BMKAUD violation semantic
(1M = last-complete-calendar-month, the reverted SmartX override) into served and require exit 2.

| # | condition | expected | ACTUAL | reads |
|---|---|---|---|---|
| LIVE | current served vs vintage-matched PKL | 0 | **0** | 250/250 cells reproduce |
| B1 | mid-month as-of, canonical served | 0 | **0** | no false alarm |
| B2 | mid-month as-of, BMKAUD 1M injected | 2 | **2** | 1M-only, all 5 models, tagged |
| **A** | **month-end as-of, BMKAUD 1M injected** | **2** | **0 — BLIND** | reported "VALUE-LIMB CLEAN" |

**Replay A is the finding.** At as-of 2026-06-30 the canonical trailing-30-day window
`(05-31, 06-30]` and the last-complete-calendar-month window `[06-01, 06-30]` are the SAME set of
trading days. Measured delta = **0.0000 on all five models**. The violation is numerically
indistinguishable from canonical, so the check cannot see it. At a mid-month as-of the same injection
diverges 0.16–0.57pp and fires cleanly.

`1Q` is blind at the same as-of for the same reason: 2026-06-30 is a quarter-end and Q2 spans exactly
91 days (30+31+30), so `(03-31, 06-30]` == Q2. Measured delta **0.0000** on all five models.

So both rolling windows the BMKAUD incident concerned — and the only two Andrew ruled on — are
undiscriminating at the exact vintage now being served. Today's "CLEAN" was TRUE but WEAK. Rendering
weak-clean as CLEAN is the silent-wrongness class.

## Findings

**P1 — SEV1 contract row declares the semantic Andrew did NOT rule.** `contracts/graph_contracts.yaml:56`
(benchmark, SEV1, Andrew-signed) and `:196` (peers, SEV2) declare `1M: "trailing-1-calendar-month"` /
`1Q: "trailing-3-calendar-months"`. Methodology-of-record is **trailing 30 / 91 calendar days**
(`lambda_function.py:445-455`, `:475-483`; Andrew ruling 2026-06-01, directive `631d8d0d9`). The WS-3
brief enumerated these as competing options (a) vs (b), warned at `:34` they "coincide now but will
drift", and offered `relativedelta(months=1)` at `:68` as the (b) implementation. **Andrew ruled (a);
the row declares (b).** No served number is wrong today; the risk is forward — the contract is the
enforced invariant, so an implementer honoring it would swap in `relativedelta` and silently break the
ruling. Prior-me's authoring error. Not self-edited (ratified SEV1 row, PRD §9) — routed for a single
consolidated Andrew sign-off. COO **pulled GCONTR from the sovereign queue** on this finding.

**P2 — `benchmarks/LATEST.json` is a dangling pointer.** It names `data_20260701_v2.pkl` and
`model_20260701_v2.pkl`; both **404** on `head-object`. Real object is `_v1`. The producer's
`get_latest_data_pkl_key()` reads exactly this field, so any invocation not carrying a key in the event
cannot resolve. ESTABLISHED: pointer dangling, fallback path cannot resolve. **INFERRED, not
established:** that a scheduled rule invokes this path and is currently failing — I did not confirm the
rule exists. Distinct from the prior `files.data_pkl` shape bug
(`docs/briefs/ae-brief-yang-benchmarks-si-unannualize.md`). Routed by COO to the yang_pkl owner.

**Not a defect claim:** served is vintage-consistent with its source (both 07-01). The source PKL
cadence has produced nothing since 07-01 (8d). Worth an upstream look on a SEV1 surface; nothing is
provably broken and I assert nothing.

## Defects fixed in my own deliverable (all mine, my folder)

1. **Source selection was wrong three ways.** `_latest_pkl` did `sorted(...)[-1]` over `*_v1.pkl`:
   picked `model_20260701_v1.pkl` (`m` > `d`) — the wrong artifact entirely — and filtered to `_v1`,
   so it could never see the canonical pointer, which names `_v2`. Replaced with producer-parity
   resolution: read `LATEST.json` → `data_pkl`, verify it exists, else LOUD-warn and fall back to the
   newest **`data_`**-prefixed pkl.
2. **No vintage gate.** A served/PKL vintage mismatch would have emitted a wall of false violations.
   Now returns **exit 3 VINTAGE-SKEW** — undecidable, not a breach.
3. **Silent weak-clean.** Now measures detection power per rolling window and returns **exit 4
   CLEAN-BUT-UNDISCRIMINATING** when the canonical and violation windows coincide. Never "CLEAN".
4. **The default S3 path had never run.** `subprocess.run(["aws", ...])` raises `WinError 2` on this
   host (`aws` resolves to `aws.CMD`). Every prior invocation used local fixtures, so the entire
   S3-resolution path was dead code at authoring time. Resolved via `shutil.which`.

Defect 4 is the one worth banking: **a script whose only exercised path is the fixture path has not
been exercised.** The live-source limb was untested precisely because testing it was inconvenient.

## Post-fix re-exercise (all six, real exit codes)

| # | condition | expected | ACTUAL |
|---|---|---|---|
| 1 | LIVE, month-end as-of | 4 | **4** UNDISCRIMINATING (1M + 1Q, delta 0.0000) |
| 2 | month-end + BMKAUD injected | 4 | **4** — still blind (physics), but LOUD, not CLEAN |
| 3 | mid-month canonical | 0 | **0** — 1M delta 1.62, 1Q delta 13.56, both DISCRIMINATING |
| 4 | mid-month + BMKAUD injected | 2 | **2** VIOLATION, BMKAUD-SIGNATURE tagged |
| 5 | mid-month PKL vs month-end served | 3 | **3** VINTAGE-SKEW (no false violations) |
| 6 | default live-S3 resolution | warn+run | **4**, dangling pointer independently re-detected |

Run 2 is the honest core: the check still cannot *see* the violation at a coinciding as-of — that is
arithmetic, not a bug — but it now **declares its own blindness** instead of certifying clean.

## grounding

- **desired:** `pipescript --resource yang-model-portfolio-benchmarks` → `model-portfolios /
  yang-benchmarks-etf-returns [in-scope | globgrph]`; `comp-which` routed the trigger question.
- **applied:** `s3api head-object` — served `2026-07-01T16:31:34Z`, `data_as_of 2026-06-30`;
  `data_20260701_v2.pkl` **404**, `data_20260701_v1.pkl` present (`16:29:35 GMT`); PKL `return_daily`
  Term max date `2026-06-30` = vintage-matched.
- **exercised:** 10 real runs of the check (4 pre-fix, 6 post-fix), exit codes as tabled; plus two
  independent probes measuring canonical-vs-violation deltas at month-end (0.0000) and mid-month
  (0.16–0.57pp), and at quarter-end for 1Q (0.0000).
- **source-confirmed (mechanism):** `lambda_function.py:445-455` (1M = `end_date - timedelta(days=30)`),
  `:475-483` (1Q = 91d), `get_latest_data_pkl_key` → `LATEST.json.data_pkl`, `load_pkl` → `get_object`.

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-which "what triggers the yang-model-portfolio-benchmarks lambda…"` | find the trigger/schedule surface | near-tie routed to `comp-aws` / `comp-iam service` / `pipescript --resource`; ran the third |
| `comp-aws --resource <fn>` | attempt trigger lookup | **GAP:** `comp-aws` takes no `--resource`; subcommands only (`derive/score/snapshot/…`). `comp-which` routed to a call the tool does not accept. |
| `pipescript --resource yang-model-portfolio-benchmarks` | estate traversal for the producer | 1 thread: `model-portfolios / yang-benchmarks-etf-returns [in-scope \| globgrph]`. Did **not** surface an EventBridge schedule — which is why the "scheduled refresh is failing" claim stays INFERRED. |
| `comp-grep "LATEST.json"` | locate the pointer's writer | `yang-generate-latest` Lambda, Step Functions (`data/yang_pkl`) |

**Coverage gap to route (CTO/COO):** `comp-which` recommended `comp-aws --resource <fn>`, an invocation
`comp-aws` rejects. Either `comp-which`'s route table is stale or `comp-aws` should accept a resource
selector. Second: no comp-tool answered "what triggers this Lambda / is it scheduled" — `pipescript`
gives producer→served lineage but not the EventBridge trigger. That gap is exactly why the P2 causal
claim had to stay bounded as INFERRED rather than source-confirmed.

## What you should have asked but did not

**Does this check validate the contract, or only the producer?** It reproduces served from source via
the **deployed transform**. That proves *producer-fidelity*: served == what the code computes. It does
**not** prove *contract-fidelity*: that the code implements the **declared** `period_defs`. Those are
different claims, and today they visibly disagree — the transform does trailing-30d, the row says
trailing-1-calendar-month, and the check passes anyway. So the value-limb as designed would report
CLEAN on a surface whose contract is being violated by the canonical producer itself. It catches the
BMKAUD incident class (a *foreign writer* overwriting served) and is blind to a *canonical transform*
drifting off its own contract. Closing the P1 row-correction makes the two agree today; it does not
close the structural gap. A real contract-fidelity assertion would have to parse `period_defs` and
check the transform against it — that is a different, larger check, and it should be a named PRD item
rather than something quietly assumed to already exist.

— 3.0.0_SA_CVO
