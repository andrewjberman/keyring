# The STEP-4 SURFACE MANIFEST -- the section a PRD needs so step 5 is mechanical

**Author:** `2.0.0_SA_COO` · 2026-09-02 · **Status:** PROPOSAL, not law. Nothing refuses on it.
**Occasion:** Andrew ran ETFS_GUARDRAIL as a live test of the canonical loop and asked what step 5
expects from step 4. This is that answer as a fillable contract, plus the ETFS_GUARDRAIL instance.

**Authority it sits under:** the canonical loop spec
`org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` s.2.1-2.3
(step 5 = atom-decomp + the 7-lens preflight, each disposition carrying a denominator or a blindness
statement). Ownership map, Andrew-direct 2026-09-02: CRO 1 | CTO 2,3,4 | **COO 5,6** | worker 7 |
CVO 8,9,10.

---

## 1. The gap this closes, stated as a measurement and not a complaint

`ETFS_GUARDRAIL_PRD.md` is a good purpose-level document. It carries the arc, the rulings, nine
numbered acceptance properties, and a Territory table. **What it does not carry is a single
resolvable address.** Its OWNS cell says *"the catch-up inside `cot-etf-ownership-daily`"* -- a name,
in prose.

> **A comp-tool takes a SUBJECT. Step 4 handed step 5 no subjects.**
> Every one of the 7 admitted lenses needs a path, an ARN or a function name to run against. So the
> first act of step 5 was not decomposition, it was **discovery** -- and discovery is the half that
> should be mechanical.

**What that cost on this project, measured:**

| Found only by going looking | Why it changes a TO |
|---|---|
| `trading_calendar.py` exists in **4** places -- `lib/` (the CLAUDE.md "one frontier") + 3 vendored lambda copies, one inside the PORT SOURCE. **Neither target producer has one.** | The port carries an unnamed shared dependency. A TO that says "port the catch-up" ships a function whose calendar import does not resolve. |
| `bd-49f-etf-ownership-daily` has a **`-canonical` sibling** (4 producer dirs, not 3). | Which one writes the served slices is unresolved. A TO naming the wrong twin is a WRONG-OBJECT error, and comp-read cannot catch it (rule 21 limb ii). |
| Brief **s.10** (the 8-step sequencing block -- what a COO actually decomposes from) **predates the FWD-7 ruling and has no SES row.** | CTO flagged s.7 as stale; s.10 has the same defect unnamed. Decomposing off s.10 alone drops an outcome silently. |
| The row's `directive` moved **D4 -> D8** and gained `fabric: laptop` at 14:10Z, mid-decomp. `DIRECTIVES.yaml` D8 members **still does not list it**. | A D8 driver resolving members from that file cannot see this project. Split carrier, live now. |

**And the structural one:** `FWD-1..FWD-8` and brief s.10's 8 sequencing steps are **two different
lists of eight, and nothing maps them.** I built outcome -> surface -> lane by hand. That mapping is
the deliverable of step 4, not an inference at step 5.

---

## 2. The contract

One section, appended to the PRD by `1.0.0_SA_CTO` at step 4. One row per surface the project OWNS.

### 2.1 Row schema

