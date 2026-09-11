# ANDREW-DIRECT 2026-09-11 ~14:0xZ -- site Z is back up: check your own logs/state, and restart Bloomberg

**archetype:** COORDINATE

**Channel:** Andrew-direct at the `0.0.0_AB_MSTR` (laptop) terminal, relayed to this seat over the
agent bus as MessageId `ffd76161-f943-4e9b-8142-5b80b5115971`, 2026-09-11T14:16:31Z, from
`0.0.0_AB_MSTR`. Acked by this seat as `77ac4dbd-6b9c-4df8-9ef2-aa527a7caf5a`.

**Received by:** `0.0.0_AB_MSTR~Z`, fresh session, pid 4376, relaunched by Andrew after the reboot.

## THE ORDER, VERBATIM AND ENTIRE

> "I just restarted the sitez device, let MSTR~Z know that they should be checking their logs/state
> as they recorded info about what agents were online and the reboot. Also have them restart
> Bloomberg"

That is the whole of his word. Two acts, both this seat's. The relaying seat stated it was relaying
without widening, and this record does not widen it either. **NOT ordered and NOT done:** any
relaunch of the five down seats, any merge, any push.

## ACT 1 -- THE ROSTER, FROM THIS SEAT'S OWN PRE-REBOOT RECORD

Read from the record, not reconstructed from memory and not from process truth on a freshly-booted
box (where the honest answer is "nobody" and it says nothing about what was running before).

Source: this seat's own `logs/2026-09-10/session_2150-2230Z_launch_d4d5_title_act_and_integrate_parity_leg1.md`
amendments 14-15, committed @a335612060 and @83c719e2af.

**Pre-reboot roster -- 7 site-Z seats, 6 of which LOGGED:**

| seat | LOGGED | state at close |
|---|---|---|
| `4.0.0_SA_CRO~Z` | @c187072692 | no open task orders held |
| `1.0.0_SA_CTO~Z` | @1d36e8df4c | both projects' state, what is owed, the POSN retag landmine |
| `2.0.0_SA_COO~Z` | @23783dd2b6 | POSN_ASTTAX round 2: wave 1 complete + drained, waves 2-4 PARKED |
| `2.0.0_SA_COO~ZZZ` | @b8386bea24 | AMGT_RESAPP rounds 1-4 terminal, round 4 drained + handed to CVO; surface round v5 PARKED on the CVO v0.4 sign |
| `0.0.3_BG_BBGTerminal` | @72aeee47ce | committed on its own serial |
| `0.0.0_AB_MSTR~Z` (this seat) | @83c719e2af | amendment 15 |
| `3.0.0_SA_CVO~Z` (codex) | **NO REPLY** | owed acts recorded in the CTO~Z and COO~ZZZ logs, so the reboot did not wait on it |

**WHO IS BACK, measured 2026-09-11T14:3xZ on TWO instruments that do not share a mechanism:**

- broker (`get_live_agents`): 2 live -- `0.0.0_AB_MSTR~Z`, `0.0.3_BG_BBGTerminal`
- process truth (`Win32_Process`): exactly 2 `claude.exe` (pid 8788 @14:11:56Z, pid 19292 @14:12:04Z,
  both within 90 s of the 14:10:36Z boot) and **zero `codex.exe`**

The two agree. **Five seats are DOWN:** `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `2.0.0_SA_COO~ZZZ`,
`3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z`. Nothing respawns on its own. The zero `codex.exe` reading is the
one that matters for `3.0.0_SA_CVO~Z` and `1.0.0_SA_CTO~Z`, which ran as codex seats.

**THE RELAUNCH IS NOT ORDERED HERE AND THIS SEAT HAS NOT DONE IT.** It is an open call at Andrew --
see the OPEN CALLS section below.

## ACT 2 -- BLOOMBERG RESTARTED, AND CONFIRMED ON DATA RATHER THAN ON THE PORT

`integrations/bloomberg/READ_HERE.md` read FIRST, per CLAUDE.md law for any Bloomberg scenario.
Section 1's symptom table routed the observed failure to section 2.

| step | result |
|---|---|
| before | `bloomberg_health` -> `ok:false`, "could not start blpapi session to 127.0.0.1:8194" -- the symptom section 1 calls "the most common failure by far" |
| step 0 | `bbg_credentials.py --check` -> CREDENTIAL OK, user `alyssaakeith` user_len=12 pw_len=9 (fingerprint only) |
| fill | focus VERIFIED, screenshot `C:\opal-elev\bbg_login_shot.png`, **zero attempts spent** |
| verify | login name matches user_len=12; masked dots counted by TWO instruments -- a visual read of a 5x crop, and a column-blob count over a tight band inside the field -- **both return 9**, matching pw_len=9 |
| submit | ONE click. Ledger recorded 14 attempts total. 8194 listener count 1 |
| after | `bloomberg_health` -> `ok:true`, service `//blp/refdata` |
| **data read** | SPY US Equity "SS SPDR S&P 500 ETF TRUST-US" PX_LAST 764.93 USD; IBM US Equity "INTL BUSINESS MACHINES CORP" PX_LAST 240.14 USD |

