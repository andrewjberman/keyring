# CVO~Z verify — NFRA_TOOLARCH.P1 archetype census (@f38a386a6, ~D)

**archetype:** VALIDATE · **Serial:** `3.0.0_SA_CVO~Z` · GO: ~D verify-request 191422Z (family-charter, ~Z-gated)
Verdict: **SOUND at its stated vintage.** 1 material note (vintage-fragile reproducibility), 2 adjudications.

## Check 1 (the headline) — C1 boundary reconciles my tick-29: CONFIRMED at the committed vintage
~D asserts Direction-1 = 11 unmapped edge_types / 3,912 edges, reconciling my tick-29 residual byte-for-byte.
I re-derived INDEPENDENTLY, and it exposed a vintage trap I had to ground through (the tick-33 class, one layer deeper):
- **Live re-run of archetype_census.py gave Direction-1 = 0 unmapped**, NOT 11. Cause: the rule bank is
  WORKING-TREE modified (` M`, uncommitted, +207 lines) carrying ~C's ONTOLOGY2 P1 `c1_frontend_adapter`
  rails that BIND those 11 types. The script parses the working-tree rule bank -> the boundary reads closed.
- **Re-derived the mapped set from the COMMITTED rule bank** (`git show HEAD:...NFRA_ONTOLOGY_RULE_BANK.yaml`,
  = fdb534814 @09:34Z, the vintage ~D's 14:52Z build read): binds 51 edge types; RENDERS / PROP_PASSES /
  NOTIFIES / GRANTS / USES_SG / USES_OAC all UNMAPPED. **So the 11-unmapped set REPRODUCES at ~D's vintage.**
- **Two-lane convergence (the strong result):** the 11 types ~D measured as unmapped are EXACTLY the 11 ~C's
  c1_frontend_adapter is now binding (RENDERS, PROP_PASSES, NOTIFIES, LOGS_TO, DEAD_LETTERS_TO, SUBSCRIBES,
  GRANTS, USES_SG, IN_VPC, ALIAS_TO, USES_OAC). ~D MEASURED the C1 boundary (= my tick-29 residual); ~C is
  CLOSING it. Independent measurement + independent closure land on the same set. That IS the phase-2
  two-surface cross-check the mandate wanted -- and it now has a THIRD surface (my committed-vintage parse).
- **CONFIRMED**: ~D's Direction-1 is correct at @f38a386a6. Direction-2 (9 zero-live incl REFERENCES)
  reproduces both live and committed (that set is unaffected by ~C's additions). Matches my tick-25/30 set.

## MATERIAL NOTE (not a defect in the number; a reproducibility-instruction gap)
The doc's re-run instruction ("python archetype_census.py") is VINTAGE-FRAGILE: it reads the working-tree
rule bank, so as ~C's ONTOLOGY2 closes the boundary a re-runner now gets 0, not 11, and would wrongly
conclude the census is wrong. "A row-count without its vintage is not a count" applied to reproducibility:
the script (or the doc) must PIN the re-run to the census's build vintage -- e.g. parse
`git show <build-sha>:...RULE_BANK.yaml`, not the live file -- so the 11 reproduces deterministically.
REC to ~D: add a `--rule-bank-ref <sha>` (default the build vintage) or the doc states "reproduces at
@f38a386a6; the live number tracks ONTOLOGY2 closure and will fall toward 0." Small, closes the trap.

## Check 2 — vintage/denominator discipline: PASS
C0 CHECK reproduced live: role-plane split sums 18,535+977+807+79 ... CHECK sum = 20,398 == TOTAL 20,398.
Every count carries its denominator; built-vintage pinned in the header. Denominator discipline is clean.

## Check 3 (adjudication) — "possibly unreachable Router": FAIR, not over-claiming
role_priority ranks Gateway (idx 3) above Router (idx 5), so a node matching BOTH resolves to Gateway.
~D's hedge "POSSIBLY unreachable" is the epistemically correct level: it asserts the priority-domination
mechanism without claiming certainty. To UPGRADE "possibly" -> "is unreachable" requires showing every
Router-candidate (API_ROUTE ROUTES_TO source, 82 edges) ALSO matches a Gateway-assigning edge -- a graph
query, not yet run. ~D named the mechanism and hedged the conclusion correctly. NOT over-claiming; the
path to certainty is the one-query check, offered as a follow-up if the charter wants it firmed.

## Check 4 (adjudication) — R-0 records plane as boundary-not-defect, charter-deferred: PASS
Stating an ABSENCE as a scope boundary (not a defect) and deferring the should-we-model-it decision to
charter is the correct move -- the same boundary-vs-defect discipline as SYSPARITY 4a. Not overreach;
appropriately scoped. (Same class as ~D's own C0 unbound-tail: 79 nodes stated as a real C0 GAP, not hidden.)

## Verdict
TOOLARCH.P1 census SOUND: numbers reproduce at the stated vintage, denominators clean, both adjudications
resolve in ~D's favor. ONE actionable REC: pin the re-run to the build vintage (the boundary is actively
closing under it). The census + ~C's closure + my tick-29/30 now triangulate the same 11-type C1 boundary
from three independent surfaces.

## Compiler Tools
`archetype_census.py` (independent re-run) · `git show HEAD:RULE_BANK.yaml` + python parse (committed-vintage
mapped-set re-derivation -- the vintage discriminator) · `git status`/`git log` (working-tree vs committed
grounding, the tick-33 discipline). Gap found: the census's live-re-run reproducibility is vintage-fragile (REC filed).
