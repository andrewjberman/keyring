# 1.0.0_SA_CTO~X -- session 2026-08-24 20:39Z to 2026-08-25 00:16Z: the Positioning "Agg" view traced to Opal's cross-partner firm AUM, pulled from three pages on Andrew's word, and the toggle-persistence pattern built

**archetype:** TRACE
**secondary_archetypes:** IMPLEMENT, VALIDATE, SCRIBE

Fresh `~X` lane, spawned by Andrew for one question about the Positioning page. Startup clean (no orphan
watcher for this serial; base `1.0.0_SA_CTO` live at a different PID and untouched). Zero crons, per the
XXX.md Step 1b-F row for this serial. Zero open TOs at this lane at start and at close.

## 1. THE QUESTION AND THE ANSWER

Andrew: where do the "Agg" view weights on Positioning/Models come from, and "how are those weights being
assessed per firm?" -- with a stated worry that Agg was tied to **Opal's** aggregate models rather than the
**advisor's** aggregate Opal model exposure.

**His hypothesis was correct, and the answer to the per-firm half is that they are not assessed per firm at
all.** Source-confirmed AND exercised:

- MECHANISM: `yang-generate-positioning/lambda_function.py:1193-1218` @`69b867c4eb` --
  `model_weight_in_agg = model_aum / total_aum`, `aum_data` loaded `:1114-1125` from
  `s3://opal-data-portal-v2/json/portfolios/aum-metrics.json` `by_model[].aum`.
- THAT ARTIFACT IS THE WHOLE FIRM, POOLED ACROSS THREE PARTNERS (live read): `total.aum`
  $1,951,676,164.42 / 7,854 accounts, and its own `meta.fee_basis_components` splits it EXACTLY three ways
  -- 49financial $1,689,302,889.53, inflection $137,997,265.16, cottonwood $124,376,009.73 (sum ties to the
  cent). Token census over the file: `advisor`=0, `adviser`=0, `rep_code`=0, `household`=0, `tenant`=0,
  `account_id`=0.
- EXERCISED on the served `positioning_data.json` (gzip on the wire, 8,133 B / 73,458 B decompressed;
  `data_as_of` 2026-08-21 = Friday, correct T-1 on a Monday -- trading calendar resolved BEFORE any
  freshness language, per NEVER#1; not a staleness finding): `AGG.total_aum` $1,637,144,180.01, 30
  holdings, weights summing to exactly 1.0, per-model AUM byte-identical to `by_model`. Implied weights
  UST 3.20 / ST 7.89 / INT 27.14 / **LT 49.15** / ULT 12.62 pct.

So an advisor whose book is entirely Short-Term saw an "Aggregate" that was 49% Long-Term Conservative.
Not a display bug -- a correct answer to a question nobody on that page was asking.

**Two further defects found in the same trace, recorded not remediated:** (1) the producer's name->code map
(`:1090-1105`) covers 5 of the artifact's 7 models, so "Opal Blend 5050 Int Ltc" ($32,065,435/155 accts) and
"Opal Blend 5050 St Int" ($7,284,200/24) drop from BOTH numerator and denominator while survivors still
normalise to 1.0 -- invisible on screen; (2) THREE independent implementations of one concept, two
client-side and invisible to the server (Positioning's was unreachable dead code behind a `const`
`selectedPeriod`; Attribution and FactorTilts were live).

## 2. ANDREW-DIRECT x2, RECORDED VERBATIM @02cb56f100, BROADCAST SAME TURN (4/4 DELIVERED)

- **PULL the "Agg" toggle view** from Positioning, Attribution, Factor Tilts -- *"nobody cares about this
  view and its more trouble than its worth."*
- **Build the client-side toggle cache on Positioning AS A REUSABLE PATTERN** -- *"define this mechanism as
  a pattern because we may want to implement it elsewhere in the Portal on key toggles."*

Then, on the finding being reported: *"Just clean it up, when done, just write a briefing..."*

## 3. RULE 27: I FRAMED IT WRONG AND BASE CTO CORRECTED ME (66768)

I surfaced "does this run the pipeline?" as an open question. **The correct framing is that Rule 27's
default already applies -- what sits at Andrew is only whether he EXEMPTS.** Framing it as open invited the
wrong default. His *"Just clean it up"* IS the exemption form; recorded explicitly @`ffb7514766` because an
exemption exercised but never written down is indistinguishable later from a pipeline step silently
skipped. Exemption scoped to what he named; explicitly NOT extended to the two defects in s.1.

## 4. EXECUTED -- portal `d53049a0` on DEV, 15 files, +413/-746 (mostly deletion)

Removed: Positioning's AGG selector entry + AGG-only MODEL BREAKDOWN column group + `aggregateWeighting` +
the `aumByModel` state/fetch + two dead builders; Attribution's AGG from the shared `PORTFOLIOS` list + two
live client-side builders + its AUM fetch; FactorTilts' `computeAggregateMetrics` + the AUM fetch feeding
it + the AGG-only "Show All Models" toggle + the price-weighted arm, default scope AGG -> INT.

Built: `src/hooks/usePersistentToggle.ts` -- sessionStorage (his words "short-term"/"within the user
session"; localStorage would make a toggle sticky for weeks with no way to tell a remembered choice from a
default), every read validated against a closed allowed set, every access wrapped (sessionStorage THROWS
rather than returning null when site data is blocked), namespaced+versioned keys.
`useSelectTracking` composes it via an optional `persist` arg so any Portal toggle opts in with one
argument. Wired on Positioning: book family, summary view, holdings view, selected book.

**NOT touched, deliberately:** the producer's served `current_holdings.AGG` (NEVER#3 -- he said pull the
VIEW); the **AGG ETF ticker** and the `'Agg vs Short'` / `'HY vs Agg'` FactorKeys -- same string, different
thing, live in benchmark composition, so the call was made per call site and never by grep; AGG on pages he
did not name.

