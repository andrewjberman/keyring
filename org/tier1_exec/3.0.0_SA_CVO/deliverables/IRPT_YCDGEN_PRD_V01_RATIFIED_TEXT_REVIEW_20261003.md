# IRPT_YCDGEN PRD v0.1 -- ratified-text half review (3.0.0_SA_CVO, 2026-10-03 ~21:1xZ)

Delivered by `1.0.0_SA_CTO` msg 104758. PRD `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` @f65ec43d8c (prd_version
v0.1), half hash c78f80ca2cda. The brief half is admitted (the CRO wrote the brief).

**Verdict: SIGN.**

| check | this seat's read | result |
|---|---|---|
| ENDPOINT verbatim against the ratified pins | The PRD's ENDPOINT block (lines 28-88) was compared with the endpoint record `ENDPOINT_FORWARD_IRPT_YCHARTS_DIRECT_GENERATION_20261003.md` at c3f2fb4bb3, block by block with whitespace normalized: FWD-1 to FWD-7 identical, 7 of 7; no outcome added or dropped | PASS |
| the pin is ratified | `ANDREW_DIRECT_20261003_203xZ_ALL_APPROVED_YCHARTS_DIRECT_GEN_ENDPOINT_AND_SITEZ_SCOPE.md` (15393344e7): verbatim "all approved"; item 1 "Confirm the seven outcomes ... CONFIRMED as written" | PASS |
| every operative constraint present | the endpoint record's five boundaries and three readings each have a carrier: no second production path and a one-time FWD-7 (C-SCOPE, C-COMPARE); the served path undisturbed, one session, firewall pace, challenge stops research (C-SESSION); naming builders and a register family (C-STORE, C-REGISTER); reading 1, data endpoints (C-ENDPOINTS); reading 2, egress to ~Y and its agents only (C-VENDOR); reading 3 and no client-facing release (section 6 ruling 10, section 8 PART II) | PASS |
| no annotation, history or seat name inside the section | lines 28-88 hold the seven blocks only (outcome, DONE WHEN, ACCEPT, SOURCE); "Andrew" is the user named in the outcomes, as in the ratified pin; the provenance sits outside, under PROVENANCE | PASS |
| CONTRACTS agree with the counterpart PRD | C-SESSION consumes IRPT_BCKEND's session broker (B8, v0.5), account coordinator (B17) and leases (B16) as the owner. IRPT_BCKEND v0.24 has no clause reserving the session to the served path and none contradicting a second, lease-serialized consumer | PASS (see note 1) |
| C-STORE builder output | re-run here through `lib/opal_naming.py address()`: the three state addresses reproduce byte for byte (`s3://opal-data-cottonwood/irpt/cottonwood/state/{ycharts_responses,ycharts_runs,ycharts_opal_reports}/request=REQ-329a56182b2668d44a28c8d7/...`); bronze for cottonwood resolves to `opal-data-assets`, as the contract says | PASS |
| C-REGISTER premise | `infra/logic/registry/reporting_policies.json` at HEAD: no YCHARTS family, no `irpt-ycdgen-research` row | PASS |
| cited code | `ycharts/session/operation_lease.py`, `ycharts/session/resident_session.py`, `ycharts/generate/recipe.py` (template ids 14141822, 14141824, 14141847 at lines 130-132) and `export/bundle.py` all exist at HEAD | PASS |

**Notes (not conditions).**
1. IRPT_BCKEND's PRD does not name IRPT_YCDGEN as a consumer of its session broker and lease. A one-line IRPT_BCKEND addendum
   would make the agreement two-sided. Nothing in either PRD conflicts.
2. The no-client-release boundary is carried by section 6 ruling 10 and section 8, not by a row of the CONTRACTS table.

-- 3.0.0_SA_CVO
