# MDPF trigger/upload sequence — why the served scopes are split across three vintages

**Author:** `1.0.0_SA_CTO` · **2026-08-10 ~13:0xZ** · **Measured at this seat, live**
**Origin:** Andrew-direct at the base CTO terminal, 2026-08-10, VERBATIM:

> *"The 'Global' view is on August 5th, Inflection is August 5th, and 49 and Cottonwood are both on
> August 6th. All of them should be on August 7th at this point, so we need to trace the routes and
> identify the basis for the delay."*
>
> He named two suspected causes: **(1)** *"how we've defined the timing/metronicity of these ingestion
> paths, which by the way these custom definitions are irrelevant now as api paths are always T+1 in
> that you get the prior days data sometime in the morning eastern time (we know its ~1:02am for Black
> Diamond)"*; **(2)** *"the timing of eventbridge rules, if the given scope's intake is after the mdpf
> floor schedule."*

> ⛔ **THIS DOCUMENT EXISTS BECAUSE IT SHOULD HAVE EXISTED BEFORE THE SPAWN NOTE.** I dispatched
> `2.0.0_SA_COO` and `0.7.0_AE_CloudOps` telling them *"the diagnosis is DONE, execute don't
> re-derive"* — for a diagnosis that lived only in my session context and in no committed artifact.
> COO correctly refused to execute a summary of a finding they could not read, and said so.
> **A DIAGNOSIS THAT IS NOT IN GIT IS NOT DONE; IT IS A CLAIM.** Same class as everything else this
> program keeps banking.

---

## 1 · BOTH HYPOTHESES CONFIRMED — and (2) is a consequence of (1)

**MEASURED** (`aws scheduler list-schedules` materialised client-side, 16 schedules, denominator
printed; each `get-schedule` read individually and normalised to UTC at EDT = UTC−4):

```
03:05Z  opal-assets-bd49f-dim-convert-daily        49f dim convert
03:30Z  wsb-49f-model-aua-pull-daily               49f model AUA        [TUE-SAT]
03:30Z  wsd-49f-partner-held-etf-pull-daily        49f partner ETF      [TUE-SAT]
═══════════ 13:00Z  mdpf-scheduled-floor  ◄── THE FLOOR BUILDS HERE ═══════════
13:15Z  smartx-rest-pull-daily                     49f / 0824    +15 min TOO LATE
13:30Z  smartx-assets-daily-pull-daily             49f / 0824    +30 min TOO LATE
13:40Z  mdpf-accrual-bridge-daily                                +40 min
13:50Z  opal-assets-mdpf-portal-publisher-daily    publishes what 13:00Z built
20:30Z  cot-bd-session-daily-et                    Cottonwood    +7.5 HOURS TOO LATE
22:30Z  opal-assets-ingest-mirror-cot-daily-et     Cottonwood    +9.5 HOURS TOO LATE
```

> ## ⇒ FOUR INTAKES FIRE **AFTER** THE FLOOR THEY FEED.
> The floor cannot see them **by construction** — not intermittently, not under load. Cottonwood is
> therefore **permanently ≥1 day behind**; 49financial misses **by minutes**.

**And hypothesis (1) is why the schedules look like that.** The late intakes are named for
business-hours rhythms — a *"session"* pull at 16:30 ET, a *"mirror"* at 18:30 ET — but the paths are
T+1: the data lands in the small hours and then sits.

**MEASURED:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_INGESTION_DRAW_VENDOR_TO_PLATINUM_20260804.md:112`
records **"BD xlsx lands (02:00Z nightly …)"**. `cot-bd-session-daily-et` fires at **20:30Z**.

> **WE WAIT 18.5 HOURS TO COLLECT DATA THAT IS ALREADY ON DISK.** Andrew's framing is exact: *"these
> custom definitions are irrelevant now."* The schedule encodes an assumed rhythm, not the real
> delivery.

## 2 · SERVED STATE — his figures confirmed, and they split into TWO causes

**MEASURED** (`s3://opal-data-portal-v2/platinum/mdpf/<scope>/aggregate-aua-timeseries.json`):

| scope | `as_of_last` | `generated_at` | cause |
|---|---|---|---|
| global | 2026-08-05 | 2026-08-07T03:52:12Z | **inherits inflection** — needs all three legs |
| inflection | 2026-08-05 | 2026-08-07T03:52:12Z | **cross-axis gate REFUSED it** (not scheduling) |
| 49financial | 2026-08-06 | 2026-08-07T22:47:09Z | **schedule ordering** (SmartX +15/+30 min) |
| cottonwood | 2026-08-06 | *(absent)* | **schedule ordering** (+7.5 / +9.5 h) |

⚠ **THE SPLIT IS THE LOAD-BEARING PART.** Two of the four are a scheduling defect and two are not.
`global` and `inflection` share a `generated_at` because they were written by the same run, and
49financial's `22:47:09Z` is **ten seconds before** inflection's refusal at `22:47:19Z` in that same
fire — the run advanced 49f and was refused on inflection.

> ⛔ **A SCHEDULE FIX MOVES COTTONWOOD AND 49FINANCIAL. IT DOES NOT MOVE INFLECTION OR GLOBAL.**
> Inflection is the cross-axis coherence gate (Andrew's separately-named next-highest priority,
> handoff `@3aac2c3e32`); global inherits it. **Any report that a retime made "MDPF current" would be
> wrong on two of four scopes.**

## 3 · THE INVERSION — carry it into any remedy

From the 08-07 evidence: inflection **REFUSED 16-minute-old data** at 22:47:19Z, having **PASSED on
two-day-stale data** at the 13:00Z fire. **It passes on stale and fails on fresh.** So moving the floor
later surfaces the refusal *more* often, not less — **a successful retime should be expected to make
the 6/12 count look WORSE**, and that is not a regression to repair toward.

## 4 · PROPOSED TARGET SHAPE — floor time unchanged

```
02:00Z  BD lands (measured)
~03:00-03:30Z  ALL intakes                    <- cot-bd-session, cot mirror, smartx pulls move here
13:00Z  floor — now strictly downstream of every intake
13:50Z  publisher
```

⚠ **STEP 1 IS MEASUREMENT, NOT EDITING.** BD's 02:00Z is measured. **SmartX / Orion / Eclipse are
NOT** — setting those from inference would repeat the exact error that produced this defect. The
per-vendor `updated` / `as of` tags are the source. **`0.7.0_AE_CloudOps~Z`'s MDPF_CANPLAT P0-2R
(arrived in the 913e84c3b8 site-Z merge) carries a measured SmartX/Orion/Eclipse clock read** — read
it before re-measuring; if an independent second derivation is wanted, measure BEFORE opening it, or
it is an anchor rather than a derivation.
**The COTTONWOOD move needs no further measurement** — 02:00Z delivery vs a 20:30Z pull is grounded now.

## 5 · Bounds

Schedules, served artifacts and the invocation policy are **measured live at this seat 2026-08-10
~13:0xZ**. The BD 02:00Z landing is **carried from the ingestion draw**, not re-derived. The
inflection refusal timeline is **carried from `2.0.0_SA_COO`'s brief `@efe8812873`**. I have **not**
exercised any schedule change, **not** read the failing per-date rows, and **not** resolved the open
A4-write fork from the handoff — so nothing here authorises a fix to inflection.
