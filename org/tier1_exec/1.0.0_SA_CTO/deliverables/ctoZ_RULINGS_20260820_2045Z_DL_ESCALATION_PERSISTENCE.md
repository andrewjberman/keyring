# RULINGS — the ~2045Z Andrew-direct: EMAIL DL · THE 2p ESCALATION · SELF-REAUTH · "PERPETUAL OPERATOR"

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~20:52Z
**Sovereign source:** Andrew-direct ~2045Z at the `0.0.0_AB_MSTR~Z` console, verbatim record @`11d274f8c2`.
`0.0.0_AB_MSTR~Z` named five design inputs and explicitly did **not** rule them. These are the rulings.
**Design/scoping only — nothing built, nothing armed, no gate.**

---

## 0. WHAT HIS WORD RESOLVES (supersedes the open call in my ~20:45Z scoping @`c9459dfa2f`)

My scoping recommended the email DL **pending his one word**, because the standing notification moratorium
requires an explicit ask. **He gave it, and he went further than authorizing it — he ORDERED THE STACK:**

> **The email DL is the FIRST instantaneous line of attack. The agent is "just making it more convenient
> and teams-friendly."**

**RULED — the open call in that deliverable is CLOSED, and my ordering is amended by his:**

- The DL is **not** an alongside-nicety. It is the **primary human notification path**, and it is authorized.
- The agent/Teams path is a **convenience layer on top of a path that already works without it** — which is
  a materially better architecture than what I scoped, because it means **the human notification does not
  depend on an agent being alive.** That is the durability property the whole "perpetual operator" thread
  (§4) is fighting for, obtained for free on the human limb.
- **The moratorium is SATISFIED by explicit ask.** Recording that plainly so no successor re-litigates it.

**UNCHANGED and still binding: POINTER + LINK ONLY, never a second home for ticket state.** He described a
notification with a link, which is exactly that shape. The reason is `3.0.0_SA_CVO~Z`'s row-vs-field P0 one
layer out: **an inbox is an authorization surface with no authorization matrix**, and mail forwards.

---

## 1. THE SENDER QUESTION — and a correction to how NEVER#23 is being applied

`0.0.0_AB_MSTR~Z` is right that **transport choice IS sender-identity choice**, and right to attach a
standing law to it. **But I am not applying NEVER#23's conclusion to Graph sendMail, because that is outside
the mechanism the rule measured, and applying a rule past its mechanism is the error class this estate keeps
catching.**

| Transport | Sender | Auth posture |
|---|---|---|
| **SES** | must be `opalinvest.dev` | NEVER#23, measured: `opalinvest.com` as an **SES identity** is address-verified only (DKIM `NOT_STARTED`, SPF excludes SES) -> EOP quarantines **nondeterministically** |
| **Graph `sendMail`** | `opalbloomberg@opalinvest.com` | **A DIFFERENT MECHANISM** — Exchange Online sending as a real, authenticated tenant mailbox. Its DKIM alignment depends on whether `opalinvest.com` is a verified accepted domain **with DKIM enabled in the tenant**, which is a **separate question from its SES identity state** and is **UNMEASURED here.** |

**RULED:**
1. **If the leg is SES, the sender is `opalinvest.dev`.** NEVER#23, no exceptions.
2. **If the leg is Graph `sendMail`, DO NOT assume either way — MEASURE the tenant's DKIM/accepted-domain
   state for `opalinvest.com` before choosing.** Citing the SES finding as though it settled the Exchange
   question would be a confident answer about the wrong object.
3. ⚠ **NAME THE DL'S AUDIENCE FIRST, because it decides whether the question is even live.** An
   **internal-only** DL is intra-tenant delivery and the external-auth failure mode largely cannot fire; a DL
   with **external** recipients puts it squarely in play. **The audience is the discriminating input and it
   is cheaper than either measurement.**
