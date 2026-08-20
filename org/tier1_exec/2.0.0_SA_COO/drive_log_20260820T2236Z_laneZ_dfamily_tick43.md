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
