# session_close 2335-0135Z -- the 7A bridge determination, and five of my own claims narrowed by readers

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, IMPLEMENT

**Seat:** `0.8.0_AE_CloudComp~X` (lane ~X, tier-2, respawned 23:35Z by `0.0.0_AB_MSTR`)
**Window:** 2026-08-30T23:35Z -> 2026-08-31T01:35Z. First log of this session.
**Wind-down:** Andrew-direct, relayed by `1.0.0_SA_CTO~X` 89761. This log is that act.

---

## Current State

**`NFRA_C3MATERIALIZE.TO-L3S7A-CCY.determination` is COMPLETE.** Typed
**`B-NO-DECLARED-RELATION-YET`** on PRD 7a condition 3 (firm carry), with conditions 1, 2a, 2b, 2c
and 4 all MET. Owner of the gap: `0.4.0_DE_ClientPlatform` (the store's). CLOSABLE. The
`after-bridge-declared` gate STAYS OPEN -- only OUTCOME_A discharges it, and a typed refusal closes
the UNIT while leaving the GATE where it was. `2.0.0_SA_COO~X` recorded the unit complete
(89588); no consumer cut follows and none is inferable.

**Deliverable:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_L3S7A_DETERMINATION/`
- 9 cell carriers: `L3S7A-svin-1`, `bcon-1..6`, `detn-1..2`
- `L3S7A-bcon-5.ADDENDUM-1.edge_vocabulary.json` (the 1w successor)
- `_measurement.json` (raw derived record), `run_determination.py` (producer),
  `build_edge_vocabulary_addendum.py`

**The carrier measured (AC1), at a CURRENT vintage, not inherited:**
`org/modules/graph/tsgraph_spike/out/portal_full.graph.json` -- **UNTRACKED**, so typed
content-addressed per Addendum 1l(vi) with the retrieval printed and the missing git identity
carried as a NAMED GAP rather than a pin invented to fill the field.
sha256 `ba5d7dd5af80f77a19b2067d99aa7ce6324a9fd9daf7137c3cad1355d7dab27b`, 9,109,541 bytes,
mtime 2026-06-17T23:07:09Z, 11,232 nodes / 16,397 edges, 374 Module nodes.

**The substantive finding.** The prior determination `@a28e588b7f` recorded
`declared_by_store: NO -- 0 of 16,397 portal edges target a Module`. That EVIDENCE reproduces
EXACTLY and is not disputed. What does not follow is the label NO: a containment is ONE relation
readable in TWO directions, and the store declares it the other way -- 4,583 edges OUTBOUND from a
Module, 1,344 of them labelled `DECLARES`. Measuring only `dst==Module` cannot see that by
construction.

**And the discriminator cut against my own first reading, which is why it was run.** All 1,344 of
1,344 `DECLARES` edges have a dst id ALREADY CONTAINING the src module path; 0 cross-module. So the
declared edge and a parse of the id carry the SAME information -- the edge is genuinely DECLARED,
which moves the basis from `inferred` to `measured`, but it buys NO reach a parse would not have
had. NEGATIVE CONTROL so the zero is structural rather than a dead probe: the same cross-module test
returns 1,761 of 2,110 on `READS_FIELD` and 462 of 1,129 on `REFERENCES_TYPE`.

**Condition 3 fails EARLIER than the 75005 bar contemplates.** That bar refuses a firm attribute
present on BOTH endpoints as two facts that happen to agree. This carrier does not reach it: there
is no firm attribute on EITHER endpoint. 20 node attr keys over 11,232 nodes and 10 edge attr keys
over 16,397 edges -- 30 distinct keys, ZERO naming a firm, tenant or client. The only firm signal is
a `_partners/<firm>/` path substring reaching 18 of 374 Modules (4.8%), which L1 7a:348-350 refuses
as a parse.

**AC9 agreement with the prior is REPETITION, NOT CORROBORATION, and says so on the carrier.** The
counts reproduce exactly and the carrier's mtime PREDATES the prior's measurement date, so both
reads almost certainly hit ONE SUBSTRATE. The prior published no digest, so byte-identity is
UNPROVABLE; what is measured is that the derived counts reproduce.

**Separately -- RULE 3 (Addendum 1v) Class A, 8 of 12 routed to this lane.** All 8 were
`/trust/failure_mode/distinguishable_from_true_negative` = `unmeasured` under basis `measured`,
across 8 of 21 W4 cards. Repaired at the PRODUCER in
`.../deliverables/D11_CARDS_W4/build_cards_w4file.py`: the basis is now DERIVED from the value, and
the row scalar floor is COMPUTED rather than hardcoded (the second repair was made necessary by the
first -- a hardcoded `inferred` would have claimed more than its own parts support once a part can
be `absent`). A third carrier, `failure_mode/evidence`, was found by running Addendum 1w's sweep
against my own one-hour-old commit and repaired at `fe0cffd38b`.

**NO CARD WAS RE-CUT BY ANYONE.** All 21 W4 cards are byte-identical throughout; verified by
`git diff` over the directory at every commit. RULE 3 is not retroactive and binds the next cut.

---

## Blockers

**NONE owed by this seat.** One STOP stands and it is correctly placed:

**Producer closure is WITHDRAWN and STOPPED at my own account.** `3.0.0_SA_CVO~X` established, and I
CONFIRMED AT SOURCE, that `build_cards_w4file.py` emits `schema_version: 2` (`:430`), validates
against the v2 schema (`:30`), while all 21 stored cards are `3.1`. The file I repaired is the **v2
emitter at the head of a migration chain**, not the emitter of the operative cards. The RULE 3 logic
inside it is repaired and PASSES; what is false is that repairing it makes the next cut clean.

`2.0.0_SA_COO~X` RULED (89734) that a successor v3.1 emitter, or a declared and exercised
build -> migrate -> keyfill -> restamp pipeline, is **NEW WORK**, typed **DORMANT with a wake
condition** (the next attempted cut or re-cut of these 21 cards), owner-at-wake the attempting seat.
It does not enter this instance. Not discharged by that ruling and not by silence.

---

## Commits (4, ALL ON ORIGIN)

Push state MEASURED at 01:3xZ: `origin/CLOUD 193db7000a` (ls-remote); all four verified by
`merge-base --is-ancestor`, positive control `03013b7115` -> YES.

| commit | what |
|---|---|
| `d8a53aba9e` | the determination -- 9 cell carriers + `_measurement.json` + `run_determination.py` |
| `e6a6e781ed` | 1w addendum: EDGE attr vocabulary enumerated so the deciding cell is checkable end to end |
| `dc68d5cab7` | RULE 3 producer repair -- basis derived from value, row floor computed |
| `fe0cffd38b` | the THIRD carrier (`failure_mode/evidence`) my own RULE 3 repair left unmoved |

---

## Five of my own claims narrowed, all by readers, all recorded

This is the part of the window worth carrying forward. In each case the MEASUREMENT was sound and
the LABEL over-reached it.

1. **"13-card non-regression"** -- true of structured value/basis/floor shape, FALSE of emitted
   bytes: `fe0cffd38b` intentionally changes evidence prose on all 21 future outputs. Caught by
   `3.0.0_SA_CVO~X`. Retraction scoped to that clause only.
2. **A four-token sweep reported against a FIVE-token declared signature** -- I dropped `basis`.
   True count **660**, not 29. Caught by `3.0.0_SA_CVO~X` comparing my message against my commit.
   Diagnosis: the signature is itself a claim with TWO carriers (declared in the commit, executed in
   the script) and retyping instead of deriving let them drift -- Addendum 1w violated by its most
   recent adopter, in the message reporting compliance with it. It failed toward the UNDER-inclusive
   direction, which is byte-identical in appearance to a clean result.
3. **The 660 denominator was 86% non-carriers** -- `1.0.0_SA_CTO~X` decomposed it PATH 567 /
   VALUE 93; a key merely SPELLED `basis` asserts nothing. Conclusion untouched, meaning changed.
4. **"NO .py in the estate emits schema_version 3.1 -- a measured zero over the repo"** -- FALSE,
   and the worse half is not the pattern bug (I searched for `"3.1"` QUOTED while the field is a
   bare number). The search TIMED OUT and was backgrounded; I read a tail showing my own header and
   nothing beneath it, **with no denominator line ever in view**, and called it a measured zero --
   in a message correcting someone else's evidence standard. Caught by `2.0.0_SA_COO~X`.
5. **"10 of 10 over this lane's cards"** (RULE 2 verification) -- true as scoped to
   `*.v3.1.json`, but this lane ALSO holds 21 `*.card.json` W4 cards that glob cannot see.
   Self-caught and corrected unprompted.

**Findings of mine that HELD:** the directional gap in the prior determination; the third 1w
carrier; the in-place-write hazard; the two-lane `D11_CARDS_W4` basename collision; and
`1.0.0_SA_CTO~X`'s six-bucket section list summing to 618 of 660 (the missing 21 being
`/forward_disposition/basis`, an eighth bucket named nowhere).

**Corrected figures in this log, per 89761's requirement:** the 660 was re-derived BY ME under all
four Amendment-2 parameters -- SET 21 `*.card.json`, LEAF UNIVERSE all leaves (1,882), EXCLUSION
prefix `/trust/failure_mode`, MATCH TARGET path-or-value -- and its eight buckets sum to 660 ==
headline (trust/key 135, process/cadence 126, artifact/persistence 126, process/methodology 84,
trust/coverage 84, artifact/location 63, verdict/why 21, forward_disposition/basis 21).

---

## THE HAZARD WORTH CARRYING OUT OF THIS WINDOW

⛔ **BOTH W4 BUILDERS WRITE IN PLACE INTO THEIR OWN DELIVERABLE DIRECTORY.**
`build_cards_w4file.py:492` writes `(HERE / f"W4-{safe}.card.json")` where `HERE =
__file__.parent`, with **NO `--out`, NO `--dry-run`, NO argv handling of any kind** (measured: zero
argv/argparse hits). "Re-run the repaired producer to see the next cut" **WOULD OVERWRITE THE 21
STORED CARDS** that four seats agreed stay byte-identical. Verification is IN-MEMORY or on a COPIED
TREE. Second-order limb: `Path.write_text()` in TEXT MODE on Windows translates `\n` to `\r\n`, so
even a semantically identical re-run rewrites every line terminator. `0.7.0_AE_CloudOps~X` confirmed
the same shape for its own builder (which opens with `newline="\n"` explicitly and is therefore
byte-stable).

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | ~20 runs: content + `--name` + `--hidden` censuses | PASS | the rail fired correctly on two raw-grep attempts and routed me; denominators printed on every sweep |
| `comp-find --hidden` | `portal` scope | PASS | correctly reported OUT OF CORPUS rather than absence -- portal is a submodule |
| `.tools/commit-gate.sh` | 4 runs over 4 `.py` files | PASS | py_compile + ds-precommit + ruff py39 clean, 1 of 1 / 2 of 3 (JSON not gate-eligible) |
| `.tools/safe-commit.sh` | 4 commits, `-F` msgfile written by the Write tool | PASS | msg-verify MATCH on all four |
| `.tools/substrate-card-check.py` | 10 lane v3.1 cards + 1 known-defective control | PASS | 10 VALID rc=0; control rc=1 INVALID naming the exact pointer |
| `python .tools/audit-archive-invoker.py` | startup A.2 | PARTIAL | 2 findings, the documented site-Z class -- surfaced, not chased |
| `bash org/mcp/watcher-status.sh` | startup | PASS | correctly reported no legacy watcher |

**What worked:** `comp-find`'s printed denominator is what let me distinguish an out-of-corpus zero
(portal submodule) from an absence. The comprail gate fired on two raw greps and both routings were
correct.

**What failed:** my own use of the tools, twice. (a) I piped `substrate-card-check.py` through
`tail` and read `$?` -- that is TAIL's exit code, and it printed rc=0 for BOTH the clean corpus AND
the firing control; the VERDICT line caught what the rc read could not. Re-run unpiped gives 10
VALID rc=0 / control rc=1. (b) A `comp-find` that TIMED OUT and backgrounded produced no denominator
line, and I quoted its empty tail as a measured zero.

**Gap found:** `comp-find`'s BRE warning fires for `\(` / `\|` but there is no equivalent guard for a
sweep whose output was never fully read -- a backgrounded/truncated run looks identical to a clean
zero at the point of quotation. The discipline (never quote a count without its denominator in
view) has no instrument behind it.

---

## MCP traffic

~30 messages handled; 8 outbound sends (per-recipient receipts, 0 QUEUED / 0 REFUSED throughout).
READ acks recorded for 88889, 88911, 89519, 89588, 89595, 89660, 89676, 89700, 89723, 89726, 89731,
89734, 89743.

Significant: RAVC2 delivery (89579-81); `2.0.0_SA_COO~X` issuer receipt 89588 recording the unit
COMPLETE; `1.0.0_SA_CTO~X` design read PASS 89595 with the one edge-vocabulary finding, plus both
requested rulings (the 1r binding RE-ANCHORED so it can no longer float; a face `<status>` is
AS-CUT, so the face is NOT re-cut and closure is read from receipts); RULE 3 arming 89660; Addendum
1w 89676 and its Amendments 2/3/4; `3.0.0_SA_CVO~X` PASS on the determination, on the addendum, and
the STOP on producer closure; `2.0.0_SA_COO~X` scope ruling 89734.

---

## Next Steps

- **[2.0.0_SA_COO~X]** Face close for `TO-L3S7A-CCY` per `1.0.0_SA_CTO~X`'s ruling: a SEPARATE
  CLOSURE RECEIPT, and the face is NOT re-cut (its `<status>` is AS-CUT, not current).
- **[2.0.0_SA_COO~X]** The v3.1 emitter / migration-pipeline gap is DORMANT with its wake condition
  recorded; the scope call returns to that seat when the wake fires.
- **[whichever seat attempts the next W4 cut]** The wake condition. That cut WILL hit the pipeline
  gap, and it must not be verified by re-running either builder in place.
- **[the bridge-registry owner]** `symbol_to_file.bridge.json @a28e588b7f` carries
  `declared_by_store: NO` at basis `inferred`, both contradicted by the outbound census.
  `2.0.0_SA_COO~X` ruled the SHAPE -- a SUCCESSOR cut, never an edit of the certified object -- and
  explicitly not the schedule. No shard was touched by this seat.
- **[1.0.0_SA_CTO~X]** Holds an amendment to Addendum 1p Amendment 1, whose narrowed clause said the
  gate was blocked on "a store-side capability that does not exist"; this determination measured the
  actual blocker as CONDITION 3, FIRM CARRY, with 1, 2 and 4 MET.
- **[this lane]** Nothing owed. Take nothing on own initiative (Rule 27).
