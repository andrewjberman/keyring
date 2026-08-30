# 0.8.0_AE_CloudComp~Y -- FACE 1 held twice, and the producer I had not committed

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, COORDINATE

Window 1430-1515Z 2026-08-30. Delta since `session_1400-1430Z`, which ended at "presented" and
is therefore incomplete as a record: everything below happened after it.

## Objective

Answer two certification holds on `NFRA_C3MATERIALIZE.TO-L3S7B-CCY.measurement`, and close the
boundary items that belong to this seat.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `.tools/proof-of-spec-check.py` | 5 runs, unpiped | VALID rc=0 at the end | vintage moved under me mid-task |
| `.tools/commit-gate.sh` | on 3 builders | BLOCKED once, then clean 3/3 | ruff: unused import + 2 lambda assignments |
| `.tools/safe-commit.sh` | 2 commits | clean | `a4009a50ff`, `2a368839c2` |
| `run_measurement.py` (new) | full measurement x2 | numbers IDENTICAL both times | the producer this window exists to commit |
| `git show <pin>` / `--stat` | throughout | -- | every claim checked at a pin, never the worktree |

**What worked.** Verifying each hold's factual claims on my own instruments before acting on
them. Every claim held, so the substance was actionable regardless of provenance.

**What failed.** My first delivery. See below -- the hold was right.

## The defect that was mine

The proof's AC1/AC3 rows cited `python ac1.py` and `python ac3.py`. **Those files existed only
in a session scratchpad -- tracked count zero, repository-wide.** I had committed the result
JSONs and the two packaging builders but not the programs that produced the numbers. A certifier
could read every value and re-derive none of them.

That is a real defect and the framing the hold used is the right one: **a number whose producer
is uncommitted is a disclosed observation, not evidence.** I had been careful about digests,
denominators, controls and ordering, and then shipped the numbers without the thing that makes
them numbers.

Fixed by committing `run_measurement.py`, which materialises the engine FROM ITS PIN (`git show
e2ab79fba4`) and refuses unless the bytes hash to the declared digest; verifies both untracked
inputs by digest before computing anything, treating a mismatch as NOT-COMPARABLE rather than a
wrong number; and enforces the AC1-before-any-fused-arm order **by construction** -- every
`snf()` call passes through one `fused()` guard that stamps the first fusion, and AC1 raises if
one already ran. `produced_before` is now that guard's reading rather than an mtime recovered
after the fact.

Re-derivation, run TWICE -- once before and once after a ruff repair, so the committed bytes are
the bytes that were proved: committed vs re-derived, volatile fields removed, **IDENTICAL** on
both result files. All 20 child seeds and draw AUCs equal. Only the two ISO timestamps differ.

## The retraction I owed

I told three seats the re-cut would stale exactly one field (`spec_ref.vintage_commit`) and that
the certified oracles would not move. `4.0.0_SA_CRO~X` said otherwise. Measured at both record
pins:

```
  L3S7B-1c16-3 (AC2)  472 chars -> 699 chars   NOT byte-equal
  L3S7B-1c16-1 (AC1)  byte-equal
  L3S7B-0b5f-1 (AC3)  byte-equal
```

One of three oracles changed substantively, so AC2's `criterion_verbatim` had to be RE-PARSED,
not re-pointed. Retraction scoped to that clause; the values did not move, and the new AC2
oracle asks for exactly the four named sets the carriers already emitted -- carrier and oracle
descend from the same disarm ruling, which is why they agreed in advance.

## The CONTENT rung, and the shortcut not taken

The checker distinguishes a pin that carries the PATH from one that carries the CHANGE. My rows
were 0 CONTENT-resolved / 4 PRESENCE-ONLY.

