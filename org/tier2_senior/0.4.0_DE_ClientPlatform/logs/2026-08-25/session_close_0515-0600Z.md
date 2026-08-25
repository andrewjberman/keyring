# 0.4.0_DE_ClientPlatform~Z -- session close, 2026-08-25 0515-0600Z

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, TRACE

Window: since `session_close_0156-0515Z.md` @ `c71263ed2c`. Two Andrew-direct items landed and one
was investigated and deliberately NOT shipped.

## WHAT LANDED -- AND IT REACHED PRODUCTION

| commit | what |
|---|---|
| `e909149f` | killed the stale ETF rollout disclaimer (Andrew-direct: *"What is this bullshit disclaimer"*) |
| `063ff4d7` | **merge** `origin/DEV` into DEV -- 19 upstream under 9 local |

```
portal DEV     0 ahead / 0 behind origin/DEV
063ff4d7       on origin/DEV AND origin/PROD
```
**All nine of the session's portal commits are in PRODUCTION**, verified by reading `origin/PROD`
bytes directly: eight-key adapter (`etfAdapter.ts:97`), "across Opal ETFs", the removed disclaimer,
`SECTOR_ORDER_BASE`, and `components/EtfModal.tsx` present.

## THE MERGE -- AND I OVER-STATED ITS BLAST RADIUS

Andrew spawned `0.2.0_DT_PortfolioAnalytics~Z` for `/prod-deploy`; `/prod-deploy` cuts from
`origin/DEV`, which still carried the THREE-KEY adapter. **So this merge was the only thing between
the promote and shipping the defect Andrew had watched get fixed.** GO from `0.0.0_AB_MSTR~Z` (8303)
discharged my own "not unasked" condition.

>> **I reported FOUR conflicting files. It was TWO.** `git merge-tree` prints *"changed in both"*,
which means both sides TOUCHED the file -- not that git cannot reconcile it. `Positioning.tsx` and
`bookSet.ts` auto-merged; only `PositioningSummary.tsx` and `HoldingsTab.tsx` conflicted, one hunk
each, **both pure import unions with zero logic overlap.** The instrument answered a different
question than the one I asked it -- the session's recurring shape, this time mine. <<
⭐ **`0.0.0_AB_MSTR~Z`'s "mechanical union" WOULD have been correct here.** Their withdrawal and my
insistence on a semantic read were both right PROCEDURALLY; the mechanical answer landing does not
make it knowable in advance.

