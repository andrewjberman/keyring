# ANDREW-DIRECT 2026-09-24 ~17:4xZ at the `1.0.0_SA_CTO~Z` terminal -- the universe has THREE inflows and TWO phases

Verbatim:

> "Ok heres how this goes. We "start" with the asset management research group. Then we aim to grow to the
> full Opal ETFs group. in parallel to the 256 universe, we may get requests from PM team to expand on
> research."

Asked in the same exchange: *"I want to understand how we got to this 250 security universe, what decided the
universe exactly?"*

## What decided it, measured at the artifact

`universe.v1.2026-09-15.json`'s own `denominators` block, with `coverage_source` and `holdings_source`
beside it:

| half | count | what decided it |
|---|---|---|
| coverage | **89** | `lib/research/identity/build_universe.py:304-307` -- `os.listdir()` of `...\Asset Management\Research`, every subdirectory, one entry per name folder. Bounded by what OneDrive has synced to this device (`:4`). Identity per folder comes from its `*ONE PAGER*.xlsx` (`:9-10`, `:135-143`); no workbook means no ticker. |
| holdings_distinct | **170** | distinct securities across four ETF books -- DIVZ, IDVZ, PFDE, PFOE -- at `gold/holding/date=2026-09-11`. |
| union | **256** | the two, unioned. |
| both | **3** | the halves are almost entirely disjoint. |

**Nothing SELECTED 250 names.** No screen, no index, no criteria: it is a directory listing unioned with
four holdings files.

## What his word changes, and it corrects this seat

This seat told him the other 167 "are in the file only because they are ETF holdings, which the goal does
not mention," framing the union as scope noise. **His word says the ETFs group is the INTENDED PHASE 2**, so
the union is a GROWTH PATH that was built early, not a defect. The correction is his and is recorded as such.

Three inflows, named:

1. **AM research group -- PHASE 1, the "start".** The coverage half. **LIVE and GROWING.**
2. **Full Opal ETFs group -- PHASE 2, the aim.** The holdings half, already present at 170.
3. **PM-team requests to expand research -- PARALLEL, demand-driven, unbounded.** No carrier exists for one
   today; a request has nowhere to land.

The `names[].source` field already distinguishes inflow 1 (`"source": "coverage"`), so the model is partly
expressible without new schema -- build-ladder rung 2, not rung 7.

## The two consequences this seat owes, measured

1. **THE COVERAGE HALF IS A LIVE DIRECTORY AND ITS SNAPSHOT IS 14 DAYS STALE.** Builder artifact
   `read_started_at 2026-09-10T23:18Z`, `denominator_folders 89`; the live listing reads **93** now.
   `NOW minus ARTIFACT` is exactly four named folders -- **Alphabet GOOGL US, Eli Lilly LLY US, Quanta
   Services PWR, UnitedHealth Group UNH US** -- and `ARTIFACT minus NOW` is EMPTY, so the folder grew and
   nothing was removed. Those four securities are invisible to every downstream consumer of the universe.
   Nothing re-runs the builder; it is a one-shot artifact.

2. **SO "EVERY SINGLE SECURITY" CANNOT BE A COUNT -- IT HAS TO BE A FRESHNESS PROPERTY.** A completion test
   against a growing directory is unsatisfiable: the goal re-opens every time a PM drops a folder in, and
   with three inflows that is the normal case rather than the exception. The formulation that survives
   growth is *"the universe build is CURRENT as of the close, and every name in it is backfilled"*, with the
   count as evidence rather than as the definition. **Which of the two he wants is HIS call and is carded;
   this seat does not pick the goal's own stop condition.**

**No freshness checker, monitor or alarm is built or proposed here** -- CLAUDE.md's standing moratorium. The
gap named is that the BUILDER has no trigger, which is a scheduling question for its owning project, not a
monitor.

## HIS ANSWER, same exchange ~17:4xZ, verbatim

> "for now, universe will be defined as the 89 group, the asset management research group"

**SETTLED, and it governs every AMGT denominator from here:** the universe is the COVERAGE half alone. The
170 ETF holdings are PHASE 2 and are NOT goal-completion work; PM requests are parallel and later. "for now"
is his, so this is a current-phase definition rather than a permanent one. Consequence already routed: the
residual identity list is over the research group, not the 256 union (msg 25674).

### ONE THING NOT SETTLED, and this seat will not resolve it silently

His sentence names the population TWICE and the two readings now disagree by exactly four securities:

- **"the 89 group"** -- the count, which is the builder artifact's SNAPSHOT at 2026-09-10T23:18Z.
- **"the asset management research group"** -- the population BY NAME, which is a live directory reading
  **93** today.

The gap is the four folders added since the snapshot: **Alphabet GOOGL US, Eli Lilly LLY US, Quanta Services
PWR, UnitedHealth Group UNH US.**

**AND THIS SEAT HANDED HIM THE 89.** The figure came from this seat's own message minutes earlier, where it
was presented as the research folder's size without its vintage. So "89" is plausibly this seat's stale
number reflected back rather than a deliberate exclusion of four names -- which is exactly why it is asked
rather than assumed. Taking the numeric reading would drop four major securities from the goal on the
strength of a number this seat mis-stated.

**REC: the research GROUP (93 live), with the builder re-run so the artifact matches the definition.** One
word settles it, and nothing waits on it: under either reading the four folders need identity like any
other, so no work is blocked either way.