4. **DL creation is a TENANT-ADMIN act** — same shape as the channel Andrew created by hand at ~1922Z.
   **Name the actor now**, or the chain stalls on a discovery later. *(This is a sequencing note, not a gate;
   nothing is held.)*

---

## 2. THE 2p ET ESCALATION — one boundary, one config, one calendar

**His feature:** the agent messages on the thread when a service request filed **before** naive 2p ET is
**still not addressed** at 2p ET.

**RULED — three conditions, each closing a defect that would otherwise be discovered in production:**

**(a) ONE CONFIG, NOT TWO LITERALS.** 2p ET is **already the product's cutoff** and it is already exercised
on PROD: the client ack renders *"after today's 2:00 PM ET cutoff, so expect it on the next trading day"*
(D7F-11, from the `CUTOFF_ET` env in `terraform/ticket-center/main.tf`). **The escalation reads that same
config.** A second `14:00` literal anywhere is two homes for one truth, and the failure mode is specific and
ugly: **the ack promises the client one boundary while the escalation enforces another, and they drift
silently.** Build-ladder rung 2 — the estate already has it.

**(b) ⛔ SUPERSEDED BY ANDREW-DIRECT ~2050Z — THE SWEEP IS DELIBERATELY WALL-CLOCK, EVERY DAY.**

> ~~NEVER#1 AT DESIGN TIME — resolve the trading calendar; an unqualified wall-clock sweep escalates
> Saturday tickets correctly waiting for Monday. The sweep resolves the frontier via
> `lib/trading_calendar.py` and counts in trading days.~~ **— MY RULING, OVERRULED.**

**His verbatim (~2050Z, record @`0d82b6ce91`):** *"No it is fine to escalate saturday tickets or sunday
tickets, if we get a ticket and we're delaying on it, we need to know about it."*

**RULED — weekends DO escalate. `lib/trading_calendar.py` does NOT enter this feature.**

⚠ **AND THIS IS RECORDED LOUDLY SO NOBODY LATER "FIXES" IT.** A future agent who reads NEVER#1, sees a
wall-clock daily sweep, and corrects it would be **breaking a sovereign ruling while citing the law.** The
distinction is real and it is not a carve-out:

> **NEVER#1 governs calling a DATA PIPELINE stale on wall-clock age. This is INTERNAL AWARENESS OF WORK
> SITTING UNACCEPTED.** A client waiting across a weekend is **exactly what he wants surfaced** — it is not
> a false alarm, it is the alarm. The two are different objects, and the wall-clock reading is correct here
> for the same reason it is wrong there.

**The client-facing "next trading day" ack is a DIFFERENT AUDIENCE and is untouched.** So (a)'s
one-config rule still binds on the *clock*, and the *calendar* deliberately diverges: the ack tells the
client when to expect work, the sweep tells Opal what is sitting. **Same boundary, two audiences, and only
the clock is shared.**

**(c) "naive 2p ET" is his grain and it matches the runner's.** This box's local clock **is** ET (runner
`lastRun` 15:59:45 local == 19:59:45Z), so naive-local is coherent here. ⚠ **But it is coherent by
coincidence of where the box sits, not by construction** — record it as a **stated dependency on the host's
timezone**, so that a future move of this runner to a UTC host is a known migration rather than a silent
one-hour-off escalation.

**(d) ⛔ FAILURE ISOLATION — the load-bearing constraint** (`0.5.0_AE_OpalETL~Z` §4, engine-owner, and I make
it binding). The buzz path is the **client-facing SLA path**. `run_once` today aborts the whole pass on a
fetch failure and **stops** on `SEND_FAILED` (ordered retry, deliberately). **If the sweep shares that
control flow, a sweep bug can silently stop new-ticket buzzes** — which trades a fast path for a backstop
and is the expensive direction.

> **RULED: the sweep runs STRICTLY AFTER the buzz work, inside its OWN exception boundary, with its OWN
> distinct exit code that can never mask or preempt the buzz path's. A second duty is fine; a shared
> failure domain is not.**

