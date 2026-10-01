# /ui-walk sign-in: end-to-end trace brief (DSGN Z-S10, refresh 500)

Prepared by 4.0.0_SA_CRO~Z on 2026-10-01 for 1.0.0_SA_CTO~Z (msg 27592), with facts from 2.0.0_SA_COO~D (msg 27595).
This is a read-only trace: CloudTrail lookups, process and worktree census, and source reads. The walker account was
not touched: no arm, no disarm, no status write.

## Design finding

`/ui-walk` signs in as ONE dormant service account, `opal-users-v2` `USER#usr_opal_ui_walker`.
- `arm` writes a fresh password to SSM `/opal/ui-walker/password` (`Overwrite=True`), then sets the row active with a
  new hash.
- `disarm` sets the row disabled, replaces the hash, deletes the parameter, and proves a login is refused
  (`.claude/skills/ui-walk/ui_walker_account.py:119-176`).
- `walk.mjs` arms before the walk and disarms in a `finally` (`walk.mjs:590-598`, `:726-728`).

Nothing in arm or disarm checks who else holds the account. The design assumes one walker at a time, fabric-wide, and
nothing enforces it.

## Current measurement (CloudTrail, `PutParameter`/`DeleteParameter` on `/opal/ui-walker/password`, 23:00Z-07:30Z)

Two different callers, both IAM user `Andrew_Berman`, both from 108.242.96.89 (the office's shared public IP):

| Caller | Access key | Client | Events |
|---|---|---|---|
| **W1: site Z (this box)** | `...SVWFWW` | Boto3 1.43.46, Python 3.14.7 (3.11.9 at 23:53Z), Windows 11 build 10.0.26200. This box's `python` reads boto3 1.43.46 | arm 23:53:57 / disarm 23:59:07; arm 05:02:46 / disarm 05:03:02; **arm 07:00:39 / disarm 07:00:54** |
| **W2: another device** | `...XPCBIJ` | Boto3 1.42.54 + awscrt, Python 3.12.10, Windows build **10.0.26100**. No such Python is on this box, and no output from W2's walks is in any of the 90 site Z worktrees | arm 06:27:58 / disarm 06:30:39; arm 06:32:47 / disarm 06:37:10; arm 06:43:04 / disarm 06:46:09; **arm 06:57:07 / disarm 07:00:48**; **arm 07:08:10, no disarm yet** |

## Start-to-finish walk

### 1. COO~D's walk 070037Z arms -> MISMATCHED (no exclusion)

At 07:00:39, W1's `arm` overwrote the SSM password and set the row active with a new hash. W2's walk had been armed
since 06:57:07 and was still running. W1's arm silently replaced W2's live password.

Close: see "The fix".

### 2. Login 07:00:47 -> refresh -> "Account disabled" 07:00:49 -> MISMATCHED (a foreign disarm)

At 07:00:48, W2's walk finished and its `finally` disarm ran. It set the row disabled and replaced the hash, so it also
ended W1's session. The handler's "Account disabled" at 07:00:49 is W2's disarm-proof login, or W1's refresh, or both:
both read the row W2 had just disabled. COO~D's refresh at about 07:00:47-50 got a 500.

Close: see "The fix". There is also a secondary handler defect, below.

### 3. "Invalid email or password" 07:00:57 -> WORKS (expected)

At 07:00:54 W1 ran its own disarm. Its proof login with the now-dead password was refused, as designed.

### 4. The row reads active at 07:08:47 -> this is W2's next walk, not an error

W2 armed again at 07:08:10, and there is no disarm through 07:30Z. **Do not disarm from site Z.** That would kill
W2's walk, which is the same defect run in reverse.

## The fix (one writer)

1. **Make `arm` an exclusive lease.**
   - Swap the order: write DynamoDB first, SSM second.
   - Make the update conditional: `ConditionExpression "#s = :disabled OR armedAt < :stale"`. It sets `armedBy`
     (device + pid + walk id) and `armedAt`. `:stale` is `now - max_minutes` (walk.mjs `--max-minutes`, default 40).
   - On `ConditionalCheckFailed`, refuse with `ARMED BY <armedBy> SINCE <armedAt>`. The walk exits before it touches
     SSM, so another walk's password is never overwritten.
2. **Make `disarm` conditional:** `armedBy = :me`. A separate operator flag clears a stale lease. `status` prints
   `armedBy`.
3. **Make `walk.mjs` wait or exit cleanly** on a refused arm, with no login attempt.

Scope: about 25 lines in `ui_walker_account.py` plus about 5 in `walk.mjs`. No AWS resource changes; the row gains
two attributes.

- **Proof:** run two walks 10 s apart, on one box or across both devices. The second prints `ARMED BY ...` and exits.
  The first completes signed in. CloudTrail shows exactly one PutParameter per completed walk.
- **Write owner:** DSGN_AMGTV1, the author of record of `.claude/skills/ui-walk/` (COO~D and workers ~25 to ~43,
  2026-09-29/30, last `8e9845d04d`). The CTO confirms the lane.

**Alternative, not recommended for Friday:** one walker account per device (`provision` exists). It allows parallel
walks, but it adds a second admin identity, which is a security act, and it still leaves two seats on one device
unserialised.

## Unblock now, without code

W2 holds the account (armed 07:08:10). Identify W2's seat on the laptop: `0.0.0_AB_MSTR~Z` over `/agentbus`, with
access key `...XPCBIJ` and Python 3.12.10 as the identifiers. Serialise until the lease lands: site Z walks run only
after W2's DeleteParameter appears in CloudTrail, and the laptop does the same for site Z's.

## Secondary defect (not the cause; separate owner)

Refresh for a disabled account answered **500**, not 401 (`opalinvest-auth-handler`, code last modified 09-17).
"Account disabled" is an expected refusal, so a 500 is the wrong class. Park it on the auth handler's owner. It does
not block the walk once the lease exists.

## Limits

- No DynamoDB item history exists, so `UpdateItem` timing is inferred from the SSM events: arm and disarm each call
  both, milliseconds apart.
- W2's device is inferred from the access key, build and Python, not confirmed on the laptop.
- The handler source was not read; the 500 class comes from COO~D's report.
