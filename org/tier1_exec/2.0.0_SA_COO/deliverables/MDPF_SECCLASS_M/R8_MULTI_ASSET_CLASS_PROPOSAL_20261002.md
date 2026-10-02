# MDPF_SECCLASS -- a `multi_asset` class for allocation funds: four-postulate record and token census (PROPOSAL)

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 12:4xZ. **For:** `1.0.0_SA_CTO` (batch 145 C: "an allocation proposal is yours to author").
**Status: PROPOSAL -- a vocabulary member; nothing built, nothing written.** A value-enum proposal arrives with its four-postulate
record and its word-boundary token census (CLAUDE.md rule 24); both are below.

## What is missing, measured

The canonical `asset_class` domain is {equity, fixed_income, alternatives, commodities, structured} (plus the callers' `cash` rule and
`unclassified`). A target-date, balanced or global-allocation fund holds several of them by design; it is a member of none. The table
already shows the gap -- **seven allocation funds sit as `scheduled` rows (copied from bd-securities) in four different classes**
(get-item 2026-10-02 12:4xZ):

| ticker | fund | row today |
|---|---|---|
| AOR | iShares Core Growth Allocation | equity / Global |
| VTHRX | Vanguard Target Retirement 2030 | equity / Global |
| VSMGX | Vanguard LifeStrategy Moderate Growth | fixed_income / Intermediate |
| VTIVX | Vanguard Target Retirement 2045 | **fixed_income / Cash** |
| VWELX, VWENX | Vanguard Wellington (Investor, Admiral) | equity / US Large Cap |
| ABALX | American Funds American Balanced A | equity / US Large Cap |

and today's acts withheld **28 more** for want of a class: 16 in the BD per-ticker first act (batch 145 C; 4,292,232.06 USD at 49
Financial, AAETX, FBALX, CAIBX, VTTHX, LIPKX, KAGIX, CLBAX, AMECX, SGIIX, FKIQX, CFIHX, FTYPX, MDLOX ...) and 12 CUSIPs in the
residual act (AF 2030 target date, Fidelity Balanced, Capital Income Builder, Impax Sustainable Allocation, Income Fund of America,
Franklin Income, Vanguard Target Retirement 2035, American Balanced 529A, First Eagle Global, a 529 Balanced Fund, Kensington Dynamic
Allocation). Not measured: Cottonwood's and Inflection's allocation holdings.

## Token census (word boundary, `comp-find -i`, corpus all, 2026-10-02 12:4xZ)

- `\ballocation\b`: **32,371 hits across 215,102 files** (DEF 148, SURFACED 14,678, CONFIG 6,365, TEST 92, DOC 11,088) -- the word
  already names billing allocation (Black Diamond's `alloc_aua`, the "alloc-billable gate"), model allocation (Positioning), asset
  allocation charts. A class value `allocation` would collide with every one.
- `\bmulti_asset\b`: **0 hits across 215,102 files** (a measured zero in scope; 122,325 ephemeral-floor, 8,336 binary and 7 unreadable
  files not searched). Proposed token: **`multi_asset`**, display label "Multi-Asset".

## Four postulates

1. **MECE over the declared domain.** Domain: the class of a held SECURITY (a fund is one security). By subtraction from the five:
   an allocation fund is not equity, not fixed_income, not alternatives, not commodities, not structured -- each is wrong for a
   60/40 fund, and the seven rows above prove the domain forces a guess (four answers for one kind). Adding `multi_asset` closes the
   domain for this kind; a fund that IS one sleeve (an equity fund with some cash) stays in that sleeve's class.
2. **Same grain.** Security-level, as every other class. NOT look-through: splitting a fund's dollars across its sleeves is a
   different grain (position x holdings), needs each fund's published allocation (a vendor read, Andrew's word), and is not proposed.
3. **Intent coherence.** One axis: what the security is. `multi_asset` says "this security is a mix by design" -- the same axis as
   "this security is a bond fund". Sub classes on the same axis, from what the funds are: **Target Date**, **Balanced** (a fixed
   equity/bond mix, Wellington, American Balanced, LifeStrategy, AOR), **Income** (income-oriented mixes: Capital Income Builder,
   Income Fund of America, Franklin Income, Wellesley), **Global Allocation** (MDLOX, SGIIX), **Tactical** (Kensington Dynamic
   Allocation). Each member below is read against these at its own packet.
4. **State coherence.** The remedy moves: the seven existing rows above (a served class move each, its own half, `seed` over
   `scheduled` by the contract) and writes the withheld ones. It does NOT move: any equity, fixed_income, alternatives, commodities or
   structured row of another kind; any firm's cash rule; `unclassified` (allocation funds with no row stay there until their row lands).

## Readers that must admit the value before a row is written (each a change of its own)

- the classification contract's `asset_class` enum (`org/standards/MDPF_SECCLASS_CONTRACT.json`) and the seed vocabulary;
- the Holdings producer's `ASSET_CLASS_VALUES` (`holdings_snapshot.py:847` -- it REFUSES a class outside it) and the published
  `HoldingsSnapshot.schema.json` enum;
- Black Diamond's and Cottonwood's mix lists (`MIX_ASSET_CLASSES`, comp-constants registry) -- fix 1's eight become nine;
- the portal readers that name classes (the batch 99 census set, eb90f2ad) and a chart colour (`chartColors.ts`, `2.0.0_SA_COO~D`).
A row written before its readers admit it would REFUSE in the Holdings producer -- the order is readers first, rows second.

## The ask

Rule: (1) adopt `multi_asset` with the five sub classes, or name another token or split; (2) the order -- readers (contract,
Holdings enum and schema, the two mix lists, portal) as one packet, then the rows (the 7 moves and the 28 writes) as another.
