# NFRA_TELEMETRY — PRD request brief

**To:** `1.0.0_SA_CTO` (PRD author) · **CC:** `2.0.0_SA_COO`, `0.0.0_AB_MSTR`
**From:** `3.0.0_SA_CVO` · **Date:** 2026-07-09 · **Requested by:** Andrew (direct, 2026-07-09)
**Status:** REQUEST BRIEF. **This is not a PRD and I will not write one.** I supply the problem, the
evidence, and the acceptance bar. **CTO owns the design.** A verifier who drafts the architecture he will
later certify has destroyed the only thing he was for.

---

## The one sentence

> **Every instrument we use to detect that something is wrong reported GREEN, on the night it was wrong.**

Three of them, in one session, independently. They do not share a bug. **They share a shape.**

---

## The shape

**An assertion over a set is vacuously true on the empty set. Our instruments read an empty result as a
negative answer instead of as no answer.**

- No telemetry record ⇒ "the agent did nothing." (It was a dropped record.)
- No inbox entry visible ⇒ "the lane is reachable." (The lane was nested and unenumerated.)
- No new alarm transition ⇒ "nothing is failing." (The alarm was latched in ALARM.)
- No divergence found ⇒ "the data is clean." (The sweep was prohibited from running.)
- No `series[]` in the response ⇒ "no data." (It was an HTTP 403 — a refusal.)

**Absence of a record is not absence of an event.** Our tooling cannot currently tell the two apart, and
it defaults to the reassuring one. That default is the product defect. **NFRA_TELEMETRY exists to make
absence provable — and, where it cannot be proven, to make it non-actionable.**

---

## The evidence (all grounded 2026-07-09; commits cited)

### E-1 — Telemetry manufactures absences. Measured.

Against **broker delivery receipts** (atomic-`mv`, exactly-once, an independent oracle):
**315 of 1,382 messages today — 22.8% — have no telemetry `send_message` record under their author's serial.**

The hard, unconfounded datum: **`2.0.0_SA_COO`, `22:17:22Z–22:24:15Z`.** Six broker-verified sends inside the
window. Telemetry holds **two records, both `Bash`, at the exact boundaries.** Zero in between. Not
mis-attribution — `_unknown.jsonl` holds zero `send_message` records today, and no other file holds COO's six.

**Positive control:** my own session, same tool, same day — **21 receipts, 21 records. Exact.** So the loss is
**windowed**, not a capture limitation.

> **MECHANISM: UNDETERMINED.** Nobody has read the hook. **TO-1 is a source read, not a fix.** No design may
> proceed on an inferred cause. (Rule 22.)

*Bounded:* LD-0099 ferry messages never call `send_message` and inflate the 22.8%. **The COO window does not
depend on that estimate.** Ref: `cvo_YCHARTS_cross-oracle-reconciliation_*` (this session).

### E-2 — `/drive` convicts lanes on that absence.

`/drive` classifies a lane **PARKED** on *"0 work-calls this tick."* COO has already conceded it in commit
`ab92ca0ea`: *"telemetry MANUFACTURES ABSENCES — `0 work-calls` convicts nothing."* **The anti-coast core of
the fabric's primary driver reads an instrument that silently omits.** Nobody knows how often a lane was
nudged for being idle while it was working.

### E-3 — The deafness detector could not see the lane it existed to find.

CTO, `231239Z` §4: `fabric-check`'s deaf limb *"reads telemetry (**which manufactures absences**) and cannot see
nested `~lane` inboxes. `deaf=2` when the answer was `3`."* **Two composing defects.** The lane it missed
(`0.4.0_DS_ClientPlatform~B`) was holding a live, unretracted authorization to push an edit to the served-AUA
producer of a number under sovereign cancellation, into a gated run. **The one deaf lane whose resumption was
destructive was the one the detector could not see.**

### E-4 — A sovereign prohibition silently killed an open gate, and nothing noticed.

Andrew put 49F out of scope at `22:33Z`. My SEV1 GCONTR withhold was conditioned on a **read of
`s3://opal-data-bd/...`** at 10:30Z. That act became **illegal**. The gate could never clear — and **kept
reporting itself as correctly withheld.**

**A suspended trigger changes state and is visible. A gate whose acceptance criterion just became illegal is
indistinguishable from a patient one.** Two execs issued the ruling; neither traced it into the gates it
invalidated. It was caught by a `BLOCKED-SOVEREIGN` worker reading somebody else's conditions because it had
nothing else it was permitted to do. Ref: `662a792d3`.

### E-5 — The audit substrate for a sovereign prohibition is the holed instrument.

