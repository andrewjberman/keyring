# NFRA_COMPASSURANCE — PRD-request brief

**From:** 3.0.0_SA_CVO · **To:** 1.0.0_SA_CTO (PRD author) · CC 2.0.0_SA_COO, 0.0.0_AB_MSTR
**Date:** 2026-07-10 · **Origin:** Andrew-direct — *"turn it into a brief and issue to CTO so they can make a new PRD and project NFRA_COMPASSURANCE."*
**Status:** BRIEF, not a PRD. I frame the problem and the evidence; **CTO authors the architecture.** I do not resolve the design and I will not — so that I can adversarially certify it later. *(A verifier who drafts the architecture he will certify has destroyed the only thing he was for — your line, on NFRA_TELEMETRY. Same discipline here.)*

---

## 1. THE SENTENCE

> **The directory-scoped graph-compiler tools (the scanners) generalize. The layer that tells you a scanner is
> WIRED, CATALOGUED, TESTED, and TRUTHFULLY-DESCRIBED does not exist — and it is missing uniformly across all 60.**
> NFRA_COMPASSURANCE builds that assurance layer as a standing, per-tool harness. It is the productization of the
> NFRA_TOOLCHECK.P4 manual audit, keyed on the RAIL_SET the audit produced.

## 2. THE EVIDENCE (tonight, exercised, grounded — not asserted)

- **The scan logic works when exercised.** `check_cross_firm_bucket_refs` (`ds-precommit-check.py:580`) blocks a
  cross-firm bucket reference at commit and I exercised it — positive control BLOCKS, negative passes. `comp-iam`
  post-fix (`6f3751a34`/`2119e91af`, CVO-certified scoped) answered a sovereign firm-separation question our own
  `grep` structurally could not. **When a directory-scoped scanner is run, it earns its keep.**
- **Every failure clustered OFF the scan, in the assurance layer:**
  - **WIRING:** `comp-surface-check` is CORRECT (rc=2/CRITICAL on 3/3 SEV1 files, rc=0 on 2/2 clean; exercised) and
    is **invoked at no point in the portal lifecycle** — not commit, not push, not CI. The SEV1 gate on client
    numbers is a manual convention. 17 commits touched those surfaces since 06-01.
  - **CATALOGUE:** the universe is **60 on disk / 63 by the is-a-tool predicate; ~42 in the mandated catalog.**
    CLAUDE.md still says *"~30 tools."* `comp-which`/`comp-grep`/`comp-glob` are absent from `tools_index` — the
    router does not index the router. **The count minted in prose is half the territory, with no control catching it.**
  - **TEST:** **32 of 60 have no test file anywhere that names them (53%)** — including `comp-surface-check`,
    `comp-firmsep-sweep`, `comp-tagauthz`, `comp-secrets`, `comp-tool-health`. Measured with a positive/negative/trap
    control on the recorder.
  - **RULE-vs-SCAN drift:** NEVER#1 asserts `bd↔cot↔inf` firm separation; the commit gate covers `bd↔cot` only
    (inf leg exercised, NOT BLOCKED). NEVER#3 asserts three prohibitions; one is gated, two are conventions.
    NEVER#7 asserts a gate; the banned op (`git pull --rebase`) executed ungated in both shells (exercised, HEAD
    rewritten in a scratch repo). **The rule promises what the code does not enforce.**
- **The framework side is further along than the P4 status suggests:** the recognizer SDK is BUILT for four artifact
  classes (`comp_recognizers_{code,config,ticket,tsx}.py`) per NFRA_COMPILERKIT. **The scanners are not the gap.**

## 3. THE THESIS + THE DECOMPOSITION ("comp-ladder")

**Thesis:** a scanner is not done when it RUNS; it is done when every rung of a two-dimensional matrix has a green
negative-control.

- **Vertical axis (pipeline layers, from NFRA_COMPILERKIT):** `front-end parse → semantic enrichment → recognizers
  → C0 primitives → C1 edges → CSE emission`.
- **Horizontal axis (failure modes, from RAIL_SET_canonical_20260710):** R1 NEGATIVE · R2 VARIANCE (per-limb / per
  code-path) · R3 NULL · R4 INVOCATION · R5 DISCLOSURE · R6 IDENTIFIABILITY · R7 DISCLOSURE-OF-OBSERVATION.

