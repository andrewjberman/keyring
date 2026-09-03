# 0.0.3_BG_BBGTerminal — session log 2026-09-02T14:29–14:40Z

**Archetype:** DAILY GUARDRAIL (continuation — no new startup)
**Serial:** 0.0.3_BG_BBGTerminal (base) · broker PID 16328 · device: site Z
**Continuity:** SAME SESSION as `logs/2026-09-01/startup_and_daily_guardrail_1855-1906Z.md`.
Registered 2026-09-01T18:55Z and **continuously live since** — no relaunch, no re-arm, both
Monitors still the ones armed yesterday (`b38eciz71` inbox, `bi6lvvse4` Teams). **The date rolled,
so the guardrail came due again; the session did not restart.** This log covers only the 09-02
delta.

---

## 1. DAILY UPLOAD GUARDRAIL (record @e77bec6e5) — **PASS**, end-to-end, for 2026-09-02

**Trading calendar resolved via the ONE frontier** (`lib/trading_calendar.py`), not by hand:
`calendar_source = NYSE/hardcoded-fallback-2024-2027`; `is_trading_day(2026-09-02) = True`
(Wednesday); `prev_trading_day(2026-09-02) = 2026-09-01`. **T-1 is 20260901.**

| surface | reading |
|---|---|
| `OPAL_BBGTML_daily_pull` | Last **9/2 07:00:01 ET**, Result **0**, Next 9/3 07:00 |
| `OPAL_BBGTML_freshness_check` | Last **9/2 07:30:01 ET**, Result **0**, Next 9/3 07:30 |
| artifacts | `data 20260901 v1.pkl` (8,627,338 B) + `model 20260901 v1.pkl` (17,598,796 B), written 9/2 07:02–07:03 |

**As-of 20260901 IS exactly T-1. Correct, not stale.**

Read at source in `~/opal_bbg_logs/bbg_tplus1_20260902_070001.log` — and the publish leg is
content-verified, so `rc=0` here is not merely the producer's self-report:
```
PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request.
TRIPWIRE: vintage 20260901 ... RESULT: PASS -- both PKLs safe to send
OK:   served data_as_of 2026-09-01 (generated_at 2026-09-02T11:05:56Z)
OK:   served 1D matches the PKL for all five models
RESULT: PUBLISHED 2026-09-01 -- verified by content, not by self-report.
RESULT: END-TO-END OK -- pulled, validated, published, served-content verified.
```
ETF leg EXIT 0, constituents leg EXIT 0. **No fallback `/terminal-upload` needed; none run.**

### 1a. The DAPI fallback did NOT sign in today — and that CORRECTS yesterday's framing
Yesterday I logged the sign-in fallback firing and wrote that *"a fallback that fires silently every
day is a fallback that has become the primary path."* **Today it did not fire in that sense:**
```
[fallback] checking DAPI availability...
[fallback] DAPI UP -- proceed with pull, no sign-in needed.
```
**The block RUNS every day; the SIGN-IN inside it does not.** Yesterday it submitted
(`bbg_signin.ps1 -Phase submit`); today it checked and passed straight through. So the watch I
opened is **1 of 2 days, not 2 of 2** — and the discriminator is the `no sign-in needed` line, not
the block's presence or its `EXIT 0`, both of which are identical in the two cases. ⛔ **My own grep
yesterday would not have separated them**: I filtered on `PRECONDITION|TRIPWIRE|RESULT|EXIT`, none
of which distinguishes a submitted sign-in from a skipped one. **A token census tuned to the
verdict lines cannot see which limb produced the verdict.** Counting this as a trend needs the
`[fallback]` lines specifically, every day, or it is not a count.

---

## 2. Merge window #2 (msg 19330) — acked; posture unchanged, deliberately not restated

`0.0.0_AB_MSTR~Z` opened a second window (inbound leg CLOUD→SITEZ, 8 commits, **overlap 0 of 17 =
0.00%**, merge-tree rc=0, inbound deploy ceiling 0). Acked (`ack_messages("19330")` accepted) and
answered SHORT — the full structural posture was given in the 19274 reply and repeating it would be
noise, not diligence. Same standing: **non-source of the staging hazard, not a complier**; this
seat does no git work.

**Nothing held back.** Yesterday's log was swept clear after the previous CLOSE. This log is the
one new untracked file and is again scoped to AFTER the CLOSE rather than offered mid-merge.

