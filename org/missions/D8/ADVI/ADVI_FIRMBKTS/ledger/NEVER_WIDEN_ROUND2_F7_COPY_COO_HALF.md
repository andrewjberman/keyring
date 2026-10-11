# NEVER-WIDEN co-sign, ROUND 2 -- the COO half: F7's COPY of 49 Financial's served platinum keys into opal-data-49financial

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~03:2xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-e-5`, by
`0.9.0_WK_ADVI_FIRMBKTS~8`, through `deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py` as
`arn:aws:iam::313476888478:user/cloudops-dell1-agent-user` | **Read against:** `deliverables/2.0.0_SA_COO~B1/round2/L5_FACTS.md`
section 3 and `ledger/ROUND_ANALYSIS.round1-addendum.md` @a7ef4d08ab sections 1 and 2 | **The other half:** `1.0.0_SA_CTO~DELL1`,
`ledger/NEVER_WIDEN_ROUND2_F7_COPY_CTO_HALF.md`. No copy begins until both halves are files at HEAD and the CTO half reads
SIGNED.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| `s3://opal-data-49financial/advi/49financial/platinum/{table}/{partition}[/{object}]`, EXACTLY the keys `lib/opal_naming.py address()` builds for a source key in the 11 prefixes `gold/artifacts/`, `gold/entities/accounts/`, `gold/entities/advisors/`, `gold/entities/clients/`, `gold/platinum/firm/`, `gold/views/`, `platinum/49financial/`, `platinum/accounts/`, `platinum/advisors/`, `platinum/clients/`, `platinum/firm/` of `opal-data-bd`. 52,910 keys at the cut (02:5xZ); the producers add a few dozen a day, so the ceiling is 60,000 | NEW keys only: each is created with a server-side `copy_object`, SSE AES256, `CopySourceIfMatch` = the ETag in the manifest (so only the listed version moves), and only if the key is ABSENT in a destination listing taken first. A key that exists is never overwritten | the manifest (`F7_MANIFEST.tsv.gz`: every source key with its size and ETag) is committed BEFORE the copy; `r2_f7.py compare` reads every key's size and ETag at the destination against it | the new keys are INERT: no router, guard or grant reads `advi/49financial/platinum/` (the router reads `opal-data-bd`; F6 is built dormant and not deployed; the serving grant on that prefix is F4's and is not applied). "Put each back" is therefore to leave each in place. REMOVING a copied key is a delete on a versioned bucket and is Andrew's word, act by act (DEC-17); it is not needed to restore any behavior |
| `s3://opal-data-bd/**` | READ only (`ListObjectsV2`, the copy's `GetObject` by the service) | -- | none needed |

**Writers of the named property, counted (N writers = N rules read):** the property is the set of objects under
`s3://opal-data-49financial/advi/49financial/platinum/`.
- LIVE: 0 objects at that prefix at 02:5xZ (a full listing of the prefix, denominator 0; the bucket holds at least 1,000 keys
  outside it, `gold/advi/**` and `_campaign/`). The worker re-lists it before the copy and reports the count.
- DECLARED: 1 writer, this act. `comp-find 'advi/49financial/platinum'` reads 265 hits in 68,279 files; in first-party source
  3 files, none a producer (two LGIC_CANON naming exercises and the issuer's own instrument). A producer that builds the
  key through `address()` is not findable by literal, so the live listing is the instrument that counts: `compare` prints
  `extras-under-prefix`, and any key there that is not in the manifest is a NOT-SIGNED reading.
- Rules read: the placement is `r2_f7.py` `dest_for()` over the round-1 table's 11 `dest_pattern` rows (`mapping.json`); the
  builder arm refuses any key `address()` does not return byte for byte.

## What the act may NOT touch

Any key outside the prefix; any key that already exists; the bucket policy, lifecycle, notification, versioning or
encryption configuration; `opal-data-bd` in any way that writes; the router, the guard, CloudFront, a Lambda, Terraform; the
residue keys under `gold/advi/` and `_campaign/` (row D1-S2's ruling: R19, an existing pipeline's output). The act does
not make the new keys authoritative: the producers still write `opal-data-bd`, so the copy is a SNAPSHOT.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the manifest verifies (`placed = objects`, `refused 0`, `destination-collisions 0`); the
  destination listing before the copy reads 0 objects at the prefix; the copy completes with `errors 0` and `stale-source 0`;
  `compare` reads `COPY-COMPLETE` (missing 0, mismatch 0, extras 0); the residue counts under `gold/advi/` and `_campaign/`
  are equal before, after and now.
- **Branch B -- NOT SIGNED, the act stops and files a row:** any key refused or colliding; any destination key present
  before the copy (a second writer); `stale-source` above 0 (the producers are writing: the window is closed and re-cut,
  never forced); `errors` above 0; `compare` missing, mismatch or extras above 0; the residue counts moved. The
  `CopySourceIfMatch` and the absent-only rule make a partial copy safe to leave: a key that exists equals its manifest line.

## Authorization

`simulate-principal-policy` on the caller's own ARN reads `allowed` for `s3:PutObject` and `s3:GetObject`; the bucket's
`DenyForeignFirmPrincipals` admit list names `user/cloudops-dell1-agent-user` (L5_FACTS sections 2-3). The other three
statements concern the performance adapter only. No grant, role or policy is created.

## Provenance

ROUND_ANALYSIS.round1.md @4c9229fee2 enrichment item 4; addendum 1 section 1 (F7's bound) and addendum 2 @a7ef4d08ab;
DECOMP_R2 (this issuance); `r2_f7.py` run read-only at the cut (manifest 52,910 / 52,910 placed, 0 refused, 0 collisions;
compare: present 0, missing 52,910). Push state: LOCAL.
