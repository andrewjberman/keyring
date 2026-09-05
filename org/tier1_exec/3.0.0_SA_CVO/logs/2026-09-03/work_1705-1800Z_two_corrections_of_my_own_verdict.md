# 3.0.0_SA_CVO~Z -- work log 2026-09-03 17:05-18:00Z: two corrections of this seat's own verdict

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake + the standing tie-break. **Prior log:** `work_1555-1705Z_*`.
**Push state as read:** local HEAD 5f15f2874b; origin/SITEZ 001709c96e at 17:04Z, so this seat's commits are
LOCAL and travel in the integrator's window. **Loops:** none armed here, and none anywhere at this seat's
request -- see s.1.

## 1. Two law edits, neither touching this seat's limbs

**MSTR can no longer write a Tier-2 seat** (Andrew-direct ~17:0xZ, @fa36d2fc8f, gate live at the tool layer).
Provoked by a Tier-0 seat sending a worker directly and routing around its issuer -- right content, wrong lane,
and the correct path was already in use, which is what made it worth a gate. Scoped to MSTR; this seat's sends
to Tier-1 are unaffected and were already refused toward Tier-2 by `cvo_send_guard.py`.

**Andrew killed the /govern loop** ("kill govern loop", ~17:3xZ, @9dc9c979a0): the cron deleted AND the durable
Step 1b-F clause struck, because the cron dies with a session and the row would have re-armed the next seat.
**The four-project sequence is NOT retracted** -- what ended is the cadence that paced it. Nothing about
NFRA_OPSEC202609, the spine, or this seat's limbs changes.

## 2. My word on the `attempted_at` proposal, and a re-send that taught something

19884 put a ledger-contract item to this seat and the integrator: `proof: null` is ambiguous between "not done"
and "done, not written", and an `attempted_at` stamp would close it. **My word: YES, with one condition that is
the whole difference -- the stamp must be WRITE-AHEAD.** A stamp written after the act shares the failure mode
it exists to remove, because the seat that dies between the act and its proof is the seat that dies between the
act and its stamp, and both read null for the same reason. Stated without overclaiming from today's case, which
does not discriminate: the worker had ~40 minutes after applying and wrote nothing on those legs. The argument
is about shape, not instance. Write-ahead yields three states where there were two.

**And the mirror half no stamp reaches**, already on the channel at Z-S47: the same ledger closed a leg against
a two-artifact target while citing a commit carrying one. `attempted_at` plus a close-time target check is the
minimum pair that makes the record self-checking in both directions.

**The re-send, worth banking:** 19887's per-recipient receipt read DELIVERED via filesystem, broker and channel
push, and the integrator lost the tool result before reading it and asked for a re-send. **A delivery receipt
proves the push and never the readership** -- the sender-side mirror of the QUEUED rule this fabric already
banks, and exactly why the ACK clock exists. Re-sent in full rather than summarised, because a partial re-send
drops the part nobody knows is missing.

## 3. Rows filed this window

- **Z-S50 @2797f3f314 (ARMED)** -- 19867's false-absence finding CONFIRMED, and its cause is structural as well
  as lexical: **two committed credential homes**, one in the superproject and one inside the portal SUBMODULE
  holding three credentials, **each invisible to the instrument that finds the other**. A superproject search
  returns 0 for the submodule home by construction (`git` answers "Pathspec is in submodule"), and the memory
  corpus points ONLY at the submodule one -- 0 of 477 memory files name the sanctioned path, so its own header's
  claim to be "the ONE structured home" is false on this device. Disarm is one sentence in either home naming the
  other. **No credential value was read at any point** -- key names, comment lines, path existence, tracked status.
- **Z-S52 @50c758b114** -- Z-S49's dilemma DISSOLVES on the spec. C-15 as amended says the access-log target
  FOLLOWS the evidence store and S27 says the same; nothing in C-16/S28 asks for access logging ON the log
  destination. So the target serves exactly one source before and after and the live ArnLike pin is STALE, not
  deliberate. **The fix is to MOVE the pin, not widen it**, and S17R28-AC3 is the narrow clause rather than the
  deliverable being wide. Ordering survives: the re-point lands BEFORE the source's logging block.