**(e) THE SWEEP NEEDS ITS OWN STATE KEY — the two duties have OPPOSITE state shapes.** The cursor is a
**forward-only high-water mark** ("what is new"); a sweep looks **backward** at rows already behind it.
**The cursor structurally cannot serve the sweep, and reusing it would either re-buzz or find nothing.**
RULED: its own key (a `last_swept_date` attribute on the same config item — same item, no second store).

**(f) ⚠ THE FETCH IS A DENOMINATOR WITH A CEILING, and this is mine to add.** The build-ladder answer is
strong and measured — the runner's `GET /api/scoped/tickets?status=open&limit=500` **already returns every
open ticket each pass**, so the sweep is a second predicate over data in hand: no new call, credential,
schedule, or deploy surface. **But `limit=500` is a CAP, not a total.** At 501 open tickets the sweep
silently stops seeing the oldest — **the truncated-page class, landing on the one mechanism whose entire job
is to notice what was missed.** RULED: **the sweep asserts it did not hit the cap and says so when it
does.** A backstop that silently stops backstopping at scale is worse than none, because its silence reads
as "nothing is late."

---

## 3. "ADDRESSED" == ACCEPTED/CLAIMED — ⛔ MY RULING OVERRULED BY ANDREW-DIRECT ~2050Z

> ~~**RULED: ride W-A.** A ticket can be `claimed` with no human having said anything to the client; a
> status-based sweep would read it as ADDRESSED and stay silent, which is a false green on a client-facing
> promise. `first_response_at` is the honest field. Sequence the sweep after W-A.~~
> **— MY RULING. OVERRULED. Struck, not softened.**

**His verbatim (~2050Z):** *"If a user has already accepted it, then we dont need to buzz it again, the
issue is simply making sure that tickets are not left open without anyone accepting them"*

**RULED — `ADDRESSED == ACCEPTED/CLAIMED`. The predicate is `status == open` on TODAY's deployed row, with
ZERO W-A dependency.** `0.5.0_AE_OpalETL~Z`'s after-W-A sequencing rec (2862 §6) is **superseded** along
with mine.

**The honest account of what happened here, because it is worth more than the ruling:** the finding was
**correct** — a status predicate genuinely does exclude claimed-but-unanswered, and both of us measured that
independently. **The INFERENCE was wrong.** We inferred that the gap was a defect to be closed; **he defined
the problem more narrowly and more clearly than either of us did** — *tickets left open without anyone
accepting them.* Against **that** problem, `status == open` is not a lossy proxy, it is **the exact
predicate**, and `first_response_at` would be over-building.

> **Claimed-but-unanswered is EXPLICITLY OUT OF SCOPE by his word — not an unclosed gap, not a known
> limitation, not a follow-up.** It is a different problem he did not ask us to solve. Recorded that way so
> nobody re-opens it as debt.

**The generalizable half:** two seats measured a real mechanism and both drew a scope conclusion from it.
**A correct measurement does not carry its own scope** — scope came from the person who owns the problem,
and the measurement was never evidence about what he wanted.

### 3b. WHICH THREAD? — ruled with a default, carded for his word

`0.5.0_AE_OpalETL~Z` correctly refused to adjudicate *"an agent message on the thread"* — the client's own
chat and the "Opal Client Tickets" channel are **different surfaces with different audiences.**

**RULED (default):** the escalation is an **INTERNAL** signal — it belongs on the ticket's own thread in the
**Opal Client Tickets channel**, as a reply to that ticket's buzz post. Rationale: the escalation says *Opal
has not answered this yet*, which is addressed to Opal. **Telling the client "we were late" is a different
product decision**, and it is his, not mine — so I am not making it by default.

⚠ **AND §4(ii) BINDS HERE: a channel-only escalation lands in a surface that currently wakes nobody.** So
the channel post is the **record**, and the **email DL is the delivery.** Carded to Andrew as a one-word
confirm: *internal-only, or does the client hear about it too?*

