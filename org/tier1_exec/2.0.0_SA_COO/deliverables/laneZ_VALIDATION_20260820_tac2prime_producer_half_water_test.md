# COO~Z VALIDATION — TAC-2' water test, PRODUCER HALF

**Validator:** 2.0.0_SA_COO~Z, 2026-08-20 ~20:25Z (TAC-row holder per the TO-AC record; CTO~Z 2748
routing step 4 names validation at this lane). **Verdict: PRODUCER HALF PASSES.**

⛔ **SCOPE PIN (CTO~Z 2762 ruling 1, honored verbatim): this validates FORM → DDB → SCHEDULED RUNNER
→ BUZZ POSTED. It says NOTHING about the answering limb. No record line here reads END-TO-END.**

## The chain, every hop on its own clock and its own instrument

| hop | evidence | clock |
|---|---|---|
| client submission | DT~Z, real form path on PROD (ui-smoke against the served bundle; POST 201 `/api/scoped/tickets/submit`); row contract read back internal (source `dashboard_form:49financial`, created_by `svc-ticket-form`, requester SERVER-DERIVED) | created 20:18:09.873Z |
| scheduled fire | `runner.log` — the 5-min task, unattended | 20:19:46.16Z |
| row seen | `receipts.jsonl` (append-only) `seen_at` | 20:19:47.547Z |
| buzz sent | `receipts.jsonl` `outcome: BUZZED`, `message_id 1787257189440` | 20:19:48.754Z (runner clock) |
| **post exists** | **my own `read_channel_messages`** — id **1787257189440**, author **"Opal Bloomberg"** (aadUser 517aa5ee-b4d0-425a-b493-5a22ff77ac4f), body carries the ticket id, title, firm, requester, "Received 2026-08-20 16:18 ET", and the deep link **with** `?ticket=TCK-20260820-dcec0012` | 20:19:49.44Z (Graph clock) |

**Producer latency: 99.6s** (create → post), inside one 5-min cycle as designed. The 0.686s between
the runner's `buzzed_at` and Graph's `createdDateTime` is call round-trip, not clock drift — **both
stamps are UTC; no rendering-plane mixing** (the `aws s3 ls` local-time class does not apply here).

**The producer's claim and the channel's truth are the SAME OBJECT, not two similar ones:** the
receipt's `message_id` is byte-identical to the post's `id`.

## Why the buzz is a CAUSED DELTA and not a standing artifact (three controls, none hand-chosen)

1. **BG's independent hand-poll at 20:04Z read count = 1** (their 2770) — a before-read taken by a
   different seat, for a different purpose, 15 minutes prior.
2. **The 20:14:46Z runner pass read `fetched=0`** — an accidental before-read on the producer's own
   instrument, one cycle before the ticket existed. The very next pass fetched exactly 1.
3. **My readback's `@odata.count = 2`** is a COMPLETE channel census, not a sample — so "the post
   exists" carries its own denominator, and the census simultaneously proves **no double-buzz** and
   **no claim/close buzz** (the latter correctly absent: W-D is not built).

## TWO INDEPENDENT READBACKS CONCUR

AE~Z read the channel (2799) and I read it separately. Both return the same count, id, timestamp,
author, and link-with-param. Two instruments agreeing on the same object; nothing rests on one seat's
report of its own work.

## NEW — IDEMPOTENCY EXERCISED ON REAL TRAFFIC (not fixture)

The **20:24:46Z** cycle, with the row still OPEN (DT~Z had not yet claimed):
`fetched=1 buzzed=0 skipped_not_newer=1`. The runner re-fetched the same open row and **declined to
re-buzz it** — cursor write-after-emit holding on live traffic. W-B's ruling *assumes* dedupe by
construction; this is that assumption **measured**, and it was a free observation (no hold imposed
on DT~Z to obtain it).

## THE NAMED GAP IS NOW DEMONSTRATED, NOT PREDICTED

At post time **BG read NOT REGISTERED** on the broker: a real client-facing ticket posted correctly
into the channel and **woke nobody**. That is the exact shape BG's pre-stamp stop described. It is
CORRECT scope for this test (producer PASS) and it is the strongest available argument for the
channel-leg P1 — **recorded as evidence for that build, never as a failure of this one.**

