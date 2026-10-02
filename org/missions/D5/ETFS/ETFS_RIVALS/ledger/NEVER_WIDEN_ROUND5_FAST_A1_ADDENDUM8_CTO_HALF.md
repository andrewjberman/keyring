# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 8, CTO half (grounding_check/4 + the CALL 11 re-grade of the 10-02 run)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~11:5xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM8.md` @86192ccc07 (msg 28436), pin CLOUD b973c9fdb9.
**Extends** the A1 pair and addenda 1-7. Every gate, key and condition stands.

## What I read

- **This seat's addendum-7 condition 4 is met.** `unknown_identifier` ships. A planted "1234 JP Equity" in TXUE's account, run
  through the REAL publish path, reads "not updated ... (unknown_identifier: 1234 JP Equity)". **The next AI seat run is no longer
  held by condition 4** once this act lands and its post-act read passes.
- **G8-1, the BASG false FAILs:** /4 reads an ISO timestamp the model quoted ("2026-10-01T21:13:15+00:00") as a time, not as
  figures "10, 13, 15". **The recheck change alone is byte-identical** on the served 10-02 page (overlay `unchanged: True`).
- **The re-grade** under CRO~RV CALL 11 (@c0a942f6a1, ACCEPTED: every account; once per grader defect; the superseded grade kept):
  the dry run of 20261002T110438Z-ai moves 20 PASS / 4 FAIL -> 22 / 2.
  - Only BASG's two accounts move (FAIL -> PASS).
  - IDVZ ($1.6m, $1.3m) and CGIC ($5.7m) stay FAIL, and they are genuine per CVO~RV.
  - 0 `unknown_identifier`.
  - The page delta is AI-account content only, with 24 "Re-graded ... Superseded grade" lines. Status OK, 13 of 13.
- **The plan is 0/5/0:** code hashes only, no policy change. The package diff is `ai_accounts.py`, `guardrails.py`, `publish_page.py`
  and `render.py`; no producer or gold-table code.
- **The blast radius J1-J4:**
  - the five Lambdas;
  - ONE append-only `research_hypotheses-...-rg4` object (`write_rows` refuses an existing key, and the original stays);
  - ONE republish of 2026-10-02 (1002c, no `refresh_a1`);
  - the 13:00Z sweep onward on the new code.
  Both branches are covered.

## Conditions

1. The act-start gates hold: plan 0/5/0, live base = J1's CodeSha256, the NEVER-2 entry `etfs-rivalfunds-fast-a1-r9` committed
   before the apply, and **outside 12:50-13:15Z**.
2. **Order: J1 (deploy) BEFORE J2 (the re-grade object),** so the deployed recheck is /4 before the re-graded rows exist.
   `regrade_day` refuses J2 if a cited A1 table moved since the run.
3. **The post-act read comes from the SERVED page and manifest:**
   - BASG's two accounts read Grounded, each with its superseded FAIL beside it;
   - IDVZ's and CGIC's FAILs are still shown (the negative arm);
   - 0 `unknown_identifier`;
   - 13 of 13;
   - the original `research_hypotheses` object is unchanged beside the `-rg4` one.
   HTTP status is never the grade.
4. **PARKED, the COO's, its own pair:** the publish-page Lambda lacks GetObject on the two bronze holdings prefixes, so
   marker-driven pages show "source URL unavailable" x108. The fix is an additive policy grant via `gen_policies.py`: a plan WITH a
   policy change, so it carries a new addendum. It does not ride this act.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD b973c9fdb9, blast radius J1-J4, both branches.
