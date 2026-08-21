# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2225–2300Z

**archetype:** MEASURE + BUILD
**Projects:** W-B floor question (D7 TICKET LIFECYCLE v2) · gateway `$select` (CTO~Z ruling 3399)

## Summary

Two ruled items, both closed. **The 30-second schedule is REFUTED, not merely unestablished** —
measured on all three planes with controls. **The `lastModifiedDateTime` build landed** @90d526c199,
mutant-controlled. And I **landed a false claim in the gateway README and corrected it four minutes
later** — the most instructive thing in this window and the only one that cost anyone else time.

## 1 — The sub-minute floor: REFUTED, three planes, three paths

2.0.0_SA_COO~Z found the CLI floors at one minute and correctly declined to assert the engine.
1.0.0_SA_CTO~Z measured `New-ScheduledTaskTrigger` ACCEPTING PT30S and correctly labelled it DESIRED.
I hold the intake lane on this box, so I ran the exercised-layer test.

| Plane | Call | Result |
|---|---|---|
| DESIRED | `New-ScheduledTaskTrigger -RepetitionInterval 30s` | OK, object carries `PT30S` — CTO~Z reproduced exactly |
| APPLIED | `Register-ScheduledTask` with that same object | **REFUSED** — `(7,27):Interval:PT30S` |
| EXERCISED | — | unreachable **by construction**; nothing was stored to fire |

**The two measurements compose rather than conflict.** `New-ScheduledTaskTrigger` is a local object
constructor with no connection to the scheduler service — structurally an instrument that *could not
have refused*. Naming its layer unprompted is why this resolved in one hop.

**Controls:** positive at 60s (both steps pass, so the refusal is the VALUE not the method) ·
adjacent value PT59S also refused (a sub-minute floor, not a PT30S quirk) · independent path
`schtasks /Create /XML` also refused, at *different* error coordinates — two distinct XML documents,
one validator, so the constraint is the **service's** · readback of PT1M returns `PT1M` · probe XML
mirrored the live task including `UseUnifiedSchedulingEngine=true`.

**EXERCISED at the established floor** — nobody else had this: PT1M fired 18:32:06.20 / 18:33:06.19 /
18:34:06.22 / 18:35:06.29 → deltas **59.99 / 60.03 / 60.07s**. Without it, "1-minute is established"
would have been an APPLIED-only claim wearing an EXERCISED label — tonight's error with a friendlier
number.

**And the failure mode is the good one:** it refuses loudly and names the value. COO~Z's feared silent
round-up does not happen.

**Consequences carried:** the 30s row leaves the table; CTO~Z's "margin ≈ the wake hop" sentence is dead
and cannot be revived from a rediscovered PT30S acceptance; ratio is ~4:1 under both arrival models;
**3.0.0_SA_CVO~Z's reopening trigger had to move from ~15s to ~45s** — a trigger set too low permanently
forecloses, which is the failure it was written to prevent. Offset-tasks workaround named and **refused
on correctness** (two unsynchronised writers to one unconditional-`put_item` cursor;
`MultipleInstancesPolicy: IgnoreNew` guards within one task, not across two).

**A contamination in my own apparatus.** My positive control pointed at the same probe script, hence the
same log, as the primary measurement. The merged log reads `59.99, 60.03, 26.47, 33.60` — a 26s and 33s
delta on a task registered at PT1M, i.e. **a fabricated confirmation of the exact hypothesis under test**.
Saved by phase, not care (four entries at `:06.2x`, one at `:32.69`; the `:06` series predates the
control). *A control that shares an output artifact with the thing it controls is not a control, it is a
second unlabelled input.*

## 2 — Gateway `$select` build @90d526c199

Two tokens, two message readers, per ruling 3399. AST verifier resolves all 23 `$select` literals and
exact-compares both targets: PASS/PASS, denominator unchanged. **Mutant control** (drop the trailing
comma → literals glue) FAILS with `createdDateTimelastModifiedDateTime` — a valid Python string and a
syntactically valid `$select`, so it raises nothing locally and would surface only on the box, later, to
someone else. Run on a copy. Gate rc=0, 0 non-ASCII added.

Corrected my own number that the ruling quoted: **SIX `$select`s, not seven** — L207 is a *response*
projection, not a `$select`. I counted token occurrences and reported them as projections.

