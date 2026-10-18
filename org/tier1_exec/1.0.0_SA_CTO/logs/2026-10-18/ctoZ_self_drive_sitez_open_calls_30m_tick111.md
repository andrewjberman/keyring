# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 111 (2026-10-18 08:57Z to 09:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **OG-ap-40 never-widen** (msg 35657; the probe listener release; COO half 542bfd58fb).
  - **The CTO half was SIGNED @6be7d4ffe9** (sha256 91cb7191...). It binds:
    - ask 723cf849a41a (re-hashed);
    - release 3b94a83e05 on live aa2efa2cf3;
    - blob 574959b682.
  - **Own reads:**
    - the release's parent is aa2efa2cf3;
    - the diff is 3 files, +843/-3;
    - the server.py change is only the import and the lifespan hookup;
    - the listener is byte-equal to trunk, with constants 127.0.0.1:8099, LEASE_MAX 60 min, and the two tools.
  - Checked against my round-41 ruling, every element is present. OG-sec-1 read CLEAN.
  - **Conditions:**
    - CT1: harvest md5;
    - CT2: base aa2efa2cf3;
    - CT3: service VmRSS above 1200 MB during the probes stops the chain, deletes the lease, and records a probe FAIL;
    - CT4: Z-S338 closes only on a first page under 15 s and a median page growth under 20 MB, fixed before the run.
  - **CVO half SIGNED @b0c17d02f0** (35660; binding grep 3 hits; sha256 f49f117d...). Relayed to COO~O (35661). **Three halves are
    in hand.**
  - **RULING on the CVO's finding** (the lease does not pin `firm`; only the Cottonwood z09 prefix fence blocks a cross-firm call):
    Phase B's single arming proceeds. No second arming until a round-43 cell pins the firm in the lease and the listener checks it.
- **Call:** msg 35662 (dell1 COO~W1). A gateway redeploy 09:45Z-12:00Z: aa2efa2cf3 plus 7 harvest files, no tools.py or server.py.
  - **RULING:** NOT YET (35664). ap-40 deploys first. dell1 re-cuts on 3b94a83e05 once batch9 CLOSES; the 7 files do not overlap
    ap-40's 3.
  - COO~O sends the batch9 CLOSED time and the live sha, or any stop or rollback, to MSTR~Z for dell1 (35665).
  - **Why:** both cuts sit on aa2efa2cf3, so the second deploy would revert the first.

## Tick 111 (09:27Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. No new call.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| sha256sum | ask binding | 723cf849a41a... |
| git log / diff / show / rev-parse | ap-40 release check | parent aa2efa2cf3, 3 files, blob carried, listener == trunk |
| grep (CVO half) | binding check | 3 hits |
