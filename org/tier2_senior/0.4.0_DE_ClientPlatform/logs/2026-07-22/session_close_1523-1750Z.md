# Phase 0 two-firm enumeration (delivered + 10 amendments), Cottonwood render by exercise, the FE fork pattern + workstream spec, D6 closed

**archetype:** MIXED
**secondary_archetypes:** EXPLORE, VALIDATE, DIAGNOSE, COORDINATE, SCRIBE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-07-22 (1523Z-1750Z) · **TO:** WSE_COTMDL / MDPF Phase 0 (CTO carve-out 3)
**Window:** re-instantiation (fresh session, predecessor PID 16984 confirmed dead) -> now. Prior log `session_close_0025-0640Z.md`; predecessor handoff `9ee995d2f`.

## Summary
Re-instantiated into a HOLD and found the advisory had already landed while the handoff was being written. Executed **Phase 0 — the two-firm enumeration** (CTO carve-out 3, "enumerating is not initiating"), delivered it, then **amended it ten times as it was corrected — four times by my own hand.** Ran the Cottonwood render and **confirmed the FE blank-charts defect by exercise with a discriminating control.** Mapped the Inflection FE fork as the template and landed the **FE workstream spec** on Andrew's word. Andrew then **closed D6 across three rulings**, striking the largest work set. Finished by relaying his BD total-AUA directive to DS with a grounded proposal — **whose headline blocker DS then correctly inverted.**

**The distinguishing feature of this session is the correction count, not the delivery count.** Phase 0 was delivered at `0aa0f2200` and was wrong or incomplete in ten identified ways afterwards. Every one is recorded in place rather than polished out.

## Work done (the arc)
1. **Startup + hold resolution.** `/watcher`, LD-0290 serial file, register (PID 28540). Broker read LIVE at PID 16984; **process truth said dead** -> genuine predecessor death, no orphan, no peer conflict. Inbox: COO's cascade splitting my lane — WS-4 re-home HELD, **carve-out 3 (the enumeration) AUTHORIZED by CTO**, merge-vs-add reserved to Andrew.
2. **Phase 0 census (`0aa0f2200`).** Four read-only limbs (producers / publisher-promote / infra dispatch+IAM / portal FE) plus `0.7.0_AE_CloudOps`'s independent infra limb. **Reported the exit condition NOT met** — shape closed, list not. CTO adopted that line.
3. **Three plan-correcting findings.** (a) **MDPF is the laggard, not the frontier** — 3-firm canonical tuples already run in production siblings (`etfs-canon-fanin:47`, `opal-assets-daily-emitter:696`), both verified by me at HEAD. (b) **The reframe: this is FIRMSEP.11**, a content-layer phase Andrew deferred 2026-05-07 and never given a TO; the "skeleton" playbook CTO's plan cited **does not exist** (positive-controlled). (c) **A forced ordering, measured:** no `cottonwood/` prefix under `gold/mdpf_revamp/`, so the audit tripwire is armed-not-tripped — the audit leg must land in the SAME change as the staging loops.
4. **Cottonwood render (`c95210ec3`) — the decisive instrument.** Pinned an external Cottonwood advisor session **entirely through the fixtures file** (`ui-smoke.mjs:79-81` checks fixtures before the auth stub) = zero source edits. **S-9 confirmed and worse than predicted:** a non-canonical model key renders **BOTH trend charts completely blank** while the legend names the models and the donut draws them. **Discriminating control:** byte-identical fixture with canonical keys renders 4 stacked bars + full area. Also confirmed the colour-fallback collapse, the un-fixed methodology twin, and the AUA/AUM label contradiction — **and confirmed the honest-None footer fix WORKS.**
5. **Read fraction closed on Andrew's direct order (`b6d9b299d`).** `dim_mdpf_aggregate_aua_timeseries.py` **10% -> 1453/1453**. Three results: the file is **three layers and only the orchestration is two-firm** (helpers/gates already N-firm, `SOURCE_PROVENANCE` already carries `blackdiamond`); **S-6 downgraded** (no axis master/follower topology exists); and **`GLOBAL_MODEL_KEYS` is the producer twin of the FE `STACK_SERIES` defect** — same shape at opposite ends, neither errors, fixing one alone still yields an invisible Cottonwood.
6. **FE fork pattern (`b0cad1965`, `108f8156c`) + workstream spec (`3bbdddbd1`).** Used the tools Andrew named. Established the fork is **four layers, with 1-3 already built for Cottonwood** and the gap at layer 4; `MdpfFirmId` blast radius = **1 file**. Landed the spec as decomposable units with acceptance criteria for COO.
7. **Andrew closed D6 (3 rulings, `3b311c044` + `ae9f7f03b`).** Conservative Growth **MERGES to LTC**; Income is **not a model** (non-model, not tracked); day one uses **canonical names** (overruling my recommendation). **Set B struck** — no non-canonical key will exist, so the render-confirmed defect cannot fire. Flagged the consequences: the merge **moves $30.99M into the canonical LTC series** (needs a named delta), and the exclusion must be **enumerated** (`KNOWN_EXCLUDED_ECLIPSE_IDS` pattern), never a loosened raise.
8. **BD total-AUA directive relayed to DS under Andrew's command.** Read the 0824 mechanism at source, measured Cottonwood's `fact_holdings` (**$458,114,003.10** @2026-07-20), proposed the analog, and named five things deciding correct-vs-plausible.