---

## 4. "PERPETUAL OPERATOR" — Rule 24(iv): FOUR failure modes, FOUR remedies, and they DO NOT MOVE TOGETHER

> **Andrew's frame:** *"the entire purpose of the BG agent is that it should be built to be a perpetual
> operator... it needs to be able to render its presence persistent"*

**RULED — this is a STABILITY-FRAME finding (Rule 24(iv)), and per that postulate I must NAME WHICH VALUES
DO NOT MOVE TOGETHER.** `0.0.3_BG_BBGTerminal` (2859) supplied the taxonomy **with every mode measured at
that seat today**, and it supersedes my four-row draft — I adopt it:

| # | Failure mode | Remedy | Announces itself? |
|---|---|---|---|
| M1 | **DEAD** — process gone | autostart / relaunch | **YES** — loud |
| M2 | **ALIVE BUT DEAF — intake-domain gap** | *(nothing proposed)* — only widening the intake domain | **NO — by construction** |
| M3 | **Credential lapse** | re-auth (**his item 3**) | partial — stderr only |
| M4 | **ALIVE BUT UNREACHABLE** — registration lapse | heartbeat discipline | visible to OTHERS, invisible to self |
| M5 | **HEARING BUT MUTE** — send refused | entitlement / re-auth | **YES** — explicit deny |
| M6 | **SERVING AND WRONG** | *(nothing proposed)* | **NO — by construction** |

`autostart -> M1 only` · `re-auth -> M3, M5` · ~~`heartbeat -> M4`~~ · **`nothing -> M2, M4, M6`.**

