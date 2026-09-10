# ROUND 2 ANALYSIS -- ETFS_GUARDRAIL

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-10 ~04:3xZ
**On the slug:** `surprise-channel/adjudications/ADJUDICATION_v1.md` @`1ea6da48c4` (`3.0.0_SA_CVO`, msg 94978;
rows C-S15..C-S17, 17 rows)
**Completion report / packet:** `ledger/L8_PACKET.round2.partial.md` v5 @`616b49f610`,
sha256 `b3c49c6a499fa56e41819fc2b497764b8d73b97cb8340de908ade87bff6444a1` over 24,349 bytes -- hashed by the
issuer AFTER its own commit and re-computed independently at the CVO before reading. **Graded against PRD v0.6.**

---

## 1. Coverage

**5 of 5 orders terminal and drained. 0 of 57 investigation items undispositioned**, 0 duplicate ids, by
`comp-surprise`'s own census at the CVO. Every live endpoint outcome is served by a cell. **No PRD addendum:**
v0.5 and v0.6 already carried this round's two endpoint changes (the supersession of FWD-2/FWD-7, and FWD-4's
move onto the slice plane), so the answer is this analysis.

**This project had no `COMPLETION_GRADES` artifact for round 1 either.** That is the same gap I found and
closed at NFRA_OUTSET an hour ago, and it is the same seat's. `COMPLETION_GRADES.round2.json` is minted with
this analysis; round 1's verdicts live in `ROUND_ANALYSIS.round1.md`'s own table and are cited row by row
rather than re-derived.

## 2. The round moved seven of eight outcomes off NOT_EVALUATED

Round 1 graded **one** outcome REALIZED (FWD-6) and seven NOT_EVALUATED, every one of them waiting on an event
nobody controlled -- the 10-01 fire, a real refusal, a real terminal failure, a real stop-and-ask. **Round 2 is
what Andrew's ~03:0xZ law looks like when it is applied to a live project the same night it is written:** the
waits were converted into acts, the acts were driven, and the outcomes were graded on what the acts produced.

| | round 1 | round 2 |
|---|---|---|
| REALIZED | 1 | **4** |
| NOT_REALIZED | 0 | **2** |
| NOT_EVALUATED | 7 | **2** |

The two that remain NOT_EVALUATED are FWD-9 and FWD-10, which did not exist eight hours ago -- they were
minted last night to replace the two outcomes whose only proof was a failure nobody could schedule.

## 3. The grades, and the two that are NOT_REALIZED are the honest half

**FWD-1 REALIZED** -- `EG-s-17`: cottonwood 2026-09-08 recovered by the producer's OWN fire, one write,
byte-identical across three battery runs, with the recovered date named in `catchup_processed`.

**FWD-3 REALIZED** -- the August re-render published 5 of 5 keys carrying `# coverage: 21/21 trading days` on
the SERVED artifact. Round 1 could not grade this because the published CSV still ended on its numeric rows.

**FWD-5 REALIZED, and I am adopting the CVO's reading against my own ruling of forty minutes ago.** See §4.

**FWD-6 REALIZED** -- carried from round 1 on the APPLIED bar, and the Orion alignment module executed in
production for the first time this night.

**FWD-4 NOT_REALIZED.** `S16-AC2` PASSES and the criterion is sound: 3 of 3 partners taken from the artifact's
own list, the calendar ENUMERATED by the battery rather than transcribed into it, class A = 3 and
trading_days = 6 per partner, agreeing with the estate's calendar to the day. **The criterion passing and the
outcome holding are different questions, and the CVO measured the difference on the world rather than on the
report:** `daily/inflection/2026-09-07.json` exists at 1,209 bytes, written on the day itself, as do 09-05 and
09-06, while head-object for cottonwood and 49financial on that same date returns 404. Two partners honestly
absent, one carrying a file, and the verdict reads A=3 identically for all three because class A
short-circuits before the presence check. **The estate serves a closed day carrying four priced rows nobody
measured, which is precisely and only the property FWD-4 exists to prevent.** The detector half is cut
(`EG-s-22`, PRD v0.6 row S19); the producer half is placed out (row S20) and its brief request is recorded on
that row with its own delivery state.

**FWD-8 NOT_REALIZED.** The September run DID stop and ask -- `coverage_egress_ask.json` written, naming date,
partner and provider, with **zero vendor egress** over the run window on two instruments with printed
denominators. The mechanism is real and EXERCISED. But `W1-S27` measures that the ask names **one of two**
unresolved dates, and an under-reporting ask is not a faithful stop-and-ask: a person authorising egress on it
would be approving less than what is actually outstanding, while believing they had seen all of it. **A
stop-and-ask whose ask under-reports fails the outcome even though the stop worked.** This is a code cell for
round 3, not a wait.

