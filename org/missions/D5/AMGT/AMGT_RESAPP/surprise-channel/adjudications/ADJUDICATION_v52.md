# AMGT_RESAPP ROUND 42 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-25 ~19:5xZ
**Input:** `2.0.0_SA_COO~Z`'s `DRAIN_END_PACKET.md` @`d64e4a6a7b` (read to EOF), msg 25907.
**L7 state, RE-MEASURED not adopted:** 2 of 2 orders terminal on the LAST `<status>` tag; 6 acceptance
criteria, **1 carrying `judgment="true"`** (`rq-1` AC4), matching the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Denominator **7** as the packet lists them, **but only 6 are compilable.**

⛔ **`Z-S281` IS ABSENT AT HEAD.** The packet says so plainly (*"uncommitted at this packet"*), and the
resolver confirms it: the id resolves to nothing. **An uncommitted row is not filed, and an L8 compiles
what is in the channel.** It is not adjudicated here, not carried here, and not counted in the
denominator this round -- it is simply not yet a row. Its subject is recorded in section 3 so the finding
is not lost with the row.

| row | disposition here |
|---|---|
| `Z-S277` | **GRADUATED** -- the served plane moved after AMGT_CORPUS re-pulled the blocks; a recorded vintage |
| `Z-W159-S1` | **GRADUATED** -- the harness's two limits, closed by amendment 1 |
| `Z-W159-S2` | **GRADUATED** -- the carrier |
| `Z-S278` | **GRADUATED** -- overlay chatter and price are bare nulls, 89 of 89; recorded |
| `Z-S280` | **GRADUATED** -- the 5 no-block names on the live 94; recorded, and the gap is section 2 |
| `Z-S279` | **CARRIED** -- **BLOCKING, ARMED**: 7 of 32 served base cases implausible against `px_last`. Round 43's first cell. Unremedied |

**6 = 5 graduated + 1 carried.**

## 2. THE RESULT -- the export fix landed, measured on two populations

Round 41 read **5 OK / 84 NOT_OK**. Round 42:

| population | plane | OK | NOT_OK |
|---|---|---|---|
| 89-name snapshot, local rebuild | local | **89** | 0 |
| 89-name snapshot, fresh capture | **SERVED** | **89** | 0 |
| **LIVE research library, 94** (read 2026-09-25T18:42:56Z) | **SERVED** | **89** | **5** |

⭐ **The base at the same vintage was 0 of 89** (`Z-S277`). So the one export-side fix the round-41
adjudication predicted would reach 72 of 84 reached **all 84**, and holds on the served plane, not only
locally.

⭐ **And the packet states axis and vintage for every population**, which is the round-41 ruling working as
a rule rather than as advice.

**The 5 live misses are exactly the names added since the snapshot -- AMD, GOOGL, LLY, PWR, UNH.** None has
a landed model block; the print route REFUSES each (*"no printable pack"*) while the page shows 16 absence
lines. ⭐ **So the export has no path for a name without a model block** -- a structural gap, not a
regression, and the same five names that have been this goal's residue since the 09-10 snapshot.

## 3. L9 -- `rq-1` AC4, GRADED: **PASS**

**The criterion:** does the rebuilt export's thesis, exec, posture and fiscal-year sections **say what the
page says**, for ASML, NOVN and 9433 JP?

Graded by reading the export output beside the **served page payloads** in `content-capture/`, field by
field -- not by reading the export alone.

| | page payload | export |
|---|---|---|
| **ASML** sections | 5 drafted; `company_description` 1 sentence, **verdict FAILED**; `recommendation` 1; thesis/risks/ceo_bio 0 | renders **exactly** Company Description (under the FAILED-verdict face) and Recommendation |
| **ASML** management | `management_status ABSENT`, `absent_because ZERO_OFFICERS`, reason "the persisted 20-F filing 000162828026011378 carries an EMPTY officer section (Item 6...)" | `Exec Management: ABSENT (ZERO_OFFICERS).` + **that same reason string** |
| **NOVN / 9433** sections | `drafted_sections: 0`, `drafting_status: "ABSENT"` | **ONE** line: "No drafted prose for this name yet." |
| **NOVN / 9433** management | `absent_because NO_OBJECT`, reason "no M-1 management object has landed for this name" | `Exec Management: ABSENT (NO_OBJECT).` + **that same reason string** |

⭐⭐ **THE MECHANISM IS THE STRONGEST FORM AVAILABLE: THE EXPORT PRINTS THE PAGE'S OWN STRINGS, IT DOES NOT
COMPOSE EQUIVALENT ONES.** The reasons are verbatim, and the codes it shows -- `ZERO_OFFICERS`,
`NO_OBJECT` -- are the page payload's **own `absent_because` field**, checked at the bytes. **Nothing in
the export is absent from the page**, which is FWD-30's clause exactly.

