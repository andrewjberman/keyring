# POSN_ASTTAX -- surprise channel, ADJUDICATION v1 (round 1, site Z)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4a). **Lane:**
`TREE_CVO`, the CVO only. Round 1's CVO rows carry `POSN_ASTTAX-Z-C-S<k>`, `k` starting at 1.

**L8/L9 on the drain-end read `@a92a72abe0`** (`2.0.0_SA_COO~Z`, msg 21234). Per spine s.1 this seat's
engagement begins at L8, so the packet's arithmetic is **verified here, not accepted** -- all seven set
figures, the value-level agreement, the trigger zero and the channel row were each re-derived.

**L8 COMPILE, this seat's own read:** 1 investigation item, 1 OPEN, 1 ARMED, 0 defects, 0 malformed, 0
duplicate ids, 0 adjudication rows before this document. 1 of 1 task order terminal with a VALID proof
instance. Both L9 obligations are discharged here: the row is dispositioned (`C-S1`) and the round's one
judgment criterion is graded (`C-S2`).

> ⛔ **THE ROUND'S HEADLINE IS THAT BOTH CANDIDATE "ONE PLACES" FAIL, FOR DIFFERENT REASONS.** The dict
> explains 116 of 285 served entries and flows through a seed **nothing triggers**; the table is what
> serving reads but its shared entries are **silently overwritable** by that same untriggered seed. FWD-5
> is not a choice between them -- it is a trigger, an accounting for the 169, and only then a testable
> claim. Graded at `C-S2`.

> ⚠ **AND `C-S2` CORRECTS A CLAIM THIS SEAT RELAYED TO ANDREW.** The "one chain, not a fork" framing is
> true about the mechanism and incomplete about the coverage. `2.0.0_SA_COO~Z` caught its own version
> first; this seat repeated it without measuring. The set comparison, not the source read, is what
> settles it.

---

## C-S1 -- W1-S1: graduates, and UPGRADED -- is_hedge() is not broken, it has NO TRUE CASE over all 136 tickers

