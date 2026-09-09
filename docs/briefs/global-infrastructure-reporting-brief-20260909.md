# BRIEF — Global Infrastructure Reporting and Analysis

**Step 1 of the canonical loop (L1).** Author `4.0.0_SA_CRO~Z`. Mode: **NEW** (greenfield — the
calibrated report does not exist).
**Commissioning:** Andrew-direct at the `4.0.0_SA_CRO~Z` terminal, 2026-09-09, opening the review:
*"which of course is alarming, although I suspect merely a miscalibration... ultimately this should
become a /brief-create subject of having a proper infrastructure report, culminating in a daily
morning review. It has been miscalibrated for a long time and it's time that we fixed that."*

**Consumer:** `/endpoint --forward` at L2, run by `1.0.0_SA_CTO~Z`. Every outcome below is numbered
and separately headed so it can carry a `SOURCE:` citation.

⛔ **THIS BRIEF RELEASES ANOTHER PROJECT.** Andrew has held `2.0.0_SA_COO~Z` seating — and therefore
all `NFRA_OPSEC202609` execution — until this brief reaches `1.0.0_SA_CTO~Z` and clears L2
(Andrew-direct 2026-09-09, quoted on OPSEC PRD v0.14). A delay here is a delay there.

---

# PART I — THE OUTCOME TERRITORY

*Each outcome is one thing a named person can DO. Cut from here.*

## O1 — Andrew opens one morning review and knows whether anything needs him today

He reads a single artifact, on trading days, before his morning, and comes away with a decision:
act, or don't. He does not need to open a second thing to find out.

**Why it is not possible today:** the subject line has read `[Opal][RED]` on every instance in the
search window (Part IV, F1). A signal that never changes value cannot answer this question.

## O2 — Any reader can tell "nobody looked" apart from "we looked, and it is broken"

For every row, a reader distinguishes an **instrument** state from a **world** state without knowing
how the report is built. "We are blind here" and "this is breached" stop sharing a colour.

**This is the naming law Andrew ratified** (Part IV, F6). It is the outcome the word *"breach"*
in the current subject line makes impossible.

## O3 — A reader sees what CHANGED since the last edition, on every row

Not just totals — per row, per property. A standing condition and a new one look different at a
glance, and a number that has not moved says so.

## O4 — A reader can tell which property a problem belongs to, and who owns it

Every finding rolls up to **Dashboard**, **Website** or **Gateway** (Andrew-direct, 2026-09-09), and
carries an owner. One underlying failure appears once, not once per instrument that noticed it.

## O5 — A person can tell whether an alert would reach a human, before an incident tests it

For any alarm, a reader can see whether its delivery path terminates at a person. A control that
cannot fire is visible as such rather than counted as protection.

**Grain that decides this outcome:** the check is **alarm-anchored** and reads **CONFIRMED**
delivery, never *subscribed* and never the alarm's own configuration (Part IV, F4).

## O6 — A person can tell a broken artifact from a deliberately retired one, without guessing

For any stale artifact, a reader learns whether anything still consumes it. Age informs the
question; it never answers it.

**Criterion (Andrew-ratified, with its grain):** deprecated = **zero consumers at the client-facing
terminus**, established by walking the chain to a served artifact and a rendered component — never
by reading the first `scripts:` field, and never by age.

## O7 — Someone can retire a dead artifact or generator and have the report stop mentioning it — on the record

