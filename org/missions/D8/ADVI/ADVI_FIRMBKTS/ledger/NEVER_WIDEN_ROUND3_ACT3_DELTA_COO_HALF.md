# NEVER-WIDEN co-sign, ROUND 3 -- the COO half: window act 3, the DELTA COPY of the served platinum keys into `opal-data-49financial`

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~09:0xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-10`, with the issuer's
`deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_delta.py` (selftest 7 of 7; live read-only plan against the round 2 manifest:
absent 0, equal 52,910, differs 0, kept-newer 0, destination versioning `Enabled`) | **Read against:**
`ledger/NEVER_WIDEN_ROUND2_F7_COPY_{COO,CTO}_HALF.md` (round 2's copy, which never overwrote), `ROUND_ANALYSIS.round2.md`
section 2 item 1 and ADDENDA 4-5, `FB-f-1`'s compare | **The other half:** `1.0.0_SA_CTO~DELL1`,
`ledger/NEVER_WIDEN_ROUND3_ACT3_DELTA_CTO_HALF.md`. No act begins until both halves are files at HEAD, the CTO half reads
SIGNED, act 2 (`FB-f-9`) is `complete`, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| `s3://opal-data-49financial/advi/49financial/platinum/<table>/<partition>/...`: the keys a FRESH manifest of the 11 served classes of `opal-data-bd` names (about 52,910 at round 2; the fresh count is printed by `manifest --verify` and is the blast radius) | each key ABSENT at the destination is created; each key PRESENT whose size or ETag differs from the manifest, and whose `LastModified` is at or before the mode-move instant, is OVERWRITTEN with the manifest's source version (`CopySourceIfMatch` on the manifest ETag) | before: `plan --keep-newer-than <T>` prints absent, equal, differs, kept-newer, refused (denominator = manifest objects); after: the same plan prints `absent=0 differs=0 refused=0` | per key: destination versioning is `Enabled` (read live 08:2xZ); the prior VersionId, ETag and size of every overwritten key are written to `F7_DELTA_ROLLBACK.tsv` and fsynced BEFORE the first write; `rollback --record F --execute` copies each recorded version back over the key. A key created by the act has no prior version: its rollback is "absent again" and is NOT a delete this act performs (a delete needs Andrew's word: CLAUDE.md section 5) |

**What the act says in its own words (the CTO's F7 half, condition 3, and the FB-f-10 un-park condition 3):** this act
OVERWRITES keys at the new home that round 2's copy wrote (round 2's copy never overwrote one); the overwrite count is of the
order of 49,000, not a handful (49,110 of 52,910 source keys had changed since the round 2 manifest, read live); the blast
radius is the fresh manifest's keys and no other.

**The guard that makes order-of-operations safe (issuer's reading, stated for the CTO to rule):** once the mode is
`canonical` the producers themselves write the new home. A destination key that differs from the OLD-home manifest AND was
last modified AFTER the mode moved is a producer's write, fresher than the manifest, and is KEPT, never overwritten
(`--keep-newer-than <T>`, `T` = the instant the export was deployed; required, no default). The act is therefore safe if a
canonical chain ran before it; its intended order is still: the export deployed, the legacy chain's last write final, THIS
act, then the first canonical chain. If a canonical chain ran first, `DEST-VS-MANIFEST: EQUAL` cannot read EQUAL for the
keys it rewrote and the criterion is read from the plan line (absent 0, differs 0) with kept-newer printed.

**Writers of the named property, counted (N writers = N rules read).** The property is the content of a key under
`advi/49financial/platinum/`. LIVE: 2 writers: (1) round 2's copy tool `r3_f7.py copy` (never overwrites; its work is done:
52,910 present and equal), (2) the producers under `canonical` once act 2 has moved the mode (0 runs of it before the move;
its rule is `lib/platinum_dest.py destination()`, read). DECLARED by this act: +1, the delta tool (reads its own rule:
`classify()` in `r3_f7_delta.py`, whose selftest 7 of 7 names the four classes and the kept-newer guard). N printed: 3.

## What the act may NOT touch

`opal-data-bd` (read only: listing and `CopySourceIfMatch` reads), any key not in the fresh manifest, `gold/advi/` and
`_campaign/` of the destination (the D1-S2 residue bound: key counts before and after equal), the router, the registry, any
delete or lifecycle rule, the bucket's versioning, IAM, schedules. No alert.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** `manifest --verify` reads every key placed once by `address()`; the plan before reads
  `refused=0`; destination versioning reads `Enabled`; the rollback record holds one row per `differs` key and is fsynced;
  the delta runs to `DELTA COMPLETE` with `stale-source=0 errors=0`; the plan after reads `absent=0 differs=0 refused=0`
  (`equal` = manifest count minus `kept-newer`); the residue counts equal before and after; the CTO's exercised read
  (`compare` re-run with `FB-f-1`'s instrument) reads DEST-VS-MANIFEST EQUAL, or its differing keys are exactly the
  kept-newer set. The expected outcome is read from the tool's own rule, not predicted from the input's shape.
- **Branch B -- NOT SIGNED, the act stops:** destination versioning is not `Enabled` when any key differs (the tool
  REFUSES; nothing is written); `refused` above 0; a `stale-source` above 0 after two passes (the source changed under the
  manifest: a fresh manifest, never this one); any `errors`; a key outside the manifest written; the residue changed. On
  Branch B after any write the rollback record is replayed for the overwritten keys and the order stays open with a
  BLOCKING row. Keys the act created stay (inert; the router does not read them until act 4).

## Authorization

The actor's identity reads `opal-data-bd` and writes the destination prefix: `simulate-principal-policy` for it on the two
bucket-prefix ARNs reads `allowed` for `s3:GetObject`, `s3:ListBucket`, `s3:GetObjectVersion`, `s3:ListBucketVersions`
(source and destination) and `s3:PutObject` (destination), at the grain of the prefix ARN and NOT `*`, BEFORE the first
write; a Dell deny on a bucket named in the earlier acts' pairs does not extend here, and any `explicitDeny` is a STOP
(the identity is then the CTO's to name). No grant is created.

## What this half does not know (stated)

- Whether a canonical chain runs before the act; the guard covers it, the criterion's reading changes (above).
- The fresh manifest's count and the exact `differs` count: read at the act, printed before the first write.
- Whether `CopySourceIfMatch` produces 412s at volume (the producers rewrite the source only until the mode moves; after
  it the old home is quiet): `stale-source` is a count the plan prints and the act stops on.
- Objects over 5 GB would need multipart copy; the largest at round 2 was 11 MB (1 multipart-ETag object of 52,910).

## Provenance

`ROUND_ANALYSIS.round2.md` section 2 item 1 (the window's order) and ADDENDA 4-5; round 2's copy halves and `FB-f-1`'s
compare; the live read-only plan of 2026-10-11 (52,910 equal, 49,110 sources changed since); `r3_f7_delta.py` selftest. Push
state: LOCAL.
