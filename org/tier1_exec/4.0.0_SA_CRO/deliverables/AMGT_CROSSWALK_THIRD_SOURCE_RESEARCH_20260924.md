# R-23 design fork: a THIRD crosswalk registration source over the 2,851-row scanner member space -- measured, and a recommendation

**Author** `4.0.0_SA_CRO~Z` -- **Date** 2026-09-24 ~05:0xZ -- **Routed by** `1.0.0_SA_CTO~Z` (msg 25215, R-23
@`c935039efd`): *"does registering a 2,851-row scanner MEMBER space as a THIRD crosswalk registration source, under
the existing refusal rules, preserve the crosswalk's 'never guessed' property -- or does it approach the
make-any-key-resolvable state R-14 refused?"* -- **Authority to research and hand off:** Andrew-direct at this
terminal ~04:5xZ, *"your recommendations on whatever else, if you need to do more research first go ahead but
otherwise hand off to CTO!Z"*.

## Answer in one line

**Yes, bounded: it preserves "never guessed" because the rule refuses 1,812 of the 2,851 rows by construction and
registers only the 1,039 whose own row states both a ticker root and the country the exchange code is read from.**
It is the builder converging up to the producer, which is R-14's endorsed direction, and it is the mirror image of
the precedent that created the stranded sets.

## What was measured (instrument, denominator, vintage)

