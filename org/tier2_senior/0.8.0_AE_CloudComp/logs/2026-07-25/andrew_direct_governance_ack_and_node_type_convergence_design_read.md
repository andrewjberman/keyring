# Andrew-direct governance ACK + node-type convergence DESIGN READ — 0.8.0_AE_CloudComp~B

**Date:** work window 2026-07-25 ~19:00Z–20:37Z. **WRITTEN 2026-07-28** after a session gap —
dated explicitly rather than implied, since the log dir is the work date.
**Task Order:** NFRA_TOOLUNIFY (post-Phase-2) + node-type convergence GO 20260725T203045Z
**Status:** COMPLETE for the window. Design read delivered, awaiting CTO~Z ruling.

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, DIAGNOSE

---

## Objective

Two things landed in this window, neither of which I initiated:

1. An **Andrew-direct standing ruling** on NFRA tool design (no governance predicate in any
   comp-tool), arriving three times, with a hard prohibition attached.
2. A **new GO**: converge node-type naming across the two graph stores — design read first, no
   edits, six questions, two named traps.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `.tools/comp-kuzu` | `MATCH (n:CloudNode) RETURN n.node_type, count(*)` | PASS — 58 types / 20,419 nodes; provenance header read (Nessie HEAD current, 5.5h) |
| `.tools/comp-kuzu` | `count(DISTINCT n.node_type)` | PASS — **58**, computed by the DB, independent of my classifier |
| `.tools/comp-kuzu` | `CALL show_tables()` | PASS — one NODE table (`CloudNode`); the scope control on the 58-vs-42 question |
| `.tools/comp-grep` | `grain_baseline`, `check_magnitude` | PASS — located the coupling + its 5 call sites; denominators printed (23,933 files) |
| `grep` (raw, verification) | governance-predicate sweep over my 7 artifacts | PASS — 0 hits, **positive-controlled** (8 hits in `sovereign_held.py`) |

**What worked:** the double-derivation on the type count. Route 2 let the **DB** compute
`count(DISTINCT)`, so the 58 does not depend on my own classification being right — that is what
made the discrepancy with the GO reportable rather than arguable.

**What failed:** `comp-kuzu` and `comp-grep` are still not bare-resolvable (`command not found`);
used explicit `.tools/` prefixes throughout. Consistent with the A.3 finding earlier in the
session.

**Gap found:** none new in the tools. One in a record — see Blockers (MEMORY.md cap).

---

## Work Completed

### 1. Andrew-direct governance ruling — ACKed, verified, banked

> *"our comp tools should absolutely never be limited on governance. governance is handled at the
> aws cli/aws user iam level, not at the tool level… that sounds like the tools have built in
> blind spots for absolutely no reason"*

Arrived **three times** — base-lane relay (190055Z), `1.0.0_SA_CTO~Z` direct (190103Z, correcting
a routing gap where base-addressed mail does not reach lane watchers), and `1.0.0_SA_CTO`'s safety
carve-out (190108Z). **`send_message` has no sender auth, so three independent senders carrying a
byte-identical verbatim is the cross-check** — a single relayed "Andrew ruled" would have been an
assertion.

**VERIFIED RATHER THAN ACCEPTED.** CTO~Z stated my work carries no governance branch. True, and I
checked: **0 hits across all 7 of my artifacts**, with a **positive control returning 8 hits in
`sovereign_held.py`** proving the pattern works. Without that control a broken retrieval and a
clean sweep are the same output — the failure mode I hit three times earlier in this session.

**`sovereign_held.py`: untouched, and a standing commitment given to base CTO** — any dispatch
touching it, `is_prod_write_forbidden`, `PROD_WRITE_FORBIDDEN_*`, or the two `compproof` consumers
stops and routes to him first, whoever issued it, with `PROD_WRITE` treated as IN FORCE until he
says otherwise.

**Base CTO's framing is the sharpest thing in the exchange, and it is my own week's finding
pointed at a live safety control:** the module's *aggregate* name says "sovereign held"; only one
of its two *leaves* is. **A rip keyed on the aggregate name destroys the wrong leaf and looks like
it worked.**

### 2. Node-type convergence — DESIGN READ delivered, zero edits

