# ANDREW-DIRECT 2026-09-09 -- rulings on the Infrastructure Report review

> **THE FILENAME UNDERCOUNTS ON PURPOSE.** It was minted at the first batch of five. This file is
> the SINGLE RUNNING CARRIER for every Andrew-direct ruling in this review session and now holds
> **nine**. A second file was rejected deliberately: two durable records of one obligation diverge
> from minute one. Read to the end; the batches are stamped in order.

**Received by:** `4.0.0_SA_CRO~Z` (site-Z terminal, Andrew present)
**Channel:** direct at the `4.0.0_SA_CRO~Z` terminal, in response to this seat's `/open-calls` segment
**Recorded:** 2026-09-09 14:58Z, same turn as receipt, per `org/XXX.md` Andrew-direct law
**Scope note:** this seat does NOT adjudicate scope. Recorded verbatim; surfaced, not interpreted.

---

## THE RULINGS, VERBATIM AND ENTIRE

> 1.) The prioritization should be relayed to CTO~Z, as I've already instructed them that we are
> going to need to create an addendum to the PRD for NFRA_OPSEC202609 to account for the incoming
> work on the Infrastructure Report. 2.) Agreed, CloudFront. 3.) Rec approved, ride the infra
> report. 4.) Ratify on s-23 output. 5.) We've excised the need for this already via not displaying
> an "AGG" view, which is what required aum-metrics. Neither /attribution nor /factor-tilts should
> have any reliance on /json/portfolios/.

---

## WHAT EACH RULING ANSWERS

The five cards were issued by `4.0.0_SA_CRO~Z` at 2026-09-09 14:53Z.

| # | Call | Ruling |
|---|---|---|
| 1 | Relay the OPSEC prioritization now, or hold for the brief? | **RELAY -- to `1.0.0_SA_CTO~Z`**, not the COO. Andrew has already instructed that seat to author a `NFRA_OPSEC202609` PRD addendum for the incoming Infrastructure Report work. |
| 2 | Website edge: CloudFront or Cloudflare? (FWD-13 / `TO-OP-S-13`) | **CloudFront.** Settles the card the OPSEC PRD carried to Andrew; it reverses the 2026-07-13 "NO CloudFront" spec line. |
| 3 | C-6 digest: ride the infra report, or a separate email? | **Ride the infra report.** The `reports/daily/` FILE remains the durable record. No second security email is minted. |
| 4 | C-3 thresholds: set now, or ratify on `TO-OP-S-23`? | **Ratify on S-23 output.** |
| 5 | Does `/attribution` keep sourcing the legacy `json/portfolios/aum-metrics.json`? | **No -- and neither does `/factor-tilts`.** The AGG view that required `aum-metrics` has been excised. Neither page should have ANY reliance on `json/portfolios/`. |

---

## THE CONSEQUENCE OF RULING 5 -- a stale catalog, surfaced not chased

Ruling 5 removes the last consumer this seat had measured on the legacy tree.

**Measured before the ruling** (`4.0.0_SA_CRO~Z`, 2026-09-09, `comp-find --band CONFIG`):

- `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml:650` -- declares
  `json/portfolios/aum-metrics.json (legacy, last written 2026-07-23, vintage field 'period')`
- `DATA_CATALOG.yaml:1015` -- describes that artifact as still supplying
  `AUM totals from the LEGACY json/portfolios/ tree` as tilt CONTEXT on page `/attribution`
- `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census/ARTIFACT_CENSUS_POD2.yaml:24` -- lists it
  `BORROWED cross-vertical (rendered here, owned elsewhere)` against the same page

**Andrew's ruling states that consumption no longer exists.** Therefore `DATA_CATALOG.yaml:650/1015`
and `ARTIFACT_CENSUS_POD2.yaml:24/149/195/231` describe a consumption that has been excised --
**the catalog and the census are STALE against the live front end.**

This is the SAME CLASS as the finding that produced the review: **a descriptive record outliving the
change it describes.** The freshness config outlived the MDPF_SCOPED migration; the data catalog
outlived the AGG-view excision. Neither has a mechanism that detects its own staleness.

**Disposition: SURFACED, NOT CHASED.** No remediation is authorized by this record. The correction
belongs to the owners of those two files. Routed as an item, not as a gate.

---

## STATE OF `json/portfolios/` AFTER RULING 5

