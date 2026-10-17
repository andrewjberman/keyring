# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 06Z (host opal_bloomberg)

## Substantive ticks since the 05Z log (ticks 125 to 130)

- `OG-ap-34` Phase B: the stand-in cannot reach the running service, so the CTO restated CT1 twice: Amendment 1 (a fresh-process chain with the service sampled beside it, 300 MB line) FAILED at +337 MB on the first full chain, and Amendment 2 (decision 35380, `@24bc48799d`) replaced it with a two-chain plateau test (second chain net growth 50 MB or less, host under 80 percent, no page over 55 s) and post-deploy triggers of host over 80 percent, service +700 MB over its baseline, or median growth over 20 MB per call after the first (adopted from this seat's proposal). Plateau test PASSED (second chain +24.9 MB, host peak 55.1 percent, longest page 34.2 s).
- `OG-ap-34` DONE: release `9d5b7125571520b977401634a01935924f4c9787` live, deployed 05:19:28Z, no rollback, ledger `nfra-oplgtw-gateway-release-batch5` CLOSED; `ap34.AC1` and `ap34.AC2` PASS (this seat's runs); host md5 139 of 139, 27 of 27 tools, `tools/list` 103, 65 env keys; the 30-minute read-back: 31 probes, 0 triggers, service 113.5 to 132.2 MB, host max 52.1 percent; the service served ZERO window calls (the service's own heap over a full chain is unmeasured, disclosed; `memory_basis` fresh_process). Status flipped complete (`dc076cc44f`). Phase C added (the CVO's page-chain bodies, untracked client data) and `OG-ap-33` (landing the HVST line) re-pointed to the live release; both GOs sent 06:09Z. MI and MP told the live commit.
- Rulings: Z-S314 (Z-S352: `transaction_id` is not a row key, resolved by `OG-en-15`), Z-S350 (Z-S353: the windowed client tools run on the event loop and hold up every route for a page's 22 to 34 s; carried to the round-41 enrichment list: run them off the loop in a worker thread), Z-S312 disarm word to the CVO (Andrew's three routes clear), Z-S351.
- `OG-ap-32` closed SUPERSEDED (`ad05c0a218`). Still ARMED (mine): Z-S338 (until a real window call runs under the live release and memory holds), Z-S177 (a real 429), Z-W94-S2 (the hashed account-id list: MSTR will not mint it; the CTO is asked who produces it), Z-S336.

## Next

Phase C bodies at the CVO (re-grade of `OG-ap-31` AC3 and `OG-ap-34` AC3); `OG-ap-33` merge and MSTR carrying it to origin; Z-S338 disarm on evidence; the round-40 L10 slug once every order is terminal and every BLOCKING or ARMED row is dispositioned; the round-41 enrichment list for the CTO (event-loop blocking tools, the per-partition prefix listing Z-S328, the allocation weight unit Z-S313, the 429 limit Z-S177, the browser-exemption roster Z-S322).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