| field | contents | why it is load-bearing |
|---|---|---|
| `outcome_ref` | `FWD-n`, or `NONE -- <reason>` | step 10's scope-change fork is decided by *"does the PRD name this outcome?"*. A surface with no outcome is either out of scope or a missing FWD. |
| `surface` | `path:lines` \| ARN \| function name \| `NEW -- <proposed home>` | **the comp-tool's argument.** This is the field whose absence makes step 5 non-mechanical. |
| `claim` | `measured` \| `inferred` \| `held` \| `absent` \| `unmeasured` | CLAUDE.md: a value must carry its claim in a field a consumer can reject on. `unmeasured` is the BORN state (atom-decomp), never a failure. |
| `evidence` | **`claim: measured` REQUIRES `file:line @ commit-ish`** or an equivalently dated pin. Tool + denominator stays legal at every LOWER rank (`inferred`, `held`, `absent`, `unmeasured`). | ⛔ **AMENDED 2026-09-02 per `3.0.0_SA_CVO` 92527, and the defect was in THIS FIELD, not in any row.** The original form read *"`file:line @ commit-ish`, OR tool + denominator"* at every rank -- so the field itself admitted a vintage-less form, the instance COMPLIED rather than deviated, and rows would have kept arriving undated for as long as the definition permitted it. A `measured` row asserts something RE-DERIVABLE; an undated tool denominator is not re-derivable at a point in time. **EVIDENCE FORM MUST RISE WITH CLAIM RANK** -- same direction as the `BASIS_RANK` correction `1.0.0_SA_CTO` landed. |
| `lane` | `0.7.0_AE_CloudOps` \| `0.4.0_DS_ClientPlatform` \| `3.0.0_SA_CVO` | seats the row at step 6 without COO re-deriving it. |
| `verb` | `port` \| `classify` \| `wire` \| `align` \| `retire` \| `verify` | one act. Two verbs in a cell is a decomp that has not finished. |
| `depends_on` | other rows' ids, **not prose** | the ordering rulings become edges. Prose orderings get read past; edges do not. |
| `acceptance` | the PRD s.4 property number | binds the TO to an EXERCISED test, not an assertion. |
| `bound` | any constraint that must travel WITH the row | a footnote is not a bound. The 10-day constant, the ZERO-vs-MISSING contract, the SES carve-out width. |

### 2.2 The four-postulate record (CLAUDE.md Rule 24 -- this is a schema I am authoring, so it binds)

- **(i) MECE over a DECLARED domain.** Domain = *every surface named in the PRD's Territory OWNS
  cell*. The check is bidirectional and mechanical: **every OWNS item has >=1 row, and every row maps
  to an OWNS item.** An OWNS item with no row is the uncovered member -- that is the hunt.
  RELIES-ON items appear ONLY as `depends_on`, never as work rows; TOUCHES-BUT-MUST-NOT-CHANGE items
  appear ONLY as `bound`.
- **(ii) SAME GRAIN.** One row = one surface one lane can change in one act. Not a component, not a
  phase. If a row needs two lanes it is two rows with an edge between them.
- **(iii) INTENT COHERENCE.** The manifest answers *"what must change, and where"* -- one axis. It is
  NOT a schedule, NOT a status tracker, and must not grow a `done` column. Status lives in the TO.
- **(iv) STATE COHERENCE.** `claim` moves under a MEASUREMENT. `unmeasured -> measured` is the only
  transition step 5 performs. **No remedy moves `absent`** -- an absent surface is a design question
  for step 4, and routing it as work is the error this field exists to prevent.

### 2.3 What makes a row REFUSABLE at step 6

Stated so the contract has teeth without an agent-made gate: a row is not TO-ready while
`surface` is `NEW` with no proposed home, or `claim` is `unmeasured` on a row whose `verb` is not
`verify`. **Not implemented as a gate.** Andrew has not asked for one, and building one on this
seat's judgment would be exactly the agent-made gate the law forbids.

---

## 3. INSTANCE -- ETFS_GUARDRAIL, filled from this session's measurements

Denominators are this seat's own runs unless the row says otherwise. **`claim` is about the SURFACE
ADDRESS, not about the work being done.**

