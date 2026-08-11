# CTO session log (delta) — proof-of-spec canonized -> the issuance lint GO'd + LIVE — 2026-08-11 0822-0840Z

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Window

Since `final_ratification_parquet_phases_proof_contract_0746-0822Z.md`. Two events, one chain.

## What happened

1. **Andrew canonized proof-of-spec into TO delivery LAW** (~0821Z at the CVO terminal; CVO
   executed same-turn @bddd6554ce: TASK_ORDER_PROTOCOL `<proof_of_spec>` element — issuer mints
   the criterion-id set at decomposition, a TO without it is NON-CONFORMING NOT ISSUED; assignee
   fills the schema instance before any complete flip; XXX.md bullet; verbatim record at CVO).
   My @76ee261895/@d9a9ce7b80 mechanism became law rather than program convention. CVO proposed
   (not implemented) the issuance-time lint as a gate candidate; I put it to Andrew with rec GO.
2. **Andrew: "Go" (~0824Z).** Implemented + exercised same window @da318438ee:
   - `.tools/git-hooks/to-proof-of-spec-check.sh` — NEW task-order files (`--diff-filter=A`,
     `task_orders/*.md|xml`) without `<proof_of_spec>` BLOCK at commit, full citation printed
     (protocol element + schema path + validator + override form). Pre-existing TOs not
     retro-gated; edits pass. Audited override `TO_POS_OVERRIDE` -> org/to-pos-override-audit.log.
   - `.tools/git-hooks/install-to-proof-of-spec.sh` — idempotent stage-8 append to the precomp_v1
     pre-commit orchestrator, with the FAIL-CLOSED sentinel (new TO staged while the check script
     is missing = DENY — the comp-surface-check silent-skip lesson honored).
   - **Exercised:** mutant TO BLOCKED rc=1 with citation; conforming TO rc=0; installer no-op on
     second run. Acceptance = first observed live behavior per the standing law.
   - GO addendum appended to ANDREW_DIRECT_20260811_PROOF_OF_SPEC_TO_CONTRACT.md.
3. **Per-clone scope stated loudly** (not discovered later): pre-commit hooks do not travel with
   git — this device wired; site Z gains stage 8 via its install chain; until then the canonized
   protocol text is the carrier there. MSTR holds the site-Z coordination note.

## The chain, now closed end-to-end (the window's product)

Canonized protocol (CVO) -> issuance lint (commit gate, this window) -> assignee instance
(PROOF_OF_SPEC.schema.json) -> mechanical validation incl. coverage (proof-of-spec-check.py) ->
adversarial cert (CVO Rule-14e re-running row invocations). Under-specified TOs cannot be
ISSUED; unproven work cannot COMPLETE — both by construction.

## MCP traffic

6 total this window; significant: CVO canonization broadcast (in), my GO card to Andrew (terminal),
3 landed-notices out (CVO w/ per-clone note, COO pre-first-dispatch warning, MSTR record).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| to-proof-of-spec-check.sh (new) | mutant staged TO + conforming staged TO, env-contract per orchestrator | PASS both directions (BLOCK rc=1 / clean rc=0) |
| install-to-proof-of-spec.sh (new) | run x2 | PASS (wired, then idempotent no-op) |

What worked: the estate's own gate pattern (tracked check + installer + fail-closed sentinel)
made the lint a 30-minute land. What failed: nothing this window. Gap found: none new; the
per-clone hook-distribution gap is stated, not new.

## Blockers

NONE at this seat.

## Current State (zero-context handoff)

The build program: five-phase order (@4dbf4a0d7c) executing; COO decomposing P1 under the
canonized proof contract; cert pipeline final at CVO (TO-vs-spec -> assignee-vs-TO -> per-row
re-run -> Rule-14e). Gates live on this clone: pre-commit stages 1-8 (8 = the TO issuance lint,
@da318438ee). Standards: org/standards/PROOF_OF_SPEC.schema.json + .tools/proof-of-spec-check.py
(coverage-capable). Watches: 13:47Z INF production cycle (two cert folds + serve-#2 branch),
14:10Z X-iii scheduled closer, first P1 proof-of-spec instances. At Andrew: the AUA basis ruling
(via COO, both exec reads attached).

## Next Steps

1. **[2.0.0_SA_COO]** first P1 dispatches — the lint's live acceptance event.
2. **[3.0.0_SA_CVO]** 13:47Z double-fold; consume first instances (step-zero first).
3. **[0.0.0_AB_MSTR]** site-Z install-chain note for stage 8.
4. **[1.0.0_SA_CTO]** oversight; M7xwo2 one-ordered-act at P4; bd-cot IAM half on the roster.
