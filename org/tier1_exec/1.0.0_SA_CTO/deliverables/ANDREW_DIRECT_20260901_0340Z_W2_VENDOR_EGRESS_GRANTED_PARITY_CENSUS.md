# ANDREW-DIRECT 2026-09-01 ~03:4xZ -- W2 VENDOR EGRESS GRANTED (the 5,309-account parity census)

**Seat:** `1.0.0_SA_CTO` (CTO terminal, Andrew present)
**Recorded:** 2026-09-01 ~03:4xZ, **BEFORE the act fires** -- deliberately, see s.4.
**Relayed at:** msg 90604-onward to `2.0.0_SA_COO` (Andrew named COO as the addressee).

---

## 1. THE WORDS, VERBATIM

> "you have vendor egress yes, granted, talk with COO and lets get this done"

Given in direct answer to this seat's question naming **W2 -- the `ADVI_BDPARITY` full-population
parity census, 5,309 accounts, performance feed only** -- and its cost (~2.1 h at concurrency 50,
~4.1 h at concurrency 1, per the census plan `@6a99820c40` graded PASS by `3.0.0_SA_CVO` 86884).

---

## 2. SCOPE -- NARROWED BY THIS SEAT, AND THE NARROWING IS DISCLOSED

⚠ **His phrase "you have vendor egress" is BROADER than the act it answers.** This seat scoped it to
W2 rather than reading it as a standing grant. **That is this seat's construction, not his words**,
and it is recorded as such so he can widen it if he meant wider.

**COVERED:** the W2 census pull, performance feed only (`feeds=["performance"]`; the per-feed
selector is live and was read on the running artifact `@3f439d2e4e`, so the pull cannot starve
`OPAL_TAXSMA_PT2`).

**NOT COVERED:**
- Any further Cottonwood re-run. **NO-THIRD-FIRE stands** (ruled 90593), discharge condition a
  MEASURED BD roster change `15 -> 14`.
- Any pull outside the census plan `@6a99820c40`.
- Any other vendor, any other feed, any other date range.

---

## 3. ⛔ TWO GATES SHARE THE LABEL "W2" -- ONLY ONE IS DISCHARGED BY THIS

**RESOLVED by `2.0.0_SA_COO` msg 90608 (03:3xZ), measured at source in
`org/projects/ADVI_BDPARITY.json`: BOTH ARE TRUE. TWO GATES, ONE LABEL.**

| Gate | What it is | Owner | State |
|---|---|---|---|
| **A** | per-use vendor-egress word, the 5,309-account BD pull | **Andrew** | **DISCHARGED 03:4xZ** by the words in s.1 |
| **B** (`Y-MINT-SEQ`) | sequencing hold at `0.4.0_DS_ClientPlatform~Y`, premise *"wait for the 00:00Z mint"* | `2.0.0_SA_COO` | premise DISSOLVED; **release pending in its own message** |

⏱ **CROSSED IN FLIGHT, and the ordering matters:** 90608 states Gate A is "NOT GIVEN". **That was
true when written (03:3xZ) and was superseded roughly ten minutes later** by Andrew's grant, relayed
at 90604. Anyone reading 90608 alone will read a stale state. Gate A **is given**.

⭐ **`2.0.0_SA_COO` RENAMED GATE B RATHER THAN RELEASING IT**, and the reasoning is the sharpest act
of the exchange: *"If I release GATE B and it is read as 'W2 released', a 5,309-account VENDOR PULL
fires with NO SOVEREIGN WORD. That is the failure mode, and it is one message away."* It declined to
release a gate while the collision was live, renamed it, and will release it separately stating
explicitly that the release **does not convey egress**.

>> **THE TRANSFERABLE SHAPE: A NAME COLLISION ON TWO GATES IS NOT A TIDINESS PROBLEM. It is a
   mechanism by which discharging the cheap gate silently discharges the expensive one.** The remedy
   is to rename BEFORE releasing either -- not to release carefully. <<

⛔ **Both gates must now be discharged in words, separately.** Gate A is discharged by this record.
Gate B is not discharged by anything here and must not be read as such.

---

## 4. ⭐ WHY THIS RECORD EXISTS BEFORE THE ACT RATHER THAN AFTER

One hour earlier, this seat relayed a vendor-egress order (msg 90576) for which **no committed
durable record existed**. `0.6.2_AE_PartnerETL` executed it and then correctly flagged that its own
four-condition test's condition 3 was UNMET at fire time -- the comparable 23:20Z order had
`fad321cf07` to read, and that one had nothing but a live message.

**That record was written after the act returned. This one is written before it fires.** The lesson
is only banked if the next instance is different, and this is the next instance.

---

## 5. THE OUTSTANDING STEP-9b QUESTION, AND WHY IT DOES NOT DELAY THE ACT

Msg 90602 asked `0.4.0_DS_ClientPlatform~Y` whether it expects the census to COMPLETE, and **which
outcome would actually discriminate**. It has not returned. **Andrew has said proceed, so nothing
waits on it.**

What binds instead is a STATEMENT, not a permission -- `/endpoint` 9b-ii `@53359a7ecb`: **the seat
holding an act that spends a sovereign per-use word states its expected outcome in the same turn it
fires, and if it expects failure it says so BEFORE, not in the report.**

**Cause, recorded so the rule is not read as bureaucracy:** at 02:49:51Z an authorized run fired
against an on-record prediction of identical failure and failed identically. The word was spent for
nothing. **The defect was at the option text this seat authored, not at the executing seat.**

---

## 6. WHAT IT UNBLOCKS

`P2-CENSUS` completes -> `P3-EXACT` (the drive-to-EXACT loop) opens. **5 of the 22 D2 task orders.**
Andrew's standing sequencing is ALL D2 FIRST, so this is the current lane rather than a jump ahead.

Acceptance is the already-graded plan `@6a99820c40` -- printed denominators (attempted / classified
/ refused against 5,309), the four declared grains, per-class counts. **No new acceptance is invented
here, and rc is not a verdict: the artifact is.**
