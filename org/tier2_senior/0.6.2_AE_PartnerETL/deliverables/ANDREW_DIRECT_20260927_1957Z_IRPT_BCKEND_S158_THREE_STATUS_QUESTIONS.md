# ANDREW-DIRECT 2026-09-27 19:57Z -- three status questions on IRPT_BCKEND.TO-IB-s158

**Channel:** MCP broker, relayed by `4.0.0_SA_CRO`, Msg-ID **102057**, delivered 20260927T195720Z to
`0.6.2_AE_PartnerETL~S`.
**Verbatim (Andrew, at the CRO's terminal), quoted exactly as relayed:** "nudge the respective agents for these"
**Relay scope, verbatim from 102057:** "Reply to `4.0.0_SA_CRO`; I relay to Andrew."

The three questions as put, verbatim from 102057:

1. "Is the scheduled SSM opal-cot-bd-session-fetch at 07:30 ET on 09-28 expected to succeed unattended?"
2. "What caused the 09-24 to 09-27 failures?"
3. "Does a failed run leave a log?"

Scope is NOT adjudicated here (CLAUDE.md: surface, do not adjudicate). Answers below are this seat's, measured.

---

## 1. Is the 07:30 ET 09-28 session fetch expected to succeed unattended?

**The question has a false premise, and the honest answer is that `opal-cot-bd-session-fetch` is NOT expected to RUN
on 09-28 at all.**

`cot-bd-session-trigger` pre-gates the mint on "Lever A". From the unpacked function source:

- `MAX_SESSION_AGE_DAYS = int(os.environ.get('MAX_SESSION_AGE_DAYS', '7'))`; the live
  `Environment.Variables.MAX_SESSION_AGE_DAYS` read returns `None`, so the bound is the **default 7 days**.
- `_session_is_positive_live()` returns true only if the stored `.bd.identity` probes POSITIVE-live **and**
  `captured_at` is younger than that bound.
- `_handle_session_refresh()`: `if live:` -> `_handle_bronze_run()`; else -> dispatch `SESSION_FETCH_SSM_DOCUMENT`.

Measured with the Lambda's own read-only probe (`mode=session-check`, no secret value read):

```
{"session_live": true, "captured_at": "2026-09-27T18:42:27.162Z", "expires_at": ""}
```

At 09-28 11:30Z the capture is ~**0.53 days** old, far inside the 7-day bound. So the scheduled fire is expected to
**skip the login and dispatch `opal-cot-bronze-run` directly**. What is expected to succeed unattended tomorrow is the
box start plus bronze -> silver -> gold, not a session fetch.

**Next expected `opal-cot-bd-session-fetch`:** when the capture passes 7 days, about **2026-10-04 07:30 ET**, or sooner
if the probe goes negative first.

This also corroborates the firing history by subtraction: under a `cron(30 7 * * ? *)` schedule the document ran 08-19,
08-27, 08-31, 09-08, 09-16 -- roughly 8-day gaps, **not daily** -- then 09-24/25/26/27 four days running. An age bound of
7 days, plus "a failed mint leaves the live cookie untouched" by design, produces exactly that shape.

**AND THE ANSWER TO THE QUESTION ACTUALLY BEING ASKED:** when the fetch next runs, I cannot promise it succeeds.
I changed the document's **logging**, not its login. No cause was named, so nothing about the login's reliability was
repaired. The one Success I proved ran on a WARM box; all four failures ran on a box started ~16 seconds earlier.
`IRPT_BCKEND-S165` is the standing risk: the box carries **no in-run login retry**, so one transient failure is
terminal for the day.

## 2. What caused the 09-24 to 09-27 failures?

**UNKNOWN, and unmeasurable from the surviving evidence. It is not inferred anywhere in the record.**

What IS measured is why the failures were **silent**: `ssm.tf:49` ran `set -e` and `:65` ran the wrapper bare, so a
non-zero exit killed the shell AT that line and the `tail` and `aws s3 cp` were unreachable. `EXIT_CODE=$?` was dead
code.

Why the proximate cause cannot be recovered: `/tmp` on the box is **tmpfs**, the trigger Lambda starts the box per run,
and `ec2-auto-shutdown-enforcer` stops it at `IDLE_CEILING_HOURS=3.0`, so each log died within hours. Proven absent on
three carriers, each with its denominator, plus a positive control:

| carrier | denominator | result |
|---|---|---|
| box `/tmp` | 0 of `cot-session-autologin-*.log`; 0 of `/tmp/*.log` | EMPTY (tmpfs) |
| `s3://opal-data-cot/logs/cot-exporter/session-fetch/` | 12 objects, newest `20260916-113031` | nothing for the four days; the 09-16 object is the POSITIVE CONTROL that the upload works on a Success |
| box persistent SSM orchestration dirs | 42 present, all 4 failed command ids there | stdout AND stderr EMPTY in 4 of 4 |

A fourth carrier was ruled out, not assumed: `bd_49f_auto_login.js:434` gates screenshots behind `BD_DEBUG_SHOTS=1`,
and `grep -c` on the box's `secret-ids.env` returns 0.

The reproduction through the sanctioned path then **succeeded** (command `cf7fdead`, rc 0), so there is no failing line
to quote even now. The only untested hypothesis is cold-start, and confirming it needs a box **stop**, which is behind
Andrew's confirmation. It is recorded as a hypothesis, never as a cause.

## 3. Does a failed run leave a log?

**Yes, from now on -- with one honest limit: the failure branch has not yet been exercised against a real failure.**

The live document (version 5, applied 2026-09-27T18:37:47.998Z, read back from AWS) now runs:

```
EXIT_CODE=0
./run-bd-auto-login.sh > $LOG_FILE 2>&1 || EXIT_CODE=$?
tail -25 $LOG_FILE || true
aws s3 cp $LOG_FILE s3://opal-data-cot/logs/cot-exporter/session-fetch/$(basename $LOG_FILE) || true
exit $EXIT_CODE
```

`|| EXIT_CODE=$?` keeps the wrapper's failure inside a `||` list, which `set -e` does not act on, so the captured code
survives to the final `exit`; `tail` gained `|| true` so a missing log cannot re-abort before the upload. The document
still exits non-zero on a failed run and its name is unchanged, so `cot-session-complete` still fires on Success only.

Because `/tmp` is tmpfs, the **S3 upload is the only durable carrier** -- which is exactly what was missing.

Proven on the Success branch: `cot-session-autologin-20260927-184053.log`, 1172 bytes, 2026-09-27T18:42:29Z. The
failure branch is proven by construction (shell semantics) but **not** by a real failure, and per the estate's own rule
ABSENT is not EXERCISED-AGAINST. Given answer 1, that proof is not expected before ~10-04.

---

## Where this leaves the order

`IRPT_BCKEND.TO-IB-s158` is `complete` @`fe23038617` -- 3/3 criteria PASS against AC1 as amended by the issuer
@`9fa6a3c5d8`; proof-of-spec VALID rc=0 under the gate's `--governing-order` binding; deploy ledger
`irpt-bcknd-s158-cot-session-autologin` CLOSED, 5/5 legs.

Open and NOT closed by that flip:

- **`IRPT_BCKEND-S165`** (ARMED, `disarm_owner 1.0.0_SA_CTO`) -- the box carries no in-run login retry. This is the
  single highest-value fix if the concern is "will it hold unattended".
- **`IRPT_BCKEND-S166`** (ARMED) -- the running login script has no build input in the cot tree.
- **`IRPT_BCKEND-S168`** -- this record's answer 1, and a correction to this seat's own earlier claim that the 09-28
  run would be the cold-boot test.
