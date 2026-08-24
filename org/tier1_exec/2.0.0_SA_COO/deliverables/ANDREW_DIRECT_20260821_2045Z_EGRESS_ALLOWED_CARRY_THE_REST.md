# ANDREW-DIRECT 2026-08-21T20:45Z — EGRESS ALLOWED; CARRY THE REST

**Channel:** the `2.0.0_SA_COO` terminal, in direct response to this seat's `/open-calls` card
(4 calls, 20:35Z) and its 20:41Z Call-4 correction.
**Received by:** `2.0.0_SA_COO`. **Recorded + broadcast:** same turn, per `org/XXX.md`.

## VERBATIM — the phrasing IS the ruling. Not paraphrased.

> **"egreess is allowed, other stuff doesnt really matter at this point just carry it"**

*(His spelling preserved exactly, including `egreess`. A verbatim record is not tidied.)*

---

## WHAT IT ANSWERS — the card it was spoken against

The `/open-calls` card carried **four calls plus one NOT-MINE pointer**:

| item | disposition from his word |
|---|---|
| **NOT-MINE pointer — L2 TrueShares standing-capture EGRESS confirm** (carded at CTO) | ⛔ **GRANTED — "egreess is allowed."** |
| CALL 1 — reseat MSTR | **MOOT before he spoke** (MSTR returned 20:42Z; verified on origin/CLOUD at this seat) |
| CALL 2 — `json/mdpf/*` park-lift + B2 delete | **CARRY** |
| CALL 3 — Schwab-authority ~$56.7M band | **CARRY** |
| CALL 4 — Schwab pre-2024-07-08 history feasibility inquiry | **CARRY** — ⚠ but see the scope note; it is *also* an egress ask |

**"just carry it" is a DISPOSITION, not a dismissal.** The calls stay on the queue, unanswered, and are
**not re-asked**. "Doesn't really matter *at this point*" is time-scoped to the ETFS_POSITIONING push —
it does not retire the questions.

---

## ⛔ SCOPE — SURFACED, NOT ADJUDICATED

**Two live items in the immediate context are egress asks, and his word names neither by vendor:**
1. **L2 TrueShares standing-capture egress** — the carded, blocking one; the only egress item on the
   ETFS critical path; the thing "egress" refers to in this fabric's current context.
2. **The Schwab history-feasibility inquiry** (Call 4, corrected 20:41Z) — a *different vendor*, a
   *different act*.

**THIS SEAT DOES NOT ADJUDICATE THE BREADTH OF A SOVEREIGN WORD** (`org/XXX.md`: *"SURFACE, DO NOT
ADJUDICATE"*; CLAUDE.md: neither narrow it nor widen it — *if wider scope seems plausible, ASK*).

**ACTED ON:** L2 TrueShares. It is the carded item, it is what he was answering, and it is the one that
unblocks work.
**ASKED, NOT ASSUMED:** whether it also covers the Schwab inquiry. ⛔ **Vendor egress is a NEVER-rule
requiring an EXPLICIT PER-USE word** — reading a general grant onto a vendor he did not name is exactly
the "availability is not authorization" failure. **NOTHING IS HELD on the question**: Call 4 was already
CARRY, so the ask costs nothing and blocks nobody.

---

## WHAT THE GRANT UNBLOCKS — `ETFS-c-1`, and what it does NOT change

**`ETFS-c-1` (issuer-capture plane) had a SOVEREIGN EVENT as its start condition. THE EVENT HAS FIRED.**

- **The cell's cause was already diagnosed and is NOT an investigation:** `DIVZ 0 / IDVZ 0` is a
  **missing call site** — `etfs-netassets-daily/lambda_function.py:381` defines `TS_HOLDINGS_ENABLED`,
  `:420` defines `fetch_trueshares_holdings`, and **neither is branched on nor called** (CTO
  source-confirmed).
- In `§6` of the decomp, `c-1` was one of the **8 uncovered cells**, uncovered *"by construction until he
  speaks."* **He has spoken, so it becomes coverable and takes a TO.**

⛔ **IT DOES NOT CHANGE THE ROUND-1 SHIP SHAPE, AND THIS IS ANDREW'S OWN PRIOR RULING (PRD s.10.4):
TWO FULL BOOKS + TWO SHELLS, UPGRADING FORWARD.** The page ships on that shape and **does not wait for
DIVZ/IDVZ constituent rows.** The producer (`ETFS-d-1`) is already specified to pick those rows up
**with no code change** when they land (`ETFS-TO1-AC3`, an exercised criterion).

**So the grant ADDS a lane; it does not re-sequence the critical path.** `TO-1` (producer) stays the DS
seat's front-of-queue work; the capture cell is sequenced behind it rather than competing with it —
**the page is what Andrew asked to be DONE, and nothing is allowed to slow it.**

---

## STANDING CONSTRAINTS THE GRANT DOES **NOT** TOUCH

Stated so no seat reads a green light wider than it is:
- **Production = SCHEDULED.** An ad-hoc capture run is a QA instrument, never production evidence.
- **No shadow path, no parallel emitter, no standing comparator** (Andrew, complete veto, twice).
- **Alert/monitor MORATORIUM** — the run manifest and log are the record.
- **Capture-forward only.** There is **no TrueShares backfill** (PRD s.10.2); the load-bearing check is
  `distinct`, not row count.
- **The `shared-infra` apply freeze is unaffected** and still binds.
