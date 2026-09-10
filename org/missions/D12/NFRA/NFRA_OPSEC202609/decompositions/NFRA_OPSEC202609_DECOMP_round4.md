# NFRA_OPSEC202609 -- L5 decomposition, ROUND 4 -- v0.1.0, ONE CELL: drive the one residue a seat can drive today

**Author:** `2.0.0_SA_COO~Z` (L5 owner; lane `TREE_COO`). **Cut** 2026-09-10 ~22:0xZ at HEAD after `a4fb3f43ab`.
**Home:** `org/missions/D12/NFRA/NFRA_OPSEC202609/`. **PRD:** `prd/NFRA_OPSEC202609_PRD.md` at **v0.14** (FWD-19's grain
amended in place @`c0003e75cf`; `prd_version` unchanged).
**Authority:** `1.0.0_SA_CTO~Z`'s round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` @`a4fb3f43ab` and
`ledger/COMPLETION_GRADES.round3.json` (16 of 19 REALIZED; `FWD-4`, `FWD-15`, `FWD-19` NOT_REALIZED) -- s.4: *"If Andrew
wants the events forced (stage a burst, arm the sentinel), that is a small ops issuance, not a round"* and *"it is your
call whether to raise that or wait"*. Andrew-direct 2026-09-10T21:23Z at this terminal, record @`9e1d2f700f`: *"tell
CTO~Z to grade it and close it out."* CLAUDE.md Rule 27, Andrew-direct 2026-09-10: *"no FWD is ever a 'wait' unless
explicitly advised otherwise ... sprint, execute, validate, and close"* -- an outcome whose only proof is an event
nobody controls is re-cut so its MECHANISM is driven deliberately, the organic case kept as the negative arm; a
genuinely essential wait is EXPRESSLY QUALIFIED on the outcome with its reason and Andrew's word.

⛔ **THIS IS A CLEAN RECTANGLE, NOT AN EDIT OF ROUND 3's.** Round 3 (`_round3.md` v0.3.0) and issuance 3A (`_round3A.md`
v0.1.0) stay frozen as the record of their rounds. Round-4 cells are `OP4-s-<n>`; nothing here reuses an earlier id.

---

## 1. The rectangle

