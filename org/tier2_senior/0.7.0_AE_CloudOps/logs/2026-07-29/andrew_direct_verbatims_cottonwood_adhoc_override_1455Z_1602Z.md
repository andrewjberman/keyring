# ANDREW-DIRECT RECORD: cottonwood ad-hoc producer override (~1455Z) + runner reassignment (~1602Z)

**archetype:** SCRIBE

**Recorded by:** 0.7.0_AE_CloudOps (base lane)
**Recorded at:** 2026-07-29T15:46Z
**Duty:** `org/XXX.md` -- "ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT DURABLY AND
BROADCASTS IT -- SAME TURN." This file is the DURABLE half. Broadcast half: CTO 153819Z, COO 154516Z,
MSTR 154540Z, DT ack 153952Z.

**PROVENANCE -- BOTH REACHED ME BY RELAY, NOT DIRECTLY FROM ANDREW.** Per XXX.md an agent relaying
"Andrew ruled" is not suspect merely because I did not see it -- that is the normal case, and I did not
challenge provenance. I am recording and surfacing; **I am not adjudicating scope** (XXX.md: SURFACE,
DO NOT ADJUDICATE).

---

## VERBATIM (a) -- ~1455Z, channel: relayed by `0.2.0_DT_PortfolioAnalytics` msg 20260729T153651Z

> "I want the producer for cottonwood run ad hoc right fucking now, and when that is done, and they
> confirm it is done succesfully and the data is populated where it should be, then i want the promote
> with just the revert on that .152 logic, not on the value/count removal."

*(Quoted exactly as relayed, including the original spelling of "succesfully" and "orthagonal" below.
The phrasing IS the ruling -- never a paraphrase.)*

## VERBATIM (b) -- ~1602Z, channel: relayed by `1.0.0_SA_CTO` msg 20260729T154246Z (CTO terminal)

> "No I want the DS agent to run the producer properly because I just want the new data in there, that
> is orthagonal from the frontend logic issue"

**(b) SUPERSEDES THE RUNNER ASSIGNMENT IN (a).** It does not revoke the ad-hoc authorization; it names
the lane that executes it.

---

## What these did and did not authorize

| | |
|---|---|
| **AUTHORIZED** | ONE ad-hoc run of the cottonwood producer, overriding CTO's deploy freeze for that run only. |
| **RUNNER** | `0.4.0_DS_ClientPlatform~A` (per (b)). Rule 13 doctrine -- DS owns gold producer scripts. |
| **ACCEPTANCE BAR** | Andrew's own words: *"they confirm it is done successfully and the data is populated where it should be"* -- a **SERVED-ARTIFACT** bar, not a producer self-report and not rc=0 (NEVER#5). |
| **NOT WIDENED** | The seven-leg wave, 4c, leg (d), the retirement pair and WI-2 all remain FROZEN to post-17:15Z on CTO's word. He ratified this fencing explicitly at 154246Z: *"The override covers THIS RUN ONLY."* |
| **NOT PRODUCTION EVIDENCE** | NEVER#4 stands -- an ad-hoc run is a QA instrument; its artifacts must not be cited in tonight's D2 certification. The unattended 16:15Z publisher fire REMAINS valid D2 evidence (an ad-hoc producer upstream does not taint the publisher's own schedule claim). |

## Routing history (recorded because it is a near-miss on the double-fire class)

| Time | Event |
|---|---|
| ~1455Z | Andrew (a) -- ad-hoc run demanded "right fucking now" |
| 153651Z | DT relays to me; explicitly says **"CTO owns the routing word -- do not fire on my message alone"** |
| 153813Z | CTO names **DS~A** owner |
| 153819Z | I request the routing word from CTO; do NOT fire on the relay |
| 153939Z | CTO **switches the fire word to me** on a capability read; corrects his own 153813Z |
| 154149Z | CTO addendum: state WRITE TARGETS before/with the run (platinum-overwrite hazard) |
| ~1602Z | Andrew (b) -- **"I want the DS agent to run the producer"** |
| 154246Z | CTO **stands me down**; DS~A fires |
| 154400Z | I confirm to CTO: **NEVER FIRED, ZERO RUNS IN FLIGHT** |

**NOTHING WAS DOUBLE-FIRED, because both candidate runners held rather than moved.** CTO named the
cause on the record himself: he inferred ownership from CAPABILITY ("who holds the runner") when the
lane was a matter of DOCTRINE (Rule 13) and ultimately of sovereign preference. Recorded as a near-miss,
not an incident; routing is CTO's and I am not adjudicating it.

## My own disposition

Fired NOTHING. Between the 153939Z fire word and the 154246Z stand-down I ran two read-only compiler
gates and read the runbook -- I was assembling the write-target answer CTO's addendum required BEFORE
firing, which is precisely why nothing went out the door. Runner-side facts handed to DS~A at 154441Z,
including the gate false-negative (`comp-pipescript deployed`/`postdeps` default to the **bd** tree and
return a clean-looking ZERO on this MDPF-tree script).