```json
[
  {
    "id": "POSN_ASTTAX-Z-C-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T06:55Z",
    "one_line": "GRADUATES, AND I AM UPGRADING IT: THE ROW UNDERSTATES ITS OWN FINDING. W1-S1 says the undocumented 'hedge' value 'silently breaks the module's own is_hedge() helper'. Measured by CALLING it: `HEDGE_TICKERS` is an EMPTY SET (len 0) while its siblings hold EQUITY_TICKERS 63 and FIXED_INCOME_TICKERS 66 (63+66+7 = 136, the dict's full count) -- so `is_hedge()` returns False for ALL 136 tickers, including the seven the dict itself classifies as hedge. ⛔ IT IS NOT A BROKEN PREDICATE, IT IS A PREDICATE WITH NO TRUE CASE: any caller branching on it takes the false branch unconditionally, for every security in the estate, forever. And the module's two access paths to the same fact DISAGREE -- `get_asset_class('GLD')` returns 'hedge' while `is_hedge('GLD')` returns False. The seven are GLD, IAU, SLV, DBC, GSG, USO, VIXY: precisely the gold, silver, commodity, oil and VIX instruments C-VOL-HEDGE-STRUCTURED exists to move, so this sits directly under FWD-2.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "POSN_ASTTAX-Z-W1-S1"
    ],
    "disarm_owner": "1.0.0_SA_CTO~Z, unchanged from the row's own field and NOT reassigned here. The disarm is a DESIGN call, not a typo fix, and that is why it is not the worker's: the vocabulary can be reconciled in three different directions and they are not equivalent. (a) ADD 'hedge' to the documented vocabulary and populate HEDGE_TICKERS -- smallest change, but it entrenches a fourth value the ratified taxonomy does not contain. (b) RETIRE 'hedge' by mapping those seven to the ratified classes now (six to Commodities, VIXY to Structured) -- correct destination, but it front-runs POSN_ASTTAX's own S1-b/S1-d cells and would be a cell writing a class definition before S1-a settles where such a definition survives. (c) DELETE is_hedge() as dead -- honest if nothing calls it, and a caller census is the precondition nobody has run. ⛔ THE ORDERING MATTERS AND IS THE REASON I AM NOT RECOMMENDING ONE: 2.0.0_SA_COO~Z's own S1-a argument is that a cell writing a class definition before the one-place question is settled 'is erased by the next seed run and looks like it worked until then'. Option (b) is exactly that shape.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ROW'S LITERAL CLAIMS, each re-measured at this seat by IMPORTING the module rather than grepping its source: ETF_CLASSIFICATIONS holds 136 entries; its value distribution is {fixed_income: 66, equity: 63, hedge: 7}; 'other' is assigned to ZERO tickers though it appears 5 times in the source as documentation; the seven hedge tickers are exactly GLD, IAU, SLV, DBC, GSG, USO, VIXY. All four confirmed.",
        "THE UPGRADE, AND IT IS THE PART THE ROW DOES NOT SAY: HEDGE_TICKERS is an EMPTY SET. `is_hedge(ticker)` is literally `return ticker in HEDGE_TICKERS`, so it cannot return True for any input. I tested it against EVERY dict key plus every HEDGE_TICKERS member -- 136 tickers, and the count of tickers for which is_hedge() is True is ZERO.",
        "THE CONTROLS PASS, which is what makes the zero a property of is_hedge() and not of my instrument: `is_equity` returns True for 21 of the first 80 dict keys, `is_fixed_income` for 59 of 80, and `get_asset_class` returns 'equity' for SPY, 'fixed_income' for AGG and 'hedge' for GLD. Three sibling helpers discriminate correctly; only is_hedge is dead.",
        "THE MECHANISM, inferred from the arithmetic and stated as an inference: 63 + 66 + 7 = 136 exactly, so the three ticker sets are derived from the dict by filtering on the DOCUMENTED vocabulary. Because the seven carry the UNDOCUMENTED value 'hedge', they match no documented bucket and fall into none of the three sets -- leaving HEDGE_TICKERS empty. The undocumented value did not corrupt a list; it caused a list to be built empty.",
        "WHY THE TWO-PATH DISAGREEMENT IS THE WORSE HALF: a reader who asks `get_asset_class` gets 'hedge' and a reader who asks `is_hedge` gets False, from the same module, about the same ticker, in the same process. Neither raises. A consumer that trusts either one is correct about the world and wrong about the other consumer.",
        "SCOPE, so the finding is not over-read: this is the AUTHORING module, not the serving path. Positioning serves from DynamoDB via ETFClassifier (Andrew-ruled canonical), and the live table's own seven hedge rows are present and correct -- I measured them separately at 285 rows, {equity 216, fixed_income 62, hedge 7}. So no served figure is currently wrong BECAUSE of this; the hazard is that any future code path using is_hedge() to make a decision silently takes the false branch."
      ]
    },
    "spec_asserts": "_shared/etf_classification.py documents a three-value asset-class vocabulary and offers is_hedge() as a predicate over it.",
    "world_is": "'other' is documented but never assigned; an undocumented fourth value 'hedge' is assigned to seven tickers; HEDGE_TICKERS is therefore empty and is_hedge() has zero true cases over all 136 tickers, while get_asset_class returns 'hedge' for the same tickers.",
    "notes": "⭐ THE CLASS, AND IT IS ONE THIS ESTATE HAS NOW MET FROM BOTH DIRECTIONS IN ONE NIGHT: A PREDICATE WITH NO TRUE CASE IS INDISTINGUISHABLE FROM A WORLD IN WHICH THE PROPERTY NEVER HOLDS. `is_hedge()` answering False everywhere looks exactly like an estate that owns no hedges, and nothing errors, nothing logs, and no test that only checks 'no false positives' can see it. Earlier tonight I graded two AMGT_RESAPP criteria FAIL for the same shape on the other side -- an ALWAYS-FAILS criterion and a bare-OR test where only the weakest arm bound. **The tell is identical in all three: ask what input would make this return the other answer, and find there isn't one.** ⚠ AND THE REASON THIS ROW IS ARMED rather than closed with the round: nothing about round 1 ending changes HEDGE_TICKERS. The predicate is still dead at HEAD and will answer False for the next caller."
  }
]
```

## C-S2 -- S1a-AC10 JUDGMENT GRADE: PASS, and the fork is RULED -- NEITHER end is FWD-5's one place

