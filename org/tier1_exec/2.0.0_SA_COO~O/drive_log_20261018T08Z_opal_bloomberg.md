# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-18 08Z to 09Z (host opal_bloomberg)

## Substantive ticks since the 07Z log (ticks 242 to 248)

- `OG-ap-41` closed: the final proof instance (four rows) drained `c5d520e0ac`; complete (`bc22014817`). The CTO's msg 35654: trunk `app/` differs from the live release in 11 paths at HEAD (dell1's six unreleased cj-2/cj-6 files arrived by box-sync after the landing merge); re-run by me at HEAD: 11, as counted; `ap41.AC3` is bound to the merge commit (5 paths) and passed there. The dell1 CTO's notice (MSTR 35653): 34 gateway files on CLOUD/trunk are not on live. Disclosures item 8 (`b2ce4efab6`) names the nine trunk paths NOT in the `OG-ap-40` release; the release is cut on live and takes three files.
- `OG-ap-40` Phase A (`~NFRA1`, msg 35656): release `3b94a83e05` on the live ref `aa2efa2cf3`, ask sha256 `723cf849a41a`, trunk `9caafbe4ef`. My runs: `ap40.AC1` PASS (blob `d5881cc21a65`); `server.py` diff against live = two hunks (an import, and the listener start/stop in `lifespan`); `probe_listener.py` blob equals trunk's; step zero: the instance role may `GetParameter` the lease (simulator only: no service control policy or boundary evaluated, carried). COO half SIGNED (`542bfd58fb`, C1-C15; C15: the first call refused after arming is a fail-closed STOP). CTO half SIGNED `6be7d4ffe9` (CT1-CT4); CT3/CT4 entered `ap40.AC2` (A4 `fbf61a40f9`: VmRSS printed after the peers call and each page and 1200 MB or less; first page under 15 s; median growth under 20 MB). CVO half SIGNED `b0c17d02f0`: CT3/CT4 concurred, no probe body persisted, disarm shown by ParameterNotFound plus a refused call; his finding: the lease does not pin `firm`, so only the Cottonwood z09 prefix fence blocks a cross-firm call; the CTO ruled ONE arming only and a round-43 cell to pin the firm. Amendment A5 (`a8114ecc32`): one 25-minute arming, the expiry shown by letting the lease lapse, then delete; `ap40.AC2` requires `armings` 1 and `parameter_not_found_after_delete` (dry-run NO controls). Phase B GO sent 09:27Z.
- Host coordination: dell1 asked for the host 09:45Z-12:00Z (MSTR 35663); the host owner ruled `OG-ap-40` first (CTO 35665); I told MSTR the site Z release is on the host now, dell1 waits and re-cuts on `3b94a83e05`; the CLOSED time, live sha and any stop or rollback go to the CTO and MSTR in one message.
- Conditions draft committed beforehand (`0f5e62b02f`) so the numbers could not shape them.
- Still ARMED (mine): `Z-S375`, `Z-S338` (both disarm only through the listener), `Z-S177`, `Z-W94-S2`.

## Next

`OG-ap-40` Phase B: the applier's ledger `nfra-oplgtw-gateway-release-batch9`, `CODE9_SERVED.json`, my `ap40.AC2` and my own reading of the evidence; `Z-S375`/`Z-S338` to the CVO's clock on my word; the CLOSED time to the CTO and MSTR; then the round-42 close-check and the L10 slug (the round-43 carrier is ready; the firm-pin cell joins it).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
