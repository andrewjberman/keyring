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

---

## Addendum -- the weight-unit episode (2115Z onward, after DS published)

DS published the real artifact. I re-fetched and **rendered the real bytes rather than trusting
the fixture I had built from the contract** -- and the fixture was shaped perfectly and hid three
defects completely, because **I wrote the fixture from the contract, and the contract is exactly
what was silent.** A fixture reproduces its author's reading of the spec; only the real bytes
carry the producer's.

The page rendered NVDA at **994.99%**, market caps in raw dollars, and ACTIVE reading NO on every
row. Root cause: **CONTRACT v1 fixed the FIELD NAMES and was silent on UNITS**, so DS emitted each
field in its source unit and I had no declared unit to build against.

### The part worth keeping: two correct fixes that would have composed into a worse bug

I fixed it in the TS adapter. DS fixed the same bug in the Python publisher **sixty seconds
later**. Neither of us could see the other. Had both landed, every weight would have rendered
**100x too small** -- and *that is the dangerous direction*: 994.99% is absurd and Andrew caught
it in seconds; a table where every row reads 0.1% looks like a rounding convention and **gets
believed**.

I did not ship it, and the reason is worth stating exactly because it was one command away from
going the other way: **I re-pulled the artifact before committing a fix I had already verified by
render twenty minutes earlier.** Nothing about my own evidence looked stale. The artifact had
moved under a verified fix.

**COO's framing is the one I'd keep: the composition was the defect, not either fix.**

### Where it landed

Ruled by AE (contract oracle), independently confirmed by CVO and COO: **the conversion lives in
the publisher, one place not two** -- a unit chosen for a consumer's rendering convention is
serving-shaped work (Rule 17b), so the artifact matches Models **by construction** rather than by
every consumer re-deriving it. Same reasoning as the separate-artifact ruling one layer up.

I deleted the conversion rather than flagging it `false`. A constant named
`ETF_WEIGHT_IS_PERCENT` reading `false` is a double negative about a fact established in another
repo, and the next seat seeing a small weight is one keystroke from flipping it back. What
replaced it states the three units as measured and **locates the truth in the publisher**.

**Nothing in the type system could have held any of this.** `number` and `number` are the same
type whether one is a percent and the other a fraction -- schema-valid, every key present, every
type right, proof-of-spec rc=0, and the answer wrong by a factor of 100.

### Final state

| commit | | |
|---|---|---|
| `a7ff6dd4` | the conversion (correct against the 21:17Z artifact) | superseded |
| `d43b88c5` | deletes it; unit contract documented | LOCAL, rides integration |

Net effect of both on `etfAdapter.ts` vs `a60b558f`: **the doc comment only** -- token census at
HEAD 0, positive control 5 at `a7ff6dd4`. Verified against the live 21:25:57Z artifact, screenshot
READ: NVDA 9.96 / MC 5239.1 / ACTIVE YES. The 9.96 against a raw 9.95 is the page's **existing**
`proportionalRound` normalising the column to exactly 100.00 -- identical treatment to Models, and
I say so rather than claim "byte-exact", which was the easier and slightly false version.