```json
[
  {
    "id": "POSN_ASTTAX-Z-C-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T06:55Z",
    "one_line": "S1a-AC10 (JUDGMENT, reserved to this seat) GRADED PASS, and the fork it reserves is RULED: NEITHER END IS FWD-5's 'ONE PLACE' AS THE SYSTEM STANDS, AND FWD-5 CANNOT BE CLOSED BY CHOOSING ONE. Every figure re-derived here: DICT 136, TABLE 285, in BOTH 116 with ZERO value-level asset_class mismatches, dict-only 20, table-only 169, union 305 -- all seven agreeing with the worker's script exactly. The chain is REAL (116 tickers agreeing perfectly on value is not coincidence) and covers 116 of 285. ⛔ THE DICT CANNOT BE THE ONE PLACE: editing it reaches 116 entries, never the other 169, and NOTHING TRIGGERS THE SEED -- my own census, wider than the worker's, found 101 references across 55,582 files and not one scheduler, EventBridge rule, CI workflow, deploy script or step function; the script's docstring instructs a human to 'run this whenever the classification source is updated'. ⛔ THE TABLE CANNOT BE THE ONE PLACE EITHER: it IS what serving reads, but a manual seed run overwrites the 116 from the dict, so a table edit is SILENTLY REVERTIBLE by an act with no schedule and no announcement.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grades": [
      {
        "criterion": "S1a-AC10",
        "instance": "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~1/POSN_ASTTAX.TO-S1A-1.which-one-place-survives-the-seed.proof_of_spec.json@a92a72abe0",
        "verdict": "PASS",
        "reason": "THE ASSIGNEE DID EXACTLY WHAT THE CRITERION REQUIRED -- assembled the instruments over both stores and offered NO verdict, leaving the fork to this seat. That is the correct handling of a judgment criterion and is not a shortfall. Its figures are not merely plausible; I re-derived ALL SEVEN independently and they agree exactly: DICT_COUNT 136 (by importing the module, after my own first attempt -- a regex over the source -- returned a FALSE ZERO and had to be thrown away), TABLE_COUNT 285 (full scan, Count == ScannedCount, so complete and not a page), in BOTH 116, dict-only 20, table-only 169, union 305, disagreement 189, and ZERO value-level asset_class mismatches across the 116. THE RULING THE CRITERION RESERVES. Neither end qualifies, for DIFFERENT and non-substitutable reasons. (1) THE DICT is not the one place on COVERAGE: it explains 116 of 285 served entries, so 169 table tickers -- 166 of them 'equity', 3 'fixed_income' -- are not reducible to its output at all. Something other than this seed populated most of the table, or it was seeded from a wider source the dict has since narrowed away from; either way an edit to the dict cannot reach them. (2) THE DICT is also not the one place on FLOW: a source that flows nowhere is not a source. The seed has NO trigger -- 101 references over 55,582 files, zero of them a scheduler, rule, workflow, deploy script or step function, and the script's own docstring asks a human to run it. FWD-5's bar is 'defined in one place and FLOWS EVERYWHERE', and the flow mechanism does not exist. (3) THE TABLE is not the one place on DURABILITY: it is authoritative for serving (Andrew ruled ETFClassifier canonical, and Positioning's lambda imports it), but the 116 shared entries are overwritable by a manual seed run at any time, so a correction made in the table is silently revertible by an act with no schedule -- and it would look like it worked until the day someone ran the seeder. SO FWD-5 IS NOT A CHOICE BETWEEN TWO PLACES; IT IS THREE PIECES OF WORK, and this is the operative half of the grade: (i) give the seed a TRIGGER, or delete the seed and author directly in the table -- until one of those, the two carriers can diverge with nothing announcing it; (ii) ACCOUNT FOR THE 169, because a single source that explains 41% of what is served is not a single source; (iii) only then is 'one place' a meaningful claim to test. ⭐ AND THE ZERO VALUE-LEVEL MISMATCHES IS THE MOST INTERESTING NUMBER IN THE SET, because it cuts against the conclusion: the 116 agree PERFECTLY, which is strong evidence the chain is real and was run. The mechanism is sound and the coverage is not, and a reader who saw only the 116 would conclude the architecture works. PASS."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SET ARITHMETIC, my own, against the live table and the imported module: DICT 136 / TABLE 285 / BOTH 116 / dict-only 20 / table-only 169 / union 305 / disagreement 189. Identical to the worker's compare_table_to_dict.py on every one of the seven figures.",
        "VALUE-LEVEL: 0 mismatches on the 116 shared tickers -- every shared ticker carries the same asset_class in both stores.",
        "THE DISTRIBUTION OF THE DISAGREEMENT, which nobody had stated and which sharpens S1-c: the 169 table-only entries are {equity: 166, fixed_income: 3}, and the 20 dict-only are {equity: 13, fixed_income: 7}. So 166 of the 169 unexplained rows carry 'equity' -- the SAME value the positioning lambda uses as its unknown-default (lambda_function.py:359, 'Default to equity if unknown'). The served 'equity' bucket therefore mixes dict-classified, unexplained-source, and defaulted-unknown rows with nothing distinguishing them.",
        "THE TRIGGER ZERO, verified at a WIDER denominator than the criterion's: the worker measured 45 hits over 30,964 files; I re-ran it and read 101 hits over 55,582 files, inspecting every band (HEAD 33 / SURFACED 25 / CONFIG 7 / DOC 36). Not one is a scheduler, EventBridge rule, CI workflow, deploy script or step function -- they are source docstrings, inbox and archive prose, decomp and PRD text, graph/census JSON, and comp-tool logs. A zero re-measured on a bigger population is the only kind worth acting on.",
        "THE SCRIPT'S OWN WORDS, read at source rather than inferred from the absence: 'This script populates the centralized ETF classification table from the canonical etf_classification.py source. Run this whenever the classification source is updated to keep DynamoDB in sync.' An instruction addressed to a person is not a mechanism.",
        "TABLE AUTHORITY, corroborating Andrew's ruling rather than restating it: yang-generate-positioning/lambda_function.py:25 imports ETFClassifier and :31 instantiates it; seed-etf-classifications.py:36 writes dynamodb.Table('etf-classifications'), the same table ETFClassifier.__init__ defaults to at :52. Serving reads the table; the dict reaches serving only through the untriggered seed."
      ]
    },
    "spec_asserts": "S1a-AC10 reserves to 3.0.0_SA_CVO~Z the judgment of which end of the classifier chain is FWD-5's 'one place', and instructs the assignee to record instruments without a verdict.",
    "world_is": "Neither end qualifies: the dict explains 116 of 285 served entries and flows through a seed that nothing triggers, and the table is authoritative for serving but its shared entries are silently overwritable by that same untriggered seed.",
    "notes": "⚠ THIS GRADE CORRECTS A CLAIM I RELAYED TO ANDREW AND SHOULD BE READ AS A CORRECTION TO MY OWN REPORT. 2.0.0_SA_COO~Z broadcast that the two modules are 'ONE CHAIN, NOT A FORK' -- the dict seeds the table -- and I repeated that to Andrew as settled. It is true about the MECHANISM and incomplete about the COVERAGE, and the gap is most of the table. 2.0.0_SA_COO~Z corrected itself first (msg 21234, 'I read the seed line and generalised from it'), and my repetition inherited the same generalisation without measuring it. ⭐ A CHAIN DEMONSTRATED AT ONE LINK IS NOT A CHAIN DEMONSTRATED AT ITS COVERAGE: `ETF_CLASSIFICATIONS.get(ticker, 'unknown')` proves the dict CAN reach the table, and says nothing about how much of the table it reaches. The measurement that settles it is a set comparison, not a source read, and neither of us ran it before asserting. ⛔ THIS ROW DOES NOT AMEND FWD-5 OR THE PRD -- naming what 'one place' must mean is an L2/L4 act. It grades the criterion and rules the fork the criterion reserves, and routes the three pieces of work to 1.0.0_SA_CTO~Z and the S1-a cell."
  }
]
```

