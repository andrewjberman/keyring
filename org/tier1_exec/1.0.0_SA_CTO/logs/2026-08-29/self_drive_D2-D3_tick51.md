# /self-drive D2 & D3 — tick 51 (2026-08-29 12:50Z) — state: ARMED

Covers tick 51 (tick 50 logged @a899dab830, **ON ORIGIN**). Cron bde882a4 (:07/:37; ran on idle).
Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). **Written SHORT and on a narrow delta: the scope
did not move at all this tick, and everything below is a correction to a claim of MINE.**

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 28
(D2 21, D3 7) — **identical to tick 50**. Flags none. Device LAPTOP. Claims scan **342 of 342
JSONs**: D2 7 / D3 1, all members, **0 claimed-not-member**. No MERGE_HEAD.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## Five corrections, all to my own published positions

⛔ **1. MY CONFOUND HYPOTHESIS IS DEAD.** I proposed today's foreign-ack spike might be measuring the
investigation (bulk acks, by the audited seats, inside the window) **and named the discriminating
cut.** Two seats ran it independently: **7.73% BEFORE vs 5.00% DURING; 113 of today's 115 predate
12:05Z.** ✅ **The spike is real; the audit did not cause it.** **A well-posed question and a wrong
suspicion — which is what naming a cut instead of asserting a cause is for.**

⛔ **2. A CAUSAL CLAIM I WROTE TO THIS SEAT'S DURABLE MEMORY WAS REFUTED, AND I REPLACED IT RATHER
THAN SOFTENING IT.** I had recorded the footer-paste as the mechanism — *"inevitable rather than
careless."* **Measured across 5,947 ack calls: the OPPOSITE. Bulk 11+ is the CLEANEST shape (0.07%,
1 in 1,474); small 2-3 batches the WORST (5.77%).** ⛔ **And shape does not explain the variance at
all — it is PER-SEAT: one serial at 20-30% at EVERY shape, two at 0.00% at every shape including
36-id calls.** **The structural excuse is false, and I adopted it while being one of the worst
offenders.** Corrected in the carrier with a post-state assertion (4 of 4).

⛔ **3. THE UNIT ON MY 47 WAS WRONG: `acked_by` CARRIES A SERIAL, NOT A SESSION** (`3.0.0_SA_CVO`'s
bound; `0.7.0_AE_CloudOps` measured it). **My serial's 47 splits 08-21:10 · 08-24:1 · 08-25:23 ·
08-26:6 · 08-29:7, and today's 224 acks show ZERO >90-min gaps — so today is one sitting and the 7
are mine.** ⛔ **I neither claim nor disclaim the other 40: unattributable by sitting, and "probably
a predecessor" is the comfortable inference I would refuse from anyone else.** ✅ **The DAMAGE claim
is unchanged — the rows are the same rows whoever wrote them.**

⛔ **4. I MISATTRIBUTED A GOOD ACT, TO FOUR SEATS.** I credited the serial-vs-session point to
`0.7.0_AE_CloudOps`; **`3.0.0_SA_CVO` stated it first (82485 §5(b)).** **The bound is CVO's, the
measurement and the positive control are the base seat's.** **Committed while assembling the
aggregate that made this very class visible.**

⛔ **5. MY CLEARANCE WAS RIGHT ON AUTHORITY AND SILENT ON TIMING.** I told the entry's author that
fixing its own entry needed no word from me. **It found the reason to wait: the card at Andrew
QUOTES THE ENTRY'S CURRENT TEXT, so editing it mid-flight would make a sovereign card's quotation
stale.** ⛔ **AN AUTHORITY CLEARANCE IS NOT A TIMING CLEARANCE**, and had it acted on mine
immediately, my ruling would have been what invalidated a card in flight.

## Verified rather than asked

✅ **The card at Andrew was in my own inbox and I measured it instead of asking whether it was
accurate:** `"ZERO call sites"` appears once, **quoted AS THE FALSE HALF** under *"a fact about the
record you should have before deciding"*, with all three call sites at `file:line` and the wrapper
named *"not a third copy"*. **Correct and complete; nobody needs to chase it.** ⛔ **My first
instinct was to ask — in an hour whose whole lesson is that.**

## Standing state

- ✅ **Nothing open at this seat.** A-vs-B closed and with Andrew; the ACK remedy is
  `0.0.0_AB_MSTR`'s, carrying my ruling that **the ACK writes the READ clock ONLY**.
- **Tracked, not mine:** the freshness gate (its guard does not fix the live case — the key names the
  WRITE date); row 7 re-opened; `safe_deploy_core.py:548` working-tree bytes; AC6-MANIFEST + AC7.
- ⛔ **Open and NOT mine: what produced the pre-12:05Z spike today.**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope. **`2.0.0_SA_COO`'s `freshguard-leg4` card is in flight and complete.**

state: ARMED · push state: read at commit.

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  `broker.db` copied and queried READ-ONLY (foreign acks by date; >90-min gap test on today's 224) ·
  card content measured in my own inbox · memory-carrier correction with post-state assertion ·
  `git ls-remote` + `rev-list --count` + MERGE_HEAD · `ack_messages` — **explicit list from each
  opened file's `Msg-ID` line, NOT a span**: 82482, 82494, 82497, 82509, 82514, 82537, 82544, 82547,
  82557 · `send_message` to_agents (82489-82492, 82505-82508, 82526-82529, 82539-82542,
  82551-82554; **20 of 20 DELIVERED, 0 QUEUED**).
