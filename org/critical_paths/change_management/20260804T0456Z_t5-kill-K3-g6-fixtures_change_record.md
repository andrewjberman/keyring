# T5 DEAD-CONSUMER KILL K3 -- platinum/mdpf/_g6_fixture/* (4 objects) (change record + rollback note)

**Executor:** 0.7.0_AE_CloudOps~F | **Executed:** 2026-08-04T04:55:52-04:56:11Z | **Status:** CLOSED (verified)
**Authorization:** COO GO 042634Z (CTO split-gate 042600Z, Andrew categorical). Kill-list row 5 @b877dbc0f5.

## WHAT DIED
`s3://opal-data-portal-v2/platinum/mdpf/_g6_fixture/{fresh-all,mixed,one-missing,one-stale}.json`
(4 objects, written 2026-07-12) -- validation fixtures for the mdpf-freshness-checker G6 family.

## WHY DEAD
The checker family is doubly dead (Lambda torn down pre-07-29 T1.A-positive-controlled; Andrew ruled
TERMINATE 0343Z; its role killed this wave, K1). Fixtures for a dead checker: zero readers (comp-grep
sweep = builder-fixture script refs only). No live IAM references remain (the only grant naming the
prefix died in K1).

## MECHANISM + ROLLBACK
Versioned bucket: `delete-object` per key -> DELETE MARKERS (content recoverable by deleting the
marker version). Marker VersionIds:
- fresh-all.json: `_WFz8vX2Xj5uSMutMDPc6eww7DVzVqBx`
- mixed.json: `h8QMz3dGgp8qgqkwKBxmdMK.0sBn3n8S`
- one-missing.json: `AjONKosfp2ySczPZBh.z7dKXW_d5hljp`
- one-stale.json: `YauzJjL9Wds77h2js689VUaYcrc50e3G`
Rollback: `aws s3api delete-object --bucket opal-data-portal-v2 --key <key> --version-id <marker-id>`.

## VERIFY
Post-delete prefix listing EMPTY (measured 04:56Z). Access window: no S3 access logging exists on
this bucket + CF logging disabled (T5.A measured) -- stated honestly; reader evidence is the code
sweep + the dead checker family, not logs.
