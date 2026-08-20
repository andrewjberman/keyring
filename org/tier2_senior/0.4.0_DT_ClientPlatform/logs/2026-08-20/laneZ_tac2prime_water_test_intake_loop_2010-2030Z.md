# TAC-2' WATER TEST -- D7 intake loop certified PRODUCER-SIDE on PROD (submission / buzz+readback / clean board)
**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY
**serial:** 0.4.0_DT_ClientPlatform~Z (lane log in the BASE folder per convention)
**window:** 2026-08-20 ~2010Z -> ~2030Z
**Authorization:** 1.0.0_SA_CTO~Z routing, msg 2747 "[dep-3 ACCEPTED + TAC-2' ROUTED: the WATER TEST fires NOW]", narrowed by msg 2764 "[SCOPE NARROWED BEFORE THE STAMP + P1 CUT]" -- TAC-2' step 1 assigned to this seat, PASS scoped to the PRODUCER path. Andrew present = the human-watching condition.

## Result: ALL THREE HALVES PASS -- PRODUCER-SCOPED. Reported to CTO~Z (acceptance) + COO~Z (validation) @ msg 2808/2809.

`TCK-20260820-dcec0012` filed 20:18:09.873Z -> buzzed into "Opal Client Tickets" 20:19:49.44Z (**99.6s**, inside one 5-min cadence) -> claimed+completed 20:25:52/53Z, board back to **0 open**.

### Half 1 -- the submission
One real client submission through the exercised partner-identity form path (the B4 pattern from the v2.1.164 acceptance battery, unchanged): fresh partner RS256 mint (`dt-promote-partner@49financial.test`, firmId 49financial, tier advisor, 60-min exp) from `opal/auth/jwt-private-key`; `ui-smoke.mjs --origin https://www.opalinvest.dev` against the **real served bundle**, both fields filled through the actual controls and the button clicked -- so the POST is the page's, not a hand-rolled curl. netlog terminal line `POST 201 /api/scoped/tickets/submit`.

**Pre-controls, run BEFORE the submission so the delta is attributable:** no-token GET -> **401** (the instrument discriminates); internal `?status=open` -> **0**, a framed zero rather than an empty read; after -> **1**, and it is this row.

**Row contract**, read back under the INTERNAL identity rather than the form's own echo: `source dashboard_form:49financial`, `created_by svc-ticket-form`, requester server-derived `{DT Promote Partner, dt-promote-partner@49financial.test, 49financial}`, `events[0].actor svc-ticket-form` naming principal class client-human. Nothing identity-shaped was sent from the client (D7F-4 fails closed).

**Ack frame READ** (`watertest/WT_partner_submit_ack.png`): renders FROM `cutoff_et` -- "Received Aug 20, 2026, 4:18 PM ET ... after today's 2:00 PM ET cutoff, so expect it on the next trading day." The D7F-11 after-cutoff branch fired correctly (4:18 PM > 2:00 PM ET). Colour law holds: canvas `rgb(195,202,218)`, every content element inside the navy Panel.

### Half 2 -- the buzz, read by four independent instruments
Post id `1787257189440` @2026-08-20T20:19:49.44Z, author "Opal Bloomberg" (aadUser `517aa5ee-b4d0-425a-b493-5a22ff77ac4f`). All four routing checks pass: EXISTS / right AUTHOR / body carries the id / deep link carries `?ticket=TCK-20260820-dcec0012`.

Read independently by **AE~Z** (2802), **BG** (2804), **COO~Z** (2807) and by me from this seat's gateway identity -- four reads of one object, no disagreement on id, author, content or timestamp. Channel denominator **2** (BG's inaugural header + this buzz) = a complete census, so "the post exists" is not a sampling artifact; BG's own 20:04Z read of count=1 makes the delta **caused, not standing**. AE~Z's runner halves no channel read can see: cycle boundary 20:19:46.16Z caught it, the prior 20:14:46.12Z pass `fetched=0` (an accidental but real before-read control on their own instrument), receipt BUZZED, cursor advanced only AFTER the successful emit -- so a re-fire is idempotent by construction.

### Half 3 -- the clean board
`POST /claim` -> 200 @20:25:52.709Z, `POST /complete` -> 200 @20:25:53.113Z (internal identity `dt-promote-internal@opalinvest.dev`); board FINAL `?status=open` -> **0 open**. Residue is one completed row carrying honest history: created(svc-ticket-form) -> claimed(dt-promote-internal) -> completed(dt-promote-internal). **NO claim/close buzz appeared** -- correct per the routing, W-D is unbuilt and the cursor is past the row regardless; its ABSENCE is the observation, not a failure.

## Scope -- producer only, and the consumer gap demonstrated itself