**Resolutions:** union on `SUMMARY_VIEW_MODES` + my imports; `getCanonicalModelName` DROPPED after
grepping the post-merge body (0 call sites -- `d53049a0`'s Agg removal deleted its only use).
**Intent verified, not just compilation:** `SECTOR_ORDER_BASE = 60` present (:244/:255) and
`canonicalOrder`'s explicit `undefined` check present (:543). Either reverting leaves typecheck GREEN
and breaks the ordering Andrew approved.

**Shared-worktree discipline:** merge window broadcast OPEN (8305) and CLOSED (8368) because a live
`MERGE_HEAD` on this one checkout silently stages other seats' files into my merge index.

## THE SALXX NAMING ITEM -- FIVE REMEDIES, FIVE FALSIFIED, NOTHING SHIPPED

Andrew: the SALXX row reads `STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS`; should be
`State Street U.S. Government MMKT`. He pointed me at the VUG fix, and he was right to.

| # | proposed remedy | falsified by | how it failed |
|---|---|---|---|
| 1 | seed `bd-securities`, producer consumes it | DS~Z census | **142 names WORSE** ("Apple Inc" -> "APPLE INC COM"), 0 better, to fix 6 |
| 2 | run `seed-etf-classifications.py` | DS~Z @ `:62` | `OVERRIDES.get(ticker, ticker)` -- writes `name = "SALXX"`, the placeholder |
| 3 | title-case the all-caps rows | CVO~Z | `BP PLC` -> `Bp Plc`, `GSK PLC` -> `Gsk Plc` -- worse, while LOOKING like the fix |
| 4 | treat "all-caps" as the defect class | COO~Z | it is not a class: `BP PLC` and the SALXX string are both all-caps, one is correct |
| 5 | **mine** -- register in `etf-classifications` | DS~Z | 0 of 7 all-caps tickers have a row; the SSOT holds HELD-ETF rows, the 7 are stocks/ADRs |

**My #5 is right for SALXX/FXFXX and does NOT generalise -- I measured two tickers and generalised to
seven.** `2.0.0_SA_COO~Z`'s fairer read: 0-of-7 proves the plan delivers Andrew's ask and nothing
more, which is a scope feature.

**WHAT I DID ESTABLISH (measured, controls firing):**
- The canonical naming SSOT is **`etf-classifications`** (DDB, TF-managed
  `infra/aws/terraform/yang-pipeline/etf-classifications.tf`), NOT `bd-securities`. My first handoff
  (8409) named the wrong table and I corrected it at full reach (8427).
- SALXX + FXFXX absent from `etf-classifications`, `ETF_NAME_OVERRIDES`, `CANONICAL_SECURITIES`.
  Controls: VUG "Vanguard Growth ETF", CLIP "Global X 1-3 Month T-Bill ETF", VUG 5/1 in the registries.
- **`etf_positioning_gold.py` has ZERO references to any naming registry** -- `:822` takes silver's
  raw vendor string. The 08-18 VUG fix taught `yang-generate-holdings-attribution` to resolve
  registry-first; **the ETF producer was never wired into that chain.**
- ⭐ **The VUG doc PREDICTED this in writing 7 days ago:** *"59 non-held DDB rows still carry
  ticker-as-name placeholders ... they become live the day such a ticker enters a model."*

**Durable finding for the backend team: there is NO single canonical naming home spanning equities,
ADRs and funds.** That is an architecture gap, not a casing bug.

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i "VUG"` over `org docs` | PASS | 289 hits, banded -- surfaced the SSOT decomp that reframed the whole naming question |
| `comp-find` | `--name "*canonical_securities*"` | PASS | located the seeder; led to the WRONG table, corrected later |
| `bun run typecheck` | `tsc -b`, 2 runs | PASS | post-merge rc=0, rc captured with no pipe |
| `scripts/ui-smoke.mjs` | 2 renders | PASS | post-merge render byte-equivalent to pre-merge |
| `git merge-tree` | conflict pre-read | **WARN** | answered "both touched" and I read it as "both conflict" -- 4 predicted, 2 actual |
| `aws dynamodb` | get-item x8, describe-table x2 | PASS | `asset_name_raw` vs `name` trap found; positive controls fired |

**What worked:** `comp-find`'s bands put the VUG SSOT decomp at the top of 289 hits -- that document
reframed the item from "fix a string" to "the ETF producer was never wired into the naming chain."
**What failed:** `git merge-tree` -- not the tool, my reading of it. **Gap found:** none new.

## DE ADDITIONS -- FILES MODIFIED

See commit messages: `e909149f`, `063ff4d7`. No extra context needed; the merge touched only
conflict resolutions in two import blocks.

## MCP TRAFFIC

~45 messages. Significant: MSTR~Z's GO on the merge (8303); my merge-window OPEN (8305) / CLOSED
(8368); the SALXX handoff to DT~Z (8409) and its correction to the right table (8427); MSTR~Z's push
of `origin/DEV` @ 063ff4d7 and the PROD promote @ `d9a98bcc`; CTO~Z's ruling that the name fix does
NOT ship tonight.

## BLOCKERS

**None BLOCKED.** Three OPEN, all with named owners:
- **Name fix NOT SHIPPED** -- CTO~Z ruled, after five falsified remedies. Correct call.
- **ETF modal SAVING** -- `etf_key_notes` surface-id family awaits `3.0.0_SA_CVO~Z`'s ruling
  (amends PK ruling @a9a173e7fa); `0.7.0_AE_CloudOps~Z` authors+deploys. READING works.
- **Asset Sub-Categories not wired for ETF mode** -- `capabilitiesFor('etfs').attribution = false`.
  Brief: `deliverables/deZ_ASSET_SUB_CATEGORIES_ETF_WIRING_BRIEF_20260825.md`.

⚠ **NOT MINE, RECORDED:** `CI - Build & Validate` FAILED on `063ff4d7` while `Deploy to Production`
succeeded on byte-identical content at `d9a98bcc`. MSTR~Z traced it pre-existing (`8ecb6b68`);
COO~Z named the class -- a headSha-scoped check structurally cannot see the workflow that validated
the content. No rollback, endorsed. My merge content is independently verified (typecheck + render +
`origin/PROD` byte read).

## CURRENT STATE (zero prior context)

- **portal: 0 ahead / 0 behind `origin/DEV`; `063ff4d7` on `origin/DEV` AND `origin/PROD`.** Clean.
- **Workspace SITEZ:** this log is the only uncommitted item at write time.
- **Live in PROD:** FXFXX + SALXX as `Fixed Income` / `Ultra Short Duration` at panel top; all eight
  return windows where data exists; economy-code sector order with the light->dark ramp; Industrials
  `blue550 #3073f1`; unmapped `#111827`; "across Opal ETFs"; editable ETF modals; narrative Model
  Key Notes; no rollout disclaimer.
- Dev server left on :5199 (NOT :5175 -- CTO~Z reserved that for Andrew).

## NEXT STEPS

1. **[0.2.0_DT_PortfolioAnalytics~Z / 0.4.0_DS_ClientPlatform~Z]** the SALXX name, per CTO~Z's ruling
   -- NOT tonight. Do not run the seeder (writes the placeholder); do not wire `bd-securities`
   (142 worse); do not title-case (breaks the acronym companies).
2. **[3.0.0_SA_CVO~Z + 0.7.0_AE_CloudOps~Z]** `etf_key_notes` family ruling -> unblocks modal saving.
3. **[backend team, via 2.0.0_SA_COO~Z]** Asset Sub-Categories Option A vs B, per the brief.
4. **[0.4.0_DE_ClientPlatform~Z, me, unsequenced]** two small display items, both derivable today
   with no producer change: distinguishing "does not pay a dividend" from "not retrieved" (30 of 38
   null-yield rows are genuine non-payers), and the fund-inception blank 1Y on PFDE/PFOE.
