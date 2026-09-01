# ADVI_49F — MIDSTREAM STATE BRIEF (the 49F canonical runner chain)

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Mode:** `/brief-create --midstream ADVI_49F`
**Authority:** Andrew-direct 2026-09-01 (the D2 member-set scoping instruction).
**Consumer:** `/endpoint --forward docs/briefs/advi-49f-state-brief-20260901.md` (step 2).

---

## PART 0 — HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**NOT READ:** `org/**/task_orders/ADVI_49F.*`; the project JSON's `phase` / `blocking`.
**READ:** the registry row's `name` / `description` / `prds`; D2 PRD; the live gold planes measured
this session; the chain source at `chain_49f_entrypoint.py`.

⛔ **WHERE IT BENT.** Like BDPARITY, this project **has no PRD of its own** — it points at the parent
D2 PRD and a sequencing brief. Its registry `name` is written as a *defect list* ("TWR-engine defect
remediation ... the in-kind zero-flow root cause, the c01 NNA sign fix, the P14 backfill vehicle, the
RPS custody repoint"), which is a **branch-shaped description of a base-shaped thing.** I have
authored Part I from what the chain is *for*, not from its defect list, and that is a deliberate
re-framing a reader should be able to challenge.

---

## PART I — THE OUTCOME TERRITORY

### O1 — Every 49F account has a daily return we can stand behind
For each account in the 49F book, each trading day, there is a return figure computed from our own
custodial data by one method, and someone can say how it was computed.
**Disputable by:** an account-day with no figure and no stated reason; two figures for one account-day.

### O2 — Money moving in or out never looks like performance
A contribution, a withdrawal, a fee, or an in-kind transfer changes what the account holds without
changing what the account *earned*. The engine distinguishes the two.
**Disputable by:** a return that moves when money moves.
⭐ *This is the outcome the in-kind zero-flow defect class attacks directly, and it is the reason the
chain is a D2 member rather than infrastructure housekeeping.*

### O3 — A figure that cannot be computed says so, in a way a consumer can act on
When an input is missing, the chain distinguishes "this is the first day of the series and there is
correctly no prior" from "this account genuinely held nothing" from "we could not compute this and
should have been able to". Three different states, three different renderings.
**Disputable by:** a refusal that reads the same as a genuine zero; a zero standing in for an
unknown.

### O4 — The chain tells the truth about its own run
Someone reading a day's chain output can tell whether it produced what it was supposed to produce.
A run that builds nothing does not report success.
**Disputable by:** a run that emitted no product and printed a pass.
⛔ *See Part IV Finding C. This outcome is currently FALSE, and its falsity is what hid a live
production regression for a day and a four-day repeated as-of before that.*

### O5 — The spine is one book, keyed once
Account → relationship → advisor → firm resolves one way, from one place, so every downstream product
(performance reporting, insurance, the roster) joins the same spine rather than re-deriving it.
**Disputable by:** two products disagreeing about which advisor owns an account.

### O6 — The chain runs itself, on a schedule, and its history is inspectable afterwards
It fires without anyone triggering it, and after it has run, what it did is readable without starting
a machine.
**Disputable by:** any diagnosis that requires booting a host to read what a run did.

---

## PART II — WHERE THE BOUNDARY SITS

**Owns:** the c-series canonical runner chain; the canonical gold tables; the TWR engine and its flow
handling; the chain's scheduling, staging and status reporting; the spine dimensions.

**Relies on / is relied upon:**

| project | relationship |
|---|---|
| `ADVI_PERFRP` | CONSUMER — the projection reads these canonical tables; PERFRP's emitters run as a stage *inside* this chain |
| `ADVI_INSURE` | CONSUMER — `insurance_nav_current` is a registered stage in this chain |
| `ADVI_BDPARITY` | GRADER — checks these facts against BD |
| `ADVI_49FSRC` | supplies the sourcing decision (complete/parked) |
| `OPAL_ADVIPOINTERS` | governs the canonical pattern this chain must conform to |

**Deliberately NOT this project:** the performance *reporting* product; insurance ingestion; the
parity method; the portal.

---

## PART III — THE QUALITATIVE BAR

No number in Parts I–III is a target.

⛔ **The failure mode here is SILENT CORRECTNESS LOSS.** This chain's outputs are inputs to everything
else in D2, so a wrong figure here is wrong in the product, in the parity check, and in the advisor's
mouth — and O4's current falsity means the chain will not tell anyone. That is why O4 is written as
an outcome rather than a monitoring nicety.

---

## PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

### FINDING A — the canonical gold tier IS in pattern and IS producing correctly
Measured 2026-09-01:
```
s3://opal-data-49financial/gold/advi/canonical/   8 tables
  accrual_materiality · canonical_positions · canonical_valuation · flow_ledger
  nna_atomic · nna_canonical · twr_daily · valuation_integrity
newest partition, canonical_valuation / flow_ledger / nna_canonical:  date=2026-08-31
twr_daily partitions:  ... 08-25, 08-26, 08-27, 08-28, 08-31
```
⭐ **The 08-29/08-30 absence in `twr_daily` is a WEEKEND, not a gap** — 2026-08-29 and 08-30 are
Saturday and Sunday. This is correct trading-calendar behaviour and a reader should not open an
incident on it. **Parquet in a per-firm product gold root is the ratified grammar; this tier
conforms.**

### FINDING B — the plan table the downstream design assumed DOES NOT EXIST
`fact_account_return_daily` (~50 columns, 8 groups) was assumed by the PERFRP design and **is not
there.** `twr_daily` carries **9 columns** (`account_id, business_date, r_net, r_gross, status,
flow_convention, provenance x3`). The gains trio (`account_gains` / `account_performance` /
`client_performance`) is **excluded from the scheduled chain by determination** and lands nowhere.
This is already ruled — consumers read the live canonical tables and declare absent columns — but it
is the single most load-bearing fact about this project for anyone designing against it.

### FINDING C — ⛔ THE STAGE CLASSIFIER CANNOT REPORT ITS OWN FAILURE
`chain_49f_entrypoint.py` maps **any** non-zero emitter rc to `emitter_refused`, and `emitter_refused`
is **excluded from `hard_fail`**. There is **no floor on `built`**. Therefore:
```
  eleven by-design refusals            ->  STAGE OK rc=0 hard_fail=0
  total failure of all eleven          ->  STAGE OK rc=0 hard_fail=0    (byte-identical)
```
and the reassuring line prints unconditionally. **A line that cannot be false is not evidence.**
This is why a four-day repeated as-of and then a complete production stop were both invisible from
any single run and surfaced only by comparing across days. **Remedy shape is a producer-lane call and
is not proposed here.**

### FINDING D — the runner is EPHEMERAL, which makes post-hoc diagnosis structurally hard
The chain runs daily at 12:45Z on an EC2 instance that boots, runs ~3 minutes, and self-halts. Its
run manifests are written to local `/tmp`. When the 09-01 stage produced nothing, the decisive
artifact was on the `/tmp` of a stopped host, and recovering it risked destroying it. **Untruncated
per-day chain logs ARE served off-box** at `s3://opal-data-49financial/gold/advi/_logs/` — that half
is good; the manifests are the half that is not.

### FINDING E — refusal reasons are written to three carriers and no consumer reads all three
`reason` (chain log, renders a bare dash because it reads stdout), `emitter_tail` (the full refusal
text), and `error` (a raw traceback — which doubles as a **box discriminator**, since a Windows path
means a laptop run and a POSIX path means the EC2 runner). At least two seats ruled an absence off
one field of one carrier and withdrew it.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. **The stage classifier must be able to fail** (Finding C) before O4 is achievable or before any
   freshness claim on this chain means anything.
2. **Run manifests must be readable after the run**, without starting a host (Finding D).
3. **One refusal-reason carrier must be canonical**, or every consumer must read all three
   (Finding E).
4. **The canonical column set must stay declared, never silently filled** — consumers declare absent
   columns rather than inventing them (Finding B).
5. **Trading-calendar behaviour must be respected by every consumer and every alarm-shaped reading.**
   Friday is Monday's answer; a T-1 default false-alarms every Monday.
6. **Ad-hoc runs stay QA-only.** Production evidence comes from the scheduled fire; an ad-hoc run can
   spend the discriminator the scheduled fire exists to produce.

---

## PART VI — STATUS ⛔ NOT OUTCOME-BEARING

*Measured 2026-09-01 ~19:30-20:30Z, `s3api` (UTC), plus source reads.*

**1. The canonical chain is healthy and current.** Eight tables, newest partition `date=2026-08-31`,
which is the correct as-of for 2026-09-01 under T-1 and the trading calendar.

**2. A live, uncaused production regression sits in a STAGE of this chain, not in the chain.** The
`perfrp_projection` stage built 6 of 11 families daily 08-27→08-31 and **0 of 11 on 09-01**, while
**fourteen other stages consumed the same partition and wrote 30 objects.** Today's partition holds
~6% *more* data than the last-good one. Nine mechanism hypotheses are dead. `2.0.0_SA_COO` ruled no
new causal story until someone measures what the chain run actually did.

**3. Two things established and not to be re-derived:** 08-29/30/31 all re-processed
`asof=2026-08-28` (correct calendar behaviour), so the before/after comparison **had no valid
before**; and the discontinuity is nonetheless real.

**4. `ADVI_INSURE`'s producer is now a registered stage in this chain** (re-armed 2026-09-01 ~17-18Z).
Its acceptance is the 09-02 12:45Z fire — **the same fire that is the next observation point for the
regression in note 2.**

**5. The project has no PRD of its own** and its registry `name` is a defect list (Part 0).

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not diagnose the 6-to-0.** That is live, owned, and explicitly not this brief's to solve
   or summarise beyond stating its status.
2. **It does not claim Finding C caused the regression.** Finding C explains why the regression was
   *invisible*, which is a different claim and the one the evidence supports.
3. **It does not propose a remedy for the classifier** — producer-lane call.
4. **It did not read the task orders**, and I am aware this project's TOs were reconciled against a
   later remediation design; that reconciliation's outcome is unknown to this brief.
5. **It re-framed the project from a defect list into a purpose** (Part 0). If that re-framing is
   wrong, Part I is wrong, and that is the challengeable claim here.
6. ⛔ **A task order serving something real that Parts I–III fail to name is evidence THIS BRIEF is
   incomplete.**

---

## REFS

```
BRIEF PATH        docs/briefs/advi-49f-state-brief-20260901.md
PROJECT           ADVI_49F  (directive D2, status active, registered 2026-08-27)
EXISTING PRD      NONE OF ITS OWN -- points at D2_ADVI_49F_E2E_PRD.md + d2-critical-path-sequencing
SIBLING PROJECTS  ADVI_PERFRP · ADVI_INSURE (both run AS STAGES in this chain) · ADVI_BDPARITY
PRIOR ART         chain_49f_entrypoint.py; the canonical gold tier; gold/advi/_logs/
MEASURED AT       2026-09-01 ~19:30-20:30Z
```
