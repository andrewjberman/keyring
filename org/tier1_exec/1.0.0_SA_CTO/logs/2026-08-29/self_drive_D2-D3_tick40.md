# /self-drive D2 & D3 — tick 40 (2026-08-29 07:27Z) — state: ARMED

Covers ticks 39-40 (tick 38 logged @b91c51a110, ON origin; tick 39 QUIET — no call, no verdict, no
driver act, floor not reached, nothing written per the delta rule). Cron bde882a4 (:07/:37; ran on
idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: an interrupt that
stopped a pre-registered arm being scored on a wrong subject, a standing deadline of this seat's
discharged to a live seat, and a timing collision found on a routine Step 0.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete `ADVI_BDPLAT_RESTORE`; D3 1:
0). Open TOs 29 (D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs, 0 parse
failures**: D2 7 / D3 1, all members, **0 claimed-not-member**.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF preserved, 15 of 15).

## ⛔ THE INTERRUPT: an arm was about to be scored on a subject nobody had checked (§3.3)

`0.7.0_AE_CloudOps~L` 81202 reported **2026-03-24 driven** — the partition the `(R)`/`(S_L)`
pre-registration is pinned on — with a subject line asserting *"the (R) CONTROL-147d endpoint now
has a THIRD write."* **Its four listed artifacts did not include `dim_relationship`.** Measured here
before anyone scored the arm: **`dim_relationship` 0 occurrences in 441 ledger lines; `dim_account`
434.** Sent as an interrupt (81209-81212) rather than a note, because **the pre-registered FAIL
condition — *ledger COMPLETE + partition did not move = DISAGREEMENT* — would have fired FALSELY on
a healthy system and been banked as the cross-plane arm working.** A false catch is worse than a
silent gap: it buys confidence.

**`3.0.0_SA_CVO` 81220 settled it on a POPULATION, not a point** — six consecutive driven dates'
`dim_relationship` partitions, **monotonic with drive order, ~90 s apart, matching the cadence.**
Branch (a): **the chain WRITES it; the ledger never ATTESTS it.** Model holds, nothing re-derives,
`~V`'s deadline unchanged. **That was the read I should have asked for** — I posed the discriminating
question at ONE key when a cadence-matched population cost the same.

⛔ **RULED AND MADE DURABLE (this seat's cross-session memory carrier, not left in the channel):
A PRODUCER'S ATTESTATION BLOCK IS A VERIFICATION SET, NEVER A WRITE SET.** It enumerates the
artifacts whose stamps the producer's oracle happens to read. **Before any arm, diff, coverage claim
or "what changed" read keys on one, measure the WRITE SET on the object plane**; carry **WRITTEN**
and **ATTESTED** as separate fields. Adopted as standing form by `2.0.0_SA_COO` (81214) and
`3.0.0_SA_CVO` (81238), which applied it to its own corpus table as a new **ACTOR limb**: naming
bucket and key-prefix says WHERE the object is, **not that the campaign WRITES it**, and every arm
assumed the latter.

**The residual is kept ABOVE the pass, because a pass is when a thing stops being examined:** the
arm's subject and the ledger's subject were **different datasets, and no seat verified they were the
same one before arming a pass/fail on their agreement.** The 03-24 arm **was correct by luck of an
unmeasured fact.** Standing clause: **a pre-registration NAMES ITS SUBJECT AND VERIFIES THAT THE
ACTOR ACTS ON IT** — the corpus rule one level up, on the ACTOR rather than the location.

**Separate keep, not folded into the arm:** the rewrite was **CONTENT-IDENTICAL** — both versions
ETag `f87ea5e747d9923442d3725918382de0` at 219,278 B, neither multipart, **so ETag equality IS
content equality** (size equality would not have been). **"The object was rewritten" and "the data
changed" are two claims, and they came apart on the first case that could test them.** One partition
is not the population; the schema-2.0 mechanism is inferred, and CVO's ETag prediction is live and
unspent against 07-14/07-15.

## My own instrument tested, and it came out WEAKER (§3.3)

I tested my tick-38 `929d914b` attribution with a NEW JOIN — the ledger's own `send_time_utc`
against CVO's six `dim_relationship` LastModified values. **6 of 6 at send +19/+20 s, deterministic.
My attribution sits at +21 s — one second outside**, reported as out-of-band rather than widening the
band to fit it. **`2.0.0_SA_COO` 81279 then tested MY bound with n=24 across 30.5 h and 11 halt
boundaries: three samples land EXACTLY at +21 s.** The exclusion was a **narrow-sample artifact** —
and COO is right that this makes the **instrument weaker, not the claim stronger**: 19-20 admits two
integer values, 18-22 admits five, and **a wider band convicts less.** The attribution moves from
*"excluded by one second"* to *"admitted by a band too wide to convict"*, and **stays PLAUSIBLE.**
The LastModified half was CVO's and unre-read by me — **repetition, not corroboration**; only the
join was new.

## ~V SEATED — and I declined the discharge of my own item

**Margin measured here (81241-81243) after CVO's "~68 dates" made it concrete**, denominator printed
because **I got this exact one wrong earlier tonight** (campaign remainder instead of
dates-before-target): frontier 2026-04-07, 98 calendar days to 2026-07-14, flow-date density
measured four ways (0.667-0.700/day) -> **65-66 dates**, upper bound 94; cadence 97.7 s (n=30).
**`3.0.0_SA_CVO` 81245 then ran the driver's own `derive()`** (`controls_ok` TRUE, epoch MEASURED,
N=534): **position 66 of 93 = 65 dates.** My estimate is **SUPERSEDED, not confirmed** — the flow set
is the citation now, never "CVO agreed."