**Domain (postulate i):** *the three NOT_REALIZED grades of `COMPLETION_GRADES.round3.json`, and nothing else* -- the
CTO's analysis sends back no other item. Partition, by whether the outcome's last limb is an act a seat can take ON
DEMAND today (Rule 27's test), measured on the live plane at ~21:5xZ rather than read from the analysis:

| grade | outcome | last limb | drivable on demand today? | measured |
|---|---|---|---|---|
| NOT_REALIZED | **FWD-4** | a burst fires the notification and the named person reads it | **YES** | `opal-login-abuse-alerts` has **1 subscription, email, andrew@opalinvest.com, CONFIRMED** (ARN suffix `:7`, not `PendingConfirmation`); both alarms `OK`, both `AlarmActions` = the topic; round 2's staged burst method is on record (S6-AC2) and transitioned `OPSEC-auth-throttled` `OK -> ALARM` on datapoint 190 |
| NOT_REALIZED | FWD-15 | an AUTOMATIC block produces exactly one email he receives | **NO -- C-4** | `allowlists/partner-egress.json` in `opal-security-evidence`: **404, does not exist**; `opal-suspicious-addresses`: **674 rows, 674 WATCH, 0 ALLOW, 0 blocked_by `auto:opal-sentinel`** (full scan, no `LastEvaluatedKey`); `opal-sentinel` env `SENTINEL_BLOCK_ARMED=false`. C-4 in the PRD's own words: *arming BLOCK with zero ALLOW rows is a VIOLATION, not a phase*; the Lambda refuses the arm in code (`decide()`, `lambda_function.py:208-217`). The list could not be built in round 2 because the only observable sign-in window was **97.8% this project's own probe traffic** (row `Z-S118`; TO-OP-S-20 S20-AC3 UNCOMPUTABLE-BY-CONSTRUCTION), and `1.0.0_SA_CTO~Z` @`affef41b63` date-gated the list's re-entry to **on or after 2026-10-04** with a clean sign-in window |
| NOT_REALIZED | FWD-19 | the volume of automated submissions measured BEFORE and AFTER, "by how much it changed" | **NO -- time** | baseline **0.217 automated/day** (8 of 53 over 36.82 days); after-window ~32 min; C-18 forbids an after-read on a different window or denominator, so a driven injection cannot stand in for the organic volume. Powered after-windows are **weeks** at that rate |

**Cell vocabulary** (Rule 24; a not-evaluated value so non-evaluation is never a verdict): `DONE` / `IN-FLIGHT` /
`OPEN` / `HELD` / `NOT-EVALUATED`. **Cell `value`** = the grade the cell serves: `APPLIED` or `EXERCISED`.

| cell | serves | value | status | one line |
|---|---|---|---|---|
| `OP4-s-1` | **FWD-4** | EXERCISED | OPEN | with delivery now live, a staged burst on the login path transitions the alarm, SNS DELIVERS one notification to andrew@opalinvest.com (measured on the topic's delivery metric, not on `Publish` succeeding), and the receipt reaches the record |

**NOT CUT, AND WHY -- TWO QUALIFIED WAITS, ROUTED TO ANDREW, NOT SILENTLY DROPPED:**

- **FWD-15** waits on C-4's precondition (at least one ALLOW row from a clean sign-in window), which the CTO has already
  date-gated to 2026-10-04+. **The one input that would make it drivable TODAY is Andrew's:** a partner-office egress
  address he can vouch for, entered as the first ALLOW row on his word -- then arming is a config change
  (`sentinel_block_armed = true`, a targeted apply), a staged block from an RFC 5737 TEST-NET address produces one real
  BLOCK row, one IP-set add and **one email**, and the organic case stays the negative arm. Without that word, FWD-15 is
  a wait the CTO already qualified by date, and this seat does not seed an ALLOW list from the fabric's own egress
  (round 2 refused exactly that, msg 20094 "DO NOT BUILD THE LIST").
- **FWD-19** waits on elapsed time under C-18. **Either Andrew's word qualifies the wait** (a stated after-window, read
  once on its date), **or `1.0.0_SA_CTO~Z` re-cuts the volume limb at L4** to something drivable (the CVO's own
  mechanism-pair reading, S1-AC7, already grades the control's effect on a scripted submission). Not this seat's to
  choose; surfaced with both branches.

---

## 1a. The cell

### `OP4-s-1` -- FWD-4's notification is DELIVERED, then READ

**Serves:** FWD-4, verbatim: *"When someone hammers the login page, a named person is told."* **DONE WHEN (EXERCISED):**
*"the notification has fired on a real or staged burst and the person named has read it."* **ACCEPT:** *"a burst of
blocked sign-in attempts produces a message that reaches a named human; a quiet day produces none."*

**Why round 2's exercise did not reach it, in the grade's words:** S6-AC2 fired the alarm at 2026-09-04T00:03:36Z, but
S6-AC3 measured **0 subscriptions** at that moment, so nothing was delivered. The subscription was confirmed by Andrew
on 2026-09-10 (TO-OP3-S-2, S2-AC4 flipped on read). **The mechanism has never been exercised END TO END with a
subscriber attached.** This cell does that once.

**The three limbs, and the instrument for each -- SENT != EMITTED != READ, stated up front:**
1. **FIRED** -- `describe-alarm-history` shows `OK -> ALARM` on `OPSEC-auth-throttled` with a timestamp inside the
   burst window, and the alarm's state BEFORE the burst is read and pasted (a standing `ALARM` is not a transition).
2. **DELIVERED** -- the topic's `AWS/SNS` `NumberOfNotificationsDelivered` (and `NumberOfNotificationsFailed`) for the
   window, read with `get-metric-statistics` at 60 s period: delivered >= 1, failed = 0. `Publish` returning a
   `MessageId` is SENT, not delivered, and does not satisfy this limb.
3. **READ** -- off-artifact by construction. The worker records limbs 1 and 2 and STOPS; the receipt is Andrew's word at
   the `2.0.0_SA_COO~Z` terminal, recorded verbatim by the issuer, and `1.0.0_SA_CTO~Z` grades FWD-4 on that record
   (schema `x-rule24.autonomy_after_L2`: *a card whose DONE WHEN names him is graded by the CTO on the record that the
   artifact reached him*).

**BOUNDS, all refusal-shaped:**
- **Staged burst under `OP-x-1`'s probe verdict, round 2's exact shape and no wider:** POST `https://opalinvest.dev/auth/login`
  with the fixture identity `opsec-s6-probe-fixture2@opal.invalid`, `User-Agent: opal-s6-probe`, ~240 requests, no
  valid credential, from this device. The alarm's metric is `opal/authabuse AuthThrottled` (the app's 429s); the WAF
  `BlockedRequests` alarm sits at threshold 0 and may also transition -- paste both. **A WAF rate-based block of this
  device's own egress, if it occurs, self-expires; note it, do not clear it.**
- **The sentinel is WATCH-ONLY and stays so.** The burst will add or append a WATCH row and a case file for this
  device's egress address, as round 2's bursts did (674 WATCH rows today). **No ALLOW row, no BLOCK row, no change to
  `SENTINEL_BLOCK_ARMED`, no edit to the ALLOW list** -- C-4 is not this cell's to touch.
- **NO new alarm, topic, subscription, metric filter, dashboard, digest or checker.** The moratorium exception FWD-4
  already holds covers exactly the two alarms and one topic that exist; this cell CREATES NOTHING and CHANGES NO
  INFRASTRUCTURE. If a limb turns out to need a change, STOP and file a row.
- **One burst.** If limb 1 or 2 fails on the first burst, the second act is a ROW naming what the instruments read,
  not a second burst -- "a quiet day produces none" is the negative arm and repeated bursts erode it.
- **Never paste a credential or the fixture's secret if one exists;** the fixture is an invalid identity by design.
- **Spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `NFRA_OPSEC202609-Z-W7-S<n>`; then keep working. Never a message.

**Grounding to RE-TAKE as the cell's first act (phase 1), because every number above is a measurement at ~21:5xZ and
the face that reads it later is exactly the stale-premise shape this project has paid for three times:** the
subscription is still CONFIRMED (`list-subscriptions-by-topic`); both alarms exist, are `OK`, and name the topic; the
probe path answers (a single unauthenticated POST returns 401/429, not 5xx). Any difference is a STOP and a ROW.

---

## 2. The four-postulate record (Rule 24)

**(i) MECE over a DECLARED domain.** Domain = the three NOT_REALIZED grades, enumerated as *the grades file's
`not_realized_ids` (3) MINUS the two whose last limb is not drivable today (FWD-15 by C-4, FWD-19 by C-18's window)* =
1. Written as a subtraction from the printed denominator, not as a recalled list; the two subtracted members are named
above with their unblock conditions and routed, so the subtraction cannot lose a member silently.
**(ii) SAME GRAIN.** One cell, one outcome, one exercise: fire, deliver, read.
**(iii) INTENT COHERENCE.** One axis: *reach the person FWD-4 names through the mechanism that already exists*. Not "make
the alarms better" (thresholds are `OP-x-5`'s card and TO-OP-S-23's date-gated review) and not "arm anything".
**(iv) STATE COHERENCE -- what the remedy does NOT move.** It moves FWD-4 from APPLIED to EXERCISED. It does **not** move
the sentinel's arm, the ALLOW list, any threshold, FWD-15 or FWD-19, or the register's `dep_stage` (which is
`1.0.0_SA_CTO~Z`'s on the re-grade).

## 3. Placement axis

`site-z` (`project.json` `fabric: site-z`). The burst originates from this device; the reads are AWS-plane in this
account.

## 4. Dependency edges, keyed to OBSERVED completion

```
OP4-s-1  phase 1 re-ground --[subscription CONFIRMED and alarms OK are RE-READ]--> burst --[alarm transition OBSERVED]-->
         delivery metric read --[delivered >= 1, failed = 0]--> worker reports; issuer records Andrew's receipt
         (an INTRA-cell ordering; there is no other cell)
```

**ONE chain. Fan-out 1 of 1, under the default cap of 8.**

## 5. What this decomp REFUSES to assume

- **No APPLIED-plane fact is carried from the analysis.** Every "the world is X" in section 1 was read at this seat
  at ~21:5xZ with its instrument named, and the worker re-takes the three that matter before acting.
- **No arm, no list, no threshold.** FWD-15's unblock is Andrew's input or the CTO's date; FWD-19's is Andrew's
  qualification or the CTO's L4. Both are routed in the issuance commit and the drain-end read, neither is cut.
- **No second burst to force a pass.** The negative arm is the quiet day.
- **No cell is owned by a Tier-0 or Tier-1 seat.** The cell goes to a worker subagent at L7; the READ limb is the
  issuer's record and the CTO's grade, by construction.

## 6. Holds

**NONE on the cell.** The two waits are not holds on this rectangle; they are named members subtracted from it, each
with its owner and its unblock condition.
