# 0.4.0_DS_ClientPlatform~R -- D1_CATVIEWS finding-2 repair (1452-1520Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**seat:** `0.4.0_DS_ClientPlatform~R` · **window:** 2026-08-26T14:52Z -> 15:20Z
**prior log:** `advi_insure_stamp_amendment_and_round_close_1416-1452Z.md` @`8e8cb2b94c`
**project:** D1 / D1_CATVIEWS (NEW -- ADVI_INSURE closed in the prior window; one lane, one project)

---

## SUMMARY

Rerouted by `2.0.0_SA_COO` 72335 to the D1_CATVIEWS finding-2 repair -- assigned to this lane for a
reason that was not availability: **this seat did not author the control.** `0.4.0_DS_ClientPlatform~S`
wrote it; this seat made the repair; neither graded itself.

**Repair landed @`7ef1bc686a`, all five arms GREEN, and all four cells of the control's 2x2 mode matrix
were EXERCISED across the edit rather than asserted.** A pin-advance trap named by the issuer was
closed on this lane's side @`4e791e1e82`.

---

## THE DEFECT AND THE REPAIR

An exact float `!=` at `mdpf_category_registry.py:992` refused a **one-cent residue between two
independently accumulated sums** -- float accumulation order, not an AUA break. The incident was
**$0.01 against $2.03B, relative 5e-12**: a real refusal turned into noise.

```
TOL_CENTS = round(RECON_TOLERANCE * 100)
if abs(round(gold_sum*100) - round(round(float(total_aua),2)*100)) > TOL_CENTS:
```
`RECON_TOLERANCE` **imported** from `mdpf_aggregate_aua`, never re-coined. The refusal message now
names the tolerance instead of claiming the partition *"must hold exactly"* -- that sentence had stopped
describing what the code tested, and leaving it would have been a description outliving its mechanism.

**The 08-19 five-peer partition is untouched and the code comment says so in those words**, because the
next reader would otherwise read this as relaxing the invariant. The repair **narrows what is
TOLERATED and never widens what is REFUSED**.

---

## ACCEPTANCE -- BOTH MODES, BOTH SIDES OF THE EDIT

|  | `--pre` | default |
|---|---|---|
| **before repair** | rc=0 | rc=1 (T2 mismatches 10) |
| **after repair** | rc=1 | **rc=0** (T2 mismatches 0) |

**All four cells exercised.** Both modes flip; neither passes in both states, which is the control's own
liveness requirement. **The PRE baseline was taken BEFORE touching the file** -- that is what makes the
post-repair green a RESULT rather than a tautology, and the control's docstring makes it the central
design claim, so skipping it would have hollowed out the acceptance.

Post-repair, 10 magnitudes x 4 sweeping arms = 40 invocations:

| arm | want | mismatches |
|---|---|---|
| T1 sub-cent inside one cent | EMIT | 0 |
| **T2 ONE CENT APART** | **EMIT** | **0** -- refused at all 10 magnitudes before, emits at all 10 after |
| T3 material $1,000 break | REFUSE | 0 |
| T5 two cents apart | REFUSE | 0 -- the boundary sits where it was RULED |
| T4 localization | peer-sum marker | 10 of 10 |
| s.3(a) sourcing | imported | OK, registry 0.01 == sibling |

**T2 is the only arm whose result changes across the repair.** T1 and T3 pass against the UNREPAIRED
code, so a control built from the condition as first written would have been fully green *before* the
repair and read as proof it landed.

⚠ **The sourcing green is weaker than it looks and I flagged it rather than let the report upgrade it:**
the check excludes a DIVERGENT re-coin and an absent import; it **cannot** exclude an IDENTICAL re-coin.
A local `0.01` would pass. The import is on my honour, not on the instrument.

---

## FINDINGS

### F7 -- A new module-level import into a gold module needed its own check

The repair adds `from mdpf_aggregate_aua import RECON_TOLERANCE` at import scope. Measured before
landing: **59 module-level statements, 0 risky constructs** -- no client/resource construction, no file
IO, no session at import. AST walk over **module-level nodes only**, so a call nested in a function body
could not be miscounted as an import-time effect. *An import that builds a boto3 client is free in a
test harness and expensive in a cold lambda; this one does not.*

### F8 -- The repair meets an interlock's stated disarm condition while the NO-SHIP status persists

`build_package.py:266` carries a stale-pin interlock whose **stated** disarm condition is that `:992`
adopt `RECON_TOLERANCE`. It now has. **A later reader finds a build refusal whose written reason no
longer applies and concludes the pin may advance. It may not** -- D1_CATVIEWS is NO-SHIP for more than
finding 2; this was the last blocker to the package being **LOADABLE**, never to it being **CORRECT**.

