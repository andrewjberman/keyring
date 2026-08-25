# OWED SEATINGS + OPEN SOVEREIGN CALLS — `2.0.0_SA_COO`, 2026-08-25

**Why this file exists:** three seatings are owed and **all three are held behind the same event** (the
`MDPF_COTREMEDIATION` P0 clearing). **An obligation held on an event, recorded only in a message,
lapses silently when the session ends** — and CTO named exactly that risk for the S7 caveat: *"if you
hand the channel to a successor, that caveat obligation travels with it or it silently lapses."*

**This is the artifact that carries them. A successor COO reads this file.**

---

## OWED SEATING 1 — the 3F-S5 LAMBDA-TWIN DEPLOY

| | |
|---|---|
| **class** | AE. Named owner `0.7.0_AE_CloudOps` (@`1351c74d96`, *"0.7.0 lambda-twin rides TF"*) |
| **held until** | the P0 clears |
| **age** | deferred 2026-07-23 — **33 days, the ride never happened** |
| ⛔ **BINDING PRECONDITION** | **`S5_TWIN_SEATING_PRECONDITION_20260825.md` — CITE IT IN THE TO OR THE DISARM DID NOT HAPPEN.** `PROVENANCE_CONTRACT_START` must be resolved **before the twin ships**, because shipping is the moment the hazard arms. First cell of that TO is the DS-lane consumer read that could falsify the preferred one-line remedy. |

**It is also the REMEDIATION half of an armed residual already disarmed in place:** the
`vendor-manifest.sh --check` rc=1 (2 of 8) that `0.5.0_AE_OpalETL~B` marked at `BUILD_MANIFEST.json`.
**The disarm is done; the gate goes green only when this ships.**

---

## OWED SEATING 2 — `OPAL_ASSETS` NEEDS A NAMED OWNER

**Not a sweep. A look.** ⛔ **Three seats hit this project from three unrelated angles inside one
hour:**

```
2.0.0_SA_COO    Class-A discriminator   "pending -- go received" TO on a project marked TERMINAL
0.0.0_AB_MSTR   spawn-target check      V2-8.silver-converters PENDING 42d -> base seat not legal
1.0.0_SA_CTO~X  B-class census          OPAL_ASSETS ... Grand Consolidation P2, malformed code field
```

> **That is a signal about the project, not about any of the three sweeps. It is where our records
> disagree with themselves.**

⛔ **It must NOT be touched by a fourth sweep aimed at something else** — which is precisely what
would happen if S1 or S3 reaches it before it has an owner. **CTO~X's recommendation and MSTR's agree
with mine: give it a named owner rather than three seats routing around it.**

---

## OWED SEATING 3 — the ESTATE-REPORT CAPTURE/UPLOADER (the frozen-corpus remediation)

| | |
|---|---|
| **class** | **AE**, per CTO routing 70850 — traced, not assigned by topic |
| **where it lives** | `infra/aws/ec2/estate-report-runner/estate_report_runner.py` · `EC2_MANIFEST.json` → `estate-report-runner`, `i-0512bd3cbaf602b7f`. **A registered EC2 service, so this is an EC2-service INPUT LEG** — AE/infra under Rule 13 |
| **project** | **needs registering and TAGGING TO ITS DIRECTIVE AT CREATION** (Andrew ~14:12Z). Best fit **D0/infrastructure**; none of D0's three current members is a natural home, so this likely **mints a new project**. MSTR owns the register row. |

⛔ **NOT `3.0.0_SA_CVO`, AND THE REASON IS INDEPENDENCE, NOT CAPACITY.** The estate report is the
instrument CVO adjudicates with — `/estate-pull` is their loop and the 160 proposals are their
ratification pipeline. **A verifier who builds their own evidence source has removed the separation
that makes the verification worth anything.** *Recorded here so nobody later "helpfully" reassigns it
to the seat with the most context.*

⛔⛔ **THIS IS A MISSING INPUT, NOT MISSING DETECTION. NEVER#13 BINDS.** The deliverable is a
capture/uploader that keeps the corpus current. **Nobody may read this as licence to build a
freshness checker, corpus monitor, or alarm.** The instrument **already** prints
`corpus_freshness: STALE`, prints the vintage, and names the missing tool in plain English.
**Detection is not the gap — and building it here would be worse than useless, because it would make
the frozen corpus feel handled.**

---

## OPEN SOVEREIGN CALLS — AT ANDREW, NOT DELEGABLE

### CALL 1 — the 160 estate-report proposals stand on a corpus frozen 25 days

Measured by CVO across 8 days spanning 08-06..08-25: `corpus_newest_source_commit_utc =
2026-07-31T02:23:07Z`, `nuggets_total = 153`, `corpus_predates_window = True` — **every day.**

**Every one of the 160 proposals cites a `[SOVEREIGN]` ruling set that excludes 25 days of his
rulings** — today's D8 re-mint, Rule 26, Rule 27, the pipeline ratification.

⛔ **The hazard is not a broken report; it is a SOVEREIGN RATIFICATION ACT ON STALE GROUND.** Semantic
changes are naming acts: pipeline proposes, **Andrew ratifies**, CVO lands. A proposal grounded on a
corpus that cannot see a ruling he made two weeks ago **can contradict it, and ratifying it makes the
contradiction canonical.**

**CVO has DISARMED it** (the caveat goes into the ratification ask, so he is told before he rules).
**The CALL is upstream of that: whether to adjudicate at all before the corpus is current.** That is
a different decision from how to adjudicate, and it is his.

### CALL 2 — the spring-clean BAR

Rule 25's 90d selects **ZERO** open projects (oldest `YALP_MACROS` at 80.9d, positive-controlled by
CTO~X against two independent age signals plus a bulk-clock-reset check). **60d selects 12; 30d
selects 45.**

**Neither CTO~X nor I will pick.** Choosing a threshold is a Rule 24 taxonomy act and it is his.
⛔ **And the consistency work needs NO bar at all** — which is CTO~X's reframe and the load-bearing
half: **the debt is CONSISTENCY, not AGE.**

---

## THE ONE CONDITION THAT TRAVELS WITH S1 WHOEVER RUNS IT

**S1 (Class A close-out) runs the timestamp discriminator as a PRE-FILTER** — TO last-touched vs
project-JSON last-touched — **and routes the newer-than-close set to a human read, not the sweep.**

Measured: **97 open TOs on terminal projects; 87 stale by construction; 10 where the TO is NEWER**,
and **the project's terminal status may be the false side.** ~90% proceeds untouched.

⛔ **Closing those 10 blind would erase the only evidence that a project was closed prematurely.**
Adopted by CTO~X unreservedly. **It is not an age bar and needs no sovereign word.**

*(Distribution, measured, in case a seating question returns: `ANY_EXEC` 40 · `POD4_OR_EXEC` 20 ·
`CLOUD_COMP_TESTER` 17 · `SHARED_CLOUD_OPS_OR_EXEC` 15 · `ANY_POD_OR_EXEC` 3 ·
`SHARED_OPAL_ETL_OR_EXEC` 2 = 97. **41% is exec-only by construction**, which is why "a fresh Tier-2
lane" was never the answer and no spawn was needed.)*
