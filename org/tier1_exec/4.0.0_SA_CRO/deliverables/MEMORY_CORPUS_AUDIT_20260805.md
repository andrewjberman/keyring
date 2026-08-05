# The agent-memory corpus — audit

**Author:** `4.0.0_SA_CRO`, 2026-08-05, Andrew-direct (*"now do the memory/ audit"*).
**Subject:** `~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/`
**Prior belief under test, Andrew's:** *"i suspect that is a deprecated/unused temp folder."*

> ## VERDICT: NOT DEPRECATED, NOT A TEMP FOLDER, AND STRUCTURALLY HEALTHY.
> **1,012 markdown files · 5.8 MB · 1,007 of 1,010 with a valid recall surface.** It is a live,
> well-formed corpus that is read on every session.
> **The defect is not rot. It is that the corpus is UNVERSIONED and UNWIRED.**

---

## 1. Composition — measured, not sampled

| | |
|---|---|
| files (depth 1, `*.md`) | **1,012** |
| subdirectories | **0** — entirely flat |
| total size | **5.8 MB** |
| non-`.md` | 2 (`.bak-20260625T144844Z`, `.bak-20260731T205755Z`) |

**By declared type** (denominator = 1,010, excluding the two index files):

| type | n |
|---|---|
| `feedback` | **659** |
| `project` | 177 |
| `reference` | 170 |
| `user` | 1 |

**By mtime month:** 03→18 · 04→84 · 05→291 · 06→249 · 07→**350** · 08→20 *(5 days elapsed)*.
Growth is steady, not abandoned.

## 2. The retrieval surface is HEALTHY — this is the finding that kills "deprecated"

Auto-recall matches on frontmatter `description`, so **frontmatter validity is the real liveness
axis** — not index linkage, and not mtime. Measured across all 1,010:

| check | failures |
|---|---|
| no frontmatter at all | **2** — `feedback_f6_vintage_anchor_s3_not_local_ls.md`, `thread-system.md` |
| frontmatter present, no `name:` | 0 |
| no `description:` | **1** — `feedback_smoking_gun_field_shape_sanity.md` |
| `description:` present but empty | 0 |
| no `metadata.type` | 1 |

**99.7% of the corpus is recall-addressable.** Three files to repair, total.

**And it is loaded, not merely stored:** `MEMORY.md` is injected into every agent's context at session
start — it is in mine right now. **`MEMORY.md` is 10,764 bytes against the stated 17,408-byte cap
(6,644 bytes of headroom), so the cap warning it carries is real but NOT CURRENTLY BITING.**

## 3. ⛔ FINDING 1 — 5.8 MB OF GOVERNANCE KNOWLEDGE WITH NO VERSION CONTROL

**`memory/` is not inside any git repository.** `git rev-parse --show-toplevel` from it fails.

Consequences, none of them hypothetical:
- **No history.** A memory file that is edited or deleted leaves no trace and cannot be recovered.
- **No diff, no blame.** *"When did this rule change, and who changed it?"* is unanswerable.
- **No revert.** The estate's entire rollback posture — *every deletion is a commit, rollback is
  `git revert`* — does not apply here.
- **The backup strategy is two `.bak` files, 5 weeks apart.**

This corpus carries Andrew-direct verbatims, standing prohibitions, and the grounded evidence behind
CLAUDE.md rules. **CLAUDE.md itself cites `memory/` paths 10 times** — so *law depends on artifacts
that have no history.* That is the same class as the gitignored `comp-tool-runs.jsonl` already flagged
in `org/XXX.md`, at ~1,000× the content.

**This is the highest-value fix in the audit and it is cheap.**

## 4. ⛔ FINDING 2 — THE TWO CORPORA ARE UNWIRED, AND THEY ARE COMPLEMENTS, NOT DUPLICATES

I went in expecting duplication with the doctrine we consolidated today. **That expectation was
wrong, and reading the files is what corrected it.**

| | |
|---|---|
| `docs/doctrine/*.md` → `memory/` citations | **0**, across all 11 files |
| the 5 reference files I created today → `memory/` | **0** |
| `memory/*.md` → `docs/doctrine` | **4 of 1,010** |
| CLAUDE.md → `memory/` | 10 |

A keyword scan put **149 of 1,010** files in the verification-doctrine topic space *(a FLOOR — keyword
scans under-reach, per `VL#12`)*. But reading them inverts the conclusion:

