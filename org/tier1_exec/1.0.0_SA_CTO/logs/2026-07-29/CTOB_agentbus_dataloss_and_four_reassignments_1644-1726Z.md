# CTO~B: agentbus data-loss closed; four re-assignments in 35 minutes, zero lines of tooling built

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE

Lane: `1.0.0_SA_CTO~B` (logged in the base-serial folder; lane named in the title per the standard).
Window: session start ~2026-07-29T16:44Z -> 17:26Z. First log of this session.

---

## Summary

Spawned 164223Z on Andrew's direct word into a NEW scope (INFRASTRUCTURE.TOOLS, not the
PORTAL_AUTHHARD my own logs carry). Closed two data-loss defects in `.tools/agentbus-sqs.sh`, both
exercised. Built ZERO lines of the three tooling workstreams I was dispatched, stood down from,
re-assigned, and superseded on -- every re-point arrived before I wrote code, which was luck, not
design.

---

## Work done

### 1. `.tools/agentbus-sqs.sh` -- two data-loss defects, both exercised (THE substantive work)

**`2bc9515c3c`** -- MSTR reported the jq-absent fallback truncating message bodies. He said
explicitly *"do not take my report on trust either; the reproduction above is runnable."* I
reproduced all four limbs before touching anything:

| claim | measured |
|---|---|
| `command -v jq` in a harness shell | NOT FOUND -> **the lossy fallback was THE LIVE PATH** |
| `.tools/jq.exe` | jq-1.7.1, tracked, works |
| `grep -o '"Body": "[^"]*"'` on a quoted body | `Andrew said \` (truncated, rest gone) |
| same input via jq | `Andrew said "stop" and more text after` |
| `grep\|cut\|while` with ZERO extractions | rc=0 -> `emitted=1` -> **DELETED having emitted nothing** |

Root cause is NFRA_TOOLARCH.PATHFIX: harness shells source no profile, so `.tools` is never on PATH
and `command -v jq` fails on EVERY harness shell. The bus carries largely verbatim Andrew quotes,
which contain quote characters by definition -- so it fired on exactly the traffic that matters most.

Fix is RESOLUTION, NOT HARDENING: derive jq from the script's own location, so the lossy path never
executes. The remaining no-jq fallback now **cannot delete anything** (`emitted=0` unconditionally) --
a stronger and more checkable property than MSTR's suggested count-matching. `recv` given the same
structural treatment; with no jq it declines to delete rather than guessing.

**Honest limit recorded in the commit:** I hypothesised a phantom-ReceiptHandle hazard, wrote the
negative control, and **IT DID NOT REPRODUCE** -- in well-formed JSON those quotes are escaped, so the
old grep could not match them either. Made the extraction structural anyway but did NOT claim it as a
fix. A control that fails to reproduce is a finding about my hypothesis, not a licence to ship the
change as a fix.

**`1bf1fa6e4a`** -- bar item (g), `send()` at :155. MSTR offered the reason to close it
(*"a UUID cannot contain a quote"*). I verified rather than accepted it: **correct, and now written
into the file** (MessageId charset `[0-9a-f-]`, truncation risk nil). But checking it surfaced a
DIFFERENT real defect on the same line -- **the third instance of one class in this single file**:

    extraction yields nothing -> mid="" -> "SENT to sitez: MessageId="  at rc=0

The send SUCCEEDED. So it is a RECEIPT failure, not a send failure, and conflating them is expensive
BOTH ways: read as send-failure the caller RESENDS AND DUPLICATES; read as success the caller holds an
unusable receipt. Rule 22b's ack discipline hangs off that id -- an empty one makes a real, delivered
message permanently UNACKABLE, which is the SENT-IS-NOT-READ gap this bus exists to close. Now exits
rc=3 (distinct from rc=2 arg errors) with the raw response dumped so the id is recoverable by hand.

**The pattern, since it is now three:** empty-vs-failed-retrieval (contract C3) has bitten this file
at the body emit, the delete gate, and the send receipt. Each looked local. The general form is that
every one allowed **SILENCE OR EMPTINESS TO STAND IN FOR A FACT** -- and in a messaging tool the facts
are precisely what the caller cannot re-derive.

### 2. Closed a gap in my OWN work before reporting it done

I had modified `send()` and only tested it against synthetic fixtures -- a config-read-grade test
backing a behavioural claim, one report away from being marked validated. Exercised it live:

    baseline  both queues peeked depth 0 / 0-in-flight (consumes nothing)
    device    resolver -> `laptop`, basis: workspace path
    SEND      -> MessageId=d7af661f-68bc-4814-8607-e8327b5d31a0, rc=0
              NORMAL PATH UNBROKEN -- the real risk of that change was the conditional I put on the
              line every send passes through
    after     depth 0 visible AND 0 not-visible

Fixture deliberately carried quote chars + a trailing marker (`END-MARKER-CTOB-9X2K`) placed AFTER
both quoted phrases -- a SECOND independent truncation test, from a different hand, through the SEND
path rather than injected at receive. A fix confirmed only by its author's chosen fixture is the
hand-chosen-control problem.

**Claimed as INFERENCE, not delivery:** queue drained to 0-visible-0-in-flight, and delete is gated on
successful emit, so a message GONE rather than merely invisible implies the consumer emitted it. But
producer-side signals are blind to consumer death -- ack requested from MSTR; that is the only oracle.

### 3. Completion bar (MSTR 171215Z, Andrew-direct: SQS is my ONLY job)

| item | verdict | evidence |
|---|---|---|
| (a) Z->laptop + ACK | MET | MSTR's, b02b96d8 / dbaf5251 |
| (b) laptop->Z + ACK | MET | MSTR's, ~Z acked 1512Z |
| (c) OFFLINE DURABILITY | MET | accidental real-traffic timeline: msg sent 16:42:46Z to a device with NO consumer, delivered intact ~17:08Z on re-arm |
| (d) consumer both devices | MET | ~Z bjnsnjyip; MSTR bnkj8hvhy |
| (e) no-data-loss EVERY emit path | MET | **verified on recv, not inferred from the watch fix**: recv prints RAW JSON at :205, never text-extracts bodies, so truncation structurally never applied there |
| (f) queues under TERRAFORM | **OPEN, NOT MINE** | 0.7.0_AE_CloudOps, TO OPAL_SQSCHAT.T1, post-freeze. Tracking. Two live queues costing money outside state is not a finished system -- not marking it green from my side |
| (g) send() text-grep | CLOSED | `1bf1fa6e4a`, above |

**KNOWN RESIDUAL, deliberately NOT closed green -- for Andrew:** the consumer is SESSION-BOUND on both
devices. Six agent sessions died today. My framing sharpens MSTR's: **the residual is NOT data loss**
(his accidental timeline disproved that; SQS durability is exercised on real traffic) -- it is an
**UNBOUNDED, INVISIBLE DELIVERY LATENCY**, bounded by nothing except when a human next starts a session
on that device, and **a deaf device and a quiet one are byte-identical from every vantage the system
currently offers**. `peek` already discriminates them by hand across two spaced reads. I proposed NO
monitor/alarm/scheduled task: the moratorium stands, and monitoring a consumer whose lifecycle is the
open question would measure the wrong thing precisely (Andrew's canonical-routes-first ordering). This
is an architectural decision (durable per-device consumer vs accepted manual re-arm), not an oversight
to patch.

### 4. Tooling workstreams: dispatched, stood down, re-assigned, superseded -- ZERO built

Four routing changes in ~35 minutes, three authorities, **every one locally correct**:

    164328Z  CVO dispatches WS1/WS2/WS3 (Andrew-direct designation)   -> ACKed 164530Z
    170158Z  CVO STAND-DOWN, all three to ~C (Andrew-direct ~1705Z)   -> ACKed, handed recon
    170957Z  base CTO AMENDS: I keep WS1                              -> conflict surfaced 171134Z
    171215Z  Andrew-direct ~1712Z: SQS is my ONLY job                 -> broadcast same turn
    171320Z  CVO deconfliction: base CTO's split RESCINDED, all ~C's

I wrote zero lines of WS1/WS2/WS3 throughout. Each re-point landed BEFORE I built -- luck, not design;
twenty minutes later on any of them and there is a half-built tool in the seam. Said so to base CTO
rather than let it read as a clean handoff.

**Recon handed to `1.0.0_SA_CTO~C` at 170449Z** rather than discarded. Credited in the record by CVO:
the **bare-except header swallow** I found in `pipescript`'s vintage banner (a missing/corrupt resolver
prints NO HEADER AT ALL -- absence reads as "no source" rather than "failed read", contract C3 inside
the very feature being promoted to a fabric-wide contract) is now a **binding clause of the
comp-tool-wide header contract @c2e38883a0**: *"no header emittable => rc=2 + explicit SOURCE
UNRESOLVABLE, never silence."* Both owned-paths blockers I flagged are in ~C's routing packet.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 startup EXERCISE (`"how do I grep the repo"`) | PASS | scored on OUTPUT (its own banner), not rc -- rc tracks MATCH/NO-MATCH, not health |
| A.3 PATH denominator | `93 of 93 comp-tools resolve bare` | PASS | ran the mandatory second half; resolution-without-execution is the anti-correlated probe that reads 100% healthy when breakage is total |
| `comp-surface-check` | auto via `safe-commit.sh` x2 | PASS | "1 changed file(s) touch no critical surface" |
| risk-reflex (`comp-pulse diff`) | auto via `safe-commit.sh` x2 | CLEAN | DENOMINATOR printed: 1 file vs 1484 danger nodes; map 13.4h/13.7h old |
| `audit-archive-invoker` | A.2 startup | **rc=1, 2 findings** | see Gap below |

**What worked:** the A.3 exercise half. Had I run only `command -v`, I would have recorded a clean
PASS -- that is the probe XXX.md documents as reading 100% healthy precisely when the failure is total.

**What failed:** nothing I ran failed.

**GAP FOUND (worth a tool, and it bit three lanes today):** *there is no comp-tool that answers
"can serial X commit path Y?"* I answered it four times today by raw-grepping `.owned-paths.yaml` and
hand-resolving longest-match + lane membership -- for `infra/aws/globgrph/**` (AE-only, no
globgrph-specific rule), `.tools/**` (ANY), `org/tier1_exec/1.0.0_SA_CTO/**` (BASE_EXEC), and
`ANY_CTO` membership. It blocked or nearly blocked THREE lanes in one session (~B, ~C, and WS1 steps
2-3 for whoever takes them). The failure mode is expensive and consistent: **it is discovered at
COMMIT time, after the work is built.** A `comp-ownpath <serial> <path>` returning the resolved lane +
longest-match rule + verdict would have cost minutes and saved hours. Routed as an observation, not a
build request -- I hold no tooling lane.

**SECOND FINDING, surfaced to base CTO, not investigated by me (not my lane):**
`audit-archive-invoker` returned `[INTEGRITY/NON-APPEND-EDIT] org/git-author-override-audit.log --
first divergence at line 1 col 1, baseline 1696149B vs live-head 12917B`. A ~99.2% shrink on an
append-only AUDIT log, diverging from byte one. May be a legitimate rotation the baseline never
learned about -- but that is byte-identical to a wipe, and it is the file recording author overrides.
Not filed as housekeeping. Routed 164944Z.

---

## Files Modified

See commit messages -- they carry the per-file reasoning: `2bc9515c3c`, `1bf1fa6e4a`.
Both touch `.tools/agentbus-sqs.sh` only. Both pushed to CLOUD.

---

## MCP traffic

~18 messages handled. Significant ones only:
- **IN** MSTR 164343Z spawn direction (Andrew-direct scope + no-fleet constraint + stale-resume warning)
- **IN** CVO 164328Z WS dispatch -> **ACK 164530Z** (7-constraint read-back, zero corrections returned)
- **IN** base CTO 165104Z boundary + freeze ruling (additive lands, rename holds)
- **IN** MSTR 165356Z agentbus data-loss item -> **CLOSED `2bc9515c3c`**
- **IN** CVO 170158Z STAND-DOWN -> **ACK 170539Z**; recon **OUT** to ~C 170449Z
- **OUT** 171134Z URGENT conflict surface to base CTO (two live instructions, ~C already building)
- **IN** MSTR 171215Z gate PASSED + Andrew-direct ~1712Z scope + completion bar
- **OUT** 171330Z / 171349Z Andrew-direct VERBATIM broadcast to base CTO + COO (XXX.md same-turn rule)
- **OUT** 172137Z completion bar filled in; **OUT** 172441Z ack request on the live fixture

RAVC: opened + closed with MSTR on the data-loss item (his independent exercise PASSED). One open:
ack on MessageId `d7af661f-68bc-4814-8607-e8327b5d31a0`.

---

## Blockers

**None blocking.** Two items are OWNED ELSEWHERE and tracked, not blocks:
- (f) Terraform for the two live queues -- `0.7.0_AE_CloudOps`, TO OPAL_SQSCHAT.T1, post-freeze.
- WS1 steps 2-3 (`extract_s3_served.py` + SERVED_FROM derive edge) -- `infra/aws/**` is AE-only with
  no globgrph-specific longest-match rule, so NO CTO serial can commit them. Unowned as of this
  writing; surfaced to base CTO and COO.

**A CORRECTION I OWE, recorded here because I stated it twice to others:** I told MSTR and CVO that
`org/tier1_exec/1.0.0_SA_CTO/**` (BASE_EXEC) blocks this lane from landing a deliverable doc. That was
an INFERENCE from lane membership which I did not test -- and prior `~B` log commits exist at exactly
that path (`5f8da26edb`, `6dd6eb8f02`). The commit landing THIS file is the test. If it passes, my
earlier statement was wrong and I will correct it to both of them rather than let it stand.

---

## Current State

- `.tools/agentbus-sqs.sh` at `1bf1fa6e4a` on CLOUD, pushed. `JQ=` resolver (`:70-90`) derives
  `.tools/jq.exe` from the script's own dir; `watch` emit + delete and `recv` delete are structural;
  no-jq paths CANNOT delete; `send()` exits rc=3 on an unreadable MessageId with the raw response
  dumped.
- Both queues (`agentbus-ajbdev-sitez-to-laptop.fifo`, `-laptop-to-sitez.fifo`, us-east-1 /
  313476888478) at depth 0 / 0-in-flight. **LIVE AND OUTSIDE TERRAFORM.**
- MSTR's consumer `bnkj8hvhy` armed on this device; ~Z's `bjnsnjyip` on site Z. **Both session-bound.**
- Completion bar: (a)-(e) MET, (g) CLOSED, (f) OPEN/not-mine. Session-bound consumer = KNOWN RESIDUAL
  for Andrew, deliberately not closed green.
- All four tooling workstreams belong to `1.0.0_SA_CTO~C` (CVO deconfliction 171320Z).
- PORTAL_AUTHHARD **PARKED** by base CTO in those words; silence means parked.
- Two PORTAL_AUTHHARD items sit unread-by-scope in my inbox from 07-23 (mockadv FIRM_ALLOWED_PATHS
  intent, expiry-clocked 2026-08-06; and four stale `opal-partner-*` allowlist rows incl. a
  Rule-23-adjacent `user@cottonwood.com` on a domain we have no ownership evidence for). **NOT
  actioned -- out of scope this session.** Flagged here so the expiry clock is not lost with me.

---

## Next Steps

1. **[0.0.0_AB_MSTR]** ACK MessageId `d7af661f-68bc-4814-8607-e8327b5d31a0` and confirm
   `END-MARKER-CTOB-9X2K` arrived -- the marker sits AFTER both quoted phrases, so its presence is the
   discriminator for a surviving truncation. Present = truncation dead on a second independent
   fixture through a different path.
2. **[0.7.0_AE_CloudOps]** bar item (f): the two live queues under Terraform, post-freeze
   (TO OPAL_SQSCHAT.T1). I track and report; I do not build it.
3. **[Andrew]** SOVEREIGN CALL: is "done" achievable with a session-bound consumer, or is the durable
   per-device consumer required? Stated as a residual with the mechanism, not escalated as a fire.
4. **[1.0.0_SA_CTO]** WS1 comp-opalbizsem re-route (unowned after my supersession) AND the unowned
   `infra/aws/globgrph/**` steps 2-3 lane question -- an AE hand or a grantor-landed scoped grant
   (SoD: not the grantee).
5. **[1.0.0_SA_CTO]** own or assign the `git-author-override-audit.log` integrity finding.
