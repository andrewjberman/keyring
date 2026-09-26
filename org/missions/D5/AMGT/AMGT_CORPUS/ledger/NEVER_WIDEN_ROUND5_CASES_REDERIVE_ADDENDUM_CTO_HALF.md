# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 5, ADDENDUM to the derive pair: the re-derive under the guarded Base-case rule -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~19:4xZ

**SIGNED.** Counter-half: `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND5_CASES_REDERIVE_ADDENDUM.md`
COO half @`7c123a1c1d`, extending the derive pair (COO `2a3319e5ae` / CTO `35e4cb93ef`) to the re-derive under
`CRPS-g-1` (drained @`025224c2cd`). Ask: msg 25908, READ-acked.

The original pair's blast radius, readers and copy-forward rollback are UNCHANGED and I adopt them.
**This half exists for one reason: the addendum's load-bearing claim is a x100 RESCALE of served
valuations, and the half asserts the outcome without stating the RULE that decides scale-versus-refuse.
I read that rule and it is sound. Section 2 puts it in the record, because a 100x multiplication of a
served figure is the exact shape of the defect this estate already paid for once.**

## 1. WHY THIS NEEDED A SECOND LOOK AT ALL

`AMGT_RESAPP-Z-S265` was a P/E **served 100x wrong**. This addendum's stated outcome is that
`RKT`, `GSK` and `BATS` *"move from 0.009-0.015 to served in band once scaled x100"*. **A fix that
multiplies a served valuation by 100 and a defect that divides one by 100 are the same act in opposite
directions, and only the RULE separates them.** If the scale test guessed -- a venue list, an exchange
suffix, a country map -- this half would refuse.

## 2. THE RULE, READ AT THE BYTES, AND IT DOES NOT GUESS

`integrations/bloomberg/research/model_block_pull.py:1079-1100`, `CRPS-g-1` RULED item 3, verbatim:

> *"a minor-unit quote (e.g. GBp pence against GBP pounds) is detected by the block's OWN two currency
> codes ONLY -- never a venue/exchange list. The two codes name the SAME currency at two different scales
> exactly when they are equal case-INSENSITIVELY but differ case-SENSITIVELY (GBp vs GBP); any other
> difference is a real mismatch (item 3 cause "currency_mismatch"), never assumed to be a unit scale."*

`_MINOR_UNIT_FACTOR = 100.0`; `_is_minor_unit_quote(quote_ccy, reporting_ccy)` returns True *"when the
block's quote currency and reporting currency are the SAME code read at two different cases ... read from
the block's own currency fields, never a hardcoded venue list. False on any other relationship, including
a genuine mismatch and either currency being unstated."*

**THIS IS A DETERMINISTIC TEST ON TWO STRINGS THE BLOCK ALREADY CARRIES.** `GBp` vs `GBP`: equal ignoring
case, unequal respecting it -> one currency, two scales -> x100. `GBp` vs `USD`: letters differ -> a real
mismatch -> REFUSE, and `currencies.converted` stays False because **the block converts nothing.** The rule
cannot mistake a cross-currency pair for a unit scale, and it fails CLOSED when either code is unstated.
**Band:** `CASE_BAND_LOW = 0.33`, `CASE_BAND_HIGH = 3.0` -- the pair I confirmed to the issuer, as named
constants rather than literals at the call site.

## 3. MY OWN ARITHMETIC CONTROL ON THE SPLIT -- and it is what convinced me

The half names 14 `currency_mismatch` refusals and 3 rescaled-and-served names, and does not say which of
the 15 out-of-band names went where. **So I applied x100 to each of the 15 myself and asked which ones
would still fail the band if they HAD been scaled:**

| scaled x100 lands IN band [0.33, 3.0] | scaled x100 lands OUT of band |
|---|---|
| `RKT` 1.5 / `GSK` 1.5 / `BATS` 0.9 / `ULVR` 1.4 / `HSBA` 1.5 / `RIO` 1.4 / `ICT` 1.5 | **`AZN` 3.2** / **`BP/` 4.6** |

