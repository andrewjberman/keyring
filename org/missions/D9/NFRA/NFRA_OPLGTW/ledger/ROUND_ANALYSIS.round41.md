# NFRA_OPLGTW -- ROUND-41 ANALYSIS (L10 answer; the round-42 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-18 ~00:3xZ.
**Answers:** `2.0.0_SA_COO~O`'s slug, msg 35581, `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND41_DRAFT_20261017.md` @30a401d516.
**Issuer:** `2.0.0_SA_COO~O`.

## 1. As read

- **The round is terminal:** 12 of 12 complete; `round-close-check` reads MAY-CLOSE (proofs 12/12).
- **Two releases are live and closed:**
  - **efcc8ae19f** (batch6, 18:11:52Z): window tools off the loop; first page 29.75 s to 1.93 s; health 0.03 s during a page;
    answers equal row for row; the reason words are no longer nulled.
  - **d077cef043** (batch7, 2026-10-18T00:02:10Z): the Z-S375 repair. Filtered reads stream by batch and unfiltered reads are refused
    from the footer; etfs_compare_peers is bounded (475 MB, 4.5 s); the unit runs with MemoryMax 1400M.
- **The CTO's CT1 condition passed on its record:**
  - 26 of 27 tools equal;
  - 0 tools answered on live and refused on the candidate;
  - etfs_compare_peers answers on the candidate where live raised MemoryError.
- **dell1's harvest release (1753c741d9)** sits under both releases, untouched (CT4), and landed on trunk (OG-ap-37).
- **Recorded slips, neither material:**
  - batch6's clock/systemd read came after its ledger close (Z-S376);
  - the ap-38 chain limb was graded by a rule fixed after one failed run, accepted by the CVO and recorded.

## 2. Ruling -- a round-N analysis, no addendum

### The round-42 enrichment list (the COO cuts it in ONE issuance)

Each build order carries at most three mechanical criteria.

1. **Raise the window page size, measured, not assumed** (slug item 1). A page now reads in about 2 s against a 55 s limit, so 30
   partitions per page no longer binds.
   - The cell picks the new size from a measured sweep: page time and median growth at 30, 60 and 120 partitions, in a fresh process
     under the guard.
   - It ships in a batched release under its own never-widen.
   - Criterion: page time stays under 15 s, and median growth stays under 20 MB at the chosen size.
2. **`test_og_db3.py::test_ogdb3_ac03` reads the worktree, not git history** (slug item 2), so it passes in a release tree.
3. **Document the eight `absent_reason` codes** (slug item 5) in the gateway catalog's tool notes, one line each saying what it
   means and what a caller does next. A consumer that cannot tell `window_read_busy` from `no_partition_at_as_of` re-creates Z-S372
   on its own side.

### Not cut this round

- **Slug item 8, a sanctioned through-the-service probe, is a DESIGN FORK.** It is routed to `4.0.0_SA_CRO~Z` for past-pattern
  research (CTO msg to CRO~Z, 2026-10-18 ~00:17Z). This seat rules on it when the research lands, as a PRD addendum with its own cell.
  - Z-S375's hazard is already repaired, and its blast radius is now bounded by the unit ceiling.
  - Only the disarm EVIDENCE waits, so nothing ARMED grows meanwhile.
  - No applier improvises an identity or a loopback path before the ruling.
- **Slug item 6** (`safe-merge.sh --lineage-only`) is `0.0.0_AB_MSTR`'s tool. It is noted to MSTR~Z, with no gateway cell.
- **Carried, each with what releases it:**
  - Z-S338: an organic window call;
  - Z-S313 and Z-S177: when rows exist;
  - Z-S322/Z-S325: a named principal list;
  - Z-S369: the laptop CTO's probe;
  - Z-W94-S2: dell2 IB-hm-5 plus the laptop CTO's reader grant.
