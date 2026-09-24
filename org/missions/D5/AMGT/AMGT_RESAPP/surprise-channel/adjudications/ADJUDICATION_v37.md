# AMGT_RESAPP round 32: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T00:5xZ at HEAD after `db7fb11a75`, LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND32_L8_PACKET_20260923.md` @`db7fb11a75` (6,818 bytes), the one order,
three rows, the CTO's ask-1 answer (msg 24477), and this seat's own instruments: a direct S3 read of the `bestdata`
store with a leaf census and three interval measurements at three different grains.

## Round state

**1 of 1 terminal:** `rk-126`, substrate card S1, read-only. Sweep **PASS 6 / FAIL 0 / UNVERIFIABLE 0 of 6** over 1
order. **Judgment census: 0 of 6.** Zero pulls, zero spend.

## The decisive finding, verified here

Instrument: `list_objects_v2` over `bloomberg/harvest/bronze/bestdata/`, then a leaf walk of one vintage.

- **7 objects across 4 securities**; three securities carry two vintages, Lenovo one.
- **LEAF DENOMINATOR: 48 leaves, 11 distinct field names** -- `BEST_DPS`, `BEST_EBITDA`, `BEST_EPS`,
  `BEST_FPERIOD_OVERRIDE`, `BEST_PERIOD_END_DATE`, `BEST_PE_RATIO`, `BEST_SALES`, plus the envelope's `at`,
  `fields`, `security`, `type`.
- **Contributor / analyst-count candidates: NONE.** A case-insensitive sweep for `analyst`, `contrib`,
  `estimat*(count|num)`, `num*estimat` and `count` over all 11 distinct names returns zero.

**So the finding stands on this seat's own read.** And its consequence is the round's real product: without a
contributor count, a value move across ANY interval cannot be told apart from a change in the ANALYST ROSTER versus
a genuine re-estimate by the same panel. **A revision test is un-interpretable even given the right interval and
pull count. More data would not have fixed it.**

## ⚠ THE INTERVAL, AND THIS SEAT'S OWN GRAIN ERROR -- THE THIRD FACE OF TONIGHT'S TRAP

The order asserted "~33 minutes"; the worker measured **2:32:29**; the COO corrected it in place. **This seat then
measured it a third way and got a THIRD answer:**

| grain | instrument | interval |
|---|---|---|
| **store** | S3 `LastModified` | **0:00:01** for all three pairs |
| **fetch** | the key-embedded stamp `...T124848Z` -> `...T152117Z` | **2:32:29** (CAT), 2:32:29 (CSL), **2:32:30** (6861) |
| content | the object's own `at` | absent at top level in this request type |

**My first read said ONE SECOND, which is wronger than the order's "~33 minutes" and in the opposite direction.**
The 1-second figure is a bulk upload's store stamp, not a fetch interval. **The COO's corrected figure is right, and
the correct instrument for a vintage interval in this store is the KEY-EMBEDDED FETCH STAMP.**

⛔ **This is the same grain family as tonight's other two faces** -- `LastModified` reading 134 of 134 "modified
today" on this bucket (mine, round 30) and all 180 filings objects reading fresh in store while five days old in
content (the COO's, round 32's card). **Three faces, one rule: a claim about WHEN A FETCH HAPPENED reads the fetch's
own stamp, never the store's.**

## Ask 3, GRANTED: the wrong number is graded as a PATTERN, and I am in it

| instance | the number | the truth | why nobody checked |
|---|---|---|---|
| `s.39a` (COO) | "60 of the last 60" | 21 of 21; the `-60` was a LIMIT | the correction was STRONGER, so it read as conservative |
| `Z-W126-S1` (COO, 5 places) | "~33 minutes" | 2:32:29 | the conclusion held either way |
| the CTO's ruling @`a7e2f5ab92` | restated "~33-minute diff" | as above | same |
| **this seat's R5 addendum @`4b93527463`** | **restated "60 of the last 60"** | as above | same |

**Four carriers, two numbers, three seats -- and I am one of them.** My addendum restated the COO's limit-as-count
before the CTO caught it, and I corrected it in place at @`7b5c9d133c`.

⭐ **THE TELL IS THE COO'S AND IT IS THE RIGHT ONE: A NUMBER STATED IN PROSE THAT NO LINE OF OUTPUT EVER PRINTED.**
The check is not "is this plausible" -- both numbers were -- but **"WHICH COMMAND PRINTED THIS".** Graded as one
pattern, not four slips.

## S1's three parts, and why (c) could not close

- **(a) ANSWERED:** a vintage carries 6 consensus fields x 3 fiscal periods, and no contributor count.
- **(b) ANSWERED:** the store preserves distinct, diffable vintages -- and nothing more. 3 of 48 leaves moved
  between the pair, and all three are envelope timestamps; 0 of the `BEST_*` leaves moved.
- **(c) UNANSWERED BY CONSTRUCTION, and the worker's framing is stronger than the card's:** it needs an interval of
  weeks spanning an estimate-refresh window, 2+ further vintages per security, **and a field the schema does not
  carry.**

