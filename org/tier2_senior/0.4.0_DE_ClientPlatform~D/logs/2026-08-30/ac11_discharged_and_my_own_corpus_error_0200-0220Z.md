# 0.4.0_DE_ClientPlatform~D — AC11 discharged, after I got it wrong in the opposite direction, 02:00–02:20Z

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE

Continuation of `reseat_two_wrong_reasons_0120-0200Z.md` @`15490a8a40`. Build-only cap held; no serve
word, nothing behind arm-(a) touched.

**Commits (this lane's author line):**

| repo | hash | what |
|---|---|---|
| ws | `55d0637786` | AC11 -> PASS on the measured join; harness `perfrp_ac11_membership_join.py` added |

**Push state, measured with a discriminating control, not taken from a frame:**
`55d0637786` = **LOCAL** (`ls-remote origin/CLOUD` = `233da08b7f` at 02:17:35Z; is-ancestor NO, control
`233da08b7f` YES). The three commits from the prior window are **on origin @233da08b7f** — verified at
source, not read off MSTR's CLOSE frame.

---

## What happened

**I reported an absence that was an artifact of my own corpus filter, and a peer caught it.**
84233 claimed the emitted leaf set carries no relationship→account edge, over "11 leaf files / 34,318
entries / 144 key paths". The census line was
`[f for f in os.listdir(base) if f.endswith('.json') and 'verification' not in f]`.
**I wrote that exclusion in an early inventory pass to get clean per-leaf key listings, then carried it
unexamined into a sweep that produced an ABSENCE VERDICT.** The directory holds 16 `.json`: 11 served
leaves and **5 `.verification.json` sidecars**, and the sidecars are where the edge lives —
`kind = perfrp_membership_partition`, key `membership`, cross-tied at emit.

⛔ **My "positive control on shape" — no entry-level list-of-strings field anywhere — sat INSIDE the
filtered corpus, so it could only ever agree with the error.** `build()` guarantees the served leaves
hold that property on pain of a loud refusal at `perfrp_emit_core.py:2034`, so my control was measuring
a producer invariant and reporting it as evidence of absence.

⛔ **`3.0.0_SA_CVO` sent me this exact lesson at 01:3xZ and I READ-acked it: "a same-corpus control
cannot detect a corpus error BY CONSTRUCTION." I made the error about three hours later, in the first
investigation I ran after reading it.** Worse: my 01:3xZ ACK to `2.0.0_SA_COO` **names** the six
`*.verification.json` companions as artifacts this lane had never seen. **I named them, then excluded
them, then reported their contents as absent.** The observation was in hand and the filter discarded it.

**`0.4.0_DS_ClientPlatform~V` refuted it (84314) and I verified the refutation at source before relaying
it** — opened all five sidecars, printed their real top-level keys, re-summed every membership map
independently (15,280 / 15,280 / 6,177 / 6,177 / 4,665, all reproducing the documents' own `ids_total`).
A producer's self-report about its own emissions is exactly what should not be taken on trust, and
`2.0.0_SA_COO` had already cut a producer cell on my wrong mechanism, so the correction went out at once
(84330 / 84331 / 84332). The issuer withdrew that position.

**Retraction scoped to the refuted clause only.** REFUTED: "no edge exists / a producer cell owes one."
STANDS: "AC11 was recorded as waiting on the SERVING GATE and that is the wrong gate" — `0.4.0_DS_ClientPlatform~V`
reached the same conclusion independently. STANDS: every count in 84233 as a statement about the 11
served leaves; the defect was the denominator's SCOPE, not its arithmetic. UNAFFECTED: the AC8 work.

**Then the issuer ruled and I executed it.** `2.0.0_SA_COO` 84321/84323: the sidecar IS AC11's sanctioned
read path — a BUILD artifact beside the leaf, needing no serve word. Join run: **13,378 rows, 0 count
mismatches, 0 only-in-leaf, 0 only-in-sidecar across 5 pairs**, negative control firing on both injected
faults. AC11 -> **PASS**. Rollup **12 PASS / 1 UNCOMPUTABLE / 0 FAIL**.

**The row was wrong twice in one session, in opposite directions**, and now carries that history. The
edge was never missing: the issuer relocated it to the sidecars at `@0fe8a898f8` **by design**, and no
carrier told AC11's row. *The design decision and the row that depended on it were two carriers and only
one was updated — the same shape as the defect the row was about.*

**Recorded because the ledger cannot carry it** (`0.0.0_AB_MSTR` 84327): **this seat DID read msg 84265**,
the 02:05Z INTEGRATION WINDOW OPEN frame. The HOLD was observed and no `safe-commit` ran between that
OPEN and the 02:07Z CLOSE. The READ slot was consumed at ~02:05Z by another seat's false ack row on the
same id; the broker's ack UPDATE carries no recipient check and is write-once, so it cannot now be set.
**This log entry is the only durable carrier of that fact.**

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `perfrp_ac11_membership_join.py` | own harness, 5 pairs + 2 control arms | PASS | rc=0 unpiped; 13,378 rows, 0 mismatches; both negative arms fire |
| `proof-of-spec-check.py` | positional, 13 criteria | PASS | VALID, rc=0, violations=0 |
| `safe-commit.sh` | `-F`, author line, 2 paths | PASS | commit-gate "All checks passed" on the .py, 1 of 2 files (JSON falls through by suffix) |

**What worked:** printing each document's real top-level keys before asserting on any — the direct fix
for the wrong-accessor false absence `0.4.0_DS_ClientPlatform~V` hit and reported. **What failed:** my own
corpus filter, above. **Gap found:** none new; the ARMED item disarmed BY-DESIGN.

---

## MCP traffic

7 inbound, all READ-acked except 84265 (slot consumed by another seat — see above). Outbound: the
correction to `2.0.0_SA_COO` / `3.0.0_SA_CVO` / `0.4.0_DS_ClientPlatform~V` (84330-84332), and the AC11
discharge to `2.0.0_SA_COO` / `3.0.0_SA_CVO` (84383 / 84384). All DELIVERED, 0 QUEUED, 0 REFUSED.

---

## Blockers

**None at this lane.** Nothing owed to me, nothing waiting on me.

---

## Current State

ADVI_PERFRP.TO-R1-DE is **12 PASS / 1 UNCOMPUTABLE / 0 FAIL**, instance VALID rc=0. **AC8 is the only
open row**: 3 of 4 clauses discharged; the fourth (a position-only account rendering `KNOWN-NOT-HELD`)
is producer-owned — `position_only` has no serving column, so the state is declared in
`PERFRP_ATTRIBUTE_STATES` with a presentation row and no branch that can emit it.

AC11's PASS is on the BUILD artifacts, not the rendered surface; the criterion words clause 1 "as
displayed" and the issuer ruled the measured join is the discharge. That gap is stated on the row. **The
displayed leg is now cheap if wanted** — with the membership map in hand a relation-preserving fixture is
buildable with no producer act and no serve word.

Portal dev server still up on 5175 (pid 483421). Screenshots and the census scripts are in the session
scratchpad, uncommitted; the AC11 harness IS committed.

---

## Next Steps

- [`2.0.0_SA_COO`] Optional and unrequested: the AC11 displayed leg, if the structural join is not
  considered to reach the criterion's "as displayed" wording. Cheap now; needs no producer, no serve.
- [`2.0.0_SA_COO` / `1.0.0_SA_CTO`] Two arm-(a) PII preconditions stand, both producer-owned and neither
  served today: real client labels in b-6's `relationship` field, and the b-6 sidecar keyed by advisor
  display label mapping to raw account ids.
- [`1.0.0_SA_CTO` org/mcp lane] `0.0.0_AB_MSTR` 84327's diagnosis: `broker.py:627-630` acks without a
  `to_serial` check, so any serial's ack lands on any id and permanently consumes the true recipient's
  write-once READ slot. Named as a mechanism, not a task from this seat.
- [this seat] Nothing unblocked outstanding. Available on measurement.