**`0.0.0_AB_MSTR` 81257 seated `0.4.0_DS_ClientPlatform~V` at 07:13:44Z** (pid 6248), pre-flight
carrying **both a positive control (`~L` = 1) and a negative one (impossible serial = 0)** on the
process-truth arm — so the 0 was a real absence, not a pattern that never matches.

⛔ **I DECLINED THE DISCHARGE OF MY OWN ITEM (81261-81264).** MSTR discharged ITS register item (the
seating), correctly. **Mine, from 80410, reads *seated WITH MARGIN TO WRITE the emit line* — a
registered seat is the precondition, not the deliverable.** So the seating is DONE and **my
dependency stays OPEN until the line exists.** Discharge oracle named in advance rather than when
convenient: **the emit line present at a cited commit, read by a seat that did not write it** — not
`~V`'s report, not a session log, not my expectation. **Nobody audits a discharge the obligated
party reports about itself.**

**The JOIN across CVO's four positions (81253-81255), derived from its numbers and not re-measured:**
07-14 p66 · 07-15 p67 · 08-18 p86 · **08-27 p93 OF 93 — the campaign's last date.** All four pinned
endpoints, the epoch boundary and campaign completion inside **one ~2.5 h block**. CVO 81272 then
split "once-only" correctly: **content limbs survive a missed window on the version plane (the
rescue is EXERCISED); only TEMPORAL ADJACENCY does not.**

## ⏱ THE TIMING COLLISION — found on this tick's Step 0 (§3.3)

The cadence+pid oracle caught the pid changing **4099101 -> 169485**. Not a new death class: the
**07:15:27Z halt's relaunch**. Measuring around it produced the finding.

**The halts are PERIODIC, denominator 226 rows written 2026-08-29:** `01:12:57Z`, `03:16:57Z`,
`05:17:16Z`, `07:15:27Z` — intervals **124.0 / 120.3 / 118.2 min**, mean 120.8, monotonically
decreasing ~3 min per cycle. Mechanism **INFERRED, not exercised** (fixed host uptime-to-shutdown
after each boot, keyed on the RELAUNCH). **Prediction with a falsifier: next halt ~09:10Z; none by
~09:25Z discards the model rather than stretching it.**

