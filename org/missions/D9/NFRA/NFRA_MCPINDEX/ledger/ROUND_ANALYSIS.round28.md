# NFRA_MCPINDEX -- ROUND-28 ANALYSIS (L10 answer; the round-29 list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-21 ~16:4xZ.
**Answers:** `2.0.0_SA_COO~MI`'s ferry slug (16:40Z) and `deliverables/2.0.0_SA_COO~MI/round28/evidence/ROUND28_STATE.md`
@679ffb5bc58.
**Issuer:** `2.0.0_SA_COO~MI`.

## 1. As read

- **2 of 2 orders (MX-l-1, MX-l-2) complete, merged @724baff7d23, proofs valid.**
  - `round-close-check` reads REFUSED only for reviewer=ABSENT, the ruled tool condition.
  - `dep_stage` moves to ROUND_CLOSE on this analysis.
- **MX-l-1:** the emitter's `--size-census` writes each row's size class as a measured claim. Unmeasured rows say so, with a
  reason. Without the option the output is byte-identical.
- **MX-l-2:** `fwd26_grade.py` grades the 12-question set by the rule this seat ruled.
- **Row Z-W97-S1** (the account-id check could not run) is disarmed by Z-S141 after a hand scan. This is consistent with
  Andrew-direct 2026-10-09: the absent hash list is intended.
- **The trunk catalog is untouched** (md5 `03d2dbbae1f0`) for batch17.

## 2. Endpoint coverage

- **FWD-26:** built, not yet REALIZED. It is realized when the size-carrying catalog is served and the question set grades
  on the served index.
- **FWD-23 to FWD-25:** unchanged (candidate e served by batch17; sheets held for Andrew).

## 3. The round-29 list (ONE issuance, cut after batch17's ledger reads CLOSED, not before 2026-10-22 06:45Z)

1. **Catalog with sizes:** re-run the census, emit with `--size-census`, and place the catalog.
2. **Serve it:** ask `2.0.0_SA_COO~O` to serve it in its next release, including whether `opal_discover` returns the size
   class (COO~O's app code).
3. **Grade:** run the 12-question set against the served index, with O3 included once candidate e is served.
4. **Carried, event-gated:**
   - routing and the battery on candidate e (batch17);
   - the per-vendor re-run after NFRA_OPLGTW's cli-shim release;
   - the 24 MiB line re-measure on NFRA_OPLGTW FWD-23 proof (e).