READ_HERE.md section 2 is explicit that "LISTENER UP -- likely success" is **necessary, not
sufficient**, so the reference_data call is the claim's actual basis. The submit budget was treated
as the 2-attempt budget it is: one fill, one verify, one submit, no loop.

**Corroborated on a DIFFERENT instrument by `0.0.3_BG_BBGTerminal`** (msg 21394), which deliberately
did not re-run this seat's call and instead read `AAPL US Equity` 332.15 and `SPX Index` 7666.67 --
an index class, exercising a different entitlement path. That is corroboration, not repetition.

**Nothing was lost to the outage.** `0.0.3_BG_BBGTerminal` censused EVERY scheduled task on the box
(**denominator 204**, not scoped to the two it already knew about), matched 7 on
opal|bbg|bloomberg|pull|constituent|etf|yang, and found the only pull-bearing ones
(`OPAL_BBGTML_daily_pull` 07:00 ET rc=0, `OPAL_BBGTML_freshness_check` 07:30 ET rc=0) both fired ~7 h
BEFORE the outage with neither due again until 09-12. READ_HERE.md section 4's CURRENT-DAY-ONLY
property therefore cost nothing today. This mattered because that property has no backfill: an
uncaptured day is gone permanently.

## WHAT THIS SEAT MEASURED THAT CONTRADICTS A FRAME IT WAS HANDED

Recorded because the correction is load-bearing and the original is on the bus where a successor
will find it.

The companion bus message `4c0abdb7` said, of the audit-archive re-baseline park: *"IT EXISTS NOW.
Pull and the limb is there."* **That is false for this device.** `6560583fd5` is on `origin/CLOUD`;
this seat's branch is `SITEZ`; a fetch or pull on SITEZ does not carry a CLOUD-only commit.

Measured by blob hash with `MSYS_NO_PATHCONV=1` (a slashed ref mangles on this device and returns
clean-empty) and a positive control:

```
.tools/audit-archive-invoker.py
  worktree      adcbf69b154c4b17410a93fcd129a26cdaa97ec0   'rebaseline-once' x0
  origin/SITEZ  adcbf69b154c4b17410a93fcd129a26cdaa97ec0   'rebaseline-once' x0
  origin/CLOUD  a9837a9cfab8fd7ecc253304c8087e16df83f5dc   'rebaseline-once' x4
  6560583fd5    a9837a9cfab8fd7ecc253304c8087e16df83f5dc
positive control org/XXX.md: SITEZ cbcf608c22 vs CLOUD e45b504c10 -- the refs DO resolve to
different blobs, so the identical invoker hash is a real equality, not a mangle.
ancestry, controls fired both directions:
  83b202ed7b  CLOUD YES / SITEZ NO
  6560583fd5  CLOUD YES / SITEZ NO
  83c719e2af  CLOUD NO  / SITEZ YES   (negative control)
```

**So the precondition for the five-step repair is not a pull -- it is the CLOUD->SITEZ merge leg**,
which is an `/integrate merge` and is gated on Andrew's direction. The predecessor's own park
condition ("`6560583fd5` fetchable and on origin/CLOUD") is now SATISFIED while the actual
precondition is NOT -- the condition as written was insufficient, and that is this seat's correction
of its own predecessor, not of the relaying seat alone.

The interval guard is intact and no longer the binding constraint: `audit-archive-invoker.py` ran at
startup (step A.2) and reported `snapshot=skip: newest 2026-09-11T103259Z is < 12.0h old`, exactly as
predicted. `org/audit/archive/sitez/` survived the reboot with `.baseline` (20 B) and both snapshots
`2026-08-20T042433Z` and `2026-09-11T103259Z` -- re-verified rather than assumed, as asked.

**Also corrected:** the invoker is `.tools/audit-archive-invoker.py`, not `-invoke.sh`. This seat
guessed the latter first and got a clean not-found. A guessed path returning nothing is UNRESOLVED,
never ABSENT; resolved from `6560583fd5`'s own stat.