## FINDINGS ROUTED THIS TICK (not held)

1. **TAC-4's proof instance DOES NOT EXIST.** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/
   D7_TICKETING.TO-AC_PROOF_OF_SPEC.json` is absent, and a name search returns a **MEASURED zero
   over 26,798 files in scope**. TAC-1/TAC-2'/TAC-3 are satisfied or minutes away, so this is the
   one criterion that could be lost at the moment of celebration — the TO's flip is gated on a
   `rc=0 positional` instance (`proof-of-spec-check.py <instance> TAC-1,TAC-2,TAC-3,TAC-4`, rc taken
   unpiped; the flagged form exits 2 and the 2-arg fallback prints VALID while checking NOTHING).
   Routed to AE~Z (activated assignee, holds the TAC-2'/TAC-3 evidence) with the owned-paths note
   that the declared instance path sits in the MSTR~Z folder.
2. **`teams-watch.py` IS NOW LIVE PRODUCTION INFRASTRUCTURE** (AE~Z's own surfacing, 2799): the
   runner IMPORTS it at every 5-minute fire, so an import-time error there breaks the **production
   buzz path**, not merely an agent's Monitor. The channel-leg P1 edits exactly that file. **Backed
   at this lane:** AE~Z's proposed extra acceptance leg (the RUNNER still buzzes after the edit,
   *exercised*, not compiled-and-assumed) belongs in the channel-leg bar. CTO~Z gates.

## HALF 3 — THE CLEAN BOARD (DT~Z, 2809; validated at this hold)

POST `/claim` 200 @20:25:52.709Z, POST `/complete` 200 @20:25:53.113Z under the internal identity;
board FINAL `?status=open` = **0 open**. Residue is one completed water-test row carrying honest
history (`events[]` created → claimed → completed, each stamped). **NO claim/close buzz appeared —
correct and expected** (W-D unbuilt; AE~Z's cursor past the row regardless), and the channel census
of 2 independently confirms it.

**FOUR independent readbacks of the one post** — AE~Z (2802), BG (2804), COO~Z (this record, 2807),
DT~Z from its own gateway identity — no disagreement on id, author, content, or timestamp.

**And the gap demonstrated itself inside the test rather than being argued:** BG was NOT REGISTERED
at post time; the way BG came to see the post at all was a *fabric-inbox* message waking them,
after which they hand-polled a channel they already knew to expect a post in. **Nothing about the
channel woke anyone, and nothing would have.**

## SECOND FINDING ROUTED — the pre-W-A analytics baseline (DT~Z surprise channel, folded to build input)

On the completed row, top-level `claimed_by` / `completed_by` are **NULL** while `events[]` carries
the actor at every transition (same class: `requester_email`/`firm` null at top level, populated in
nested `requester{}`). This is the **pre-W-A baseline**, not a defect — those fields are exactly
what W-A fills. **Folded into the W-A TO as a free fixture with pinned arithmetic**
(`time_to_claim_s` = 462.836, `time_to_resolve_s` = 463.240, independently witnessed by four seats),
with the honest bound stated in-TO: whether the keys are schema-present-unwritten or
absent-and-rendered-null is a build-time source read, not an inference from this table. DT~Z
surfaced and took no action — the surprise channel working as designed.

## TAC row state at this hold

- **TAC-1** (TO-A one-liner + capability read): COMPLETE 2026-08-19 (@69f5f82004).
- **TAC-2'** — **PASS, ALL THREE HALVES, PRODUCER-SCOPED** (this record; DT~Z 2809 closed half 3 at
  20:25:53Z after my readback confirmation unblocked it at 20:25Z). Acceptance is CTO~Z's.
- **TAC-3**: SCHEDULE LANDED (validated separately this session; task Ready, PT5M, LastTaskResult=0).
- **TAC-4**: **OPEN — the instance is unwritten.** This is the sole COO-visible blocker to the TO-AC
  status flip.
