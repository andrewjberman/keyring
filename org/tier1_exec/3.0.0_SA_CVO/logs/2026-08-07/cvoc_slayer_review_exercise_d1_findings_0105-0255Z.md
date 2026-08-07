# 3.0.0_SA_CVO~C — S-layer spec review, first exercise, and two D1 declaration findings (0105-0255Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), DIAGNOSE, TRACE

**Lane:** `3.0.0_SA_CVO~C` — logged in the BASE folder; no `~C` agent folder exists (fresh lane).
**Window:** 2026-08-07 01:05Z (session start) -> 02:55Z. **Commits:** 9 authored + 2 automated
(audit-archive-invoker snapshot/baseline at startup A.2) = 11 under my author line, reconciled.

---

## Current State

**Engagement:** Andrew put `4.0.0_SA_CRO` (driving), `1.0.0_SA_CTO~D`, and me on one piece of work and
named me reviewer of CRO's SCRIPT I/O ONTOLOGY spec. **The engagement is CLOSED on all sides** — CRO's
disposition landed `@118fb1585` (RAVC step 4 closed), CTO~D's arch ruling + corrections landed
`@d430a55de`.

**OUTCOME: the proposed S-layer is DISSOLVED — not built, and correctly so.** Andrew's own question
("wouldn't that sit at D1 anyway? what is in D1?") falsified the framing all three seats were working
inside. Every capability the spec proposed across three revisions already exists on the ratified D1
rail; the layer required **zero new vocabulary**. The real gap is a **population** gap: field-grain
extraction exists for the React/portal substrate and has never been built for Python.

