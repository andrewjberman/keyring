# 0.4.0_DS_ClientPlatform~T -- D1_CATVIEWS.TO-I1-DS: the path-to-live channel enumeration (2035-2340Z)

**archetype:** TRACE
**secondary_archetypes:** VALIDATE · SCRIBE

Window: since `aa64961557` (2026-08-26T20:34:49Z). Continues
`global_union_fix_and_a9_MET_1850-2035Z.md`. D8 closed at 2035Z; this window is one new
dispatch, delivered and ratified, plus an `/open-calls` at Andrew.

---

## SUMMARY

New TO seated at 21:21Z (`2.0.0_SA_COO` 73727), delivered at 22:27Z, **RATIFIED at 22:29Z**
(73935): AC1/AC2/AC3 PASS, AC4 correctly APPLIED-GATED.

**The cut question was "which of two code channels does each pinned module reach, and which does
the scheduled floor execute" -- and the answer is that the axis is THREE-VALUED.** A pinned module
reaches EC2 by a route no deploy path can refresh.

`2.0.0_SA_COO`'s ratification: **the surprise outweighs the TO.**

---

## WORK DONE

| commit | what |
|---|---|
| `a6c2bac919` | the deliverable + the proof-of-spec instance at the TO's declared path |

**Push state MEASURED:** LOCAL ONLY -- `git fetch origin CLOUD` (tip `c6f803e0b8`), ancestry
against the FETCHED ref, positive control `8d87d4784c` reads ON ORIGIN. Not a default.

---

## FINDINGS

### F12 -- THE TO's DENOMINATOR IS A VINTAGE, NOT AN ERROR

The TO says **"19 pinned modules."** Measured:

| source | entries | `.py` |
|---|---|---|
| PACKAGE at HEAD | **22** | 18 |
| PACKAGE at the running pin `1b96f70ad3` | 21 | 17 |
| PACKAGE at `a4d71e9544` (**2026-08-06**) | **19** | 16 |
| **THE EXECUTING ARTIFACT** (deployed zip) | **23** | 18 |

`19` was true 20 days ago. The executing artifact's 23 = 22 members + a builder-GENERATED
`BUILD_MANIFEST.json`. **Operative denominator: 22, printed beside every count. Reconciled, not
silently adopted** -- adopting it would have produced a correct-looking table over a wrong
population, which is the class this estate spent the night on.

### F13 -- THE SWEEP RETURNED A THIRD VALUE (AC2's whole point)

Five candidate routes, each built so it COULD fire:

| route | instrument | result |
|---|---|---|
| ZIP | downloaded the deployed artifact, enumerated members | 22 of 22 |
| S3 code channel | `safe_deploy_core.file_to_s3_target` + `head_object` | 17 of 22 have an object |
| **LAYERS** | downloaded BOTH attached layers, 1,507 entries | **controlled negative** -- third-party deps only |
| **EC2** | `EC2_MANIFEST.json` exact-filename sweep, +/- controls | **FIRED -- 3 of 22** |
| **runtime fetch** | read the EXECUTING handler's own bytes | **controlled negative** -- `get_object` reads DATA, `importlib` loads the PACKAGED comparator from a local path |

**Axis: `lambda-zip` | `s3-code-channel` | `ec2-distribution`.** A clean two-value result was
reachable and is not what came back.

**EXECUTING CHANNEL FOR THE SCHEDULED FLOOR: THE ZIP, FOR ALL 22.** `build_package.py` assembles
from an immutable pin via `git show` (`:230-232`) and refuses a symbolic ref; the lambda runs
`/var/task`. **The S3 code channel is not on the scheduled lambda's execution path at all** --
`D1-inv-5` as a measurement rather than a caution.

### F14 -- ⛔ THE SURPRISE: A NO-WRITER ROUTE ON THE FILE `NEVER#1` MAKES LOAD-BEARING

`trading_calendar.py` has **THREE routes and NO WRITER for the one an EC2 service consumes.**

- **ZIP:** present, built from `lib/trading_calendar.py` at the pin.
- **S3:** an object EXISTS at `code/scripts/gold/trading_calendar.py`, 6,979 B, **2026-08-11**.
- **`file_to_s3_target("lib/trading_calendar.py")` returns `None`** -- no DS deploy path writes
  that key. It was placed by a one-off recovery (`EC2_MANIFEST` cites the 2026-08-11 WS-A ledger).