## Corrections I issued on myself (four), and three issued on me
**MINE:**
- **D3 OVERSTATED (`91e3120a6`).** I reported the conservation identity as "arithmetically false with a third firm — the single most expensive item." **Reading the arithmetic reversed it:** `non_model` is 49F-only under basis B, so `(m49+minf+mcot) + nm49` balances by construction, and the leg pins are non-model pins that a firm with null non-model cannot falsify. **D3 removed from the decision table.** Root cause: a limb **grepped** the file and reasoned from the docstring.
- **POPULATION-A FRACTION OVERSTATED (`2307956f3`).** CVO's A11 added an ALIAS axis; I ran it against my own finished work and found **3 of my 4 limbs never searched `bd`**. Marked overstated rather than restated.
- **3 OF 4 FRACTIONS FAIL 7f (`64c3ed4b1`).** Only the READ fraction's denominator comes from outside my own instrument's configuration. A, C, D are **leads, not clearance** — sent to COO, whose decomposition it invalidates.
- **VINTAGE: CITATIONS WITH NO COMMIT ANCHOR (`0b20e3aa9`).** Two structural findings cited `mdpf-daily-dispatch.sh` **working-tree** code absent at HEAD — including a **CTO-approved governance prohibition (134926Z) I routed to two Tier-1 lanes as binding law.** It exists in no commit. Retracted.
- **FALSE-ALARM INSTRUMENT DEFECT (`93dd76ef8`).** Ran `pd.to_numeric()` over a boolean flag column and reported "`Cash Equivalent` 0/16,762 non-null — cash cannot be identified," handing DS a settle-before-derive blocker. **It is 16,762/16,762 populated; cash is 3.33% and already in the base.** DS inverted it; I verified the inversion myself.

**ON ME (folded, credited):** `0.7.0` supplied the **unnamed-arity** and **absence** axes (and proved Phase 1a is IAM-blocked, `implicitDeny`, positive control in a separate invocation); COO bounded the absence axis with the **key-space** rule; DS corrected both the cash measurement and my *framing* — the 0824 `.fillna(0.0)` **has never fired**, so "mirror the shape" is wrong; **mirror the identity, re-decide the nulls.**

