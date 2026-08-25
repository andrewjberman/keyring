# 2.0.0_SA_COO~Z — ADDENDUM 3: Andrew's page smoke, four TO acts, and a carrier that would have INVERTED (2345–0035Z)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, DIAGNOSE, SCRIBE

Continues `2026-08-24/laneZ_addendum2_...md` @86aa8eefe0. **9 further commits (~35 this session).**
~14 MCP sends, ~40 messages read, 17 READ-acked. **Zero crons, whole session. `/drive` never armed.**

---

## 1. ⛔ STATE — FOR A FRESH SEAT, AND TWO THINGS FIRE AFTER I AM GONE

| clock | what | owner |
|---|---|---|
| **~11:00Z** | **ADR pre-check** — `universe_count` ~166 **NOT `> 109`**; `BBSEY`/`AMX` in `characteristics.parquet` | **whichever seat is ALIVE**, resolved from the register |
| **13:00Z** | **`ETFS-TO5-AC7`** — the first SCHEDULED fire, at its own invocation record **AND** the artifact | whoever is alive |

⛔ **BOTH ARE NOW DOUBLE-CARRIED WITH A NAMED PRIMARY:** `org/XXX.md` MSTR row @`21d800c18d`
(**PRIMARY** — the surface a fresh seat reads at startup) and the `ETFS_POSITIONING.TO-5` face
@`6fe9f4b` (secondary). **If they disagree, XXX.md wins.**

**Andrew's six page items:** 1 needs nothing · **2 dissolved** (correct-by-design; a Bloomberg
backfill is a **spend card**) · **3 dissolved** (nulls are non-payers) · **4/5/6 → TO-6, BUILT
@de32bacb, validated 6/6** · **5 answered by Andrew** (economy code, 10/10 mapped).

---

## 2. ⭐ THE TWO FINDINGS THAT MATTERED

### (a) The silver Lambda was 208 lines behind its tree — and the planned fix had NO INPUT

```
DEPLOYED 1,127 lines / TREE 1,335    vendor_trueshares_Date 0 · as_of_basis 0 · _v_ts_Date 0
                                     NEG CONTROL 0 · TS_HOLDINGS_ENABLED 6 (so the fetch WAS live)
```
>> **The remedy the fabric was about to build — point `data_as_of` at `vendor_trueshares_Date` —
>> read a field that did not exist in production. It would have passed commit-gate, cited Andrew's
>> sovereign ruling correctly, and been a NO-OP.** Rule 22a's CODE layer, live, on the critical path.
**Closed at 23:24Z; the as-of fix itself deployed 00:09:54Z and is VERIFIED in the running bytes.**

### (b) My own carrier for the 11:00Z check would have INVERTED it

MSTR~Z landed the XXX.md carrier at 00:03:59Z. **I landed a second one at 00:14Z without knowing** —
**and mine omitted the ticker-TOKEN warning.** `security` carries `AAPL US Equity`, so a bare-ticker
compare returns a **clean ABSENT for every row** — read at 11:00Z as *"A5 failed"* when nothing
failed.
>> **REDUNDANCY IN RECORDS BUYS SURVIVAL AND COSTS CONSISTENCY.** Two carriers with no precedence
>> rule is the defect; I created it inside eleven minutes **while writing about durability.** Fixed
>> @`6fe9f4b`, XXX.md named primary. **Found by asking "do these AGREE?", not "does one exist?"**

---

## 3. FOUR TO ACTS

| act | commit |
|---|---|
| `ETFS_INGEST.TO-7` (provider as-of, cell `INGEST-T2-4`) | @a5e19f8a86 |
| `ETFS_POSITIONING.TO-6` (page items 4/5/6) + 2 amendments | @0ad590849c · @06a9e6a784 · @dc35e8737d |
| `ETFS_POSITIONING.TO-7` (per-fund as-of) + 2 amendments | @dcfec08903 · @124bdce13d · @284f5f68a4 |
| `ETFS_POSITIONING.TO-5` — **AC7 + its prerequisite finally on the face** | @0a300883ca · @6fe9f4b |

**`ETFS-TO5-AC7` was routed to me at 22:22Z and I carried it in message traffic for 98 minutes.**
CTO~Z came looking for it. Their half was routing-without-verifying; **mine was that it was addressed
to me, on a surface I own.** The same edit killed a **two-`AC7` collision** (`ETFS-TO2-AC7`, an ADVI
fetch) — *"not a missing record, a confidently wrong one"* — and recorded that **`AC6` was never
minted**, so the gap reads as deliberate.

---

## 4. ⛔ MY DEFECTS — SIX, AND THE PATTERN IS SHARPER THAN THE LIST

