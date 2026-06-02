# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~1924Z

## W2 per-endpoint coverage confirm (RD~C omit-param dependency) — gates Andrew re-smoke

RD~C landed the W2-FE rewire (portal DEV 8ff69f18): 9 'firmOverride required' throwers
eliminated; 8 fetch wrappers now OMIT ?firmId= for external users, RELYING on the W2
opal-partners-data JWT-firmId-fallback to self-scope. COO + RD~C asked (DRIVE-URGENT): does
W2 cover EVERY Lambda endpoint those wrappers hit, or just clients-tab?

### Verification (DEPLOYED Lambda invoke, external auth firmId=inflection, ?firmId= OMITTED)
ZERO endpoints return 400 "Missing required query parameter: firmId":
| Endpoint | Block | Result |
|---|---|---|
| clients-tab | advisor-intel :1685 | 200 (real data) |
| books/relationship/{key}/platinum-summary | books :1778 | 404 bogus-key (fallback fired) |
| books/advisor/{id}/platinum-summary | books :1778 | 404 |
| books/firm/all/composition | books :1778 | 404 |
| books/advisor/{id}/composition | books :1778 | 404 |
| advisor-intelligence/clients/{key}/detail | advisor-intel :1685 | 404 (admin-bypass) |
| advisor-intelligence/advisors/{id}/book | advisor-intel :1685 | 404 (admin-bypass) |

404 "Data not found" = the firmId fallback RESOLVED the firm from JWT and proceeded past the
gate to a bogus-test-key lookup (real keys return data). The only failure RD~C cares about --
400-missing-firmId -- occurs on none.

### Why blanket coverage
opal-partners-data has EXACTLY two ?firmId= gate blocks (advisor-intelligence :1685 + books
:1778); W2 put the `if not firm_id: firm_id = user_firm_id` fallback in BOTH. Every endpoint
RD~C's wrappers hit routes through one. is_authorized() still gates the resolved firm (no
cross-tenant; CVO SECURITY PASS holds across the class). No fallback extension needed.

### Nuance flagged (NOT a W2 gap)
L1/L2 advisor-intel endpoints (clients/{key}/detail=L2, advisors/{id}/book=L1) have a
firmId-INDEPENDENT advisor_role tier gate (:1655) that runs before the firmId gate -- 401
"Insufficient advisor role" for an under-privileged external user, by design, with or without
firmId. advisors/{id}/book also has an L1 scope check (path advisor_id == jwt advisorId).
Used admin-bypass to isolate the firmId path for those two.

### Outcome
RAVC2 "coverage COMPLETE, no extension needed" -> COO + CTO + CVO + RD~C. Andrew re-smoke
unblocked from the backend side (pending 8ff69f18 served on DEV + CVO e2e re-verify). No
commit of code (verification-only tick); evidence reproducible via .runtmp/oppd_cov/ payloads.