| id | outcome_ref | surface | claim | evidence | lane | verb | depends_on | acceptance | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-1 | `infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py` | measured | comp-read --enumerate **0 hits / 177 lines** @`dbff7603bf` (2026-08-01) | AE_CloudOps | port | S3, S10 | A1, A2 | window is REPORTING-OBLIGATION, never a day count. **Do not port `CATCHUP_WINDOW_DAYS = 10`** |
| S2 | FWD-1 | `infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py` | measured | comp-read --enumerate **0 hits / 122 lines** @`08d0a9bff6` (2026-07-28) | AE_CloudOps | port | S3, S10, S11 | A1, A2 | 49F lag tail **12-13 d** exceeds the shipped 10-d constant. A straight port passes review and fails A2 |
| S3 | FWD-1 | `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:271-314` | measured | `lambda_function.py:271,274,314` @`001a73530a` (2026-08-03); **4 hits / 317 lines** | AE_CloudOps | verify | -- | A1 | PORT SOURCE. Relied on, **not owned** -- do not modify to suit the port |
| S4 | FWD-4 | classifier A/B/C/D -- **NEW, home unproposed** | unmeasured | -- | DS_ClientPlatform | classify | S10 | A4 | **Class B is the trap.** Discriminator = read upstream partition + count priced. Must not "fix" the ZERO-vs-MISSING contract |
| S5 | FWD-3 | `data/etfs/scripts/presentation/render_month_end.py` | measured | `render_month_end.py` @`9ea991b080` (2026-09-01); comp-find 3 hits / 148,724 files | DS_ClientPlatform | wire | S4 | A6 | coverage line prints **regardless of verdict** |
| S6 | FWD-2 | pre-publish gate -- precondition INSIDE S5 or the orchestrator immediately before it | unmeasured | -- | AE_CloudOps | wire | S1, S2, S4 | A3, A5 | **NOT a standing service.** Catch-up before gate: a gate shipped first only blocks |
| S7 | FWD-8 | remediation ladder rungs 1-2 unattended, rung 3 STOPS-AND-ASKS | unmeasured | -- | AE_CloudOps | wire | S4, S12 | A9 | **No rung may fabricate.** Rung 3 = per-use egress, no standing grant |
| S8 | FWD-7 | terminal SES send -- **NEW**, on the ladder's terminal-failure path | unmeasured | -- | AE_CloudOps | wire | S7 | A8 | **ONE send, terminal path only.** Not a monitor, no schedule, no polling. Fires only when EVERY rung failed |
| S9 | FWD-5 | `etfs-reports-orchestrator` env `EMAIL_RECIPIENT` | **inferred** | brief s.6 -- **NOT re-measured by me.** comp-trigger BLIND on this function (see preflight) | AE_CloudOps | wire | S13 | A7 | **JOIN, not replace:** `"aj@opalinvest.com,andrew@opalinvest.com"`. Verify as DELIVERY -- a comma-joined string can be accepted-and-mis-delivered, silently |
| S10 | -- | `lib/trading_calendar.py` **+ 3 vendored copies**; neither target producer has one | measured | `lib/trading_calendar.py` @`0cbb0ad174` (2026-06-26); 5 hits: `lib/` + `bd-served-vintage-alarm/` + `inf-etf-ownership-daily/` + `opal-assets-absence-check/` + `lib/tests/` | AE_CloudOps | verify | -- | A4 | **RELIES-ON, shared beneath S1/S2/S4.** Rule 22: check what the members have in COMMON. Which calendar each producer resolves is UNANSWERED |
| S11 | -- | `bd-49f-etf-ownership-daily` **vs `-canonical` twin** -- which writes the served slices | **absent** | 4 producer dirs measured; discriminator not run | AE_CloudOps | verify | -- | -- | WRONG-OBJECT risk under S2. comp-read cannot detect a wrong file (rule 21 limb ii) |
| S12 | -- | Inflection lineage: repo computes `opal-data-assets/orion/...`, slices cite `opal-data-inf/gold/canonical/holdings_`, deploy POSTDATES last repo change | **absent** | brief s.9.2, **attributed, not re-measured** | AE_CloudOps | verify | -- | -- | Needs a **deployed-bytes diff vs build input**, NOT a source read. Binds ladder rung 2 |
| S13 | FWD-6 | Orion date-basis alignment; `orion_normalize_as_of` | held | brief s.6a: **0 calls / 19 files** -- brief's denominator, not mine | DS_ClientPlatform | align | -- | -- | **PREREQUISITE TO THE SEND ONLY.** Guardrail lands first. Forward-only: restate nothing, notify no partner |

