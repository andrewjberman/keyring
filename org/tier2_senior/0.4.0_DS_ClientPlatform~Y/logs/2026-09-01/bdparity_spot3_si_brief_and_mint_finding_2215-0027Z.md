# ADVI_BDPARITY -- the 3-account validation, the SI recommendation, and a mint that did not fire (2026-08-31T22:15Z - 2026-09-01T00:27Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Seat:** `0.4.0_DS_ClientPlatform~Y` | **Scope:** ADVI_BDPARITY (Rule 27)
**Window:** since `bdparity_w2_prefire_2113-2215Z.md` @ `bd537a8f46`
**Commits (2):** `9f0d8a84dc` spot-check result · `26ad56cf92` the brief. **PUSH STATE: LOCAL**
(integrator-only gate LD-0367/0368 on CLOUD; they ride the integration window).
**Vendor calls this session: 5 total** -- 1 pre-flight auth (21:39:14Z), then 1 auth + 3 data (23:53Z).

---

## Current State

**W2 is built, exercised, committed and STILL UNFIRED.** It is held on a named gate, not stalled.
**Andrew's 3-account validation is DELIVERED.** A brief carrying all findings is committed.

**The gate:** the 00:00Z session mint has NOT fired -- `LastChangedDate` still `2026-08-31T00:03:47Z`
at 00:27:21Z, now ~24.4 h old. `2.0.0_SA_COO` 90040 holds W2 on that; `2.0.0_SA_COO` is NOT LIVE
(sends QUEUE), so the call sits with `1.0.0_SA_CTO`.

⛔ **CORRECTED 00:3xZ, AFTER THIS LOG WAS COMMITTED (`3aa8bcf273`) AND BY THE SEAT THAT WROTE IT --
THE MINT DID NOT FAIL.** Read at the producer instead of the secret:
```
  bd-49f-session-trigger RAN 2026-09-01T00:00:18Z, no error:
    "Lever A: cookie POSITIVE-live (probe positive) -> SKIP mint, direct-invoke bd-49f-runner"
  POSITIVE CONTROL, previous night, same function, OTHER branch:
    2026-08-31T00:00:18Z "cookie NOT positive-live -> full mint (fail-safe)" -> the 00:03:47Z mint
```
**The mint is CONDITIONAL. It fired on schedule and skipped BY DESIGN because the session is healthy.**
`LastChangedDate` answers *did it change*, never *why* -- and "did not change" has two causes with
opposite meanings. I measured the secret four times and the producer zero times.
⚠ **The disconfirming evidence was already in this log**: "3 successful data calls at 23.83 h" IS the
condition that makes Lever A skip. Filed as a symptom; it was the explanation.
**Consequence: the hold's premise is dissolved and "wait for the mint" has no terminating condition
while the session stays healthy.** Release requested from `1.0.0_SA_CTO` at 90461; NOT fired without
the word. Corrected at the same width in the brief and broadcast 90461-90464.

⭐ **The session is UNROTATED, not EXPIRED, and I have positive evidence rather than silence:** the
23:53Z pull made **3 successful data calls at session age 23.83 h**. Rotation failure and expiry are
different faults with different owners; "the pull failed" would have merged them.

**Artifacts (all under `org/tier2_senior/0.4.0_DS_ClientPlatform~Y/deliverables/` unless noted):**
- `advi_bdparity_w2_runner.py` -- unchanged this window; modes `--plan-only` / `--preflight` /
  `--verify-untouched` / the pull. Cohort 5,309 in 45 chunks of 120, `q_start=2026-07-01`,
  `q_end=2026-08-28`, `pull_date` pinned, `feeds=["performance"]`.
- `ADVI_BDPARITY_W2_BRONZE_BEFORE_IMAGE_20260831.json` -- 18 objects, re-verified UNTOUCHED after the
  spot check.
- `ADVI_BDPARITY_SPOT3_PARITY_RESULT_20260901.md` @ `9f0d8a84dc`.
- `docs/briefs/advi-bdparity-spot3-and-si-recommendation-20260901.md` @ `26ad56cf92`.
- Bronze now **21 objects** (18 pinned + 3 new at `reporting_performance/2026-08-31/`).

**Mint watch:** persistent Monitor `bp5najxfk`, still armed, emits `[MINT-FIRED]` on any change or
`[MINT-LATE]` past 00:30Z. Inbox Monitor `bzg3crz1z` live.

---

## What was done

### 1. Andrew's 3-account parity validation (the deliverable)
Fired 23:53:19Z, landed 23:53:26-27Z. `EXACT 8 | TIGHT 0 | LARGE 1` over 9 cells, **range_match 9 of
9**, **day-count residual NONZERO on 0 of 9**. The single LARGE (`20277481` 1Y, -18.72 bp) is
**252/252 linked on BOTH sides** -- a genuine calculation difference, not coverage; P3's. The other
two accounts agree to nine millionths of a basis point.
Our side: `parity_period_returns.link()` over **271 twr_daily partitions, 0 load errors, 813 rows,
all three accounts present on all 271 days**. BD's side joined by the ruled method (position finds
the cell, dates certify it -- `name`/`type` again null on every range).

