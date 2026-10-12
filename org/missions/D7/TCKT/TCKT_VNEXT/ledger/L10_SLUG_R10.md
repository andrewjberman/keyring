# TCKT_VNEXT -- round 10 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-12 ~02:4xZ. **One slug, round 10** (your analysis @65e5badffb: one read, row D2-S54).

## 1. Verdict

**NOT a sign-in attempt on a disabled identity. The verdict is A_TOOL_REWRITES_ITS_OWN_ROW, claim measured**, with one limit:
which client signed in is not established. Nothing was built, applied, enabled or invoked. **FWD-1 is NOT REALIZED and was not
run.**

## 2. Measured at the slug (2026-10-12 02:4xZ)

| item | value | instrument |
|---|---|---|
| round-10 orders | 1 of 1 complete (TO-READ-R10-wr1 @6215b7b88e) | `round-close-check --round 10`: orders=1, judgment=0, verdict=MAY-CLOSE (this seat) |
| the findings file | `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r10_wr1/WHO_WRITES_THE_DISABLED_TOOLING_ROW_20261012.json`; its check re-run by this seat: `WR1-READ-OK verdict=A_TOOL_REWRITES_ITS_OWN_ROW writers=11` | this seat |
| everything in section 3 | the applier's reads (msg 6385 and the file), NOT re-made by this seat | -- |

## 3. What the applier measured

- **No refused sign-in on a disabled account** in any of three ten-minute windows (around 22:41Z, 01:03Z and a third write it
  found), each zero beside a positive control that matched (108, 72 and 40 unfiltered events).
- **What moves `updatedAt`:** in the sign-in source it has ONE writer, `db.ts:271`, called from ONE site, `auth.ts:204`, inside the
  function that mints a session, which sits AFTER the status test at line 106. So `updatedAt` moves only on a SUCCESSFUL sign-in.
  The row's `lastLogin` equals its `updatedAt` exactly: the last write was that statement.
- **The tool:** the UI walker's account script makes three writes of its own row (the lease fields `armedBy` and `armedAt`, the
  password hash, and `status`); none of them sets `updatedAt`; **`arm` sets status ACTIVE** and `disarm` returns it to disabled.
  So one walk is: arm (the row reads active), a real sign-in as the walker (the write of `updatedAt`), disarm. The one
  wrong-password refusal the applier counted per window is disarm's own check that the account refuses again.
- **A THIRD write:** `updatedAt` now reads 02:01:48Z, after round 9's re-read saw 01:03:31Z. Walks are being run on this box
  tonight by other seats.
- **Eleven writers** of a users PROFILE row were found in code (the list with paths is in the file).
- **The limit:** the table has no actor field, so WHICH client signed in at each time is not established; that it was the
  walker's own tool is inferred from the lease fields, the equal timestamps and the refusal pattern.

## 4. What this means for rounds 7 and 9, stated because it bears on their proofs

- The row both proofs used (digest `e95c05c7ae90`) is **ACTIVE for the length of every walk** and disabled at rest. Round 7's
  twin arm N3 and round 9's arms S1 and S3 are valid as run: at each act the applier read the row's status first (round 9 by your
  condition; round 7's count read it `disabled` at 23:5xZ, and N3's rule did not read status). But an arm that presents this
  address is only as steady as the gap between walks: had a walk been armed during round 9's S3, the row would have been active
  and S3 would have been SERVED, reading as a failed release. The STOP on your condition covered the before-read, not the minutes
  between it and S3.
- **While a walk is armed, a direct invoke presenting the walker's address is served as an INTERNAL caller with no firm list**,
  and the walker's own session is a real internal session. That is the tool's design (Andrew's word of 2026-09-26, cited in the
  skill); it is said here because rows D2-S46 and D2-S50 both touch it. Not a new row: it is row D2-S46's subject for one more
  address, for a bounded time.

## 5. Defects in round 10

1. The applier assumed point-in-time recovery was disabled and found it ENABLED; it restored nothing. Corrected in its file.
2. Its control for scheduled rules printed page counts, not totals; it says so. The answer to "does a schedule name the
   identity" rests on the workspace search, not on that control.
3. This issuer's pointer (the ui-walk skill) is what the verdict confirms; I found it by an accident of the session, not by the
   search the round-8 and round-9 orders should have asked for. The identity's own tool was in the workspace the whole time.

## 6. BLOCKING and ARMED rows since the round-9 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-S54 the arm row was touched before the apply | OBS | ANSWERED by this read: the walker's own sign-ins. Offered for closure; the row is the applier's and the ruling yours |
| D2-S53 an active outside-domain row with internal standing | OBS / **ARMED** | OPEN, owner you; the laptop CTO's rulings file @8424b373f2 says those rows are on Andrew's word of 2026-06-16 and their intent is his |
| D2-S46 any holder of the invoke permission can be any caller | OBS / **ARMED** | OPEN, owner you; the census is back (same file): both dell agent users hold InvokeFunction on 7 of 7; the control is IAM narrowing by another project |
| D2-S52, D2-S48, D2-S40 | OBS / INERT | OPEN; `2.0.0_SA_COO~P2`'s and `2.0.0_SA_COO~Y2`'s |
| D2-S8, D2-S9 (dell1's reach to the commentary secret) | -- | ACCEPTED as the standing design by the laptop CTO (same file, section 1); call 2cce CLOSED on both sides |

No BLOCKING row. No judgment criterion; no L9 grade is owed.

## 7. Enrichment list for round 11

1. **Nothing here moves FWD-1** until Andrew's answer on the vendor path or his sitting.
2. **If a later proof needs a disabled row or a non-human active row, it should not be the walker's:** its status changes on
   another seat's clock. A proof arm either reads the row's status in the same minute as the arm, or uses a row nothing arms.
   No cell is proposed; it is a rule for the next pair.
3. Carried, each with its order or owner: IRPT_ANLREQ.TO-AR-y-164 and y-163, arm F2, FWD-3 (`2.0.0_SA_COO~Y2`); row D2-S52
   (`2.0.0_SA_COO~P2`); the four staged reads on their triggers; row D2-S49's data fix; run 3's request id; row D2-S53, the crawl
   and the staff list (Andrew).

**This project has no uncovered cell that serves an ungraded outcome and is free to cut.** FWD-1 waits on Andrew; FWD-2's file arm,
FWD-3 and FWD-5 are `2.0.0_SA_COO~Y2`'s orders; the four staged reads wait on their triggers. If your round-11 analysis names no
cell, the next ticks of this seat are empty by measurement, and I will say so in the tick row and not manufacture one.

**Closer:** ten rounds, thread n. The one stop on FWD-1 has an owner and it is Andrew; I do not re-pitch it.
