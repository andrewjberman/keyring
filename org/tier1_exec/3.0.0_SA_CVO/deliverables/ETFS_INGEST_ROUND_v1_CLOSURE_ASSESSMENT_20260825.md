# ETFS_INGEST surprise channel — round v1 closure assessment

**Certifier of record:** `3.0.0_SA_CVO~Z` · **Assessed:** 2026-08-25T06:0xZ
**Artifact:** `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` @`b6cebbcc85`
**Protocol:** CLAUDE.md Rule 27 · `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md`

---

## VERDICT: ROUND v1 REMAINS OPEN, AND IT IS NOT CLOSE

The protocol closes a round **only on a zero-graduation round**. This round graduated **27 of 48
items**. That is not a near-miss; it is a round still in its productive phase.

**I am not closing it, and I am not proposing a date.** A closure judgment predicting when other
seats' items will disarm would be exactly the inference this channel exists to prevent.

---

## STATE, MEASURED

| axis | count |
|---|---|
| items | **48** (ids contiguous 1..48, 0 dups, 0 CRLF, all schema-valid) |
| BLOCKING + ARMED | **12** ← gates closure |
| OBSERVATION + ARMED | **16** |
| BLOCKING + INERT | 8 |
| OBSERVATION + INERT | 12 |
| GRADUATED | 27 · UNDER_INVESTIGATION 20 · DISMISSED_WITH_REASON 1 |
| **ARMED without a named owner** | **0** |

---

## ⛔ THE STRUCTURAL FACT THAT GATES CLOSURE IS NOT THE COUNT — IT IS THE CONCENTRATION

```
1.0.0_SA_CTO~Z              14 of 28 ARMED items   <-- FIFTY PERCENT, ONE SEAT
0.4.0_DS_ClientPlatform~Z    5
0.7.0_AE_CloudOps~Z          3
2.0.0_SA_COO~Z               3
0.0.0_AB_MSTR~Z              2
0.4.0_DE_ClientPlatform~Z    1
```

**Half the armed surface sits with one seat, and that seat carried the heaviest execution load of the
night.** Closure throughput is bounded by that seat's availability, not by the total item count —
so a plan that reasons from "28 items across 6 seats" will size the remaining work wrong by roughly
2×. **Naming it as a routing input for whoever schedules v2; not proposing a reassignment, which is
an owner's call.**

---

## ⭐ THE SYNTHESIS: FIVE ITEMS, ONE MECHANISM

`Z-S43` · `Z-S44` · `Z-S45` · `Z-S46` · `Z-S48` are **not five defects. They are one mechanism in five
places:**

> **A DISPLAY COLLAPSING TWO DIFFERENT THINGS ONTO ONE APPEARANCE.**

| item | the two things that render identically |
|---|---|
| Z-S43 | weight *correctly excluded* vs weight *silently dropped* — the sector axis has no residue bucket |
| Z-S44 | a security with *no history* vs one whose *history leg failed* — RBGLD |
| Z-S45 | a *null datum* vs a *dead resolver* — the five blank columns |
| Z-S46 | a window *not yet grown* vs one *floored by `HISTORY_LOOKBACK_DAYS`* |
| Z-S48 | *correctly* uppercase (BP, GSK) vs *wrongly* uppercase (VZ, MRVL) |

**In every case the detector a reader reaches for is itself unable to tell the defect from the correct
case** — count the all-caps, count the nulls, read the blank cell. **That is why each of these
survived review: the instrument that would find them shares the blindness.**

⛔ **The operational consequence, and it is the reusable one: a remedy for any of these must be
verified by a test that CANNOT BE PASSED BY CHANGING SOMETHING.** Z-S48's oracle is the worked
example — *exactly four names change, 162 stay byte-identical* — and it is the shape that killed four
successive remedies which each presented as success.

---

## WHAT I VERIFIED THIS ROUND, AND ON WHICH LAYER

| claim | layer | result |
|---|---|---|
| producer returns are correct | **oracle published BEFORE the run** | **12/12 exact**, twice (04:45 and 04:53 artifacts) |
| ask 1 + ask 2 delivered | DATA → REF → DEPLOY → **BYTES** | all four measured; spread present in `index-CJlD8UOW.js` |
| the promote ships the fix | pre-cut assertion on the ref | 7/7 `<NONE>` → 7/7 `origin/DEV`, control fired both times |
| calendar explains the gaps | census + **positive control** | **class excluded** — Thanksgiving 0/168 vs these 164–167/167 |
| range queries drop rows | — | **falsified by CTO~Z**; the *probe* fabricated, the range was right |

⚠ **NOT verified and named so nobody inherits it: nobody has RENDERED the page.** The shipped
JavaScript contains the spread; no seat has watched eight columns appear in a browser. That is the
fifth rung and it belongs to `0.4.0_DE_ClientPlatform~Z`.

---

## ⛔ MY OWN ERRORS THIS ROUND

Recorded because a certifier's error rate is part of what its certifications are worth.

| error | caught by | shape |
|---|---|---|
| `history_window_end` called an observation | DS~Z + COO~Z | read the OUTPUT, invented the field's meaning without opening the writer |
| "109 covered" | DS~Z | counted whether a FILE EXISTS; the predicate is whether the WINDOW COVERS |
| "105 at 8/8" quoted as current | self, re-measuring | true for one artifact version, stale against a newer one |
| "confirmed at the render" = delivered | COO~Z | collapsed RENDER into DEPLOYED — a rung I had not put in my own ladder |
| "two resolvers" inference | DE~Z's fix | labelled an inference, and still wrong |
| Z-S47 filed as "range omits rows" | CTO~Z | filed the wrong defect; the real mechanism is worse |

**Four of six were caught by other seats. The pattern under all of them is one thing: a measurement
that was true about a narrower domain than the claim I drew from it** — which is the same sentence as
the five-item synthesis above, pointed inward.

---

## NEXT

1. **The 13:00Z scheduled fire** — the production record, per Andrew's 04:30Z posture where the
   ad-hoc run is the proof and the schedule is the confirmation. Read the invocation record.
2. **Z-S48's oracle** stands ready for whenever the name fix is attempted; CTO~Z has ruled it does not
   ship tonight.
3. **Round v1 closure stays withheld.** It reopens as a question when a round graduates zero items.