> **`VL#2` — "an injected column is a HYPOTHESIS" — is TWO LINES in doctrine.
> `memory/feedback_an_injected_column_is_a_hypothesis` is 52 lines with three measured phantoms
> (`732` vs a true 164; `21` vs a true 0; a rigged proven-RED), the mechanism, four corollaries, and a
> four-step test.**

**Doctrine holds the law; memory holds the grounded incident.** That is *exactly* the split Andrew
ordered for `docs/` today — and memory already implements it, by accident, with nothing connecting the
two halves. **The remedy is wiring, not deletion. Nothing here should be deleted.**

## 5. ⛔ FINDING 3 — I MADE IT WORSE TODAY, AND THIS IS THE ONE I OWN

The pre-merge `VERIFICATION_LAW.md` carried **four** `memory/` citations (`VL#8`, `VL#11`, `VL#12`,
`VL#13`) plus a header explaining that `memory/<slug>` roots at the memory directory.

**My merge dropped all four.** They were **the only doctrine→memory links in the entire directory**,
which is why the count in §4 is zero rather than four.

> **Consolidating a document and silently severing its evidence is `M4` copy-drift committed by the
> merge that was fixing `M4`.** The law text survived; its grounding did not — and a law whose evidence
> is unreachable is the bare-prohibition failure mode CTO warned me about at 1615Z, produced by the
> edit that was preserving their mechanisms.

**REPAIRED this session:** all four restored, plus two new ones (`VL#2`, `VL#3`) where I verified rich
memory evidence exists. `MECHANISM_LAWS.md` now carries **8** `memory/` references and a header
explaining the root path.

## 6. Index hygiene — real but minor

| | |
|---|---|
| linked from `MEMORY.md` | 36 |
| linked from `MEMORY_FULL.md` | 872 |
| **union indexed** | **906 of 1,012** |
| **ORPHANS** (present, unindexed) | **114** — recall-reachable, browse-unreachable |
| **DANGLING** (indexed, file absent) | **9** |

The 9 dangling rows, in full:
`feedback-andrew-product-invariant-overrides-sequenced-gates` ·
`feedback-anticipatory-patience-discipline` · `feedback-cto-reversal-requires-new-empirical` ·
`feedback-empirical-state-supersedes-directive` · `feedback-loop-directive-reading-divergence-respect` ·
`feedback-verify-hold-attestation-before-propagating` · `feedback_eastern_time_only` ·
`feedback_serving_provenance_narrative_drifts_from_data` ·
`project_find_insure_no_firm_match_precision_not_recall`

**Severity is low** because the index is a *browse* convenience and auto-recall does not use it — but
`feedback_eastern_time_only` is a live standing rule (CLAUDE.md: *times to Andrew, US Eastern only*)
whose index row points at nothing. **A dangling row on a live rule reads as "the rule was retired."**

## 7. Recommendations, in value order

1. **PUT IT IN GIT.** One-time, cheap, and it converts an unrecoverable corpus into a recoverable one.
   Either a dedicated repo or a tracked path in this one with the harness pointed at it. **This is the
   only finding with unbounded downside if left.**
2. **WIRE THE TWO CORPORA, BOTH DIRECTIONS.** Every doctrine law that has grounded memory evidence
   cites it (6 done, more available); memory files carrying a law point at its canonical doctrine home.
   *The two halves already exist and were built for each other.*
3. **Repair the 3 frontmatter defects and the 9 dangling rows.** Under an hour, and it removes the only
   cases where the corpus lies about itself.
4. **Do NOT prune on age or count.** 1,012 files is not a problem when 99.7% are recall-addressable and
   nothing is loaded eagerly except a 10.7 KB index. **The cost of this corpus is nearly zero and its
   grounded incident records are irreplaceable** — they are the evidence layer the doctrine spent today
   trying to build, already written.

## 8. What I did NOT measure — stated so nobody reads this as complete

- **Recall efficacy.** I measured that files are *addressable*, not that the right one *surfaces* for a
  given query. That needs instrumentation of actual recall events, which I have no access to.
- **Content staleness.** I read 3 files closely and sampled headers. **I did not assess whether the
  1,010 are still TRUE.** A recall-addressable file asserting a retracted rule is worse than an orphan,
  and I cannot tell you how many of those exist.
- **Semantic duplication within memory.** 659 `feedback` files certainly contain internal restatement;
  I measured overlap with *doctrine*, not within the corpus.
