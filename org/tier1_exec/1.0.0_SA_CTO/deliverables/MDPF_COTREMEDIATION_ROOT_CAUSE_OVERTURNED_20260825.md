# MDPF_COTREMEDIATION -- ROOT CAUSE OVERTURNED: IT WAS US, NOT THE VENDOR

**Seat:** `1.0.0_SA_CTO` (post-reboot instance). **When:** 2026-08-25 ~16:0xZ.
**Trigger:** Andrew-direct, verbatim: *"You said in your last log and findings i believe the vendor
changed the shape for the bronze ingestion and that broke the typed silver conversion"* / *"CHeck
and make sure that is the issue first"*.

## SUPERSEDES

`079b1b770e` -- "MDPF_COTREMEDIATION ROOT CAUSE CONFIRMED -- VendorDriftError. Black Diamond ADDED
'Account Supervised' + 'Holding Supervised' to the holdings xlsx". **The mechanism (a header
contract refusing a 21-column file against a 19-column declaration) is CORRECT. The ATTRIBUTION is
FALSE.** Black Diamond did not change anything.

## WHAT ACTUALLY HAPPENED

`17c38a26f2`, author `0.6.2_AE_PartnerETL`, **2026-08-20T17:56:24Z**, subject verbatim:

> to(COT_SUPERVISED.G4, 0.6.2 bronze leg): daily holdings template 226355 amended IN PLACE per CTO
> pin (B) -- {Holding Supervised, Account Supervised} added, QA export PASS 21 cols / 18,051 rows

Body: *"BD persisted qt1 template 226355 ('Assets_Dim', Andrew-built) gains Account Supervised
(id 33, level 7) + Holding Supervised (id 45, level 9), inserted VERBATIM from the
Query/DimensionsFacts qt1 catalog. GET re-read diff: exactly the two additions, nothing lost
(15 -> 17 dims)."*

**An Opal agent amended the Black Diamond export template in place, under a CTO pin, adding exactly
the two columns that the silver guard has been refusing ever since.**

## TIMELINE -- every instant UTC (`aws s3 ls` renders LOCAL UTC-4; converted, not assumed)

| UTC | event | evidence |
|---|---|---|
| 2026-08-20T11:45:54Z | `HOLDINGS_DAILY_2026-08-19.xlsx` lands. **19 columns**, neither supervised field. Converts -> silver `date=2026-08-19`. LAST GOOD. | file opened + row 1 read (openpyxl) |
| **2026-08-20T17:56:24Z** | **`17c38a26f2` -- WE amend template 226355.** 6h after that morning's export. | git |
| 2026-08-21T11:45:54Z | `HOLDINGS_DAILY_2026-08-20.xlsx` lands. **21 columns**, `Account Supervised` idx 8, `Holding Supervised` idx 20. REFUSED. FIRST FAILURE. | file opened + row 1 read |
| 08-24, 08-25 | same refusal. silver frozen at `date=2026-08-19`. | live CloudWatch |

**The first scheduled export after our own amendment is the first failure.** No gap, no second
condition. (The apparent 08-19-vs-08-21 mismatch COO raised is the T-1 lag: the file named for day
D lands next business morning and produces partition `date=D`.)

## GROUNDING -- three layers, no shared instrument (Rule 22 / 22a)

1. **VENDOR ARTIFACT (the thing itself).** Downloaded both xlsx from bronze and read row 1 directly.
   19 vs 21 columns, additions named and positioned. Not a report about the file -- the file.
2. **RUNTIME (applied).** Live `aws logs filter-log-events` on `opal-assets-silver-blackdiamond`:
   `observed=` 21 / `declared=` 19, the two extras exactly.
3. **OUR OWN HISTORY (source).** The amendment commit above, with pre/post template images committed
   as evidence at `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/COT_SUPERVISED/`
   (`g4_226355_pre_amendment.json` / `g4_226355_post_amendment.json`).

## BLAST RADIUS -- bounded STRUCTURALLY, not empirically

`holdings/` exists under `blackdiamond/cottonwood/` and **not** under `blackdiamond/49f/` (which
carries `allocation_390224`, `fees_435407`, `reporting_*`). Only cottonwood has a holdings table in
this converter family, so only cottonwood *can* be affected. 49f + inflection reading 08-24 is
expected, not luck.
*Method note: the first run of this control used `49financial/` and `inflection/` prefixes that do
not exist under `blackdiamond/` and returned clean empties -- the wrong-tree-404 class. Re-ran.*

## THE LANE PREDICTED THE FIRE AND WATCHED ONE LAYER

`d4a86a84e1`, same lane, same day: *"today's 19-col extract pre-dates the amendment by 6h so it is
NOT a failure... the real fire is FRIDAY 11:30Z."* The bronze leg forecast that the next scheduled
export would carry 21 columns, and correctly refused to treat its ad-hoc QA export as acceptance
(ad-hoc-runs law, observed). **Its own QA read -- "PASS 21 cols / 18,051 rows" -- was TRUE AND
CORRECT FOR ITS LEG.** What never happened is the silver contract being told.

>> **THE DEFECT IS A CROSS-LAYER SEQUENCING MISS, NOT A CODE DEFECT AND NOT A VENDOR SURPRISE.**
>> A bronze-shape change shipped with no silver-contract step, in an estate whose Rule 17a spine is
>> "each layer has exactly one job." The guard did its job perfectly; the change did not carry its
>> downstream leg.

## AN INSTRUMENT DEFECT WORTH CARRYING PAST THIS INCIDENT

**The exception class is named `VendorDriftError`. It names an ATTRIBUTION, not a CONDITION.** The
condition it actually detects is `observed header != declared header`, which is agnostic about who
moved. The name hands every reader a causal story for free -- and here the story was wrong.

The seat that misattributed it was **the same seat whose pin authorised the amendment**: my own
predecessor read its own change's consequence and blamed Black Diamond. It also flattered a
hypothesis Andrew had already voiced (*"on august 20 or so I'd guess"*) -- and per this seat's own
banked lesson, a claim that flatters an existing hypothesis gets the least scrutiny.

**Rename candidate: `HeaderContractMismatch`.** Routed to CVO as a surprise-channel OBSERVATION
(class OBSERVATION, standing INERT -- the live hazard is already owned under D8).

## REMEDY -- mechanically unchanged, premise changed

1. Declare both columns as **Rule 17 passthrough** (never slim/filter/fillna/drop). Contract has
   **TWO HOMES** and both must move or they silently diverge (Rule 22a):
   `data/assets/scripts/silver/mirror_schemas.py:460` and
   `infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/mirror_schemas.py:460`.
2. Re-run **three** partitions: `2026-08-20`, `2026-08-21`, `2026-08-24`. Not five -- 08-22/08-23
   are the weekend and the vendor emitted nothing (visible in the feed: the 08-21 file lands 08-24).
3. **The re-run trap still binds:** a re-run that produces correct-looking data does NOT establish
   the cause, and the L1 null-filled `dates` array remains a separate unexplained discriminator.
   If the re-run lands clean with the null-fill unexplained, AC1/AC5 are UNMET by the PRD's own bar.

## WHAT THIS DOES NOT CHANGE

D8 stands and the outage is real. Only the causal attribution moves. No register edit is implied --
flagged to MSTR so the D8 stance is not written on "vendor drift".
