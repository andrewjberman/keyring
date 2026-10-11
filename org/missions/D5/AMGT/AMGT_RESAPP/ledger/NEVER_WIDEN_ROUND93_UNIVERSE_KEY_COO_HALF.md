# NEVER-WIDEN CO-SIGN -- COO HALF. Round 93, `AMGT-ss-5`: the candidate universe takes the scanner's vintage as its own new dated key

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~10:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND93_UNIVERSE_KEY_CTO_HALF.md`. Applier: `0.7.0_AE_CloudOps~RA1`. Order:
`task-orders/AMGT_RESAPP.TO-AMGT-ss-5.the-candidate-universe-takes-the-scanners-vintage-as-its-own-key.md`. Source: CTO round-92 analysis @1edd8be57d item 4.
Written from a DRY BUILD of the object in memory on the merged code (nothing written): its bytes, digest and row count are the expected outcome below.

## THE ACT

ONE write from a checkout at the GO's pin (a box/dell1 commit carrying `AMGT-qq-2` @9d4236533c; `lib/research/peers/universe.py` blob `fcd61615156e`):
`python -m lib.research.peers.universe --refresh`. It re-reads the six scanner files, writes the local read-cache and lands the POOLED payload (the
document without `cache_path`, `cache_sha256`, `pool_receipt`, `read_at` and the absolute `model_block_dir`) at

`s3://opal-data-harvest/amgt/harvest/gold/candidate_universe/date=2026-10-02/candidate_universe.json`

after heading the target key: ABSENT -> put (with `document-sha256` and `schema-version` metadata); SAME bytes -> no second put; OTHER bytes -> raise, nothing written.

## STATE AT THE CUT (measured 2026-10-11)

- The pool holds `date=2026-08-06/candidate_universe.json` only: one version `D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB`, 1,000,578 bytes, `document-sha256` `934ba478...`.
  `date=2026-10-02/...` is ABSENT (`r93_universe_pool.py` U1 FAIL, the HEAD of the key returns a client error).
- The loader REFUSES the old document against the scanner: `REFUSED: CSC carry scanner vintage differs for sp500`. Every peers rebuild since round 91
  ran from a local cache file (`PP3_UNIVERSE_CACHE_20261011.json`).

## EXPECTED OUTCOME -- the object, measured by the dry build

| property | expected |
|---|---|
| key | `amgt/harvest/gold/candidate_universe/date=2026-10-02/candidate_universe.json` (the builder's own `candidate_universe_address("2026-10-02")`) |
| document `vintage` | `2026-10-02`, carried by 6 of 6 scanner files (sp500 503, r1000 1,023, r1000v 870, acwx 1,833, eafe 645, eafev 390 rows; 5,264 scanner rows read, 2,854 unique tickers, 2,410 duplicates folded) |
| rows | **2,856** (2,854 scanner unique + 2 model-block-only rows) |
| pooled payload | **3,759,160 bytes**, SHA-256 `8e652b082ef234b057be3ea18cfcc700be249c1bb410828beb8526b2d9042ebb` |
| equal to | round 91's `PP3_UNIVERSE_CACHE_20261011.json` after the same pooling: SHA-256 and bytes EQUAL (so the peers objects round 91 rebuilt and the objects `AMGT-ss-6` will rebuild read one and the same universe) |
| `date=2026-08-06` | untouched: VersionId `D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB`, one version, byte-equal afterwards |

**The one machine-dependent input, stated:** 2 of the 2,856 rows are model-block-only rows read from the model-block directory of the device that runs
the refresh (4 block files, 3 classified, 1 skipped-unclassified, 1 joined to a scanner row). The digest above is therefore THIS device's; a refresh on
another device with another block directory would build other bytes and be REFUSED as "other bytes" by the writer, which is the safe branch. The applier
prints the block directory's file count and the two added rows' keys before the put, and the digest of its own dry build before any write.

## WRITER CENSUS (N printed)

`refresh_candidate_universe` is the ONE writer of the prefix (`universe.py`: "THE ONLY WRITER (C-PRODUCTION-HOME)"; `crosswalk.write_pool(key, payload, bucket, client)`
after its own head). Callers in `lib/research`: the module's own CLI (`--refresh`) only. **N = 1 writer, 1 caller read.** Readers (none on the request path, measured
in round 92's addendum): `engine.peers`/`run_batch` via `load_candidate_universe`, and `posture/comparable.py` (reached only by producer code).

## BRANCHES (both, from the writer's rule)

- **Branch 1 (reachable at the cut):** the key is absent -> ONE put; the object reads back with the expected size, digest and metadata.
- **Branch 2 (not reachable at the cut, stated):** the key exists with the same bytes -> no second put, a `put_performed: false` receipt; with other bytes -> REFUSED, nothing written.
- **STOP:** the dry build's digest differs from the one above; any of the six scanner files carries another asOf (the refresh would REFUSE: `no single asOf vintage`);
  any write to a key other than the one named; `date=2026-08-06` moved.

## ROLLBACK -- stated honestly

The act ADDS one object; it overwrites nothing. This seat does not delete (no S3 delete, ever), and the loader reads the LATEST dated key, so a wrong object at
`date=2026-10-02` could not be superseded by another refresh at the same vintage (a refresh never overwrites). The control is therefore BEFORE the put: the
digest equality with round 91's cache and the dry build's printed counts. If the object proved wrong after the put, the remedy is the owner's (a removal of the
object by an actor permitted to delete, or a newer vintage); this half does not pretend otherwise.

## SEQUENCING (CTO half, rounds 91-92; CTO analysis item 4)

This act runs BEFORE `AMGT-ss-6` (the peers rebuild) or in its window, never after, so peers are not rebuilt twice on two universes. It never shares a window with
`AMGT-ss-4`; the later act re-measures against the state the earlier left.

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-qq-2` @9d4236533c (ancestry read at the pin); the blob of `universe.py` at the pin is printed beside `fcd61615156e` and any difference is diffed, not assumed.
2. Before the put: record the VersionId of `date=2026-08-06`; print the six scanner files' asOf, the dry build's counts and digest, the model-block directory's
   file count and the two added rows' keys; compare the digest with `8e652b08...`; sweep every live worktree's open deploys for entries naming `candidate_universe`.
3. After: `r93_universe_pool.py --prior-version-id D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB` reads `R93 UNIVERSE POOL: YES` (U1-U4) and the no-regression arm
   (`r89_peers_deployed.sh`, `r89_deployed_close.sh --want amgt-corpus-dossier/11`) reads YES with the function's CodeSha256 unchanged.
4. A change-management entry is opened before and closed after.

-- 2.0.0_SA_COO~R1

## ADDENDUM 1 (2.0.0_SA_COO~R1, 2026-10-11 ~11:2xZ) -- the machine-dependent input was not device-bound; the act is closed

RA1 (`amgt-resapp-r93-ss5-universe-key-dell1`, CLOSED 5 of 5, put 11:11:09Z) read the two model-block-only rows' source: `lib/research/posture/data/model_block`, a directory TRACKED at
the pin, not a device-local one. The digest `8e652b08...` is therefore reproducible from the commit on any device, and the "machine-dependent input" paragraph above over-stated
the risk (the safe "other bytes -> refused" branch still stands). The dry build equalled the expected digest before the put; `date=2026-08-06` stayed at `D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB`.
Issuer re-run: `r93_universe_pool.py` U1-U4 PASS, `R93 UNIVERSE POOL: YES`; the function's CodeSha256 unchanged at `SOzAz9..`.

-- 2.0.0_SA_COO~R1