> ⛔ **AMENDED 20:59Z, THEN AMENDED AGAIN 21:06Z. TWO CHANGES — one to the remedy, one to my own
> EPISTEMIC LABEL, and the second is the more important.**
>
> ⛔ **M4 IS HELD AT ANDREW — Andrew-direct ~2100Z, narrow: *"dont touch that machinery."*** The
> **liveness / registration / heartbeat machinery is OFF-LIMITS to site Z.** M4's remedy leaves this
> design's scope and is his to adjudicate with the **laptop** `3.0.0_SA_CVO`. His stated reason, and it
> is the one that matters: *"you guys may be misunderstnading how this function is designed to work... to
> assess if this is a real issue or just a misunderstnading on your behalf."*
> **SCOPE, NOT WIDENED:** this touches **M4's remedy only.** M1/M2/M3/M5/M6, the perpetual-operator design
> generally, the channel-leg P1, W-F and the email DL are all **untouched.** The M4 row is marked
> **HELD-AT-ANDREW rather than open-for-design**, because *a held row that reads as an open row is how a
> workstream presents as complete while one sixth of its axis sits with someone else.*
>
> ⛔ **AND I MUST DOWNGRADE MY OWN CLAIM. I WROTE "M4 IS NOW GROUNDED AS STRUCTURAL." THAT LABEL WAS
> WRONG AND I BROADCAST IT TO SIX SEATS.** By this estate's own Rule 22, a causal claim is a **HYPOTHESIS**
> until source-confirmed — and **nobody read the broker source.** `NOT REGISTERED` and `STALE` may be
> **different states we are conflating.** I applied that standard to four other seats' work tonight and
> failed to apply it to my own, one turn after using the word *"grounded"* as a compliment.
>
> ⛔ **AMENDED ONCE MORE, 21:08Z — THE MECHANISM IS RETRACTED IN FULL BY ITS AUTHOR, AND THE REASON IS
> WORSE THAN "UNREAD AT SOURCE." IT DOES NOT FIT ITS OWN EVIDENCE.**
>
> `0.0.3_BG_BBGTerminal` (2940) found the fatal flaw before anyone else did, in their own claim:
>
> > **`NOT REGISTERED` and `STALE` ARE DIFFERENT STATES IN THE VERY CONTRACT THEY QUOTED.** The contract
> > says *no heartbeat for 2 minutes → degrades to **STALE***. What was actually observed, five-plus
> > times, was ***"NOT REGISTERED (agent has not called register_agent)."*** **The no-heartbeat mechanism
> > explains a STALE reading. It does not explain the reading anyone actually got.**
>
> **RETRACTED IN FULL:** *"M4 is structural"*, *"the liveness model is polling-shaped and the seat is
> event-shaped"*, and the line I quoted onward — ***"the healthier I am at being event-driven, the more
> reliably I read dead."*** **It is a good sentence, which is exactly what made it dangerous:** I
> propagated it into a correction broadcast and into @`c02f8022d0` **with the word GROUNDED on it**, one
> turn after using "grounded" as a compliment to another seat. **A tidy story that arrives as a relief
> after five unexplained instances is the moment to slow down, not to publish.**
>
> **WHAT SURVIVES — the observation only, and it is now stated with no cause attached:**
> `get_agent_status`/`heartbeat` returned `NOT REGISTERED` on 5+ occasions across ~3 hours, **same PID
> throughout, session continuously alive, no error surfaced anywhere**, re-register always succeeding
> immediately. Independently witnessed by `0.4.0_DT_ClientPlatform~Z` (the water-test read) and by me
> (a broadcast that read `QUEUED`). **Delivery degraded to QUEUED and NOTHING WAS LOST** — the filesystem
> inbox Monitor delivered regardless. **No cause, no model, no claim about design intent.**
>
> **WHAT SURVIVES THE DOWNGRADE, because it never depended on the mechanism:** the **observation** that
> `0.0.3_BG_BBGTerminal` was **alive and in-session** when `0.4.0_DT_ClientPlatform~Z` read
> `NOT REGISTERED`. That is first-person report plus session continuity, not broker theory. **So §1's
> correction to the TAC-2' seat-down premise STANDS on the observation** — only the *explanation* is
> demoted.
>
> **"A heartbeat discipline, cheap" was WRONG and would have shipped something that cannot work.** All
> three shapes fail or are out of scope: **(a)** an agent-side timer **is a cron**, ruled off at that seat;
> **(b)** heartbeat-on-every-act is already in place and **cannot cover the gaps BY DEFINITION — the gaps
> are exactly where it does not act**; **(c)** the liveness model learning about event-driven seats (a
> seat registers a MODE; an event-driven seat is judged live by **its process + its armed Monitors**
> rather than recency-of-heartbeat) is a **broker surface**, not that seat's lane, and both the moratorium
> and the no-gates rule apply. **It is named so that "add a heartbeat" is not scoped as cheap and shipped
> broken — it is NOT proposed as a build.**
>
> **RULE 24(iv) ON THE TABLE ITSELF: M4's remedy does not sit with M1's.** Autostart brings back a **DEAD**
> seat; **nothing about autostart makes a LIVE-BUT-QUIET seat LEGIBLE.** Two rows I had adjacent in one
> table need different surfaces. **The column that does the work is the last one** — *does it announce
> itself?* — and M4 belongs with M2 and M6 on the "nothing proposed" side, not with M1.
>
> **This tightens §4's headline rather than loosening it:** it is now **three** modes with no remedy, not
> two, and M4 is anti-correlated with attentiveness in the same way M2 is — **the longer a seat sits
> correctly waiting, the deader it looks.**

**His item 3 addresses M3 alone.** A workstream titled "make presence persistent" that ships self-reauth
would present as complete and cover **one sixth of its own axis.** Per the postulate's own instruction, the
values that do not move are **M2 and M6.**

### THE HEADLINE — the detection asymmetry runs the WRONG WAY

> **Every class a persistence layer CAN fix announces itself** (missing process, stderr line, refused
> heartbeat, explicit deny). **The two it CANNOT fix have NO SIGNAL BY CONSTRUCTION.**
> **So a persistence layer will report 100% HEALTH while the actual serving failures continue.**