## Files Modified / Commits
See commit messages: `0aa0f2200`, `eba3f57c9`, `c95210ec3`, `91e3120a6`, `54f528fbf`, `2307956f3`, `54ab7c983`, `66b07fe3c`, `64c3ed4b1`, `b6d9b299d`, `b0cad1965`, `108f8156c`, `3bbdddbd1`, `0b20e3aa9`, `3b311c044`, `ae9f7f03b`, `93dd76ef8` (17). **Zero production code changed. Zero applies, publishes, ETag moves, producer runs.** Portal tracked tree clean at `08c6d8b2` throughout.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `comp-which` | PASS | routed the TS/data-flow question to comp-platinum / comp-cluster / comp-types (Andrew-directed) |
| `comp-cache key mdpf` / `map` | PASS | found all 3 MDPF keys AND **states its own denominator** (104/104 useQuery sites, names `useQueries` as unaudited) — the best-behaved instrument used today |
| `comp-types blast` / `fields` | PASS | `MdpfFirmId` blast radius = 1 file; `MdpfPerFirmTimeSeries` = 19 fields, 7 UNUSED by the FE |
| `comp-platinum page --firm inf\|cot` | **PARTIAL / GAP** | traces byte-identical except the bucket line, and enumerates **2 of 5+ fetches** — misses every MDPF per-firm query. Its "no firm delta" is an **instrument limit, not a finding**; not reported as one |
| `comp-cluster ModelPortfolios` | PARTIAL | timed out >120s (Kuzu rebuild), completed in background; 118/119 tree, 0 silent — but clustered **only** the peers subtree, not the MDPF panels |
| `ui-smoke.mjs` + discriminating control | **PASS (decisive)** | the only instrument that found the FE defects; fixture-pinned session, zero source edits |
| `aws s3 ls` / `s3api` / `s3 cp` (rail-checked) | PASS | retrieval control caught a broken listing returning `None` while `head-object` succeeded on a known key |
| `git show HEAD:<path>` | PASS | the check that caught the no-commit-anchor citations; **none of my four limbs ran it** |
| `safe-commit` surface-check + risk-reflex | PASS x17 | narrow single-file pathspecs throughout (COO's shared-worktree hazard) |

**What worked:** running new axes against my own finished work rather than noting them for the next person; the discriminating control on the render; `git show HEAD:` as a vintage check. **What failed:** five of my own claims ran past what I had verified — each caught, retracted, recorded in place. **Gap found:** `comp-platinum`'s page-trace fetch enumeration is incomplete for MDPF; `Glob`/`comp-glob` is CASE-SENSITIVE (retroactive doubt on prior Glob-based clears); `comp-grep -l` truncates silently at `--max`. All three answer "nothing found" when the honest answer is "I cannot see that kind of thing."

## Blockers
**None on my side.** External gates: Andrew's resumption path (CVO verify 4-of-12 -> COO decomposition -> dispatch); Phase 1a is **IAM-blocked** (`AssetsRevampSilverRead` omits `blackdiamond/cottonwood/silver/*`; desired+applied AGREE = never built, exercised `implicitDeny`) — CTO to sequence.

## Current State
- **HELD, and nothing started:** WS-4 re-home, fold, pin, publish, ETag move, serve-path apply. Nothing half-landed; NEVER#5 not engaged.
- **Deliverables (all pushed):** `MDPF_PHASE0_TWO_FIRM_ENUMERATION_20260722.md` @`93dd76ef8` (census + 10 amendments) · `mdpf_cottonwood_render_20260722/` @`c95210ec3` (2 PNGs + both fixtures, reproducible control) · `MDPF_FE_FORK_PATTERN_INFLECTION_TO_COTTONWOOD_20260722.md` @`108f8156c` · `WSE_COTMDL_FE_WORKSTREAM_SPEC_20260722.md` @`ae9f7f03b`.
- **FE workstream after D6:** **Set A** (A1 methodology caption `:1422`; A2 `lastNonNull` `:617`/`:968` — **a DECISION needing CTO ack, not a cleanup**; A3 `AUMGrowthMetrics.tsx:87` AUA/AUM) **+ C1** (exhaustive-by-type — the only item that pays forward to firm four). **Set B STRUCK.**
- **Dispatch-file hazard CLOSED:** Andrew ordered it resolved; routed to DS as owner (I captured the patch first, sha `6145935b`, so revert was non-destructive); **DS reverted, three-way verified.**
- **Census methodology, for anyone quoting a number from it:** FOUR encoding axes (token / arity / absence / alias), each discovered by a FAILURE not a review, so the list is treated as OPEN. **Only the READ fraction is evidence.**

## Next Steps
- **[1.0.0_SA_CTO]** sequence the Phase-1a IAM statements (two additive); confirm A2's `lastNonNull` widening; note S-4's governance lock has **no commit anchor** — do not carry it as landed law.
- **[2.0.0_SA_COO]** decompose Set A + C1 when the gate clears; Set B struck; quote the READ fraction only.
- **[0.4.0_DS_ClientPlatform]** BD total-AUA proposal @`0ecf2139b`; largest remaining risk is my #5 — 49F's model side is MODEL-level, Cottonwood's must be ACCOUNT-level; the residual identity holds only if both cover the same account universe.
- **[0.4.0_DE_ClientPlatform]** (self) on hold-lift: Set A + C1 against the §4 render matrix (four selections + discriminating control), **Andrew visual smoke as the close leg** — the leg MDPF_SCOPED reopened without on 2026-05-29.
- **[Andrew]** no open sovereign calls at this lane. D6 closed; day-one naming ruled.