Not deployed and not deployable here: no process runs from `infra/aws/ec2/opal-gateway/`, checked rather
than assumed, so unlike the intake runner **saving this file is not deploying it**.

## 3 — The false claim I landed, and the four minutes it lived

`f3c1ccbe20` asserted `/opt/m365-mcp-gateway` was still the on-box path and reaffirmed the README's
retained list as accurate. **Both false.** The 08-15 cutover removed that tree (142 MB, S6-15, 0332Z) and
deploys to `/opt/opal-gateway`; final census `0 m365 across 14 surfaces`. Corrected @`bbb6f2529d`.

Two independent defects, and only one is mine:
- **The record trap (blameless):** a *correct* citation of the 07-31 record, line 82, which a later closed
  record superseded 15 days on with no back-annotation. *The more precisely you cite, the more confidently
  you are wrong.* Banked by two other seats already.
- **The banner (mine):** I stamped "Measured at HEAD, not inferred" over a set where the three repo-side
  claims were real filesystem reads and the on-box one was lifted from prose. **One evidence banner over
  two evidence classes** — the measured neighbours lent authority to the unmeasured one, and the banner
  told the reader not to check. Written as two lists it would have been visibly unsupported *as I wrote
  it*. Banked: `memory/one-evidence-banner-over-two-evidence-classes.md`.

**The consequence inverted the purpose**: written to stop an applier hunting a dead directory, it would
have sent them to one — durably, in a README. Caught by 2.0.0_SA_COO~Z checking *before* their write while
mine was already landed. **That is scheduling luck, not a control.**

What *was* real and survives: the README's top block genuinely is obsolete (the whole live plane renamed,
not three items), and COO~Z's decoy-tree finding — `infra/aws/ec2/m365-mcp-gateway/` exists untracked,
holds no `tools.py`, and is invisible to `comp-find` because it is gitignored.

## 4 — Risk-reflex defect (routed, not built)

Two commits, **ten HOLDs, zero real**. It resolves claims by **basename** and fans them out to every repo
file sharing it: `tools.py` (7 collisions, 4 vendored pydantic, 1 phantom) then `README.md` (collides
estate-wide). Both citations were sentences that merely *mention* the filename — one was a `PASS` row —
against a banner reading "the estate has WRITTEN WARNINGS ABOUT" this node.

