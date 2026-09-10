# NFRA_REPORT — PRD ADDENDUM 01: THE SYNTHESIS

**archetype:** SCRIBE (spec)

| | |
|---|---|
| **Authored by** | `1.0.0_SA_CTO~Z` (L2–L4 owner) |
| **Authored** | 2026-09-10 ~14:1xZ |
| **Authority** | Andrew-direct at the `1.0.0_SA_CTO~Z` terminal, VERBATIM: *"What I need you to do is an addendum to the PRD that covers the synthesis of this tool with the existing resource... Write that now and issue to the relevant COO on the case so they can begin decomposing/cutting the full addendum into TOs"* |
| **Adds** | `FWD-13`, `FWD-14`, `FWD-15` to the PRD's 12 |
| **Cut owner** | `2.0.0_SA_COO~ZZ` at L5/L6 |

---

## 1. WHY THIS ADDENDUM EXISTS

Andrew received the 9 AM infrastructure email on 2026-09-10 and **saw no change**, after this project
had been graded 11 of 12 outcomes realized. He was right, and the measurement is unambiguous:

| | measured |
|---|---|
| `compose_edition.py` locations across the estate | **1** — a worker's deliverables folder. **0 hits across all 6,415 files of `infra/`** |
| live emailer `opal-infrastructure-monitor` code vintage | **2026-07-08** — two months before this project was registered |
| this project's 74 files naming either live job | **0** |

⛔ **AND THE SHARPER FACT, WHICH IS WHY A CODE SWAP WAS REFUSED:** `compose_edition.py` performs
**zero live reads** — no boto3, no requests, no AWS call. Its facts are `ROW_FACTS`, a hard-coded
Python list of hand-transcribed round-1 findings. Its own docstring says so: *"This script does not
re-run any live AWS read... It composes what already exists."* **Deployed as-is it would email the
same frozen 9-September snapshot every morning forever, and it would look correct while doing it.**

⭐ **SO THE PROJECT DID NOT BUILD A REPLACEMENT. IT BUILT A SPECIMEN** — a worked proof of the
FORMAT, verified against real findings. That is real work and it is not wasted; it is the half that
was hard. **This addendum is the other half: joining that format to a collector that already runs.**

**THE GRADING LESSON, RECORDED BECAUSE IT IS THIS SEAT'S** — and **CORRECTED ~14:3xZ, because the
first version of it let this seat off too lightly.**

11 of 12 outcomes were graded REALIZED against artifacts that can never run in production.

> ⛔ **THIS PARAGRAPH ORIGINALLY READ: *"no outcome asked whether the thing being graded could produce
> tomorrow's edition. The question was absent from the spec, so grading could not have caught it."*
> THAT IS FALSE AND IT EXCUSED THE WRONG PARTY.** Raised by `3.0.0_SA_CVO~Z` (`Z-S19`
> @`7577025b1e`) at this seat's own invitation; verified here against the PRD before accepting.
>
> **THE QUESTION WAS IN THE SPEC ALL ALONG. EIGHT of the eleven REALIZED grades sit on an EXERCISED
> bar** — `FWD-1`, `3`, `5`, `6`, `7`, `8`, `11`, `12`. Only `FWD-2`, `9`, `10` carry APPLIED, which
> a specimen genuinely satisfies. `FWD-1`'s own DONE WHEN requires *"at least one morning where the
> verdict was 'nothing'"* — a verdict that **DIFFERS ACROSS MORNINGS**, which a hard-coded fact list
> cannot produce under any reading.
>
> **The grading pass read each outcome's ACCEPT paragraph — what the report SHOWS — and not the DONE
> WHEN line directly above it, which says it must have RUN. Two adjacent lines of the same block.**
>
> ⭐ **A BAR THAT SAYS "EXERCISED" DOES NOT ENFORCE ITSELF.** Rule 22's STATE axis, failing on a bar
> that named the exercise it wanted. Re-graded in `ledger/ROUND_ANALYSIS.round2.md`: **3 REALIZED,
> 9 APPLIED of 12.**

⚠ **SO `FWD-13` IS NOT WHOLLY NEW, AND s.5's "not a re-litigation" IS AMENDED.** For `FWD-2`, `9`
and `10` it is a genuinely new bar. For the **eight EXERCISED outcomes it is the bar they already
carried**, and a new outcome numbered 13 does not retire a grade recorded against outcome 1.

⭐ **THIS COSTS THE CUT NOTHING AND MUST NOT DELAY IT.** The same deployment that satisfies `FWD-13`
**exercises all eight at once**. The difference is entirely in what the round may CLAIM afterwards,
not in what it must BUILD — so `2.0.0_SA_COO~ZZ` decomposes exactly as issued.

---

## 2. THE SEAM — BOTH HALVES ALREADY EXIST, WHICH IS WHY THIS IS SMALL

### The live side — `infra/aws/lambda/infrastructure_monitor/lambda_function.py` (2,591 lines)

Already does, every weekday at 9 AM ET, and **must be preserved**:

- **collects live state** — `check_lambda_health()`, `check_smartx_pipeline()`,
  `check_data_freshness()`, `check_deploy_drift()`, `check_producer_drift()`
- ⭐ **`_load_prior_report()` — IT ALREADY PERSISTS AND RELOADS THE PREVIOUS REPORT.** This is the
  single most important fact in the addendum: **the per-row delta's "previous state" substrate
  already exists on the live side.** Nothing needs building for it.
- **sends** — `send_email(email_body, report)` via SES, on an EventBridge rule that already fires.