**One datum offered to the integrator, bounded:** msg 19330 repeats the "courtesy, not the control"
caveat, and last night's measured reach was **0 of 7**. This seat has been continuously live since
18:55Z on 09-01 and read all three broadcasts within a minute of send — so a reach figure carried
over from last night would understate by at least this one row. **I asserted no number for the other
six seats and claimed no knowledge of their state.**

---

## 3. Compiler Tools

| tool | use | outcome |
|---|---|---|
| raw `grep`, marked | `~/opal_bbg_logs/bbg_tplus1_20260902_070001.log` verdict lines, then the `[fallback]` limb | **Rule 21 non-application limb (iii)** — a transient run log outside the repo corpus; marked `# rail-checked:` on both calls |
| `python lib/trading_calendar.py` | T-1 frontier | the ONE frontier, queried not recalled |

**Rule 21 limb (i) is DISCHARGED as of the 09-01 merge** (`comp-read --enumerate` landed and is
certified) — a count no longer justifies `grep`. **That did not bind either call above**: both were
outside the repo corpus under limb (iii), which is unchanged. Stating it because the discharge is
one day old and the temptation is to either over-apply a fresh rule or forget it; neither happened,
and the reason is the corpus boundary, not my discipline.

---

## 4. State

- Both Monitors armed and unchanged since 09-01; **ZERO crons**; zero pending task orders.
- Fabric inbox: 3 messages received, read at source and acked this session (19274, 19282, 19330) —
  all `0.0.0_AB_MSTR~Z` integration frames. Nothing else.
- **Nothing owed on Teams** (no emit since the 09-01 arm).
- **Guardrail PASS 2026-09-02**; served vintage 2026-09-01 = T-1, content-verified.
- Holding for the CLOSE frame. **Available.**

---

## 5. 18:19–18:25Z — windows #3, and a correction I had to issue against myself in 50 seconds

Msg 19392 opened a THIRD window (inbound CLOUD→SITEZ, 46 commits, overlap 1 of 92 = `DIRECTIVES.yaml`,
deploy ceiling 0). Acked. Msg 19399 CLOSED it @`055ca5499d`. Both acked; posture unchanged throughout.

### 5a. I reported a state that aged in 50 seconds — and the rule for it was already on the books
Between the OPEN and the CLOSE I measured the broadcast sequence and found **3 OPENs, 1 CLOSE**:
```
get_delivery_state(0.0.3_BG_BBGTerminal, limit=12)   denominator 12 of 12 ACKABLE, READ=11 SENT=1
  19274 OPEN -> 19282 CLOSE   PAIRED
  19330 OPEN -> (no row)      UNDISCHARGED ~4h
  19392 OPEN -> (no row)      UNDISCHARGED
```
I sent that at **18:23:53Z**. The CLOSE for 19392 (msg 19399) was sent at **18:23:03Z** — it crossed
my message in flight by **fifty seconds**. So the 19392 limb was TRUE when measured (18:19–18:22Z)
and FALSE when delivered.

⭐ **The failure is not the measurement — it is the MISSING VINTAGE, and this estate already has the
rule.** CLAUDE.md: *a push-state claim "is perishable and ages the moment an integrator runs."* I
applied that discipline rigorously to **git** state this session — ls-remote read, HEAD re-read the
moment it moved — and **did not apply it to the MESSAGE state I was reporting on**, while an
integrator was demonstrably mid-leg at that exact minute. **A delivery census taken during an active
integration leg needs its read-time stamped exactly like a push state does.** Retracted to
`0.0.0_AB_MSTR~Z` immediately, before the original could be read.

**What still stands:** the 19330 window (merge `364c523281` landed 14:30:10Z) has no CLOSE addressed
to this seat. Now MOOT — 19399's "safe-commits are clear" discharges globally — so it is a
record-keeping observation, not a stalled seat. Bound restated: my ledger is scoped to messages
addressed to THIS seat, so the sound claim is *no CLOSE addressed to this seat*, never *no CLOSE
was sent*.

### 5b. A negative control "failed" and the instrument was fine — my BASELINE was 4 minutes stale
Verifying whether window #2 landed, I ran `merge-base --is-ancestor` with a negative control
(`dea3bccad3`, the CLOUD head 19392 says is NOT yet merged). **The control returned rc=0** — the
shape of a broken instrument. I stopped and did not report off it.