**MECE check against the PRD OWNS cell (postulate i), run rather than asserted:**

```
  OWNS item                        rows        verdict
  catch-up in cot- + bd-49f-       S1, S2      covered
  coverage classifier              S4          covered
  pre-publish gate                 S6          covered
  coverage line in the report      S5          covered
  remediation ladder               S7          covered
  terminal SES notification        S8          covered
  EMAIL_RECIPIENT                  S9          covered
  DENOMINATOR: 7 of 7 OWNS items carry >=1 row. 0 uncovered members.
  Reverse direction: S10-S13 map to RELIES-ON / unresolved-dependency, NOT to OWNS -- correctly
  carried as verify rows and edges, never as work.
```

**Out-of-scope, carried so it is not lost and explicitly NOT a row:** retiring `etfs-canon-fanin`
(ENABLED on `cron(45 15)` against a DynamoDB table that does not exist, so it fires daily and cannot
succeed). Independent finding, owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`. **PRD s.5 excludes it
and this manifest keeps that exclusion.**

---

## 4. What this instance shows about the CONTRACT

- **9 of 13 rows resolved to an address from the two documents plus my own scans; 4 did not.**
  S4 and S6-S8 are `NEW` with no proposed home -- **half the OWNS surfaces have nowhere to land
  yet.** That is a step-4 design question, and it is visible here in one column instead of surfacing
  as a stuck TO at step 7.
- **S11 and S12 are `absent`, and postulate (iv) says no remedy moves `absent`.** Both are routed as
  `verify` rows *before* the work they sit under, rather than being discovered by the lane mid-build.
- **S9 is `inferred`, and it is the one I would most want CTO to convert to `measured`** -- it is the
  only row where the failure mode is silent (Andrew stops receiving his own report, which looks
  exactly like the render not running), and it is the row my own battery went blind on.

---

## 5. `<preflight>` -- PARTIAL, and reported as partial

Step 5's battery was interrupted by an Andrew redirect at ~14:1xZ. **Not complete, and not to be
read as complete.**

```
<preflight>
comp-trigger: RUN -- 140 events-rules + 18 schedules scanned, us-east-1; 3 of 3 producers ENABLED,
  FIRED 7x, last datapoint 2026-09-01. BLIND on etfs-reports-orchestrator -- NO MATCH by name or
  target-ARN; v1 scans EventBridge rules + Scheduler only, so an S3-notification/sentinel trigger
  would not appear. The SEND PATH (S9) is UNRESOLVED by this lens.
comp-read --enumerate: RUN -- catchup symbols: inf 4 hits/317 lines; cot 0/177; bd-49f 0/122.
  Absence MEASURED with its denominator, not inferred from silence.
comp-schedule: RUN -- 5 carriers, denominators 21/2/12/20/336; C5 PROJECT-BLOCKING NOT-DECIDABLE.
  NOTE: this is the GATE LEDGER, not an AWS schedule census -- comp-trigger is the scheduler lens.
comp-blast: NOT RUN
comp-dataflow: NOT RUN
comp-iam: NOT RUN -- and when run, SILENCE FROM IT IS NOT "ALLOWED". This project touches three
  partner firms' buckets, so NEVER#1's unparsed cross-firm Deny belts are live here, not theoretical.
comp-pipescript: NOT RUN
comp-denytest: NOT RUN
comp-adversary: NOT RUN -- must record its CITED-PATH DENOMINATOR; a 0-over-0 is an unrun check.
comp-similar: REFUSED per spec s.2.2 -- no vintage, no denominator on either carrier.
</preflight>
```

---

## 6. Status of this document

**PROPOSAL.** It refuses nothing and gates nothing. Adopting it as the step-4 standard is
`1.0.0_SA_CTO`'s call (the PRD is that seat's artifact) with `3.0.0_SA_CVO` holding the schema
question under Rule 24. **No TO has been cut against ETFS_GUARDRAIL and none will be at this seat
without a step-6 word** -- the GO at 92484 was explicitly step 5 only.