Instrument: the ranker's own cached candidate database,
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/candidate_universe.json` (2,851 rows,
vintage 2026-08-06, read 2026-09-15; the union of the six scanner `universe_data.json` files, which this seat also
downloaded live at 05:0xZ from `opal-data-portal-v2`), joined against `crosswalk/v1/2026-09-22.json` (96 records,
36 MEASURED keys; the 2026-09-24 object published at 03:32Z adds the 158 subject keys and was not re-read here)
and the `peers/v1/` listing (797 objects). Python over the JSON, this seat, 05:0xZ.

| measure | value |
|---|---|
| rows in the member space | 2,851 |
| rows already carrying a `security_key` (the union join) | 3 |
| identifier shape: alpha root (1-6 letters) | 1,132 |
| of which country == United States | **1,039** |
| of which non-US | 93 |
| identifier shape: SEDOL-shaped (six characters with digits) | 1,466 |
| identifier shape: asterisk-prefixed (Canadian, e.g. `*ABX`) | 78 |
| identifier shape: root with a class separator (`.`/`-`/`/`) | 6 |
| identifier shape: other | 169 |
| tickers appearing under more than one country | **0** |
| minted `<ROOT>_US_Equity` keys already a crosswalk key (same identity) | 9 |
| US roots already a bare-root PILOT alias in the crosswalk | 5 (`BA`, `COST`, `HAL`, `HD`, `VLO`) |
| minted US keys that already have a `peers/v1` object | 119 of 1,039 |
| Boeing's twelve comparables: US alpha roots, one country each | 12 of 12 (`DE` is Deere and Company, United States) |

## Why it preserves "never guessed"

The crosswalk's own text names two admissible ways a form enters: MEASURED on a persisted surface, or DERIVED BY A
RULE READ FROM A SOURCE FILE. A scanner row is a persisted surface (`opal-data-portal-v2/json/security_scanner/
latest/universes/*/universe_data.json`, vintage stamped), and it carries two fields the rule reads: `ticker` and
`country`. The rule `ticker matches the root shape AND country == "United States" -> <ROOT>_US_Equity` appends
nothing the row does not say. That is not "guessed as US": the row states US.

Everything the row does NOT state stays UNRESOLVED, exactly as `_parse_bloomberg` disposes today:
- a non-US alpha root (93 rows) carries no exchange code and the country-to-exchange mapping is NOT on the row
  (United Kingdom is `LN`, Canada `CN` or `CT`, Japan `JP` or `JT`; a share class changes it), so it is refused;
- SEDOL-shaped, asterisk-prefixed, class-separated and other identifiers (1,719 rows) carry no root, so they are
  refused;
- a collision would be refused by `_build_index` as AMBIGUOUS, and none exists: zero tickers appear under two
  countries.

So the refusal rate of the third source is **64% (1,812 of 2,851), printed, not discovered.** A source that says no
to two rows in three under its own rule is not "any key resolvable"; it is a fourteen-times-wider space of which
about a third is measurable.

## Why it is not what R-14 refused

R-14 refused THE ROUTE accepting a landed peers object's own identity block: a resolver trusting the artifact it is
resolving. This proposal adds a REGISTRATION SOURCE IN THE BUILDER (`build_crosswalk`, beside the coverage list and
`registrations.json`), so the route keeps one resolver and one object and gains nothing but rows. The line is
builder versus resolver, and this is on the builder side.

## The precedent the CTO asked for, and it argues FOR the builder

The estate has widened a registration space by an order of magnitude once: AMGT-rk-4's widened identity set gave
the RANKER 191 keys while the CROSSWALK stayed at 36. Measured in the Peers trace brief (`d350781052`): 158 of the
191 landed peer objects were UNRESOLVED at the route, 111 of them real derived sets, and the fix was the crosswalk
re-mint the CTO ruled at R-14(c) and `2.0.0_SA_COO~Z` published at 03:32Z. That is the cost of widening the
PRODUCER without the BUILDER. Deere is the same shape one hop down: the ranker mints `DE_US_Equity` for a member
and the builder has never heard of it. Widening the builder to the member space is the same remedy applied before
the next stranding, not after it.

## The recommendation, as five bounds

1. **Register only rows with an alpha root AND `country == "United States"`, keyed `<ROOT>_US_Equity` by the row's
   own country field.** Everything else stays UNRESOLVED with the reason carried ("scanner row carries no exchange
   code"). The 1,812 refusals are printed beside the 1,039 registrations in the builder's denominators.
2. **Existing records WIN.** The builder raises on a second row for one key today (`build_crosswalk`, "never
   appended, never guessed"); the member source is applied last and SKIPS a key the coverage list or
   `registrations.json` already holds (9 today), recording `also_in_scanner: true` on the winning record. It never
   overwrites an identity a richer source measured.
3. **Alias forms for a member record are the canonical key and the `<ROOT> US` Bloomberg form only -- never the
   bare root.** The bare-root convention is the harvester's PILOT convention (five names, measured: `BA`, `COST`,
   `HAL`, `HD`, `VLO`); giving 1,039 members a bare-root alias would make every bare US root resolvable and would
   collide with those five. This bound is what keeps the third source from becoming "any key".
4. **A member record carries its claim.** `basis: scanner-member`, the scanner vintage (2026-08-06 today), the
   universe ids and the row's `mktVal`, so a consumer can reject on it: Posture may NAME a comparable through it;
   the analysis layer treats a scanner-member identity as thinner than a registered one; nothing inducts a name
   into the corpus from it (the America Movil refusal and the calls-not-picks line are untouched).
5. **The member source re-mints when the scanner vintage moves**, which couples it to the scripted Security
   Scanner refresh brief (`docs/briefs/sscn-scripted-refresh-brief-20260924.md`): a fresh screening export changes
   the member space, so the crosswalk builder's third source reads the scanner's `asOf` and the re-mint follows the
   refresh. Today's vintage is seven weeks old; that is a freshness fact, not a reason to wait.

Under these bounds `DE_US_Equity` resolves after the next re-mint, Posture's Boeing comparable stops reading
UNRESOLVED, and the 1,812 refusals stay visible as refusals.

## The alternative, priced

"Posture names only comparables inside the crosswalk" keeps the crosswalk small and renders UNRESOLVED for
legitimate comparables on a real screen: with 158 subject keys registered and the member space at 2,851, the ranker
will keep choosing comparables the builder has never heard of, and every one reads UNRESOLVED to the person the
page is for. That price is paid on the screen, in the Posture tab's first line, on every name. The third source's
price is one builder change, one registry row for the source, and a re-mint per scanner vintage.

## Not measured here

The 2026-09-24 crosswalk object (523,207 bytes) was not re-read; the 9 same-identity collisions were measured
against the 2026-09-22 object and are a floor. The 93 non-US alpha roots were not checked against a
country-to-exchange table because no such table is ratified on the estate; if one is, it is a registry row and a
separate ruling, not part of this recommendation. The scanner's own `name` field was not used for any matching and
should not be. No builder was run and nothing was written to the pool.