**Cause: the shared tree advanced between my two reads.** HEAD was `ed41b8c424` when I read it and
`055ca5499d` four minutes later — window #3's merge landed mid-investigation, which legitimately
made `dea3bccad3` an ancestor. **The instrument was sound; the baseline was stale.** Banked
[[working-tree-is-a-snapshot-ref-is-current]], met from the other side: normally that note warns a
stale tree makes things look ABSENT, and here a *freshening* tree made a control look BROKEN. **A
failing control is not automatically the instrument's fault — re-read the baseline before condemning
the tool.** Cost of getting this right: one `rev-parse`. Cost of getting it wrong: a filed
false instrument-failure against a tool the estate depends on.

### 5c. Two things I checked before asserting, and one I declined
- **Window #2 and #3 both landed** — `364c523281` @14:30:10Z, `055ca5499d` @18:20:41Z; ls-remote
  `origin/SITEZ = 055ca5499d = local HEAD`, no `MERGE_HEAD`. Measured on git, not inferred from the
  broadcast absence.
- **Attribution:** 19392 credited this seat with establishing that QUEUED describes push availability
  rather than liveness. I did not write that — I wrote only that I had been continuously live. I
  corrected it, then **softened the correction** when 19399 supplied the evidentiary half I lacked
  (this seat QUEUED on three sends while demonstrably live). The conclusion is sound and is
  `0.0.0_AB_MSTR~Z`'s to claim; only the attribution to me was wide.
- **Declined:** the msg-id discrepancy in 19399 ("the hold from **19391**" vs the OPEN this seat
  received as **19392**) — almost certainly per-recipient fan-out ids. Not chased; it would not
  change what I do. **CONFIRMED by msg 19407**: the ids are per-recipient (OPEN went out as
  19329/19330/19331/19332/19333/19334/19335). Declining to chase it was correct.

### 5d. RESOLVED @18:25Z (msg 19407) — the 19330 gap was real, and larger than this seat could see
`0.0.0_AB_MSTR~Z` confirmed the defect and issued a retroactive close. **Both windows DISCHARGED**
(`364c523281` @14:30:10Z, `055ca5499d` @18:20:41Z); nothing held.

**The measured shape, from the integrator's own send receipts:** the 14:29Z window was
**OPENED to SEVEN seats and CLOSED to THREE**. Four seats — `0.0.3_BG_BBGTerminal`,
`0.7.0_AE_CloudOps~Z`, `0.4.0_DE_ClientPlatform~Z`, `0.3.0_DT_TradingOperations~Z` — were formally
held for ~4h on a lock that had been irrelevant for the whole period. **My bound was the right
one:** `get_delivery_state` is scoped to messages addressed to this seat, so all I could ever claim
was *no CLOSE addressed to this seat* — and the true scope turned out to be four seats, not one.
**Stating the bound is what made the report useful rather than either overclaiming or staying
silent.**

⭐ **THE PART WORTH BANKING IS WHO COULD SEE IT.** The three stalled seats with an actual lane were
**down and could not report**. The seat that noticed holds no lane, runs zero commits, and had
**exactly zero cost** from the stall — no incentive to look. **A failure anti-correlated with
compliance is invisible to everyone it harms**, so it can only be caught by someone it does not
harm. That is a general argument for a no-cost observer checking protocol pairings, not a credit to
this seat.

**Remedy is the integrator's and it is mechanical, not a resolution to be careful:** the CLOSE
recipient list IS the OPEN recipient list, never a subset drawn from whoever is in the current
thread.

**Attribution corrected at the source:** 19407 records that this seat never made the QUEUED-semantics
claim, that the inference was the integrator's, and that the conclusion stands on its own ground.
Named there as *a claim strengthening in transit, moving SIDEWAYS rather than upward* — harder to
catch than the upward form because the author of the strengthened version is not the author of the
claim, so the one person able to spot it only does so if cc'd. I was cc'd.

---

## 6. FILE STATE — final

**Both this seat's logs are FINAL as of 2026-09-02T18:26Z and will not be written again this
session.** `0.0.0_AB_MSTR~Z` takes them on the current ordinary sweep (msg 19407 §3, per the
standing offer made in the 19274 reply):
- `logs/2026-09-01/startup_and_daily_guardrail_1855-1906Z.md`
- `logs/2026-09-02/daily_guardrail_1429-1440Z.md` (this file)

**Session state:** both Monitors armed and unchanged since 09-01T18:55Z, zero crons, zero pending
task orders, nothing owed on Teams, guardrail PASS for 2026-09-02. Six fabric messages received,
read at source and acked (19274, 19282, 19330, 19392, 19399, 19407). **Available.**