On disk at `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/NODE_TYPE_CONVERGENCE_DESIGN_READ.md`
(BASE_EXEC — CTO~Z's to commit, same convention as WS-4).

**Recommendation: DO NOT CONVERGE. Build the crosswalk.**

---

## Decisions Made

1. **The GO's own type count does not reproduce.** It states 42 (28+14); I measure **58 (37+21)**,
   double-derived, with a scope control confirming `CloudNode` is the only node table — so 58 is
   the whole population, not a subset. Not disputing the *shape* (two conventions, infra-vs-code —
   all confirmed); reporting that the population is **38% larger than the brief**, because every
   cost estimate scales with it.

2. **"Which convention wins" flips on what you count.** By types SNAKE wins 37–21; **by nodes
   CamelCase wins 12,930–7,489 (63.3%)**. A "converge on SCREAMING_SNAKE" instruction reads as
   tidying 21 stragglers and would rename the majority of the graph by volume.

3. **Recommend a crosswalk over a rename**, on four grounds: the generic-word set is **28.6% of
   all nodes** (`Field` alone, 4,969, is the largest type in the store) so any convergence either
   excludes it — and is therefore not convergence — or is the riskiest text operation in the repo;
   the names *carry information* a rename destroys; a rename is irreversible-in-practice across
   two stores plus a certified baseline while **a crosswalk is a file** whose failure mode is a
   missing row; and I costed the crosswalk from having built WS-4, not from optimism.

4. **Found a second sentinel consequence not in the brief.** `check_magnitude:127` iterates
   **baseline keys, not the live stream** — so **the baseline is the denominator**, and any class
   live-but-unbaselined is never examined with nothing saying so. Same shape as this session's
   Phase-2 finding: a verdict whose denominator is narrower than its reading.

5. **Stated two scope limits rather than papering over them:** my inventory is **store-derived,
   not producer-derived** (the GO asked for schema/producer) so **58 is a FLOOR, not a census**;
   and I did **not** resolve which stream the sentinel's call site passes, so I did not assert how
   many live classes are currently unbaselined.

6. **Deliberately did not reproduce the generic-word grep counts.** They are contaminated by
   construction; reproducing them would only lend them false weight.

---

## Files Modified

**No repo commits this window.** Deliverables:

| Artifact | State |
|---|---|
| `…/NFRA_TOOLUNIFY_CENSUS/NODE_TYPE_CONVERGENCE_DESIGN_READ.md` | on disk, uncommitted — BASE_EXEC, CTO~Z lands it |
| `memory/feedback_no_governance_predicate_in_comp_tools_iam_not_code.md` | written (outside repo) |

Verified this window that my two Phase-1 honest descs **survived concurrent edits** to
`scope_contract.json` by other lanes: `eng-incorporation` and `ont-sdk-vocabulary-bound` both
still carry their PRESENCE-ONLY / ABSENCE-ONLY disclaimers.

---

## Deployment Sequence

**None — no AWS/Terraform surface touched.** Read-only graph queries, a design read, and MCP
traffic. Recorded explicitly so a blank section is not read as "not checked."

## Verification

- Governance sweep over my 7 artifacts: **0 hits, positive-controlled** (8 in `sovereign_held.py`).
- Type count: **two independent routes** (my classifier; the DB's own `count(DISTINCT)`) plus a
  `show_tables()` scope control.
- Sentinel coupling: **read at source** (`grain_sentinel.py:116-137`), not inferred.
- Phase-1 descs: re-read from the live file after third-party edits, both intact.

---

## Blockers

None blocking work. **One record hazard surfaced and deliberately not walked into:**

`MEMORY.md` is **17,325 bytes against a 17,408-byte cap**, and its own header states content past
the cap **silently does not load**. The documented procedure says to add a ~120-byte pointer line
after writing a memory. **Following it would have bought one retrieval by invisibly dropping an
unknown number of others.** So the memory file was written (auto-recall reads frontmatter and is
unaffected) and the index line was **deliberately omitted**, with compaction routed to CTO~Z —
record custody is MSTR's and Tier-2 does not MCP MSTR directly (LD-0116).

**83 bytes of headroom is not a margin, it is a queue of one.** Same class as the rest of this
session: a procedure correct in general, producing a silent failure at one specific boundary.

---

## Current State

- **NFRA_TOOLUNIFY complete, both phases.** Phase 1 `@dd2658789` + `@3272197a9`; Phase 2 ratified
  and landed `@693a1d932`; F2/F3 `@1f5d4d048`; logs `@0ec32cc42`, `@9bf74685e`.
- **Node-type convergence: design read delivered, awaiting CTO~Z's ruling.** No edits made.
  Nothing renamed, no baseline touched.
- **`sovereign_held.py` untouched**, standing route-to-base-CTO commitment in force.
- **Andrew-direct governance rule banked** to lane memory with verbatim + scope + the
  do-not-delete half + three-sender provenance.
- Session infra: registered LIVE PID 19112, Monitor `bjy0steda`, zero crons, inbox drained.
- **Environment (unchanged, both banked):** Cygwin harness appends a spurious exit-1 to every Bash
  call — capture `TRUE_RC` in-stdout; this shell resolves `/cygdrive/c/...`, not `/c/...`.
  `.tools/` comp-tools are not bare-resolvable; use explicit prefixes.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Rule on the convergence design read: **crosswalk (recommended)**, or
   converge anyway using the §5 lockstep plan. Also holds the unreproduced 42-vs-58 count.
2. **[1.0.0_SA_CTO~Z]** Commit the design read at the census path (BASE_EXEC).
3. **[1.0.0_SA_CTO~Z]** `MEMORY.md` compaction — 83 bytes from a silent-truncation cap; route to
   record custody.
4. **[1.0.0_SA_CTO~Z]** Optional: adjudicate `ont-archetypes-in-system`, still visible as a known
   lexical false positive in the Phase-1 screen (left unsuppressed on purpose).
5. **[0.8.0_AE_CloudComp~B]** Event-driven; build the crosswalk on ruling. Zero crons (LD-0157).