| Fact | Source | Class |
|---|---|---|
| `account-distribution.json` superseded by `json/mdpf/{firm}/account-distribution.json` | `graph_contracts.yaml:278` | measured |
| `aum-metrics.json` had one live reader (`/attribution`) | `DATA_CATALOG.yaml:1015` | **superseded by ruling 5** |
| EC2 `smartx-exporter` dual-writer DORMANT since 2026-06-01 | `graph_contracts.yaml:201` | measured |
| Tree marked `RETIRE-WHOLE-CANDIDATE` | `MDPF_GLOBAL_T5A/kill-list.yaml:36,38` | measured |
| Last write 2026-07-23 | `DATA_CATALOG.yaml:650`; agrees with the report's 1144.1h | measured |

**Consequence for the Infrastructure Report:** the SmartX `RED` is a **false alarm on a fully
retired tree with zero live consumers**, and the monitor is simultaneously **BLIND to
`json/mdpf/{firm}/*`**, which is what actually serves Portfolio Analytics. One defect, two
directions; the blind direction is the dangerous one.

**Retirement itself remains gated** -- moving served output requires never-widen sign-off
(`CTO`+`COO`) per CLAUDE.md. Ruling 5 removes the CONSUMER objection; it is not a delete order and
is not recorded as one.

---

## ACTS TAKEN BY `4.0.0_SA_CRO~Z` ON THIS RECORD

1. This record committed (durable half of the Andrew-direct law).
2. Ruling 1 executed: OPSEC dependency set + prioritization relayed to `1.0.0_SA_CTO~Z` as the
   RAVC 4 answer to its msg 20508 ASK, carrying ruling 2 (CloudFront) so the addendum can name the
   Website edge without a second round trip.
3. Broadcast half: this record notified to `2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR~Z`.

**Not done, and deliberately:** no task order is cut, no sequencing order is issued to any executing
seat, and no retirement is initiated. `4.0.0_SA_CRO` does not dispatch.

---
---

# BATCH 2 -- 2026-09-09 ~15:0xZ (rulings 6 and 7)

Answering the two cards `4.0.0_SA_CRO~Z` put up at 15:0xZ, after this seat's additional review of
the ten months-stale artifacts.

## VERBATIM AND ENTIRE

> 1.) All of these look deprecated, that is worth additional review. If any artifact is over 1 week
> old it is almost certainly deprecated. 2.) Correct, rec approved.

**Ruling 6** = the ten stale artifacts look deprecated; additional review directed; the age
heuristic offered. **Ruling 7** = the morning review lands on trading days only, before Andrew's
morning (this seat's rec approved).

# BATCH 3 -- 2026-09-09 ~15:1xZ (rulings 8 and 9)

Answering the two cards issued after the additional review came back and FALSIFIED ruling 6's
hypothesis on the evidence available to this seat.

## VERBATIM AND ENTIRE

> 1.) I dont believe any client-facing surfaces are consuming these artifacts. Accordingly this
> information should simply be rolled up into the brief, as decommissioning/cleaning
> artifacts/generators should be a function of this work. 2.) Agreed.

**Ruling 8** -- the ten-artifact finding is NOT routed separately; it rolls into the brief, and
**DECOMMISSIONING / CLEANING ARTIFACTS AND GENERATORS BECOMES A FUNCTION OF THE BRIEF'S WORK.**
That is a SCOPE ADDITION to the brief, sourced to Andrew's sentence, not to this seat.

**Ruling 9** -- the deprecation criterion is **ZERO DECLARED CONSUMERS, NOT AGE**, evidenced by an
empty consumer set plus an explicit `deprecated:` marker carrying a reason and a date. The age
heuristic of ruling 6 is superseded by Andrew's own word here.

---

## THE ONE REFINEMENT RULING 9 STILL NEEDS -- A GRAIN, surfaced not adjudicated

Ruling 8's premise and this seat's measurement are **NOT in contradiction; they were taken at
DIFFERENT GRAINS**, and saying so is the point:

- **This seat measured ONE HOP:** artifact -> the `scripts:` field in the freshness config. At that
  grain all ten have declared consumers (`B_01`, `B_02`, `A_03`, `INF_D_00`, `INF_D_04`,
  `INF_D_07`, `INF_D_03`, `INF_D_02b`, `INF_C_01`, `INF_D_00c`). MEASURED.
