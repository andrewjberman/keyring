# 2.0.0_SA_COO~Z — ADDENDUM 2: gold's first run, a deployed/tree gap, and Andrew's page smoke (2245–2345Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE, SCRIBE

Continues `laneZ_addendum_round1_executed_and_closed_2110-2245Z.md` @0afd50d3df.
**2 further commits** (21 this session, all mine). ~8 MCP sends, ~30 messages read, 9 READ-acked.
**Zero crons, whole session. `/drive` never armed.**

---

## 1. ⛔ CURRENT STATE — FOR A FRESH SEAT

### The chain finally reaches the page

| tier | state |
|---|---|
| **BRONZE** | ✅ EXERCISED |
| **SILVER** | ✅ EXERCISED — 187 rows, four funds |
| **GOLD** | ✅ **RAN FOR THE FIRST TIME EVER, 22:56:44Z** — 3 objects in Andrew's C2 home |
| **PLATINUM** | ✅ **REPUBLISHED 23:00:45Z** — new ETag, 4th manifest |
| **END TO END** | ✅ **bronze → silver → gold → platinum, first time** |

⛔ **BUT EVERY ARTIFACT ABOVE IS `run_class: adhoc`.** That is **AC3**, not AC7. **The scheduled
`cron(0 13)` has never fired.** Downstream these bytes are indistinguishable from a scheduled run's
— which is exactly why the law says an ad-hoc run's artifacts are never production evidence.

### `ETFS_POSITIONING.TO-5` — deploy CLOSED

`20260824T2251Z_...` — **all 8 legs, closed 23:06:44Z, inside the 4.0h window.** **I verified the
closure at the ledger file rather than accepting AE~Z's report.** **NEVER#6 discharged.**

---

## 2. ⭐ THE FINDING OF THE STRETCH — DEPLOYED BYTES 208 LINES BEHIND THE TREE

Measured on `etfs-netassets-daily`, negative control run:

```
DEPLOYED 1,127 lines   TREE 1,335 lines
  vendor_trueshares_Date 0 · as_of_basis 0 · _v_ts_Date 0 · zzz_no_such_token_9999 0 (NEG CONTROL)
  TS_HOLDINGS_ENABLED 6 · fetch_trueshares_holdings 3     <- these ARE deployed
```

**TO-4's conventions layer is COMMITTED AND NOT RUNNING**, so the 22:00Z partition has 17 columns.

>> **THE CONSEQUENCE IS WHAT MATTERS: the remedy the whole fabric was about to build — point
>> `data_as_of` at `vendor_trueshares_Date` — READS A FIELD THAT DOES NOT EXIST IN PRODUCTION. It
>> would have passed commit-gate, cited Andrew's sovereign ruling correctly, and been a NO-OP.**
**A fix that looks right, reviews right, and changes nothing is worse than one that fails.**
This is CLAUDE.md **Rule 22a's CODE layer**, live, on the critical path — and `as_of_basis`, the
field built to make the defect *legible*, is missing by the same gap.

**Second-order, and nobody had said it:** the as-of defect is in the **silver** producer (fires
22:00Z, **already fired**); the 13:00Z fire is **gold**, reading a partition already on disk. **So
the fix is three acts — code, redeploy, partition rewrite — and the third is a production backfill I
NAMED AND GATED ON CTO~Z rather than took.**

---

## 3. NEVER#1, AND WHY I DID NOT GET TO CLAIM IT

`gold/.../date=2026-08-21/` on 2026-08-24 was reported as *"three calendar days behind"*. **I
resolved the calendar before reasoning:** 08-24 is a **Monday**, 08-21 the **Friday**, 08-22/23
non-trading. `expected_last_trading_day` = 08-24, `trading_days_behind` = **1**.
**One trading day, not three — and for a T-1 pipeline that is the healthy steady state.**

⭐ **CTO~Z, DS~Z and MSTR~Z reached this independently and MSTR~Z retracted in full before my read
finished.** My contribution is corroboration, not the catch: I re-derived the producer's
self-reported `trading_days_behind: 1` **from the canonical `lib/trading_calendar.py`, at a seat that
did not write the producer** — different instrument, same answer. **Recording it as corroboration
because a fourth seat agreeing is worth exactly one rung, not four.**

---

## 4. ANDREW'S PAGE SMOKE — six items, and only one was a build

| # | item | disposition |
|---|---|---|
| 1 | no DIVZ/IDVZ data | **needs nothing** — T-1 = Friday; they populate at 13:00Z |
| 2 | no PFDE/PFOE performance | ⛔ **NOT a build.** DS~Z measured: `history_topup` IS feeding, 2-day series, `0/114` is the producer's own documented correct output; the 1D "gap" of 5 is **4 cash lines + the unpriced TPG row = 109 of 109 real securities.** → **CARD at Andrew: wait, or a Bloomberg BACKFILL (vendor egress, his word)** |
| 3 | patchy yield | resolved by read — the nulls are **non-payers** |
| 4 | `# of ETFs` → `# of Securities` | **TO-6 AC1**, one render site, measured |
| 5 | GICS + canonical order | ⛔ **CARD at Andrew** — see below |
| 6 | light→dark ramp on Sub-Asset | **TO-6 AC4** |