- **`mdpf-daily-runner` (EC2) distributes FROM that key.**

>> **A change to `lib/trading_calendar.py` reaches the lambda via the next pin and DOES NOT reach
>> the EC2 runner. No instrument reports it: `comp-pipescript deployed` resolves the repo->S3 pair,
>> and for this file that pair does not exist.** <<

Same shape as tonight's D8 defect one layer out -- a delivery route whose currency nobody owns --
on the file every staleness verdict in the estate stands on.
**RECORDED, NOT CHASED** per the refactoring/migration embargo (Andrew ~20:32Z). Surfaced to
`3.0.0_SA_CVO` cc the issuer; this lane kept working.
`partner_roster.json` and `mdpf_model_registry.json` read EXISTS/NO-WRITER too. Stated, no action.

### F15 -- `inv-5` CAUGHT ME MID-TASK (the third seat in one night)

Reading `build_package.py` **AT THE RUNNING PIN** showed `mdpf_category_registry.py` ABSENT from
its PACKAGE list. **I was one step from reporting the registry is not in the running bundle. THE
ZIP BYTES SAY IT IS.** The pin is an ephemeral cherry-pick whose `build_package.py` is an older
vintage than the builder that actually ran.
**Rule 22a's ephemeral-pin clause `@4424c948f7` -- landed hours earlier after two OTHER seats hit
it independently -- arriving a third time in one night at a third seat.** Read the bytes, not the
graph. The clause earned its place the same day it was written.

### F16 -- A WRONG INTERMEDIATE READING, RECORDED RATHER THAN ONLY THE RIGHT FINAL ONE

My first EC2 sweep matched module **stems** and I read its output as containing two false
positives -- and said so mid-work. The exact-filename re-run **with a positive control**
(`mdpf-accrual-bridge.tar.gz` -> 1) **and a negative control** (`zzz_nonexistent.py` -> 0) shows
**all three hits are real**: `partner_roster.json` is named inside the accrual-bundle leaf, past
where my first 160-char display truncated.
**Two sweeps, same count, different reasons. Only the controlled one is evidence -- and the
uncontrolled one happening to AGREE is the worse outcome, because agreement retires the question.**

---

## ACCEPTANCE

| id | status | note |
|---|---|---|
| `I1DS-AC1` | **PASS** | 22 of 22 classified, executing path named, denominator printed + the TO's stale 19 reconciled |
| `I1DS-AC2` | **PASS** | 5 candidate routes, 1 third route CONFIRMED, 2 controlled negatives |
| `I1DS-AC3` | **PASS** | every claim grounded on the executing artifact / head_object+404 control / layer bytes / manifest with controls |
| `I1DS-AC4` | **APPLIED-GATED** | expected terminal status, NOT PASS |

**CELL STATUS -- written ONLY from observed states, never synthesized from criterion verdicts:**
`D1-i-1` **OBSERVED-COMPLETE** · `D1-i-2` **OBSERVED-DID-NOT-EXECUTE** (I observed the fence and the
decision; I observed NO property of a re-pin, because none occurred) · `D1-inv-5` **OBSERVED-HELD**
(a binding constraint that changed my method -- NOT "verified" as an estate property, which is not
what an invariant cell asserts).

**AC4 / THE NO-SHIP FENCE:** no re-pin, no `safe-apply`, no pin advance performed **or proposed as
ready**. **THE TRAP WAS MET AND BEHAVED AS PREDICTED:** `mdpf_category_registry.py` IS present in
the running bundle, and **its presence is not evidence of safety** -- it is the inert copy the
fence protects. A disarm condition being met is not a ship decision.

---

## DELIVERABLES WRITTEN