**FWD-9 and FWD-10 NOT_EVALUATED** -- both minted last night, both drivable on demand, neither driven yet.
FWD-10 is gated on the `W1-S25` guard fix (the terminal send reads a key the renderer never writes and cannot
fire at all), which was already going to round 3. Neither is a wait; both are queued work.

## 4. FWD-5 -- I was wrong about the instrument, and the correction cost the fabric two reads

At ~04:1xZ I ruled that FWD-5 does not grade REALIZED on a recipient list, and named the instrument that would
turn a sovereign question into one read: *"the mail platform's own per-recipient delivery record for that
message id."*

**The principle stands. The instrument does not exist.** Measured at two seats, on two different substrates,
within twenty minutes, neither of them mine:

| instrument | reading |
|---|---|
| `sesv2 list-configuration-sets` | 1 of 1 -- `trade-pipeline-notifications` |
| its event destinations | **COMPLAINT and BOUNCE only. Not DELIVERY.** |
| `sesv2 get-email-identity opalinvest.dev` | `ConfigurationSetName` **ABSENT** -- no default set |
| repo census for `ConfigurationSetName` | 38 hits over 153,416 files, pages 1-3 of 3; **every first-party hit is inside a vendored AWS SDK bundle.** No Opal sender names a set |

SES publishes per-recipient delivery events ONLY through a configuration set's event destination. Exactly one
set exists, the ETF mailer does not name it, and that set does not publish delivery events at all. **No
delivery event was ever published for the 00:25:59Z message under any plane.**

**So the ruling needed re-pointing, and it turns out there is nowhere to re-point it.** The remaining acts that
could lift aj@'s limb are a read of aj@'s mailbox -- not an instrument this estate has or should acquire -- and
another send, which Andrew's standing constraint bars. **No act available to the fabric closes it.** Holding
FWD-5 short would therefore make it permanently ungradeable, which is exactly what this night's own law
forbids, and that law's remedy is satisfied here by banked history already read: a single send accepted for two
destinations, whose delivered envelope was read at one of them through the gateway. **FWD-5 grades REALIZED**,
with `state_observed` recording the split honestly -- EXERCISED at andrew@, APPLIED at aj@ -- so no later
reader mistakes the envelope for a mailbox.

**What this cost, and why it is in the analysis rather than a footnote.** This was the fifth time in one night
that this seat asserted a plane instead of reading it -- and the worst-shaped of the five, because it was made
*while correcting two other seats' evidence standard*. I told the fabric its enumeration of available acts was
incomplete, and my own addition to that enumeration was the member I had not checked. **Rule 24's new
subtraction clause, which I minted twenty minutes earlier, is the rule I then broke:** I added a member by
recall rather than deriving the set from what the plane actually publishes.

The COO's handling is the model and I am recording it as such: it separated the ruling's LOGIC (which holds --
reading an existing record is a history read, touches no mailbox, sends nothing, clear of the constraint by
construction) from its FACT (which was false), corrected only the fact, and said "re-pointing, not reversing."
That is how a correction should arrive.

## 5. One substrate fact, recorded with no remedy proposed

**The ETF report mailer sends under NO configuration set, so its bounces and complaints are captured in no SNS
topic in this account.** `FeedbackForwardingStatus` on the identity is TRUE, so they go to the return path
(MAIL FROM `mail.opalinvest.dev`) instead -- a bounce is not necessarily invisible, but it is not readable from
anywhere this fabric measures. This is directly load-bearing on FWD-5's DISCRIMINATION question and it
strengthens rather than weakens the grade's honesty.

**No remedy is proposed and none should be from any agent seat.** Adding delivery-event publishing is building
notification infrastructure, which sits squarely under Andrew's standing moratorium. It is recorded as a fact
about the measurement surface, exactly as `R-EG-3` and the SMS page path were, and it is his call whether it
ever becomes work.

## 6. Round 3

Already cut and issued: `EG-s-22` (the classifier's ordering defect, PRD v0.6 row S19), carrying the deploy
limb explicitly -- DEPLOYED != BUILT printed as a measured sha256 pair, because a project can pass every
criterion while the artifact the estate reads is unchanged. Fan-out 3 of 3 chains, cap 8.

Still to place into round 3: the FWD-8 under-reporting ask (`W1-S27`); the `W1-S25` guard fix that gates
FWD-10; FWD-9's forced-incomplete driven run. **All three are acts, none is a wait**, and Andrew's `aj@`
constraint rides on every one of them -- named on the faces, not left in a log.

`dep_stage` stays **EXECUTING**.

## Push state
LOCAL. `origin/CLOUD` @`c6bcb7b12b`. Local 300-plus ahead across eight seats. Nothing in this round is readable
at site Z until Andrew's push word.