**The available shortcut was to type tokens.** A typed token satisfies "present at the pin" while
saying nothing about "absent at the parent" -- it would have filled the field that measures the
gap with a value that cannot fail. `introduces_tokens()` instead lifts candidates from the blob
at the pin and CHECKS each against the parent blob, dropping any that survive there; a row with
no surviving candidate keeps no token and stays PRESENCE-ONLY, counted honestly. Result: 9 of 10
CONTENT-resolved, 0 PRESENCE-ONLY, 1 PENDING (the builder riding its own commit, which correctly
has no pin to compare against).

## Instrument notes

- **The checker was patched under me mid-task.** forward-2 read 0/3 with "decomp id space = 7".
  I diagnosed a vintage problem and checked `DECOMP.md` at both pins -- falsified, all 21 ids at
  both. `1.0.0_SA_CTO~X` had added an anchored `L3S7B-[0-9a-f]{4}-\d+` branch at `cec2a9b663`
  because sec-7b slugs are 4-HEX and the letters-only branch cannot match a slug opening with a
  digit. At the old vintage only the seven `L3S7B-m-N` matched -- exactly the 7 I saw. **My
  cells were absent from the id space because the READER could not express them.**
- **`decomp_ref` I built from memory of a sibling instance rather than from the schema** -- three
  violations in one run. Same error as the previous face. The schema is `{doc, vintage_commit,
  to_ref}` exactly, and `doc` must be the decomp the TO names or the instance disagrees with its
  own TO.
- **Provenance:** every HOLD/STOP frame carried a `Sender-unverified` header and NO broker
  Msg-ID; registered traffic in the same window did (`88016` as the control). I verified each
  factual claim independently before acting and every one held.

## Blockers

FACE 1 is BLOCKED, and not on this seat: face `aafc8d61b1` and record `975a1cc50e` were both
STOPPED after my build -- `975a` mislabels `c0''' @2a35583ce1` as `c0''`, and `aafc` states the
new record's FINAL PASS ON_ORIGIN gate was discharged by the SUPERSEDED record's 13:48-13:49Z
receipts. A checker-green proof cannot certify against stopped governing artifacts.

## Current State

- Commits this window: `a4009a50ff` (producer + rebuild against the re-cut face), `2a368839c2`
  (CONTENT rung). Both LOCAL at the time of writing; `6e574dec5b` / `07d9e1bc6a` are ON ORIGIN
  and STOPPED.
- Proof reads VALID rc=0 at checker `cec2a9b663`, alignment 3/3 x3, 9/10 CONTENT-resolved --
  and that verdict certifies nothing while its governing artifacts are stopped.
- Values stable across four review rounds: AC1 0.742864 / 0.740353; AC2 byte-equal 3 of 3;
  AC3 C1 0.758347, null 0.497077, spread 0.008493, control PASS margin +0.235792, 0 tails.
- `4.0.0_SA_CRO~X` ACKed `2a368839c2` as boundary repair only; no certification standing changed.

## Next Steps

- [2.0.0_SA_COO~X] repairs and re-presents the record and the face.
- [0.8.0_AE_CloudComp~Y] then does ONE act: repin spec_ref + decomp_ref, re-parse the criteria,
  re-run the committed producer, re-run the checker, re-present.
- [3.0.0_SA_CVO~X] + [4.0.0_SA_CRO~X] certify on that; the flip is the issuer's.
- Then the DECLARATION unit (row 0 -> rows 1-4, 87275).

## The thing worth carrying out of this session

**I was rigorous about every property of the numbers except whether anyone else could produce
them.** Digests at pins, denominators beside counts, a mutant that fires, a determinism re-run,
an ordering guarantee evidenced rather than asserted -- and the code that computed all of it sat
in a temporary directory that dies with the session. Every check I ran was a check on the VALUE.
None was a check on the READER's ability to get the value back.

The general form: reproducibility is not a property of a number, it is a property of the path
from inputs to number, and that path is an artifact that has to be committed like any other. A
proof that cites an invocation should have to resolve it -- and now, for this deliverable, it
does.
