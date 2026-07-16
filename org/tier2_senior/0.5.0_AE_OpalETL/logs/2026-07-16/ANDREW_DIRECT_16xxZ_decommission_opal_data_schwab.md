# ANDREW-DIRECT INSTRUCTION -- RECORDED VERBATIM (same-turn law)

**archetype:** SCRIBE

**Channel:** Andrew direct, 0.5.0_AE_OpalETL's own terminal session.
**Time:** 2026-07-16 ~16:2xZ (immediately following the WP7 deploy-leg report + the 01_raw
lineage confirmation).
**Verbatim:** "yes 01_raw is 0824, but now that we have that clearly defined and in canonical
form in the actual opal-data-assets correct location, we do not need to use the schwab bucket,
just need to identify anything that points to it still and redirect that to the correct
location in opal-data-assets and then decommission the opal-data-schwab bucket"

**Scope as surfaced (not adjudicated):** (1) CENSUS everything still pointing at
opal-data-schwab (code, TF/IAM, skills/docs, event wiring, live writers/readers); (2) REDIRECT
each to the correct opal-data-assets location (schwab/08242234/... per the monolith grammar);
(3) DECOMMISSION the opal-data-schwab bucket. Standing rulings this lands on: the CTO seam
ruling (pre-deletion, legacy pre-SI2 history copies INTO monolith bronze; 01_raw then
read-only-retained; deletion was reserved for Andrew's word -- THIS IS THAT WORD, scoped to
the whole bucket, conditional on the redirects landing); L5b (the 0824 seven's parameterized
re-point, pre-approved, ~A's lane) is now the redirect vehicle for the converter class.
Deletion execution remains destructive-class: staged (redirect -> verify zero readers/writers
-> read-only -> Andrew's final go on the delete itself).

**Broadcast:** MCP to COO + CTO + MSTR same turn. **Execution:** census started same turn.
