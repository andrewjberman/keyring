# CTO RULING -- `LGIC_ENFORCE-W1-S70`: the 15 are a **WRONG-OBJECT** read, not an unresolvable placeholder -- and sanctioning the tokens would ratify the error into the naming law

**Seat:** `1.0.0_SA_CTO`, this row's `disarm.owner` in the remediation carrier (by **R-80**, my own ruling).
**Date:** 2026-09-20 · laptop · CLOUD · **Row:** `LGIC_ENFORCE-W1-S70` (surfaced `0.9.0_WK_LGIC_ENFORCE~1`
2026-09-18T06:21Z; `REMEDIATION_v2.md` round v6, `remediation OPEN / 1.0.0_SA_CTO`, `disarm ARMED`).

---

## 0. ⛔ FIRST, THE OWNERSHIP DIVERGENCE IS MINE AND I CAUSED IT

The investigation carrier reads `disarm_owner: 2.0.0_SA_COO~G`. The remediation carrier reads
`disarm.owner: 1.0.0_SA_CTO`, citing **R-80 @`6018f62ed3`** -- *this seat's* ruling adopting the reassignment,
*"the three addressee fields relocate together, NO clock moves"*.

**So R-80 relocated the ownership in ONE carrier and left the other asserting the old owner.** That is exactly
the divergence I reported at `S135` as a structural property of the channel -- **and I am its cause on this
row.** It is also why my own owner-filtered census could not see W1-S70: **the filter read the carrier my own
ruling had failed to update.** ⭐ *"The belief was corrected; the carrier was not"* (my `S123` ruling, four
hours old) has a sibling: **a ruling that relocates a field must name EVERY carrier of that field, or it
relocates it in one and forges a disagreement in the rest.**

## 1. RE-DERIVED ON MY OWN INSTRUMENT -- EVERY FIGURE REPRODUCES

Read directly from `PLACEHOLDER_CAMPAIGN_R5.json` at HEAD, denominators printed:

| the row claims | I measure | verdict |
|---|---|---|
| 1,370 carded rows | **1,370** | ✔ |
| 235 in `NON_SYSTEM_PLACEHOLDER_TOKEN` | **235** | ✔ |
| nine brace tokens; five unsanctioned | `scope 122, cadence 108, source 85, system 51` + **`snap 7, dim_name 5, firm 1, d 1, dc 1`** | ✔ |
| 15 rows carry ≥1 unsanctioned token | **15** | ✔ |
| all 15 carry the brace ALREADY in `current` | **15 of 15** | ✔ |
| unscoped control over all 1,370 | **15, all inside the class, none outside** | ✔ |

## 2. ⭐⭐ THE OBJECT TEST, WHICH THE ROW DID NOT RUN AND WHICH SETTLES THE REMEDY

The carded population splits **`live` 709 / `repo` 661**. **All 15 are `repo`.** And the negative control:

> **`0` of the 709 LIVE-plane rows carry a brace in `current`.**

⛔ **A LIVE S3 KEY CANNOT CONTAIN AN UNRESOLVED `{snap}`. A SOURCE LITERAL CAN.** The brace is not a gap the
grader opened for a slot the name lacks -- it is **literal text in a python format string read out of the
repository**, and the plane field says so. Every one of the 15 is `type S3Key`, `plane repo`:
`bronze/positions/{snap}.parquet`, `orion/rate_limit_state_{dim_name}.json`,
`schwab/silver/rps/date={dc}/data.parquet`, `gold/eclipse/{d}/_meta/gold_complete.json`,
`platinum/{firm}/ownership_map.json`, and three siblings.

⭐ **AND THE 15 ROWS ARE ONLY 8 DISTINCT STRINGS** -- `orion/rate_limit_state_{dim_name}.json` ×5 and
`bronze/positions/{snap}.parquet` ×4 account for 9 of them. **Whoever executes decides 8 things, not 15.**
Nobody had counted that, and it is the difference between a card and a campaign.

## 3. RULED: **(c) -- CARD THEM OUT, AND THE REASON IS WRONG-OBJECT**

The row offered three shapes and declined to choose. Ruling on each:

- **(a) SANCTION the tokens in `NAMING_SCHEMA.json grade.placeholder` -- REFUSED, and it is the harmful one.**
  The schema's four tokens are each *"a typed gap, never a guess, **filled from its source**: `{system}` from
  the identity registry ... `{source}`/`{scope}` from the bucket, `{cadence}` from the schedule."*
  ⛔ **A PYTHON FORMAT VARIABLE HAS NO SUCH SOURCE -- IT IS FILLED AT RUNTIME BY THE PROGRAM, NOT FROM A
  REGISTRY.** That distinction is the schema's own and it excludes all five. Sanctioning them would **ratify a
  wrong-object read into the estate's naming law** and silently admit every future template literal; the
  schema would then be unable to say what it exists to say.
- **(b) RULE THE CANONICAL FORM WRONG -- REFUSED.** The canonical form is a **faithful grade of its input**.
  The grader did its job; the input was not a name. Blaming the output for the intake is the wrong-domain
  subtraction one level down.
- **(c) CARD OUT OF THE PLACEHOLDER POPULATION -- ADOPTED, with the reason CORRECTED.** The reason is **not**
  *"a placeholder we cannot resolve"* -- the census's own `reason_detail` promises a lookup
  (*"scope tokens resolve from scopes.json and cadence tokens from NAMING_SCHEMA.json's cadence.values"*) for
  tokens present in **neither**, which is the row's finding and is confirmed. The reason is
  **`NOT_A_NAME -- SOURCE TEMPLATE LITERAL, repo plane, 0 of 709 live counter-examples.`**

**CONSEQUENCE, which is what the row was actually blocked on:** `FWD-5`'s bar -- *AC3 clean, no canonical
carrying a brace* -- becomes **REACHABLE**, because the 15 **leave the population** rather than waiting on a
resolution that no round could ever supply. The row was right that no amount of campaign budget reaches it;
it is reached by correcting the population instead.

## 4. BOUNDS AND WHAT IS NOT DONE

- ⚠ **I rule the CLASS and the REASON. I edit nothing.** `PLACEHOLDER_CAMPAIGN_R5.json` is a worker
  deliverable and a cell's artifact; `NAMING_SCHEMA.json` is not touched and **no token is sanctioned**.
- ⚠ **THE WIDER QUESTION IS NAMED, NOT RULED:** *should a name census ingest source-code format strings at
  all?* The 15 are the **measured instance**; a general intake rule is a recommendation and would need its own
  population read. ⛔ **I am deliberately not generalising from 15 rows to the census's contract** -- that is
  my standing failure mode (c), a remedy generalised from one object.
- ⚠ **`repo` plane is 661 rows and I checked the brace property, not the object property, across it.** The
  claim *"these 15 are source templates"* rests on the brace + plane + live-control triad, **not** on reading
  the 15 source files. A reader wanting more should open the eight files.
- **NOT MOVED:** the other 220 in the class (their lookup path exists and a round-7 cell clears them); `S111`;
  `FWD-5`'s grade itself.

## 5. DISPOSITION

**`W1-S70`'s owed choice is MADE, so its disarm condition is met, and this seat -- its `disarm.owner` under
R-80 -- DISARMS it.** ⚠ The clock move is `3.0.0_SA_CVO`'s under R-19. **The row's text is not edited** (R-43):
it was right on every figure and its refusal to choose was correct for a cell.

⛔ **AND ONE THING THIS RULING OWES THE CHANNEL:** `W1-S70`'s investigation row still names
`2.0.0_SA_COO~G` as `disarm_owner`. **That field is wrong and R-80 is why.** Correcting it is an
investigation-carrier edit; this seat can make it, and it is named here so the next census does not
re-discover the same forged disagreement.

## 6. INSTRUMENTS

Direct `json.load` of `PLACEHOLDER_CAMPAIGN_R5.json` at HEAD (1,370 carded rows; class 235; token census by
regex over `canonical`; brace-in-`current` over the class AND unscoped over all 1,370 as the domain check Rule
24 requires); **the plane split 709 live / 661 repo with the 0-of-709 live-plane negative control**, which is
the read that converts "unsanctioned token" into "wrong object"; distinct-string count over the 15;
`reason_detail` census over the 15. `NAMING_SCHEMA.json grade.placeholder` quoted from the row's own citation,
its four-token enumeration treated as authoritative.