## LD-0255 -- THE ARM THAT RECORD HAS NEVER HAD

The reboot DID reset the Rio leak. Post-boot baseline, measured 2026-09-11T14:18:16Z, uptime 0.13 h:

```
Rio pid 6924   private 0.226 GB   workingset 0.200 GB
Rio pid 5220   private 0.057 GB   workingset 0.023 GB
HuntressAgent  27596 private 0.047 GB / 27636 private 0.066 GB
box            free phys 46.09 of 63.46 GB; commit free 71.34 of 89.46 GB
```

Compare the pre-reboot frame in @83c719e2af: Rio 0.7.77 pid 5380 at **55.31 GB private after 31.4 h**,
and `2.0.0_SA_COO~Z`'s 13:35Z RED at free RAM 0.2 GB / load 100%.

**NOT claimed:** the "~8 GB/h" figure in circulation. 55.31 GB over 31.4 h is **1.76 GB/h average**,
so the curve's shape (linear vs late-knee) is unmeasured and point T1 is what discriminates it.
T1 owed at roughly 2 h post-boot, same instrument, reported as two points with the interval rather
than as a rate. Sent to the laptop as bus `8e321521`.

## OPEN CALLS AT ANDREW -- NONE OF THESE IS ACTED ON BY THIS SEAT

1. **THE RELAUNCH.** Five site-Z seats are down and nothing respawns on its own. The memory condition
   that forced the reboot is cleared (46.09 GB free vs 0.2 GB before). His predecessor's recommended
   order stands: `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `2.0.0_SA_COO~ZZZ`, `3.0.0_SA_CVO~Z`,
   `4.0.0_SA_CRO~Z`. Spawn of WORK-population seats is the COO's own function; MSTR holds the
   primitive for infra-class population including fleet relaunch -- but he did not order one, so
   this is his call, not an inference from "the device is back".
2. **THE CLOUD->SITEZ MERGE LEG.** Assessed and ready (see the separate integrate record). It is the
   precondition for the audit-archive repair. Bare `/integrate` is assess-only by his own standing
   ruling; `merge` needs his word.
3. **GATEWAY ATTACHMENT ALLOWLIST** -- surfaced by `0.0.3_BG_BBGTerminal` (msg 21392), routed here,
   not acted on. Two people in one day (Andrew 06:44Z, Manav Shah 13:20Z) sent attachment-only
   messages the seat cannot open; `get_item` and `list_onedrive` both return `identity_scope_denied`
   against the server-side allowlist (OPAL_ANALYST PRD 4.3), exercised live at ~14:25Z. Denominator
   stated honestly by that seat: 2 instances, both 09-11, both DM, no rate claimed. Widening the
   allowlist is his ruling. His own 06:44Z attachment remains UNSERVED.
4. **D7 CLIENT-TICKET INTAKE IS MOVING ZERO** -- see the separate record; it is client-facing.

## COMPILER TOOLS

| tool | result |
|---|---|
| `comp-which "how do I grep the repo"` | forwarder RAN (startup A.3 exercise; scored on OUTPUT, not rc) |
| PATH denominator | 104 of 104 comp-tools resolve bare |
| `.tools/directives-check.py --code D7` | D7 Opal Ticketing, SITEZ, OPAL_TICKET_VNEXT active, 0 of 101 TOs open, last 08-31 |
| `.tools/to-check.py --all --assignee 0.0.0_AB_MSTR~Z` | 0 active TOs (scanned 2532) |
| `.tools/audit-archive-invoker.py` | rc=1, 21 findings, snapshot=skip (interval guard), baseline 2026-08-20T042433Z |
| `.tools/agentbus-sqs.sh device` | sitez, basis workspace path |

**On the 21 audit-archive findings:** `org/XXX.md` A.2 names only `[LIVENESS/STALE-BASELINE]` and
`[COVERAGE/UNCOVERED-AUDIT-LOG] org/to-pos-override-audit.log` as known-owned, and this run is wider
than that. Not filed as new: every extra row is the same foreign-baseline artifact the re-baseline
repair exists to fix -- the `[INTEGRITY/NON-APPEND-EDIT]` rows all show the baseline LARGER than live
(e.g. 2114503B vs 473513B), which is the signature of comparing this device's live logs against
another device's chain. They are the symptom, not a second defect. Expect them to clear when the
repair lands; findings that persist after it lands ARE a finding.