- **Andrew's claim is about the TERMINUS:** whether any *client-facing surface* consumes them --
  hop N, after those scripts' own outputs are followed to a served artifact and a rendered
  component. **This seat has NOT measured that.** HELD, not measured, and not contradicted.

Both can be true: an artifact can feed a script whose output reaches nothing a client sees.

**THEREFORE ruling 9's criterion is under-specified by exactly one word, and will return OPPOSITE
answers depending on where a reader stops walking the chain.** "Zero declared consumers" at hop 1
says none of the ten is deprecated; at the terminus it may say all ten are. A criterion that
inverts on grain is not yet a criterion (CLAUDE.md rule 24 (ii), SAME GRAIN).

**Recommended completion, for the brief to carry:** *deprecated = zero consumers at the
CLIENT-FACING TERMINUS, established by walking the chain to a served artifact and a rendered
component, not by reading the first `scripts:` field.* That is precisely the instrument Andrew
already required for the brief (`/atom-decomp` denominator coverage on every presented metric), so
it adds no new machinery -- it names which end of the chain the criterion is evaluated at.

**Consequence for ruling 8, stated so the brief does not inherit an assumption as a fact:** Andrew's
"I dont believe any client-facing surfaces are consuming these artifacts" is a TESTABLE claim and
the brief's own instrument tests it. It is carried into the brief as a HYPOTHESIS TO BE MEASURED,
never as an established premise. If it holds, the ten are decommissioning candidates and ruling 8's
disposition is exactly right. If it does not hold for some subset, that subset is a live outage the
brief will surface with evidence. Either way the brief answers it rather than assuming it.

## ACTS TAKEN ON BATCHES 2 AND 3

1. This record extended (single carrier; no second file minted).
2. No separate routing of the ten-artifact finding -- ruling 8 directs it into the brief, and this
   seat does not override a disposition with its own urgency read.
3. Requirements carried forward into the brief: decommissioning/cleaning as an explicit function
   (ruling 8); the consumer-based deprecation criterion with its grain named (ruling 9 + the
   refinement above); trading-day-only delivery before Andrew's morning (ruling 7).

# BATCH 4 -- 2026-09-09 ~15:3xZ (rulings 10 and 11)

## VERBATIM AND ENTIRE

> Both recs approved

Answering the two cards issued at 15:2xZ on the Deploy Drift / Producer Drift section. The rulings
are Andrew's approval of this seat's recommendations, which are therefore quoted here in full so
the record does not depend on the cards being read alongside it.

**Ruling 10 -- the 15 unassessable Terraform modules.** APPROVED: *"fold them in, but as a NAMED
separate workstream inside the brief. Nine of the fifteen share one error class and three share one
line, so the fix is far smaller than the count suggests; and the report cannot honestly claim drift
coverage while blind to a quarter of the estate. Keeping it inside the brief keeps one owner, per
ruling 8."*

Measured basis: `coverage 40/55 assessable (73%)`; 9 of 15 are `Archive creation error`; 3 of those
9 (`served-guard-49f`, `served-guard-cot`, `served-guard-inf`) fail on the identical line
`../modules/served-guard/main.tf line 41`.

**Ruling 11 -- out-of-band Lambda deploys.** APPROVED: *"enforce, and make the report say so.
'Deployed-ahead' should render as a violation with an owner, not a WATCH. mdpf-gold-lambda is the
argument: it is one of the four AND one of the 100%-failing functions, so nobody can currently
trust a source-line citation against it. If any surface genuinely needs out-of-band deploys, that
is worth naming explicitly rather than leaving as drift."*

Measured basis: 4 modules `[deployed-ahead]` -- `opal-partners-data` (artifact 4245.6h),
`mdpf-accrual-trigger` (695.4h), `mdpf-gold-lambda` (705.8h), `opal-assets-mdpf-portal-publisher`
(276.1h). CLAUDE.md names `aws lambda update-function-code` a NEVER (Terraform only).

**SCOPE NOTE, so no seat over-reads ruling 11.** It approves (a) enforcement as the report's
RENDERING of deployed-ahead, and (b) that a genuine need for out-of-band deploys be named
explicitly. It is NOT a remediation order against any of the four modules, and this seat issues
none. `4.0.0_SA_CRO` does not dispatch.

# BATCH 5 -- 2026-09-09 ~15:5xZ (rulings 12 and 13) -- THE NAMING LAW

## VERBATIM AND ENTIRE

> Both recs approved, move to Costs

