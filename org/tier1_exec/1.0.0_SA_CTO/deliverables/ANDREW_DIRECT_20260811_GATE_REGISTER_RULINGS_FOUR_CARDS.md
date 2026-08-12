# ANDREW-DIRECT 2026-08-11 ~1905Z (CTO terminal) -- the gate-candidate register ruled, four cards one sitting

## VERBATIM

> "1 yes, 2a yes 2b no, 3 yes, 4 yes as sequenced"

Issued against the CTO gate-candidate register card set (four cards, presented ~1903Z). The
rulings, with disposition and owner:

| # | Candidate | Ruling | Owner / landing |
|---|---|---|---|
| 1 | Handoff-summarization rule: a registry `blocking` field naming a COO/CTO action may not be summarized as an "Andrew decision" in any handoff unless the field itself changes | **APPROVED** | 2.0.0_SA_COO (their proposal, their registry surface) -- implementation routed with CTO design note: the checkable predicate is an "at Andrew" handoff claim citing the registry field VERBATIM; lint flags any Andrew-decision list item whose cited project's `blocking` names a non-Andrew actor |
| 2a | Lint denying `jq` INVOCATIONS in `.claude/skills/**` + `.tools/**` shell contexts | **APPROVED** | 1.0.0_SA_CTO -- landed same turn: `.tools/git-hooks/jq-ban-check.sh` + installer (pre-commit stage 9), fence-aware for .md, comment-excluded, prose-mention-safe (the LD-0274 matcher caution designed in), audited override `JQ_BAN_OVERRIDE` |
| 2b | Deny `2>/dev/null` on verdict-feeding reads | **DECLINED as a gate** (his "2b no") | stays Rule-16 PROSE prohibition -- not mechanically decidable; no gate built |
| 3 | VOID-terminal machine check: schema constraint binding run `status:CERTIFIED` to a non-VOID certifying attempt (PASS / PASS-WITH-REFUSAL cert_ref) | **APPROVED** | CTO~Z (cross-fabric surface per the ratified FABRIC_ONTOLOGY_INTEGRATION boundary) -- routed via 0.0.0_AB_MSTR's MSTR-to-MSTR channel with Andrew's word attached |
| 4 | Shared-enum drift check on {MEASURED/UNMEASURED/INFERRED/NOT_MEASURABLE} | **APPROVED AS SEQUENCED** -- builds only AFTER the integration single-sources the enum (a drift check on a not-yet-unified enum measures the wrong thing precisely) | registered to ride the integration's single-sourcing milestone; owner assigned at that event (MSTR carries the trigger) |

Recorded by 1.0.0_SA_CTO same turn. Broadcast: COO (#1 + #2a/#2b), MSTR (#3 routing + #4
trigger), CVO (FYI -- they flagged #3/#4).
