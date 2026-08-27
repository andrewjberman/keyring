# ANDREW-DIRECT 2026-08-27 -- NO DAILY MINT. THE 7-DAY BOUND IS A REFRESH SCHEDULE, NOT A TECHNICAL NECESSITY.

**Received by:** `0.7.0_AE_CloudOps~Z`, 2026-08-27, at this terminal, during the COT session-chain
parity build. **Recorded same turn per the record+broadcast law.**
**Broadcast:** `1.0.0_SA_CTO~Z` (he named them), `0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z`.

---

## s.1 -- VERBATIM. THE PHRASING IS THE RULING.

> *"Something that is important to understand here is that we do not need a daily mint, the cookie
> works fine without daily mint. we do not even know if the cookie would ever die, we simply just
> set a 1x every 7 days process in the interest of keeping a refresh schedule. accordingly, if what
> youre saying is that we are now running a mint every single day, that would be noisy/unnecessary.
> are we clear on this subject?"*

Then, on being shown the measurement below:

> *"ok good, confirm that back to CTO~Z so it's on the record"*

---

## s.2 -- WHAT HE IS ESTABLISHING

Three separable claims, and the second is the one most likely to be lost:

1. **A daily mint is NOT needed.** The cookie works fine without one.
2. **`MAX_SESSION_AGE_DAYS = 7` IS A POLICY CHOICE, NOT A MEASURED COOKIE LIFETIME.** In his words,
   *"we do not even know if the cookie would ever die"* -- the 7-day figure was set *"in the interest
   of keeping a refresh schedule,"* not derived from an observed expiry. **Nobody should cite 7d as
   evidence about how long a BD cookie lives.**
3. **A daily mint would be NOISY/UNNECESSARY** -- i.e. a defect to be avoided, not a safe default.

---

## s.3 -- THE STATE OF THE SYSTEM, MEASURED, NOT RECALLED

**WE ARE NOT RUNNING A DAILY MINT. WE NEVER WERE. THE 2026-08-27 RESTORE DOES NOT ADD ONE.**

The daily EventBridge Scheduler entry fires `mode=session-refresh`, and **that mode name is
misleading**: it does not mean "mint." `cot-bd-session-trigger` runs **Lever A** first
(`lambda_function.py:256-277`) -- if the cookie probes positive-live AND is younger than
`MAX_SESSION_AGE_DAYS`, it **SKIPS the OIDC mint** and dispatches the bronze pull directly.

| act | document | measured frequency |
|---|---|---|
| MINT | `opal-cot-bd-session-fetch` | **4 scheduled runs**: 2026-08-03, 08-11, 08-19, 08-27 -- **+8d intervals** |
| PULL | `opal-cot-bronze-run` | **30 distinct days** of 32 in window (2026-07-27 .. 08-27) |

*(A 5th `session-fetch` on 08-27 is an AE ad-hoc QA invoke fired at 15:18Z as the acceptance test for
the restore -- a one-off, not a schedule. Its only lasting effect is re-phasing the next scheduled
mint to ~2026-09-03.)*

**The daily thing is the PULL. The mint is roughly weekly.** That is exactly the shape he described.

---

## s.4 -- WHY THE RESTORED RULE CANNOT CAUSE A MINT

`cot-session-complete` (restored @`57a373d336`, tag `cot-pipeline-v0.7.6`) has target input
`{"mode":"bronze-run"}` -- it dispatches **`opal-cot-bronze-run`, never `opal-cot-bd-session-fetch`.**

- It is **keyed on** a session-fetch Success, so it can only fire **after** a mint that has already
  happened -- ~1 day in 8.
- It **dispatches** the bronze pull, so it cannot originate a mint.
- No loop: bronze-run Success does not match its pattern. **Exercised negative control, 2026-08-27:
  four real SSM Command Status-change Success events in one window, `TriggeredRules` = exactly 1.**

**The defect it fixes is narrow and mint-day-only:** the mint would succeed and then nothing pulled
bronze, because the mint leg terminated at `lambda_function.py:277` with no handoff. Cottonwood
served ~24h stale roughly once a week. The six skip days were never affected -- they dispatch bronze
themselves.

---

## s.5 -- THE CONSEQUENCE THAT MATTERS GOING FORWARD

**The restore is NEUTRAL to the bound.** It assumes no cadence. If the 7-day bound is later widened
(14d, 30d) or dropped entirely so the mint only runs when the cookie actually fails, the mint simply
becomes rarer and this rule fires less often. **Nothing about the fix locks in a weekly mint.**

⛔ **`MAX_SESSION_AGE_DAYS` WAS NOT TOUCHED** by this build and no change to it is proposed here. The
governing spec put it explicitly out of scope. This record exists to make his reasoning available to
whoever revisits that value -- not to revisit it.

⚠ **ONE OFF-CADENCE MINT PATH, stated for completeness:** Lever A **fails safe** -- if the liveness
probe fails for any reason (including transiently), it falls through to a full mint rather than
risking a pull on a dead cookie (`:276`). So an unexpected mint is possible and is **by design, not a
defect**. The clean +8d intervals above indicate it has not been firing.

---

## s.6 -- PROVENANCE

Measured at `0.7.0_AE_CloudOps~Z` on site Z, 2026-08-27, via `aws scheduler get-schedule`,
`aws ssm list-commands` (materialised client-side, denominators printed),
`aws events list-targets-by-rule`, and CloudWatch `AWS/Events TriggeredRules`. Source read at
`infra/aws/lambda/cot-pipeline/cot-bd-session-trigger/lambda_function.py` @`f56af5748a`.

**Correction owned:** the impression that a daily mint had been introduced came from this seat's own
completion report, which led with the mint because the mint was what had to be driven to *test* the
fix. The report was accurate and the emphasis was misleading. Andrew caught it.