| # | defect | caught by |
|---|---|---|
| 15 | **A pandas ternary printed `date` under the label `vendor_ts_Date`** — ~90s from broadcasting "the input is corrupt" when it was *absent* | an **IMPOSSIBLE** value (a vendor-only column on the other vendor) |
| 16 | **Declared in-spec work OUT of spec** — `INGEST-T2-4` covered it; I wrote that cell 3h earlier | the proof-of-spec gate |
| 17 | **Invented `POS-SERVE-1`** across six criteria — **it would have PASSED the gate** | grepping the id I was about to write |
| 18 | **Two wrong assert constants** (13 vs 24, 13 vs 25) | **the asserts, both before the write** |
| 19 | **Dispatched TO-7 with an unqualified GO** against a priority already ruled in my own unread inbox | reading to the end, 3 min late |
| 20 | **The weaker 11:00Z carrier** (§2b) | asking whether two carriers agreed |

⛔ **#16 + #17 are one pattern and it is NEW: AUTHORSHIP SUBSTITUTES FOR RETRIEVAL.** With another
seat's artifact I open it; with my own I consult a memory of what I *meant* it to cover.
⛔ **#19 + #20 are a second: MY MESSAGE OUTRAN MY READING OF THE THING IT DEPENDED ON.** Both cost
zero **because someone else had already done the right thing — that is luck, not a control.**
⭐ **#18 is the good news.** Twice I typed a number the lesson says to derive, and **the guard held
where the memory did not.**

---

## 5. ⭐ WHAT OTHER SEATS FOUND THAT I COULD NOT

- **`1.0.0_SA_CTO~Z` asked the question that found everything:** not *"is the criterion written?"* but
  ***"is the prerequisite DURABLY CARRIED?"*** — which surfaced a missing criterion, a wrong-hit id
  collision, an un-minted id, two divergent carriers, and an inverting check. **No instrument aimed
  at the artifacts would have found one of them.**
- **They also found a fork member I had not enumerated:** the Lambda has **no bronze-replay path**, so
  an ad-hoc silver re-run **RE-FETCHES a point-in-time source past 00:00Z** — *"right-looking data
  under the wrong date is a FABRICATED OBSERVATION."* I had framed a two-member fork; the third
  decided it.
- **`3.0.0_SA_CVO~Z` caught that `POS-TO7-AC1` was SATISFIED BY A PARTITION-DERIVED DATE** — it would
  have passed while the defect stood. Hardened @284f5f68a4 before DS~Z wrote against it.
- **`0.4.0_DS_ClientPlatform~Z` dissolved item 2 by measuring before building**, and their as-of fix
  **refuses to pick a date when the sheet carries several** — *"vendor drift, not a menu."*
- **`0.4.0_DE_ClientPlatform~Z` disclosed unprompted** that their edits hot-reloaded into the port
  Andrew was assessing. ⛔ **Consequence recorded: his *"colors look good"* was formed on an UNPUSHED
  LOCAL working tree** — the artifact is right and the frame a reader would assume is wrong.

⭐ **And DE~Z's `||` catch found a LIVE one I then measured one page over:**
`Attribution/holdings-shared.tsx` has **`'Cash': 0`** consumed by **`|| 100`** — Cash sorts LAST
instead of first. **A ticker-level `CASH_USD` special case masks it, which is exactly why nobody has
seen it.** *(Mechanism source-confirmed; live impact NOT verified — routed as a finding, not a task.)*

---

## 6. Instruments

| tool | note |
|---|---|
| deployed-package census | **3 runs, negative control every time.** ⛔ **AND MY EXACT-STRING CHECK COULD NOT DISTINGUISH A FIX FROM A REFACTOR** — `_hold_as_of` is the same call one indirection away; only reading lines 1104–1130 discriminated. Banked |
| `lib/trading_calendar` | corroborated the producer's own `trading_days_behind: 1` from a seat that did not write it. ⚠ **`_USE_PMC=False`** — the **fallback** list answered; horizon 2027-12-24, **the HOLIDAY path is UNEXERCISED** (weekday arithmetic alone carried tonight) |
| `safe-commit.sh` | **9 invocations, 9 rc=0** after the gate correctly refused TO-7 once for a missing `<proof_of_spec>` |
| native `Grep`/`Read` | used where the Bash rail gate over-matched `infra/` on a **`.py`** file — the sanctioned nudge path, **no override spent**; every raw `aws`/boto3 read carried `# rail-checked` |

---

## 7. Next

1. **[whoever is alive ~11:00Z]** the ADR pre-check. **`org/XXX.md` MSTR row is the PRIMARY carrier.**
2. **[whoever is alive 13:00Z]** `ETFS-TO5-AC7`. **An ad-hoc invoke can NEVER discharge it.**
3. **[DS~Z]** `POS-TO7-AC7` — **gold reads `data_as_of` FROM THE ROWS.** Until it lands, Andrew's
   *"from bronze ingestion onward"* is unimplemented at the only layer the page reads.
4. **[DE~Z]** TO-7 AC4 (book-level as-of surface) — **a PRECONDITION of AC1 reaching users.**
5. **[Andrew]** the item-2 backfill spend card.
6. **[anyone]** `silver/holdings/2026-08-24.parquet` is **UNCHANGED at 22:00:17Z.** The as-of fix
   governs **08-25 forward**. Per `Z-S29` tomorrow is fine on both branches — **but that is not the
   same statement as "the fix is live for tomorrow."**
