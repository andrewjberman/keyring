# AMGT_RESAPP ROUND 44 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-26 ~16:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round44/DRAIN_END_PACKET.md` @`1acfcabb21` (read to EOF, 5,812 B), msg 26122.
**L7 RE-MEASURED not adopted:** `rs-1`, `rs-2`, `rs-3` all `complete` on their LAST `<status>` tag; 7
acceptance criteria (4+2+1); **exactly 1 carrying `judgment="true"`** (`rs-1` AC4). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **626 items, 67 files read, `unknown: []`, 22 NON-TERMINAL.**

**Round-44 window (on/after 2026-09-26T05): ZERO new rows.** The packet's *"No new rows this round"* is
**independently verified**, not adopted. Nothing minted, nothing to dispose from this round.

### THE AMENDED L10 CLAUSE NAMES BLOCKING AND ARMED ROWS, SO THE CARRIED SET IS DISPOSITIONED HERE

CLAUDE.md now reads *"every BLOCKING or ARMED row is dispositioned"*. Of the 22 carried, **11** are BLOCKING
or ARMED. ⚠ `hazard_standing` is the value written AT SURFACING and **is never a current-state field**, so
none of these is claimed live today; what follows is a disposition, not a re-measurement of hazard.

**GRADUATED -- 2, each on a remedy that landed and was measured:**

| row | why it closes |
|---|---|
| `Z-S265` (BLOCKING/ARMED, mine) | the Peers P/E 100x defect. Remedied in round 39 (`rn-2`): 24 of 24 in band, Deere 0.35 -> 34.70, exactly x100 as predicted, and only the peers path moved. ⚠ I am closing on my own round-39/41 verification, not a fresh re-measure today |
| `Z-S268` (BLOCKING/ARMED) | *"FWD-30 is NOT met on the served plane"*. **Round 44 measures FWD-30 at 95 of 95 on the deployed function with cases 285 of 285 and a positive control on 6 of 6 states.** That is the remedy, measured this round on the served plane the row names |

**CARRIED -- 9, each unremedied, each with its reason:** `Z-S236` (179 no-span sentences of 389; the span
write is still a carried enrichment item) - `Z-S237` (portal submodule commits land on a DETACHED HEAD with
every gate rc=0) - `Z-S238` (28 unattributable 500s; an observability gap nothing has closed) - `Z-S248`
(the `scheduled_daily_pull.cmd` empty-interpreter branch -- **a Bloomberg-pipeline surface, not this
project's**, and named so its owner is not lost) - `Z-S251` (11 places still assert the retired
`--bg-band` identity) - `Z-S255` (portal is an embedded repo with ZERO active hooks; `.gitmodules`
tracked-and-empty) - `Z-W158-S1` + `Z-S276` (the literal-`/` key pair; the disarm owner's read BOUNDS it at
0 greedy routes of 106 but names two arms still unmeasured, so a row with open arms is not closed) -
`AMGT_RESAPP-W130-S1` (the naming-gate REFUSEs the `rl-1` fixtures file because captured API-response data
carries production S3-key-shaped literals its registry has no pattern for).

### ⭐ FINDING 1: 14 OF 626 ROW IDS DO NOT CARRY THE `-Z-` FABRIC MARKER, AND ONE OF THEM IS BLOCKING

Every row in this channel is minted `AMGT_RESAPP-Z-...` **except fourteen**, all worker rows:
`AMGT_RESAPP-W130-S1`, `-W135-S1`, `-W136-S1`, `-W137-S1`, `-W137-S2`, `-W138-S1`, `-W140-S1`, `-W140-S2`,
`-W141-S1`, `-W144-S1`, `-W146-S1`, `-W148-S1`, `-W150-S1`, `-W152-S1`.

⛔ **ANY CENSUS OR SEARCH ANCHORED ON THE `-Z-` CONVENTION SILENTLY MISSES ALL FOURTEEN -- INCLUDING
`W130-S1`, WHICH IS CLASS BLOCKING.** The resolver keys on the literal `id` and is unaffected; a human or a
grep is not. This is the enumerated-pattern-lapses-silently class, inside the channel's own id space.

⚠ **AND I FOUND IT BY WALKING INTO IT.** I searched for `AMGT_RESAPP-Z-W130-S1`, a string I had
RECONSTRUCTED from a display that stripped the project prefix, re-adding `-Z-` by analogy with the rows
beside it. Two scoped searches and one unscoped search all returned zero for a row that exists.
⭐ **THE TELL IS EXACT AND REUSABLE: the unscoped search's ONLY three hits were MY OWN tool-run logs from
the search itself. When a content census finds nothing but its own audit trail, the string was invented by
the searcher, not read from the corpus.** Cost of the correct move: print the ids and filter, rather than
construct one. NON-APPLICATION: a string copied verbatim from a file you have open.

