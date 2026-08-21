# /drive tick 43 — 2.0.0_SA_COO~Z lane Z — 22:26Z→22:36Z

**Cycle result: W-B RE-CUT (the stream is dropped), and the number underneath the sovereign card was
found to be unbuildable — then refuted by exercise at two seats within nine minutes.**

## Movement — all seven seats, no nudge ladder opened

| seat | since_tick | verdict |
|---|---|---|
| `0.0.0_AB_MSTR~Z` | 7 | ADVANCING |
| `0.0.3_BG_BBGTerminal` | 6 | ADVANCING (broker QUEUED at 22:32Z — utility seat, work discharged) |
| `0.4.0_DT_ClientPlatform~Z` | 11 | ADVANCING |
| `0.5.0_AE_OpalETL~Z` | 9 | ADVANCING |
| `1.0.0_SA_CTO~Z` | 8 | ADVANCING |
| `2.0.0_SA_COO~Z` | 6 | self |
| `3.0.0_SA_CVO~Z` | 4 | ADVANCING |

Denominator: 22,820 telemetry rows scanned. Nothing PARKED; no dispatch ladder required this tick.

## The advancement act: W-B re-cut

`1.0.0_SA_CTO~Z` @3388 ruled option (ii) on the numbers — **transport dropped, nudge semantics
kept** — and named the re-cut to this seat: *"that is a RE-CUT rather than a cancellation."*

**The prohibition went at the TOP of the task order, not in a footer.** The superseded stream cut is
retained as the record and explicitly marked NOT AN INSTRUCTION. The reason is operational rather
than editorial: `0.5.0_AE_OpalETL~Z` is a live builder and the file instructed building a DynamoDB
stream. **A task order nobody has re-cut is not inert documentation; it is an instruction.**

Also recorded: the four ratified config decisions were *stream* configuration, so they are
**MOOT-BY-SUBJECT rather than overturned** — available intact if the stream is ever revisited, and
flagged so nobody reads a surviving ratification as a surviving instruction.

## The finding: the card's decisive number rested on an unchecked platform constraint

The recommendation went to Andrew quoting a **~30s schedule → ~29s expected**. Nobody had asked
whether the local scheduler can express 30 seconds.

**MEASURED, with a positive control on the retrieval** — the raw task query returned 1,570 chars;
**two earlier greps came back EMPTY and were not read as answers:**

- live `OPAL_D7_ticket_intake` repetition: `<Interval>PT5M</Interval>`
- `schtasks /Create /RI` unit: *"the repetition interval in **minutes**"*

I filed it as **UNESTABLISHED, not refuted** — the CLI's floor is one minute, but whether the
*engine* honours an XML-registered `PT30S` was a different question that I had not measured.

**Why it was urgent rather than pedantic:** at a 1-minute floor the stream's marginal benefit is
~28s against a 14.13s wake hop, so **"the stream's marginal benefit is approximately equal to the
wake hop it cannot touch" — the sentence that makes the card answerable in one word — is true at 30s
and false at 60s.** `1.0.0_SA_CTO~Z` @3423 owned it immediately: *"I built a decisive-sounding
sentence on an UNVERIFIED PREMISE about a scheduling floor, and put it in front of the sovereign."*

## The corner nobody had run

Two sensitivities existed on **different axes** and neither covered the other:
`0.0.3_BG_BBGTerminal` measured detect at 0.83× interval (pessimistic *arrival*, interval held at
30s); I measured the *interval floor* (arrival model held). **The combined corner was unevaluated** —
and it is the one the estate would actually land in.

| corner | ratio | stream margin vs 14.13s hop |
|---|---|---|
| model arrival + 30s | 10.4:1 | ~13s ≈ the hop |
| pessimistic arrival + 30s | 9.6:1 | ~28s — twice |
| model arrival + 60s | 4.3:1 | ~28s — twice |
| **pessimistic arrival + 60s** | **4.1:1** | **~58s — four times** |

>> **THE DECISION IS ROBUST IN ALL FOUR CORNERS; THE RHETORIC IS TRUE IN ONE.** Those are different
claims with different evidence, and collapsing them is how a sound recommendation acquires a fragile
justification — then loses credibility on the justification when the decision was never in doubt.

## Refuted by exercise, two seats, two designs

`0.5.0_AE_OpalETL~Z` ran the full three-plane test with controls; I ran a **disabled far-future
registration probe**, designed to read APPLIED without ever reaching EXERCISED. **Identical
refusal — HRESULT `0x80041318`, `(7,27):Interval:PT30S`.** Their `PT59S` control makes it a
**sub-minute floor** rather than a fact about `PT30S`, and their hand-written XML refusing at
*different coordinates* attributes the constraint to the **service**, not to `schtasks.exe`.

**And the failure mode is the one you would design:** the worry was a *silent round-up* to `PT1M`,
indistinguishable from success. It does not do that — it refuses and names the value.

## Two things this seat got wrong

**1 — My own cleanup control printed a FALSE GREEN.** My probe ended `"CLEANUP: scratch task
deleted, absence CONFIRMED by readback"`. **Nothing was ever registered and the `Unregister` itself
errored.** `Register-ScheduledTask` threw a *non-terminating* error, so `catch` never fired, so
`$landed = $true` executed on the failed path. The absence was true **for the wrong reason**, and
the line would have printed byte-identically had a real delete silently failed. I wrote that
verifier deliberately, in a session spent cataloguing instruments that cannot fail, and shipped one.

