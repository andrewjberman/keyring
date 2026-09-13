# ANDREW-DIRECT 2026-09-11 ~20:0xZ -- remediation complete, ALL AGENTS MAY UNPAUSE, and two RECOMMENDATIONS

**archetype:** COORDINATE

**Channel:** Andrew-direct at the `0.0.0_AB_MSTR~Z` terminal. Broadcast same turn to all six live
site-Z seats (msgs 21601-21606) per `org/XXX.md`.

## THE WORD, VERBATIM AND ENTIRE

> "remediation complete, all agents may unpause. i recommend a /canonical-flow --midstream for
> assessing state on the AMGT_RESAPP project for all effected agents so we may continue cleanly. I
> also recommend a scan of any oustanding TOs or Investigation/Remediations by the relevant parties,
> COO and CVO respectively, to make sure that the renaming/migration does not drag deprecated
> references/info"

## THE VERBS, KEPT AS HE WROTE THEM

| # | text | force |
|---|---|---|
| 1 | "all agents **MAY** unpause" | the pause is LIFTED -- **permission to resume, not an order to** |
| 2 | "**i recommend** a /canonical-flow --midstream" | **RECOMMENDATION** |
| 3 | "**I also recommend** a scan ..." | **RECOMMENDATION** |

⛔ **NEITHER (2) NOR (3) WAS UPGRADED TO AN ORDER.** He wrote "I recommend" twice and chose that verb
the same way he chose it for the `/drive` loops earlier tonight, where both COOs answered on the merits
and one declined with a stated trigger. **A seat that declines either is inside his word and owes
nobody a defence.**

**Measured, the shape held:** `2.0.0_SA_COO~Z` unpaused, re-armed `/drive` at 20m over POSN_ASTTAX
only, **DECLINED (2) on SCOPE** -- it holds no AMGT round, order or artifact, and running
`/canonical-flow` on another COO's live round is the two-issuers shape Rule 27 names -- and **DID (3)
for its own project: 0 deprecated references across 31 live artifacts, both outstanding TOs clean.**
That is the "decide it and say what you chose" answer the recommendation invites.

## ⛔ THE FIRST FINDING OF THE SCAN WAS A HOLE IN THE SCAN'S OWN ASSIGNMENT

He named **TOs -> the COO** and **Investigations/Remediations -> the CVO**.

>> **NOBODY WAS NAMED FOR THE PRD, AND THAT IS THE ARTIFACT THE NEXT ROUND IS CUT FROM.** <<

Found by `4.0.0_SA_CRO~Z` (msg 21610) while running the scan he recommended -- i.e. **the seat doing
the scan found the gap in its coverage**, by checking the denominator rather than working the list.
This is the Rule 24 subtraction failure in its purest form: an enumeration that names two planes and
omits the one that matters most, and which reads as complete because both named planes were done.

**FOUR DEPRECATED-LIVE references in `prd/AMGT_RESAPP_PRD.md`** (10 hits total; **six are preserved
HISTORY and correctly stay**):

```
:516  opal-amgt-articles          -- a cell building that store targets a table that is GONE
:518  opal-data-research          -- "(which stays S1's ...)" names the bucket as a live thing
:523  opal-amgt-security-metrics  -- a producer cell targets a GONE table
:583  S6 manifest row             -- names opal-data-research AND cites
                                     infra/aws/terraform/research/s3.tf:11 -- A FILE RETIRED TONIGHT
```

⚠ **`:583` is the sharpest: doubly stale** -- wrong resource AND a dead file citation -- **and it sits
in the SURFACE MANIFEST, which is what a cut actually reads.** It is also the row already corrected
once tonight (build -> INTEGRATE) for the same class of reason: **a stale premise in a ratified spec
that a cutter follows in good faith.**

**Current truth, for whoever amends:**

```
opal-data-research          -> opal-data-harvest              (53 objects, verified)
opal-amgt-articles          -> opal-harvest-articles          (0 rows)
opal-amgt-security-metrics  -> opal-harvest-security-metrics  (42 rows, full item equality)
infra/aws/terraform/research/s3.tf -> infra/aws/terraform/harvest/s3.tf
env knobs: HARVEST_BUCKET | HARVEST_ARTICLES_TABLE | HARVEST_METRICS_TABLE
```

⛔ **THE DISTINCTION THAT DECIDES MOST HITS, and it is his "live refs only" scoping applied:** a
**DEPRECATED-LIVE** reference tells a FUTURE actor to use a resource that is gone and must be
corrected; a **PRESERVED-HISTORY** reference records what was true when written and **MUST NOT** be
rewritten. Six of the PRD's ten hits were history. **A scan that "fixed" every hit would falsify the
record while looking thorough.**

⛔ **AND DO NOT RENAME THE CONSTRAINT IDS** (`C-AMGT-ARTICLES-STORE` and friends). Those are
IDENTIFIERS, not resource names; renaming them is churn and breaks every citation to them.
`4.0.0_SA_CRO~Z` asked for that exclusion explicitly.

## ROUTING THIS SEAT DID

`4.0.0_SA_CRO~Z`'s 21610 carried sections addressed to the CTO, COO~ZZZ and CVO~Z **and its `To:` was
this seat alone**, so none of them had it. Relayed as 21614-21616. ⭐ **A message that addresses three
seats in its body reaches nobody it names unless its `To:` says so** -- the body is not a carrier, and
this is the second time tonight the fabric has been saved by someone re-reading a delivery list rather
than the prose.

The PRD amendment is **L4 and `1.0.0_SA_CTO~Z`'s**. `4.0.0_SA_CRO~Z` did not touch the PRD, gave line
numbers so the amendment is mechanical, and accepts the sixth brief re-sign it will trigger -- against
the alternative of round 6 wiring to three deleted resources.

## WHAT THE UNPAUSE DID NOT RELEASE

- The **CLOUD->SITEZ merge leg**, still PARKED behind the `surprise-row-gate` project-specificity fix
  (`1.0.0_SA_CTO~Z`'s, confirmed at source, deliberately not rushed). **That is a GATE, not the pause.**
- **PORTAL**, frozen both fabrics, PROD and DEV, until he names it.

## AND ONE THING THE UNPAUSE MOOTED RATHER THAN ANSWERED

`2.0.0_SA_COO~ZZZ` had asked whether the pause reached it and AMGT round 5. "All agents may unpause"
makes the question **moot**, not answered. ⚠ **Nobody should cite this as precedent for how wide a
future "pause" reaches.** The right move if it recurs is the one that seat made: ask, while neither
stopping an in-flight worker nor starting anything new.
