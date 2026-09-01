# CTO FINDING — two carriers of Andrew's word disagree about whether PERFRP may publish, and the served plane matches the PERMISSIVE one

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-01 ~13:5xZ · **Class:** FINDING + **RESERVED card to Andrew**
**Trigger:** chasing what actually gates the three empty panels, after discovering my own "one deploy
away" claim was false (the fix has been deployed since 09:15:31Z).

⛔ **THIS IS NOT AN EXPOSURE REPORT AND I AM SAYING SO FIRST.** Nothing here says anything served is
unauthorized. It says **two records of the same person's word, four hours apart, imply different
correct states — and an infra file asserts the more restrictive one as fact.**

---

## THE MEASUREMENT (mine, this turn)

```
  s3://opal-data-portal-v2/platinum/advi/49financial/      19 keys
  PERFRP leaves SERVED: 4     book_advisor · gainloss_account · gainloss_relationship ·
                              performance_account
  all four published 2026-08-31T23:1xZ .. 2026-09-01T07:27Z   (i.e. in the last ~14h)

  aws scheduler get-schedule advi-49f-publisher
     State DISABLED · cron(15 13 * * ? *) UTC · doc advi-49f-publisher-dispatch
     NEGATIVE CONTROL: a fabricated name returns ResourceNotFoundException -- the probe fires
```

## THE TWO CARRIERS

| when | carrier | what it says |
|---|---|---|
| **08-25 ~04:0xZ** | `ANDREW_DIRECT_20260825_HOLD_BREADTH_...md` — *"Agreeed with your rec"* | **(b) ratified: publishing IS part of "build it out"; the hold binds THE PROMOTE ACT ALONE.** Plus a condition: *"PERFRP keys publish only after the round-1 emitters are wired and their first emission is read — never as a side effect of someone activating the publisher's schedule for the ten legacy twins."* |
| **08-25 ~08:5xZ** | `advi_49f_publisher.tf:55-59` — *"I'm fine with it on PROD, let's just get the data part sorted"* | reads the **DATA half as standing**, with **PERFRP publication inside it**, and states: **"Zero PERFRP leaves served is the correct state until that half is discharged."** |

>> **THE EARLIER CARRIER RATIFIES PUBLISHING. THE LATER CARRIER'S READING FORBIDS IT. FOUR LEAVES ARE
   SERVED, WHICH MATCHES THE EARLIER ONE.** <<

## WHY I DO NOT READ THIS AS A VIOLATION

1. **The 04:0xZ ratification is the one that answered the question directly** — the call was put twice
   and named both branches; he picked (b). The 08:5xZ line answered a *different* question (PROD/branch).
2. **The four leaves went out under never-widen CTO+COO co-sign**, the correct mechanism for served
   output — not as a side effect of a schedule activation, which is exactly what his attached
   condition forbids. **The condition appears SATISFIED, not bypassed.**
3. **The manual path carries two independent factors** (`--publish` plus
   `OPAL_ADVI_PUBLISH_GRANT=1`, `d_publisher_port.py:525` refuses without it). These were not evaded.

## ⛔ SO THE FINDING IS ABOUT THE CARRIER, NOT THE ACT

`advi_49f_publisher.tf:58-59` states a **CURRENT-STATE FACT** — *"Zero PERFRP leaves served is the
correct state"* — that the served plane has contradicted for ~14 hours. It is an **AUTHORITATIVE-looking
infra comment in a file an operator reads before touching the schedule**, and it would tell that
operator the estate is in a state it is not in.

⚠ **And note WHICH direction the staleness runs: the restrictive carrier is the stale one.** A reader
trusting it concludes that four served leaves are a breach and may "remediate" authorized output.
**That is the expensive failure here** — not an over-publish, an over-correction.

## THE HALF THAT IS ANDREW'S — RESERVED, with the citation

**NEVER#1/#3 (served output, never-widen) and his own verbatim hold both name this decision class**, so
this does not go to CVO and I am not ruling it:

- **Was the 08:5xZ "let's just get the data part sorted" meant to NARROW the 04:0xZ ratification of
  (b), or was it about the branch/PROD question only?** The tf's author read it as narrowing. The
  served plane reflects the other reading.
- **Nothing is being changed on either reading.** No publish is being fired, no schedule enabled, no
  comment edited, until he speaks.

## WHAT GATES THE THREE EMPTY PANELS — the operational answer, stated plainly

**Not a deploy** (done, 09:15:31Z, byte-verified). **Not the never-widen co-sign** (exists). It is:

```
  scheduled path   1. schedule DISABLED, DELIBERATELY -- "the contracted design, not a half-landing"
                   2. the named SSM document does not exist (a deliberate contract hook)
                   3. the dispatcher's ALLOWED_DOCUMENTS refuses it, and refuses FIRST
  manual path      4. --publish required, default is a full dry-run
                   5. OPAL_ADVI_PUBLISH_GRANT=1, a second independent factor
```

**Five gates, three of them deliberate contract hooks.** The documented activation is a three-step TF
change *"at DS~B's deploy-ready MCP"*. **The panels are not one act from populating; they are one
CONTRACT from it, and that contract has a named owner and a named condition.**

## Grounding

`aws scheduler get-schedule` + `list-schedules` (negative control fires) · `aws s3 ls` on the platinum
serve root · `advi_49f_publisher.tf:1-110` read in full at source · the 08-25 hold-breadth record read
at source, sections 9-31 and 106-116. `s3 ls` renders LOCAL time and `s3api` UTC — timestamps above are
normalised to UTC and stated as such.

**Push state stated in the commit report, measured, never defaulted.**