**My artifacts (all committed under `3.0.0_SA_CVO~C`):**
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_C_REVIEW_SCRIPT_IO_ONTOLOGY_SPEC_20260807.md`
  `@117190a3a` — the review. 2 P0, 3 P1, 2 P2, **1 P1 self-retracted (struck in place, not deleted)**.
- `.../CVO_C_EXERCISE_SLAYER_ENGINE_20260807.md` `@2df1a002a` — **the only exercised evidence any seat
  produced** in the engagement, plus the attack-point-4 portal correctness audit.
- `.../CVO_C_FINDING_D1_EDGEKIND_GUARD_DECLARATION_20260807.md` `@e5644d78b` — two ratified-declaration
  findings against the rule bank, both at census.

**Findings that OUTLIVE the dead spec** (CRO's disposition §8 carries five of mine):
1. **SDK coverage defect** — `Coverage` measures what was **DISPATCHED**, never what was **WANTED**.
   `comp_recognizer_sdk.py:304-308` filters an over-tier recognizer out of the dispatch set *before*
   `:243 recognize()` runs, so `attempted` never increments. A run where **no** recognizer could be
   dispatched is byte-identical to a run with nothing to find: `0/0/0`, invariant satisfied, green.
   **This is in the SDK, not the spec — it will bite whoever builds the Python population.**
2. **`folded` is two values wearing one name** — `folded_local` reachable at the LOWEST tier
   (`script_io_ast.py:60,82`), `folded_imported` unreachable at EVERY tier.
3. **Resolved tier is MODULE-grain, not VALUE-grain** — real (245 trees / 67 with resolved
   `local_imports` over `org/modules/graph`) but its 4 meta keys carry no values/symbols/bindings.
4. **Observer-relativity** (the unknown-unknown) — nothing records WHO measured a site at WHAT tier.
5. **Declaration discriminators** — mandatory-vs-optional, sharpened to **STAMPED-vs-UNSTAMPED**.

**Two D1 rule-bank findings, both CENSUS not sample:**
- `:321` `recompute_guarded` — *"props.condition carries the guard. LIVE: 482/961."* Count EXACT;
  **condition populated on 23/482 (4.8%)**. 14 distinct guards / 14 files. **COVERAGE defect, not
  correctness** — `condition` non-null on a non-recompute edge = 0, so where populated it is correct
  and exclusive. Surfaced by CTO~D, adjudicated here.
- `:330` `coverage_boundary` — *"77/961 FLOWS_TO carry no dstField."* **Measured 0/961: the gap has
  CLOSED.** Understates the estate; a reader would scope remediation that no longer exists.
- **Swept the class: it is a ONE-OFF.** Exactly 3 `LIVE: N` claims in the bank; all 3 counts exact,
  2 mechanisms hold at 100%, and `rename`'s own **advertised cross-check genuinely passes** (142==142).
  `PROP_PASSES` `forward` declaration verified TRUE (kind on 0 of 1382). **3 of 4 clear — the rail is
  precise and this RAISES confidence in it.**

**Material correction delivered pre-disposition:** CRO and CTO~D each measured the `via` locus at
**961/961 on FLOWS_TO** and concluded it universal. Census of `PROP_PASSES` (1382, the LARGER carrier
of the same `derives-from` relation per rule bank `:139`): **`via` on 0 of 1382.** Field-flow locus is
**961/2343 = 41%**, not 100%. Landed ~20 min before CRO's disposition shipped; both seats amended.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-kuzu` | `CALL show_tables()` | **PASS** | **Ground-the-class step.** Schema is TWO generic tables (`CloudNode`/`CloudEdge`), label is a PROPERTY (`edge_type`) |
| `comp-kuzu` | `MATCH ()-[r:READS_FIELD]->()` | **FAIL (correctly)** | `Binder exception: Table READS_FIELD does not exist` — my query shape was unbindable |
| `comp-kuzu` | `MATCH ... RETURN r.label` | **FAIL (correctly)** | `Cannot find property label` — property is `edge_type` |
| `comp-kuzu` | `CALL table_info('CloudEdge')` | **PASS** | 4 properties: `edge_type`, `layer`, `snapshot_ts`, `props`. No locus column — locus lives INSIDE `props` JSON |
| `comp-kuzu` | FLOWS_TO props census (961), PROP_PASSES props census (1382), edge_type denominators | **PASS** | Complete censuses, not samples. Provenance header read every call |
| `comp-grep`/native Grep | producer-side field-grain emitter census; rule-bank claim enumeration | **PASS** | Independent aperture — vintage-immune corroboration of CRO's portal-only zero |
| `safe-commit.sh` | 9 commits, `-F` message files | **PASS** | risk-reflex CLEAN on each (1 file vs 1659 danger nodes) |
| `to-check.py` | `--all --assignee 3.0.0_SA_CVO~C` | **PASS** | 0 active TOs |
| `audit-archive-invoker` | startup A.2 | **PASS** | rc=0, 0 findings, snapshot minted |
| **engine exercise** | `comp_recognizer_sdk.py` self-test; `gensdk smoke.py`; custom harness | **PASS** | 16/16 + 3/3 front-ends, true rc unpiped |

**What worked:** Running the positive control FIRST, every time. It caught me **four separate times** —
the `READS_FIELD` table, the `label` property, the `--author` filter returning 0 while 11 commits
existed, and `class Site` before trusting `class Binding = 0`. Every one would have produced a
confident wrong answer.

**What failed:** `comp-kuzu` served **STALE with a FAILED refresh** at 02:16Z (`wait-timeout-served-stale:
mutex wait 180s exceeded`), then rebuilt clean at 02:20Z. Reading the provenance header is what caught
it; a consumer that skipped the header would have quoted a superseded pin as current.

**Gap found:** **`git log --author="3.0.0_SA_CVO~C"` combined with `--since` returned 0 while 11
matching commits existed.** Without `--since` it returns 11 correctly. A log written off that zero would
have reported "no commits this session." Same class as the estate's `grep -c` and paginated-`length()`
hazards already in CLAUDE.md — **an author/date filter is a retrieval, and a retrieval failure returns
a VALUE.**

---

## MCP traffic

**~14 messages handled**, all acted on same-turn. Significant:
- **IN** CRO: review request (Andrew-directed) -> STOP-READ (SDK found) -> REV 2 -> reframe/attack-4 ->
  stand-down -> disposition closed. **IN** CTO~D: pairing terms -> §7 arch read -> arch ruling ->
  concessions x3 -> load-bearing query run.
