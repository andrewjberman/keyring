# 0.1.0_DE_MarketIntelligence~Z — PORTAL_LINT.FIX1 (single-entry log, per the TO's own sizing)

**archetype:** DIAGNOSE

**Date:** 2026-08-11 · **TO:** PORTAL_LINT.FIX1 (1.0.0_SA_CTO~Z) · **Commit:** portal DEV `ce98e334`

Repo-wide `bun run lint` gate restored: **rc=1 → rc=0**. One line changed.

**The blocker was misattributed, and I was the source.** My OPAL_ANALYST.EXP1 surprise #1
named `ModelPortfolios.tsx:873 react-hooks/preserve-manual-memoization`, and the TO was
written from that. Measured from the resolved eslint config:

| rule | severity | |
|---|---|---|
| `react-hooks/preserve-manual-memoization` | **1 — WARNING** | never the blocker |
| `unused-imports/no-unused-imports` | **2 — ERROR** | the actual failure |

`lint` is a bare `eslint .` with no `--max-warnings`, so warnings alone exit 0. The real error
was `'ReferenceLine' is defined but never used` at line 15. **I had reported the co-located
warning — which eslint prints with a large code frame — instead of the terse error line above
it. The visually louder finding was not the operative one.**

**Fix:** removed the `ReferenceLine` binding from the line-15 recharts import. 1 insertion,
1 deletion, nothing else in the file touched. Zero behaviour change — an unused import binding
is never referenced, so no call site, render path, or timing moves. `ReferenceLine`'s only
other occurrence is a **comment** at `:580` documenting the participation-UI deletion that
orphaned it (`45e5843f`, Andrew-direct 2026-08-04). Sibling `ReferenceArea` is live JSX at
`:2165` — census run *before* editing so the wrong binding could not be removed.

**`:873` deliberately untouched.** It was the TO's named STOP condition, and the gate passing
at rc=0 with that warning **still printed** is the proof it was never the blocker — so the stop
condition never needed to fire.

**Evidence (rc captured as the next statement, unpiped):** `bun run lint` repo-wide → **rc=0**,
`1 problem (0 errors, 1 warning)` (was `2 problems (1 error, 1 warning)`, rc=1).
`bun run typecheck` → **rc=0**.

**Cross-pod, on the record:** Pod 2 / PortfolioAnalytics content; owner
`0.2.0_DE_PortfolioAnalytics` (per `.owned-paths.yaml:177-181`) did not make this change.
Authorization cited in the commit message, with an explicit invitation to reverse.

## Compiler Tools

| Tool | Result |
|---|---|
| `eslint --print-config` (resolved severities) | The instrument that falsified the TO's stated blocker — reading the config beat reading the console, where the warning is louder than the error. |
| `bun run lint` (the gate itself, repo-wide) | BEFORE rc=1 / AFTER rc=0. C1's own denominator. |
| `bun run typecheck` | rc=0 — no type reference broken. |
| occurrence census (pre-edit) | ReferenceLine 2 (import+comment) → unused; ReferenceArea 3 (incl. live JSX) → keep. |
| `comp-to` | `PORTAL_LINT.FIX1` set race-free per session. |

## Surprise (surfaced, not adjudicated)

`ModelPortfolios.tsx` authorship: Andrew Berman 81, `0.4.0_DE_ClientPlatform` 47,
`0.4.2_RD_AdvisorIntelligence` 17, `0.4.1_RD_ModelPortfolios` 3 — `0.2.0_DE_PortfolioAnalytics`
appears **zero** times. The pod-2 designation is correct per owned-paths, but the file is
routinely edited by other pods, so tonight's crossing is less anomalous than the TO's framing
implies. Ownership is not mine to rule on.
