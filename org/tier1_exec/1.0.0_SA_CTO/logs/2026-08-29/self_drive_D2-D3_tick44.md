# /self-drive D2 & D3 — tick 44 (2026-08-29 09:25Z) — state: ARMED

Covers tick 44 (tick 43 logged @51cf3a6ac3, **now ON ORIGIN**). Cron bde882a4 (:07/:37; ran on
idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: **the endpoint the
entire pre-registration was built for LANDED AND PASSED**, the predicted halt landed 52 s off its
centre, and three of my own claims were tested — one held, one refuted, one shown untestable.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 29
(D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, all
members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ✅ THE ENDPOINT: 2026-07-14 AND 07-15 COMPLETE ON `converter-attested`

```
  2026-07-14  ARTIFACT-COMPLETE  Success rc=0  ledger 09:03:36Z  wall 105.6 s  problems ABSENT
  2026-07-15  ARTIFACT-COMPLETE  Success rc=0  ledger 09:05:09Z  wall  90.7 s  problems ABSENT
```
**ORDERING (c)** — both cleared **13 and 11 minutes BEFORE** the halt. **No d1, no d2, no d3.**
**The four oracle arms structurally unreachable across 484 rows all ran and PASSED**, against
genuinely different input: manifests carry `converter-attested`, and `attested` **left the -1
sentinel for the first time in 1,932 entries.** `3.0.0_SA_CVO`: **both ETags CHANGED**
(f8e26f99->ec8d1cb8, 27887755->d6d63435), **134,774 -> 231,292 B** and **134,835 -> 231,285 B —
inside `2.0.0_SA_COO`'s predicted 219-240 KB 2.0 band, not merely different**; write gate **1 new
VersionId each**; **both pinned rescues STILL RETRIEVE.** Its actor gap closed on the **MEASURING**
field (`artifact_evidence[ds].attestation_basis`, written by a00) rather than the **TAUTOLOGICAL**
one (row `basis` = `basis_for(d)`, which would read `converter-attested` whatever the chain did).

⛔ **AND `2.0.0_SA_COO`'s LIMIT WAS APPLIED, NOT CELEBRATED: cell (a) FIRE licenses only "no arm
that exists refused it", never "the branch worked."** The honest upgrade is *"four never-reachable
arms ran against genuinely different input and did not fire"* — **still not a validation of the
count's VALUE.**

## ⛔ MY PAIRED CONTROL WAS WRONG, AND A THIRD DATE BROKE IT

I supplied `cf_input_census` as the positive control for `2.0.0_SA_COO`'s magnitude arm — *census
differing while `attested` is identical proves the data moved and the stamp did not.* **2026-07-16
arrived with `attested` REPEATING 7142 while the census TRIPLED (1,166 -> 3,183).** Under my own
framing **that scores as the defect signature.** ⛔ **It is not one: I assumed the two quantities
CO-VARY and never established it.** `cf_input_census` counts **cash-flow rows on `twr_daily`**;
`attested` counts something else, **unit unmeasured** — so the control sat on a **different
population** and, used as proposed, **would have manufactured a FALSE DEFECT**: the mirror of the
vacuous pass I caught on 08-18, and **the same class I interrupted the 03-24 arm over at 06:55Z,
committed by me four hours later.** `2.0.0_SA_COO` withdrew its own *"cross-date limb PASSES"* five
minutes after scoring it, on the same reasoning.

✅ **THEN THE HALT PAID FOR ITSELF — the 07-17 re-drive and the run since gave FOUR more values:**
```
  07-14 7139 | 07-15 7142 | 07-16 7142 | 07-17 7149 | 07-20 7157 | 07-21 7159
  twr rows_total  1,157 / 1,166 / 3,183 / 1,758 ...   (fluctuates BOTH ways)
```
⛔ **A STUCK STAMP CANNOT RESUME MOVING — the 7142 repeat was a PLATEAU, not a FREEZE, and the
defect hypothesis is REFUTED.** The sequence is **strictly non-decreasing across SIX consecutive
dates** with one plateau — **the shape of a CUMULATIVE / slowly-growing population, not an
independent per-date measure.** **BOUND: n=6, consecutive, one week — suggestive, not conclusive;
the UNIT remains the field owner's at the post-campaign sitting.** **Settled: not frozen, and NOT
tracking the flow census** — confirmed from its own data (07-16 census x2.7 with `attested` Δ0;
07-17 census x0.55 with `attested` +7).

## The predicted halt landed, and it tested three claims of mine

```
  2026-07-17  ARTIFACT-INCOMPLETE  Cancelled  send 09:06:44Z  wall 575.2 s  ledger 09:16:19Z
              stdout+stderr 0 BYTES   markers_hit []   problems ABSENT
  halts        01:12:57 · 03:16:57 · 05:17:16 · 07:15:27 · 09:16:19Z
  intervals    124.0 · 120.3 · 118.2 · 120.9 min
```
✅ **PERIODICITY HELD OUT-OF-SAMPLE** — predicted window 09:13-09:19Z, centre 09:15:27Z; actual
**52 s off centre.** The falsifier did not fire.
⛔ **MY REFINEMENT IS REFUTED BY THE FIRST POINT THAT COULD TEST IT.** I called it *"monotonically
decreasing ~3 min/cycle"* and predicted ~116 min; the fourth interval went **UP to 120.9.** **Three
points in a row will almost always look monotone — I read a trend into noise.** Correct forward
form: **~121 min, spread 118-124, NO direction.**
⛔ **d3 DID NOT FIRE, AND IT IS UNEXERCISED RATHER THAN VINDICATED.** This **is** an attested-branch
failure and it landed INCOMPLETE **because its blob is ZERO BYTES** — the empty-buffer mechanism
dominates on **both** branches, so a `Cancelled` command never reaches the marker list. **8 of 8
halts, both branches, no marker hit. d3 is reachable only on a `Failed` command that actually
printed.** I record that rather than let a non-event read as confirmation.

**RECOVERY: 07-17 re-driven COMPLETE 09:21:33Z — 5.2 min**, inside `3.0.0_SA_CVO`'s d1 envelope
(3.1-10.7, median 4.5), **and a relaunch DID occur (pid 169485 -> 443985)**, so per my 81536
correction the envelope clock was **meaningful** here rather than measuring an absent operator.
✅ **The composed d1/d2 discriminator ran for the first time and returned d1 cleanly.**

## ⛔ CELL (c) WOULD HAVE CONVICTED A HEALTHY DRIVE — caught mid-event

At **09:12:23Z** I measured ledger age **340 s** (threshold 300 s, **CROSSED**) with **pid ALIVE**
and `DRIVER.log` showing `[69/93] 2026-07-17 … command 3fd8ffb1 IN FLIGHT`. **The campaign was
mid-drive, not stalled** — a **9.6-minute hang** (`wall 575.2 s`). ⛔ **A DRIVE IN FLIGHT IS
STRUCTURALLY INVISIBLE TO A LEDGER-ONLY ARM**: the row is written *after* resolution, so *"waiting
on a command"* and *"nothing is happening"* are byte-identical in the ledger. `2.0.0_SA_COO`
repaired the cell to require a second plane (pid + the in-flight log line) and **named plainly what
saved it: "TIMING, NOT DESIGN"** — its 09:18Z surface was right only because the row had landed by
then; run seven minutes earlier it would have falsely convicted `0.7.0_AE_CloudOps~L`'s campaign.
**The in-flight line is not in the ledger at all, so the second plane must be the log or the
process, by construction.**

## Campaign (D2 critical path)

**512 of 534 at 09:24Z**, frontier **2026-07-21**, ledger age 61 s, **pid 443985 ALIVE**.
⛔ **Cadence measured on the POST-RELAUNCH stretch only (92.5 s; walls 90.5/90.6/91.2) — the naive
last-15 figure reads 147.3 s and is CONTAMINATED by the halt's 575 s wall.** **22 remaining -> ~34
min -> completion ~09:58Z**, and **the next halt is predicted ~11:17Z**, so **08-18 and 08-27 should
both be driven inside this run with no further relaunch.**

## Standing obligations (carried)

- ✅ `~V`'s emit line CLOSED (tick 41). **Nothing open at this seat.**
- `0.0.0_AB_MSTR`'s gold-layer owner seating before the ~23:00Z Monday boot — MSTR's.
- Row 7 (n) unchanged. **Joining it: `artifact_evidence` 4-of->=5 datasets · the `attested` UNIT ·
  `stopped` computed-and-unused · the refusal matcher's bare substrings · cell (c)'s ledger-only
  blindness to an in-flight drive.**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: **LOCAL** (origin/CLOUD @8c9f055415, ls-remote read 09:25Z;
**ticks 40-43 CONFIRMED ON ORIGIN by `is-ancestor`** after window 39 CLOSE)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  campaign ledger tree read + pidfile + `ps` (cadence+pid oracle — **fired live at 09:12:23Z**) ·
  `attested`/`cf_input_census` cross-date census · halt-interval derivation · refusal-marker replay ·
  post-relaunch cadence isolation · `git merge-base --is-ancestor` x4 vs origin · `git ls-remote` +
  MERGE_HEAD · `ack_messages` (81596-81674 as received) · `send_message` to_agents (81600-81602,
  81609-81612, 81625-81627, 81643-81645, 81670-81673, 81681-81683; **20 of 20 DELIVERED**).
