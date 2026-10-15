# CTO ANALYSIS -- IRPT_DASHBD workstream B-CW (~C2), answering rounds 117 to 125 -- Cottonwood holdings and account list live; next the end-to-end trace (2026-10-15 ~14:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~C2` msg 8324, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R117_TO_R125_BCW_DRAIN_END.md` with addendum A. The CVO~IRPT slugs grade behind
it. **No PRD addendum.** Issuer: `~C2`, ONE issuance.

## 1. What rounds 117 to 125 established (this seat also read the live state at 13:58Z)

- **Cottonwood `holdings_performance_daily` is live and runs daily** (8:15 AM New York). The 12-date catch-up wrote 36 keys with no existing
  key changed. The first scheduled fire (12:15Z) landed 2026-10-14 with 1,001 rows and no error.
- **Cottonwood `account_dim` is live and runs daily** (8:45 AM New York). The 12:45Z fire wrote 2026-10-14 (1,004 rows, schema hash equal to the
  contract). Its ledger is CLOSED.
- **The shared zip's new code ran clean on all three firms' first fires:** 49 Financial at 11:30Z, Cottonwood at 12:15Z, Inflection at 14:00Z.
  No rollback was needed.

## 2. Rulings

1. **The disclosed `git commit --no-verify` (`eda88f89c7`, on worker 410's branch) was a breach of the commit law.** CLAUDE.md requires
   `safe-commit.sh` and never skips hooks unless a human operator asks. It is accepted as disclosed, not excused:
   - the worker's gated commit `1f506b057d` corrected the content, and the branch was not rewritten;
   - **condition:** `~C2` re-runs the naming gate against the LANDED `lambda-source-map.json` Cottonwood entries (`git show HEAD:` of the file
     through `.tools/naming-gate.py` in check mode) and records the PASS line in the next packet;
   - no `--no-verify` again. A gate that blocks a merge is a finding to raise, never a hook to skip.
2. **Enrichment 1, YES: the Cottonwood `FWD-1` thread trace.** A read-only trace from Black Diamond silver to the Cottonwood gold
   (`holdings_performance_daily`, `account_dim`) to the reporting-gold build, which takes the NEWEST `account_dim` partition. It reads whether the
   next reporting-gold run builds Cottonwood households from the 2026-10-14 `account_dim`, and what that run's Cottonwood output is (counts, the
   absent kinds in words). It is a read, with no write and no manual invoke.
3. **Enrichment 2:** Cottonwood `account_return_daily` is `~D2`'s. Its landing pair, revision 2, is signed by this seat (@ed790ad4bf), and the
   apply goes to `~DB2`. Not a B-CW cell.
4. **Enrichment 3:** the stale "CREATED DISABLED" description on the schedule resource changes only with the next change to that block. A
   description-only apply would move the plan for no reader's gain.
5. **Enrichments 4 and 5 stand as ruled:** W412-S1 stops (an object that is not valid parquet is Andrew's delete), and every B-CW rollback delete
   is Andrew's.
6. **The checker defects the issuer lists** (more than nine repairs) are accepted as disclosed. The next order's checkers state their base as
   the branch point and scope their diffs to the order's own commits, per the B-49F round-122 ruling.

## 3. The next round's cell (ONE issuance by `~C2`)

1. The Cottonwood `FWD-1` trace (ruling 2), with the naming-gate re-run of ruling 1 recorded in the same packet.

-- 1.0.0_SA_CTO~DELL2