## C-S3 -- CORRECTION to C-S2's coverage limb, on Andrew-direct ~07:1xZ: the 169 are attributed, and a hand-curated list needs no scheduler

```json
[
  {
    "id": "POSN_ASTTAX-Z-C-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T07:20Z",
    "one_line": "CORRECTION TO C-S2, MADE BY A NEW ROW AND NOT BY EDITING IT. Andrew-direct at this terminal ~07:1xZ described what ETFClassifier IS FOR: a DEVELOPING, HAND-CURATED LIST of how we tag the securities we own -- low churn by design, added to as needed, to keep proper capitalization and proper sub-asset-class. Measured against that, TWO OF C-S2's THREE LIMBS COLLAPSE. (1) The 169 table-only entries are NOT UNEXPLAINED: `updated_by` names their author -- 169 written by `seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)`, a DIFFERENT AND DELIBERATE seeder, plus 59 placeholder-name-sweep, 55 attr-restore-from-_shared, 1 vug-naming-fix, 1 canonical_si_seed = 285 with every entry attributed. (2) The seed's missing TRIGGER is not a defect: for a list a person extends when the firm acquires a security, A PERSON IS THE MECHANISM, and demanding a scheduler invents a requirement the artifact's purpose excludes. So C-S2's 'NEITHER end is one place' is WRONG IN EMPHASIS -- the TABLE is the list, and the hardcoded dict is a superseded seed input that fell behind. Andrew's earlier ruling was right and simpler than my elaboration of it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ANDREW-DIRECT at the 3.0.0_SA_CVO~Z terminal 2026-09-11 ~07:1xZ, the operative words: ETFClassifier is 'basically a developing list of how we tag securities we own. We do not trade really fast or move through so many securities, so we basically just add things there as we need to in order to keep securities with proper capitalization, proper sub asset class, etc etc'. A statement of PURPOSE, which is not a thing this seat can measure and is taken on his word as the product owner.",
        "THE PROVENANCE I FAILED TO READ, measured after his correction by projecting `updated_by`, a field that was in the table the whole time: 169 `seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)`; 59 `1.0.0_SA_CTO~X placeholder-name-sweep`; 55 `1.0.0_SA_CTO~X attr-restore-from-_shared (put_item drop casualty, Andrew chase-down)`; 1 vug-naming-fix; 1 canonical_si_seed. Sums to 285. ZERO entries lack an author.",
        "THE DATES CONFIRM DELIBERATE ACTS RATHER THAN DRIFT: 169 on 2026-08-25, 115 on 2026-08-18, 1 on 2026-03-25. Three dated operations by named seats, two of them on Andrew's own word.",
        "THE ARTIFACT IS DOING THE JOB HE DESCRIBES: `sub_asset_class` is populated on 282 of 285 rows across 31 distinct values (Information Technology 32, Financials 29, US Large Cap 25, Industrials 21, Ultra Short Duration 16, Intermediate 14 ...). A registry whose stated purpose is proper sub-asset-class tagging is 98.9% populated on exactly that field.",
        "⛔ AND THE ANSWER WAS IN A FILE I HAD ALREADY LISTED. `seed-etf-constituents.py:10` opens with 'THE UNIVERSE THIS SEEDS IS DIFFERENT FROM `seed-etf-classifications.py`, AND THAT IS THE POINT', and :17 explains why: a model's ETF list is stable so it can be frozen as literals, a fund's constituents are not. That file appeared in MY OWN comp-find output when I measured the trigger zero. I read the line and did not connect it."
      ]
    },
    "spec_asserts": "C-S2 ruled that NEITHER end of the classifier chain is FWD-5's 'one place', on the grounds that the dict explains only 116 of 285 served entries and that the seed carrying it has no trigger.",
    "world_is": "The other 169 entries are attributed to a second deliberate seeder run on Andrew's direct word, and the absent trigger is appropriate to a hand-curated registry a person extends as securities are acquired. The table is the living list; the dict is a superseded seed input.",
    "notes": "WHAT SURVIVES C-S2 UNCHANGED, because the correction is to its coverage reasoning and not to its measurements: the seven set figures are still exact (136 / 285 / 116 / 20 / 169 / 305 / 189), ZERO value-level mismatches across the 116 still holds, and the two findings that matter are untouched. (a) `is_hedge()` still has NO TRUE CASE over all 136 tickers -- C-S1 stands entirely. (b) `equity` is still BOTH a real class and the serving code's unknown-default (lambda_function.py:359), and ⭐ THAT ONE MATTERS MORE UNDER HIS FRAMING, NOT LESS: if the whole purpose is keeping securities properly tagged, then a bucket where 'properly tagged as equity' and 'not recognised' are the same string is precisely the thing that cannot be audited. (c) The ratified vocabulary is FIVE and the store holds THREE, so Commodities and Alternatives still do not exist as values -- real work, and it is ADDITIVE to a curated list rather than a migration of a broken one. (d) 3 of 285 rows carry a blank sub_asset_class: on his account that, not the 169, is the actual coverage gap. ⭐ THE METHOD LESSON, AND IT IS THE THIRD TIME TONIGHT I HAVE HIT THE SAME SHAPE FROM A DIFFERENT ANGLE: I CALLED 169 ROWS 'UNEXPLAINED' WITHOUT READING THE FIELD THAT NAMES WHO WROTE THEM. I projected `ticker` and `asset_class` because those were what my hypothesis needed, got a clean set-difference, and reported the residue as a mystery. `updated_by` and `last_updated` were sitting in every row. **A set difference tells you two sets differ; it never tells you why, and PROVENANCE FIELDS ARE WHERE THE WHY USUALLY IS.** Ask what the record already says about itself before calling any part of it unaccounted for. ⚠ And the deeper one: I was measuring an artifact against a purpose I had inferred (a single-source-of-truth architecture) rather than the purpose it has (a curated tagging list). Every measurement was correct and the frame was wrong, which no amount of further measuring would have corrected."
  }
]
```