## 2. L9 -- `rs-1` AC4, GRADED ON THE RENDER

**The criterion:** *"does each served value read as a price in a named currency, the same on both
surfaces?"* Three sub-clauses, and they do not grade alike.

### (a) A NAMED CURRENCY -- **PASS**

`rs-1.AC4.served.txt` carries RKT `7386.63633 GBp`, AMD `652.7344928 USD`, GOOGL `537.6961078500001 USD`;
the packet reports 48 of 48 SERVED cases naming a currency, read independently by the lane's own AC2.
⭐ **THIS IS THE DEFECT I RAISED AT ROUND 43 AND IT IS FIXED.** Round 43's render printed a bare
`7386.63633` two inches under a `Price GBp 4923.00` tile, on a name whose whole prior defect class was
currency scale. It now names its unit on both surfaces.

### (b) THE SAME ON BOTH SURFACES -- **PASS for RKT, and I read the render myself**

`round44/real-run-rkt/model.png`: `Base case: SERVED -- 7386.63633 GBp (consensus EPS (FY1) x
trailing-median P/E)`, Price tile `GBp 4923.00`. Export and page agree byte for byte on the value and the
unit. The CONTROL file is real and is the thing I have been pressing for: **6 of 6 states carry a positive
control** (location under `/security-analysis`, not `/login`, `textChars` > 300 against the login page's
141) beside every absence metric.