**2 — I came within one send of filing false debt against a peer.** At 22:33Z I measured two of
`0.5.0_AE_OpalETL~Z`'s scratch tasks `State=Ready` and firing every minute, against their message
saying *"cleaned up, nothing left running."* I had the accusation half-drafted with the
shadow-pipeline *"these never get decommissioned"* line attached. **I re-read instead of sending:**
22:35:41Z shows **0 remaining, denominator 210 → 208** — exactly two removed, which is what
separates a real delete from a filter that stopped matching.

>> **A CLEANUP OBSERVED MID-FLIGHT IS BYTE-IDENTICAL TO A CLEANUP THAT NEVER HAPPENED.** My snapshot
was true and my conclusion would have been false. **The discriminator was re-reading, not reasoning
harder about the first read.**

## Production state

`OPAL_D7_ticket_intake`: `State=Ready`, `<Interval>PT5M</Interval>`, verified across a 208-task
enumeration. Untouched by any probe this tick.

## Carry-forward

- W-A apply at the laptop (grant first, then deployed exercises) — MSTR~Z holds it on the
  cross-fabric board
- W-D limb (2) at Andrew; W-E criteria (2)(3) + DL tenant-admin actor
- W-C capacity-blocked behind the 6-seat ceiling; the release call is mine when it goes hot
- The intake's gateway-credential expiry window — the standing production exposure, unchanged
- **WB-R1 is DISCHARGED** by the two-seat exercise; the re-cut's remaining open item is the nudge
  semantics, which never depended on the transport


---

## Addendum 22:41Z — S2's repo half is NOT stranded, and the proof was in my own tool manifest

`3.0.0_SA_CVO~Z` caught, with the ferry in flight, that **~88% of the stream's ~16s best case is the
agent WAKE HOP, not transport** — so the honest answer to *"can it be faster?"* is **"not from here"**
rather than "no." `1.0.0_SA_CTO~Z` amended the card. **That clause routes the residual to "a
different workstream with a different owner and its own possible remedy."**

**A phrase that routes a question should name a workstream that is actually moving.** I checked it
rather than letting the card assert it — the same act that found W-C naming a serial with no seat.

**It is real and it is owned:** S2 (resident schemas), owner `0.5.0_AE_OpalETL~Z`, ruled by
`1.0.0_SA_CTO~Z` msg 2617. But their own log records the repo half as
*"Live broker NOT restarted (ruled — rides the next reserved restart)"* — **an accepted-but-unapplied
leg, the exact shape that goes quiet without anyone deciding it should.**

**MEASURED:**

| fact | value |
|---|---|
| S2 repo-half commit `83e6a786d7` | 2026-08-20 14:37:16 -0400 (**18:37Z**) |
| my session's broker server PID 29444 | started 15:44:27 -0400 (**19:44Z**) — **after** |
| further server starts after it | 15:44:32, 16:08:21, 16:23:35 local |
| denominator | 14 broker-candidate processes, paired launcher+python |

>> **THE RESTART NEVER NEEDED SCHEDULING.** The broker is a **per-session stdio server**, not one
long-running daemon — so every session spawned after the commit picks up the new `server.py`
automatically.

>> ✅ **AND THE EXERCISED PROOF WAS SITTING IN MY OWN TOOL MANIFEST.** In this session
`ack_messages` is a **RESIDENT** top-level tool. **All fifteen** of its `opal-agent-comms` siblings —
`check_inbox`, `send_message`, `heartbeat`, `get_agent_status`, `register_agent`, `get_live_agents`,
`get_org_summary`, `list_agents`, `list_task_orders`, `query_project`, `read_agent_latest_log`,
`set_summary`, `deregister_agent`, `deregister_all_stale`, `get_delivery_state` — are **DEFERRED**
behind `ToolSearch`. **One of sixteen is resident, and it is exactly the one carrying the `_meta`.**

**THE CONTROL IS BUILT IN AND I DID NOT HAVE TO CONSTRUCT IT:** if `_meta anthropic/alwaysLoad` did
nothing, `ack_messages` would be deferred alongside its fifteen siblings. The discriminator is the
**15 negatives sitting beside the 1 positive** — same server, same box, same session.

**WHY IT LANDS ON THE CARD:** the routed question now has a **working mechanism** under it rather
than a hoped-for one. The lever that attacks the wake hop is demonstrated to function on this box,
today, in a live session — so the clause can drop the word *"possible."*

**BOUNDS, stated before anyone quotes it:**
- Proves `alwaysLoad` **works**; does **NOT** prove S2 is **done**. Exact-six residency spans two
  servers and is not expressible as seat config alone (AE~Z's own structural finding). The gateway
  half and the env `auto:25` half are **separate legs and I measured neither**.
- Proves residency in **my** session. BG's 14.13s wake hop was measured in **theirs**, and whether
  that seat carries the resident schema is a different question I did not ask. **The 14.13s figure
  is not retroactively improved by this.**
- The per-session stdio architecture is an **inference** from the process pattern. Strong, and still
  an inference; the tool-manifest evidence stands independently of it.
