# DEPLOY COMPLETION LEDGER -- THE MANUAL SERVED DAY, 2026-09-10 keys (NFRA_OUTSET.TO-OS-s-24)

**Opened:** 2026-09-10T00:20Z by `0.7.0_AE_CloudOps~W`
**Status:** **CLOSED RED 2026-09-10T00:58Z -- THE RUN WROTE 09-09 KEYS, OUTSIDE THE SIGN-OFF. ROLLBACK EXECUTED AND VERIFIED BY CONTENT.**
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-24.the-manual-served-day.md`
(cell `OS-s-24`, PRD v0.8; issuance `26f1cd8b82`)

⛔ **OPENED BEFORE STEP (iii), THE ORCHESTRATOR INVOKE.** The invoke has not happened at this
entry's commit. This is a RULE (2) served-output move: a report run writes `daily/` and `manifest/`,
which the estate reads.

## THE NEVER-WIDEN SIGN-OFF -- BOTH HALVES, QUOTED

**COO half -- issuance `26f1cd8b82`**, TO-OS-s-24's own face, verbatim:

> The COO's half is GIVEN HERE, in this face, for exactly this run: 09-10 keys, nothing
> overwritten, the four pins named, the rollback named -- quote this face's commit hash as the
> COO's line.

**CTO half -- message id `94764`** from `1.0.0_SA_CTO`, 2026-09-09T22:30:20Z, verbatim:

> This message id is the CTO's half of the never-widen sign-off (CLAUDE.md NEVER-1) for exactly the
> run below; the COO's half is issuance 26f1cd8b82. [...] WHEN: after 2026-09-10T00:00:00Z, before
> 13:00Z, so every key is dated 2026-09-10 and nothing dated 09-09 is written or overwritten [...]
> Anything outside this shape (a 09-09-dated run, a write under a different prefix, a run without
> the token) is not covered and needs a new sign-off.

⛔ **THE ID IS 94764, NOT 94763.** I was carrying 94763 forward from an earlier note and it was
wrong. It was corrected by OPENING the message and reading its own `Msg-ID` line rather than
trusting the number I had. A sign-off quoted by the wrong id is not a sign-off.

## What this run writes -- NEW KEYS ONLY

`daily/2026/09/10/estate-report-2026-09-10.json`, the `.md` sibling, `manifest/2026-09-10.json`,
and one `logs/` key. **No existing key is overwritten.** The `outset/` seam writes of steps (i) and
(ii) are producer artifacts under their own faces' QA clauses and are explicitly OUTSIDE this
sign-off.

## THE PROTECTED RECORD -- the four 09-09 pins, measured live at 00:19Z BEFORE the invoke

| key | VersionId | LastModified | IsLatest (before) |
|---|---|---|---|
| `daily/2026/09/09/estate-report-2026-09-09.json` | `M.3hYlFn8PRvTcqxCUouBTNygDd73huK` | 15:32:41Z | **true** |
| `daily/2026/09/09/estate-report-2026-09-09.json` | `8SP4fGAuhE8twzBpucMPsYbotD6Tddty` | 13:11:02Z | false |
| `daily/2026/09/09/estate-report-2026-09-09.md` | `xfSKTGqkdljsQTyUt20nC1RJsPtPGBSU` | 15:32:41Z | **true** |
| `daily/2026/09/09/estate-report-2026-09-09.md` | `GcEjGK_GwkDzyyvVo190fPSODn9svmLx` | 13:11:02Z | false |

Version denominators before the invoke: `.json` 2, `.md` 2, `manifest/2026-09-09.json` 4 (its
latest is `68kpLcmJw.4hNCbaIjMgSFU3a.oHP9.G` @15:32:41Z).

⛔ **HOW ARM (e) IS READ, STATED BEFORE THE RUN SO IT CANNOT BE FITTED AFTERWARDS.** O24-AC1 (e)
says "the four 09-09 pins are STILL the latest versions of their keys ... IsLatest true on the
pinned id". **Taken literally that cannot hold for two of the four**: the four pins are TWO KEYS x
TWO VERSIONS, and the 13:11:02Z pair is by construction the SUPERSEDED version -- the face itself
names it "O20-AC1's negative arm". This is loose phrasing, not a defect: the face's own parenthetical
shows the issuer knows which pin is which. The SUBSTANCE the arm buys is that the manual day
overwrote nothing, and it is read as three checks, all stronger together than the literal one:

1. the version DENOMINATOR on each 09-09 key is unchanged after the run (2 / 2 / 4);
2. the IsLatest id on each key is still the 15:32:41Z pin;
3. all four pinned ids are still PRESENT and retrievable.

## Rollback

One `copy-object` from the pinned VersionId per key, in session, no Terraform. Bucket versioning is
ENABLED (all four pins listed above prove it). **Expected to be unnecessary**: this run creates
09-10 keys and touches no 09-09 key. If a 09-09 key is ever touched, that is outside the sign-off
and the entry closes RED with the copy-object executed.

## Legs

1. [x] Step (i): OS-s-25's on-demand drift run -- artifact VersionId
       `3AE8of7Q44VkfbsNNpwWD0EH8lqPj.Sn` @2026-09-09T23:58:14Z, `git_head_moved` false.
2. [x] Step (ii): freshness CodeBuild started BY HAND 2026-09-10T00:17:51Z --
       `estate-report-seam-freshness-publisher:dc71343c-9118-4037-86b5-23e9bdd5e4b0`, build #3,
       `initiator` `Andrew_Berman`, source type NO_SOURCE (the same project and call the 08:30 ET
       rule targets; `Target.Input` NULL, so the hand start and the rule start are the same call).
3. [x] All THREE seam artifacts in place and ahead of the invoke, measured 00:19Z:
       `outset/comp_heat_freshness_tools.json` @2026-09-10T00:18:59Z v`wPjEwsCY4Fg2o84Wp3bGYUs7fqSKb7Pz`
       (moved from 16:54:39Z), `outset/comp_fedobs_coevolution.json` @2026-09-10T00:19:02Z
       v`PX68UJFO3pcBlpUn.P8rl79YZ6Ado5l4` (moved from 16:54:42Z),
       `outset/laptop/comp_heat_drift.json` @2026-09-09T23:58:14Z. **Both off-host keys MOVED**, so
       the build wrote them rather than leaving yesterday's bytes to read as fresh.
4. [ ] Step (iii): orchestrator invoked with `{"mode":"daily-run","trigger":"manual"}`.
5. [ ] The 09-10 keys written; `run_bundle.trigger == "manual"` with the matching `run_id`.
6. [ ] The four 09-09 pins intact on all three checks above.
7. [ ] The host STOPPED at the read.

## The host

`i-0584e17d283fa7ef4`. The run ends with the host self-stopped by its boot units' design. **A host
still running 30 minutes after the report lands is a FINDING, not a wait** (the face's own words).
---

# CLOSED RED -- what happened, in order

⛔ **THE RUN WROTE THE 2026-09-09 KEYS, WHICH IS THE ONE SHAPE THE SIGN-OFF EXCLUDES BY NAME.** The
CTO's half (94764) says: *"Anything outside this shape (a 09-09-dated run, a write under a different
prefix, a run without the token) is not covered and needs a new sign-off."* A 09-09-dated run is
exactly what happened. The pre-authorized rollback was executed in session and verified.

## Timeline, measured

| instant (UTC) | fact |
|---|---|
| 00:29:57Z | orchestrator invoked, payload `{"mode":"daily-run","trigger":"manual"}`, returned `started: true`, `prior_state: stopped` |
| 00:30:07Z | trigger token minted -- `trigger` manual, `run_id` `a588a7ea-8ad2-4f03-a814-4f02668a66d6`, 1 version (the key did not exist before) |
| 00:30:08Z | host `i-0584e17d283fa7ef4` launched; cloud-init finished 00:30:28Z |
| 00:30:33Z | `manifest/2026-09-09.json` written PENDING at boot -- **the first 09-09 write, 22 minutes before I saw it** |
| 00:47-00:49Z | AI authoring stages progressing normally (read live over SSM) |
| 00:52:49Z | `daily/2026/09/09/*.json`, `*.md` and `manifest/2026-09-09.json` written -- **new versions on all three protected keys** |
| 00:52:50Z | `logs/2026-09-10T005248Z-i-0584e17d283fa7ef4.log` |
| ~00:55Z | host self-stopped, as designed |
| 00:57:56-00:58:03Z | **ROLLBACK**: three `copy-object` calls restoring each pinned VersionId as latest |
| 00:58Z | rollback VERIFIED BY CONTENT (sha256), negative control fired |

## THE CAUSE, measured in the code and not inferred from one observation

`estate_report_runner.py:219-226` (`_window`) derives the report date from **the most recent 09:00
America/New_York mark**, never from the calendar day:

```
local_now = now_utc.astimezone(SCHEDULE_TZ)
todays_mark = local_now.replace(hour=SCHEDULE_HOUR, ...)
end_local = todays_mark if local_now >= todays_mark else todays_mark - timedelta(days=1)
```

That is CORRECT and deliberate -- CVO approval condition C1 requires boundaries from the schedule,
not from wall time, so consecutive windows cannot overlap or gap. Evaluated:

| run instant (UTC) | local | report date |
|---|---|---|
| 2026-09-10T00:29:57Z (my invoke) | 2026-09-09 20:29 EDT | **2026-09-09** |
| 2026-09-10T04:00:00Z (midnight ET) | 2026-09-10 00:00 EDT | **2026-09-09** |
| 2026-09-10T12:59:00Z | 2026-09-10 08:59 EDT | **2026-09-09** |
| 2026-09-10T13:00:00Z | 2026-09-10 09:00 EDT | 2026-09-10 |

⛔ **SO THE FIRST INSTANT THAT YIELDS 09-10 KEYS IS 2026-09-10T13:00Z, WHICH IS THE SCHEDULED FIRE
ITSELF. THERE IS NO EARLIER MANUAL WINDOW.** The premise shared by PRD v0.8, this face and both
sign-off halves -- "run after 00:00Z and every key is dated 2026-09-10" -- conflates the CALENDAR DAY
with the SCHEDULE MARK. Waiting until 04:00Z would not have helped either; I checked that before
asserting it, because it was my own first guess.

## Rollback -- executed and VERIFIED BY CONTENT

Three `copy-object` calls, each restoring the pinned VersionId as the key's latest.
**NOTHING WAS DESTROYED**: versioning is enabled, so the run's 00:52:49Z versions remain in history
and are retrievable.

| key | restored from pin | new latest VersionId | sha256 vs pin |
|---|---|---|---|
| `daily/2026/09/09/estate-report-2026-09-09.json` | `M.3hYlFn8PRvTcqxCUouBTNygDd73huK` | `n9hMlZsbfUrv1jzuhXnDBbzPV1cpYMIk` | `9d0ff4d6135a9ccb`, 204,352 B -- **IDENTICAL** |
| `daily/2026/09/09/estate-report-2026-09-09.md` | `xfSKTGqkdljsQTyUt20nC1RJsPtPGBSU` | `5Z_065g.pfGjX1CtHLPEsL72K7wF6WqO` | `c3b6a88eeaf1da87`, 27,505 B -- **IDENTICAL** |
| `manifest/2026-09-09.json` | `68kpLcmJw.4hNCbaIjMgSFU3a.oHP9.G` | `admN2Jz26T7DJ.NN7gaVRtnWdvBsnqAF` | `0a7f44e8812ba910`, 16,812 B -- **IDENTICAL** |

**NEGATIVE CONTROL:** the run's own version `F3CLuHhwgcRKo7OdbCdLbexIO6BUo3Mw` hashes
`dbe02e28c705f3eb` at 206,144 B -- it DIFFERS from the restored bytes, so the comparison
discriminates rather than passing on any pair of objects.

Verified by SHA256 OF THE BYTES, not by VersionId: a copy-object mints a new VersionId whatever it
copies, so the id proves the call ran and nothing about what it restored.

## What the run DID prove -- OS-s-26's carrier, end to end

The trigger carrier worked exactly as built, and this is its first EXERCISED read:
`run_bundle.trigger` = **manual**, `run_bundle.run_id` = **a588a7ea-8ad2-4f03-a814-4f02668a66d6**,
byte-equal to the token the orchestrator wrote at 00:30:07Z. A manual run was told apart from a
scheduled one ON THE ARTIFACT, never by the clock. That is O26-AC1's positive arm, and it passed on
a real run.

## What is NOT decided here

The 00:52:49Z report is a legitimate, newer report of the 09-09 window and it is NOT lost. Whether
the estate should serve it instead of the 15:32:41Z pin is the ISSUER's call, not this lane's. I
restored the pin because that is what the sign-off names as the remedy, and because the pin is the
artifact OS-s-20's accept depends on.

**No re-run was attempted.** A second invoke before 13:00Z would write the 09-09 keys again.