**RULING 12 IS THE ONE THAT BINDS THE BRIEF.** It ratifies the TWO-AXIS STATE MODEL as the report's
naming law, settling the question Andrew opened the review with ("we need to define what Blind and
Breach even are"). The answer the estate's own artifacts already contained: **Blind and Breach were
never on the same scale. They are values on two DIFFERENT axes**, which is exactly why one colour
could not hold both.

**AXIS 1 -- THE INSTRUMENT. Did the check happen, and could it?**

| State | Meaning | Promoted from |
|---|---|---|
| `CHECKED` | looked, and the result is trustworthy | Contract Integrity |
| `BLIND` | could not look -- nothing governs or detects this surface | Contract Integrity |
| `INERT` | a control exists but CANNOT FIRE (names no live role; pages no subscriber) | Contract Integrity |
| `COARSE` | looked at the wrong grain -- the answer is advisory only | Contract Integrity |
| `UNCHECKED` | deliberately not asserted | Contract Integrity |
| `DENY-BY-DESIGN` | cannot look, and that is intentional and recorded | Terraform drift |

**AXIS 2 -- THE WORLD. What was found. Only meaningful where Axis 1 = `CHECKED`.**

| State | Meaning |
|---|---|
| `OK` | within standard |
| `DEGRADED` | outside standard, contained |
| `BREACH` | outside standard, NOT contained |

**WHY THIS IS NOT AN INVENTION.** Every Axis-1 value is PROMOTED from a section already running in
this estate -- five from CONTRACT INTEGRITY's own output line, one from the Terraform drift
sub-section's `deny-blocked-by-design [recorded]` tag. Two subsections had already solved the
problem the other six had not. Ruling 12 makes them the standard instead of the exceptions.

**WHAT IT FORBIDS, which is the point:** it becomes structurally impossible to print `BREACH` on a
surface nobody looked at, and impossible to print `OK` on a surface nobody looked at. Worked
examples: `opal-login-abuse-alerts` is `INERT`, never `RED`. `comp` is `CHECKED/OK` carrying a
stale-instrument qualifier, never `RED`. Website security is `BLIND`, never `OK`.

**AND GREEN GETS ITS DEFINITION FOR FREE** -- the definition Andrew asked for in his third message:
**every property `CHECKED` on Axis 1 and `OK` on Axis 2. Nothing is green by virtue of not having
been looked at.**

**Ruling 13** -- repairing the 13 non-delivering SNS topics falls INSIDE the brief, as a SECOND
NAMED WORKSTREAM beside the Terraform one from ruling 10. Basis: 8 topics have 0 confirmed
subscribers; 3 more have a single SMS subscriber against an SNS SMS sandbox of unknown status and
are therefore non-delivering, which is ONE account-level root cause, not three. The report's own
escalation channel `opal-infrastructure-alerts` is among the thirteen.

**Standing-moratorium note:** ruling 13 authorises REPAIR of existing topics, not the creation of
new alerting. The CLAUDE.md moratorium on building alerts/monitors is untouched by it.

# BATCH 6 -- 2026-09-09 ~16:5xZ (rulings 14-17)

## VERBATIM AND ENTIRE

> 1.) Just flip her needsMFA on opal-users-v2 to True. 2.) First of all moltbot should be completely
> terminated at this point, I am suspcting this is a mistake reference. But yes, should be named
> separately id say by group (Dashboard, Website, Graph). 3.) Yes agreed. 4.) Let's hold onto this
> for now, we will come back to the rotation subject because I want a clean and easy mechanism for
> doing it reliably so we don't inadvertently get locked out of any property.

## RULING 14 -- patricia MFA. **INSTRUCTION RECEIVED, NOT EXECUTED. ONE WORD IS OWED BACK.**

Recorded as NOT DONE so no reader infers closure. Two measurements taken before acting, both of
which bear on whether the instructed act reaches the reported exposure:

1. **`needsMFA` is a MEASURED ZERO** -- `comp-find 'needsMFA'` returns 0 hits across **52,598 files
   scanned** (`corpus=all`). Qualifiers preserved: 1 UNREADABLE, 1945 BINARY and 425,106
   ephemeral-floor files were NOT searched, so the zero does not cover them. For a code identifier
   a zero over 52.6k first-party files is strong but is not proof of absence from the running system.
