# MDPF trigger/schedule remediation — DECOMPOSITION + SEQUENCE

**archetype:** COORDINATE
**Author:** `2.0.0_SA_COO` · 2026-08-10 · **Owner of decomposition + sequencing**
**Executes:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_TRIGGER_SEQUENCE_DIAGNOSIS_20260810.md` @087938fa61
**One workstream.** MDPF_REMED W1–W5 is the same subject and is not run as two.

---

## 0 · THE ONE FINDING THAT CHANGES THE TARGET SHAPE

> **THE TWO `opal-assets-ingest-mirror` SCHEDULES ARE NOT SEPARABLE BY FIRM. THEY ARE TWO CLOCKS ON
> ONE ALL-ROWS FUNCTION, AND THE NAMES SAY OTHERWISE.**

**SOURCE-CONFIRMED**, `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py:353`
@087938fa61:

```python
for row in MAP + PROVENANCE_RIDERS:      # :353 -- unconditional. `event` is NEVER consulted.
```

The handler iterates **every** row on every invocation. Both invokers pass an empty payload —
`infra/aws/terraform/opal-assets/mirror.tf:155` (`input = "{}"`) for the Scheduler entry, and the
`mirror_inf` EventBridge target for the other. **Neither schedule scopes to a firm.** `MAP` carries four
rows (`:94` orion/inflection · `:115` eclipse/inflection · `:122` blackdiamond/cottonwood · `:153`
cottonwood meta-templates).

**⇒ CONSEQUENCE FOR THE PLAN, and it is the reason this document leads with it:**

| | |
|---|---|
| The diagnosis's §1 table reads | `22:30Z opal-assets-ingest-mirror-cot-daily-et — Cottonwood +9.5 HOURS TOO LATE` |
| Measured (AE, live) + source (above) | That schedule drives **eclipse/inflection** bronze → silver. It is named `cot`; it is **not** a cottonwood-only intake. |

**So "move the cot mirror earlier" is not a cottonwood change. It moves an INFLECTION intake** — which
(a) sits inside Andrew's 12:00–13:30Z window, and (b) is governed by the inversion below. **The
diagnosis's proposed target shape cannot be executed as written**, because one of the three things it
moves is not the thing its name says it is.

*This is the R-20/R-32 class again — the label and the referent came apart, and the label is what a
plan acts on. Recorded, not blamed: CTO's own §5 bounds the table as a schedule read, and a schedule
read cannot see a handler's row loop.*

---

## 1 · WHAT IS ACTUALLY WRONG — four scopes, and the causes DO NOT share a remedy

Served state, measured by CTO 2026-08-10 ~13:0xZ (`platinum/mdpf/<scope>/aggregate-aua-timeseries.json`):

| scope | `as_of_last` | cause | in THIS workstream? |
|---|---|---|---|
| cottonwood | 2026-08-06 | schedule ordering | ✅ **YES** |
| 49financial | 2026-08-06 | schedule ordering (SmartX +15/+30 min) | ✅ **YES** |
| inflection | 2026-08-05 | **cross-axis coherence gate REFUSED it** | ⛔ **NO — CTO's thread** |
| global | 2026-08-05 | inherits inflection (needs all three legs) | ⛔ **NO — follows inflection** |

> ⛔ **A SCHEDULE FIX MOVES TWO OF FOUR SCOPES. IT DOES NOT MOVE INFLECTION OR GLOBAL.**
> Carried verbatim into every TO. Any report that a retime made "MDPF current" is wrong on half the
> product. Andrew's own framing named all four as late; **two of them are not a scheduling defect at
> all**, and that distinction is the first thing that must survive to him.

**Trading-calendar frame, resolved FIRST per the standing rule (2026-08-08 Sat / 08-09 Sun; today Mon
2026-08-10):** the expected frontier is **Friday 2026-08-07**. So `as_of 08-06` is **one** trading day
behind and `as_of 08-05` is **two** — real lag, not a weekend artifact. Stated so nobody re-derives it,
and so nobody inflates "three days" out of a wall clock.

---

## 2 · THE TWO CONSTRAINTS THAT BIND EVERY REMEDY

**(A) THE INVERSION — a successful retime should make the count look WORSE.**
Inflection **refused 16-minute-old data** at 22:47:19Z on 08-07, having **passed on two-day-stale data**
at that morning's 13:00Z fire. It passes on stale and fails on fresh. Moving intakes earlier surfaces
the refusal *more* often. **A 6/12 that degrades after a correct retime is the inversion predicting
itself — not a regression, and never something to repair toward.**

**(B) THE T-1 TRAP — the window may not be executable as literally stated.**
In steady state the floor is **not starving**: at 13:00Z on day D the newest orion partition is `date=D-1`
(written D-1 14:16Z) and the newest eclipse is `date=D-1` (written D-1 22:31Z). **Both are correct T-1
reads.** Moving intakes into 12:00–13:30Z and the floor to 13:30Z would have the floor read a partition
written ~10 minutes earlier **the same day**. W1-5's own `do_not` forbids silently converting a T-1 read
into a same-day one, and CLAUDE.md's first NEVER-rule makes T-1 the default for every AUM/holdings path.

**This resolves only on one unanswered question, and `0.7.0_AE_CloudOps` is resolving it now:**
**does `date=D` CONTAIN day-D data, or is it a run-date label on D-1 content?** No schedule moves until
that is answered. If it is a run-date label, the window is safe; if it contains same-day data, **honoring
Andrew's window literally breaks T-1** and the conflict is his to resolve, not ours.

---

## 3 · SEQUENCING DECISIONS I OWN — each with its reason on the record

**D-1 · P0-7R is OUT of this workstream. It is a DECOMMISSION item, not a schedule item.**
MSTR proposed folding it in as the other half of one NEVER#4 class. **Refused**, on CTO's R-31: NEVER#4
binds a **production** pipeline, and the `mdpf-daily-trigger` EC2 leg is deliberate cutover residue —
`scheduled-floor.tf:128`'s own comment names the same-apply atomic swap as intentional. Giving it a
schedule resurrects a closed path and leaves **two live producers on one floor**. CTO verified the leg by
measurement rather than filename (docstring `:1` + ec2/ssm clients `:186-187` + an invoke policy naming
only `mdpf-daily-refresh-trigger`) and confirmed **R-31 stands**. *Recorded either way so the call is
deliberate rather than an artifact of which finding reached a spawn note.*

**D-2 · W1-2 retires as SUPERSEDED, citing R-31 — with two carve-outs that are not optional.**
It hardens a freshness reader inside the condemned Lambda. **(i)** `0.7.0_AE` **commits the existing
132/36 first** — "condemned path" is not a licence to leave work uncommitted in a shared tree across
another dark window. **(ii)** The *insight* banks as a register row even though the code does not:
**"SILVER-FRESH IS NOT GOLD-COMPLETE"**, grounded on 08-07 where silver wrote at 16:00Z while the gold
chain failed at INF_C_01. That is true of **any** surviving path.

**D-3 · The work splits by GROUNDING STATE, not by firm.** A firm-shaped split would have put the cot
mirror in the cottonwood track, which §0 shows is wrong.

**D-4 · W1-5 is CORRECTED, not executed as written.** Its context table presents one landing pattern for
both prefixes. Measured: **orion was NEVER on the T+1 03:30 pattern** (same-day 14:16Z, unbroken 07-20→08-09),
and **eclipse left it three days ago** (now same-day 22:31Z steady). Its criterion 1 survives in its real
form — the declared producers do not reconcile with the measured landing — but the *reason* is that the
landing is driven by an **S3 ObjectCreated event** from a third function, not by either 16:00 sweep.

**D-5 · The mirror's 100%-failure is its own item and it is NOT the lag cause.** Do not fold it into the
retime; do not let the retime be credited with fixing it.

---

## 4 · THE TRACKS

### TRACK A — COTTONWOOD retime · **GROUNDED, blocked only by (B)**
`cot-bd-session-daily-et` 20:30Z → the early window. BD xlsx lands **02:00Z nightly** (measured), so we
wait **18.5 hours to collect data already on disk**. Andrew: *"these custom definitions are irrelevant now."*
⚠ **Track A does NOT include the 22:30Z mirror** — see §0. That schedule moves in Track C or not at all.

⚠ **CUTOVER GAP — MINE TO FLAG, AND THERE IS PRECEDENT IN THIS EXACT FUNCTION.** Moving a daily pull
across the clock either double-runs or **skips one business day**. That is not hypothetical here:
`ce99054e44` (committed 07-29, **applied 08-06T00:04:48Z**) moved the cot mirror and **`date=2026-08-06`
is missing from both feeds** — the cutover gap, measured. **And a missing trading day mid-series is
precisely what the cross-axis gate's limb (vi) fires on.** So a careless cottonwood retime can *manufacture*
the very refusal shape currently afflicting inflection. **Every retime states its gap plan before it applies.**

### TRACK B — 49FINANCIAL / SMARTX retime · **MEASUREMENT-GATED**
`smartx-rest-pull-daily` 13:15Z (+15) and `smartx-assets-daily-pull-daily` 13:30Z (+30) — misses by minutes.
⛔ **NOT ready.** P0-2R establishes SmartX silver lands 13:40–13:42Z and is **EARLY-INVALID on the current
clock**, but its own method limit is explicit: **silver LastModified measures when the CONVERTER wrote, not
when the vendor made data available.** It **bounds the current pipeline clock; it does not prove SmartX is
unobtainable earlier.** Moving the pull earlier without vendor-availability evidence sets a schedule from
inference — **the exact error that produced this defect.** Per P0-2R, the remedy targets
`smartx-assets-daily-pull-daily`, whose OnSuccess chain produces the binding silver.

### TRACK C — THE MIRROR · **HELD pending §0 + (B)**
Both schedules run all four rows. Any move is simultaneously an inflection change. **Held until the
partition-date question resolves AND Andrew rules on the window** (§5).

### TRACK D — MIRROR 100% FAILURE · **ROUTED, NOT IN THE RETIME**
`opal-assets-ingest-mirror` fails **every invocation**, ≥14 consecutive days (07-27→08-09, Invocations ==
Errors == 6.0/day; **14 days is the read window, not the failure's age**). Source-confirmed shape:
`_assert_landed_membership` (`:449`) is a **POST-WRITE** assertion, so rows 1–3 **write successfully**, then
the cottonwood row raises `ALIEN SURPLUS … 653 unexpected key(s)` (`:241`) — **and row 4
(cottonwood meta-templates, `:153`) therefore NEVER RUNS.** A green data path on a red function.
**This is not the lag cause** (the writes land) — but a producer reporting total failure for two weeks with
nobody seeing it is the silently-frozen class, and the 4th row's silent non-execution is a real gap.

### OUT OF SCOPE — INFLECTION + GLOBAL
The cross-axis coherence gate. CTO's thread, Andrew's separately-named next-highest priority. CTO's
`(a)`-vs-`(b)` A4-write fork is **still open** — whether inflection also failed at 13:00Z unlogged, or the
consolidator no-ops. **Until that resolves the morning error list is not trustworthy as a record, and
nothing I sequence rests on it.**

---

## 5 · THE ONE CALL THAT IS ANDREW'S — surfaced, not adjudicated

**His window was set on a premise that measurement has since changed.**

On 08-07 he ruled: *"all that shit that we need from inflection should be somwhere between 12:00 and 13:30
so any orion/eclipse ingestions, need to be in there"* and *"i am ok with moving mdpf_scheduled floor to
13:30, as long as whatever it needs from inf is at least 10 min before that."* At that time the record
showed orion+eclipse landing **T+1 at 03:30Z**. **Measured now: orion is same-day 14:16Z and was never on
that pattern; eclipse is same-day 22:31Z.**

**Two candidate shapes, and they are not equivalent:**

| | shape | T-1 effect |
|---|---|---|
| **his** | intakes into 12:00–13:30Z, floor → 13:30Z | floor may read a **same-day** partition — possible T-1 break |
| **CTO's §4** | intakes → ~03:00–03:30Z, **floor unchanged at 13:00Z** | preserves T-1; floor stays strictly downstream |

**Both satisfy his stated goal** (every intake strictly before the floor). **They differ on whether the
floor keeps reading T-1.** I am not choosing between a sovereign instruction and an architectural
preference. **Routed to Andrew via MSTR with the measurement attached.** Track A and Track C do not apply
until he rules or the partition-date answer makes the question moot.

---

## 6 · INSTRUMENT DEFECT FOUND WHILE DOING THIS — register candidate

**`comp-trigger` reports `TF-DESIRED: not found in infra/aws/**/*.tf` for a resource that IS
Terraform-managed, when the resource name is INTERPOLATED.**
`opal-assets-ingest-mirror-cot-daily-et` is declared at `infra/aws/terraform/opal-assets/mirror.tf:138-149`
as `name = "${local.mirror_name}-cot-daily-et"`. A literal text search cannot see it. My own confirming
grep reproduced the same false absence, and only reading the file resolved it.

**WHY IT MATTERS MORE THAN A COSMETIC MISS: "live but not in Terraform" reads as console drift, and the
natural next move on console drift is a console fix — a NEVER-rule violation, reached by trusting a tool.**
The failure is silent and confident. Positive control that discriminates: `cot-bd-session-daily-et`
(literal name) **was** found in the same run.

---

## 7 · WHAT HAPPENS NEXT, IN ORDER

1. **`0.7.0_AE_CloudOps`** — resolve `date=D` semantics (contains D, or run-date label on D-1). **Blocks A and C.**
2. **`0.7.0_AE_CloudOps`** — commit the W1-2 132/36; then W1-2 flips `superseded` (D-2).
3. **COO → MSTR → Andrew** — the §5 window call, with the measurement.
4. **Track A** on his ruling + the date answer, **with a stated gap plan**.
5. **Track B** only after vendor-availability evidence.
6. **Track D** routed as its own item.
7. **Inflection/global** stay with CTO. **Nothing here is reported as fixing them.**

---

## 8 · BOUNDS

Source citations (`lambda_function.py:353/:94-153/:241/:449`, `mirror.tf:138-155`) are **read at this seat
at HEAD @087938fa61**. Served-state figures and the 16-schedule census are **carried from CTO's diagnosis**,
not re-derived. Landing times, CloudWatch failure counts, the `ce99054e44` apply date and the denominators
(139 rules / 16 schedules) are **carried from `0.7.0_AE_CloudOps`'s live reads**, credited not re-measured.
The BD 02:00Z landing is carried from the ingestion draw. **I have exercised no schedule change, and
nothing here authorises one.**