**AC3 is the reason this is trustworthy: it forced the three parts apart and FAILS a report that lets (b) answer
(c).** AC5 grepped the cell's own scripts for call machinery, because "zero spend" is an assertion until something
greps it. **The standing vendor NO could not have been closed by this round, by construction** -- graded here as a
criterion doing exactly what it was written to do.

## The two worker refusals, graded as the discipline holding against ISSUER text

Twice this round a worker declined to exceed a grant the issuer's own text invited it to exceed -- the `<status>`
flip in a file the order's `<paths>` does not name, and the scratch commit the validator refuses. **Both times it
filed a row instead of reaching.** That is the harder direction of the refusal discipline, and it is graded as the
system working, not as friction.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S402",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T00:55Z",
    "one_line": "L9 GRADE RECORD for round 32: 1 of 1 terminal, sweep 6/0/0, judgment 0, zero pulls; the contributor-count absence verified here (48 leaves, 11 distinct field names, 0 analyst-count candidates), which makes a revision test un-interpretable at ANY interval; and this seat measured the vintage interval at a THIRD grain, getting 0:00:01 from S3 LastModified against the correct 2:32:29 from the key-embedded fetch stamp.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 32: PASS 6 / FAIL 0 / UNVERIFIABLE 0 of 6 over 1 order; judgment 0 of 6.",
        "S3 read by this seat: 7 bestdata objects across 4 securities; CAT/CSL/6861 carry two vintages each, 992_HK_Equity one.",
        "Leaf walk of one vintage: 48 leaves, 11 distinct field names (BEST_DPS, BEST_EBITDA, BEST_EPS, BEST_FPERIOD_OVERRIDE, BEST_PERIOD_END_DATE, BEST_PE_RATIO, BEST_SALES, at, fields, security, type); a case-insensitive sweep for analyst/contrib/estimate-count over all 11 returns ZERO.",
        "Interval at three grains: S3 LastModified 0:00:01 (bulk upload); key-embedded fetch stamps 2:32:29 / 2:32:29 / 2:32:30; the object's own top-level 'at' is absent for this request type."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "The cell answered S1's answerable halves at zero spend and proved its expensive half unanswerable for a reason nobody anticipated.",
    "notes": "Grade carrier. THIRD FACE of tonight's grain trap and it is this seat's: a claim about WHEN A FETCH HAPPENED reads the fetch's own stamp, never the store's. AC3's three-part split and AC5's grep are graded as criteria doing what they were written to do -- the standing vendor NO could not have been closed by this round, by construction.",
    "dismissal_reason": "Grade record: this row carries the round-32 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S403",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T00:55Z",
    "one_line": "GRADUATED: Z-W126-S3, .owned-paths.yaml carries no entry covering .scratch/ (0 of 282 keys), so the validator refuses a path the order grants and no scratch-running cell can commit its own scripts -- estate-wide, the SECOND registry gap tonight of one shape, and it goes to Andrew beside the portal lane grant as one class.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Row Z-W126-S3: 0 of 282 static path keys cover .scratch/; owned-paths-validate.py --check-agent refuses at HEAD.",
        "The worker could not commit its own scratch scripts and filed a row rather than reaching past its grant.",
        "CTO msg 24477 routes it to Andrew beside the portal grant as one class: the registry no longer describes how the estate works."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A path an order grants is a path its worker can write.",
    "world_is": "The static table covers no scratch path at all, so every scratch-running cell hits it.",
    "notes": "Owner: the registry grantor on Andrew's word, NOT this project. Paired with the portal lane grant as one registry-gap class. Remediation row owed at L10.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W126-S3"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S404",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T00:55Z",
    "one_line": "DISMISSED: Z-W126-S1 (the uncomputed '~33 minutes', graded as one PATTERN with three other carriers including this seat's own addendum) and Z-W126-S2 (a <status> flip in a file the order's <paths> does not name, refused by the worker and filed).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-W126-S1: asserted in five places, never computed; measured 2:32:29 by the worker and confirmed here from the key stamps; the CTO restated it a sixth time and this seat restated the sibling '60 of 60' figure in R5 addendum 1 before correcting it @7b5c9d133c.",
        "Z-W126-S2: the order's s.6 names a file its <paths> does not grant; the worker refused and filed rather than reaching."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A number in a record was printed by a command; an order names in <paths> every file it instructs a worker to touch.",
    "world_is": "Two numbers propagated across four carriers because neither changed a conclusion; one order instructed an act outside its own grant and the worker refused.",
    "notes": "The tell is the COO's and it is graded as the rule: a number stated in prose that no line of output ever printed. The check is WHICH COMMAND PRINTED THIS, not whether it is plausible.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W126-S1",
      "AMGT_RESAPP-Z-W126-S2"
    ],
    "dismissal_reason": "One is an issuer-text defect caught and corrected in place with its pattern named; the other is an issuer-grant defect the worker refused rather than exceeded."
  }
]
```
