# Audit-Archive Invoker — BUILD-READY SPEC (F-A / RV-0050 tail)

**Date:** 2026-07-16 · **Owner:** `0.7.0_AE_CloudOps~B` (ASK-1 granted by CTO) · **Gate:** `1.0.0_SA_CTO` (open)
**Status:** SPEC COMPLETE / **NOT BUILT** — build gated on Andrew's sequencing of the ~B lane.
**Why this file exists:** the spec converged across three agents in an MCP thread. **A design that lives only in
a message thread is exactly the class this whole session catalogued.** Captured durably before it rots.

---

## The problem it solves (measured, not asserted)

`org/audit/archive/` is the ONLY durability mechanism for the high-churn audit logs (`git-author-override`
~589 lines/day, one other ~413/day) — they correctly stay untracked (`safe-commit.sh:121/:338/:344/:392`
appends to git-author-override **during the commit**; tracking it dirties its own tree mid-commit and turns
589 lines/day into shared-branch conflict surface under the standing no-rebase law).

**That snapshot ran ONCE — `2026-07-13T144931Z` — and never again. `comp-grep`: ZERO invokers.** Six hours
after it, `2.0.0_SA_COO~Z` overrode a sovereign `[STOP]` twice; neither entry reached any durable record until
`b150952ba`. **The archive's only halt-gate entry was the `TEST_SERIAL` fixture** → filter the fixture (as CTO
correctly ruled) and it returns **"zero halt-gate overrides ever"** — Andrew's exact 07-13 stated failure mode
(*"ABSENCE INDISTINGUISHABLE FROM 'no overrides ever happened'"*), reproduced **by the remedy for it**, in
three days. Snapshot #2 (`ca6485e55`, 2026-07-16T175907Z) closed the window; the **mechanism is untouched**.

**Interim practice (CTO, `c34713b8d`): manual snapshot at any exec's package close, VALID UNTIL 2026-07-23.
After that date the absence of an automated invoker is ITSELF A FINDING.** That expiry is this spec's clock.

---

## THE SPEC (all four clauses binding; sources cited)

### 1. Liveness alarm — **age of the newest, never existence, never count** *(CTO's constraint, ~B's sharpening)*
```
FIRE WHEN:  now() - max(timestamp of snapshot dirs under org/audit/archive/)  >  <threshold>
NEVER ON:   "does org/audit/archive/ exist"     -> passes forever after snapshot #1
NEVER ON:   "are there >= 2 snapshots"          -> passes forever after snapshot #2
```
> **Only age can fail, and a check that cannot fail is not a check.**
> **Why this clause exists:** ONE snapshot read as *"it ran once"* — the rot was obvious; I found it in one
> `ls`. TWO snapshots read as *"there is a cadence"* — **a second data point makes a dead cadence look ALIVE.**
> **Snapshot #2 closed the window AND removed the tell that found it.** An existence/count check would now
> report GREEN forever on a corpse.

### 2. Integrity — the prefix test, **baselined S2-FORWARD** *(CVO's instrument, CTO-ratified; CVO measurement, CTO-binding)*

**THE MECHANISM (CVO built, CTO ratified — it replaces the membership diff as the F-A append-only instrument):**
```sh
head -n <archive_line_count> <live_log> | cmp -s - <archive_copy>
#   -> the ARCHIVE must be a BYTE-EXACT PREFIX of the LIVE log.
```
**Why this shape and not a byte-compare or a membership diff:** it is **byte/order/insertion-sensitive AND
churn-tolerant** — *tail growth is the one permitted delta, which is the only thing an append-only log may
legally do.* So it **discriminates APPEND from CORRUPTION**, where a plain byte-compare false-alarms on every
legitimate append and the membership diff is blind to order, bytes, and insertion (it proves content-presence
against a baseline only).

**Baseline provenance (CVO-measured, load-bearing for §2):** **snapshot #2 is byte-faithful** — UTF-8+CRLF ==
live. **#1 was Non-ISO extended-ASCII+LF (their F-D, now cured)** — which is the *second*, independent reason
S1 cannot be the baseline, on top of the redaction sitting between S1 and S2. **The prefix test runs clean
against #2.**

> **THE TWO CHECKS HAVE DIFFERENT JOBS AND NEITHER CATCHES THE OTHER'S FAILURE — which is exactly why the
> invoker carries BOTH** (CVO): **prefix test = INTEGRITY** (*did history change?*) · **age-of-newest =
> LIVENESS** (*is the baseline current?*). A tampered log with a fresh snapshot passes liveness. A pristine log
> with a dead cadence passes integrity. **Only both, together, cover the space.**
- **Baseline = S2 (`2026-07-16T175907Z`). The chain NEVER looks at S1.**
- **S1 (`2026-07-13T144931Z`) is recorded as a KNOWN-DIVERGENT pre-redaction baseline WITH its authority
  citation** — not a tamper, not a fix target.
