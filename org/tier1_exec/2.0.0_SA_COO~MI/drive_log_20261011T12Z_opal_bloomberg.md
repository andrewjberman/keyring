# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: gateway slot taken; MX-r-10 v2 cut, both halves signed, full GO -- 2026-10-11 04:0xZ-13:0xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | act |
|---|---|
| 04:0xZ | Laptop CTO @de13ed0e00 (XB-b98e) also placed NFRA_CTLPLN CT-i-11 after OG-ap-6. Asked `2.0.0_SA_COO~O`, who answered (33173, CTO~Z ruling 33141): MX-r-10 goes FIRST, then CT-i-11 on our ref, unless we are not ready to cut at OG-ap-6's close |
| 05-11Z | Dated waits (owner ~O). `0.0.0_AB_MSTR~Z` GC 33248: answered DROP for `C:/tmp/mx-rel-r9` and `mx-dep-r9`. Shipped blobs equal d3c31e972e; 12 uncommitted files are CRLF-only, 0 content lines. MSTR archived both heads as tags on origin before removal (33250); `mx-dep-r10` kept |
| 12:05Z | OG-ap-6 ledger `nfra-oplgtw-gateway-release-e2` CLOSED @a54fa42da7. Live `6aadf7db37` (manifest + `-latest`) |
| 12:0xZ | Slot claimed: re-cut GO to `0.7.0_AE_CloudOps~MX` (A1); ~O told |
| 12:25Z | ~MX cut `c3af8687e4` on `6aadf7db37`. ANNOUNCE v2 @22923bd7f8: host 106/106 by hash, 2 files, `.env` 53=53, tools 67=67, ENABLED_INTEGRATIONS 7=7 |
| 12:5xZ | Issuer re-verify: parent `6aadf7db37`; 2 files +110/-15; blobs equal MX-c-7's (`d0bddad2f1`, `a8fd2fa900`); `deploy-to-ec2.sh` identical; deploy tree clean at the cut; rollback key `opal-gateway-6aadf7db37.tar.gz` 538772 B |
| 12:5xZ | COO half SIGNED and A2 (`<instance_path>` to ~MX's folder) @a6e212dfe8 |
| 13:04Z | `1.0.0_SA_CTO~Z`: G-A PASS and CTO half SIGNED @b51c82abe6 (33282) |
| 13:05Z | Base re-read `6aadf7db37`, no gateway ledger open. FULL GO to ~MX for PHASE B, with the label read-back before leg 1 closes (the Z-S92 lesson) |

## Next

- At ~MX's close: verify the label, host md5, /health and r10.AC1/AC2; drain the proof. Tell `2.0.0_SA_COO~O` the new
  live ref (CT-i-11 follows).
- Then: the round-9 one real run, round-close-check, and the L8 packet to `3.0.0_SA_CVO~Z`. FWD-19 is NOT done (both
  readers GAP).
- J1 HELD at Andrew. MX-s-19: s19.PRE on 2026-10-13 after 03:00Z.

## Compiler Tools

- `.tools/aws s3api head-object` on `-latest` and on the versioned rollback key; `EC2_MANIFEST.json` read.
- `git diff --stat`, `git rev-parse <rev>:<path>` blob equality, `git diff --quiet` on the deploy script.
- `unblock.py tick --wait-until --owner` for each dated-wait tick.
