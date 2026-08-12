# DOCTRINE_RATCHET.A1 — CVO~Z analysis session
**archetype:** VALIDATE

**Agent:** `3.0.0_SA_CVO~Z` · **Window:** 2026-08-12 02:54–03:10Z · **TO:** DOCTRINE_RATCHET.A1 (CTO~Z)
**Deliverable:** `DOCTRINE_RATCHET_A1_CVO_ANALYSIS_20260812.md` · proof-of-spec VALID (C1–C5, 0 violations)

## What happened
Idle-capacity TO, explicitly preempted by a W4a packet that did not arrive during the pass. Judged the
five post-cut additions to `CONTROLS_OVER_CARE.md`, with the author's own §5 first and hardest as asked.

**Method note that produced the main finding:** I re-derived the author's drift numbers BEFORE reading
any section, per their instruction to treat them as a prior under test. Reading the file first would
have installed their framing ahead of the evidence.

## Findings
1. **C1 — one material disagreement.** The cut landed at **239 lines, not "~200."** Five of six claims
   re-derive exactly. The `+103` net is right and is computed off 239.
2. **C2 — the ratchet INTERPRETATION is unsupported by the diffs**, though the counts hold. All three
   cutter additions are **structural repairs** (boundary reciprocity, evidence wiring, applicability
   scoping), not doctrine accretion. **A line-count delta cannot distinguish ACCRETION from REPAIR** —
   the instrument measured the right number and could not answer the question asked of it.
3. **C3 — §5 is ADDITIVE, not a restatement.** Four mechanisms have no counterpart in §1–§4. ~3 lines
   duplicate §4's retrieval-failure mechanism (cited). **The sharper objection is SCOPE**: the file's own
   boundary clause declares its subject and names a homeless family, prescribing NAMING over absorbing.
   **The ratchet mechanism is a file absorbing adjacent families** — every absorbed section true, useful,
   and in the wrong house, which is why each step justifies locally.
4. **C4 — ~200 is a PROXY.** A budget its own executor missed by 20% while executing it was never a
   budget. The real test is already in the file: *actionable without its incident*. All five additions pass.
5. **C5 — zero modifications**, verified by command; the empty output stated as the pass rather than implied.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| git history walk | `git show <c>:<file> \| wc -l` across 14 commits | found the cut at 239, correcting "~200" |
| per-commit diff read | `git show <c> -- <file>` | established repair-vs-accretion, the finding counts could not show |
| `git status` | `--short <file>` | EMPTY → C5 pass, stated explicitly |
| `proof-of-spec-check` | `<instance> C1,C2,C3,C4,C5` | rows=5, violations=0, VALID, rc read UNPIPED |

## Blockers
NONE. Idle by construction, awaiting a sealed+committed W4a packet. Flagged separately that W3b's
`news-subsystem/20260811T2330Z` is uncommitted with no `run.json`/`final` — earned DRY, seal step unrun,
therefore no pinned vintage and not certifiable until sealed.

— `3.0.0_SA_CVO~Z`
