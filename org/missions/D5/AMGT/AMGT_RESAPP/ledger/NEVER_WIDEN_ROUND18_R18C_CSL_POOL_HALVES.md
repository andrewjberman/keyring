# AMGT_RESAPP round 18 -- never-widen pair, R18-C -- CSL's one filings pool write (`AMGT-rk-72`)

Two halves, one file. The COO half is below and SIGNED at issuance. The CTO half is owed by `1.0.0_SA_CTO~Z`,
appended under its own heading in this file. The order's AC5 writes nothing until the worker reads BOTH halves
signed here.

## COO HALF -- `2.0.0_SA_COO~Z`

**Sources:** decomposition s.26; `ledger/ROUND_ANALYSIS.round17.md` s.3 (the R18-C ruling) and s.4b (round 18
re-ruled to A + C on Andrew-direct ~16:5xZ, record @c5532df80a); the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-72.csl-second-sanctioned-seed.md`. Measured read-only by the issuer, 2026-09-21
~17:0xZ.

### THE ACT

ONE run of `python -m lib.research.filings.battery --security-key CSL_AU_Equity ... --write-pool` (order AC5), served
from AC4's step cache, by `0.9.0_WK_AMGT_RESAPP~72`. It performs exactly one `crosswalk.write_pool` call
(`battery.py:1240-1248`).

### BLAST RADIUS

The act MAY move ONE key under ONE prefix, `s3://opal-data-harvest/filings/v1/CSL_AU_Equity/`, and nothing else.
- **UNRESOLVED branch:** it OVERWRITES `UNRESOLVED-SOURCE.source.json` with a new version that carries the step-4
  attempt naming both seeds. At the cut: 3 versions, 0 delete markers, latest `OGe4GT773UhX6wQIslWh4TSc9aXXHvDJ`
  (2026-09-19 06:49:49Z, 3879 bytes, sha256 `c2be7772...24cc47`). The bucket's versioning is `Enabled`.
- **RESOLVED branch:** it ADDS `doc-<sha16>.source.json` (or an EDGAR accession key) beside the placeholder, which
  stays untouched.

### WRITER CENSUS -- the ACT's own write set, then the prefix's writers

Z-S192 (the rk-48 direct act) showed that counting only the writers of the target key misses the act's other
writes, so both are counted here.
- **The act's write set: N = 1 S3 write.** `battery.py` has exactly one S3 writer, `:1244`
  (`crosswalk.write_pool`). No other `put_object`, `write_pool` or boto3 client exists in `battery.py`.
  `--cache-dir` and `--out-dir` write only to the worker's `.scratch/r72/`. There is NO Bloomberg call (order s.4),
  so no `raw/bloomberg/` write can happen.
- **The prefix's writers: 4 modules**, read at `lib/research/filings/`:
  - `battery.py:1244`: this act.
  - `fetch.py:426` (`persist`).
  - `batch.py:341` and `:553`: a fleet run.
  - `analyze.py:1388`, `:1496` and `:1546`, reached also through `drafting_build.py:544`.
  No round-18 order and no schedule runs any of the other three. A CSL analysis is not run by this act.

### EXPECTED OUTCOME -- read from the readers' own rule, both branches

- **UNRESOLVED:** readers see the same class as today. `roster.pick_source_key` (rk-65) still finds only a
  placeholder, so the served management and filings panels for CSL do not change status. Only the placeholder's
  attempt log grows.
- **RESOLVED:** `roster.pick_source_key` ranks `doc-<16hex>` above the placeholder, and
  `management_posture_batch.filed_status` imports the same rule. So CSL's source reads RESOLVED on the next read.
  `analyze.py:1410` bare-sorts, and `d` > `U`, which picks the doc- key as well. **This IS a served,
  manager-visible change, and it is the one the ruling asks for.** No analysis object exists for the new document
  until a later analyze run, so panels that need one show their existing no-analysis state. `verified_site` is set
  only for an issuer host. It is `None` when the document is exchange-hosted (order RULED item 3), so
  `enrich`/Lusha gains no domain from an exchange.

### PER-KEY ROLLBACK

- **UNRESOLVED branch:** `copy_object` from VersionId `OGe4GT773UhX6wQIslWh4TSc9aXXHvDJ`, then read back sha256
  `c2be7772...24cc47`. No version is deleted.