2. **THE FINDING AND THE INSTRUCTED TARGET ARE ON DIFFERENT IDENTITY PLANES.** The report's finding
   is `iam_users / patricia@thewhitelabelcreative.com: Console access with NO MFA` -- the **AWS IAM**
   plane. `opal-users-v2` is the **portal application** table. A portal-table flag does not remove
   AWS console access, and AWS MFA is not enforced by a DynamoDB attribute.

**Two readings, DIFFERENT OWNERS AND DIFFERENT REMEDIES, and the difference is not decidable from
here:** (a) patricia is a PORTAL user whom the security scanner mislabels `iam_users` -- then the
instructed portal fix is right and the scanner carries a labelling defect worth its own row; or
(b) she genuinely holds AWS IAM console access -- then the remedy is IAM (enforce MFA or disable
console) and the portal flag does not touch the exposure.

**A wrong-plane control cannot catch a wrong-plane error** (CLAUDE.md rule 22a / retrieval law), so
this seat does NOT guess, and does not execute either reading. The act is additionally an
identity-plane write outside `4.0.0_SA_CRO`'s lane. Held, surfaced, one word owed.

## RULING 15 -- moltbot. **ANDREW'S SUSPICION IS CORRECT AND THIS SEAT'S SURFACING WAS WRONG.**

Andrew: *"I am suspcting this is a mistake reference."* It is. Measured:

- `org/critical_paths/change_management/20260629T1313Z_moltbot-teardown_deploy_completion.md`
- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-29/SCTY.W2_moltbot_teardown_0residual_VERDICT.md`
  -- **independent CVO verdict, re-run against LIVE AWS acct 313476888478, not off the producer's
  sweep table: `EC2 instances (any state) -> describe-instances Name tag -> []`; IAM role, instance
  profile, SGs, Lambdas, CodeBuild project all `[]` / NoSuchEntity. "0 active residual."**

**moltbot was torn down 2026-06-29 and independently verified gone.** Its absence from the
September manifest is CORRECT, not a gap.

**THE MECHANISM OF THIS SEAT'S ERROR, banked because it is the exact class this whole review is
cataloguing:** `4.0.0_SA_CRO~Z` read the 2026-04-02 auto-shutdown audit -- a DESCRIPTIVE record --
and treated it as CURRENT STATE. comp-find had even banded those files `[DOC] -- prose -- DESCRIBES
the code and may be STALE; confirm against source`, and the warning was not applied. This is the
same defect as the freshness config outliving MDPF_SCOPED and the data catalog outliving the
AGG-view excision: **a record outliving the thing it describes.** It strengthens requirement 31
(declared-vs-live reconciliation as a STANDING check) rather than weakening it -- the review's own
author walked into it.

## RULING 15b -- THE EXCEPTION SET IS NAMED BY GROUP, NOT BY BOX

Andrew: *"should be named separately id say by group (Dashboard, Website, Graph)."* The always-on
exception set is expressed on the SAME three-property axis as the report itself (ruling: the three
Opal properties). **moltbot is NOT in it -- it does not exist.**

Open sub-item carried to Andrew: no graph-ops box appears in the 27-service manifest, and the
security sweep reports **7 unused `opal-globgrph-*` security groups** as bulk-deletion candidates.
The **Graph** group may therefore be EMPTY. Not resolved here.

## RULING 16 -- the EC2 manifest backfill is the THIRD NAMED WORKSTREAM, SEQUENCED FIRST

Agreed as recommended. It is the precondition for box-grain cost anomaly (ruling: >=15% vs trailing
30 days), for the autoshutdown answer, and for any decommissioning under ruling 8.

## RULING 17 -- KEY ROTATION IS DEFERRED, WITH A STATED REQUIREMENT

Andrew: *"we will come back to the rotation subject because I want a clean and easy mechanism for
doing it reliably so we don't inadvertently get locked out of any property."*

**That mechanism is already specified and STAGED inside NFRA_OPSEC202609.** FWD-10: *"The keys that
sign logins can be replaced without signing everyone out, and have been replaced at least once on
purpose."* Its task orders `TO-OP-S-10` (signing-key-rotation) and `TO-OP-S-10B` (two-slot and TTL
for the JWT consumers) are both STAGED, Round 3. **DISTINCTION PRESERVED:** those cover **JWT
signing keys**, NOT the **IAM access keys** the security sweep flagged -- a different key type on a
different plane. What generalises is the DISCIPLINE (two slots, overlap window, no cutover), not
the implementation. Surfaced as a candidate brief requirement; not adjudicated here.