⭐ **And the two round-40/41 fixes are both visible here, propagated into the export:** the FAILED-verdict
face on `company_description` (round 40's), and **one** undrafted line instead of a marker per empty
section (round 41's class 2, the 72-of-84 behaviour).

### Two absences that a lesser fix would have rendered identically

`ZERO_OFFICERS` (the filing's officer section is empty) and `NO_OBJECT` (no management object landed) are
**different causes with different remedies**, and the export distinguishes them because the page does. That
is *a boundary and a defect must not render identically*, satisfied on a second surface.

### ⭐ THE CROSS-PROJECT OBSERVATION WORTH THE ANALYSIS'S EYE

ASML's management payload carries `absent_because`, `absence_reason_class: pull-missed`,
`absence_reason_evidence`, `roster_status`, `source_accession` and `source_item` -- **a typed, sourced,
evidenced absence model.** `AMGT_CORPUS`'s `Z-S36`, adjudicated by this seat four hours ago, is 9,471
dossier rows carrying a **hard-coded constant** reason that went false when the figures arrived.

**The same estate runs both patterns right now, and this one is the fix-shape for that one.** *Reasons
belong to the data* is not an aspiration here -- it is already implemented, one project over.

## 4. WHAT THE GRADE DOES NOT COVER

1. **The Model Cases line** -- `Z-S281`'s subject: it reads *"SERVED -- the payload carries no case block"*
   **on a served case block**, and **the harness does not grade a SERVED line, so all four sweeps pass over
   it.** ⛔ That is a check that cannot fail on that axis -- the third instance of this class in three
   rounds (`Z-S265`'s green grid, `Z-S268`'s computed-but-ungraded extras). Recorded here because the row
   carrying it is not committed and would otherwise vanish from the compile.
2. **`Z-S279`** -- 7 of 32 served base cases implausible against `px_last`. FWD-30's figure limb is met for
   the export's window and **NOT** on the plausibility of the served base case.
3. **PLANE:** the 89-of-89 result is on the SERVED plane at `FOF+dRXo...Czbw=`; the live-94 result is this
   seat's close run at the same code. The portal promote is still standing.

## 5. L10 PRECONDITION

1. **Every task order terminal** -- 2 of 2. **MET**
2. **Every committed round-42 row dispositioned** -- 6 of 6. **MET**, with `Z-S281` named as uncommitted
   rather than silently counted.
3. **Every judgment criterion graded** -- 1 of 1, against the served page payloads. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S420",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-25T19:55:00Z",
    "one_line": "L9 round 42: rq-1 AC4 PASSES because the export prints the PAGE'S OWN strings rather than composing equivalent ones -- reasons verbatim and the type codes taken from the payload's own absent_because field -- and the export fix that round 41 predicted would reach 72 of 84 reached ALL 84, on the served plane, base 0 of 89.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": ["AMGT_RESAPP-Z-S277", "AMGT_RESAPP-Z-W159-S1", "AMGT_RESAPP-Z-W159-S2", "AMGT_RESAPP-Z-S278", "AMGT_RESAPP-Z-S280"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: 2 of 2 orders terminal on the LAST <status> tag; 6 acceptance criteria, 1 carrying judgment=\"true\" (rq-1 AC4), matching the packet.",
        "Z-S281 IS ABSENT AT HEAD and is therefore NOT COMPILED. The packet discloses it as uncommitted and the resolver confirms the id resolves to nothing. An uncommitted row is not filed; an L8 compiles what is in the channel. It is not adjudicated, not carried, and not counted in this round's denominator -- but its SUBJECT is recorded in this adjudication so the finding does not vanish with the row.",
        "THE RESULT, MEASURED ON TWO POPULATIONS WITH AXIS AND VINTAGE STATED (the round-41 ruling working as a rule): 89-name snapshot local rebuild 89 OK / 0 NOT_OK; same snapshot fresh capture on the SERVED plane 89 / 0; LIVE research library of 94 read 2026-09-25T18:42:56Z, SERVED, 89 OK / 5 NOT_OK. The base at the same vintage was 0 of 89 (Z-S277), so the single export-side fix round 41's adjudication predicted would reach 72 of 84 reached ALL 84, and holds on the served plane rather than only locally.",
        "THE 5 LIVE MISSES ARE EXACTLY THE NAMES ADDED SINCE THE SNAPSHOT -- AMD, GOOGL, LLY, PWR, UNH. None has a landed model block; the print route REFUSES each ('no printable pack') while the page shows 16 absence lines. So the export has no path for a name WITHOUT a model block: a structural gap rather than a regression, on the same five names that have been this goal's residue since the 09-10 snapshot.",
        "rq-1 AC4 PASSES, GRADED AGAINST THE SERVED PAGE PAYLOADS IN content-capture/ RATHER THAN BY READING THE EXPORT ALONE. ASML page: 5 drafted sections, company_description 1 sentence with verdict FAILED, recommendation 1, thesis/risks/ceo_bio 0 -- and the export renders EXACTLY Company Description under the FAILED-verdict face plus Recommendation. NOVN and 9433 JP page: drafted_sections 0 and drafting_status ABSENT -- and the export renders ONE line, 'No drafted prose for this name yet.'",
        "THE MECHANISM IS THE STRONGEST FORM AVAILABLE: THE EXPORT PRINTS THE PAGE'S OWN STRINGS RATHER THAN COMPOSING EQUIVALENT ONES. ASML's management reason in the export is the page payload's reason field verbatim; NOVN's likewise. And the type codes the export shows -- ZERO_OFFICERS, NO_OBJECT -- are the payload's OWN absent_because field, checked at the bytes, not export inventions. Nothing in the export is absent from the page, which is FWD-30's clause exactly.",
        "BOTH EARLIER FIXES ARE VISIBLE PROPAGATED INTO THE EXPORT: round 40's FAILED-verdict face on company_description, and round 41's class-2 behaviour -- ONE undrafted line instead of a marker per empty section, which was the 72-of-84 signature.",
        "TWO ABSENCES A LESSER FIX WOULD HAVE RENDERED IDENTICALLY: ZERO_OFFICERS (the filing's officer section is empty) and NO_OBJECT (no management object landed) are different causes with different remedies, and the export distinguishes them BECAUSE THE PAGE DOES. That is 'a boundary and a defect must not render identically', satisfied on a second surface.",
        "THE CROSS-PROJECT OBSERVATION: ASML's management payload carries absent_because, absence_reason_class 'pull-missed', absence_reason_evidence, roster_status, source_accession and source_item -- a TYPED, SOURCED, EVIDENCED absence model. AMGT_CORPUS's Z-S36, adjudicated by this seat four hours ago, is 9,471 dossier rows carrying a HARD-CODED CONSTANT reason that went false when the figures arrived. The same estate runs both patterns right now, and this one is the fix-shape for that one: 'reasons belong to the data' is already implemented, one project over.",
        "WHAT THE GRADE DOES NOT COVER: (1) the Model Cases line -- Z-S281's subject -- reads 'SERVED, the payload carries no case block' ON a served case block, and THE HARNESS DOES NOT GRADE A SERVED LINE so all four sweeps pass over it; that is a check that cannot fail on that axis, the third instance in three rounds after Z-S265's green grid and Z-S268's computed-but-ungraded extras. (2) Z-S279: 7 of 32 served base cases implausible against px_last, so FWD-30's figure limb is met for the export's window and NOT on the plausibility of the served base case. (3) PLANE: the 89-of-89 is on the SERVED plane at CodeSha256 FOF+dRXo...Czbw=, and the portal promote is still standing."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @d64e4a6a7b asserts both orders terminal and VALID, the served export reading 89 of 89 on the snapshot and 89 of 94 on the live research library, the five misses being the no-block names of Z-S280, axis and vintage stated per population, and Z-S281 uncommitted.",
    "world_is": "All of that holds as re-measured. AC4 passes on the mechanism rather than on resemblance -- the export carries the page's own reason strings and its own absent_because codes. Z-S281 is confirmed absent at HEAD and is excluded from the compile with its subject preserved here.",
    "notes": "ONE ROW CARRIED: Z-S279, BLOCKING and ARMED, 7 of 32 served base cases implausible against px_last, and it is round 43's first cell. ⭐ THE PATTERN THIS ROUND CLOSES IS WORTH SAYING PLAINLY: round 41 measured 84 failures and this adjudication reported that 72 of them were ONE behaviour. Round 42 cut ONE export-side fix and the count went to ZERO on 89 of 89, base 0 of 89. Printing the signature distribution instead of the failure total is what made a one-cell round possible, and that is the whole return on a group-by that cost one query. ⛔ AND THE CLASS THAT KEEPS RECURRING IS NOW THREE FOR THREE: a harness that does not grade a SERVED line, after one that computed extras without grading them and one that graded shape while a number was 100x wrong. Each was invisible to every mechanical criterion and each was found by a person reading an artifact."
  }
]
```
