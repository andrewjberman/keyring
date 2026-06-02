# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~1933Z

## INFPRM pre-Andrew-smoke backend/data verifies (COO DRIVE 192748Z) — both done

### Check #1 — per-endpoint coverage: COMPLETE (already RAVC2'd 192402Z)
W2 JWT-fallback blankets both ?firmId= gate blocks; all of RD~C's omit-param Lambda endpoints
covered (getPlatinumClientSummary / getPlatinumAdvisorDrilldownSummary / relationship
platinum-summary under the books block). No extension needed.

### Check #2 — Peter book-data verify: book RENDERS; client-drills blocked by provisioning gap
RD~C's book FE-leg routes external Peter -> getPlatinumAdvisorSummaryStaticInflection ->
static-S3 platinum/advisors/{advisorId}/book.json.

**(b) book.json EXISTS** (verified S3): peter_lee 169KB, joe_brandenburg, patrick_scanlan,
inflection_wealth_management -- all fresh 2026-06-02 11:09. Book renders.

**(a) advisorId claim**: Peter's user record (USER#peter@inflectionwealth.com, SK=PROFILE) =
role=user (non-admin), firmId=inflection, NO advisorId / advisorRole / firmRole -> JWT carries
EMPTY advisorId.
- BOOK: unaffected. The advisor book.json path is NOT edge-004c-scoped (ACCOUNT_SCOPING_PATH
  :93 = platinum/accounts/{id}/*.json; RELATIONSHIP_SCOPING_PATH :96 = partners/books/
  relationship/{id}/* -- neither matches advisors/{id}/book.json). Book-drill advisorId = the
  selection SLUG (peter_lee), not the JWT claim. Renders.
- CLIENT/RELATIONSHIP/ACCOUNT drills: WILL 403. auth-validator-edge:312 004c does
  `if (!advisorId || !firmId) forbidden("missing identity claims")` for non-admins. Peter
  non-admin + empty advisorId -> 403 on getPlatinumClientSummary (relationship platinum-summary,
  Segment drill) + account drills. PLUS no inflection ownership_map.json exists -> 503 even if
  advisorId were set. Double-blocked, INDEPENDENT of W2 (edge identity/ownership layer).

### Outcome
RAVC2 to COO+CTO+CVO+RD~C+DS. Pre-smoke guidance: Peter Firm Overview ✓ + Book ✓; client
drills 403 = a user-provisioning gap (record lacks advisorId=peter_lee link + no inflection
ownership_map), NOT a W2/FE regression. Open question for Andrew/COO: is Peter a firm-level-only
viewer (403-on-client-drill correct) or an advisor who should see his 63 clients (needs advisorId
provisioning + ownership_map -> DT/DS before smoke). W2 + W6.2 stand done.