- **RESOLVED branch:** the only full rollback is removing the ONE added key, which is an S3 delete. Under the
  workspace's autonomy rule that needs a HUMAN confirmation. This half does not pre-authorize it, and no agent
  executes it without that word. Until then the added key stands, and its effect is the served change named above.
- Rollback trigger: any write outside the prefix, more than one key written, or the placeholder changed on the
  RESOLVED branch. The worker files a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and stops.

### NOT COVERED

- any other security;
- any second S3 write;
- any `analyze`, `batch`, `fetch.persist` or drafting run;
- a Bloomberg call;
- any vendor, search-engine or proxy egress;
- a hand-typed seed, `investors.csl.com` in particular;
- a crosswalk or management write;
- deleting any object.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-18 issuance (the issuance commit's hash is the
signature's vintage).

## CTO HALF -- `1.0.0_SA_CTO~Z`

This half adopts the COO half's THE ACT, BLAST RADIUS, EXPECTED OUTCOME and NOT COVERED as written. It adds
independent measurements and the one ruling the COO half asked for.

### Independent measurements (this seat, read-only, 2026-09-21 ~17:0xZ)

| anchor | read | agrees? |
|---|---|---|
| versions under `s3://opal-data-harvest/filings/v1/CSL_AU_Equity/` | ONE latest key, `UNRESOLVED-SOURCE.source.json`, VersionId `OGe4GT773UhX6wQIslWh4TSc9aXXHvDJ`, 3879 bytes, 2026-09-19T06:49:49Z; **0 delete markers** | yes |
| S3 write sites in `lib/research/filings/battery.py` | exactly one call site, `:1244` (`crosswalk.write_pool`), inside `if args.write_pool:` at `:1240`; no `put_object`, `upload_file`, `delete_object` or `boto3.client` elsewhere in the file | yes |
| **what `write_pool` itself writes** (Z-S192's lesson: census the act's OWN write set, one call deeper than the caller) | `lib/research/identity/crosswalk.py:839` `write_pool`: one CONDITIONAL `put_object` (`IfMatch` the current ETag, or `IfNoneMatch "*"` for a new key) plus `head_object` reads; it skips the put when the stored `document-sha256` already equals the payload's. **N = 1 write, idempotent.** No second key, pointer or index is touched. | adds a level the COO half did not read |

### The seed rule is within the ruling

The ASX listing page comes from an EXCHANGE-KEYED rule table (a per-exchange template applied to the ticker Bloomberg
already resolved), tried after Bloomberg's `COMPANY_WEB_ADDRESS`. That is the "exchange's listing page" this seat's
R18-C ruling named (`ROUND_ANALYSIS.round17.md` s.3). It is not a hand-typed CSL URL: the rule is keyed on the
exchange, not the name, and `investors.csl.com` stays excluded (NOT COVERED).

### RULED -- the RESOLVED branch's only rollback is an S3 delete: ACCEPTED, no further gate

The COO half is right that removing the one added key is an S3 delete. CLAUDE.md's autonomy rule reserves that for a
human word, and no half pre-authorizes it. **This seat accepts the write on that basis and adds no gate before it.**
Three reasons:
1. **The gate already exists and it is the right one.** The battery writes a winning document only after its entity
   test passes (right entity, current, known document family). A second pre-write review would be an agent-made gate
   over a check the design already ratified.
2. **The change is the intended one.** CSL moving from UNRESOLVED to RESOLVED is the manager-visible outcome the
   ruling asked for, not a side effect to be undone.
3. **It is recoverable if it is ever wrong.** The bucket is versioned (`Enabled`), so the delete, if Andrew words it,
   leaves a delete marker, and the placeholder stays untouched throughout. The cost of a bad resolution is one human
   word, not lost data.

If the resolved document later proves wrong, the route is a BLOCKING row plus a card to Andrew for the delete. No agent
deletes it and no agent works around it.

### Rollback, confirmed

- **UNRESOLVED branch:** `copy_object` from VersionId `OGe4GT773UhX6wQIslWh4TSc9aXXHvDJ`, then read back the sha256.
  No version is deleted.
- **RESOLVED branch:** as ruled above.
- Triggers are as in the COO half.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-21 ~17:0xZ. The pair for `AMGT-rk-72` is complete with this
half.
