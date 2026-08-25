# SIZING: `org/critical_paths/.open_findings/` - 210 findings, measured

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-08-24 · **Andrew-direct:** approved on the /next-steps set.
**Verdict in one line: this is not a backlog. It is one advisory instrument that emits automatically
and is deleted manually, which guarantees the number only ever grows.**

---

## 1. The population

| | |
|---|---|
| Files | **210** (209 json + 1 md) - **it was 207 when I started measuring** |
| Parsed clean | 209 of 209 json, **0 unparseable** |
| Distinct finding types | **1** - `closeout-drift` |
| Distinct severities | **1** - `advisory` |
| Distinct triggers | **1** - `closeout-comp-state-post-commit (NFRA_MSBEFF.R4-A)` |
| Owners | 181 `2.0.0_SA_COO~Z` · 20 `1.0.0_SA_CTO` · 4 `4.0.0_SA_CRO` · 1 `1.0.0_SA_CTO~A` · 1 `0.0.0_AB_MSTR~Z` |
| **From ONE sweep** | **181 of 210 (86%), all stamped `20260806T23`** |

**So the headline number was never 210 findings.** It is **one sweep that fired 181 times in a single
moment**, plus roughly 29 individual fires since - twelve of them today, three during this sizing.

---

## 2. Classification against the instrument's own oracle

**Oracle:** `comp-state --json` at HEAD. Self-test **PASS 4/4** ("the instrument discriminates") run
as a gate before any verdict was read. **`--json` output is documented as never truncated** - which
mattered, because the text report renders only the top 60 of 902 drift rows and reasoning from that
page would have produced a confident wrong answer.

| Class | n | % | What it means |
|---|---|---|---|
| **LIVE** - the project's JSON record still reads `BEHIND` | **121** | 58% | the drift the finding names is still there |
| **CHANGED** - now `POST-CLOSE`, no longer `BEHIND` | **54** | 26% | a different state; the finding's stated condition no longer holds but a new one does |
| **CLOSED-IN-FACT** - no `BEHIND` on the JSON record | **35** | 17% | deletable now |

**Controls:** `ADVI_49FSRC`, which the text report printed as `[BEHIND] JSON`, classifies LIVE -
so the classifier agrees with the instrument on a known case. A fabricated project name is absent,
so the classifier is not matching indiscriminately.

**MY PRIOR WAS WRONG AND IS RECORDED AS SUCH.** I predicted "a large fraction will read
closed-in-fact," reasoning by analogy from the binding reconciliation where 76 deflated to 8. **It
did not repeat: only 17% are closed-in-fact and 58% are live.** The analogy failed because the two
populations have different physics - a binding is discharged by a human act that may go unrecorded,
while this drift is re-evaluated by a running instrument every time it fires. **An analogy between
two populations is not evidence about either.**

---

## 3. The actual finding, which is structural rather than numerical

Each file carries its own disposal instruction: *"Resolve the drift or record why it is expected,
then delete this file."*

**BIRTH IS AUTOMATED. DEATH IS MANUAL. Nothing else about the system needs to be wrong for the
count to grow without bound** - and it grew by three during the hour I spent measuring it.

This is the same shape as the closure gap in the binding matrix, with the asymmetry sharpened: there,
both birth and death were manual and death simply never happened. Here the birth side is a running
job. **A manual deletion step behind an automated emitter is not a workflow, it is a queue with no
consumer**, and 181-at-once is what that looks like when the emitter sweeps.

**Note also that deleting 181 files by hand is not a task anyone will do**, which is why they are
still here 18 days later. The disposal instruction is individually reasonable and collectively
unexecutable.

---

## 4. What this means for the cleanup pass

- **35 are deletable immediately** on today's measurement, with no judgment required.
- **54 need one adjudication each** - `POST-CLOSE` is a different condition from the `BEHIND` the
  finding was raised against, so neither deleting nor keeping is automatic.
- **121 are real drift** and are the actual repo-cleanup surface. They are JSON/REGISTRY consistency
  items - an unmoved row, an open TO, a record behind its closeout commit.
- **The emitter keeps firing**, so any sweep that does not also change the disposal mechanism is
  re-run work.

**RECOMMENDATION, and it is a design change rather than a cleanup:** give the emitter a **read-time
verdict instead of a durable file**. The condition is already recomputable on demand - that is
precisely what this sizing did, in one command, over the whole population. A finding whose truth is
recomputable does not need to be stored, and storing it is what created the manual-deletion step
that nobody performs. **This is the same remedy as the discharge lease: compute standing at read
time rather than writing a status that then has to be un-written.**

---

## 5. Method note

`comp-state` is a Python entry point. I first invoked it through `bash`, which produced a cascade of
shell syntax errors - the exact inverse of an error made earlier the same day invoking a bash tool
through `python`. **Both failures were loud and cost seconds. The failure that costs is the one that
returns a well-formed answer to the wrong question**, which in this case would have been reading the
truncated 60-row text report as though it were the 902-row population.