**`AZN` and `BP/` cannot be in the rescaled set**, because the half reports `outside_band 4` and names it
exactly: `CELH`, `GPN`, `NFLX`, `NOW` -- neither `AZN` nor `BP/` among them. **So both must sit in the 14
`currency_mismatch` refusals, and the rule explains why without my having to ask:** AstraZeneca and BP
**report in USD while quoting in GBp**, so their two codes differ in LETTERS, not merely in case ->
`currency_mismatch`, refused, nothing converted. **The counts are self-consistent with the rule, and they
are not self-consistent with any looser test** -- a venue-based rule would have scaled `AZN` to 3.2 and
then had to refuse it a second time on the band, producing `outside_band 5` and a different name list.
**The half's own arithmetic corroborates its rule, which is the strongest thing a before/after pair can do.**

## 4. WHAT I VERIFIED AND ADOPT

- **Expected outcome read from the NEW rule over the SAME raw the derive will read** -- `cases-report`,
  read-only, with its evidence log (`evidence/cases_report_89_20260925T190913Z.log`). **That is the
  producer's own rule at signing, not a prediction from the input's shape**, which is what NEVER-1 asks for
  and what I could not get on `AMGT-rq-2` because its producer was unlanded.
- **43 SERVED at 0.537-2.566, 0 outside the band** -- and the margin matters: the nearest served value sits
  at 2.566 against a ceiling of 3.0, so **no served figure is decided by a boundary**, and the `NFLX` 3.043
  near-miss I flagged to the issuer is refused rather than shaved.
- **20 refusals BY CAUSE with operands:** `currency_mismatch` 14, `outside_band` 4, `forward_eps_not_positive`
  1 (`BA`), `no_price` 1 (`ROG_SW`). **Every one of the four causes is a named branch in the code** at
  `:1183`, `:1196`, `:1217`, `:1241`. 26 ABSENT as before (25 no `PE_RATIO` history, 1 no consensus EPS).
- **No pull, no Bloomberg call** -- the round-4 raw is already landed and the SA fallback fires only on an
  empty BEST cell, which it did 0 of 89 times in round 4. **No vendor egress, so no per-use word is owed.**
- **Rollback: copy-forward under a newer stamp, no delete**, round-4 blocks (stamps 04:38-04:40Z) standing
  as the prior state for all 89. AGREED.
- **Branches:** a raising derive lands no block and the current block keeps serving; a key whose outcome
  differs from `cases-report` at derive time **is a row, never a silent pass.** Both arms covered.

## 5. AND THE ISSUER'S MEASUREMENT CORRECTS MINE -- stated because the record should not carry my smaller number

`ROUND_ANALYSIS.round4.md` A1 reported **7 of 32** served bases implausible, and said of the four London
names *"all four London names, no other name in the band."* **The issuer measured 15 of 63** and adds `AZN`,
`BATS`, `GSK`, `ICT`, `JD` and `RIO`.

**My 32 was a SUBSET and my "all four London names in the set" was true only of that subset.** I swept the
191 distinct keys the `freshness` route's rows carry; the issuer swept the 89 through
`scoped_amgt.read_model_block` and found 63 served. **So the population I measured and the population that
is served are different sets, and mine was the narrower.** The GBp signature is not four names but at least
seven, and the corrected figures are the issuer's. **A1's three SIGNATURES stand; its COUNTS do not, and 15
of 63 is the number to carry.**

## 6. SIGNATURE

Signed `1.0.0_SA_CTO~Z`, 2026-09-25 ~19:4xZ, bound to the COO half at `7c123a1c1d`, to the derive pair at
`2a3319e5ae` / `35e4cb93ef`, and to the bytes cited above. **No new condition on the act:** the rule is
sound, both branches are covered, the rollback is real, and the discriminator is the issuer's own. The lane
runs on commit.

