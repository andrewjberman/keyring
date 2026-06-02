# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2046Z

## W4f data-scope pre-stage (COO 204209Z, Andrew-flagged) — non-admin cross-advisor drill = 403

Q: with Joe (non-admin, firmRole=null, advisorId=joe_brandenburg) on the FULL Distribution tab,
what happens drilling a DIFFERENT advisor (peter_lee)?

### Edge trace (code-definitive — pure JWT-claim logic)
auth-validator-edge getAllowedAdvisorIds(payload): role=admin OR firmRole=admin -> null (all
advisors); !advisorId -> []; else -> [jwt.advisorId].

1. ADVISOR grain (.004a, :267-286; ADVISOR_SCOPING_PATH_PATTERNS covers /partners/books/advisor/{id}/*
   AND /advisor-intelligence/platinum/advisors/{id}/*.json = the inflection static book path):
   - Joe -> peter_lee: peter_lee not in [joe_brandenburg] -> 403 "not authorized for this advisor".
   - Joe -> joe_brandenburg (own): 200 (book.json exists).
   - Peter (firmRole=admin): getAllowedAdvisorIds=null -> any advisor, no 403.
2. RELATIONSHIP grain (.004c, :289+; /partners/books/relationship/{key}/*): non-admin -> getOwnershipMap
   (inflection ownership_map.json ABSENT) -> 503 fail-closed for ALL non-admin relationship drills.
   If produced: own-clients 200 / cross-advisor 403.

Lambda (opal-partners-data) is firm-OPEN at both grains; the per-advisor scope is ONLY the edge.

### Answer + recommendation (RAVC2 to COO+CTO+CVO+RD~C)
Non-admins are scoped to THEMSELVES by design (.004a/.004c key on jwt.advisorId). For Joe's
Distribution at "Peter fidelity":
- firm-aggregate + own-advisor drill: work as-is.
- cross-advisor drill: 403 by design.
Fork: (a) [rec, no backend change] RD~C W4f FE scopes/disables non-admin cross-advisor drill targets;
(b) [edge-policy change] non-admin "distribution-viewer" exemption from .004a/.004c (mirror admin
getAllowedAdvisorIds->null) + produce inflection ownership_map.json -- CTO/Andrew decision; I can
implement edge + map if ruled. NB: even Joe's OWN relationship drills 503 until ownership_map exists.

### Outcome
Bounded analysis RAVC2 (204649Z). Routes the (a)/(b) policy decision to Andrew/CTO. Not blocking
RD~C W4f FE. Analysis-only (no code change this tick).
