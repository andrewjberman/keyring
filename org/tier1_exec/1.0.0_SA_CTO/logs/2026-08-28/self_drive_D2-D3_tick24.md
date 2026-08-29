# /self-drive D2 & D3 — tick 24 (2026-08-28 23:20Z) — state: ARMED

Covers tick 24 (tick 23 logged @14b5b0116d). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: a ruling of this seat's was WRONG at
its premise and broke a scheduled production run for ~10 minutes; the rollback, the corrective
ruling, the starter census, and the record of the error are below. Also: every computable row of
the PERFRP rewrite accepted at three seats.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## THE ERROR (this seat's), the rollback, and the corrective ruling (§3.3)

- **What broke.** Tick 20's ruling 79107/79117 disabled `gold-layer-runner.service` on the shared
  runner i-01003b035d2988dfb (APPLIED 21:04Z, SSM bba44ddd) on the premise that the boot-started
  `chain:full` was "an UNREQUESTED SECOND WRITER the campaign never invoked". **FALSE, measured by
  ~L at 23:0xZ (79518):** `bd-gold-trigger` (`bd-daily-trigger-lambda-role`) started the host on
  schedule at 23:00:30Z and dispatched NOTHING — the trigger only powers the box on; the boot unit
  IS the execution half of Black Diamond's scheduled nightly (corroborated by the 08-27 23:00 boot,
  1h53m50s). Tonight's 23:00:38Z boot came up with the unit disabled: `journalctl -b 0 -u
  gold-layer-runner.service` = "No entries", `is-active` inactive, zero chain processes. **BD's
  2026-08-28 nightly gold run did not start, and the cause was this seat's ruling.**
- **Rollback (~L, before escalating):** SSM c81ed72b rc=0, `is-enabled` disabled -> enabled — a
  pure reversal of its own act. Re-enable binds from the NEXT boot only; tonight's run was still
  missing, so ~L escalated for one word: start it by hand on this boot, or accept a missed
  production run.
- **RULED (A) (79523/79524/79525, 23:0xZ): start the unit on THIS boot.** A backfill is never
  worth a missed production night (the campaign's own doctrine). **EXECUTED (~L 79526):** SSM
  fecefc73 at 23:08:5xZ; the unit is Type=oneshot so `systemctl start` BLOCKS ~1h53m and its rc is
  not the evidence — confirmed on a SEPARATE read at 23:10:39Z: `is-active` activating; pids
  4390/4523/4530 running `gold_dispatch.sh --chain full`; unit log "Spine: 12,445,982 rows
  (2020-03-06 -> 2026-08-28)", 11,300 assets / 16 workers. BD's nightly RUNNING ~10 min late;
  finish ~01:0xZ. COO CONCURRED (79529). CVO filed it (79536 @bd1cee89f3) as **BLOCKING — ARMED
  23:07Z, DISARMED same-turn by a named owner, REMEDIATED only when the nightly FINISHES** (CVO
  reads then; DISARMED != REMEDIATED).
- **Consequences ruled:** NO further disable/mask/edit of that unit or its script for the
  campaign's duration; the per-boot `shutdown -c` race stays rejected; the campaign ACCEPTS the
  ~1h53m ceiling on every boot and absorbs each halt on the proven path. Row 7 (n) REFRAMED (COO's
  carrier, this turn): not "should a boot-started chain:full exist" — it is BD's nightly's execution
  half by design — but (a) a boot-time unit runs a FULL production chain on EVERY start incl. ad-hoc
  and campaign resumes (a trigger that only powers the box on cannot tell the unit WHY it is up);
  (b) fabric item 12, the `/tmp/run-gold-layer-new.sh` the unit actually runs; (c) the STARTER
  INVENTORY as a standing fact on the substrate card (row 2 cadence/trigger; row 6 identity).
- **THE STARTER CENSUS (~L 79526; the read whose absence made the ruling possible; one
  command):** CloudTrail StartInstances on the runner 2026-08-26 -> now, DENOMINATOR 14 events:
  `bd-daily-trigger-lambda-role` 5 — **23:00:30Z AND 04:00:25Z, TWICE DAILY, both nights to the
  second**; `advi-49f-gold-dispatch-role` 4 (12:45:16Z); `Andrew_Berman` 5 (08-27 x2; 08-28 the
  driver's two resumes + ~L's forensic start). THREE scheduled starters, every one running a full
  ~1h53m chain via the boot unit. The disable would have broken the 04:00 run too.
- **Owned, at grain.** The premise was this seat's: written from the ~1h53m PATTERN and from
  CVO's bucket read, with the nine-boot table in front of me showing 04:00Z and 23:00Z boots that
  were nobody's in the story — and I never asked what STARTED them. ~L had asked for exactly that
  in 79088 ("needs an owner who is not me"); I ruled past it. CVO's refinement (79536) is correct
  and adopted: its bucket read answered "does the boot chain write into the 49F bucket" (NO,
  520/520, structural) and was never evidence for "unrequested" — I cited it beyond its question.
  COO owned its concurrence (79529). What kept the record honest was ~L's rung discipline: APPLIED
  was true, EXERCISED was never claimed, and the premise failed in between. **Memory written:**
  `feedback_enumerate_the_starters_before_disabling_the_started.md` — *a boot you cannot attribute
  is a starter you have not found, not an ad-hoc start.*
- **Halt #3** (boot -1 died 22:45:24Z, INSIDE ~L's predicted 22:40:57-22:45:57Z window; the
  command had started, Failed rc=1 after 1011.6 s; 2025-04-04 re-driven clean at 23:03:30Z)
  confirms the MECHANISM a third time — nothing about the cause is withdrawn, only the remedy.

## Campaign (D2 critical path)

**198 of 534 at 23:20Z** (newest 2025-04-17; last write 23:19:03Z ARTIFACT-COMPLETE), driver live
(task bfvbh85eq) on the 23:00:38Z boot beside BD's running nightly. Predicted halts: ~01:0xZ (the
nightly arms its shutdown), ~03:0xZ (if resumed immediately, the resume boot's own chain), ~05:53Z
(the 04:00:25Z bd-daily boot). 342 dates x ~110 s = ~10.5 h of driving -> **the 12:45Z pre-fire
PAUSE is now the likely operative boundary, not completion** — the price of this seat's ruling; ~L
re-derives from the ledger at the date-200 read (2 dates away) and names which boundary arrives.
The 04:35Z INSURE fire is a Lambda chain, not a process on this runner — unaffected (CVO 79536).

## PERFRP round 2 (issuer plane, no CTO act this tick)

Every computable row of TO-R2-DS ACCEPTED at three seats: AC8 VALID (@8100db4ce2 ~V; COO's seat;
CVO's seat), AC3 part 2 CLOSED @160ab97c36 on this seat's named set (identity (i) 0 of 10,076; (ii)
0 of 146; 0 bare of 60,456 — CVO re-derived from the leaf), AC5 re-emission @c118a8e4d7 (0 bare of
80,088; tie-out unchanged; COO closed on its OWN census at the new mtimes after catching the
instance's PASS scored against the OLD files), AC4 trim closed with both PII controls RE-RUN on the
trimmed projection (this seat's 79356 condition met); instance VALID under ENFORCE 11/11 (COO),
re-cut @c93acc2f76 VALID (CVO). Remaining: AC6 (ledger 534/534), AC7 (round close). DE~D binds
gain/loss and reads AC6 on the b-6 re-emission. ~V's keeper (adopted): both misses were arms that
checked the artifact against ITSELF and never asked whether the consumer-rejectable fields were
present; one of its arms went stale against a ruling and was NARROWED, not deleted.

## Standing obligation (carried)

**05:07Z 2026-08-29 tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO
79396): list `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped
>= 04:52Z carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @6a5dd1cfab, ls-remote read 23:20Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read (outcome-filtered) · `git ls-remote` + MERGE_HEAD · `ack_messages`
  (79493-79536 as received) · `send_message` to_agents (79523-79525; 3 of 3 DELIVERED) · memory
  Write + MEMORY.md index (python append preserving LF).
