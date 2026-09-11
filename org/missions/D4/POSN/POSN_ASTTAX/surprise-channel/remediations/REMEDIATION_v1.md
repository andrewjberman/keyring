# POSN_ASTTAX -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-1 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 1, 2026-09-11 ~07:0xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, ALL THREE LIMBS -- and I censused the third MYSELF, because it is the one I missed on
AMGT_RESAPP earlier tonight and was corrected on.**

```
LIMB 1  task orders       1 of 1 TERMINAL (full-pair <status> read, occ-unique 1, no conflict),
                          1 of 1 carrying a VALID proof instance
LIMB 2  channel           1 item | 0 UNDISPOSITIONED | 0 defects | 0 malformed | 0 duplicate ids
LIMB 3  judgment grades   1 of 1 flagged (S1a-AC10), 1 of 1 GRADED -- PASS at C-S2
```

**WHAT THIS SLUG CARRIES:** two rows, both ARMED, neither disarmed by the round ending. No row carries a
`route` -- the three route tokens are retired under spine v3.

> ⛔ **THE ROUND'S HEADLINE IS A NEGATIVE RESULT, AND IT IS THE USEFUL KIND.** Both candidate answers to
> FWD-5's "one place" FAIL, on different axes, so the outcome cannot be closed by picking between them.
> The dict explains 116 of 285 served entries and flows through a seed **nothing triggers**; the table is
> what serving reads but its shared entries are **silently overwritable** by that same seed. A round that
> establishes the question was wrong is worth more here than one that answered it.

> ⚠ **AND THE ROUND CORRECTED A CLAIM THIS SEAT HAD RELAYED TO ANDREW** -- that the two modules are "one
> chain, not a fork." That is true about the MECHANISM and incomplete about the COVERAGE, and the gap is
> most of the table. `2.0.0_SA_COO~Z` caught its own version first; this seat repeated it without
> measuring. **A chain demonstrated at one LINK is not a chain demonstrated at its COVERAGE**, and the
> instrument that settles it is a set comparison, not a source read.

---

