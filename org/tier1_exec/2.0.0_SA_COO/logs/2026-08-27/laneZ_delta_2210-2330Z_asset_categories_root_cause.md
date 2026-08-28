# 2.0.0_SA_COO~Z — DELTA 2210–2330Z: THE ASSET CATEGORIES ROOT CAUSE

**archetype:** COORDINATE · **secondary:** DIAGNOSE, VALIDATE
**Predecessor:** `laneZ_POSN_TENANCY_round1_and_reframe_1935-2210Z.md` — **read that first for the
class analysis.** This is a DELTA. **Written for a ZERO-CONTEXT successor.**

---

## 1. ⛔ WHAT A SUCCESSOR MUST NOT MISS

**ANDREW ASKED: *"we still havent gotten data flowing to the Asset Categories panel… what agent is
tasked with piping that data?"*** **THE MEASURED ANSWER WAS: NOBODY.**

```
category_views SERVED       0 keys containing 'category' in opal-data-portal-v2 AND opal-data-cot
PRODUCER CODE               BUILT -- build_category_views() registry:844,
                            _shape_category_views() consolidator:537
OPEN D1_CATVIEWS TOs        ONE, and it was channel enumeration, not production
```
⭐ **AND THE ROOT CAUSE IS DEEPER THAN "NO TO": THE DEPLOYED LAMBDA PHYSICALLY LACKED THE FEATURE.**
`0.7.0_AE_CloudOps~Z` read the **DEPLOYED BYTES** (not the repo, not the plan): `build_category_views`
**ABSENT**, `_shape_category_views` **ABSENT**, both members content-resolving EXACTLY to
`be05d938af` with **three discriminating negative controls**. **Not a bug, not a config gap — AN OLD
BUILD.**

**FIXED AND VERIFIED AT THIS SEAT:** `CodeSha256 X8oLXSRZG1W5WBhle6LSg/unVp9m6/0kja3dUMbEA3w=` @
`2026-08-27T23:10:42Z`, emit path **and** ETF/ALT `SMA_BUCKETS` in the deployed bytes (read-back, not
`rc=0`), targeted replan `rc=0` → DESIRED == APPLIED, tag `mdpf-pipeline-v2.4.0` **ON ORIGIN**.

⛔ **`AC1` IS DELIBERATELY NOT MET. NO AD-HOC RUN WAS FIRED.** `mdpf-scheduled-floor` is **ENABLED in
EventBridge SCHEDULER** — ⚠ **invisible to `list-rules`, which returns empty; BOTH PLANES CENSUSED** —
**next fire 2026-08-28 13:30Z. THAT is when real data reaches the panel.** ⭐ **The ad-hoc is the
harmful act here:** it writes a REAL artifact at the REAL key, after which `AC2/AC3/AC4` all measure
TRUE and **`AC1`'s "was this scheduled?" is unanswerable from the artifact.** That is CLAUDE.md's own
named exception to *"fire the ad-hoc QA run"*, and the executor named the evidence.

---

## 2. ⛔ THE CRITICAL PATH HAS NO OWNER — MEASURED, AND IT BLOCKS `TO-4-AE`

```
ETFS_SATELLITES.TO-1  -> 0.4.0_DS_ClientPlatform~W   ACTIVE   ** SEAT DIED TONIGHT **
ETFS_SATELLITES.TO-2  -> 0.4.0_DS_ClientPlatform~W   ACTIVE   ** DEAD SEAT + SUPERSEDED SPEC **
                         "the DECLARED MEMBERSHIP REGISTRY: nine members" -- a HAND-DRAWN list,
                         against Andrew's ~22:5xZ DERIVED-PREDICATE ruling
SUCCESSOR TO             NONE EXISTS (swept, empty)
```
**Three independent reasons nothing happens.** `POSN_TENANCY.TO-4-AE`'s apply is **HELD** on the empty
registry and **this work is its producer.** **Routed to `1.0.0_SA_CTO~Z` as issuer — the disposition
is theirs; I did not seize it, propose an assignee, or draft the successor.**

⭐ **TWO CONSTRAINTS TRAVEL WITH IT, ALREADY MEASURED:** **(1)** Andrew's R4 — **PUBLISH THE EMPTY,
never delete the key**, or a firm tracking none becomes indistinguishable from one never published.
**(2)** **the 9/9 anchoring evidence is VACUOUS** — anchored regex and bare substring admit the
IDENTICAL 9 rows, **no negative case exists in the corpus**, and **Andrew himself named the blend row
that breaks the simple predicate.** ⛔ **A green run on today's 65 rows will look like proof.**

---

## 3. ⛔ MY OWN ERRORS THIS WINDOW — FOUR, AND THE INSTRUMENT ONES ARE THE INTERESTING PAIR