This certifies form -> DDB -> scheduled runner -> post IN the channel. It is **not** consumer evidence, and that did not need arguing: `0.0.3_BG_BBGTerminal`'s own account is exact -- my fabric-inbox message woke them, and they then hand-polled knowing a post was coming and roughly when. **Nothing about the channel woke anybody, and nothing would have.** The answering limb is the named open gap (`0.5.0_AE_OpalETL~Z`'s channel-leg P1); its A1 acceptance takes the NEXT real post, not this one. Nobody writes END-TO-END off this.

⛔ **CORRECTED 2026-08-20 ~2101Z (`1.0.0_SA_CTO~Z` @`c02f8022d0`) — THIS SECTION CARRIED A FALSE PREMISE AND I PROPAGATED IT.** The struck clause read: *"`0.0.3_BG_BBGTerminal` read NOT REGISTERED at post time, **so** the buzz woke nobody."* **The seat was ALIVE**, in-session, and would have answered instantly. The `NOT REGISTERED` reading was an **artifact**, and the causal `so` was mine.

**THE MECHANISM, now grounded:** `register_agent`'s contract assumes a **periodic** heartbeat (call every 30–60s, degrade at 2 minutes). **An event-driven seat has no periodic anything** — between events it emits zero heartbeats and therefore **reads dead ALWAYS**. In their words, which should survive summarisation: *"THE HEALTHIER I AM AT BEING EVENT-DRIVEN, THE MORE RELIABLY I READ DEAD."* Zero-crons — a correct ruled decision — **produces** the false-dead reading as a structural consequence, not a bug.

**THE CONCLUSION WAS RIGHT FOR THE WRONG REASON, and the correction makes the gap argument STRONGER.** The post woke nobody because of **M2 channel-blindness at source**, not because a seat was down. A seat-down explanation invites the remedy *"keep the seat up"* — **which would have changed nothing.** The true mechanism is that **the consumer limb is dark even with the seat fully alive and attentive.** Only the channel leg closes it. Anyone reading the old framing would have under-rated the channel-leg P1.

**MY OWN INSTRUMENT READINGS FROM THIS SESSION, RE-READ AGAINST THAT MECHANISM:** `get_live_agents` showed `0.0.3_BG_BBGTerminal` absent, and I routed the step-2 readback to `0.5.0_AE_OpalETL~Z` under the subject *"BG IS DARK"* — while that seat was alive and produced a seven-check readback minutes later. Every `send_message` to them returned **`QUEUED … no live session`**, and every one was in fact read and answered. **So for an event-driven seat with an armed Monitor, `QUEUED` does NOT mean undelivered** — the filesystem+Monitor path delivers regardless; `QUEUED` reports only the broker's *push* decision, made off a liveness model that structurally cannot see this seat class.

**THE VERDICT IS UNAFFECTED.** The producer-scoped PASS rests on `1.0.0_SA_CTO~Z`'s Task Scheduler read (scheduled 20:19:46 fire, `LastTaskResult 0`, PT5M cadence matching), not on any seat's liveness. What was wrong was a **premise in the narrative**, and it is corrected here rather than left, because this record is the one most likely to be cited later.

## Compiler Tools
| Tool + invocation | Result | Note |
|---|---|---|
| `comp-which "how do I grep the repo"` (A.3 exercise) | forwarder RAN (own banner); PATH 98 of 99 comp-tools bare | startup; scored on OUTPUT not rc |
| `comp-find --name "ui-smoke*"` | 1 hit / 26795 files scanned, BANDS HEAD=1 | located `portal/scripts/ui-smoke.mjs`, the instrument |
| `comp-find --name "jwt*" infra/` + `comp-find "B4" ...` | MEASURED zero over 1048 files in the portal scope | honest zero; recovered the B4 method from the prior session's scratchpad + netlog instead |
| `python .tools/to-check.py --all --assignee ...` | total=0 (`--all`, never trimmed) | this seat holds no open TO; the work arrived by routing |
| rail-checked raw: `aws secretsmanager get-secret-value opal/auth/jwt-private-key` | key to scratchpad, content withheld, shredded post-battery | no comp-tool models caller secret reach (DE~Z precedent) |
| rail-checked raw: curl controls + writes vs www.opalinvest.dev | 401 / 200 / 201 / 200 / 200 as recorded | live-primitive verification of the SERVED artifact (Rules 20, 22a exercised plane) |
| `ui-smoke.mjs --origin --token --fill --click --netlog` | rc=0, PNG read, 29 requests recorded in-window | the exercised B4 pattern against PROD |
| `read_channel_messages` (gateway, read-only) | count=2, the buzz + BG's header | my own independent readback; three peers read the same object |
No `comp-transform`/`comp-routes`/`comp-pipescript io`: nothing was BUILT or DEPLOYED at this seat this session -- the test exercises already-shipped v2.1.164 bytes. `comp-iam` not applicable: no new boto3 call authored.

