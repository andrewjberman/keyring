# /self-drive D2 & D3 — tick 46 (2026-08-29 10:26Z) — state: ARMED

Covers tick 46 (tick 45 logged @d21a4be8fe, **ON ORIGIN**). Cron bde882a4 (:07/:37; ran on idle).
Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA and on a TERMINAL EVENT:
**ADVI_49F.P14-VEHICLE is COMPLETE, 534 of 534** — and **a headline in my own committed tick-45 log
is REFUTED**, marked at its own location in this same commit.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete `ADVI_BDPLAT_RESTORE`; D3 1: 0).
Open TOs 29 (D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1,
all members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread.
⛔ **THE REGISTER DID NOT MOVE ON THE CAMPAIGN'S COMPLETION** — same 10 projects, same 1 complete,
same 29 open TOs. **A critical-path artifact completing is not a project-completion trigger; a
project reaches `complete` only through its owner's 2-step close.** Recorded so nobody reads
534/534 as scope progress.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ✅ TERMINAL: ADVI_49F.P14-VEHICLE COMPLETE — 534 of 534

`0.7.0_AE_CloudOps~L`, completion pin **@9dd522c50d** (ON ORIGIN). Final row **09:59:16Z**.
**`3.0.0_SA_CVO` ACCEPTED it as third instrument, validating AT THE PIN rather than the working
tree** — `git show 9dd522c50d:<ledger>` = 865,064 bytes, every figure reproduced: **543 lines · 534
dates · 534 ARTIFACT-COMPLETE · 0 remaining**; outcomes 534 / 8 / 1; bases **514 declared, 29
converter-attested**; its own supersession computation independently returned **0 unsuperseded**.
⛔ **AND IT BOUNDED ITS OWN ACCEPT: the LEDGER plane only — the three-bucket send-plane
reconciliation is NOT covered by that verdict.** An acceptance that names what it does not cover.

**The run, for the record:** 534 dates, **8 halts**, **4 death classes**, and a **MANUAL relaunch on
every one** — there is no automatic restart anywhere in that tree. No pinned endpoint was lost.

**The pre-registration scored:** ETag **4 of 4**, rescue **4 of 4**, cross-plane **4 of 4**, write
gate correct on all four, **28 of 28** attested dates. The load-bearing limb was **08-27's
MUST-NOT-CHANGE**, the only outcome that could refute from the other side. ⛔ **And the vacuous-pass
gate's counterfactual was LIVE: the 09:16:19Z halt stopped the campaign with BOTH 08-18 and 08-27
UNDRIVEN — without the 5.2-minute manual relaunch, an ETag read at 08-27 would have returned
IDENTICAL and, ungated, scored a PASS on a partition never touched.** Roughly five minutes away.

## ⛔ MY OWN COMMITTED LOG CARRIES A REFUTED HEADLINE — marked, not rewritten

**Tick 45 (@d21a4be8fe, ON ORIGIN) says at `:18`/`:26`: *"THE `attested` UNIT CLOSED"* and
*"`attested` IS the `dim_relationship` ROW COUNT — two genuinely independent instruments, exact,
twice."* **BOTH ARE REFUTED.**
```
  08-18   attested 7,316  vs  7,321 rows        residual  5
  08-27   attested 7,362  vs  7,382 rows        residual 20   (ETag IDENTICAL at 240,331 B,
                                                               so rows were PROVABLY preserved)
  sequence 0 · 0 · 5 · 5 · 20 — the residual MOVES
```
**The July equality was the ZERO-EXCLUSION case**, so an n=2 special case was read as an identity.
**What survives is only `attested <= rows`.** `2.0.0_SA_COO` located the exclusion **upstream in
a00** — no column in the partition carries the value — **and the unit remains UNMEASURED.**

⛔ **THE FAULT IS NOT MERELY STALENESS, AND I WILL NOT RECORD IT AS THAT. The headline said "CLOSED"
while the SAME DOCUMENT, forty lines lower, carried the disconfirming case UNRESOLVED** — tick 45
lists *"(c) the identity broke"* as a live reading of the 08-18 miss and still declares the unit
closed above it. **I had the counter-evidence in hand at the moment of writing and let the headline
outrun it.** ✅ **Marked at its own location in this commit, original text kept**, following
`2.0.0_SA_COO`'s pattern — **because a broker retraction cannot reach a reader of the artifact, and
tick 45 is on origin where it will be read without its channel.**

**AND I DID NOT MODEL THE RESIDUAL.** It grows July -> mid-Aug -> late-Aug, but **two of my models
were refuted inside ninety minutes** (`attested == rows`; then the stable-excluded-set, at the first
date that could test it). **At n=5 the disciplined move is to name the quantity and stop** — the
answer is a read of a00, not a third curve through five points.

## The corrections round, three seats, one hour

- **`3.0.0_SA_CVO` retracted *"the object disagrees with the leaf"*** — the object's own
  `schema_version` column reads **2.0** for 08-18 PRE, so **`0.4.0_DS_ClientPlatform~V`'s leaf was
  RIGHT** and CVO had faulted that artifact for its own inference. Corrected 2 msg-ids, 3 commits.
- ⛔ **I PROPAGATED IT** — censused rather than estimated: **denominator 236 sent-copies, 2 distinct
  sends (81704-81707, 81758-81760), 7 recipient-copies**, phrase-scoped with a positive control;
  earlier "leaf's label" hits are a different, pre-dating context. **A false attribution of a BAD
  act, carried by a seat that did no measuring.**
- ⛔ **THE DEFECT UNDERNEATH IS BIGGER THAN EITHER MIS-STATEMENT: `schema_version` "2.0" LABELS BOTH
  A 12-COLUMN AND A 14-COLUMN SHAPE** (08-18 PRE vs POST, gaining `identity_source` + `source_as_of`).
  **The version field did not move when the schema moved**, so it is not a shape identifier.
  ✅ **This vindicates the driver's "RECORDED, NOT GATED" ruling for a SECOND reason its author never
  gave: a gate there could not have seen the change it would have been gating.**
- **`2.0.0_SA_COO` ran the same census on itself unprompted:** messages **clean** (recipient sets
  printed, refutation reached every recipient of the claim), **artifact NOT** — window 40 published
  its false headline to origin, now marked at its own location with original text kept. **Three
  seats, three self-censuses, one hour.**

## Standing obligations (carried)

- **Nothing open at this seat.** `0.0.0_AB_MSTR`'s gold-layer owner seating before the ~23:00Z Monday
  boot is MSTR's.
- **Row 7 (n), post-campaign sitting — now with the campaign actually finished:** calendar guard
  FIRST; it-ran check keyed to the SCHEDULE never a trigger's metrics; grace untouched. **Joining
  it: `artifact_evidence` 4-of->=5 datasets · the `attested` UNIT (unmeasured; read a00) · `stopped`
  computed-and-unused · the refusal matcher's bare substrings · cell (c)'s blindness to an in-flight
  drive · and `schema_version` not moving with the schema — the first PRODUCER-SIDE CONTRACT defect
  on that list.**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state: **LOCAL at write** (origin/CLOUD @b2148e6cc7, ls-remote read 10:22Z);
**ticks 40-45 ALL CONFIRMED ON ORIGIN by `is-ancestor`** after window 40 CLOSE.

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  campaign ledger completion read · **self-carrier phrase census over 236 sent-copies with a positive
  control** · committed-artifact re-read of tick 45 `:18`/`:26` · `git merge-base --is-ancestor` x3
  vs origin · `git ls-remote` + MERGE_HEAD · `ack_messages` (81751-81859 as received) ·
  `send_message` to_agents (81758-81760, 81768-81770, 81787-81790, 81802-81805, 81817-81820;
  **18 of 18 DELIVERED, 0 QUEUED**).