Decommissioning is part of this work, not a separate errand (Andrew-direct: *"decommissioning/cleaning
artifacts/generators should be a function of this work"*). A retired thing is recorded as retired,
with a reason and an owner, and stops being re-reasoned every day.

## O8 — A person can see a cost movement that matters and ignore one that does not

A material divergence from a segment's or a box's own recent history surfaces; ordinary variation
does not. **Andrew's detector, verbatim:** *"whether there is a material divergence from historical
cost for a given compute box or cost segment... if something moves say 15% or more from its trailing
30 day price."*

## O9 — Anyone can answer "what compute do we run, and what shuts itself down" from one place

One record covers **EC2 and ECS**, states each unit's duty cycle and whether it stops itself, and
distinguishes *not declared* from *declared as none*. The always-on set is expressed by group —
**Dashboard, Website, Graph** — and everything outside it defaults to autoshutdown-required.

## O10 — A reader can trust that a number covers what it claims to cover

Every count carries its denominator and its coverage. A pipeline monitored thinly and a pipeline
monitored thoroughly do not produce comparable-looking scores.

---

# PART II — WHERE THE BOUNDARY SITS

## Owns

- The **report artifact** — its state model, its structure, its schedule, its delivery.
- The **compute manifest** as a reporting substrate (EC2 + ECS), including the schema fix and the
  backfill.
- **Reconciliation between what is monitored and what is actually served** — the standing check that
  no existing instrument performs.
- **Suppression / deprecation as recorded state**, with owner and reason.

## Relies on, does not own

| Surface | Owner |
|---|---|
| Detection of suspicious activity; the sentinel, address table, evidence store, WAF/IP sets | **`NFRA_OPSEC202609`** |
| Portal MFA enforcement (`mfaChannel` / `mfaEnabled` on `opal-users-v2`) | **`D12_PLATFORM_OPS`** |
| The gold/silver producers whose artifacts are reported on | the DS/AE pipeline lanes |
| Terraform module correctness | the owning infra lanes |
| The marketing site's DNS at GoDaddy | outside AWS entirely |

## Explicitly NOT re-opened

- The **standing moratorium on building new alerts/alarms/monitors.** This project **repairs**
  existing egress and **reports**; it does not mint alerting.
- **`NFRA_OPSEC202609`'s** endpoint. Its 19 outcomes are consumed here, not amended here.
- Retirement of served output still needs never-widen sign-off (CTO+COO). This project **classifies**;
  it does not delete on its own authority.

---

# PART III — THE QUALITATIVE BAR

*Disputable, and deliberately without invented numbers.*

1. **Andrew reads it every morning and does not learn to skip it.** The current report earned the
   opposite habit; the bar is that a reader who acts on it is rewarded rather than fatigued.
2. **A row that says OK has been looked at.** Nothing is green by virtue of not having been examined
   — this is the ratified definition of GREEN, and it is the single most contestable claim here.
3. **One failure reads as one item.** A reader encountering a broken thing sees it once, attributed
   to a property and an owner, not scattered across the instruments that happened to notice.
4. **A number in the report can be trusted at the grain it is stated.** Where it cannot, the report
   says so in its own words rather than by omission.
5. **The report tells you what it cannot see.** Its blind spots are content, not gaps — a reader can
   enumerate what is unmonitored without leaving the artifact.
6. **A control that cannot fire is not counted as protection.** This is the difference between the
   estate being defended and the estate believing it is defended.

---

# PART IV — THE SUBSTRATE: findings, with what was measured

*All measured 2026-09-09 unless stated. Instrument named per finding.*

## F1 — The rollup is a `max()` over eight rows and has carried no information

**Measured:** every Infrastructure Report in the mailbox search window is `[Opal][RED]` —
2026-08-25 through 2026-09-09, **12 of 12**. Graph returned an `@odata.nextLink`, so **12 is a
floor, not the total**. Instrument: `search_email` over `Andrew@opalinvest.com`.
Today's composition: **1 RED, 4 ACT, 2 WATCH, 1 OK** — one row sets the banner.

## F2 — The detectors are weekday-aware and not trading-day-aware, and the report proves it on itself

**Measured:** the report does not send on 2026-08-29/30 or 09-05/06 (weekends) but **did** send on
**2026-09-07, Labor Day**. Its thresholds are flat wall-clock hours.
**Consequence, computed:** the four `inf_gold_*` artifacts that fired RED last landed
**2026-09-05 12:45–12:51, a Saturday**; ~72 of those 96 hours contain no trading day. The four
landed within a **6-minute window** — one runner stopping, rendered as four findings.
The frontier logic already exists (`lib/trading_calendar.py`; `.tools/comp-freshness` implements
`freshness_basis: trading-day-frontier`). The INF config declares `cadence: daily` for the
overwhelming majority of entries, which routes them to a wall-clock basis by the manifest
generator's own locked contract (`.tools/freshness_manifest_gen.py:34`).

## F3 — Coverage, not staleness, is the freshness story

**Measured:** 51 of 77 monitored artifacts fresh. Per pipeline: bd 23/32, inf 19/31, cot 5/8,
**mdpf 0/1**, model-portfolios 2/3, news 1/1, nna 1/1.
**Root cause, cited:** `freshness_manifest_gen.py:36` — *"INCREMENT-1a: bd/inf COVERED; the 5 gaps
(cot/mdpf/model-portfolios/news/nna) emitted GAP-no-config. INCREMENT-1b: author the 5 gap freshness
configs."* **Increment-1b landed for cot only** — `comp-find --name 'gold_freshness_config.yaml'`
returns exactly **3** (bd, cot, inf). The rest sit in the generic `data/served_freshness_config.yaml`.
`mdpf 0/1` therefore means *one artifact is monitored*, not *MDPF is broken*.
**The manifest itself is 2014.2h old (2026-06-17)** — the same date its contract was locked.

## F4 — Alert egress: controls that cannot reach anyone

**Measured (report, topic-anchored):** 16 topics checked; **8 with 0 confirmed subscribers**; **3
with a single SMS subscriber against an SNS SMS sandbox of unknown status → non-delivering**; 2
WATCH. The three SMS rows are **one account-level root cause**.
**Measured (`1.0.0_SA_CTO~Z`, alarm-anchored, msg 20519):** **51 alarms → 7 distinct SNS targets, 3
with zero confirmed subscribers**, with **4 positive controls** returning subscribers through the
identical call.
**The alarm-anchored join is the correct instrument** — a topic nobody points at is harmless; an
alarm pointing at a dead topic is the failure.
**`opal-infrastructure-alerts` is itself among the non-delivering.** The daily email became the
estate's alert channel because the alert channels do not deliver.

## F5 — The drift section colours on instrument freshness, not on findings, and inverts both rows

**Measured, verbatim from the report:**
`[RED] comp: drift_state 95.5h old` / `OK: no comp drift (1 tools ran clean)` — RED, finding clean.
`[OK] terraform: ... source_zip 89.2h (RED) | coverage 40/55 assessable (73%) (RED) | 15 ERROR gap(s)`
— OK, carrying two REDs and fifteen errors.
**Of the 15 unassessable modules, 9 share one error class** (`Archive creation error`) and **3 of
those fail on the identical line** `../modules/served-guard/main.tf:41` — one line, three rows. Those
three are the served-guards for 49f/cot/inf.
**4 modules are `deny-blocked-by-design [recorded]`** — the one place in the report where *cannot
assess because broken* and *cannot assess by design* are separated.

## F6 — The vocabulary this project needs already exists in two subsections

**Measured, verbatim from Contract Integrity:** `CHECKED (3)` · `BLIND: 2 SEV1 surfaces UNCONTRACTED`
· `COARSE: 2 contracts grain=bucket ADVISORY` · `INERT: 5 never-widen tripwires name 0 live IAM role
(cannot fire)` · `UNCHECKED: period_defs value-check not_wired`. It also prints its own artifact
vintage (10.9h).
Plus `DENY-BY-DESIGN` from F5.
**Andrew ratified these as the report's naming law**, on two axes — instrument
(`CHECKED/BLIND/INERT/COARSE/UNCHECKED/DENY-BY-DESIGN`) and world (`OK/DEGRADED/BREACH`, meaningful
only where instrument = CHECKED). **Blind and Breach were never on the same scale.**
⛔ Contract Integrity currently renders `[WATCH]` — **the section that most honestly declares its own
blindness receives the softest colour in the report.**

## F7 — Monitors outlive migrations, and nothing detects that

**Measured:** the report renders `SMARTX ... json/portfolios/*.json: 1144.1h old ... Overall: STALE`.
`DATA_CATALOG.yaml:650` already declares that exact path *"legacy, last written 2026-07-23"* — the
same date the age resolves to. `graph_contracts.yaml:278` names the live path as
`json/mdpf/{firm}/account-distribution.json`; `graph_contracts.yaml:201` records the writer DORMANT
since 2026-06-01; `MDPF_GLOBAL_T5A/kill-list.yaml:36,38` marks the tree `RETIRE-WHOLE-CANDIDATE`.
**Andrew ruled the consumer question closed:** *"Neither /attribution nor /factor-tilts should have
any reliance on /json/portfolios/."*
**One defect, two directions:** the monitor is **loud about a retired path** and **blind to
`json/mdpf/{firm}/*`**, which is what actually serves Portfolio Analytics. The blind direction is
the dangerous one. The config already supports a `[deprecated]` annotation with a reason — used
correctly for `inf_gold_fee_rate_history` and `yang_volatility_data`, never applied to the migrated
paths.

## F8 — The compute manifest cannot answer what runs or what stops itself

**Measured** on `infra/aws/ec2/EC2_MANIFEST.json` (`_last_updated: 2026-09-04T12:52:42Z`):
**27 declared services**; **1** declares both `duty_cycle` and `autoshutdown`
(`consolidation-gold-runner`); **18 of 27 carry a lifecycle word** (`persistent`/`transient`/
`ephemeral`) **in the `instance_type` field**, so no machine type is available for two-thirds of the
fleet; **2 services share one instance id** (`bd-allocations` / `bd-price-runner`); **2 have none**.
**ABSENT is not NONE** — the 2026-04-02 audit shows real shutdown mechanisms living in user-data
scripts, SSM documents, Lambda triggers and systemd timers, none of them declared.
**And the manifest is EC2-only.** The Graph property runs on **ECS**: `aws_ecs_service` `nessie`
(`globgrph/nessie.tf:196`), `trino` (`trino.tf:308`), `globgrph_serving` (`serving.tf:173`). **An
entire property's compute has no fleet record**, which is also why `Amazon Elastic Container Service:
$31.36` has nothing to attribute against.

## F9 — Cost has no standard, so it cannot fail

**Measured:** account total MTD **$340.02**; the seven per-pipeline lines sum to **$344.97** — the
parts exceed the whole by **$4.95 (1.5%)**, and it holds on the daily figures ($38.32/day vs
$37.78/day). **No reconciliation line is printed**, so a reader cannot tell whether that is tax
allocation, credits, or double-counting.
**`(untagged)` is $154.21 — 45% of spend and the largest line in a per-pipeline view.**
`inf` moved **+41.2%** ($11.42 → $16.13/day) and the section renders `OVERALL: OK`. There is no
threshold anywhere in it.
**Two instruments agree on one failure:** `schwab_rld/uln/ult` are 47 days stale (S3 object age)
while `canonical-schwab-si2`, a t3.large, averages **1.0% CPU over 14 days** (CloudWatch). Different
planes, same conclusion.

## F10 — Security is posture only, and contradicts itself

**Measured:** `CRITICAL 0 | HIGH 120 | MEDIUM 56 | LOW 40`. The structured block prints
`TREND (vs 2026-09-08): +0 +0 +0 +0`; **the AI briefing four lines below states "No prior trend data
available for comparison."** Both cannot be true.
`21 NEW findings` alongside `TOTAL +0` is unreconciled, and the "new" items include conditions
**302 days**, **203 days** and **146 days** old — `NEW` is carrying *newly-detected* and *newly-true*
at once.
**All 216 findings are configuration properties. Not one is an event.** The section cannot detect a
breach in any sense, which is precisely why the word in the subject line was wrong.
The AI briefing's `SUPPRESS/ACCEPT` block is sound judgement with **nowhere to land** — no
suppression state exists, so the same items are re-reasoned daily.

## F11 — A live external admin identity with no second factor

**Measured directly, with a positive control** (`aws iam`, Andrew-authorised 2026-09-09):
`patricia@thewhitelabelcreative.com` is one of **7** IAM users;
`arn:aws:iam::313476888478:user/website/patricia@thewhitelabelcreative.com`, created 2026-07-08;
**`list-mfa-devices` → `[]`**; **`get-login-profile` → exists** (console enabled);
**`PasswordLastUsed` absent → never signed in**. Control: `Andrew_Berman_Console` returns a real U2F
device through the identical call, so the empty list is a true absence.
Tags: `ManagedBy: Terraform`, `Project: NFRA_WEBSITE`, `Org: TWLC-external`,
`Role: website-estate-admin`, `Environment: Production`. One attached policy, `website-estate-admin`
(**contents unread**).
**Recorded here because it is the class, not the instance:** an identity-plane exposure that the
report surfaced correctly and that the sovereign's own prior expected not to exist. It is
Terraform-managed, so its remedy is a Terraform change, not a console act.

---

# PART V — WHAT MUST BE TRUE, NOT SEQUENCED

*Named, not ordered. Sequencing is L5 and is not this brief's to make.*

**D1 — `NFRA_OPSEC202609` supplies every detection surface this report reads for security.**
Staged and unexecuted: `TO-OP-S-20` (partner-egress allow-list), `TO-OP-S-15-19` (reconciler +
unblock), `TO-OP-S-23` (threshold review), `TO-OP-S-12` (gateway request logging + key expiry),
`TO-OP-S-13` (website edge), `TO-OP-S-10`/`-10B` (signing-key rotation).
⛔ **A sequencing constraint that is NOT this brief's:** OPSEC PRD 7.2(b) requires `TO-OP-S-20`
before `TO-OP-S-15-19` — the allow-list is checked before every block and a block can never override
it. Recorded as an existing constraint, not imposed here.
⛔ **A STATE dependency, sharper than an absence:** `TO-OP-S-14-21` is complete and the sentinel runs
**watch-only**. A `BLOCKED` row today is **DESIRED, never APPLIED**. A report rendering that table
without saying so reports intent as fact.

**D2 — The Website property's edge telemetry is UNBUILDABLE, not deferred.**
OPSEC C-19, measured 2026-09-09: `opalinvest.com` and `www` resolve to EC2 Elastic IP
`18.208.18.213`, `server: LiteSpeed`, no CloudFront. AWS WAF cannot attach to a bare EC2; both
candidate edges need the DNS record repointed **at GoDaddy**, and Route53 does not help because
moving the zone changes the nameservers there too. **There is no AWS-only route**, and Andrew has
ruled *"we do whatever we can without having to engage with GoDaddy."*
**Consequence this project must carry:** Website's security row renders **`BLIND` with that reason
attached permanently** — not as a gap awaiting a fix.

**D3 — Compute attribution at box grain requires the manifest schema fix.** Per-box cost anomaly
(O8) cannot be computed while 18 of 27 rows carry a lifecycle word where a machine type belongs, two
services share an id, and ECS is absent entirely. **Segment-grain anomaly is available now.**

**D4 — An estate inspection instrument is down.** `comp-find --corpus aws` returns
`BLOCKED: comp-kuzu rc=2 / unparseable JSON on unit EC2_INSTANCE -- NO MEASUREMENT, not a zero`
(`kuzu_cli.py: unrecognized arguments: --mode`). Declared-versus-live fleet reconciliation cannot be
automated until it is repaired. It needs an owner.

**D5 — Existing tooling that must not be re-bought.** `sync-ec2-manifest.sh` (populates instance ids
from AWS), `lib/trading_calendar.py`, `.tools/comp-freshness` frontier logic,
`.tools/freshness_manifest_gen.py`, and the `/atom-decomp` method — already run and certified on this
exact surface at `workflows/atom_decomposition/runs/portal-page-portfolios/20260811T1640Z/`.

**D6 — Andrew's rulings that bind the design.** Seventeen recorded verbatim at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md`.
The load-bearing ones: the two-axis state model; GREEN = every property CHECKED and OK; deprecation
by consumer at the terminus; the three-property axis; cost anomaly at ≥15% vs trailing 30 days;
trading-days-only delivery; decommissioning as a function of this work; the always-on set named by
group. **Sequencing of the three workstreams is Andrew's ruling, recorded there — not a decomp
made here.**

---

# PART VI — STATUS TODAY — ⛔ NOT OUTCOME-BEARING

*Measured 2026-09-09, mostly 13:03 ET report edition. Ages here move; do not cut outcomes from this.*

- Today's rollup: **OVERALL RED**; 1 RED / 4 ACT / 2 WATCH / 1 OK.
- Automation: 203 Lambdas, 27 errors, 7 functions with errors — **5 of the 7 at 100% failure**.
  `cot-rebalancer-runner`'s failures are a **fail-closed self-gate refusing a 15-vs-14 roster
  mismatch** — a control working, counted as a failure.
- Freshness: 51/77; manifest 2014.2h old.
- Deploy drift: 164 artifacts checked, 6 findings, **all `[standing]` with no first-seen date**;
  1 genuine half-land (`smartx-rest-pull`, 802.8h), 4 `deployed-ahead`, 1 self-declared false
  positive.
- SNS: 13 of 16 topics non-delivering.
- Cost: $340.02 MTD, $37.78/day; 5 right-size candidates at 0.4–1.3% CPU (**~$170/mo, INFERRED from
  public list prices, not read from the bill**).
- Security: 120 HIGH, trend +0, **5 of 120 surfaced in the body**.
- OpenAI: 3 of 6 functions uninstrumented, including `opal-infrastructure-monitor` — **the report
  cannot measure its own AI cost and prints `$0.0000` rather than unknown**.
- `NFRA_OPSEC202609`: PRD v0.14, 19 outcomes, 21 of 28 task orders complete, **7 staged**;
  `2.0.0_SA_COO~Z` **seating HELD pending this brief**.

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **The live AWS fleet was never enumerated.** `comp-find --corpus aws` is BLOCKED (D4). Every
   fleet statement is **DECLARED** (the manifest), never **LIVE**. The declared-vs-live gap is
   asserted to exist and is **not measured**.
2. **`website-estate-admin`'s policy document was not read.** F11 states the exposure, not its blast
   radius.
3. **Andrew's premise in ruling 8 — that no client-facing surface consumes the ten stale artifacts —
   is carried as a HYPOTHESIS TO BE MEASURED, not as an established fact.** This brief measured one
   hop (artifact → `scripts:`) and found declared consumers on all ten; the terminus walk has not
   been run. Both can be true.
4. **The cost reconciliation gap ($4.95) is reported, not diagnosed.** Tax allocation, credits,
   granularity and double-counting are all untested candidates.
5. **The 115 unsurfaced HIGH security findings were not read.** Only the 5 in the report body and
   the S3 pointer were seen.
6. **No claim is made that any alarm ever fired.** F4 measures delivery capability, never delivery
   history.
7. **Two inferences by this author were falsified during the review, both by reading a descriptive
   record as current state** — `moltbot` (torn down 2026-06-29, independently verified 0-residual)
   and the Graph group (asserted empty; three ECS services exist). Both are recorded because they
   are the same defect class this project exists to remove, and because a reader should discount
   this author's absence-claims accordingly.
8. **No number in Part III.** The qualitative bar is deliberately unquantified per the L1 contract;
   quantification belongs to the PRD.

---

# REFS TO CARRY

```
  BRIEF PATH        docs/briefs/global-infrastructure-reporting-brief-20260909.md
  PROJECT           NONE-YET  (registration is L3, 1.0.0_SA_CTO)
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_OPSEC202609 (D12)  -- detection surfaces, and HELD on this brief
                    D12_PLATFORM_OPS        -- portal MFA (mfaChannel/mfaEnabled)
                    NFRA_WEBSITE            -- the marketing site + its IAM path /website/
                    MDPF_SCOPED             -- the migration the freshness config outlived
  PRIOR ART         .tools/freshness_manifest_gen.py      (manifest contract; increment-1b unfinished)
                    .tools/comp-freshness                 (trading-day-frontier, built)
                    lib/trading_calendar.py               (the one frontier)
                    infra/aws/ec2/EC2_MANIFEST.json       (+ sync-ec2-manifest.sh)
                    Contract Integrity + Terraform drift  (the ratified state vocabulary, F6)
                    workflows/atom_decomposition/runs/portal-page-portfolios/20260811T1640Z/
  RULINGS           org/tier1_exec/4.0.0_SA_CRO/deliverables/
                    ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md  (17 rulings, verbatim)
  MEASURED AT       2026-09-09, report edition 13:03 ET; IAM reads 2026-09-09 ~16:2xZ;
                    repo reads at HEAD 5f4d4b894f
```

**Next:** `1.0.0_SA_CTO~Z` runs `/endpoint --forward` on this at L2. `2.0.0_SA_COO~Z` seating and all
`NFRA_OPSEC202609` execution release on that step.