- **Z-S57 @d1fc693c71 and Z-S58 @5f15f2874b** -- the two self-corrections, s.4.

## 4. TWO DEFECTS IN MY OWN TICK-6 VERDICT, both caught by workers' pre-write reads

**AMEND D's split was wrong (Z-S53 -> my Z-S57).** I printed the denominator as `39 = 20 non-OPTIONS + 19
OPTIONS`. Measured at this seat on the live plane -- `get-resources --embed methods --limit 500`, no `position`
key so a single complete read, plus an independent per-verb census (GET 12, POST 7, PUT 2, OPTIONS 18) -- it is
**39 = 21 + 18**. The total was right, so every check that verified the total passed; halves wrong in opposite
directions cancel. **Load-bearing:** AMEND D's fallback says the denominator falls to 20, and at 20 a worker
attaches 20 of 21, prints "20 of 20", PASSES, and leaves one real data method unauthenticated. **Root: a GRAIN
MISMATCH.** I never measured the plane. I derived 20 by subtraction and cross-checked it against the decomp
cell's "20 methods" -- which is 20 method-bearing RESOURCES, confirmed exactly 20 by my own read. Two different
quantities sharing a value, in two carriers that agreed with each other and with my arithmetic, none of them the
world.

**AMEND C's bar contradicts itself (Z-S56 -> my Z-S58).** Row (4) requires "0 to add" while the same sentence
names "the in-place body update AND ITS DEPLOYMENT" as expected, and row (2) MANDATES declaring that deployment,
which cannot be imported and must be created. Verified against the ledger's verbatim record rather than the
worker's report. **Worse than the row states, which makes the fix clearer:** THREE of my clauses expect the
create -- rows (2) and (4), plus AMEND D's S1-AC3 requiring a NEW deploymentId on BOTH stages -- and exactly ONE
forbids it. **Root: a bar transplanted across a premise it no longer fits.** Z-S14's "0 to add" was written for a
PURE import where nothing is created and is right there; this adoption necessarily creates the deployment that
makes the imported body serve. **Corrected bar:** 0 add and 0 destroy AMONG THE IMPORTED OBJECTS, no
forces-replacement anywhere, and exactly three named expected changes -- the body update, the deployment CREATE,
and the provider default_tags on both stages that my bar named nowhere (the ~S face's S8R2-AC1 had already set
that pattern on this project). Release is the issuer's word, not mine.

**THE TWO ARE THE SAME ERROR AT DIFFERENT LEVELS:** a figure moved carriers and its GRAIN was never re-checked;
a rule moved cells and its PREMISE was never re-checked. Both were mine, both were caught by a worker's mandated
pre-write read, and in both cases the worker refused to substitute its own reading into a frozen face and asked
instead -- which is exactly the behaviour those bars exist to produce. Neither cost an act: one was caught before
limb 2, the other with the apply held.

## 5. State at close

Channel 58 rows. **Resolved-live ARMED: 4** -- Z-S50 (credential homes, CTO's), Z-S53 and Z-S58/Z-S57 (the two
verdict corrections, the issuer's on the face and the driver's on the ledger row), Z-S56 (the held apply). Note
the raw `hazard_standing` field reads ARMED on 22 rows; the channel is append-only so a disarm lands as a LATER
row, and the raw count overstates open risk by roughly five to one. **The resolved read is the one L9 will need.**

Two memories banked this window: the delivery-receipt/readership mirror (added to the existing QUEUED item), and
**two carriers agreeing on a number may be measuring different things** -- a partition is never verified by
checking its total.

**Still owed and still blocked:** the four round-1 closure rows. Gate here still `c3ef3a2530`; the ruled arm
arrives with the leg, which is assess-only with the site not quiet and the push declined at Andrew's terminal.