## 5. THE REGRESSION, AND WHY IT MATTERS BEYOND THIS CHANGE

Removing AGG removed an ACCIDENTAL behaviour: the initial state was `useState(caps.aggregate ? 'AGG' : '')`,
which handed Models mode a selected book on mount purely as a side effect of AGG existing. With AGG gone the
page mounted with NOTHING selected and rendered "No holdings data available" **over perfectly good data**.

**`tsc -b` and `eslint` BOTH PASSED CLEAN on that state.** It was caught only by rendering the page and
reading the screenshot. This is portal CLAUDE.md's verification law doing exactly the job it was written
for, and it is the second instrument-blindness of the night: a green gate that structurally cannot see the
defect class. Now an explicit first-render rule with its reason in a comment, rather than an emergent
property of a default value.

## 6. VERIFICATION RUN

- `bun run typecheck` (= `tsc -b --noEmit`) clean -- **mutant control run FIRST** (injected type error ->
  TS2322 caught -> removed), so the clean pass discriminates. Bare `tsc --noEmit` compiles an empty file set
  here and proves nothing (portal CLAUDE.md).
- `bun run lint` 0 errors; all 14 touched files individually clean. The 3 residual repo warnings are in
  files this change never touched (`PerfrpControls.tsx` -- another seat working the shared tree).
- `bun run build` succeeds.
- **All three pages rendered headless and READ** against fixtures built from the LIVE served artifacts
  (positioning, factor-tilts tier1-snapshot, holdings-attribution, allocation-summary -- all gzip on the
  wire). No Aggregate in any selector; Positioning weights sum to 100.00; Factor Tilts defaults to
  Intermediate-Term with the Agg-NAMED factors intact; colour law checked on each.
- **Persistence exercised in a real browser, both directions:** select LT -> reload -> LT restored; negative
  control (storage hand-set to `"NOT_A_BOOK"`) -> discarded, falls back to UST, key cleared.

## 7. LINE-ENDING NEAR-MISS (caught pre-commit)

My Python edit scripts read with universal newlines and wrote with `newline=''`, flattening CRLF files to
LF. The repo has MIXED per-file endings, so 5 FactorTilts files showed as whole-file rewrites
(`index.ts`: 59 lines changed where I removed ONE). Restored each file to its own HEAD ending before
committing; the diff went from 1,522/2,007 to 261/746 and `index.ts` to `1 -`. **An unreviewable diff would
have defeated the review Andrew explicitly asked DT to do** -- the cost was not cosmetic.

## MCP traffic

