# 1.0.0_SA_CTO -- 2026-09-03 04:50-05:10Z -- "Recs approved": the L8 send guard, gate (iii) second limb, gate (iv) fix

Push state at close: origin/CLOUD @800b85c1a2 (ls-remote read after 0.0.0_AB_MSTR's window, frames 93117/93124);
local HEAD @f56aa9b280 + this log, LOCAL ahead 3-4; no window until Andrew's word.

## Inputs (READ-acked)
- Andrew at this terminal: `/open-calls here` -> 2 cards; then `Recs approved` (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_045xZ_RECS_APPROVED_CVO_SEND_REFUSED_L7_L9_GATE_III_INVESTIGATIONS_LIMB.md`).
- Andrew mid-turn: "how do you differentiate between a decomp invalidation versus a spec error? ... at the L10 cycle
  back" -- answered in the turn from the estate's own axis (remediation_row.schema.json `route`: what does the remedy
  need that does not exist yet -- a cell the decomp holds = SPEC_ERROR -> L6; a cell it lacks = DECOMP_INVALIDATING ->
  L5; an outcome the PRD lacks = SCOPE_CHANGE -> L2); the cheap-direction mis-route is caught at L6 by the decomp-ref
  lint; the other direction costs an L5 pass that changes no cells.
- 93110 2.0.0_SA_COO: gate (iv) refused the COO's own task orders (GIT_AUTHOR_IDENT reads the config name at
  pre-commit); 93111 3.0.0_SA_CVO: annex v2.1 mirrors spine v2.1; 93117/93124 0.0.0_AB_MSTR: push window open/close,
  origin @800b85c1a2.

## Acts
1. Record of the word (verbatim + the two cards + scope reading), committed with the gates.
2. `org/mcp/cvo_send_guard.py` (new; pure decision + one census + `--self-test` 8 arms + live census) wired into
   `org/mcp/server.py` send_message before any write over the whole recipient list, and into `org/mcp/broker.py`
   `/send-message`. Refuses 3.0.0_SA_CVO (any ~lane) -> any Tier-2 serial while any tree project.json reads
   dep_stage EXECUTING. Applied: MCP path per session start; daemon path at its next restart (not done -- fabric hold).
3. `.tools/surprise-row-gate.py`: gate (iii) second limb (`_index_paths`, `_resolve_latest` pure, `_latest_dispositions`
   from the INDEX, `_investigations_precondition_violations`), both route shapes (remediation `route`; investigation
   `disposition: DECOMP_INVALIDATING` -- round 1's stamp shape, unseen by the first limb), `--self-test` 6 arms +
   live census (NFRA_COMPEFFICACY: 7 items, undispositioned S1/S2/S3/S5 by machine reading, 0 phantom).
   `org/surprise_channel/schemas/investigation_item.schema.json`: optional `adjudicates` (array of ids) -- the
   append-only carrier for dispositioning an existing item. Standing corpus pass unchanged (4 known, 0 new).
4. `.tools/to-pipeline-gate.py` `_committer_serial`: resolve-actor precedence ($OPAL_AGENT_SERIAL -> session serial
   file -> GIT_AUTHOR_IDENT). Exercised red / green / negative control (1 / 0 / 1 violations). Shape (a) NOT taken:
   `owned-paths-check.sh` and `mstr-ledger-check.sh` read GIT_AUTHOR_NAME and skip when unset -- exporting it would
   silently arm two dormant fabric-wide hooks. Finding surfaced to the registry grantor (COO) and MSTR, not chased.
5. Commits: gates + record @4774db2c87 (7 files; commit-gate clean 5 of 5 .py); spine v2.2 @f56aa9b280 (L8 Gate,
   L10 Gate both limbs/shapes/`adjudicates`, section 3 L8 row, changelog 2.2; form check 13 of 13).
6. Broadcast (law edit, third surface) to 2.0.0_SA_COO, 3.0.0_SA_CVO, 0.0.0_AB_MSTR, 0.8.0_AE_CloudComp with push
   state as measured; RAVC to 93110 answered (shape (b)); CVO told which items round 2's slug must adjudicate.

## Instruments this window
cvo_send_guard --self-test, surprise-row-gate --self-test, three env-arm probes of _committer_serial, jsonschema
check_schema, surprise-corpus-validate, commit-gate x5, ast.parse x2, spine_form_check (13 arms), safe-commit -F x2,
git ls-remote / rev-list.

## Open, with owner
- 3.0.0_SA_CVO: adjudicate S1/S2/S3/S5 with `adjudicates` rows in round 2's L10 slug; certify the water test (standing
  certifier, decided in lane).
- 2.0.0_SA_COO (registry grantor) + 0.0.0_AB_MSTR: the two dormant GIT_AUTHOR_NAME-keyed hooks -- run them or retire
  them; a decision, not a CTO act.
- Broker daemon restart for the HTTP-path guard: at the next window Andrew opens, or never needed if no sender posts
  to /send-message directly (server.py grades first).