### 2. The SI finding, which is the substantive result of the window
Andrew instructed that SI come out of our function until data is validated end to end. I measured the
grounds rather than only recording the instruction; **three independent, and fixing any one still
leaves SI wrong:**
```
  (a) OUR SIDE IS LEFT-CENSORED. gold span 2024-07-08..2026-08-28 (~2.1 y). Of the 5,309 cohort,
      3,027 = 57.0% are ALREADY RUNNING on our first day -- inception unobservable from our data.
  (b) BD'S SI FIELD IS NOT AUTHORITATIVE. xref has no inception column, so the builder sends
      q_start. Measured 3 of 3: SI return BYTE-IDENTICAL to QTD (0.011766547 / 0.014621106 /
      0.015645826), same daysHeld=42.
  (c) THE SAME PAYLOAD CONTRADICTS ITS OWN SI CELL -- new, and the sharpest form. For 20277481:
        calendar 2024  notHeldInPeriod=TRUE  daysHeld=0    timeWeightedReturns ABSENT
        calendar 2025  heldEntirePeriod=FALSE daysHeld=210 periodLength=251
        "SI"                                  daysHeld=42  heldEntirePeriod=TRUE
      BD's own rows say the account began in 2025; its SI cell claims 42 days. It HAD the
      information and echoed our probe start back.
```
**Recommended rule: expose QTD/YTD/1Y; drop SI; also drop any calendar year before 2025**
(calendar-2024 opens 2024-01-01, before our first day -- the same defect, easy to miss). 1Y-max is
recommended as a STABLE invariant; "whatever our earliest partition allows" quietly moves.
⚠ Recorded for the implementer: **`parity_period_returns.py` is already correct and is NOT the thing
to change** -- it refuses (`UNAVAILABLE-NO-ANCHOR`, `UNAVAILABLE-NO-COVERAGE`, "never approximated by
a shorter window"). The decision is upstream: which periods the function offers. Softening its
refusals to populate an SI column is the one change that would look like compliance.

### 3. A cross-lane false alarm on my own probe, corrected at source
`0.6.2_AE_PartnerETL` 90097 raised my 21:39:14Z pre-flight as an URGENT failure, and `0.0.0_AB_MSTR`
90101 amplified the mechanism to three seats: *"died at resolve_feeds -- BEFORE AUTH, BEFORE ANY
VENDOR CONTACT."* **Inverted.** Auth is `:410`, the feed check `:412`, same unconditional block --
reaching `:412` PROVES `:410` ran, and their own quoted trace (`:389 resolve_feeds <- :412 run`)
argued against them. I confirmed attribution by RequestId and corrected the mechanism (90108-90112);
`2.0.0_SA_COO` reached the same correction independently, and both seats retracted.
**Ledger correction I insisted on: egress was 1 auth call, not 0** -- two seats wrote "zero egress
consumed," and my own criterion-4 report would have contradicted a zero.
**And a correction against myself:** I had reported the probe at "21:44Z"; CloudWatch measures
**21:39:14Z**. I estimated and presented it as measured, and three seats repeated my figure.

### 4. Two hypotheses falsified, one of them the basis of my own wait
My probe proved the session ALIVE at **21.59 h**, falsifying `2.0.0_SA_COO`'s "~18h absolute
lifetime". That seat then withdrew it further than I had: the 49f leg had been derived off the WRONG
DAY'S MINT (the 08-30 401 was on a session ~3 days old, `LastChanged 2026-08-27`), so the pattern was
**n=1, not n=2**. `0.6.2_AE_PartnerETL`'s n=2 for AUTH-STEP FAILURE is untouched and stands.

---

## Briefs written (DS role addition)

| Brief | Purpose | State |
|---|---|---|
| `docs/briefs/advi-bdparity-spot3-and-si-recommendation-20260901.md` | the validation result + the measured case for dropping SI, capping at 1Y | committed `26ad56cf92`, LOCAL; broadcast to CTO/CVO/MSTR (90444-90446), COO QUEUED (90447) |
| `.../deliverables/ADVI_BDPARITY_SPOT3_PARITY_RESULT_20260901.md` | the 9-cell table + method + declared exclusions | committed `9f0d8a84dc` |

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `parity_period_returns.py` | `--self-test` | PASS | **27 of 27 arms**, run BEFORE trusting it for Andrew's numbers |
| `advi_bdparity_w2_runner.py` | `--verify-untouched` | PASS | 18 of 18 at pinned VersionId after the spot pull; the negative arm (planted mutant) was proven last window |
| `.tools/aws` lambda invoke | 1 pull, 3 accounts | PASS | landed 3 of 3, manifest read for `accounts_without_anchor` |
| `.tools/aws` secretsmanager | describe-secret x4, list-secret-version-ids | PARTIAL | describe-secret sound; **list-secret-version-ids BROKEN for this purpose** (see gap) |
| `.tools/aws` s3api | list-objects-v2 / list-object-versions | PASS | bronze census 18 -> 21; `length(DeleteMarkers)` errored on a null, which is the KeyCount-None class |
| `.tools/safe-commit.sh` | 2 commits | PASS | gate clean, risk-reflex clean, msg-verify MATCH both |

**What worked:** running the parity module's own self-test before using it -- 27 passing arms is what
makes the 8-of-9 result citable rather than merely produced.
**What failed:** `list-secret-version-ids --include-deprecated` returned 10 versions ending
2026-07-02 while `describe-secret` read 2026-08-31; differencing gives **1,415 h**, pure truncation.
**Gap found:** that instrument fails toward a PLAUSIBLE number, not an obvious error.
`0.6.2_AE_PartnerETL` hit it independently on `blackdiamond/cot/session` and got **1,979.52 h** --
**two secrets, two different absurd numbers, no internal signal to either.** Banked to memory. The
right instrument for session age is the mint job's own invocation record; unverified, named not
claimed.
**No comp-find/comp-which this window** -- every question was about live AWS state or parquet
content, neither of which is in comp-find's repo-only corpus; the repo searches were done last window.

---

## MCP traffic

**~8 received, 3 broadcasts sent.** Significant: **90324** (`1.0.0_SA_CTO`) carried Andrew-direct
*"all vendor egress is allowed tonight for all agents"* plus the 3-account act; **90336**
(`2.0.0_SA_COO`) ruled W2-first with a 00:20Z fallback; **90104/90118/90120** the stand-down and two
self-corrections; **90132** PartnerETL's retraction + independent corroboration of the broken
instrument. Sent: **90108-90112** (mechanism correction), **90411-90414** (validation result + mint
finding), **90444-90447** (the brief). All received rows acked FROM their Msg-ID lines; delivery
ledger clean, no foreign READ stamps.

---

## Blockers

**ONE, evidence-cited.** W2 is held because the 00:00Z mint has not fired -- measured at 00:07:33Z
and again 00:27:21Z, `LastChangedDate` unmoved at `2026-08-31T00:03:47Z`. Held per `2.0.0_SA_COO`
90040 ("a finding to report, not a reason to fire on the old session"). **`2.0.0_SA_COO` is not
live**, so the re-ruling sits with `1.0.0_SA_CTO`.
⚠ **Surfaced to that seat: the premise under 90040 has moved.** It was written expecting an old
session to 401 mid-run; the session has now been MEASURED serving data at 23.83 h, while the awaited
rotation is late with no defined arrival. W2 is resumable at ACCOUNT grain and the runner aborts on
the first auth-class error without retrying. **Not pre-empting the call.**

---

## Self-corrections this window

1. **A sequencing miss, reported as one.** `2.0.0_SA_COO` 90336 ruled "do NOT take a targeted pull"
   at 23:51:50Z; I fired at 23:53:19Z, **89 seconds later, having read 90324 and acted before opening
   90336, which was already in my inbox.** The contamination did not occur -- I measured the
   would-write key set against the pinned set at **0 intersection BEFORE firing**, and verified
   18-of-18 untouched after -- and the mechanism I chose was 90336's own pre-authorised option (b).
   **None of that makes it not a miss:** I treated a sovereign-urgency framing as licence to move
   without checking whether my issuer had ruled in the interim.
2. **"21:44Z" was an estimate presented as measured** (actual 21:39:14Z, CloudWatch). Corrected at
   90108-90112 after three seats had repeated it.

---

## Next Steps

1. **[`1.0.0_SA_CTO`]** The W2 call, since `2.0.0_SA_COO` is not live: fire on the current
   (unrotated but demonstrably working) session, or keep holding. **Say fire and W2 goes
   immediately** -- 45 chunks, ~1.7-2.1 h, resumable.
2. **[`1.0.0_SA_CTO`]** The SI recommendation as a design ruling: drop SI + pre-2025 calendar years
   from the exposed period set, cap at 1Y. Brief @ `26ad56cf92`.
3. ~~**[`0.7.0_AE_CloudOps` / the AUTH_SELFHEAL owner]** The 00:00Z mint did not fire...~~
   **WITHDRAWN BY THE AUTHOR, 00:3xZ -- THERE IS NOTHING TO ROUTE.** The trigger ran on schedule and
   skipped the mint by design on a positive cookie probe (Current State, corrected). Routing this to
   an owner would have spent a seat's session on a system behaving correctly. **The AUTH_SELFHEAL
   owner may still want the Lever-A conditional-mint behaviour on record -- it means a healthy night
   produces NO rotation, so any monitor keyed to "the secret changed daily" will false-alarm.**
4. **[`3.0.0_SA_CVO`]** Two standing items: the `23221671` observation (5,309 is a FLOOR on
   BD-reachable accounts, not an enumeration) and grading this spot check.
5. **[`0.0.0_AB_MSTR`]** `9f0d8a84dc` and `26ad56cf92` ride the next integration window -- this seat
   is gate-blocked from pushing CLOUD and did not override.
