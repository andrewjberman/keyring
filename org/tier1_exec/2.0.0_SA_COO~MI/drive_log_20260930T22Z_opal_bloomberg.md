# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-09-30 20Z-23Z (host opal_bloomberg)

Lease FULL, round 5, limb L7. Thread y.

## Decisions closed this span

- **R20 entries landed** by 1.0.0_SA_CTO~O (msg 27365):
  - authority record @e692000c06;
  - carrier @0d71a22887, entries NFRA-MCPINDEX-R20-01..08, cutoff 2026-12-31, register rows X11/X12.
  - This un-holds MX-t-10, MX-t-13 and MX-r-7.
- **MX-t-10 COMPLETE.**
  - ~15 applied the frozen candidate 03a19ac282 as-is on CLOUD 7aba7bcc4d and committed @78ee79c3ba
    (`etfs_get_positioning`). The naming limb reports 0 REFUSE (3 DECLARED-EXCEPTION under X11).
  - Issuer re-grade: t10.AC1 5 of 5, t10.AC2 16 passed.
  - Drained @29a40f5d4c after waiting out peers' staged indexes; closed @26cc4e7252.
- **MX-t-13.**
  - ~21 merged CLOUD 7aba7bcc4d into wk-21 (@975832d5ad). The pre-commit took ~35 min: the surprise-row-gate corpus
    pass over 1,180 staged paths.
  - It then committed the cell @6ccbf91e1c (`blackdiamond_list_fees`, dormant). The 5 literals are admitted under X12
    with counts unchanged; equality re-proved on silver/fees/2026-09-29.
  - Issuer re-grade: t13.AC1 1 of 1, t13.AC2 4 of 4.
  - CLOUD moved (t-10), so ~21 is continued to sync CLOUD before the drain:
    - re-emit the catalog;
    - union the channel;
    - fix the registered-tool pin to 55 (both sides auto-merge to 54).
- **CTO rulings:**
  - msg 27367: the Schwab catalog row (discover: catalogued:false) rides the round-5 slug. This seat told the CTO that
    H2 was done @c9be59c0c7.
  - msg 27415: after MCPMSP applies its Opal-internal reader role, MCPINDEX routes portal_index and opal_discover
    through it. It is a next-round enrichment item.
- **COO~O msg 27389:** OG-t-2 PHASE A is on live 42c52ed4d9 and will be the next gateway releaser after its halves.
  MX-r-7 coordinates order with ~O before any PHASE B.

## State at 23:16Z

- Round 5 complete: MX-a-8, MX-s-15, MX-q-3, MX-t-10 (round-4 order).
- MX-r-6 is LIVE; its ACs PASS and J1 awaits Alyssa's cold run.
- MX-t-13 is committed; its sync with CLOUD is in flight.
- NEXT: MX-r-7 (BD + ETF release).
- HELD: MX-t-12 (to L10). Round 4: MX-s-14 (fires).

## Compiler Tools
- None. The reads were git, the round battery, the naming gate's `--diff`, and process and mtime liveness probes.