⚠ **BUT THE FIXTURE PREDATES THE CHANGE, AND THAT BOUNDS WHAT THIS PROVES.** The render's own header reads
**`Sep 25, 2026, 4:37 PM`** -- identical to round 43's -- because `real-run-rkt.fixtures.json` IS round
43's capture (2026-09-25T20:37:22Z) replayed through the new page code. So the page's `GBp` is **computed
by the page** from a fixture that carried no currency, not read from round 44's served payload. The two
surfaces agree via **two independent implementations** (`_case_currency` in Python, `caseCurrency` on the
page -- the packet's own carried item 4), which is real and arguably stronger than one value flowing twice;
**but no single served value was observed traversing both surfaces.** FWD-30's 95-of-95 comparison is what
would catch drift between them, and it is the reason this bound is recorded rather than held against the
round.

### (c) READS AS A PRICE -- **EXERCISED ON 1 OF 3, AND UNGRADED FOR THE OTHER TWO**

- **RKT: GRADEABLE and PLAUSIBLE.** 7386.63633 / 4923.00 = **1.5004** against its own Price tile -- inside
  the [0.33, 3.0] band `AMGT_CORPUS` round 5 established.
- ⛔ **AMD (652.73 USD) and GOOGL (537.70 USD): NOT GRADEABLE from this evidence.** Neither has a render,
  and the packet supplies **no `px_last` for either**; the model blocks are served from S3 and are not in
  the corpus, so no ratio can be formed here. **Their plausibility is UNGRADED, and the ratio band is not a
  substitute for a number I do not have.**

⭐ **AND THE SAMPLE CANNOT EXERCISE ITS OWN CRITERION.** The three names were chosen for CURRENCY variety
(GBp / USD / USD) -- correct for clause (a). But only ONE has a render, so clause (b) is exercised on 1 of
3, and the two that are export-only are precisely the two whose plausibility clause (c) cannot reach.
⚠ **AMD and GOOGL are also two of the five names that first gained blocks in round 43** -- the
sub-population most likely to behave differently, and the same argument round 41 made about this project's
newly-added folders. **A sample chosen to vary one axis was unable to exercise the other two.**

**VERDICT: AC4 PASSES on the clause the round exists to move (a), PASSES on (b) for the one name with a
render under the fixture bound above, and is UNGRADED on (c) for AMD and GOOGL.**

### ⚠ THE SECOND ROUND-43 DEFECT IS NOT FIXED, AND NAMING THE CURRENCY ARGUABLY SHARPENS IT

`537.6961078500001 USD` -- sixteen significant figures of IEEE-754 noise, now carrying a unit. Round 43's
finding was that raw float repr reaches the reader; round 44 fixed the missing unit beside it and left the
repr. **A number that now reads as a price in a named currency reads as a MORE precise price.** The packet
discloses it plainly as *"for the judgment reader, not a claim of a defect"*, which is the right disclosure
-- recorded, not held against the grade.

## 3. ⛔ FINDING 2: THE PACKET'S CARRIED ITEM 3 IS STALE

It reads *"a NEWLY-ADDED round-45 order is refused until the ratified-text half is re-signed at v0.27."*
**Measured now: `prd-signoff.py status AMGT_RESAPP` reads `v0.28 @496b42d725 -> ADMITTED`, ratified-text
`SIGNED ... current`.** I signed v0.27 @`9fb74a6222` and then v0.28 @`fd8432d6dc`, the latter covering
FWD-31 and FWD-23's positive control in one signature. **Round 45 is NOT blocked on this seat**, and an
issuer reading item 3 would hold for a gate that is already open.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 3 of 3 on their last `<status>` tag. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 0 new this round; 11 carried BLOCKING-or-ARMED
   dispositioned above (2 graduated, 9 carried with reasons). **MET**
3. **Every judgment criterion graded** -- 1 of 1, on the render, with clause (c) explicitly UNGRADED for
   two of three names and the reason named. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S422",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-26T16:45:00Z",
    "one_line": "L9 round 44: rs-1 AC4 PASSES on the clause the round exists to move -- the served case value now names its currency on BOTH surfaces, which is the round-43 defect I raised, fixed and verified on the render. But the three-name sample cannot exercise its own criterion: only ONE has a render, and AMD and GOOGL have no px_last anywhere in the evidence, so 'reads as a price' is UNGRADED for two of three. Plus: 14 of 626 row ids in this channel lack the -Z- marker and one is BLOCKING, so any census anchored on that convention misses them; and the packet's carried item 3 holds round 45 on a signature that is already ADMITTED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: rs-1, rs-2, rs-3 all read 'complete' on their LAST <status> tag; 7 acceptance criteria across the three; exactly 1 carries judgment=\"true\" (rs-1 AC4). Matches the packet.",
        "L8: _latest_dispositions reads 626 items over 67 files, unknown [], 22 NON-TERMINAL. Banding by surfaced_at gives ZERO rows in the round-44 window, so the packet's 'No new rows this round' is INDEPENDENTLY VERIFIED rather than adopted.",
        "THE AMENDED L10 CLAUSE names BLOCKING and ARMED rows, so the carried set is dispositioned here: of the 22 carried, 11 are BLOCKING or ARMED. hazard_standing is the value written AT SURFACING and is never a current-state field, so none is claimed live today. GRADUATED 2: Z-S265 (Peers P/E 100x, remedied round 39 rn-2 at 24 of 24 in band, Deere 0.35 -> 34.70 -- closed on my own round-39/41 verification, not a fresh re-measure) and Z-S268 ('FWD-30 is NOT met on the served plane', remedied by THIS round's 95 of 95 with cases 285 of 285 and a positive control on 6 of 6 states). CARRIED 9 with stated reasons: Z-S236, Z-S237, Z-S238, Z-S248 (a Bloomberg-pipeline surface, not this project's), Z-S251, Z-S255, Z-W158-S1 + Z-S276 (two arms still unmeasured), AMGT_RESAPP-W130-S1.",
        "FINDING 1: 14 of 626 row ids in this channel do NOT carry the -Z- fabric marker -- AMGT_RESAPP-W130-S1, -W135-S1, -W136-S1, -W137-S1, -W137-S2, -W138-S1, -W140-S1, -W140-S2, -W141-S1, -W144-S1, -W146-S1, -W148-S1, -W150-S1, -W152-S1, all worker rows. Any census or search anchored on the -Z- convention silently misses all fourteen, and W130-S1 is class BLOCKING. The resolver keys on the literal id and is unaffected; a human or a grep is not.",
        "AND I FOUND IT BY WALKING INTO IT, which is the transferable part. I searched for AMGT_RESAPP-Z-W130-S1 -- a string RECONSTRUCTED from a display that stripped the project prefix, with -Z- re-added by analogy with neighbouring rows. Two scoped searches and one unscoped search returned zero for a row that exists. THE TELL WAS EXACT: the unscoped search's only three hits were MY OWN tool-run logs from that same search. When a content census finds nothing but its own audit trail, the string was invented by the searcher and not read from the corpus. COST of the correct move: print the ids and filter rather than construct one.",
        "L9 (a) A NAMED CURRENCY -- PASS. rs-1.AC4.served.txt carries RKT 7386.63633 GBp, AMD 652.7344928 USD, GOOGL 537.6961078500001 USD; the packet reports 48 of 48 SERVED cases naming a currency, read independently by the lane's AC2. This is the defect raised at round 43 -- a bare 7386.63633 two inches under a 'Price GBp 4923.00' tile, on a name whose prior defect class was currency scale -- and it is fixed.",
        "L9 (b) THE SAME ON BOTH SURFACES -- PASS for RKT, read on the render by this seat rather than taken from the issuer's RENDER READ line: model.png shows 'Base case: SERVED -- 7386.63633 GBp (consensus EPS (FY1) x trailing-median P/E)' beside Price tile 'GBp 4923.00'. The CONTROL file carries a positive control on 6 of 6 states (location under /security-analysis, not /login, textChars > 300 against the login page's 141). BOUND: the render's header reads 'Sep 25, 2026, 4:37 PM', identical to round 43's, because the fixture IS round 43's capture (2026-09-25T20:37:22Z) replayed through new page code -- so the page COMPUTES the currency from a fixture that carried none, rather than reading round 44's served payload. Export and page agree via TWO INDEPENDENT IMPLEMENTATIONS (_case_currency in Python, caseCurrency on the page), which is real evidence and arguably stronger than one value flowing twice, but no single served value was observed traversing both surfaces. FWD-30's 95-of-95 comparison is the catcher for drift between them.",
        "L9 (c) READS AS A PRICE -- EXERCISED ON 1 OF 3. RKT is gradeable and plausible: 7386.63633 / 4923.00 = 1.5004 against its own Price tile, inside the [0.33, 3.0] band AMGT_CORPUS round 5 established. AMD (652.73 USD) and GOOGL (537.70 USD) are NOT GRADEABLE from this evidence: neither has a render and the packet supplies no px_last for either, while the model blocks are served from S3 and are not in the corpus, so no ratio can be formed. Their plausibility is UNGRADED and the band is not a substitute for a number I do not have.",
        "AND THE SAMPLE CANNOT EXERCISE ITS OWN CRITERION: the three names were chosen for CURRENCY variety (GBp/USD/USD), correct for clause (a), but only ONE carries a render, so clause (b) is exercised on 1 of 3 and the two export-only names are exactly the two clause (c) cannot reach. AMD and GOOGL are also two of the five names that first gained blocks in round 43 -- the sub-population most likely to behave differently, the same argument round 41 made about this project's newly-added folders.",
        "THE SECOND ROUND-43 DEFECT IS NOT FIXED: 537.6961078500001 USD is sixteen significant figures of IEEE-754 noise, now carrying a unit. Round 44 fixed the missing unit and left the repr, and a number that reads as a price in a named currency reads as a MORE precise price. The packet discloses it plainly as 'for the judgment reader, not a claim of a defect', which is the right disclosure; recorded, not held against the grade.",
        "FINDING 2: the packet's carried item 3 is STALE. It reads 'a NEWLY-ADDED round-45 order is refused until the ratified-text half is re-signed at v0.27'. Measured now: prd-signoff.py status AMGT_RESAPP reads v0.28 @496b42d725 -> ADMITTED with ratified-text SIGNED current. This seat signed v0.27 @9fb74a6222 and v0.28 @fd8432d6dc, the latter covering FWD-31 and FWD-23's positive control in ONE signature. Round 45 is not blocked on this seat, and an issuer reading item 3 would hold for a gate that is already open."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S265",
      "AMGT_RESAPP-Z-S268"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @1acfcabb21 asserts three orders terminal and VALID, FWD-30 met on the served plane at 95 of 95 with cases 285 of 285 and 48 of 48 SERVED cases naming their currency, the page rendering it with a positive control on 6 of 6 states, and no new rows.",
    "world_is": "All of that is true as re-measured, and three things the packet does not carry: the three-name AC4 sample cannot exercise two of its own three clauses, because only one name has a render and two have no px_last anywhere in the evidence; 14 of this channel's 626 row ids lack the -Z- marker, one of them BLOCKING, so a convention-anchored census misses them; and carried item 3 holds round 45 on a signature that is already ADMITTED.",
    "notes": "FOR THE ROUND-44 ANALYSIS, three items. (1) THE CURRENCY FIX IS REAL AND SHOULD BE CREDITED AS SUCH -- it closes the round-43 finding on the surface a person reads. What it does not yet have is a name whose plausibility anyone can check: give the next AC4 sample at least one name with BOTH a render and a px_last, and clause (c) becomes gradeable instead of ungradeable. (2) The unrounded repr is now the single most visible presentation defect on the page and it is cheaper to fix than anything else carried -- one format call at the render boundary, on a value whose correctness is no longer in question. (3) FINDING 1 is a FABRIC item, not a project one: the -Z- marker is how every seat's eye and every hand-written grep finds a row, and fourteen rows in one channel are invisible to it. The remedy is either minting discipline at the worker face or a lint that refuses an id not matching the project's own pattern -- and the second is the one that does not rot."
  }
]
```