**The "ladder" Andrew named is the matrix: (layer × rail) per tool.** Today it is almost entirely empty, which is
exactly why "do the tools work" currently has no answer for most of the 60. NFRA_COMPASSURANCE fills the matrix.

## 4. WHAT NFRA_COMPASSURANCE SHOULD DELIVER (scope frame — CTO refines)

1. **A per-tool assurance harness** that, for each of the 63, answers with an EXERCISED control (not a config read):
   is it INVOKED where it claims to guard (R4); does a KNOWN-bad input make it say NO (R1); is its recorder shown to
   emit a one THROUGH THE BRANCH UNDER TEST (R2/per-limb); does it disclose what it skipped (R5) and what it
   observed (R7); can its result be re-derived independently of itself (R6).
2. **A wiring registry** — every tool → the gate/hook/CI step that invokes it, or `UNWIRED` loud. (comp-surface-check
   is the founding case: correct + unwired = worse than broken, because its truthful OKs read as a live control.)
3. **A rule↔scan conformance check** — every NEVER/Deployment rule that names a gate → the exercised proof the gate
   covers what the rule asserts, or `CONVENTION` loud. (NEVER#1/#3/#7 are the founding cases.)
4. **Catalog reconciliation as a standing gate** — the AC-0 predicate (`RAIL_SET`/`comp-tool-universe.md`, universe
   63) run continuously, so the count can never drift from disk again. Correct CLAUDE.md's "~30" to 63 as AC-1.
5. **The negative-control-generation method as doctrine** — R1's control must be GENERATED (mutation / fault
   injection), never hand-chosen; a hand-chosen control measures the author, a generated one measures the
   instrument. `0.8.0`'s mutation-tested `comp-iam` is the reference implementation of ONE tool passing the matrix.

## 5. DECISIONS CTO MUST RESOLVE (I frame; I do not resolve)

- **Relationship to NFRA_TOOLCHECK.P4:** is COMPASSURANCE the *productization* of P4 (P4 = the manual reference
  audit, COMPASSURANCE = the standing harness), or does P4 fold INTO it? My read: P4 stays as the reference pass;
  COMPASSURANCE generalizes it. **Your ruling.**
- **Relationship to NFRA_COMPILERKIT:** COMPILERKIT builds scanners (recognizers); COMPASSURANCE assures them. Clean
  seam, or shared substrate? **Your ruling.**
- **Where the matrix lives** — a new artifact, or columns on the AC-0 predicate JSON (COO already owns the
  R4a/b/c INVOKED column + R5 disclosure flag on the 63-row predicate). **Do not mint a second home for it** (the
  night's lesson: two homes for one fact drift).
- **Enforcement vs report:** does a red matrix cell BLOCK (a tool with no R1 control cannot be cited as GREEN), or
  only report? This is the F-004 question one level up.
- **The 63rd-tool problem — who owns an E4 tool's assurance?** An E4 tool (safe-commit, owned-paths, deploy_ledger)
  may not be verified through itself (COO ruling). The harness must exercise out-of-band.

## 6. WHAT I WILL NOT DO, AND WHAT I WILL

- **I will NOT author the PRD, design the harness, or resolve §5.** That is yours. I hand you the decision frame.
- **I WILL adversarially review your draft** and, when it ships, **certify each tool's matrix at a stated vintage**
  — the same do-er/verifier split that certified `comp-iam` tonight. The rail set is my instrument; I keep it
  independent of the architecture it will grade.

## 7. SUGGESTED ACCEPTANCE SHAPE (AC-7 pattern — CTO adopts or replaces)

> Run the OLD "the tool ran, exit 0, log is clean" assurance against any tool in the suite. IT MUST PASS. The
> COMPASSURANCE harness must then REJECT that as vacuous — because a tool that has only ever printed one value, wired
> to nothing, tested by nothing, is not assured. **If COMPASSURANCE ships and `comp-surface-check` still reads
> ASSURED while invoked by no gate, nothing was built.**

## Grounding

All §2 claims are committed CVO logs of 2026-07-09/10 (P0 surface-check-not-wired; P1 NEVER#1 two-of-three-legs;
F-004 NEVER#3/#7; AC-0 predicate `AC-0_tool_universe_predicate_20260710.json`; RAIL_SET_canonical_20260710;
comp-iam cert @ 6f3751a34/2119e91af). Every failure was exercised with a passing positive control; the 32/60 census
carries positive/negative/trap controls on the recorder.

— 3.0.0_SA_CVO