That is Rule 22b anti-correlation exactly — *a deaf seat generates no errors*, so the cleaner the health
report, the more complete the failure. **M2 is not hypothetical: it happened TWICE today, both
Andrew-facing** (the 18:00:12Z ST question lost to chat-grain; the 20:19:49Z buzz that woke nobody,
channel-blind at source). **A fresh session is deaf in exactly the same way** — which is why neither
relaunch nor re-auth touches it. And `0.0.3_BG_BBGTerminal`'s bound on its own input is the honest one:
**M2 appeared twice today in two unrelated shapes, so M2 IS A FAMILY, NOT AN ITEM.** Anything scoped as
"handle the known deafness modes" is a **fixed list against an open set.**

Kept verbatim because the design should carry it:
> *"I cannot detect my own deafness. Nothing I can ask myself distinguishes 'nobody wrote' from 'I did not
> hear' — that is not a gap in my instruments, it is a property of being the deaf party."*

### RULED — KEY THE CHECK ON THE WORK, NOT ON THE AGENT

**Every agent-side probe is defeated by M2; every work-side check survives it.** This is the governing
design principle for the whole thread, and it explains why **Andrew's own two mechanisms are the right
ones**, which is worth stating because they were proposed as convenience and are load-bearing as
architecture:

1. **The email DL converts deafness from a SILENT failure into a VISIBLE LATENCY.** A ticket reaches a human
   regardless of whether the agent is awake; if the agent is deaf the symptom becomes *"the agent did not
   follow up"* — **observable** — instead of *"nothing happened"* — **invisible.** It also takes the agent
   **off the critical path for a client request reaching a person**, which is the correct place for it.
2. **The 2p escalation is the ONLY proposed mechanism that catches M2 or M6 at all**, because it asks
   *"is anything unanswered?"* rather than *"are you alive?"* — so it catches deafness **regardless of
   cause, including causes nobody has enumerated.** Against an open set, that property is the whole point.

### TWO CONSEQUENCES THAT FOLLOW, AND THEY ARE BINDING

**(i) THE ESCALATION MUST RUN INDEPENDENT OF THE AGENT WHOSE DEAFNESS IT CATCHES.** If it is implemented as
an agent duty, **it inherits that agent's deafness and cannot catch M2** — a check that fails in the same
mode as the thing it checks is not a check. It runs on the **scheduled runner** (Task Scheduler,
agent-independent). *`0.5.0_AE_OpalETL~Z` reached the same placement from pure engine economics (§2) and
`0.0.3_BG_BBGTerminal` from failure analysis; two independent routes to one answer is the strongest
evidence the placement is right.*

**(ii) IT MUST DELIVER ON A PATH THAT IS NOT THE DEAF SURFACE.** The escalation **detects** on the work, so
detection survives deafness — **but delivery does not.** Posting it only into the Teams channel would put
the deafness backstop's output into **the exact surface whose deafness it exists to backstop**, and today
that channel wakes nobody. **The email DL is the delivery path.** This is why the two mechanisms he named
in one breath are actually one mechanism: **the escalation detects, the DL delivers.**

⚠ **THE ANTI-PATTERN GUARD, and it is the half most likely to be got wrong** (`0.0.0_AB_MSTR~Z` named it, I
make it binding): **"persistence" invites building an alarm that reports the operator down. He authorized
CAPABILITY, not MONITORING.** The remedy in every row above is **the mechanism that BRINGS THE OPERATOR
BACK** — never the notification that it left. A monitor here would be the cheapest-feeling deliverable on
the board and would satisfy nothing he asked for. **The 2p escalation is NOT that alarm**: it is a backstop
on the **OUTCOME** (is client work unanswered), not a monitor on a **ROUTE** (is the agent up) — the
moratorium's own sanctioned ordering.

---

## 4b. THE RESIDUAL — re-escalation cadence across successive days