```json
[
  {
    "id": "POSN_ASTTAX-Z-W1-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "_shared/etf_classification.py documents a THREE-value vocabulary (fixed_income, equity, other), assigns 'other' to ZERO tickers, and assigns an UNDOCUMENTED fourth value 'hedge' to seven. The three ticker sets are filtered on the DOCUMENTED vocabulary, so those seven match no bucket and HEDGE_TICKERS is built EMPTY. is_hedge() is literally `return ticker in HEDGE_TICKERS`, so it has NO TRUE CASE over all 136 tickers. It is not a broken predicate; it is a predicate that cannot fire, and any caller branching on it takes the false branch unconditionally, forever.",
    "evidence": [
      "Measured by IMPORTING the module rather than grepping it: EQUITY_TICKERS 63, FIXED_INCOME_TICKERS 66, HEDGE_TICKERS 0. 63+66+7 = 136 exactly, which makes the derivation mechanism visible.",
      "is_hedge() tested against every dict key plus every HEDGE_TICKERS member -- 136 tickers, TRUE for ZERO, including the seven the dict itself classifies as hedge.",
      "CONTROLS PASS, so the zero is a property of is_hedge and not of my instrument: is_equity TRUE for 21 of the first 80 dict keys, is_fixed_income for 59 of 80, get_asset_class correct for SPY (equity), AGG (fixed_income) and GLD (hedge).",
      "THE TWO-PATH DISAGREEMENT: get_asset_class('GLD') returns 'hedge' while is_hedge('GLD') returns False. Same module, same ticker, same process, neither raising. A consumer trusting either is correct about the world and wrong about the other consumer.",
      "SCOPE, so it is not over-read: this is the AUTHORING module. Serving reads DynamoDB via ETFClassifier and the served table's seven hedge rows are present and correct (285 rows, equity 216 / fixed_income 62 / hedge 7). No served figure is currently wrong BECAUSE of this; the hazard is the next code path that asks is_hedge() to decide something."
    ],
    "remedy": "A DESIGN call with three non-equivalent directions, which is why it is not a typo fix. (a) DOCUMENT 'hedge' and populate HEDGE_TICKERS -- smallest change, but entrenches a fourth value the ratified taxonomy does not contain. (b) RETIRE 'hedge' by mapping the seven to ratified classes: SIX TO COMMODITIES (DBC, GLD, GSG, IAU, SLV, USO) and VIXY TO STRUCTURED -- a split this seat ruled from the authoring dict and 2.0.0_SA_COO~Z independently confirmed from the served table's own sub_asset_class field (Commodities 2, Gold 2, Silver 1, Oil 1, Volatility 1). Correct DESTINATION, wrong TIMING. (c) DELETE is_hedge() as dead -- honest if nothing calls it, and a CALLER CENSUS is the precondition nobody has run. ORDERING IS THE LOAD-BEARING PART: settle S1-a's carrier question FIRST, then retag in whichever carrier survives. A retag today is a cell writing a class definition before S1-a settles where such a definition survives the seed -- the shape 2.0.0_SA_COO~Z described as erased by the next seed run and looking like it worked until then.",
    "owner": "1.0.0_SA_CTO~Z, unchanged from the row's own disarm_owner and NOT reassigned here.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z -- the vocabulary reconciliation, after S1-a settles the carrier",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z -- the vocabulary reconciliation, after S1-a settles the carrier",
      "at": null
    }
  },
  {
    "id": "POSN_ASTTAX-Z-C-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "FWD-5 asks that the classification be defined in one place and flow everywhere. NEITHER candidate end qualifies, on different and non-substitutable axes. The DICT fails on COVERAGE (it explains 116 of 285 served entries; 169 are not reducible to its output) and on FLOW (the seed carrying it to the table has NO trigger). The TABLE fails on DURABILITY (it is what serving reads, but its 116 shared entries are silently overwritable by that same untriggered seed). FWD-5 is therefore not a choice between two places -- it is three pieces of work.",
    "evidence": [
      "SET ARITHMETIC re-derived at this seat, agreeing with the worker's script on all seven figures: DICT 136 / TABLE 285 / BOTH 116 / dict-only 20 / table-only 169 / union 305 / disagreement 189.",
      "ZERO value-level asset_class mismatches across the 116 shared tickers. Stated because it CUTS AGAINST the conclusion: the chain is REAL and was run. The mechanism is sound and the coverage is not, and a reader who saw only the 116 would conclude the architecture works.",
      "THE TRIGGER ZERO, verified at a WIDER denominator than the criterion's -- the worker read 45 hits over 30,964 files, I read 101 over 55,582 and inspected every band (HEAD 33 / SURFACED 25 / CONFIG 7 / DOC 36). Not one is a scheduler, EventBridge rule, CI workflow, deploy script or step function; they are docstrings, inbox and archive prose, decomp and PRD text, census JSON and comp-tool logs.",
      "THE SCRIPT'S OWN WORDS, read at source rather than inferred from an absence: 'Run this whenever the classification source is updated to keep DynamoDB in sync.' An instruction addressed to a person is not a mechanism.",
      "THE DISTRIBUTION OF THE UNEXPLAINED 169, which nobody had stated: equity 166, fixed_income 3. So 166 carry 'equity', the SAME value the positioning lambda uses as its unknown-default (lambda_function.py:359). The served equity bucket mixes dict-classified, unexplained-source and defaulted-unknown rows with nothing distinguishing them.",
      "TABLE AUTHORITY: yang-generate-positioning/lambda_function.py:25 imports ETFClassifier and :31 instantiates it; seed-etf-classifications.py:36 writes the same table ETFClassifier.__init__ defaults to at :52. Serving reads the table; the dict reaches serving only through the seed."
    ],
    "remedy": "THREE PIECES, in order, the first a precondition for the rest: (i) GIVE THE SEED A TRIGGER, or delete the seed and author directly in the table -- until one of those, the two carriers can diverge with nothing announcing it; (ii) ACCOUNT FOR THE 169, because a single source explaining 41 percent of what is served is not a single source; (iii) only then is 'one place' a claim worth testing and FWD-5 becomes gradeable. Fold in making UNKNOWN distinguishable from equity, or (ii) cannot be audited -- you cannot inventory what you cannot tell apart from the default.",
    "owner": "1.0.0_SA_CTO~Z at L2/L4 for what 'one place' must mean; the S1-a cell for the carrier decision.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z with the S1-a cell via 2.0.0_SA_COO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z with the S1-a cell via 2.0.0_SA_COO~Z",
      "at": null
    }
  }
]
```
