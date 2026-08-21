# ETFS_POSITIONING TO-3, 2000-2115Z -- the flip, and a census that was right about the wrong domain

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~2000Z -> ~2115Z (fresh seat; spec-at-pickup first act)

## The assignment

TO-3 (COO @10f94e4f13, decomp @308fcaea0d): the Positioning Models<->ETFs flip plus the five
hardcoded `'UST'` model-list sites. Andrew priority, front of queue. My own prior read of the
plane was adopted into the TO as binding input.

## Spec-at-pickup, run before touching anything

| oracle | result |
|---|---|
| O-1 `comp-find -i "'UST'" portal/src/` | 31 hits / 415 files, DEF=11 -- the five in-plane sites at the exact `file:line` the TO names |
| O-2 `portfolios` in `portal-proxy.ts` | `Record<string, PositioningPortfolio>` at `:1064` -- the artifact side is OPEN |
| O-3 `git -C portal branch --show-current` | `DEV` (rule 19 satisfied) |

## The finding: the five were right, the pattern's DOMAIN was too narrow

I positive-controlled the TO's number before disputing anything -- the quoted form returns
**exactly 5**, at exactly the lines named. Then I asked what the pattern *could not* match.
`comp-find -i "'UST'"` is **quote-delimited**, so the same membership fact written another way
is invisible to it:

| form | n | why the census cannot see it |
|---|---|---|
| quoted array | 5 | (the five in the TO) |
| bare object keys | 3 | `UST:` has no quotes -- `PORTFOLIO_CONFIG`, `DEFAULT_CUSTOM_WEIGHTS`, `zeroWeights()` |
| fixed-length array | 2 | five `'N/A'` literals silently asserting exactly five columns |
| fixed count | 1 | `repeat(5, ...)` in the grid template |
| silent filter | 1 | `.filter(id => PORTFOLIO_CONFIG[id])` **dropped unknown books with no error** |

**True denominator: 12, not 5.** The load-bearing consequence, and the reason this was worth
raising rather than quietly fixing: *fixing only the five would have left `repeat(5)`, two
five-long N/A rows and a five-key config still closing the set -- while the census that found
the five read CLEAN afterwards.* A partial fix would have shipped and been re-confirmed by its
own instrument. COO recorded it as Amendment E against the decomp @1018a9cebc.

## The discriminator I proposed was a bipartition with an empty side

I had offered "order-only vs membership-carrying" as a read; the TO hardened it into a binding
rule. Measured: **zero of the twelve are purely order-only.** `PORTFOLIO_ORDER` is the trap --
its NAME says order, its BEHAVIOUR is membership (the header renders exactly
`portfolioNamesFor(...).map(...)`, so it decides the column SET, and the panel indexes back into
it to recover identity). A name that understates a coupling invites the tolerant treatment the
code does not tolerate.

COO took the issuer half of this squarely. The half that is mine: **I offered it without
measuring it, and I could have measured it at the time.** It read as obviously true, which is
exactly the property that got it through.

## AC3, and why the method is most of the claim

`git stash` was **refused by the shared-worktree gate** -- correctly; it parks every seat's dirty
files. The gate's own advice produced the better method: a **detached worktree at HEAD** on a
second dev server, `node_modules` reached by a junction.

Two design decisions did the real work:

- **Fixtured with the LIVE served artifact.** An unfixtured capture was rejected as the oracle --
  the dev server has no backing data, and one empty state is byte-identical to another however
  badly the code between them broke. *A capture that cannot fail proves nothing.*
- **All four view modes, matrix expanded.** `generateSections` branches per mode; the landing
  view alone leaves three branches unrendered and therefore unverified.

Result: `PRE == POST(normalised)`, sha256 `ce818051...`, residual diff **0 lines**, grid template
string reproduced exactly. **Mutant control:** swapping `MODEL_BOOKS` order produced 16 changed
lines, so the instrument sees precisely the regression class AC3 exists to exclude. Re-run after
every subsequent edit, including one I could have argued was unreachable from Models mode --
"unreachable by inspection" is the thing this method exists not to rely on.

## Two defects that only a rendered screenshot could find

1. After the flip the selector stayed on `'AGG'` -- a code that does not exist in ETF mode -- so
   the page opened on "No holdings data available" **with correct data sitting behind it**.
2. A **designed shell rendered with the words for a broken one.** `holdings_status` exists
   precisely because an empty array from a shell and one from a failed producer are
   byte-identical; rendering both as "No holdings data available" discards the entire
   discrimination AE built the field to carry. Later verified in **both** directions -- with no
   payload at all the panels correctly say "No holdings data available" and *not* "Book-level
   metrics only".

A third, found only because CTO asked me to confirm a state I had **not exercised**: my
unavailable-notice **named the specific blocker**, and the blocker moved under it twice inside
one hour (bucket-policy grant landed; then the route deployed live). Neither sentence was wrong
when written; both were wrong within the hour. Rewritten cause-agnostic at `a60b558f`.
**A user-facing string that names a moving cause is a claim requiring re-verification on every
leg of a rollout, by someone who is not thinking about that string -- and its failure mode is
confidently telling a reader the wrong reason, not saying nothing.**

## Structural decisions worth keeping

- **ETF books carry no `benchmark` block**, so Benchmark and Relative are switched off in ETF mode
  rather than rendering zeroes that read as measured spreads.
- **Custom stays models-only.** `MODEL_IDS` was deliberately NOT generalised -- it is the clearest
  membership-carrying site in the plane and an appended member misaligns every blended cell.
- **Build-ladder rung 2:** AE's B-form holding is field-for-field the live `current_holdings[]`
  row shape, so ETF mode reuses the existing renderer through one adapter instead of a second
  render path. The path not on screen is the one that rots.

## Push state

| commit | what | state |
|---|---|---|
| `ee90fa8e` | the flip + 12 derived sites | **ON `origin/DEV`** (ls-remote), carried by MSTR's window |
| `a60b558f` | cause-agnostic notice | **LANDED LOCAL**, rides integration |
| `19e8f166b3` | proof-of-spec + TO status | **LANDED LOCAL**, rides integration |

A direct portal push was attempted and correctly **BLOCKED** by the LD-0367 integrator-only gate.
DT's seating condition (i) is met at `ee90fa8e`; I surfaced that rather than letting DT discover
it, since the seating message predated it being true.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `-i "'UST'" portal/src/` | DENOMINATOR 31/415, DEF=11; confirmed the five, and its **domain** is what the whole finding turned on |
| `comp-find` positive control | quoted-form grep in-plane | exactly 5 -- which is what established the pattern was RIGHT and its domain too narrow, rather than the TO being wrong |
| `ui-smoke.mjs` (/frontend-dev) | `--fixtures`, `--click`, `--fail` | 5 screenshots rendered and READ; found all three render defects |
| `bun run typecheck` | `tsc -b --noEmit`, **mutant first** | rc=0; mutant rc=2 naming the line. Bare `tsc --noEmit` compiles an empty file set here and would pass on anything |
| `proof-of-spec-check` | positional, 6 ids, **rc read without a pipe** | VALID rc=0, 6 rows, 0 violations; COO re-ran it independently |

## Blockers

None at this seat. The ETF artifact (`platinum/etfs/positioning_data.json`) is a 404 -- verified
with a positive control, prefix empty -- and that is DS's leg; the page renders the correct
unavailable state and flips to real books when it lands, with no portal change. The promote is
DT's.
