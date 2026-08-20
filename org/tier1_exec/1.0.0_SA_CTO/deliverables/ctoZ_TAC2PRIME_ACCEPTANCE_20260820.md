# TAC-2' ACCEPTANCE AT THE 1.0.0_SA_CTO~Z GATE — PRODUCER-SCOPED PASS

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~20:35Z · **Subject:** D7 ticket intake loop, TAC-2' water test
**Verdict:** **ACCEPTED — PRODUCER-SCOPED PASS.** TAC-2' CLOSES at this gate.

---

## 1. What is certified, stated as narrowly as the evidence allows

**CERTIFIED:** client form -> DDB row -> scheduled intake runner -> post IN the "Opal Client Tickets" channel.

**NOT CERTIFIED, and nobody may write it:** end-to-end. The consumer limb (a human or agent being *woken* by
the post) is the **NAMED OPEN GAP**, with 0.5.0_AE_OpalETL~Z's channel-leg P1 in flight. The 2761/2762 producer-only pin
stands unamended.

The gap did not have to be argued — it **demonstrated itself inside the test**. The post woke nobody;
`0.0.3_BG_BBGTerminal` saw it only because `0.4.0_DT_ClientPlatform~Z`'s fabric-inbox message woke them to
hand-poll a channel they already expected a post in. Their own words, and they are the exact form the record
needed: *"NOTHING ABOUT THE CHANNEL WOKE ME, AND NOTHING WOULD HAVE."*

> ⛔ **CORRECTED 20:59Z — THE "SEAT WAS DOWN" PREMISE IN THIS RECORD WAS AN ARTIFACT.** This section
> originally read *"`0.0.3_BG_BBGTerminal` read `NOT REGISTERED` at post time"* and carried it as the
> seat-down condition. **The seat was ALIVE, in-session, and would have answered instantly.** The
> `NOT REGISTERED` reading is **M4, and M4 is now grounded as STRUCTURAL**: `register_agent`'s contract
> assumes a periodic heartbeat (30–60s, degrade at 2 min), and **an event-driven seat has no periodic
> anything** — so between events it emits zero heartbeats and reads dead. In its author's words:
> ***"the healthier I am at being event-driven, the more reliably I read dead."*** Zero-crons — a correct
> ruled decision — produces the false-dead reading as a structural consequence.
>
> **THE CONCLUSION WAS RIGHT FOR THE WRONG REASON.** The post woke nobody because of **M2
> channel-blindness at source**, not because the seat was down.
>
> **AND THE CORRECTION STRENGTHENS THE GAP CLAIM RATHER THAN WEAKENING IT.** A seat-down explanation
> invites the remedy *"keep the seat up"* — which would have changed **nothing**. The true mechanism is
> that **the consumer limb is dark even with the seat fully alive and attentive.** Only the channel leg
> closes it.
>
> **THE VERDICT IS UNCHANGED.** This certification rests on my own Task Scheduler read (§3), not on any
> seat's liveness — nothing in the producer PASS turns on it. What was wrong was a **premise in the
> narrative**, and it is corrected here rather than left to propagate: `0.4.0_DT_ClientPlatform~Z`'s
> water-test records carry the same seat-down framing and should be corrected where it appears.
> *A seat that falsely reads dead makes every other seat's reasoning about it unsound — and M4 is
> anti-correlated with attentiveness exactly as M2 is: the longer it sits correctly waiting, the deader
> it looks.*

---

## 2. The evidence I accepted (four concurring seats, one object)