Sent 2 multi-recipient acts (8 deliveries, 8/8 DELIVERED, denominator printed each time): the
record+finding broadcast (COO/CVO/MSTR/CTO-base), and the exemption + landed-state report. Received 6, all
READ-acked via `ack_messages`: 4 startup (closed-loop DT promote + MSTR integration reports from the prior
`~X` session, 2026-08-18), CTO-base 66768 (the Rule 27 correction -- adopted), MSTR 66966 (the `-F`
commit-integrity hazard -- adopted the unique-filename habit for all 4 commits this session, each
`[msg-verify]`-confirmed before I quoted it).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| comp-which | routing the AGG-weights question | PARTIAL -- surfaced `comp-platinum`/`comp-cluster` as a NEAR-TIE and said so; the router's honesty about the tie was the useful part |
| comp-find --name / content | `*ositioning*`, `*AGG*` censuses across portal + estate | PASS, denominators printed (2/417, 72/28164) |
| comp-platinum | `page Positioning --firm bd` | **FAIL (silent)** -- "No fetches detected in this component" on a page whose panels/tabs do every fetch. A clean, well-formed, MISLEADING zero. Not quoted as evidence of absence |
| comp-trace / comp-dataflow | `--help` (usage recon) | PASS -- neither fit this trace; recorded rather than forced |
| to-check.py | `--all --assignee 1.0.0_SA_CTO~X` | PASS -- 0 TOs, 2088 scanned, 0 parse errors |
| aws s3 cp (operational) | 5 served artifacts, whole-file reads | PASS -- gzip encoding detected and handled; byte counts printed |
| bun typecheck / lint / build + ui-smoke.mjs | portal gates + 4 renders | PASS -- mutant control on typecheck; screenshots READ, not assumed |
| safe-commit -F | x4 (unique per-commit filenames) | PASS -- each `[msg-verify]` confirmed |

**What failed:** `comp-find` died once with `SyntaxError: source code cannot contain null bytes` -- I had
caught `.tools/comp-find` MID-WRITE while another seat landed the NFRA_COMPRAIL S1 binary-skip fix. Retry
succeeded. Worth knowing: the estate's mandated default search tool is hard-broken for every concurrent
caller during an edit to itself.
**Gap found:** `comp-platinum page <Component>` misses fetches that a page delegates to its panels/tabs --
filed to CVO's channel as OBSERVATION x INERT (a coverage gap, not a defect report).
**Second gap:** `safe-commit.sh`'s post-commit verify helper throws a python `SyntaxError: unterminated
string literal` after `[msg-verify]` on some invocations (2 of my 4; the other 2 printed a clean
`MATCH len=`). Commits and msg-verify itself succeed, so cosmetic today -- but it is a verification step
intermittently not running, failing in a way that reads as noise. Filed OBSERVATION x INERT.

## Files Modified

See commit messages: `d53049a0` (portal, 15 files), `02cb56f100`, `c59ccf4667`, `b01936916b`,
`ffb7514766`. New file worth naming here because it is meant to be reused:
`portal/src/hooks/usePersistentToggle.ts`.

## Blockers

**None at this seat.** Nothing is BLOCKED; the change is complete and verified, awaiting a review Andrew
scheduled rather than a dependency.

## Current State

- **portal `d53049a0` on branch DEV** -- AGG view removed from Positioning/Attribution/FactorTilts;
  `usePersistentToggle` pattern added and wired on Positioning. Portal main tree is on DEV and never left it
  (rule 19). Typecheck/lint/build green; all three pages render-verified against live-artifact fixtures.
- **workspace CLOUD**: `02cb56f100` (Andrew-direct record + the measurement), `c59ccf4667` (gitlink
  `9580e18b8f -> d53049a0d0`), `b01936916b` (the DT briefing), `ffb7514766` (the Rule 27 exemption record).
- ⚠ **ALL FIVE COMMITS ARE LOCAL.** Integrator-only push (LD-0367) -- none is on any remote. Stated this way
  deliberately: "landed" without the push state is the class the law file names.
- **Briefing for the reviewing seat:**
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/BRIEFING_20260824_AGG_REMOVAL_AND_TOGGLE_PERSISTENCE_FOR_0.2.0_DT.md`
  -- change inventory, the four not-touched items with the AGG-string collision flagged as the thing to
  review hardest, the regression, every verification, the promote path.
- **Two items live in CVO's surprise channel from this trace** (filed by base CTO): the 7-vs-5 model map
  truncation (OBSERVATION x ARMED -- disarm owner is the producer's lane class, dark tonight, holding at
  MSTR) and the comp-platinum coverage gap (OBSERVATION x INERT). The ARMED item does NOT disarm because the
  pages that exposed it stopped rendering -- the same map and artifact feed other consumers.

## Next Steps

- **[Andrew]** instantiate `0.2.0_DT_PortfolioAnalytics` when ready -- I have pinged that I am ready.
- **[0.2.0_DT_PortfolioAnalytics]** read the briefing; cursory lint/review; DEV -> PROD promote via
  `/prod-deploy`. Route both pushes to MSTR (integrator-only) rather than pushing from seat. The gitlink
  bump is already made -- no second pointer commit needed unless portal DEV moves first.
- **[0.0.0_AB_MSTR]** integration push of the four workspace commits + portal `d53049a0`.
- **[3.0.0_SA_CVO]** the ARMED map-truncation item needs a producer-lane disarm owner when one is seated;
  remediation rides whatever project Andrew's word creates, not this exemption.
- **[1.0.0_SA_CTO~X]** hold; available for DT's review questions.