### The specimen side — `compose_edition.py`

Already implements, and **is the thing being ported**:

- `compute_delta()` / `compute_delta_watch()` — per-row `worse | better | unchanged`, never a
  `max()` across rows
- `compute_verdict()` — the top-line "does anything need Andrew today" rule
- `render_markdown()` — the row structure, the attribution column, the per-row reading
- the **QUOTED / COMPUTED / GENERATED** three-region discipline, declared per row

### ⭐ THE JOIN IS ONE SUBSTITUTION, AND THE SPECIMEN'S OWN ARCHITECTURE MADE IT SO

`compose_edition.py` already separates its **data** (`ROW_FACTS`, QUOTED) from its **logic**
(COMPUTED) and its **prose** (GENERATED). **The synthesis replaces the data source and keeps the
other two unchanged:** the row list stops being a literal and starts being the collector's output,
mapped into the same row shape the compute functions already accept.

That separation was designed for legibility, not for this — but it is what makes this a port rather
than a rewrite, and the cut should exploit it rather than re-architect around it.

---

## 3. NEW OUTCOMES

```
  FWD-13  The morning email a person actually receives carries the new edition's
          structure with TODAY's live numbers
         DONE WHEN  EXERCISED -- a real 9 AM email has arrived carrying live collected
                    values rendered in the edition format, and a person has checked at
                    least one row's state and delta against the underlying data and
                    found it right
         ACCEPT     Andrew opens the morning email and sees per-row state, per-row
                    delta and attribution over real numbers. NOT a specimen, NOT a
                    file in the repo -- the email.
         BOUND BY   C-NO-FROZEN-FACTS, C-NO-REGRESSION (section 4)

  FWD-14  The report's facts come from the live collection, never from a literal
         DONE WHEN  APPLIED -- the deployed path contains NO hard-coded fact list;
                    the composer's rows are built from the collector's output, and a
                    check that changes state on Tuesday changes that row on Wednesday
         ACCEPT     a grep of the DEPLOYED package for the transcribed fact list
                    returns zero, and two consecutive editions differ where live
                    state differed
         BOUND BY   C-NO-FROZEN-FACTS

  FWD-15  Nothing a reader relies on today disappears in the swap
         DONE WHEN  EXERCISED -- the first new edition has been compared against a
                    saved copy of the last old one, and every section the old email
                    carried is present in the new one or its removal is recorded with
                    a reason
         ACCEPT     a named before/after comparison exists; no section vanishes
                    silently
         BOUND BY   C-NO-REGRESSION
```

---

## 4. CONSTRAINTS ON THE CUT

**`C-NO-FROZEN-FACTS`** — no transcribed fact may reach the deployed path. If a row cannot yet be
collected live, it is **omitted with a stated reason**, never rendered from a literal. A frozen fact
in a daily email is worse than an absent row, because it looks current.

**`C-NO-REGRESSION`** — the live collector's existing sections are preserved unless a removal is
recorded. ⚠ The cut must read the current Lambda before changing it: it is 2,591 lines and carries
more than this project measured.

**`C-DEPLOY-PATH`** — ⛔ **NEVER `aws lambda update-function-code`.** This function's own Terraform
says so explicitly. The only path is artifact → `s3://opal-<account>-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip`
→ `source_code_hash` → **`safe-apply`**, at `infra/aws/terraform/shared-infra/infra-monitor.tf`,
resource `aws_lambda_function.infra_monitor`. Package is dep-free and boto3-only; the composer is
pure-python, so **no new dependency and no layer is required** — verified: zero third-party imports.

**`C-CHANGE-LEDGER`** — this touches a daily email to Andrew. A change-management entry under
`org/critical_paths/change_management/` is **opened before the first deploy act and closed at
completion**. Half-landed is not an option: finish in session or roll back and say so loudly.

**`C-MORATORIUM-CLEARED`** — the standing no-alerts moratorium does **not** block this. Andrew's
word, VERBATIM: *"this isnt creating an alarm, it is just swapping out the code of the existing
lambda"*, and *"wire it up so tomorrow's email is the new one, then run a manual trigger so i can see
the output."* ⚠ This clears **this** work only — no new alarm, topic, schedule or notification may be
minted under it.

**`C-MANUAL-TRIGGER`** — Andrew asked to see the output without waiting for 9 AM. A manual
invocation of the deployed function satisfies this; it is a QA exercise and the **scheduled fire
remains the acceptance**.

---

## 5. WHAT THIS ADDENDUM DOES NOT DO

- It does **not** re-open or re-grade `FWD-1`–`FWD-12`. They were graded against the specimen and
  those grades stand on their own terms. `FWD-13` is a **new** bar, not a re-litigation.
- It does **not** rebuild the collector. The live Lambda's checks are reused as they are.
- It does **not** ask for a second report. There is **one** morning email and it keeps its schedule,
  its recipient and its delivery path.
- It does **not** widen scope to the estate report (`estate-report-0900et`), which belongs to a
  different directive and is untouched.

---

## 6. FOR THE CUT

`2.0.0_SA_COO~ZZ` owns L5/L6. The natural shape is small and the dependency chain is short — read
the live collector, map its output into the composer's row shape, port the compute/render functions,
deploy on the Terraform path, then exercise. ⚠ **The mapping cell is the one that carries the risk**,
because that is where a frozen fact could re-enter; its acceptance criterion should score the
**deployed package**, not the source.

**Nothing here is owed by Andrew** beyond what he has already given: the authorization above, and
seeing the manual trigger's output when it runs.
