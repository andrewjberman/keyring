# AMGT_RESAPP round 29 -- never-widen pair, `AMGT-rk-113` (L-ID, the Lenovo identity pull) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at the round-29 issuance.** The rollback's byte-equal criterion binds the rollback run too, and the vintage-stamp move sits in the CTO half's blast radius (CTO msg 24310). The paired CTO half is written by `1.0.0_SA_CTO~Z`
at `ledger/NEVER_WIDEN_ROUND29_RK113_CTO_HALF.md` and signed against live reads (CTO msg 24261 Q5: *"I sign my half when
L-ID is cut"*). The order acts on neither half alone (its AC0).

**Sources:** PRD v0.23 s.12; CTO msgs 24257, 24261 (Q4, Q5), 24300 and 24307 (the rollback is without a delete, and
states its form); the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-113.lenovo-identity-pull.md`; its precursor `AMGT-rk-114`.
**Measured at the draft:** SITEZ `0972b8631c`, read-only. Where the worker's AC1 differs, the ROLLBACK TARGET is AC1's
snapshot.

## THE ACT

After `AMGT-rk-114` has drained, ONE command:
`python -m lib.research.identity.add_security --folder "Lenovo 992 HK" --bloomberg "992 HK" --as-of <today UTC> --write-pool`.
- **Before it:** AC0's login probe (`dapi_check.py`, 1 request on `SPX Index`) and the sized-pull print.
- **The pull:** 1 ReferenceDataRequest, `992 HK Equity` x 9 identity fields.
- **Deploy ledger:** `amgt-rk113-lenovo-identity`, opened before the pull and closed on the AC3/AC4 reads.

## BLAST RADIUS -- what the act MAY move, and nothing else

- **(B1) Lenovo's crosswalk record** gains an `identity` object (composite FIGI, FIGI, ISIN, SEDOL, LEI, website, CIK,
  exchange, name, field_errors, source, registered_at) and one `provenance.identity` line. Its `security_key`,
  `bloomberg`, `display_ticker`, `model_key`, `association_keys`, `exchange`, `share_class`, `source_row`, `resolution`
  and `raw_identifier` are UNCHANGED.
- **(B2) A new served-latest crosswalk key** `crosswalk/v1/<today>.json`: the SAME 96 records, with only (B1) differing.
  Document-level `as_of` becomes today, and `denominators` gains `"enriched": 1`.
  - Because EVERY reader loads the latest key, every served identity block's `crosswalk_vintage` and
    `crosswalk_source` (`scoped_amgt.py:1725-1732`) move from `2026-09-19` / `.../2026-09-19.json` to today's, FOR EVERY
    NAME, with no record content changing.
  - Warm Lambda containers keep the cached 09-19 document until they recycle.
- **(B3) One immutable identity bronze object**
  `bloomberg/harvest/bronze/identity/security_key=992_HK_Equity/<stamp>.json`. It has 0 production readers.
- **(B4) `lib/research/identity/registrations.json`** +1 row (`mode: ENRICH`, `resolution: MEASURED`), committed.
- **(B5) Quota:** 2 Bloomberg requests (1 probe on SPX, 1 pull on 992), 10 security-field points.

**NOT moved** (asserted by AC3 and AC4):
- the other 95 records, byte-equal (a local rebuild of the served 09-19 object is byte-identical at the draft);
- `crosswalk.resolve()`'s output for 992 and for every other form (it does not return `identity`);
- the coverage file, the harvester config and the key grammar;
- every model block, filing object, management document and peer set;
- the adapter code and artifact, IAM and the portal;
- every other S3 object;
- the posture file.

## WRITER CENSUS -- per written property

- **`crosswalk/v1/<date>.json`: N = 2 writers** -- `add_security._persist_registration_and_pool` (`add_security.py:168-194`)
  and the `crosswalk` CLI `main` (`crosswalk.py:964+`, `--write-pool`). Only the first runs in this act. The rollback uses
  the second.
- **`registrations.json`: N = 1 writer**, `add_security._write_registrations` (`:159-165`).
- **`bloomberg/harvest/bronze/identity/`: N = 1 writer**, `add_security._land_raw` -> `harvest.bloomberg.bronze_write`
  (`:139-156`).
- **Readers of a record's `identity`: 0 in production** (a `lib/` and `integrations/` census; test files only). Readers of
  the crosswalk document: every `load_crosswalk()` caller, all through `resolve()` / `record_for()` / `aliases()`, none of
  which projects `identity` except `record_for`, whose callers read other fields.

## EXPECTED OUTCOME -- read from the producer's rule, both branches

- **KEEP:** AC3 reads 95 of 95 others byte-equal, the record count unchanged, and Lenovo's non-identity fields equal, with
  each identity field present or recorded in `field_errors`. The new key stays served.
- **ROLLBACK:** any other record changed, the count changed, or Lenovo's non-identity fields changed.
- **UNRESOLVED branch** (Bloomberg returns a security error for `992 HK Equity`): add_security's `_finish_unresolved`
  writes an UNRESOLVED registration row. Under rk-114 that row carries no identity, and the ENRICH attach is a no-op;
  AC3 grades it. If it appends a record (count +1), that IS a rollback trigger.

## PER-KEY ROLLBACK

- **Crosswalk -- RE-PUBLISH THE PRIOR CONTENT AS A NEWER VERSION (CTO msg 24307). Never a delete, and NOT a VersionId
  restore.**
  - Measured: `opal-data-harvest` versioning is Enabled (the 09-19 key holds 8 versions, 0 delete markers).
  - But readers pick the latest DATED KEY (`crosswalk.py:806-830`, `sorted(keys)[-1]`), and this act writes a NEW key
    and never writes the 09-19 key. So today's key has no prior version to restore, and restoring 09-19's would change
    nothing served.
  - The steps:
    1. a NEW commit removing the ENRICH row from `registrations.json`;
    2. `python -m lib.research.identity.crosswalk --as-of <the UTC day the rollback runs> --write-pool`, which writes a
       document whose records equal AC1's:
       - on the same day, a newer version of today's key (IfMatch; the enriched version stays noncurrent);
       - on a later day, that day's new key, which becomes the latest;
    3. verify with AC3's comparison.
- **`registrations.json`:** the new commit in step 1.
- **Identity bronze:** immutable, with 0 production readers. It is LEFT and recorded; a removal would be an S3 delete,
  which needs a human word and is not covered.
- **No S3 delete in any branch.**

## NOT COVERED

- any second pull, or a sign-in submit (an attended act);
- any other name's registration;
- a crosswalk rebuild on any other date;
- a model-block derive -- including for the 12 non-December names rk-109 routes (CTO msg 24300), none of which this act
  derives;
- any adapter deploy.

The held branch `wk-amgt-14-50` is not read or named.

**Signature (COO):** SIGNED `2.0.0_SA_COO~Z`, 2026-09-22, at the round-29 issuance; the issuance commit is its vintage.