| artifact | commit |
|---|---|
| `D1_CATVIEWS.TO-I1-DS_PATH_TO_LIVE_CHANNEL_ENUMERATION.md` | `a6c2bac919` |
| `D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json` (at the TO's declared `instance_path`) | `a6c2bac919` |

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `safe_deploy_core.file_to_s3_target` | imported, called per member | PASS | used the DEPLOY'S OWN resolver rather than re-deriving the bucket/prefix map by hand; its `None` returns are what surfaced the NO-WRITER class |
| `safe-commit.sh` | `-F <msgfile>` | PASS | message authored with a non-shell writer per Rule 14a |
| `commit-gate.sh` | via safe-commit | PASS | doc + JSON only |

**`comp-pipescript deployed` -- DELIBERATELY NOT USED, and the reason is the finding.** It
certifies the repo->S3 code-channel pair and is **structurally silent about the lambda bundle** --
the exact gap this TO exists to enumerate, and the gap that made `trading_calendar.py`'s third
route invisible. Using it would have answered a different question cleanly and wrongly.

**What worked:** downloading the EXECUTING artifact and the LAYERS rather than reasoning from
declarations. Every material finding this window came from bytes.
**Gap found:** none new in the tools; the `comp-pipescript` blind spot is the one already carried
from the prior log, now with a second, sharper instance (a file with NO repo->S3 pair at all).

---

## MCP TRAFFIC

~12 handled, all acked (READ clock). Significant: `2.0.0_SA_COO` 73727 (the GO), 73759 (the
absorbing amendment + the `D1-i-3`-is-not-in-your-TO seam), 73935 (RATIFIED). Sent: 73728 (ACK
with the trap pre-acknowledged and AC4's expected status pre-registered), 73924/73925/73926
(delivery + the surprise to CVO).

---

## BLOCKERS

**None.** TO delivered and ratified.

---

## CURRENT STATE

`D1_CATVIEWS.TO-I1-DS` is **DELIVERED AND RATIFIED** (`a6c2bac919`, LOCAL, rides integration).
Deliverable + proof instance at
`org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/`.

**The estate fact this window establishes:** the mdpf-gold code path has **three** delivery
channels, not two; the scheduled lambda floor executes **the ZIP for all 22 pinned members**; and
`lib/trading_calendar.py` reaches an EC2 consumer through an S3 key **no deploy path writes**.

`D1-i-2` remains **APPLIED-GATED** behind the D1_CATVIEWS NO-SHIP, whose lift is Andrew's by-name
word. At the lift it re-seats to an AE lane as its own TO (`0.6.2_AE_PartnerETL~A` is the natural
seat; seat selection is the issuer's).

**Scope boundary held:** `D1-i-3` joined surface (i) at `@eb73d94342` and is NOT in this TO's cell
set (3 cells / 4 criteria). Nothing else on `D1_CATVIEWS` was touched.

**`/open-calls` run at 23:37Z: ONE call at Andrew** -- lift the D1_CATVIEWS NO-SHIP by name?
**REC: NOT YET** (loadable is not the bar; the decomp carries a live re-cert refusal on postulate
(i)). Three candidates were EXCLUDED as already-ruled or not-sovereign: the serve decision
(answered 20:15Z), the `Sleeve - Tax-Free Bond` bucketing (answered 18:0xZ), and the
`trading_calendar` embargo-exception question (COO's to apply, and that seat holds it).

---

## NEXT STEPS

1. **[`3.0.0_SA_CVO`]** the `trading_calendar` no-writer surprise -- filed, that seat's to
   disposition.
2. **[`2.0.0_SA_COO`]** whether the no-writer route meets the embargo's "blocks a product from
   shipping correct data" exception. Not escalated past that seat.
3. **[Andrew]** the NO-SHIP lift, whenever -- nothing is blocked on it.
4. **[`0.4.0_DS_ClientPlatform~T`]** idle, reachable, event-driven.

---

## DO NOT

- **Do not read `comp-pipescript deployed` as covering the lambda bundle.** Second instance this
  session; for `trading_calendar.py` the repo->S3 pair it needs does not exist at all.
- **Do not resolve an ephemeral pin's package contents from that pin's `build_package.py`.** It is
  an older vintage than the builder that ran. Read the zip.
- **Do not quote a count from a stem-matched sweep.** Exact-match it with both controls; two
  sweeps agreeing for different reasons is the trap, not the confirmation.
- **Do not read `mdpf_category_registry.py`'s PRESENCE in the bundle as safety.** It is the inert
  copy the fence protects, and a pin advance destroys both its properties.
