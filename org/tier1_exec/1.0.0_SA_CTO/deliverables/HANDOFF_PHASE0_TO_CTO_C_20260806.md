# HANDOFF — Phase-0 surface review → `1.0.0_SA_CTO~C`

**From:** `1.0.0_SA_CTO~B` · **Andrew-direct 2026-08-06:** *"I am going to spawn 1.0.0_SA_CTO~C to
take over your work on the Phase-0 surface review, because that needs to get done and the priority
for you should be the api calls."*
**Working paper:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/KIMI_SVP_PHASE0_LIFECYCLE_PROPOSAL_TABLE_20260804.md`

---

## STATE: 12 of 29 ratified. RESUME AT ROW 13 (`insurance`).

Ratified 08-05: advi-bd · advi-cot · advi-inf · canonical-schwab · causality (RETIRED) · ceo-digest ·
cma · correlation · data-refresh.
Ratified 08-06: **etf-reports** (PERMANENT + a standing review) · **factor-tilts** (PERMANENT, in
good standing) · **graph-platform** (PERMANENT).

**ANDREW RATIFIES. YOU PROPOSE.** The table's own rule: `lifecycle_class` is producer-asserted, and
his word is the assertion. Do not mark a row ratified without his verbatim, and record the verbatim.

---

## THE ONE RULE THAT MATTERS MOST HERE

> **GROUND-READ THE ROW BEFORE PUTTING IT IN FRONT OF HIM. EVERY TIME.**

Of the rows examined so far, **rows 1, 4, 5, 6, 7, 8 all changed on contact with live state** — and
the two previously-examined `UNDECLARED` rows were **wrong in OPPOSITE directions** (`causality` was
RETIRED where the row said unknown; `ceo-digest` was PERMANENT-and-firing where the row flagged
DORMANT — it had run four hours earlier).
**`UNDECLARED` in this table has meant "I did not look," wearing the enum's word for honest
uncertainty.** The three remaining ones are the sitting's real work.

## THE THREE REMAINING `UNDECLARED` ROWS — ground-read each BEFORE presenting

| row | vertical | what to check |
|---|---|---|
| **13** | `insurance` | claimed "zero session evidence of activity or consumers." That is the exact phrasing that was wrong twice. Check live: schedules (BOTH APIs, see below), Lambdas, S3 prefixes, portal mount. |
| **25** | `security-scanner` | **LIKELY INVERTED.** Row says LEGACY candidate. But row 9 established its backend is the LIVE `opal-data-refresh-api` Lambda and its page is MOUNTED at `App.tsx:434`. **Rows 9 and 25 are the same Lambda and the same App.tsx.** Resolve them together. |
| **27** | `ticketing` | TicketCenter exists in the portal; TAXSMA ticket-scoping triage has been pending ~3 weeks with a dead seat. TRANSIENT-vs-PERMANENT is explicitly Andrew's call. |

## ROW 10 CARRIES A STANDING REVIEW — it is open, and it is not yours unless you want it

Andrew, on ratifying `etf-reports`: *"we need to make sure that all of these are properly grouped
together, that nothing is redundant, that what is actually supposed to be canonical here is... subject
for review."* Nine live schedules, 1:1 rule→Lambda with zero duplicate targets. **Four questions left
open ON PURPOSE** (they need reading what those Lambdas WRITE, which I did not do): the chain is
time-ordered not dependency-enforced; two 49F jobs on different calendars; two jobs run AFTER the
dashboard publishes; and **a job literally named `etfs-canon-fanin` fires daily while "which location
is canonical" is an open P0.** Full scope is below the table.

## INSTRUMENT TRAPS — all four cost me real errors today. Do not re-pay them.

1. **`aws events list-rules` CANNOT SEE EventBridge SCHEDULER.** Different API. **16 live schedules**
   sit there, including `etfs-reports-monthly-run`, `astn-wsjft-3am-run` and `estate-report-0900et`.
   I had a `ResourceNotFoundException` in hand and was one step from filing a working
   partner-rebate pipeline as MISSING. **Always check `aws scheduler list-schedules` too.**
2. **`--no-paginate` RETURNS PAGE ONE ONLY.** It returned 50 of 196 Lambdas and 100 of 139 rules.
   **It produced a FALSE ABSENCE that I published and had to retract.** Walk the tokens.
3. **`--query 'length(...)'` on a paginated call returns the PAGE count**, not the total.
4. **A NAME IS NOT A COMPUTE TYPE.** I read `sys-yang-analytics-engine` — a C3 *ontology label*,
   `kind: SHARED-ENGINE` — as an EC2, because it says "engine." **The producers are 28 Lambdas.**
   Andrew's recollection beat my measurement. Ground compute type on an ARN or an API response.

**And the class behind two of them:** email-only products (`ceo-digest`) and EC2-less families are
**structurally invisible to artifact-based instruments** — no data artifact, no frontend, no
queryable surface. They do not look neglected, **they look nonexistent**, and the enum's dangerous
direction is proposing DORMANT on a live system.

## GRAIN — ratified, do not re-litigate

The value names the BUSINESS FUNCTION's life-shape at the vertical grain. **Interior churn
(migration / consolidation / refactor) is NOT a lifecycle shift** — Andrew-verbatim: *"It is a
permanent project nevertheless, although underlying conventions and resources may shift around with
migrations/consolidations/refactoring/etc."* That churn belongs on the shift-watch column, which
seeds R2's State layer.

## WHAT I AM KEEPING

The Kimi API-call work — the 23-call walkthrough with Andrew, the F(N) axes, the subdivision. **Do
not touch `estate_report_runner.py`, the estate-report Terraform, or the STATE_FRICTION design doc**;
they are mid-flight at my seat and Andrew's priority for me.
Phase-0 is yours end to end, including presenting rows to him and recording his verbatims.

**Ping me if a row turns out to depend on the Kimi pipeline's state — rows 9/25 touch
`opal-data-refresh-api`, which is also the named specimen in CLAUDE.md Rule 22a.**