- **OUT** ACKs (RAVC step 2, both seats) · review delivery + 3 amendments · exercise report ·
  attack-point-4 audit · D1 finding + sweep + F-5 · gate-candidate refinement to CTO~D.
- **RAVC:** CRO's Request ACKed 0109Z, delivered 0132Z, closed by CRO 0250Z.

---

## Blockers

**None at me.** Nothing is held behind me and I proposed no gate at any point — explicitly stated in
writing to both seats at the outset and honoured throughout (CLAUDE.md NEVER#6/#7).

---

## Next Steps

1. **[Andrew]** **Held-out fence scope** — the ADVI/MDPF fence vs the S-layer sequence. **My audit made
   it concrete: it is now a DIRECTORY-LISTING problem** — ADVI endpoints sort alphabetically FIRST in
   `portal/src/api/endpoints/`, so ANY systematic audit or validation of the portal template hits
   held-out surfaces **by construction**. "Validate portal then copy it for Python" and "do not touch
   ADVI_PERFORMANCE" conflict mechanically, not merely in principle. Cited in CRO's disposition as
   Andrew's call. **Self-disclosed my own corpus: I read one comment line at
   `advisor-intelligence.ts:833`; fence-clean figure supplied; finding unchanged.**
2. **[Andrew]** Two proposals from `1.0.0_SA_CTO~D`, correctly framed as his and NOT landed: the Build
   Ladder rung-2-applies-to-SCHEMA law call `@611f0e18b`, and a declaration-vs-population gate keyed on
   my discriminator. I have no verification objection to either; both are proposals, not gates.
3. **[whoever takes the Python-population build TO]** The **SDK coverage defect** is the item that
   outlives all three documents. Remedy: assert on a denominator the dispatch filter cannot shrink
   (`registered_for_artifact_class` vs `dispatched`, difference enumerated by
   `(recognizer, required_tier, served_tier)`). **Route the verification to me and I will EXERCISE it
   rather than read it.**
4. **[UNCLAIMED, stated so it does not quietly close]** `RENDERS` (2447), `READS_FIELD` (2110),
   `HAS_FIELD` (4269) are **UNSWEPT** for the declaration-vs-population gap. 95.2% is a FLOWS_TO
   figure; 41% is FLOWS_TO+PROP_PASSES; **neither is an estate figure.**
5. **[3.0.0_SA_CVO~C]** Available. Zero crons, zero TOs.

---

## Method notes worth keeping

- **A hand-chosen control measures the author.** I picked my own target file rather than reuse CRO's,
  systematically sampled the portal audit (first-per-file, alphabetical) rather than hand-pick, and ran
  a **negative control** (2 of 81 unrelated lines = 2.5%) — without which the 9-of-14 hit rate would
  have meant nothing.
- **I falsified a leg of my OWN P0-1 and reported it against myself, unprompted** (F-1a) — the
  tier-ladder mechanism I had adopted from CRO without testing. Conclusion stood; the leg was replaced
  with a measured one. **The harder discipline was not the fast retraction — it was re-testing evidence
  for a finding that had ALREADY BEEN ACCEPTED, because acceptance is when nobody is looking anymore.**
- **P1-5 retracted in 13 min**, re-verified at source rather than taking CTO~D's word, mechanism named
  (*a symbol-table comparison cannot distinguish a fork from a re-export — both produce identical
  symbols*), **struck into the review rather than deleted.**
- **Four failure shapes surfaced across the three seats in one session.** Three announced themselves
  (a grep pattern that could not match its counterexample; my symbol table; a falsified locus
  hypothesis) and each was caught by another seat within the hour. **The fourth had nothing to trip
  over** — a true count welded to a false mechanism claim, found only because reproducing the count
  exactly happened to be someone's positive control. CTO~D called that *luck with good posture, not a
  control*, and was right to. **The stamped-vs-unstamped predicate is the attempt to convert it into
  something keyable.**

— 3.0.0_SA_CVO~C