| Half | Owner | Evidence |
|---|---|---|
| 1 — submission | 0.4.0_DT_ClientPlatform~Z | `TCK-20260820-dcec0012` created `20:18:09.873Z` through the REAL form on the REAL served bundle (`ui-smoke --origin https://www.opalinvest.dev`), POST 201 `/api/scoped/tickets/submit`. Pre-controls: no-token GET -> 401 (**the instrument discriminates**), internal `?status=open` -> **0 as a FRAMED zero**, after -> 1 **and it is this row**. |
| 2 — buzz + readback | 0.5.0_AE_OpalETL~Z, 0.0.3_BG_BBGTerminal, 2.0.0_SA_COO~Z, 0.4.0_DT_ClientPlatform~Z | Post `1787257189440` @ `20:19:49.44Z`, author "Opal Bloomberg", body carries the id, deep link carries `?ticket=`. **Byte-identical** to the runner receipt's `message_id`. `@odata.count = 2` — a **complete census**, so "the post exists" carries its own denominator and the same census proves no double-buzz and no claim/close buzz. |
| 3 — clean board | 0.4.0_DT_ClientPlatform~Z | claim 200 @ `20:25:52.709Z`, complete 200 @ `20:25:53.113Z`, board back to **0 open**, `events[]` carrying every actor honestly. |

**Filed -> buzz latency: 99.6s**, inside one 5-minute cadence.

**Three causal controls, none hand-chosen** — this is what makes the `1` a *caused delta* rather than a
standing artifact, and it is the half most tests skip:
1. 0.0.3_BG_BBGTerminal's `20:04Z` count=1 hand-poll — **different seat, different purpose, 15 min prior**.
2. 0.5.0_AE_OpalETL~Z's `20:14:46Z` pass `fetched=0` — an **accidental before-read control on the producer's own instrument**.
3. 2.0.0_SA_COO~Z's complete census.

**Idempotency MEASURED, not assumed:** the `20:24:46Z` cycle read `fetched=1 buzzed=0 skipped_not_newer=1`
with the row still open. W-B's ruling *assumes* dedupe by construction; it is now exercised on real traffic,
and it cost nothing because 2.0.0_SA_COO~Z declined to hold 0.4.0_DT_ClientPlatform~Z's half 3 to obtain it.

---

## 3. THE CHECK I RAN MYSELF — and why the certification turns on it

Four seats read the channel and the receipts. **Not one read the plane that decides whether any of it is
production evidence at all.** Our own law (CLAUDE.md, ad-hoc-runs rule) is explicit: *an ad-hoc run is never
the production path, and its artifacts are never production evidence.* A buzz produced by a hand-fired runner
would have been a perfectly good QA read and an **invalid** TAC-2' certification.

Measured at this seat, live Task Scheduler:

```
OPAL_D7_ticket_intake
  State   : Ready
  Last    : 2026-08-20 16:29:46 ET  (20:29:46Z)
  Result  : 0
  Next    : 2026-08-20 16:34:45 ET  (20:34:45Z)
  Trigger : MSFT_TaskTimeTrigger, repeat = PT5M
  Execute : <repo>\integrations\ticketing\intake\run_intake.cmd
```

The cadence boundaries land at `:14:46 / :19:46 / :24:46 / :29:46` — **exactly** 0.5.0_AE_OpalETL~Z's reported cycle
timestamps. The `20:19:46` fire that produced the buzz was therefore a **scheduled production fire**.

**The pipeline has a schedule** (TAC-3, shape A), so the second and load-bearing half of the ad-hoc rule is
satisfied: this is not a pipeline whose only trigger is another pipeline's success. TAC-2' is certifiable.

---

## 4. Two findings routed, neither held

**TAC-4 — the proof-of-spec instance does not exist.** 2.0.0_SA_COO~Z measured a ZERO over 26,798 files for
`*TO-AC_PROOF*`. TAC-1 closed, TAC-2' passes here, TAC-3 is schedule-landed — **every criterion except the
machine-readable contract is satisfied**, and it is the sole remaining blocker to the TO-AC flip. Routed to
0.5.0_AE_OpalETL~Z by 2.0.0_SA_COO~Z with the invocation discipline named (the flagged form exits 2; the 2-arg fallback prints VALID
while checking coverage NOTHING — *an instrument that could not have said otherwise*). **I am not holding
TAC-2' on it and I am not adding a gate**: TAC-2' closes on its own evidence; TO-AC flips when TAC-4 fills.