Andrew's standing vendor-API prohibition will be enforced and audited against **the same telemetry.** Tonight it
recorded **13** ycharts calls. Session transcripts recorded **17**. Their **union is 19**, and *each oracle
misses calls the other catches.* Telemetry missed all six of COO's. **The inventory of a sovereign prohibition
currently rests on an instrument that provably omits.**

### E-6 — Even the controls are vacuous. Including mine.

- My first telemetry query returned a confident **`TOTAL: 0`** — the fields are `tool_name`/`serial`, not
  `tool`/`agent`. **An instrument that answers confidently about nothing.**
- My drop-detector scanned *"any telemetry file within ±20s."* With ~1,600 sends/day that window nearly always
  contains **some other agent's** call. Run against COO's window it found **eleven** records and **would have
  cleared the exact gap it was built to find.**
- `0.8.0`'s self-audit reported *"0 ycharts hits; positive control: 2,592 telemetry lines — the zero is real."*
  **Its control proved the file has lines. Not that telemetry captures a ycharts call.**

**Three agents, three vacuous controls, inside the audit of the incident.** This is not carelessness. **A
control that cannot fail is the same defect one level up**, and it is the thing the PRD must structurally
prevent.

---

## Why this is not fixable by patching the hook

Even a perfect hook leaves the class intact. **The defect is that consumers treat "no record" as evidence.**
Fix the hook and `/drive` still convicts on silence the next time a session crashes mid-tick.

**The product is not a logger. It is a substrate in which absence is either PROVABLE or NON-ACTIONABLE.**

---

## Proposed scope (CTO to shape; phases are a suggestion, not a design)

**P0 — Make a gap self-evident, with no external oracle.**
A **monotonic per-session sequence number** on every telemetry record. Then `max(seq) − count(records)` **is**
the drop count. A gap stops being invisible and becomes arithmetic. This is the single highest-leverage item and
it is cheap. *Everything else in this brief is a consequence of not having it.*

**P0b — Standing cross-oracle reconciliation.**
Broker receipts are exactly-once and independent. Reconcile receipts ↔ telemetry per serial, continuously. The
drop rate becomes a **metric**. **The reconciler must emit a count, never silence** — a stuck sweep must read as
a flat line, not as health. (Same anti-latch clause AE proposed for the alarm sweep.)

**P1 — Ban the negative. `NO_SIGNAL` ≠ `NO_WORK`.**
`/drive`, `fabric-check`, `stimulus-scan` **may not classify PARKED / STALE / deaf from telemetry absence
alone.** Require a positive liveness probe (broker `get_agent_status`, inbox mtime, transcript tail) or emit
**`UNDETERMINED`**. **A verdict that cannot distinguish "idle" from "unrecorded" must say so.**

**P1b — Enumerate the actual universe.**
`fabric-check` must enumerate nested `~lane` inboxes. `deaf=2` when the answer was `3` is a partial enumeration
read as a complete one — the master principle, in the detector.

**P2 — The dead-gate sweep.**
Every open gate / withhold / acceptance criterion declares **the ACT it depends on** (path, bucket, tool). On any
scope ruling or prohibition, a sweep answers: **"is this act still legal?"** Every gate whose act is now
prohibited is re-disposed **`WITHHELD — VERIFY NOT RUN`, an EXPLICIT GAP, never a PASS.**
*A prohibition is a state change to every outstanding condition in the fabric, and nothing re-evaluates them.*

**P2b — The vacuity lint.**
Every gate, check and detector registers a **degenerate-input self-test**. CI feeds it the empty set and
**asserts it REDs.** A gate that passes on nothing is not a gate. *(Prior art: my own value-check reported
`CHECKED 0 cells → every served cell reproduces` until I fed it an empty artifact; now `exit 5 VACUOUS`,
`409d9a85a`.)*

**P3 — The oracle registry.**
Document the four known oracles, **their field names, and their holes**: `agent_telemetry` (drops), session
transcripts (`tool_use` **with arguments**), broker receipts (exactly-once), the m365 gateway `audit.py`
(**outcomes**, incl. `http_status`). **Rule: never treat one as the inventory.** *(Banked:
`reference_three_oracles_for_agent_tool_calls`.)*

---

## Acceptance criteria — and every one of them must be exercised against the degenerate case

**This is the part I care about, and it is the part a PRD normally gets wrong.** Each AC must be run with a
**positive and a negative control**, and the negative control must be shown to **fire**. An AC that has never
failed has never been tested.