**Item 5 is a genuine fork in his own sentence:** *"canonical Sector/GICS ordering"* →
`SECTOR_INDICES` (ascending, name-keyed, nearly free); *"how PM handles it (Yang was very adamant)"*
→ `ECONOMY_ORDER` (25, 45, 40, 10 — **deliberately not ascending**, needs an unverified name→code
bridge). **Only one can be built and the cheap one may be the wrong one.**

**TOs cut:** `ETFS_INGEST.TO-7` @a5e19f8a86 (provider as-of) · `ETFS_POSITIONING.TO-6` @0ad590849c
(page items 4/5/6). **Both landed LOCAL; both ride integration.**

---

## 5. ⛔ MY OWN DEFECTS THIS STRETCH — FIVE, AND FOUR WERE CAUGHT BY A GUARD, NOT BY CARE

| # | defect | what caught it |
|---|---|---|
| 10 | **A pandas ternary hit a missing column and printed `date` under the label `vendor_ts_Date`.** I was ~90s from broadcasting that the remedy's input was *corrupt* — the truth was *absent*, a different owner and a different fix | **an IMPOSSIBLE value** — a TrueShares-only column populated for filepoint. Not plausibility |
| 11 | **Declared in-spec work OUT of spec.** TO-7 shipped a banner saying "outside the certified decomp" when **`INGEST-T2-4` covers it exactly — a cell I wrote three hours earlier** | the proof-of-spec gate demanding a `cell_refs` value |
| 12 | **Invented a cell id.** `cell_refs="POS-SERVE-1"` on six criteria; **it exists nowhere in the estate** | grepping it and finding only my own new file |
| 13 | **Two wrong assert constants** (`13` vs 24, `13` vs 25) | **the asserts themselves — both fired before the write** |
| 14 | TO-7 shipped with **no `<proof_of_spec>`** | the commit gate |

⛔ **#11 AND #12 ARE ONE PATTERN AND IT IS NEW: AUTHORSHIP SUBSTITUTES FOR RETRIEVAL.** With someone
else's artifact I open it; with my own I consult a memory of what I *meant* it to cover. **The
out-of-spec banner would have laundered a covered cell into an exception, inside the document whose
job is to say what is covered. The fabricated `cell_refs` PASSES THE GATE** — the checker validates
presence and consistency, not existence.
⭐ **And grounding the ref paid for itself: looking up the real cell surfaced `ETFS-f-3` —
Models-mode BYTE-IDENTICAL — a live constraint on a shared panel I would not have written down.
The check found a fact, not just a compliance.**
Banked: `authorship-makes-me-skip-reading-my-own-artifact`,
`a-fallback-branch-answers-under-the-original-label`.

⭐ **#13 is the good news in the list.** Twice I typed an expected count and twice the assertion
fired **before** the write. **The lesson was already banked and I still typed the number — the guard
held where the memory did not.** Third time I derived it (`PRE` + delta) and it passed.

---

## 6. Compiler tools

| tool | result |
|---|---|
| `lib/trading_calendar.py` | the canonical frontier, run directly — `_USE_PMC=False`, so the **fallback holiday list** answered (41 entries, horizon **2027-12-24**, 487d out; next holiday **Labor Day 2026-09-07**, present). ⚠ **Tonight's answer rests on WEEKDAY arithmetic alone — the holiday path is UNEXERCISED**, so the layer got credit for work pure weekday logic would have done identically |
| `boto3` direct | bronze CSV `Date` census, silver partition per-source value counts, deployed-package token census. **Every raw `aws` call carried `# rail-checked`** |
| `safe-commit.sh` | 2 invocations, **2 rc=0** after the gate correctly refused TO-7 once |
| `proof-of-spec-check` | ⚠ **`firm` enum still has no ETFS value** — FABRIC entered and DECLARED, third TO running. Routed to CTO~Z as gate owner; **I do not edit a gate** |
| native `Grep`/`Read` | used where the Bash rail gate over-matched on the `infra/` path prefix for a **`.py`** file — the sanctioned nudge path, **no override spent** |

---

## 7. Blockers and next

**None at this seat.** Open and owned elsewhere:
1. **[Andrew]** two cards — the sector ORDER (item 5); the Bloomberg BACKFILL spend (item 2).
2. **[CTO~Z]** `INGEST-TO7-AC3` — authorize (or refuse) the 2026-08-24 silver partition rewrite.
   **Refusal is fine and records as BLOCKED, not deleted** — a criterion dropped to make a contract
   pass is the coverage frame lying about its own domain.
3. **[DS~Z / AE~Z]** TO-7: fix, **redeploy the 208-line-behind silver Lambda**, then the partition.
4. **[DE~Z]** TO-6 AC1 now; AC2–AC4 on Andrew's answer.
5. **[AE~Z]** **AC7 — the 13:00Z fire, at its own invocation record.** Nothing tonight closes it.

⚠ **A fresh seat must not read "end to end ran" as "the pipeline works."** It ran **once, ad-hoc,
on Friday's data, with a known-stale silver producer underneath it.** Tomorrow's 13:00Z fire is the
first honest test, and **it will publish a provenance stamp the provider never asserted unless all
three acts of TO-7 land first.**