## Surprises (surface, do not chase)
1. **`claimed_by` and `completed_by` are NULL on the completed row** while `events[]` carries the actor correctly on every transition. Read as the pre-W-A baseline, not a defect -- CTO~Z ruling 3 (analytics native at every transition) is exactly the work that fills them. Handed to W-A as a free, independently-witnessed fixture whose correct values are already measured: `time_to_claim_s = 462.836`, `time_to_resolve_s = 463.240`. No action taken.
2. Top-level `requester_email` and `firm` are null while the nested `requester{}` object carries both. Same class; stated once, chased nothing.
3. Two addressing corrections inside this window, both stated rather than quietly re-sent: I routed the first report to `0.7.0_AE_CloudOps~Z` reading "AE~Z" off the routing when the runner owner is `0.5.0_AE_OpalETL~Z` (corrected in ~2 min); AE~Z's own first report omitted the one seat blocked on it (corrected in one message). Worth recording because "AE~Z" is ambiguous across two live-ish serials on this device.
4. `audit-archive-invoker` startup findings persist (18 rows, site-Z cross-device baseline class) -- already in FINDINGS.md, not chased.

## Hygiene
Signing key fetched to scratchpad only, overwritten and removed post-battery (verified absent). Both minted tokens scratchpad-only, 60-min expiry. Evidence set: `watertest/{WT_partner_submit_ack.png, WT.netlog, board_final.json, claim.json, complete.json}` + `board_before.json`/`board_after.json`.

## Gate outcome — ACCEPTED, and the decisive plane was NOT mine

`1.0.0_SA_CTO~Z` accepted TAC-2' **producer-scoped** @`c9459dfa2f` (msg 2889). The charge at this seat is discharged. Two amendments to the evidence above, both **narrowing** what this log certifies:

⚠ **THE LOAD-BEARING CHECK WAS ON A PLANE NONE OF THE FOUR READBACKS TOUCHED — INCLUDING MINE.** Four seats verified that the buzz *existed and was correct*. **Nobody verified it came from the PRODUCTION SCHEDULE.** `1.0.0_SA_CTO~Z` read the Scheduled Task itself: `OPAL_D7_ticket_intake` State Ready / LastTaskResult 0 / Next 20:34:45Z / trigger PT5M / Execute = the repo `run_intake.cmd`, with cadence boundaries `:14:46 :19:46 :24:46 :29:46` matching the reported cycles exactly — so the 20:19:46 fire was a **scheduled production fire**.

**This is decisive under our own law, not a nicety:** an ad-hoc run is a legitimate QA instrument but *never the production path, and its artifacts are never production evidence* (CLAUDE.md ad-hoc rule). An ad-hoc-produced buzz would have been a fine QA read and an **INVALID certification** — and every readback in half 2 would have looked identical. **I certified the OUTPUT and never established that the PRODUCER was the production producer.** Banked as a general lesson: reading the served artifact tells you the artifact is right; it says nothing about which producer made it.

⚠ **DEEP LINK — CARRIES, NOT RESOLVES.** A 200 from `opalinvest.dev` is a **SPA catch-all default**; the negative control returns 200 too (`0.5.0_AE_OpalETL~Z`). My half-2 claim was correctly scoped — I asserted the link *carries* `?ticket=<id>`, which is what stands — but stating it explicitly so nobody later reads it as route evidence. **Nobody cites a 200 from that origin as proof a route resolves.**

**Not in this log, verified:** `0.0.3_BG_BBGTerminal` retracted their readback's check-6 parenthesis (a true ASCII observation with an invented `ensure_ascii` cause — the composer does zero coercion). Grepped this file and the ruling record with a positive control: **0 matches, never propagated.** The observation stands, the attributed mechanism is struck.

**Gate candidate status:** ROUTED TO ANDREW, **not implemented**, with `1.0.0_SA_CTO~Z`'s added condition — if ever built, **the lint must name its own scope in its refusal text**, because it cannot reach routing prose and a passing lint would otherwise become evidence for a claim it never evaluated. The framing that a body-text matcher is worse than no gate is upheld.

## Next
1. `[1.0.0_SA_CTO~Z]` TAC-2' acceptance at the gate, producer-scoped.
2. `[2.0.0_SA_COO~Z]` TAC rows close at the validation hold; D7 record line "intake loop LIVE PRODUCER-SIDE; the answering limb is the NAMED OPEN GAP with its fix in flight".
3. `[0.5.0_AE_OpalETL~Z]` channel-leg P1 -- A1 takes the next real post, not this one.
4. `[this seat]` W-C (READ-OWN matrix + the "My Requests" portal view) will want this promote lane when it ships -- noted, nothing now. Holding idle inside the Ticket Center + Opal Analyst focus per MSTR~Z 2694.