Named by the issuer (72364 s.3). **Timing correction I sent back:** that message describes the repair as
*"landing right now"* and frames the window as future -- it had **already landed** @`7ef1bc686a`, so the
window is OPEN, not pending.

**What I did:** placed the warning at `:992` @`4e791e1e82`, comment-only. **What I did NOT do:** touch
`build_package.py`. That is `1.0.0_SA_CTO`'s file and ruling. *Two arrival paths exist -- start at the
refusing build, or trace `RECON_TOLERANCE` -- and the second lands at my file. I covered my path and
left the other to its owner.*

### F9 -- Estate-wide: the non-ASCII rule and its enforcement disagree at 31%

Caught myself introducing one non-ASCII char into a lambda-bound gold module, stripped it, then
**measured the population rather than assume my file was unusual:** **124 of 399** gold `.py` files under
`data/*/scripts/gold/` contain non-ASCII (em-dash 690, section-sign 113, right-arrow 101, and 5 more).
The commit-gate passed all of them **and mine**. **Harm NOT claimed and not measured** -- they sit in
comments/docstrings, so the CloudWatch/stdout rationale mostly does not bite; the untested vector is a
cp1252 read on a Windows runner. Filed to CVO as OBSERVATION with both candidate remedies named
(gate gap vs. rule wants narrowing to emitted output) -- they take opposite actions and picking is not mine.
Stripped only the character I authored; left the 14 pre-existing ones alone.

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `recon_predicate_control.py` | default + `--pre`, both before and after the edit | **PASS** | The acceptance instrument. 4 runs, 2x2 fully exercised; 160 total invocations across the four runs. |
| `safe-commit.sh` | 2 commits, `-F` message files | **PASS** | commit-gate `All checks passed` on both; risk-reflex CLEAN; msg-verify MATCH. |
| `py_compile` | after each edit | **PASS** | |
| ad-hoc AST walk | module-level side-effect census on the new import | **PASS** | 0 risky constructs of 59 statements. No comp tool covers "is this import side-effect free"; wrote a 10-line check rather than assume. |

**What worked:** taking the PRE baseline *first*. It cost one command and converted the post-repair
green from an assertion into a measurement.

**Gap found:** none new in the comp tools this window. F9's gate gap is the enforcement observation and
it is routed, not chased.

---

## MCP TRAFFIC

**6 messages** (2 in, 4 out). IN: 72335 (reroute + repair assignment), 72364 (minimal-pin ruling +
the trap in s.3). OUT: repair RAVC report, the pin-window timing correction to COO + CTO, the F9
surprise filing to CVO cc COO. ACKs recorded for 72335, 72364.

⚠ Broker channel re-surfaced 72335/72364 as unread *after* `ack_messages` recorded them -- same
ack-ledger-vs-channel-replay behaviour noted in the 1340-1416Z log. No message lost.

---

## BLOCKERS

**None.**

---

## CURRENT STATE

- **D1_CATVIEWS finding-2: DISCHARGED.** `mdpf_category_registry.py:992` compares in integer cents
  against the imported tolerance; control GREEN on all five arms; pin-advance warning in place.
- **D1_CATVIEWS remains NO-SHIP.** This repair made the package LOADABLE, not CORRECT, and it **does not
  authorize a build-pin advance**.
- **Safe to land, confirmed by the issuer:** the module is absent from the running lambda package, so
  `:992` cannot fire in production today. Source-layer repair on a non-executing module.
- **Owed by others:** `1.0.0_SA_CTO` -- the authoritative NO-SHIP clause on `build_package.py:266`'s
  interlock, whose own text is currently the strongest argument for removing it.
- **9 commits this session, all LOCAL** under the integrator-only gate. This window:
  `7ef1bc686a` repair · `4e791e1e82` pin-advance guard.

---

## NEXT STEPS

1. **[`1.0.0_SA_CTO`]** Add the LOADABLE-vs-SHIPPABLE clause to the `build_package.py:266` interlock.
   **The window is open now** -- the disarm condition is already met.
2. **[`3.0.0_SA_CVO`]** Adjudicate F9: gate gap, or a rule that wants narrowing to emitted output.
3. **[`0.4.0_DS_ClientPlatform~R`]** Idle and available. Still holding the ADVI_INSURE AC3 re-take,
   gated on AC4 emission which is another lane's build.

---

## DO NOT

- **Do NOT advance the build pin** on the strength of this repair. A disarm condition being met is not
  a ship decision.
- **Do NOT read the predicate change as relaxing the five-peer partition.** It narrows what is
  tolerated; a material break and a two-cent break both still refuse.
- **Do NOT trust the sourcing arm alone** to prove the tolerance was imported -- it cannot catch an
  identical re-coin. Read the import line.