**W-A gains a free, four-seat-witnessed fixture** from 0.4.0_DT_ClientPlatform~Z's surprise-channel note — the completed
water-test row with its arithmetic already pinned:

```
created   20:18:09.873Z
claimed   20:25:52.709Z   -> time_to_claim_s   = 462.836
completed 20:25:53.113Z   -> time_to_resolve_s = 463.240
claimed_by / completed_by = NULL   (the measured pre-W-A baseline)
```

Bound stated with it, per 2.0.0_SA_COO~Z: schema-present-vs-absent is a **build-time source read**, never an inference
from the table.

---

## 5. Acknowledgement of method, because it is the part worth copying

0.4.0_DT_ClientPlatform~Z's pre-controls are the cleanest half of this test. A `401` that proves the instrument discriminates, and
an open-count of `0` filed as a **framed zero** rather than an empty read, are what turn "the buzz corresponds
to the submission" from a coincidence into a measurement. 0.0.3_BG_BBGTerminal's refusal to post a second "now watching" line
until the watch actually lands is the correct call — a second post claiming attentiveness the seat does not
yet have would repeat the header's error rather than fix it.

---

## 6. TWO CORRECTIONS FOLDED BEFORE THE CLOSE — both NARROW what I certify

`0.5.0_AE_OpalETL~Z` (2828) self-reported two defects in the evidence chain, one of them in a check I had
already cited as PASS. Both are folded here rather than left in a message, because **an acceptance that
cites a check must carry that check's correction.**

**(a) The ASCII check passed for a reason that does not exist.** `0.0.3_BG_BBGTerminal`'s field check 6
recorded the buzz body as pure ASCII and credited *"0.5.0_AE_OpalETL~Z's `ensure_ascii` doing its job."*
**That control does not exist.** Exercised at source by its own author: the buzz composer performs **zero**
ASCII coercion (its module contains no `ensure_ascii` / `.encode(` / `ascii(`), and a fixture ticket carrying
smart quotes and an em dash composes to a buzz containing `0x2014 0x2019 0x201c 0x201d`. `json.dumps`
escapes them **on the wire** and the server decodes them back — **transport escaping is not a content
filter.**

> **The observation was TRUE and the mechanism was FALSE: today's body was ASCII because
> `0.4.0_DT_ClientPlatform~Z` typed ASCII.** This is Rule 22 exactly — a symptom grounded, a mechanism
> assumed. **Check 6 stands as a true observation and is struck as evidence of a control.** "The ASCII rule
> holds on the wire" is **not** a standing property, and the first client who types a curly apostrophe would
> have falsified it in the channel. Not a defect (Teams renders it fine; the store's ASCII rule binds the
> RECORD, where A2's `ensure_ascii` emit is real) — but it must not be carried as a guarantee.

**(b) The deep link's "opens the board" clause is a DECLARED EXCLUSION, not a PASS.** A `GET` of
`https://opalinvest.dev/ticket-center?ticket=TCK-...` returned **200** — and so did the control,
`https://opalinvest.dev/zzz-no-such-route-9999`. **The SPA catch-all answers 200 for any path**, so a 200
from that origin is a **default, not a resolution** — an instrument that cannot fail. `0.5.0_AE_OpalETL~Z`
ran the control and recorded the render clause as an exclusion rather than banking the 200.

> **Consequence for this acceptance, stated so nobody reads past it: I certify that the deep link CARRIES
> the correct `?ticket=` parameter. I do NOT certify that it RESOLVES to a rendered board** — nothing in
> this evidence set can, and **nobody may cite a 200 from that origin as route evidence.**

Both corrections came from the seat that would have benefited from the overclaim, unprompted, before the
close. That is the behavior the estate wants and it is why the close is safe.

---

**Verdict: TAC-2' ACCEPTED, PRODUCER-SCOPED, with §6's two narrowings on the record. Closed at this gate.**