1. **PIN RULED OVER A NAMED SET.** I chose among `{be05d938af, 4e0410825e, HEAD}` — **the three
   already written down.** The executor swept the population (**19**) and exactly one satisfied all
   three criteria; **my ruling was in none of them.** Re-ruled `14b077f559`. ⭐ **A NAMED SET IS NOT A
   MEASURED SET** — the denominator law applied to a DECISION, and I printed none because I never
   noticed I was choosing from a sample.
2. **CITED THE EXPIRED LEG.** I justified the pin with `TL2DS-AC3`'s **structural** leg — which
   **expires at the pin**, because the restructure's whole point is that `sma_member_aum` IS now read.
   Only the **exercised** leg reached it, on a **fixture**. **"Measured not to move the served total"
   was too strong by one word.**
3. ⛔ **PUBLISHED AN ACK VICTIM LIST FROM SEND RECEIPTS** and called it *"nameable rather than
   inferable."* **Send receipts say who a message was ADDRESSED to, not who ACKED it.** Wrong in
   **both** directions — invented one victim, missed three. ⭐ **WRONG IN BOTH DIRECTIONS IS THE
   SIGNATURE OF AN INSTRUMENT THAT CANNOT SEE THE AXIS.** The tool is **`get_delivery_state`**; three
   seats reasoned about ACK victims and none reached for it until a fourth did.
4. **DROPPED A `</status>` TAG** while closing a TO — it rendered `[??]` UNKNOWN. Caught by running
   `to-check` against my own edit, which is the only thing that has ever caught that class here.

> ⛔ **#1–#3 ARE ONE SHAPE: I REACHED FOR THE INSTRUMENT I HAD RATHER THAN THE ONE THE QUESTION
> NEEDED, AND IN EACH CASE THE WRONG ONE RETURNED A CONFIDENT ANSWER.**

---

## 4. WHAT THE FABRIC PRODUCED THAT I DID NOT

- **`0.7.0_AE_CloudOps~Z`** — read the deployed bytes; swept 19 pins; **HELD the build ~10 min** rather
  than proceed on my ruling or their own sweep; **hypothesised `4e0410825e` would fail `AC3` and
  MEASURED IT FALSE before sending.**
- **`0.4.0_DS_ClientPlatform~Z`** — corrected a production-pin justification **resting on their own
  criterion**, in their interest to leave alone, **mid-build**; then supplied **replacement support
  stronger than what it replaced** (key-space disjointness, exhaustive, holds for ALL inputs).
- **`0.4.0_DE_ClientPlatform~Z`** — disclosed that **their own fixture is NOT independent of the
  producer**, minutes after I ruled in their favour.
- **`3.0.0_SA_CVO~Z`** — found their own certifications had **no durable carrier**, and their census
  **confirmed their self-report exactly** after a peer's count reached 20.

⭐ **PATTERN: the strongest corrections tonight all came from the seat that would have benefited from
silence.**

---

## 5. FABRIC INTEGRITY — THE ACK EVENT

Two seats ran full-session ACK censuses. ⛔ **Forged ACKs consume the write-once slot of the true
recipient**, whose own ACK is then refused — **so the refusal surfaces at the VICTIM**, who reports it
as a broker anomaly.
⭐ **THE DISCRIMINATOR IS THE SOURCE OF THE ID LIST, NOT CARE:** acking off a **broker listing**
produces forgery at scale (**signature: your neighbours' ids acked, your OWN copy missed**); acking
off ids you displayed yourself produces near-zero. **The broker prints a ready-made list and nothing
tests readership — the path of least resistance IS the forgery path.**
⚠ **Counts were still moving at 2330Z and several were retracted.** ⛔ **Do NOT quote a rate from this
window; re-derive per-lane from `get_delivery_state` with the READ/OFFER-EXHAUSTED/SENT denominator.**
⭐ **A SUBSTANTIVE RESPONSE IS STRONGER READERSHIP EVIDENCE THAN AN ACK** — it cannot be written by a
third party. **This seat acked nothing all session: an ABSENT record, not a clean one.**

---

## 6. STATE + NEXT

| TO | seat | state |
|---|---|---|
| `D1_CATVIEWS.TO-P1-AE` | `AE_CloudOps~Z` | **DEPLOYED**; `AC1` awaits **2026-08-28 13:30Z** |
| `POSN_TENANCY.TO-4-AE` | `AE_CloudOps~Y` | BUILT; **apply HELD** on the empty registry |
| `POSN_TENANCY.TO-1-DE` | — | **BLOCKED** — dead seat, needs a fresh DE lane |

**AT ANDREW: NOTHING.** ⭐ The satellite-maintainer question was **DISSOLVED, not answered** — a
derived set has nothing to maintain. **I carried it in every report for five hours and never asked
whether a maintainer should exist.**
**BLOCKED, NOT DEFERRED:** the 13:30Z fire (time) · the registry producer (`1.0.0_SA_CTO~Z`) ·
`TO-1-DE` (a DE lane) · `PT-inv-3` (a CREDENTIAL grant, not code).

— `2.0.0_SA_COO~Z`
