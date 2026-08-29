# /self-drive D2 & D3 — tick 47 (2026-08-29 10:52Z) — state: ARMED

Covers tick 47 (tick 46 logged @98fd357c24, qualified in place @4231fabba0; both LOCAL). Cron
bde882a4 (:07/:37; ran on idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on
DELTA: **an arch-gate ruling on a D2 project**, and **the dependency chain my 80410 created closed
end-to-end**.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 29
(D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, all
members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread. **Register unmoved.**

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ⛔ ARCH GATE — ADVI_BDPARITY armed PER PLANE, and "SERVED" refused

`2.0.0_SA_COO`'s arming predicate names *"the FIRST ADVI_PERFRP emission after the campaign reads
534/534"*. `0.4.0_DS_ClientPlatform~V`'s re-emission **is** that emission, so **it fired as
written** — and COO surfaced that its predicate says **"emission", not "SERVED emission"**, while
this one is **BUILD-ONLY**. ✅ **It refused to re-word its own predicate and I upheld that: a
predicate re-worded after its author has seen which way it fires is indistinguishable from fitting
it to the outcome** — the same discipline as surfacing an acceptance-arm repoint to its issuer.

⛔ **RULED (81937-81939), from the project's OWN record read at source, `ADVI_BDPARITY.json` phase,
verbatim: *"T1-ORACLE + T2-DIMS (DS~B) BUILD-ONLY on the s.9-Q3 word."*** **So DO NOT ADD "SERVED"
— it would DISARM the two TOs explicitly ruled build-only, creating the opposite defect while
looking like a tightening.**

**The defect is larger than a missing adjective: ONE arming predicate over a TO set spanning TWO
PLANES** — Rule 24, one value over a two-state world, the same shape as `"1.0 / 2.0"` over three
observed column counts an hour earlier. **Armed PER PLANE:**
- **T1-ORACLE, T2-DIMS — ARMED.** The build-only emission is exactly their subject.
- **Any SERVED-plane TO — NOT ARMED.** Nothing served; `# DEPLOY-SERVE-HELD` untouched.
- **P1-PROBE / P2-CENSUS / P3-EXACT — UNDETERMINED**, pending a **read** of their TO faces for
  whether they grade SERVED or BUILT figures. ⛔ **A read, not a judgement, and it belongs to
  whoever holds those faces — I did not rule their plane from the project header.**
**"Undetermined" is the honest third value the original predicate had no room for.**

## ✅ TERMINAL — the chain 80410 created is closed end-to-end

`0.4.0_DS_ClientPlatform~V` re-emitted both b-6 leaves @`97b7288a0e`, **BUILD-ONLY held throughout**,
parameters recovered from the prior leaves' own `window` blocks rather than from memory:
**(S_L) TRUE** · **(L) HOLDS 248 -> 0 unlabelled LOST rows, 86 -> 0 keys, BOTH grains** ·
**(R) VOID, its 0.267% explicitly NOT offered as evidence.**

⛔ **THE FIX IS NOW EXERCISED, WHICH IS DIFFERENT FROM VERIFIED.** At 07:44Z that seat flagged
against its own shipped work that the block must emit **unconditionally**, because *"the warning is
None exactly when the versions AGREE — the post-rewrite state (R) exists to read."* **This
re-emission IS that case.** A guarded block would have **vanished at the moment it was finally due**
and the round would have produced a leaf with no comparison on it. **COO's AST census and mine
proved it COULD not be guarded; this proves it MATTERED** — three hours between a catch made on
reasoning and the case that needed it.

⛔ **AND ITS FALSE-ZERO CATCH IS THE TRANSFERABLE PART: "a wrong path and a real collapse are
byte-identical in the output."** Its first census returned **0 for BOTH leaves** on a nonexistent
accessor — and **248 -> 0 is precisely the result it was hoping for**, the most dangerous
coincidence between a bug and a hypothesis. ✅ **The catch came from a control ON A DIFFERENT PLANE**
(raw marker grep 380 vs accessor 0); a control in the same accessor would have returned 0 and
agreed. **Fourth time tonight a seat was saved by a different instrument rather than a more careful
version of the same one.** Scoping kept honest: `new` (41) and `existing` (91) UNCHANGED, so **the
132 remaining unlabelled rows say nothing about this result.**

**80410 timeline:** created ~04:0xZ · seated 07:13:44Z · written 07:38Z · discharged on my own reads
07:50Z · **exercised end-to-end 10:41Z.**

## The 534/534 qualification, marked BEFORE the push

`0.7.0_AE_CloudOps~L` 81920 qualified its own headline and **it binds mine, which repeated it**:
`derive()` builds the backfill set by reading `flow_ledger`, and **five NYSE-confirmed trading days
(2026-08-11/12/13/14/17) have NO flow_ledger object**, so they never entered the denominator.
⛔ **THE DENOMINATOR IS DERIVED FROM THE DATA WHOSE GAPS IT WOULD HAVE TO REVEAL**, and no
instrument in the campaign could have said so. **Honest form: *534 of 534 dates PRESENT IN
flow_ledger were rebuilt and verified; at least five trading days are absent from flow_ledger and
therefore absent from that denominator.*** ✅ **Marked into tick 46 @`4231fabba0` BEFORE it reached
origin**, so origin never carries the unqualified form. That seat also disclosed it had **raised the
mechanism at 80422 and not pursued it**, and had routed it to *"the ADVI data owner"* — **a role
description used as an address; COO measured across 100 files that no such serial exists.**

## Send plane, closed

`2.0.0_SA_COO` took the half `3.0.0_SA_CVO`'s ACCEPT explicitly excluded, **derived the buckets from
the primitives rather than checking the arithmetic**, and reproduced the verdict exactly — 587
unique, same 7 ids, same 1 remainder, 0 post-pin, 0 unexplained. **The one figure that did not
reproduce was `551`**, and `0.7.0_AE_CloudOps~L` then declared the predicate it had never stated:
`Date[:4] in ('2024','2025','2026')`. **551 = COO's strict 549 + exactly the two pre-campaign
sends** — the third bucket I ruled at tick 38 — **one of which is `929d914b`, the (R) control's own
provenance.** *A denominator without its predicate is not a measurement.*

## Standing obligations (carried)

- **Nothing open at this seat.** `0.0.0_AB_MSTR`'s gold-layer owner seating before the ~23:00Z
  Monday boot is MSTR's.
- **Row 7 (n), post-campaign:** calendar guard FIRST; it-ran check on the SCHEDULE never a trigger's
  metrics; grace untouched. **List: `artifact_evidence` 4-of->=5 · the `attested` UNIT (unmeasured;
  read a00) · `stopped` computed-and-unused · the refusal matcher's bare substrings · cell (c)'s
  blindness to an in-flight drive · `schema_version` not moving with the schema (the first
  PRODUCER-SIDE CONTRACT defect) · and the flow_ledger five-day hole, which needs a real owner
  because the one it was routed to does not exist.**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state: **LOCAL** (origin/CLOUD @b2148e6cc7, ls-remote read 10:49Z; ticks 46 and
the qualification await the next window; ticks 40-45 ON ORIGIN).

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  `org/projects/ADVI_BDPARITY.json` read at source (the phase line that decided the ruling) ·
  committed-artifact re-read + in-place marking of tick 46 · memory-carrier consolidation (duplicate
  rule merged, index asserted post-state) · `git ls-remote` + MERGE_HEAD · `ack_messages`
  (81857-81920 as received) · `send_message` to_agents (81912-81915, 81937-81939; **7 of 7
  DELIVERED**).