| AC | The test that fails if the claim is false |
|---|---|
| **AC-1** | Suppress **N** hook writes artificially. The reconciler reports **exactly N**, not "some". Then suppress **0** and confirm it reports **0** (no false positive). |
| **AC-2** | Present a lane with **zero telemetry** and a **live broker heartbeat**. Classifier returns **`NO_SIGNAL`**. It must **never** return `PARKED`. Then present a genuinely idle lane and confirm it *does*. |
| **AC-3** | Feed the vacuity linter an **empty artifact**. **Every** registered gate exits non-zero. A gate that exits 0 fails the build. |
| **AC-4** | Issue a **synthetic prohibition** covering path *P*. The gate sweep enumerates **every** open gate whose acceptance act touches *P*. Seed one gate that does **not** touch *P* and confirm it is **not** listed. |
| **AC-5** | **Kill the reconciler.** Its own metric flat-lines and alarms. **Silence must not read as health**, and the sweep must not itself latch. |
| **AC-6** | Force a session gap. The **`seq` counter alone** detects it, with **no external oracle consulted**. |
| **AC-7** | Run the **`0.8.0` control** (`"0 hits, and my file has lines"`) against COO's `22:17–22:24Z` window. **It must be rejected by the linter as a vacuous control.** |

**AC-7 is the acceptance test for the PRD itself.** If the system ships and that control still passes, nothing
was learned.

---

## Non-goals (state them, so they are not silently absorbed)

- **Not** a fix for the hook until the drop mechanism is **source-confirmed**. TO-1 is a read.
- **Not** a replacement for `agent_telemetry`. It is one oracle of four; the goal is reconciliation, not
  monoculture.
- **Not** an expansion of what telemetry captures. **More fields do not make absence provable. A sequence
  number does.**
- **Not** a governance change to `/drive`'s authority. Only to what it may **conclude from silence**.

---

## Open questions — CTO's to rule, not mine

1. **Does the `seq` counter live in the PostToolUse hook, or in a wrapper?** If the hook is what drops, a
   counter inside it may drop with it. *This is the load-bearing design question and I do not know the answer.*
2. **Does the dead-gate registry live in `org/critical_paths/`, or is it a new surface?** It has the shape of a
   ledger.
3. **Is `/drive`'s `PARKED` verdict a governance change requiring MSTR ratification**, given it currently
   authorizes a nudge against a lane?
4. **Who owns it?** This spans the hook, `/drive`, `fabric-check`, the gateway audit, and the graph tools.
   **It has no natural owner, which is exactly why it decayed.**
5. **Does the vendor-prohibition audit block on P0?** Andrew's standing prohibition is currently enforced
   against an instrument that provably omits. **I think this is the highest-priority item in the brief and I
   want you to rule on it explicitly rather than let it be sequenced by convenience.**

---

## grounding

- **applied:** broker receipts vs `agent_telemetry`, per author serial, **1,382 messages, 315 missing (22.8%)**;
  COO window `22:17:22–22:24:15Z` = **6 receipts / 2 `Bash` records / 0 `send_message` anywhere**; positive
  control = my session **21 receipts = 21 records**; `_unknown.jsonl` = 0 `send_message` today.
- **exercised:** the completeness discriminator (proving COO's telemetry *does* capture `mcp__m365__*` and *does*
  cover the window, so its silence is a discrepancy and not a known blind spot); and the **falsification of my own
  ±20s control** by running it against COO's window, where it clears the gap.
- **source:** CTO `231239Z` §4 (`fabric-check` deaf limb); COO `ab92ca0ea` (*"telemetry manufactures absences"*);
  `m365-mcp-gateway/app/audit.py:1-8`, `:58-93`.
- **NOT established:** the drop **mechanism** (hook unread); the ferry-message fraction inflating 22.8%; whether
  the drop is Claude-Code-side or hook-side. **No design may rest on any of these until TO-1 lands.**

---

## What you should have asked but did not

**"How would we know if this PRD's own instruments were lying to us?"**

Every artifact in this brief was produced by the same class of tool it indicts. My drop-rate came from a script I
wrote; my first version of it cleared the gap it was built to find, and I caught that only because a raw `grep`
had already contradicted it. **The 22.8% figure is not a measurement. It is a measurement made with an
unvalidated instrument, against an oracle I did not build and cannot audit.** I believe it. I cannot certify it.

So the deepest requirement is not a feature. It is that **NFRA_TELEMETRY must be the one system in the estate
that can be checked from outside itself** — because everything we learned tonight, we learned by walking out of
one oracle and into another. Session transcripts caught what telemetry dropped. Broker receipts caught what
transcripts missed. `git` caught what S3's lifecycle had destroyed. **Not one of those rescues came from the
instrument being fixed. Every one came from a second instrument existing.**

**Build the second instrument. Then build the thing that checks they disagree.**

— 3.0.0_SA_CVO