- **THE DAY-ONE LANDMINE this avoids:** `S1 -> S2` on `git-author-override-audit.log` **fails legitimately and
  forever**, for two independent benign reasons: (a) the **Andrew-authorized 17-record redaction (07-13T16:16Z)
  sits between the snapshots** — a real non-append edit the instrument correctly detects; (b) **S1 is Non-ISO
  extended-ASCII + LF (F-D)** — not byte-comparable to anything.
- **CVO's warning, verbatim, and it is the reason this clause is first-class:** *"if you chain from S1, your
  very first alarm is a false alarm on a legitimate, Andrew-authorized event. An alarm whose first fire is
  noise is an alarm the fabric learns to ignore — and then you have built the fourth costume."*

> **THE FOURTH-COSTUME TEST — apply to this build before shipping.** Today catalogued three:
> a **vacuous PASS**, a **latched alarm**, and a **corpse cadence**. **An alarm that fires but that nobody
> reads is STRICTLY WORSE than the frozen baseline it replaces, because it LOOKS like coverage.**
> **Do not let the cure be the fourth.**

### 3. Division of labour — **detect the EDIT; a human rules on the AUTHORITY** *(CVO, verbatim)*
> The prefix test **cannot distinguish an authorized non-append edit from an unauthorized one, and MUST NOT
> TRY.** It detects the EDIT; a human rules on the AUTHORITY. **That is exactly why it is trustworthy — it has
> no opinion about who was allowed to do what, so it CANNOT BE ARGUED INTO A PASS.**

Alarm text is therefore **"a non-append edit occurred at line N, removing these records"** — **never** *"this
was bad."* **An instrument with no opinion about authority has no surface to lobby.** (Contrast the AI triage
layer, which had opinions about causation and was falsified 3/3.)

**Proof this earns its place:** CVO exercised the prefix test against the 07-13 authorized redaction as a
positive control. **RV-0050's numstat walk on that same event → PASS (vacuous). The prefix test → FIRED**,
localized to line **12925**, enumerated all 17: **12× `serial=1.0.0_SA_CTO`** (`test_never_rules_gate.sh`
fixtures) + **5× `serial=0.0.0_AB_MSTR`** (RV-0048 harness) — **byte-exactly matching MSTR's claim,
serial-for-serial, count-for-count.** *A redaction that was on the record as "(recorded)" and taken on trust is
now **audited**.* **That is what a control that can fail buys you.**

### 4. Alarm-on-its-own-death *(CTO's law)*
> **"A cadence's corpse problem is not solved by adding a cadence. It is solved by ALARMING ON THE CADENCE'S
> DEATH."** — `1.0.0_SA_CTO`, 2026-07-16
The invoker's own liveness is instrumented (absence-registry row, bucket-side, or equivalent). **An invoker
without a failure instrument is just a fourth corpse waiting.** Measured 3× in one afternoon:

| Instrument | Mechanism | Rot |
|---|---|---|
| freshness manifest | snapshot + cadence, no invoker | **29 days** authoritative after its keeper stopped |
| `org/audit/archive/` | snapshot + cadence, no invoker | **3 days** → into a FALSE CLEAN |
| CVO's `git ls-files` criterion | reads the INDEX, not HEAD | would have certified a fix **never committed** |

**Also carry CVO's baseline-freshness as a FIRST-CLASS ALARM, not a note.** Their RV-0050 36-override census
reads against the frozen 07-13 baseline; they had written the caveat (*"a control that verifies the past and is
silent about the present"*) **before** it was measured. In their own words: **"a caveat with no instrument
behind it is a hypothesis, and the estate reads hypotheses as clean."** This clause is what converts it.

---

## Build notes

- **Vehicle:** TBD at CTO's gate. Terraform-only per Deployment Rule 1; no console, no `update-function-code`.
- **Cadence:** the interim manual practice expires **2026-07-23** — that is the build's deadline, not a
  suggestion. After it, no invoker = a finding against this owner.
- **Do NOT** encode "snapshot exists" or "snapshot count" anywhere. If a reviewer asks for either, cite §1.
- **Do NOT** teach the integrity check about authority. If a reviewer asks for an allowlist of authorized
  editors, cite §3 — that is the request that turns it into something that can be argued into a PASS.
- **Positive control before recording a PASS:** run the prefix test against the 07-13 redaction (a KNOWN
  non-append edit). If it does not fire, the instrument is broken. *A sweep that cannot find a known-present
  instance is a broken instrument reporting silence.*
- **Negative control:** an append-only window (S2 → S3) must NOT fire. An alarm that fires on everything is the
  fourth costume wearing a different hat.

## Provenance

`1.0.0_SA_CTO`: ASK-1 grant, the alarm-on-death law, S2-forward binding, the expiry (`c34713b8d`).
`3.0.0_SA_CVO`: the S1 landmine + its two mechanisms, the fourth-costume warning, the division-of-labour line,
the prefix-test positive control on the redaction.
`0.7.0_AE_CloudOps~B`: the archive-rot measurement, the age-not-existence sharpening, the second-data-point
tell, the expiry ask.
