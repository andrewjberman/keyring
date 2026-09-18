# L4 RULING -- the AMGT_RESAPP key grammar: the scope token is `harvest`, everywhere, and there is no `global` route

**Seat:** `1.0.0_SA_CTO~Z`, 2026-09-18 ~23:0xZ. **Answering:** `4.0.0_SA_CRO~Z`'s plan @`0756d2897d`
(`PLAN_RESAPP_DATA_STRUCTURE_20260918.md` s.4), which measured two candidate token pairs and named the choice *"the L4's
to fix"*. **Standing under:** Andrew-direct ~21:45Z (*"the whole pipeline will exist within opal-data-harvest"*) and
~21:1xZ (*"structured in said bucket in proper form"*), recorded at
`ANDREW_DIRECT_20260918_21xxZ_AMGT_RESAPP_REGISTER_OPAL_DATA_HARVEST.md` @`6d71e904fe`.

## The ruling

**ONE scope token for every AMGT_RESAPP key: `harvest`.**

| stream class | address shape |
|---|---|
| vendor bronze | `<vendor>/harvest/bronze/<table>/<partition>/<object>` -- `bloomberg`, `seeking-alpha`, and the new `sec`, `lusha`, `brightdata` vendor rows |
| our own derivations (silver, gold, state, code) | `amgt/harvest/<tier>/<table>/<partition>/<object>` |

**The COMPOSITE `global` route is NOT taken, and no `amgt` scope row is minted.**

## Why -- three reasons, each measured, and the third is the one that decides it

1. **It is legal, and the only rule that could forbid it does not.** `lib/opal_naming.py:1551-1552` refuses exactly one
   pairing -- `if scope == source` -- with *"a product is never a scope beneath itself"*. `amgt` under source `amgt` is the
   refused shape and is why the plan reached for `global`; **`harvest` under source `amgt` is not that shape**, so
   `amgt/harvest/...` resolves with no composite detour. `key()`'s other bars are satisfied: `source` is a `systems.json`
   key (`:1548-1549` -- `amgt` and `harvest` both already exist there) and `scope` needs a `scopes.json` row (`:1550`),
   which is the one row this ruling asks for.
2. **The precedent is the estate's own.** `mdpf` and `etfs` are each BOTH a `systems.json` source and a `scopes.json`
   PRODUCT scope row. A product token living in both files is the normal case, not a novelty.
3. ⭐ **THE BUCKET NAME AND THE SCOPE TOKEN MUST AGREE, AND ONLY `harvest` MAKES THEM AGREE.** The data-bucket grammar is
   `opal-data-{scope}` in the scope's LONG form (`org/standards/NAMING_SCHEMA.json`, `bucket.data_bucket` +
   `data_bucket_scope_form: LONG`; `scopes.json._about.row_fields` says the same in terms). Andrew named the bucket
   `opal-data-harvest`. **So the scope whose bucket that is, is `harvest` -- by the grammar, not by preference.** An `amgt`
   scope row naming `opal-data-harvest` would be a row whose bucket contradicts its own key, i.e. a second departure
   invented to serve a token choice -- and the plan's `global` route needs exactly that row, because gold, state and code
   under `global` are SOURCE-homed. **Taking `harvest` retires that requirement instead of declaring it.**

## What this ruling costs the registry, stated as the ask

**ONE scope row** -- `key: harvest`, `class: PRODUCT`, `long: harvest`, `short: harvest`, `bucket: opal-data-harvest`,
`bucket_provisioned: true` -- plus **three vendor `systems.json` rows** the plan measured as missing (`sec` for EDGAR,
`lusha`, `brightdata`), without which three of our real sources cannot be named in a conforming key at all.

⛔ **WHAT THIS RULING DOES NOT DECIDE, because it is not L4's:** the TENANCY question -- which tenancy the `harvest` row
takes, and therefore whether bronze and silver resolve to `opal-data-harvest` or to the shared `opal-data-assets`. Measured
by `4.0.0_SA_CRO~Z` and confirmed by this seat's own read of `_home_bucket` (`lib/opal_naming.py:249-261`): all 4 tenancies
home bronze and silver to `opal-data-assets`, so a scope row ALONE leaves them there, against Andrew's word. That choice --
a new scope-homed tenancy, or the doctrine recording his "`opal-data-assets` is for client/partner custodial information"
reading -- is held at `0.0.0_AB_MSTR~Z` with Andrew, and this ruling is deliberately independent of it: the token pair is
the same under either shape.

## What else the plan settles, and where it lands

- **The per-prefix TIER CLASSIFICATION this seat owed the round-14 slug addendum is the plan's s.2**, and it is ADOPTED as
  the L4 classification: bronze = the two `raw/` families; silver = crosswalk, union universe, filing analysis, management
  roster, model block (+FYE), publication links; gold = drafting, management pool, posture, peer sets, scores, metrics;
  state = UNRESOLVED markers, pack ledgers and status, run logs; platinum = none in S3 today. **Two re-classifications
  ADOPTED against their current prefix names:** `derived/model_block/` is SILVER despite the folder name, and
  `filings/v1/<key>/<accession>.source.json` is bronze and silver in ONE object.
- **`v1` retires from the ten prefixes** (no prefix ever had a `v2`; `schema_version` is the field that actually moved).
  ADOPTED as part of the target grammar.
- ⛔ **THE ONE FINDING THAT IS A SPEC DEFECT, NOT A NAMING ONE, AND THIS SEAT OWNS IT:** the filings bronze half is a
  TRUNCATED excerpt plus a `document_sha256` over bytes **nobody kept** -- 0 of 1,333 objects hold a raw filing, and
  `publications/v1` keeps no vendor response either. **A hash over bytes that do not exist attests nothing, and a re-parse
  under a new `parser_version` cannot be replayed** -- which `C-RAW-BEFORE-DERIVED` already forbids and
  `C-FILINGS-ANALYZER` assumes against. It lands in the round-14 slug addendum as a clause and, if it needs a build, as a
  round-15 cell. It is NOT a rider on any round-14 cell.

## Timing, stated so nobody waits on the wrong thing

The PRD is FROZEN for round 14 (v0.13, both halves signed). This ruling is the L4 answer the registry work needs NOW, and
its PRD text lands in the addendum answering round 14's slug, beside `C-PRODUCTION-HOME` gaining the bucket by name.
Nothing here re-opens the issuance and nothing here is a round-14 rider.

-- `1.0.0_SA_CTO~Z`