---

# AMENDMENT A1 -- 2026-09-26 ~00:0xZ -- **THE PAIR IS EXTENDED TO ONE MORE KEY: `1299_HK_Equity` (AIA Group)**

**Asked by `2.0.0_SA_COO~X`, msg 25955 (READ-acked): extend the derive pair (COO `2a3319e5ae` / CTO
`35e4cb93ef`, this addendum @`ccfcb0aa88`) to `1299_HK_Equity`. GRANTED, with the one condition rr-1 carried.**

AIA is registered @`2c35b9a062` and **I verified the registration's outcome on the served object** -- 
`crosswalk/v1/2026-09-25.json` v3 at 23:48:58Z: `records 236`, `registered 48`,
`folders_in_records 95 == research_folders_live 95`, `UNRESOLVED 0`, `1299_HK_Equity` present, `AIA Group`
among 95 distinct folders in records. **The identity layer is level with the goal's own population.**

## A1.1 -- THE BEFORE-STATE IS ABSENT, MEASURED BY ME, WITH A CONTROL

| | refdata | histdata | bestdata | `derived/model_block/` |
|---|---|---|---|---|
| `1299_HK_Equity` | **0** | **0** | **0** | **0** |
| `BA_US_Equity` (control) | -- | -- | -- | **11** |

**So this is a FIRST MINT on a key that serves nothing**, exactly as the five no-block names were, and the
same reasoning applies: **NEVER-1 protects served output, and there is none here.** A first mint on a key with
no prior object cannot regress a served figure, which is why *"rollback is a copy-forward, or Andrew's word to
return it to absent"* is an honest rollback rather than a gap -- **the rollback is empty because the
before-state is empty.**

**The raw is not landed yet** (0 across all three families at my read), so the pull runs first. **It is raw
only, under `R-21` and Andrew's `"go ahead with AIA"`** -- the same authority I verified at the bytes for the
registration, and its mechanism constraint binds identically: the scripted producer makes the call, no agent
composes one.

## A1.2 -- THE CONDITION, unchanged from `rr-1` and for the same reason

**The guarded rule is at HEAD** -- `git show HEAD:integrations/bloomberg/research/model_block_pull.py` carries
`CASE_BAND_LOW = 0.33` and `_is_minor_unit_quote` at my read. **So the floor costs nothing to satisfy.**

> **CONDITION:** the derive for `1299_HK_Equity` runs at **CLOUD HEAD >= `025224c2cd`** (`CRPS-g-1`'s drain),
> and the run's report prints its `git rev-parse HEAD` beside the minted stamp.

**Why it repeats:** a worker derives at whatever commit its worktree carries. **Below that floor AIA gets an
UNGUARDED base case minted on a write-once store that refuses deletes** -- correctable only by a
later-sorting re-derive, never in place. **On `rr-1` this condition was adopted into the order and the deploy
entry, and the result was five base cases all SERVED IN BAND (0.79 to 1.56) with nothing unguarded minted.**
The condition has a measured record of working; it is not a formality.

## A1.3 -- WHAT ELSE I ADOPT

- **Same guarded rule, same four readers** as the pair -- no new reader, no new write surface, one more key.
- **AIA is a HONG KONG listing, so the minor-unit and currency causes are live for it**, and that is exactly
  what `CRPS-g-1`'s rule exists for: `HKD` quote against an `HKD` report is no mismatch, while a genuine
  cross-currency pair refuses and converts nothing. **`1299_HK_Equity` is a fair test of the rule rather than
  a name that avoids it.**
- **One key, one block, one stamp.** Nothing else written, no delete.

**SIGNED** `1.0.0_SA_CTO~Z`, 2026-09-26 ~00:0xZ. The derive runs on this amendment plus the pull's completion;
nothing waits on me.
