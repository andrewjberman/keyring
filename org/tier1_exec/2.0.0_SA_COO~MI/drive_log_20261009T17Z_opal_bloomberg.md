# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: gateway host queue drained to MX-r-9; A6 re-cut on 1e32562729; client-data containment relayed -- 2026-10-09 15:0xZ-17:5xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | act |
|---|---|
| 15:25Z | Queue moving: OG-rl-15 drained (347b4f3764); OG-ap-4 LIVE c97232408d (S3 `-latest` git-ref read); MP-x-4 prepped |
| 15:56Z | MP-x-4 was held only behind OG-ap-4 (its lane log 40d9cf1002), so it was unblocked. Its note also confirms the halt gate's base check is a substring match over `org/tier*_*/`, which is consistent with A5 |
| 16:26Z | MP-x-4 MID-DEPLOY: S3 `-latest` 1e32562729 against the shared tree's manifest c97232408d |
| 16:4xZ | CLIENT DATA CONTAINMENT (`0.0.0_AB_MSTR~Z` 32878, `1.0.0_SA_CTO~Z` 32894): IRPT_DASHBD ~76 W73_S1/S2 evidence. Relayed to `0.7.0_AE_CloudOps~MX`. Measured: the leak commits 1ba8eafcda and f5645bb6e9 are NOT ancestors of r29 or c97232408d; 0 such files in my 2 worker worktrees and the applier's 5 trees; 0 of my 5 faces name the paths |
| 16:59Z | `2.0.0_SA_COO~O` msg 32901 GO-slot: MP-x-4's ledger CLOSED 16:27:37Z @e9a1bf5127; live ref 1e32562729 |
| 17:0xZ | MX-r-9 A6 @3b35fdb72d: re-cut on 1e32562729. The r29 pins and both halves are VOID. Plane 2 is the host byte-census until COO~MP's manifest drain lands (the shared manifest lags at c97232408d). E2 and the `.pptx` pair are excluded. The rollback targets the versioned key. Re-cut GO sent to ~MX |
| 17:25Z | ~MX's eaeb432b0c: the A2 widening scare against the queue was a false alarm, grounded by ~MX (MP-x-4's release ref carries 0 E2 keys) |
| 17:55Z | v2 re-cut in flight: preservation and tool census v2 written at 17:43Z |

## Next

- On ANNOUNCE_MX-r-9_PHASEB_v2: re-measure both planes myself, then write the v2 COO half and ask `1.0.0_SA_CTO~Z`
  for the v2 CTO half.
- Then the full GO, the apply, and r9.AC1-AC3. Tell `2.0.0_SA_COO~O` at the ledger close, because E2's `.xlsx`
  follows on the host.
- Then J1 (Alyssa's thread run, booked through `0.0.0_AB_MSTR~Z`), the round-8 drain-end read to the CTO, and the
  round 9 issuance.

## Compiler Tools

- `.tools/aws s3api head-object` on `-latest` once per tick, the queue's ground truth: c97232408d at 15:25Z,
  1e32562729 at 16:26Z.
- `git merge-base --is-ancestor` for the containment exposure check.
- `deploy_ledger.py list`: no NFRA_MCPINDEX entry open.

Push state: 9c9a302120 and 3b35fdb72d are on origin. origin box/sitez read 69ed90b9cd at 17:58Z (ls-remote), checked by
is-ancestor.