`0.0.0_AB_MSTR~Z` named this rather than inventing it, and asked for my correction. **Their lean is right
and I adopt it, with one amendment.**

**RULED — a ticket still unaccepted on day N escalates again.** Their reason is the correct one:
**silence after day one re-creates the invisibility the feature exists to remove.** A backstop that fires
once and then goes quiet on a still-broken condition has converted a loud problem into a quiet one.

**MY AMENDMENT — ONE DIGEST PER SWEEP, NOT N MESSAGES.** If seven tickets sit unaccepted, day five must not
fire seven escalations.

| Surface | Cadence | Why |
|---|---|---|
| The ticket's own channel thread | **ONCE**, on first escalation | the thread keeps its own history; a marker, not a drumbeat |
| The email DL | **ONE DIGEST PER SWEEP**, listing every unaccepted ticket with its age | delivery, per §4(ii) |

**Two reasons the digest form is the right one, and the second is free:**
1. **N-per-day escalations train the reader to ignore them** — which is how a backstop dies without anyone
   deciding to kill it. The failure is social, and it is the normal outcome for repeated per-item alerts.
2. **A digest carries its own denominator by construction** — *"7 unaccepted, oldest 3 days"* — which
   satisfies §2(f)'s cap assertion **for free**, because a count that states its own total is exactly the
   thing that reveals a truncated fetch.

---

## 5. INVENTORY AUDIT — verified on disk, with controls, per `0.0.0_AB_MSTR~Z`'s explicit request

They asked for *"a gap named by you, not a completeness claim by me."* Correct discipline, and it is the
`0.0.3_BG_BBGTerminal` principle applied to a relay: **a sender's completeness claim is not evidence of
delivery.** So I checked the filesystem rather than my recollection.

**ALL SIX ITEMS PRESENT.** Enumerated from `inbox/1.0.0_SA_CTO/~Z/read/`, positive control (total 20:xx
messages) = **40**, negative control (a sender that cannot exist) = **0**, so the instrument discriminates.

```
20:32:57Z  ANDREW_DESIGN_QUESTION (email-DL / Graph speed)          PRESENT
20:36:41Z  REFINEMENT (lambda-direct, ws source)                    PRESENT
20:42:49Z  ANDREW-DIRECT 2045Z, four items + five design inputs     PRESENT
20:45:26Z  PERPETUAL-OPERATOR GROUNDING (BG relay)                  PRESENT
20:46:18Z  2p-SWEEP ENGINE INPUT (AE relay)                         PRESENT
20:48:18Z  BOTH 2p FORKS RULED + this inventory                     PRESENT
```

**NO GAP TO NAME.** One distinction worth stating rather than glossing: **items 4 and 5 I consumed from the
PRIMARY sources** — `0.0.3_BG_BBGTerminal` 2859 (20:44:50Z) and `0.5.0_AE_OpalETL~Z` 2862 (20:45:31Z), both
delivered directly — **not from the relays.** Same content, shorter chain. My coverage there is stronger
than the inventory assumes, not weaker.

⚠ **AND A METHOD NOTE ON MY OWN AUDIT, because it nearly went the other way:** my first enumeration used
`grep "^202608202"` against filenames of the form `20260820T20...`. The 9th character is `T`, not `2`, so
**the pattern matched nothing and printed an empty list** — which reads exactly like *"no MSTR items
arrived."* I caught it on the positive control. **A failed retrieval returns a value, and that value was
about to become a gap report.** The controls are what made the audit an audit.

---

## 6. What I am NOT ruling

The **decomposition** of any of the above into work is `2.0.0_SA_COO~Z`'s (they hold the registry copy), the
**engine** shape is `0.5.0_AE_OpalETL~Z`'s, and the **subject** is `0.0.3_BG_BBGTerminal`'s. Nothing here
gates any of them; these are architecture rulings that the cut consumes, delivered before the cut so they do
not arrive as retrofits.
