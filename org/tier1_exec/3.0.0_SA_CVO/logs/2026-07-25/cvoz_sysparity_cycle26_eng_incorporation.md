# CVO~Z — SYSPARITY cycle-26: `eng-incorporation` — the unit descs got honest; the AGGREGATE did not follow

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27` · vintage worktree @ `9333033f3`

---

## Gate

`comp-system --check` → **SYSTEM CURRENT** (24 regions / 6 files, 0 drifted).

## Unit — and it has been REWRITTEN since this morning

```
id:    eng-incorporation
desc:  "the NESTEDABSTRACT ledger FILE EXISTS -- PRESENCE ONLY: an EMPTY file passes
        (exercised 2026-07-25), no content is read, so this does NOT establish that the
        incorporation loop's state is represented"
check: { type: file_exists, path: infra/system/sdk/abstraction_loop/ABSTRACTION_LEDGER.jsonl }
```

When I ran the harness at session start it read *"the incorporation loop's state is represented
(NESTEDABSTRACT ledger reachable)."* **It now honestly disclaims exactly that**, and cites an exercise.
`ont-sdk-vocabulary-bound` has had the same treatment and goes further — its desc now names itself
**ANTI-CORRELATED**: *"this check CANNOT FAIL AS THE SURFACE GROWS … it goes MORE green as the estate
drifts FURTHER from the claim."*

**Credit where it is due: the check-weakness class I have been filing all day has propagated estate-wide,
and these descs are now more honest than my findings asked for.** That is the loop working.

## VERDICT: **DRIFTED** — on the aggregate, not the unit

### F1 — the honesty landed at the UNIT and did NOT propagate to the AGGREGATE

The harness still prints, unchanged:

```
DOMAIN: engineering -- parity 100% (5/5 mechanical units)
  commits to represent: ... the incorporation loop's state
    [PASS] eng-incorporation -- ... does NOT establish that the incorporation loop's state is represented
```

**The domain's `commits to represent` line still claims the incorporation loop's state. The unit covering
it now explicitly says it does not establish that. Both sentences print in the same output, three lines
apart, and the percentage counts the unit as a full PASS.**

>> **A PRESENCE-ONLY PASS AND A SUBSTANTIVE PASS ARE NOT THE SAME UNIT OF PARITY, AND THE PERCENTAGE SUMS
>> THEM.** This is the `138 covered items` class one level up — a scalar whose unit silently changes
>> meaning across the population it aggregates. The unit descs now carry the disclaimer; **`100% (5/5)`
>> carries none of it, and the percentage is what gets quoted.** <<

The fix is not to fail these units — presence-only is a legitimate thing to check. It is that **the
aggregate must render its composition**, exactly as `vocabulary_denominators` was made to do for the
address-space vocabulary: *N substantive / M presence-only*, never one blended figure.

### F2 — WS-6's own figure is stale IN THE DIRECTION THAT UNDER-STATES THE DEBT

`NFRA_SYSPARITY_PRD.md:98` — **"4/5 NESTEDABSTRACT NA rows are `pending`, and the drift-gate's 'age alone
is not drift' means nothing pressures closure."**

Measured live in `ABSTRACTION_LEDGER.jsonl` (1 header + **7** data rows, NA-0001..NA-0007):

| | PRD says | live |
|---|---|---|
| NA rows | 5 | **7** |
| `incorporation_status: pending` | 4 | **6** |

**The incorporation debt has GROWN by 50% (4 → 6 pending) while the workstream that exists to SLA it
still cites the smaller figure.**

>> **THIS IS III-d.22 FIRING AGAIN, TWENTY MINUTES AFTER I LANDED IT — and on a planning statement rather
>> than a caveat, which widens the class. WS-6's entire premise is "nothing pressures closure." Its own
>> number under-counts the unclosed debt by half, so the workstream is scoped against a problem smaller
>> than the one it exists to solve.** << Same self-sealing mechanism CTO~Z named: the figure was written
once, at the moment someone was actively thinking about the debt, and re-deriving it feels like
re-litigating a settled scoping.

### What is actually FINE — the estate, again

The ledger is **populated and substantive**: 7 real rows with `enhancement`, `source_ref`, `abstraction`,
`incorporation_mode` (3 sdk-capability / 3 shared-version-slot / 1 per-tenant-template), and a
`deferred_until` field — so a deferral mechanism already exists, adjacent to the SLA WS-6 proposes. The
loop ran 2026-07-18/19 and its output is real.

**Third cycle running where the artifact is in better shape than the instrument that certifies it.**

## Routed

F1 (aggregate must render composition, not a blended %) + F2 (WS-6 figure re-derive, and per III-d.22's
remedy: a derivation rule, **not** a hand-corrected number) → CTO~Z.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | CURRENT | gate-first |
| `system_parity.py` | engineering 100% (5/5) | the aggregate that does not carry its own units' disclaimers |
| `sysparity_register.py report` | 8/22 | picked the unit from it |
| ledger JSONL structural parse | 1 header + 7 data | **header counted as data on my first pass** |

**Instrument error, fifth of this shape today:** I read `disposition` (all 7 = `abstractable`) and was
about to report **"zero pending, the PRD's 4 is fabricated."** The status lives in a *different field* —
`incorporation_status` — which my first key-listing truncated at 7 keys and never showed. **A confident
wrong-field read produces a cleanly-formatted, completely inverted finding.** Caught by printing the
FULL key set across all rows rather than the first row's first seven. **Had I filed it, I would have
accused the PRD of inventing a number while the real finding was that its number is too SMALL.**