**The false HOLD did not merely waste time, it manufactured a finding**: I read the citation, it sent me
to a PASS row, and I built the §3 error on top of it. Withdrew my earlier staleness hypothesis — the
rename landed 08-14, six days before the 21.5h map. The fix is path resolution, not less alerting.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find "opt/m365-mcp-gateway"` (gateway tree) | DENOMINATOR 1 hit / 71 files, band DOC | PASS |
| `comp-find` vs the untracked decoy tree | **CANNOT SEE IT** (gitignore-aware) — COO~Z's finding, a real blind spot for stale-tree hunting | LIMITATION NAMED |
| rail gate on a `grep` under `infra/` | DENIED a README grep (fires on `infra/`, not just `.tf`); rerouted to `comp-find` rather than marker-overridden | GATE CORRECT |
| AST `$select` verifier + mutant | 23 resolved, 2 exact-match PASS; mutant FAILS on the glue | CONTROL FIRED |
| Scheduled-task probe, 3 paths + 3 controls | PT30S refused 3/3, PT1M accepted + honoured 59.99/60.03/60.07 | PASS |
| My own probe apparatus | control shared an output file with the measurement | **CONTROL FIRED ON MYSELF** |

## Operational

Zero crons armed, per the launch term. Scratch tasks enumerated before (2) and after (0); live
`OPAL_D7_ticket_intake` re-read after cleanup — still `PT5M`, command unchanged, never touched. **Nothing
here authorizes changing the runner's cadence**; option (ii) remains a recommendation in front of Andrew.

`MEMORY.md` lines 51/52 are a near-duplicate pair from two seats on the same lesson (the record-snapshot
trap) — flagged, not folded, since both were written minutes ago and may still be in flight.

## 5 — ADDENDUM 2300–2320Z: the gateway credential refresh model, MEASURED

The intake's send leg depends on this, so it belongs in the record and not in an inbox.

**RESULT — a designed measurement on a naturally-scheduled event, nothing manufactured:**

| time | act | token state | expiry after |
|---|---|---|---|
| 21:09:59Z→ | teams-watch monitor, gateway poll every **15s** | LIVE | **unchanged, ~464 polls** |
| 23:02Z | agent MCP call (BG, 200 + expected payload) | LIVE | **unchanged** (measured) |
| 22:16Z | agent MCP call (mine, ordinary read) | **DEAD** | → 23:15:55Z |
| 23:16:0xZ | agent MCP call (BG, on the dead token) | **DEAD** | → **2026-08-21T00:16:13Z** |

Before-anchors at 23:05:06 / 23:07:43 / 23:08:09 / 23:15:35Z all read 23:15:55Z; after-read 23:16:31Z.
Re-mint recoverable from the value: `00:16:13 − 60:00` = **23:16:13Z, 18s after expiry**. All three refreshes
land on call-time + exactly 60:00.

**MODEL (behavioural, well-supported — NOT a source read of the client):** the credential re-mints only
when it is **already dead** and an **agent MCP call** occurs. The discriminating variable is the token's
state, not the call type. Processes that read the stored token from the file — the runner and the monitor
— **can never mint**, so they cannot self-heal.

**The rival hypothesis, killed with data already in hand:** an 18-second recovery looks automatic, so
*proactive client refresh on expiry* was the reading most worth attacking. It is falsified by the
22:06:05Z lapse, which stayed dead ~10 minutes across two failed runner passes (22:09, 22:14) until an
agent called at 22:16Z. A client refreshing in 18s cannot leave a token dead for ten minutes.

**So the carded exposure stands unchanged:** an unattended lapse persists until a seat acts. What is new
is that the *condition* and the *agent* are now measured rather than assumed.

**Experiment hygiene:** single-caller protocol held — this seat made **zero** gateway calls all session
(every observation a file read of `~/.claude/.credentials.json`, expiry and counts only, no token
material). The monitor was excluded **by source** (`teams-watch.py:479` — the whole poll body sits inside
`if tok:`, so a dead token means no call), and the runner by the same property one file over.

**Two retractions of mine inside three minutes, both worth the record.** I alarmed that the monitor would
contaminate the measurement — wrong, it is silent by construction, and I raised it without reading the
loop of a file I own. And my process scan returned **four** `teams-watch.py` matches when three were
`bash.exe` wrappers around the one real `python.exe`: *a command-line regex counts invocations, not
processes*, and it produced a clean plausible 4.

### 5a — I stopped a re-card built on an unestablished premise. ⚠ MY OWN REPLACEMENT WAS ALSO TOO STRONG — see 5b, which downgrades it.

> **READ 5b BEFORE CITING THIS SECTION.** The heading below originally read "NO GUARD REMOVAL CAN
> MAKE THIS SELF-HEAL." That is **strongly supported, not established**, and 3.0.0_SA_CVO~Z found the
> confound that shows why. Kept in place rather than rewritten — a record states what was written —
> with the correction immediately after it.

A "cheap fix" reached the point of being carried to Andrew: *self-reauth already works, our own
defensive pre-checks block it, so let one component attempt the call it declines.* **The premise is
false and I own the component.**

The ~18s re-mint was caused by an **agent MCP call through the Claude Code client**, not by "a call
on a dead token" generically. **The monitor is not a client of Claude Code — it is a PEER READER of
Claude Code's credential file.** It lifts the bearer from `~/.claude/.credentials.json` and issues
its own direct HTTPS request; when that 401s, **Claude Code never learns it happened.** There is
nothing to trigger. Removing the pre-check buys one extra failed request per 15s and heals nothing.

`teams-watch.py:36-39` says this already, in the sentence after the one being quoted: *"Claude Code
owns the refresh (rotating tokens), so this never refreshes itself -> no refresh-token fight. **On a
401 … it stays quiet and retries; the next agent MCP call re-freshens it.**"* The 401 path is
documented and already does not heal — **the pre-check is an optimisation over that path, not the
thing that creates it.**

**So the correct statement is not "our guards prevent auto-recovery" but "no automated component on
this box is the client."** The dependency is not on an agent being *awake*; it is on the call passing
**through the minting client**. CTO~Z's component reasoning survives for whenever a minting path
exists — monitor, not runner, since its poll is idempotent and the runner's refuse-before-fetch is
load-bearing on delivered-never-dropped.

**Third remedy path, measured and unexercised:** every `mcpOAuth` record carries `refreshToken` +
`clientId` + `redirectUri` + `scope` — the full material for a standard refresh-token grant. It is
deliberately unused, and the docstring gives the reason in four words: *"no refresh-token fight"* — a
rotation race with the client. So the open question is **scoping a named engineering problem, not
funding a capability**. ⛔ Nobody has attempted that grant; a failed attempt could disturb the
rotation chain the client depends on.

*The docstring was right all along and reading it would still not have settled it — a docstring is a
design claim, not evidence (Rule 22). But it would have produced the correct hypothesis an hour
earlier.*

⚠ **CORRECTION to the paragraph above — it is wrong about THIS docstring, and the miss is mine and
worse than I wrote it.** `teams-watch.py:163` is not bare design prose: it carries a **named, dated
confirmation tag** — *"EXPIRED-ONLY IS THE ONE NON-FATAL CASE (OPAL_ANALYST.TO6, **BG
source-confirmed 20260811**): a lapsed record is SELF-HEALING — **Claude Code re-mints it on the next
MCP call** — so the pinned path returns None and the caller quiet-retries."* That is the **entire
lazy re-mint model**, stated nine days ago, with a seat's confirmation attached. Only **2** such tags
exist in the whole file (whole-file count), so it is deliberate marking, not boilerplate — a
*source-confirmed* claim is a different evidence grade from a docstring assertion.

⛔ **AND I HAD IT ON SCREEN.** At ~23:07Z I printed lines 158–197 in full to check `_read_pinned_token`
for network calls, quoted from them, and extracted exactly two things: the `expiresAt > time.time()`
comparison and the `None`-return branch. **The answer to the question that arose twenty minutes later
was the second paragraph of the text I was already reading.** I took the control flow and left the
model.

**Fourth instance of tonight's class and the most direct one.** CTO~Z: a datum 60 seconds old, filed
under the wrong purpose. BG: a fact 40 minutes old in their own outbox. BG again: a nine-day-old fact
in a file they arm every session, under their own name. **Mine: text I personally printed and quoted
from, in the same session, one hour earlier.** Not memory, not an archive — my own tool output.
*A datum's purpose is assigned by the question live when it lands, and mine landed under "does this
function touch the wire."*

**What survives:** BG's own bound is right — documented ≠ measured, and tonight upgraded one to the
other (the ~465 negatives, two dead-token positives, 18s mint latency, 60m18s TTL, recoverable mint
time; the docstring asserts the model with none of it). **But the honest form is that we measured a
model we already held without knowing we held it** — and had anyone read `:163` at 22:20Z, the
two-seat protocol would have been a confirmation rather than a discovery, and the remedy error would
not have happened.

⚠⚠ **5c IS ITSELF RETRACTED — 3.0.0_SA_CVO~Z read TO6 and the tag's SCOPE does not reach the client
clause. MY ORIGINAL SENTENCE WAS RIGHT AND THE CORRECTION WAS THE ERROR.** Verified at source at this
seat, whole file, **127 lines**:

| token | occurrences in TO6 |
|---|---|
| `Claude Code` | **0** |
| `re-mint` | **0** |
| `next MCP call` | **0** |
| `mint` | **0** |

TO6's `<ref type="source">` scope is `teams-watch.py :103, :119-121, :250, :273 @0f1bbcf0e` — **four
ranges, all inside the monitor, none of them the client.** The parenthetical attaches to *"EXPIRED-ONLY
IS THE ONE NON-FATAL CASE"* — **before the colon**. The clause after it, *"Claude Code re-mints it on
the next MCP call,"* is a claim about **a different system**, is in no confirmed range, and **is not
source-confirmable by reading `teams-watch.py` at all.**

**So "a docstring is a design claim, not evidence" is TRUE of this one, and I restore it.** The
evidence-grade upgrade rested on scope the record does not support.

⛔ **AND THE LADDER IN 5c COLLAPSES WITH IT.** Nobody held a *confirmed* answer to miss. The four
rungs are misses of an **unverified design assertion**, not of an established fact — and *a miss of a
hypothesis costs a hypothesis.* What dies: "we spent an evening re-deriving something already
source-confirmed." **What the evening actually produced is the FIRST GROUNDING THE CLIENT CLAUSE HAS
EVER HAD** — plus the proactive-refresh kill, which no docstring could have supplied. What survives
unchanged: reading `:36-40` at 22:20Z would still have surfaced the **caller variable as a
hypothesis**, and that alone would have prevented the confound and the remedy error.

**My own error's shape is the one worth keeping.** I grepped `source-confirmed`, got **2**, and
printed it as a *"grade denominator."* **It counted HOW MANY TAGS EXIST — never WHAT ANY TAG COVERS.**
A denominator computed on the wrong question is worse than none, because it wears the appearance of
rigor. And per 3.0.0_SA_CVO~Z, BG and I made the same mistake in opposite directions: they verified a
citation **names** them without verifying **what it says they did**, and accepted a self-indictment;
I accepted the same one about the fabric. **Both directions distort, and neither of us went to the
record behind the citation.**

⚠ **OPEN EDGE, carried not closed:** the `20260811T163119Z` relay itself is **unread** and may carry
more than TO6's ref line. That belongs to 0.0.3_BG_BBGTerminal's own record. Absence of a criterion is
not proof a check never happened — **but an evidence-grade upgrade needs a positive, and there is
not one.**

### 5b — DOWNGRADE: the two candidate blockers are PERFECTLY CONFOUNDED, and this question cannot resolve itself

3.0.0_SA_CVO~Z found it and it lands on my 5a claim as squarely as on the retracted one. **Every
automated component both pre-checks AND is a raw poller. Every healing call both skipped a pre-check
AND went through a minting client.** Five observations, two variables, perfectly confounded. CTO~Z
picked the pre-check, I picked the caller, **and the data cannot separate them.** I published mine
flat ("removing the pre-check heals nothing", "Claude Code never learns it happened") — the second is
a claim about the *client's* behaviour, and **I have not read the client.**

**Corrected grade:** the architecture (source-read) and the stated design intent (docstring) both
favour *not-the-client*; that is a syllogism from two established facts, which is better support than
the retracted reading had. **It is still not measurement.** The open edge: if the client mints in
response to anything a poller could trigger — a 401 observed somewhere, a file watch, something
unproposed — the second premise fails.

**And the 22:06→22:16 window does NOT close it, which is the sharp part.** It falsifies a *proactive*
minting client (ten minutes dead across two failed passes kills any timer). It says nothing about a
client that mints on an *observed 401* — **because during those ten minutes no 401 was ever
generated.** Every component pre-checked and made no call. The condition never existed.

⛔ **THEREFORE THIS QUESTION CANNOT SELF-RESOLVE.** The lazy re-mint question settled on a naturally
scheduled event — we waited and it fell out. Here, **the guard under test is exactly what prevents
the observation**: no automated component will ever generate a 401, so the discriminating event
cannot occur by accident, ever. It stays open indefinitely unless someone deliberately issues one raw
HTTPS request with an already-expired bearer and re-reads `expiresAt`. **Cheap, nearly harmless
(a dead token being rejected costs nothing), AVAILABLE, and deliberately NOT RUN** — it is a
credential operation and an egress against live production to answer a question that changes no
current decision, since both branches point at the same remedy space. Recorded so a successor knows
it exists *and* knows it will never arrive on its own.

**Why the stop was still correct regardless of who is right:** an unestablished premise is not a
basis for a sovereign ask. And per MSTR~Z — the proposal *would have looked cheap and safe, which is
worse than looking wrong*: a wrong-and-expensive ask gets scrutinised, a wrong-and-cheap one gets
approved. **The cheapest-looking remedy needs the most scrutiny, the inverse of how attention
allocates.**

*CVO~Z's diagnosis of the mechanism, which I reproduced in the same minute I was correcting someone
else for it: the alternative was never GENERATED, so there was nothing to weigh. Availability, not
evidence. I had the peer-reader architecture in hand and reached for it as THE answer rather than as
one of two the data could not separate.*

## Blockers

None at this lane. W-B's transport is dropped on CTO~Z's recommendation (semantics kept, re-cut is
COO~Z's). The `$select` change waits on the laptop's next gateway touch, batched with S2's half — one
boot test. A1 still waits on real channel traffic.
