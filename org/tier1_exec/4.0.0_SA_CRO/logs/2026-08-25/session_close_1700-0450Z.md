# 4.0.0_SA_CRO — session close, 2026-08-24 ~17:00Z to 2026-08-25 ~04:50Z

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

Coordinator for six tier-2 seats (`~A`..`~F`) building an eight-week product program in the
`docs_abcdeg` planner, plus estate-side ontology work. Roughly twelve hours; this is the whole
window (last log 2026-08-21).

---

## What this session was

Andrew stood up six proposal seats and made me their coordinator. The window covers: five plans
delivered, a 41-call sovereign decision sheet compiled and ruled in one word, two external
adversarial review passes answered, four shared instruments built, and an independent certifier
spawned that withheld certification on three of them.

## MCP traffic

**~180 messages handled.** Significant dispatches only:

| Act | Detail |
|---|---|
| **41-call master sheet** | compiled from 5 of 5 seats (21 raw seat calls -> 19 distinct, +16 Proposal F, +1 held rec). Andrew: *"All recs approved"*. Broadcast 66761-66765, 5/5 DELIVERED. |
| **Ruling 4 HELD then RESOLVED** | held ~2h with the collision named; resolved as the execution-seam cut. |
| **Three spawns authorized** | estate build lane, cold certifier, `~F` (Andrew instantiated `~F`; I spawned the other two on his word at ~03:2xZ). |
| **~20 placements** | seam edges, schema conditions, vocabulary rulings. |
| **6 self-filed corrections against my own claims**, broadcast rather than silently patched. |

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-find` | locating estate artifacts, token censuses | PASS |
| `comp-kuzu` | node/edge `layer` distributions for the substrate migration | PASS — surfaced the two-axis defect |
| `git log -S` / `ls-files` / `check-ignore` | inbox-tree exposure census | PASS — **inverted a seat's finding** |
| `safe-commit.sh` | 6 commits, all gated | PASS |

**What worked:** `comp-kuzu` produced the measurement that falsified my own migration spec —
`edge.layer` (41,503 edges / 3 values) is not `node.layer` (20,779 nodes / 5 values).

**What failed:** my own predicates, repeatedly. A case-sensitive `grep` reported a placement as
unpropagated when it was in five artifacts. `ls --time-style=+...Z` printed **local** time with a
literal `Z`. A `git log -1` read another seat's commit as mine.

**Gap found:** no estate tool measures **placement absorption**. Built `propagation.py` for it.

## Files modified

See commit messages: `65c3977c66`, `9525a45b71`, `e68a5efd2b`, `5c93199eda`, `c2f4cfe7ba`,
`1670715c26`. Non-estate work (not committed — `docs_abcdeg` is the planner, not a repo):

| Artifact | State |
|---|---|
| `plan/MASTER_OPEN_CALLS_20260824.md` | 41 calls, ruled |
| `plan/OPEN_AT_ANDREW.md` | live decision queue, 11 items |
| `plan/shared/evidence_plane.py` | v0.9, 7 axes, 23/23 |
| `plan/shared/interface_edge.py` | v0.2, 12/12 |
| `plan/shared/propagation.py` | 9/9 |
| `plan/shared/publish.py` | atomic publication, 15/15 |
| `plan/shared/program_registry.py` | 32 deliverables, 7/7 |
| response docs to the external reviewer | 2, ~35 KB |

## Blockers

**None at this lane.** Nothing is waiting on me.

## Current State

**Six seats live and current.** Plans total ~1.26 MB across `plan/proposal_{a..f}/`. All seats
folded every placement; four bilateral edge reviews returned 3 AMEND / 1 RATIFY.

**Five shared instruments published atomically** with self-describing digests
(`sha256/lf:` + `sha256/raw:`), pointers in `plan/shared/_published/*.CURRENT.txt`.

⛔ **THE COLD CERTIFIER WITHHELD CERTIFICATION ON THREE OF FOUR.** 31 mutants, **14 survived
(45%)**; `program_registry.py` worst at 71%. 22 numbered disagreements. Two are stale (fixed
after its pin — it flagged that its subjects moved under it mid-run). **Its systemic finding:**

> *Each fix was verified by testing the case that motivated it, and the new mechanism itself went
> unmutated.*

In every artifact the surviving mutant is **the mechanism its own comments call most recently
fixed**. Live and unfixed at session close: the 7th axis has no validation coverage (mutant loop
covers 6 positions); `claim_limits` is cardinality-blind while `set_may_support` is not;
`EDGE_STATE` is a fused axis that blinds `unreviewed_coordinator_edges` at its two strongest
states; `gaps()` never surfaces **20 UNTESTED rows** (largest cohort) or `FAILED`; the registry
silently drops one live blocked edge; the digest de-truncation can regress silently.

**The estate build lane is still running** (C2 repair: `motif_family` 0 of 45).

**At Andrew:** milestone name · program start gate · demonstration estate · `AGENTS.md` path rule
· identity-namespace root · Q-A8 (product vs specification object — sets what "done" means for all
six seats).

## Next Steps

1. **[4.0.0_SA_CRO]** Fix the certifier's 20 live findings. Start with `program_registry.py`
   (71% survival) and the mutation-coverage gap that spans all four.
2. **[4.0.0_SA_CRO]** Correct D-1 in `publish.py` — my "four of four" claim was **three of four**,
   and the heuristic I froze into its docstring fails on its own subject.
3. **[0.0.0_AB_MSTR]** Six commits ride the next integration window; all reported LOCAL, none
   claimed as pushed.
4. **[Andrew]** The six decisions above. The certification lane has now paid for itself twice.

## One thing worth carrying

Twenty verification principles recorded at
`deliverables/VERIFICATION_PRINCIPLES_FROM_THE_20260824_SEAM_ROUND.md` (@`1670715c26`).
**Part I's defects were in seat plans. Part II's are almost all in what I built or placed** — and
the certifier then found 45% mutant survival in the instruments I built to catch exactly that.

**The seats reviewed each other rigorously all night and were right almost every time. The
reviewer nobody had was mine.**
