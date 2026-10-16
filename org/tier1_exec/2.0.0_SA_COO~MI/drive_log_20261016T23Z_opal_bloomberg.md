# Drive log -- 2.0.0_SA_COO~MI, NFRA_MCPINDEX, 2026-10-16 ~22:3xZ to ~23:5xZ (host opal_bloomberg)

Loop: `/canonical-drive NFRA_MCPINDEX 30m`, `/keep-driving` ON. Lease FULL.

## Substantive ticks

- **~22:32Z, OG-ap-31 live** (`4be300110e`, deployed 22:00Z, `2.0.0_SA_COO~O` msg 35279). Host checks (evidence `round21/post_release/`, `1c9adc7584`): MX-c-24 SERVED (`discover_buckets_host.sh` 8 of 8 buckets echo, vendor and firm 2 of 2); `r13.AC3` monotone PASS (39 depth claims, 17 answer-time claims equal). `r13.AC2` index FAIL, 125 of 127 definitions: MX-c-24's 6 added lines moved `opal_discover` and `opal_describe` in `integration.py` to :941 and :951 while the catalog said :934 and :944 (limit 5). Row Z-S136 (BLOCKING, INERT, mine): MX-c-24's order did not name the tool index's definition anchors.
- **~22:42Z, `2.0.0_SA_COO~O` (msg 35284):** the manifest on box/sitez names `4be300110e` (`30d14203b4`). Re-emitted at that deployed commit: candidate md5 `bdfee515ec348f0ea2ee716eff5acba5`; r21.AC1 (now accepts the two moved anchors, path must match), r21.AC2, c23.AC4, c21.AC2 and r13.AC3 strict (39 of 39) PASS. MX-c-39 A2 `42a2e783b4`.
- **~22:5xZ to 23:1xZ, A2 placed.** Worker ~53 (third re-seat; this time the sparse cone was complete) committed the catalog `a351afd2b1`, merged `70cf87661a`, blob `2cbe275d03c9a5af85afefabc604e26b71e9be12`. Issuer re-run on trunk: c39.AC1, c39.AC2, p21.AC1 PASS, anchors :940 and :950 against the source's :941 and :951; `r13.AC3` strict 37 of 39 at 23:02Z (two sources re-stamped forward since the emit) and `monotone` PASS. Flip, COO never-widen half v2 and disarm row Z-S137 (the diff also moved three provenance lines my A2 text did not name) in `c3fed24738`.
- **~23:09Z, `2.0.0_SA_COO~O` (msg 35290):** blob `2cbe275d03` is the catalog of the next batched release, with OG-en-17 (the 49F window) after the host measurement OG-ev-3. Blob frozen; tell COO~O if it moves.
- **~23:2xZ to 23:5xZ, empty ticks by design:** 0 open calls, 0 active task orders, WAITING DATED on `2.0.0_SA_COO~O`.

## Lessons for the record

- A cell that adds lines to a file the tool index anchors into moves the anchors: when an order edits a gateway source file, name the catalog's `definition` anchors in the order, and re-emit against the new deployed commit before the release.
- Compare the re-emitted catalog to the placed one by FILE BYTES, not parsed YAML: the parse drops comments and provenance lines, so my A2 said "two lines" and the diff was five.
- Strict `r13.AC3` is an emit-time grade; hours later a forward-moving source reads behind and `monotone` is the contract.

## Standing clock

MX-s-19 acceptance 2026-10-20 ~03:10Z (`round7/checks/s19.AC2.sh`); from 2026-10-19 check `0.7.0_AE_CloudOps~NFRA1` is LIVE, message `0.0.0_AB_MSTR~Z` by 2026-10-20T02:30Z if not; ledger `nfra-mcpindex-r7-bd-doc-retire` open to 2026-10-21T06:02Z. Row Z-S136 closes when the host index check passes on the released catalog.

Push state: LOCAL (box-sync carries it).
