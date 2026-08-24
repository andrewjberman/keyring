# Session log — `0.4.0_DE_ClientPlatform~Z` — 2026-08-24 20:20–21:55Z

**Archetype:** BUILD-GENERAL (executed as MEASUREMENT + DETERMINATION — no build was authorized or needed)
**Seat:** site Z, spawned 20:24Z. **Project:** `ETFS_INGEST` (D4). **TO:** `ETFS_INGEST.TO-5` — COMPLETE + ACCEPTED.
**Commits:** `b332cc4fa2` (evidence record), `911da28017` (TO-5 deliverables). Both on `origin/SITEZ` — local at my measurement, carried by MSTR~Z's integration between my read and COO~Z's.

---

## What I was seated for, and what I actually did

Seated ahead of my TO (MSTR~Z disclosed the spawn ran past COO~Z's own placement hold). Measured
**zero lane TOs** at startup (`to-check --all`, `scanned=2084`) rather than agreeing with the report
of it. Held the build boundary until COO~Z's TO + GO arrived, and executed one CTO~Z-directed
measurement in the interim — surfacing my reading of the boundary *before* acting rather than after.

Three deliverables: the **placement proof**, the **`Z-S12` answer**, and **`ETFS_INGEST.TO-5`**.

---

## 1. Placement condition — DISCHARGED. Site Z, proven by EXECUTION

MSTR~Z had measured PRESENCE and bounded it themselves (*"deps EXIST is not that a dev server RUNS"*).
Closed by execution: bun resolved **from PATH** (not CLAUDE.md's `/c/Users/AndrewBerman/.bun/bin/bun`,
which does not exist on this box), vite v7.3.5 booted 971ms / HTTP 200, three headless renders,
`LOC=/positioning` on all three, canvas `rgb(195,202,218)`, and the ETFs flip exercised by a real click.

## 2. ⚠ The stale-tree episode — the most important thing that happened

The shared portal checkout was **13 commits behind `origin/DEV`**, and **4 of those touched the exact
surface I was sent to render** (the TO-3 flip). **My first render was of a tree with no flip in it.**
Stopping there would have produced *"the ETF flip does not exist on portal DEV"* — confident,
well-formed, and **entirely false against a PRD cell that was right**.

Two of my own intermediate reads were wrong and both were caught before they reached anyone:
- `rev-parse origin/DEV` read **pre-fetch** returned a stale ref that looked current;
- `branch -a --contains` showing `origin/DEV` → I inferred `==`. **Contains is not equals** — wrong by
  a further 10 commits.

Remedied with `merge --ff-only` after checking clean tree / unchanged deps / true fast-forward; stayed
on DEV (Rule 19); did not touch the submodule pointer. **Disclosed before the findings, because it
changed what I measured.** RATIFIED by CTO~Z; MSTR~Z surfaced the gitlink consequence I could not see
from inside the submodule, which CTO~Z then closed as its own scoped commit.

## 3. `Z-S12` — answered by looking, and it is a third thing

Rendered against the **real** platinum artifact (76,149 B, 12:30:47Z UTC, 114 rows; negative control 404):
- ✅ **Labels correct** — the fallback ends in `return apiSubAssetClass`, so the raw value survives.
- ❌ **Colour channel dead** — `getAssetClassBgColor` falls through; all 110 equity rows take one fill.

**It does not render *wrong*, it renders *UNDIFFERENTIATED*.** The lookup census predicted breakage,
the fallback chain predicted harmlessness, and neither was right. Only the screenshot could say that,
which is why CVO~Z filed it as a question.

## 4. `ETFS_INGEST.TO-5` — 6 PASS + AC4 KNOWN-UNREACHABLE, proof-of-spec `rc=0`

**AC6 ruled option (b)** on four legs: the ~8-slot categorical ceiling (the estate's own table is
already at 16 distinct colours; 24 is 3×); a **fourth lookup site nobody had named**
(`getSubAssetTextColor`'s 8-entry allowlist → white-on-light, invisible to grep *and* typecheck);
**the estate already made this decision on another page** (SecurityScanner renders `industryGroup` as
recessive text + filter, zero colour keyed on it anywhere); and **I built a fixture to falsify my own
remedy and it failed** — 46-char labels collide with the ticker column against a fixed 165px
(`HoldingsTab.tsx:1161`), which is a **third T5-1 component nobody had named: column geometry**.

The determination changes nothing in code: **the current fallback is what the colour rules would
prescribe anyway. The defect was never that it falls through — it is that it falls through UNDECLARED,
so nobody could tell a decision from an accident.** AC6 discharged by declaring, not by building.

**AC5 corrected a premise three seats were carrying:** `FUND_PCT_TOP_TEN_HOLD` is absent from
`characteristics.csv` entirely and **sole-sourced** to the constituents leg — the overlap is one field,
not two, and for the second the dependency runs the opposite way. A premise offered as reassurance is,
for half its members, the opposite. Routed to DS~Z by serial; not edited (spec frozen mid-round).

## 5. The C3 asymmetry — measured, surfaced, reached Andrew

After Andrew's 21:47Z architecture ruling I measured that `constituents_issuer_fill.csv` carries
**zero** classification of any scheme per-security, while the Bloomberg HB vocabulary exists **only**
as a fund-level aggregate. So C3's two candidates are **asymmetric**: GICS is per-security and free to
serve; serving the HB vocabulary needs either Bloomberg's own fund-level number — the shape his word
just retired — or a per-security classification we do not pull. Surfaced, explicitly not adjudicating
C3. COO~Z and CVO~Z each corroborated independently; CTO~Z took it to him.

## 6. Smoke test — refused, and the refusal was the deliverable

Andrew was ready to smoke-test. I refused tonight and gave the reason: **the current render shows the
11 GICS sectors — the very vocabulary condition (ii) exists to REPLACE** — so a smoke test could only
be passed by the wrong artifact. Accepted by MSTR~Z, backed by CTO~Z (who withdrew their own offer of
it), confirmed by COO~Z.

⚠ **And I was half-wrong in the other direction, corrected by CTO~Z:** withholding is also a choice
made on his behalf. "This could mislead him" argues for **labelling**, not withholding. Our positions
crossed in flight and converged: the synthetic render reached him as a **decision input**, correctly
labelled, not as a smoke test. Banked to memory.

---

## Compiler tools

| tool | result |
|---|---|
| `comp-transform schema-check HoldingsTab` | All rendered fields match their response types; no MISSING. Phase-1 clean. |
| `comp-transform ternary-audit HoldingsTab` | "Nothing to audit" — **read as a SCOPE statement, not an absence**: `PositioningMode` lives in `shared/bookSet.ts:44`, outside the paths the tool resolves. Recorded so nobody cites it as "no mode-branching exists". |
| `comp-cache collisions` | No new key (no code written). `['positioning-data']` is shared by 3 readers, pre-existing; the ETF artifact already has its own key. |
| `comp-find -i "GICS" portal/src` | 6 hits, **0 in `pages/Positioning/`** — reproduces the TO's premise oracle, and surfaced the rung-2 lead (`portfolio-optimization.ts:22`) that became AC6's leg 3. |

## Controls, including one that did not fire

- **Positive controls that fired:** `GICS_SECTOR_NAME`=1 in the same header returning 0 for the target
  (re-run separately after an `&&` chain died on a `grep -c 0` and skipped it); artifact HEAD 200 vs
  a 404 negative control; `merge-base --is-ancestor` run in **both** directions, which is what revealed
  the checkout was behind rather than ahead.
- **Did not fire, stated:** my chosen positive control for the ticker parse (`SPY`/`AGG`) was **absent
  from the file**. The parse is corroborated by the 36 recovered keys being plainly ETF tickers, not by
  the control I picked. Weaker evidence than intended.
- **The validator proved able to fail:** proof-of-spec returned 13 violations → 1 → 0 across three runs.
  COO~Z used that history as the failability evidence rather than building a mutant.

## Bounds carried forward

Pre-deploy read (not live-serving). The 1 NULL `sub_asset_class` row of 114 not isolated. Which field
list requests `FUND_PCT_TOP_TEN_HOLD` — unmeasured. Whether the Models artifact's vocabulary can reach
the shared tables — **unmeasured**; I could not locate it under the platinum or assets trees and said
so rather than assuming.

## Open at close

Blocker #1 answered by Andrew's 21:47Z word (DS~Z's additive-field cell). **#2** producer chain / held
`ETFS_POSITIONING.TO-5` contract (AE~Z). **#3** the T5-1 **build** has no TO (COO~Z) — I will not start
it without one. The frontend is **not** the long pole and that is on the record.

Zero crons armed at this seat.