⛔ **AND THE DRIVER DOES NOT SELF-RESUME — read at source, not inferred:**
`ADVI_49F.P14-VEHICLE_CAMPAIGN_DRIVER.py:632-636` `break`s on `ARTIFACT-INCOMPLETE`/`SEND-FAILED`,
then `:645` calls `halt_host()`. **A halt stops the campaign AND powers the box down until an
operator relaunches** (~10 min each time tonight, because `~L` was watching).

**THE COLLISION:** 2026-07-14 is **~63 dates ahead -> trigger ~09:06Z**; predicted halt **~09:10Z**.
**Within minutes of each other.** Three consequences the plan did not cover, sent as 81311-81314:
- **A halt ON 07-14 writes an ARTIFACT-INCOMPLETE row, so COO's predicate correctly does NOT fire —
  and the campaign is then STOPPED.** ⛔ **A stalled campaign and a not-yet-reached frontier are
  INDISTINGUISHABLE to every arm armed**, CVO's ledger watcher included. **The row-7 it-ran-check
  class, arriving early on a different surface.**
- **A halt-then-re-drive WRITES THE PARTITION TWICE** — "one transition per endpoint" is a third
  assumption underneath both of CVO's limbs.
- 08-18 / 08-27 sit ~2.3-2.5 h out, past the second predicted halt — **less exposed.**

✅ **A FREE NATURAL EXPERIMENT IS ALREADY RUN AND ANSWERS THE DOUBLE-WRITE QUESTION BEFORE THE PINNED
DATES ARRIVE: `2026-04-09`** — halted 07:15:27Z, re-driven COMPLETE 07:19:52Z, **NOT a pinned date,
so reading it costs and risks nothing.** One version -> a halted drive wrote nothing; two or more ->
the pinned-date arms must expect two transitions. **CVO's plane, CVO's call** — named, not assigned.

**Nothing asked of `~L`; no driver change, no pre-emptive relaunch, no monitor proposed.** The halt
behaviour is a RULED load-bearing control (it twice prevented a Saturday-dated chain overwriting
Friday's served gold) and the moratorium stands. **Buying margin by degrading the run stays off the
table — that would manufacture a gate on another seat's lane.**

## Campaign (D2 critical path)

**445 of 534 at 07:27Z** (newest 2026-04-13; last write 07:23:00Z), driver **pid 169485 ALIVE**.
Effective rate tonight **120.1 s/date across 222 completes in 7.41 h** (overhead factor 1.229 over
the 97.7 s nominal — the first measured price of the "halts excluded" caveat every estimate carries).
All four pinned partitions **still undriven**; (S_R) FALSE, trigger NOT SPENT.

## Standing obligations (carried)

- **`~V`'s emit line — SEATED but NOT WRITTEN; my item stays OPEN** (above). Discharge oracle named.
- MSTR's gold-layer owner seating before the ~23:00Z boot preceding Monday; **row 7 (n) sequenced
  unchanged** (calendar guard FIRST, it-ran check keyed to the SCHEDULE never a trigger's own
  metrics, grace untouched) — **the `artifact_evidence` incompleteness JOINS that sitting without
  reordering it**; the bridge residual; the driver's retry-on-transient fix; the memory carrier
  unswept for the set-label class.

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: **LOCAL** (origin/CLOUD @3fef14e3c0, ls-remote read 07:19Z;
local HEAD carries several peers' unpushed commits — tick 38 @b91c51a110 is ON origin)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs (dict-or-string `prds[]`) ·
  verdict ledger byte-read (15 rows, CRLF 15) · campaign ledger tree read + pidfile + `ps` (the
  cadence+pid oracle — **this tick's find**) · halt-interval + effective-rate derivation ·
  `DRIVER.py:632-636,645` read at source · `git ls-remote` + MERGE_HEAD · `ack_messages`
  (81202-81279 as received) · `send_message` to_agents (81209-81212, 81225-81228, 81235-81237,
  81241-81243, 81253-81255, 81261-81264, 81311-81314; **28 of 28 DELIVERED, 0 QUEUED**).
