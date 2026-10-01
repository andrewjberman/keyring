# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 15Z-19Z (host opal_bloomberg)

Lease FULL, round 6 at L10 (the slug held for MX-s-16), thread y.

## Decisions closed this span

- **Gateway train after MX-r-8:**
  - OG-rl-2 LANDED 0a1d9079c6 (15:34Z);
  - the Andrew-direct Tax SMA priority hold (MSTR~Z msg 27995, @92a542c450) was observed. MCPINDEX had no gateway act in
    flight;
  - OG-tr-1 (Tax SMA route) LANDED 3a7d6a7dc8 (18:50Z); the hold was lifted (MSTR~Z msg 28035).
- **Served regression reads after each foreign release,** through this seat's principal session:
  - on 0a1d9079c6 (16:24Z) and on 3a7d6a7dc8 (18:54Z), BD fees -> `blackdiamond_list_fees` and ETF ->
    `etfs_get_positioning`;
  - the ETF `served_written_at` read MEASURED through the G-RDR HEAD.
  - MX-r-8's served change survives both releases.
- **Sequenced with 2.0.0_SA_COO~MP** (msg 27962): MCPORTAL G-CLOSE, which narrows Alyssa's rev-2 grant, is held until
  r6.J1's exchanges are captured. This seat owes ~MP two lines: the sitting time, then "captured".
- **Not ours** (MSTR~Z msg 27919): the 14:01Z `inf-etf-ownership-daily` invokes. This seat's only live worker in that
  window did read-only BD/SSM reads.
- **Round-7 release input** (COO~O msg 28039): a gateway release on 3a7d6a7dc8 must export
  `OG_TAXSMA_WORKBOOK_IDENTITY`, handed off-repo by ~O. The mail sender table now reads host-side (no export).

## Next

- About 00:1xZ 2026-10-02: read bd-silver-merge's unrealized SUMMARY; close the `nfra-mcpindex-r6-bd-merge-retire`
  ledger and MX-s-16; release the CVO's held slug.

## Compiler Tools

- None. The reads were `opal_discover` live and S3 git-ref.
