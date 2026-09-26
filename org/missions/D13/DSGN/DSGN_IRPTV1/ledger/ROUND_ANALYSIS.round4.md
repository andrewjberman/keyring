# DSGN_IRPTV1 -- ROUNDS 2-4 ANALYSIS (L10, the CTO's read)

**Seat:** 1.0.0_SA_CTO (Claude). Written 2026-09-26 ~13:2xZ on receipt of the CVO's slug
`surprise-channel/remediations/REMEDIATION_v2.md` @`36eb3c9492` and `ADJUDICATION_v3.md` @`7a96a83218` (3.0.0_SA_CVO 101146),
under the self-drive arm @`ce6aa15a17`.

**Inputs:**
- PRD `prd/DSGN_IRPTV1_PRD.md` v0.8 @`31a61d0466` (ratified-text half signed at v0.8).
- Rounds 2 (IV-e-1..8), 3 (IV-e-9..20) and 4 (IV-e-21..30).
- PROD `36a37afc` = `portal-v2.1.188`.
- ~D's walk record `deliverables/2.0.0_SA_COO~D/prod-walk-20260926.md` @`9b5eed8f9d`.

**Terminality:**
- Every order of rounds 2-4 is `complete`.
- 15 of 16 ARMED rows are dispositioned by the CVO (12 remedied and disarmed; 2 dismissed and carried by S7).
- S7 is the one OPEN row and is ruled below.

**ROUNDS 2-4 CLOSE here.**

## 1. Coverage, graded on the artifact

No EXERCISED outcome can grade REALIZED yet.
- Every close run so far is fixture-driven.
- Tonight's Opal-class walk could not open the page: the route admits admin + internal + Dev only (101105).
- Its HAR was lost to a full disk.

Andrew chose "Agent on an admin+dev login" (record addendum @`e2eae53ae3`). That walk is round 5's drain act, and it
grades these outcomes.

| FWD | DONE WHEN | Grade now | Why |
|---|---|---|---|
| FWD-1 thread | EXERCISED | NOT_EVALUATED | The signed-in trace is owed by the admin + Dev walk. The `spread` hop depends on P. |
| FWD-2, 3, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18 | EXERCISED | NOT_EVALUATED | Built and on PROD `36a37afc`, per rounds 2-4 and the CVO's disarm reads. They are graded by the walk: round 4's AC4s, plus round 3's five NOT_EVALUATED (model level, map, picker list, drill, the once-over). |
| FWD-4 one firm control | APPLIED | REALIZED | Round 2 landed it. The CVO read the code on DEV and PROD. |
| FWD-9 one Export | APPLIED | NOT_REALIZED | Holdings export is not served. 2.0.0_SA_COO~P owes a `holdings` report kind (routed at 101048), and IVE16 stays uncut until it lands. |
| FWD-10 panel system + tab order | APPLIED | REALIZED | The tab order is Performance / Holdings / Analysis, seen on the round-3 close run and on PROD. |
| FWD-11 no state tokens on the body | APPLIED | REALIZED | Round 3's IVE18 census found 0 banned tokens (the CVO disarm read). The UNAVAILABLE residual is S7's. |

## 2. S7 ruling -- the 80 legacy failures (per-test, BY CLASS)

Each failing test at the round-5 base takes exactly ONE class. ~D records the class per test in a table. The S7
disarm row quotes this ruling and that table.

| class | test | disposition |
|---|---|---|
| **R -- RETIRED** | Asserts behaviour a PRD amendment retired or changed: account chips on the header (FWD-2 v0.6); the drawer or truncated menu (FWD-3 v0.6); the left rail or request history (FWD-7/8 v0.6); method, lineage, basis, denominator or provenance in the footer (FWD-5/6 v0.8); an "UNAVAILABLE" string on a body (FWD-15); the retired `render/performance/Summary.tsx` block. | Re-scope the assertion to the current ENDPOINT, or delete it. Name the FWD and version that retired it on the row. |
| **G -- REGRESSION** | Asserts behaviour the current ENDPOINT still requires, and fails. | Fix the CODE. Never edit the test to pass. |
| **H -- HARNESS** | Fails for an environment reason: fixture paths resolved from a worktree (the known fe-s-10 artefact), missing browser APIs, timing. | Fix the harness. The assertion is unchanged. |
| **Q -- QUERY** | Cannot be classed from the PRD. | One line each, batched to the CTO in the drain message. At most 5; more than that means the classing is too loose. |

**Grade:**
- Test-level: the suite fails only the Q rows at the drain.
- Record-level: every test carries a class, and every R row carries its retiring FWD and version.
- The CTO reads the table at the round-5 analysis.

## 3. Round-5 enrichment list (the next round cuts these; the COO sequences)

1. **S7:** the batched legacy-suite cell (section 2).
2. **FWD-12 remainder:** colour keyed by the SERVED `model_code` (2.0.0_SA_COO~M serves it since the 09-25 republish),
   retiring `getModelColor`'s longest-key label fallback for IRPT (C17's intent).
3. **SearchSelect accessibility:** combobox, listbox and option roles, plus keyboard navigation (round-3 close item 1).
4. **IVE16, Export on Holdings:** cut when P serves the `holdings` report kind. The FE hookup is one
   EXPORT_KIND_BY_TAB line.
5. **The admin + Dev walk (drain act):** under its two-half packet (P drafts; CTO + 4.0.0_SA_CRO sign). The HAR is
   written scrubbed in-stream, with at least 5 GB free first. It grades section 1.
6. **Owed PROD reads (Monday 2026-09-28, after ~M's runs):**
   - z09305589's Other slice ($19,653,063.27, after Part 2);
   - a cash relationship summing to 100%;
   - an all-cash client at 100%.

   These are IVE28-AC4 and IVE29-AC4.

**Surfaced, not an IRPT cell:**
- **The 403s:** the walk read 403 on every Advisor Intelligence Cottonwood drill as an Opal-class principal (@`9b5eed8f9d`).
  ~D files it as a surprise row: owner, the AI drill authorizer's lane; disarm, an Opal-class read of one drill
  returning 200, or a ruling that Opal-class is excluded by design.
- **Disk:** the laptop C: drive filling (ENOSPC cost the walk's HAR) is 0.0.0_AB_MSTR's. About 11 GB of CTO worktrees
  are released for removal (the CTO's reply to 101135).

## 4. Close

`dep_stage` -> ROUND_CLOSE for round 4. Round 5 is cut in ONE issuance from section 3. `FWD-1` stays open until the
admin + Dev walk grades it.
