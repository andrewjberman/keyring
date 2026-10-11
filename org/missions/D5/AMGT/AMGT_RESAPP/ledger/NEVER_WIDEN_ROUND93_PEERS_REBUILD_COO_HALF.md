# NEVER-WIDEN CO-SIGN -- COO HALF. Round 93, `AMGT-ss-6`: the peers objects rebuilt so no subject lists its own company

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~11:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND93_PEERS_REBUILD_CTO_HALF.md`. Applier: `0.7.0_AE_CloudOps~RA1`. Order:
`task-orders/AMGT_RESAPP.TO-AMGT-ss-6.rebuild-the-peers-objects-without-the-self-peer.md`. Source: CTO round-92 analysis @1edd8be57d item 3 (row D1-S21).
Written from a member-by-member DRY BATCH of the merged code (nothing written): evidence `round93_prep/PEERS_BATCH_DRYRUN_20261011.json` and
`round93_prep/PEERS_BASELINE_20261011.json` (the 243 live routes' members before).

## THE ACT

ONE batch over the 243 MEASURED subjects, from a checkout at the GO's pin (carrying `AMGT-ss-3` @3318cd4e85 and `AMGT-qq-2`; `AMGT-ss-5` landed or in the same window):
`python -m lib.research.api.peers_rebuild --as-of <date> --write-as-of <a partition that sorts AFTER 2026-10-11T0707Z> --write-pool` (the caller above the peers
package that builds the held-name index once; `python -m lib.research.peers.engine` runs WITHOUT the rule). It writes `peers/v1/<security_key>/<partition>.json`,
243 NEW objects; every reader picks the latest partition by string order. No existing object is overwritten.

## THE INSTRUMENT AND ITS CONTROL

`engine.run_batch(..., write_pool=False)` on the merged tree, universe = round 91's pp-3 cache (byte-equal to `AMGT-ss-5`'s expected object: SHA-256 `8e652b08...`),
the held-name index from `scoped_amgt._held_name_index()` (107 tokens). **Control arm:** the same batch WITHOUT the index reproduces the live objects' member lists for
**243 of 243** subjects (so the instrument is the producer's own, and the only moving input is the rule).

## EXPECTED OUTCOME -- member by member

**243 subjects. 231 member lists byte-equal; 12 change. Member count is unchanged for all 243** (a removed member is backfilled by the next ranked candidate).

### Class A -- the CTO's ten: the subject's own company is served as a member under another name string (removed, one backfill each)

| subject | removed | added (next ranked) |
|---|---|---|
| `BZLFY_US_Equity` | `B0744B` | `B4TH69` |
| `NOVN_SW_Equity` | `710306` | `ISRG` |
| `ORA_FP_Equity` | `517617` | `TKO` |
| `PBR_US_Equity` | `268236` | `713360` |
| `ROG_SW_Equity` | `710891` | `DHR` |
| `SAN_FP_Equity` | `567173` | `MDT` |
| `ST_SP_Equity` | `B02PY1` | `632217` |
| `TSM_US_Equity` | `688910` | `645026` |
| `UBSG_SW_Equity` | `BRJL17` | `PGR` |
| `ZURN_SW_Equity` | `598381` | `*BN` |

### Class B -- two MORE than the analysis named: the subject's own company's OTHER SHARE-CLASS line (removed, one backfill each)

| subject | removed (name) | added |
|---|---|---|
| `HEI_US_Equity` | HEICO Corporation Class A `HEI.A` | `NVT` |
| `JD_US_Equity` | JD.com, Inc. Class A `BKPQZT` | `SYY` |

`HEI.A` (HEICO Corporation Class A, a US line of HEICO's own) and `BKPQZT` (JD.com, Inc. Class A) are in the live sets today. The serve path does NOT
attach the subject's key to them (pp-1's exact-name arm refuses a Class or Series designator, its N8 guard, because the key's record would be another listing's), so
they are not "served key equals the subject's key" members of the CTO's census; the ranker's identity rule excludes them because the held NAME is the subject's own company.
That is the engine's own existing intent (`self_excluded_by_share_class_sibling`), but it is a widening of the analysis's ten to twelve and **the CTO rules it**: sign both classes,
or have `AMGT-ss-3` refuse a designator the way pp-1 does (these two then stay members and the table is ten).

### Class C -- 12 more subjects exclude a row from the candidate pool and the set does NOT change (the row was not among the 12 ranked)

| subject | rows excluded by identity (ticker, name) |
|---|---|
| `1299_HK_Equity` | `B4TX8S` AIA Group Limited |
| `2317_TT_Equity` | `643856` Hon Hai Precision Industry Co., Ltd. |
| `939_HK_Equity` | `B0LMTQ` China Construction Bank Corporation Clas; `B24G12` China Construction Bank Corporation Clas |
| `992_HK_Equity` | `621808` Lenovo Group Limited |
| `AMXB_MM_Equity` | `BMVRB7` America Movil SAB de CV Class B |
| `BBSE3_BZ_Equity` | `B9N3SQ` BB Seguridade Participacoes SA |
| `GOOGL_US_Equity` | `GOOG` Alphabet Inc. Class C |
| `ICICIBC_IN_Equity` | `BSZ2BY` ICICI Bank Limited |
| `ICT_PM_Equity` | `645581` International Container Terminal Service |
| `MER_PM_Equity` | `B247XZ` Manila Electric Co. |
| `OMAB_MM_Equity` | `B1KFX1` Grupo Aeroportuario del Centro Norte SAB |
| `RIO_LN_Equity` | `622010` Rio Tinto Limited |

`SAN_FP_Equity` (class A) also excludes `570594` Banco Santander, S.A. as "its own company": a mislabel in the held-name index (row `AMGT_RESAPP-D1-S23`: the served display name of
Sanofi is "Banco Santander S.A.", an ETF-classification name). It changes no set (a bank is never a candidate for a pharmaceutical set) and is named here so it is not read as a self peer.

### What else differs in the 243 new objects against the stored partition (full objects diffed, 243 of 243)

| top-level fields that differ | subjects | why |
|---|---|---|
| `as_of, denominators, vintage` | 177 | the clocks, and `denominators.self_exclusion_rule` gains the identity sentence and `self_excluded_by_identity` is an empty list |
| `as_of, vintage` | 42 | the new partition's own clocks (absent-basis subjects, nothing else moves) |
| `as_of, denominators, reason, vintage` | 12 | the clocks, the rule sentence, and a candidate row excluded by identity (the `reason` line's self count) |
| `as_of, denominators, members, reason, vintage` | 6 | class A/B above |
| `as_of, denominators, fit_denominators, members, reason, vintage` | 6 | class A/B above, the fit denominators counted over the changed set |

`subject`, `basis`, `rungs`, `csc_columns`, `identity` and `sa_candidates` are equal for 243 of 243 (not in any difference set). For the 231 unchanged subjects the whole `members` field is equal. The retained members' own fields inside the 12 changed sets were NOT diffed field by field here; the applier's member compare does (condition 3).

## WRITER CENSUS (N printed)

`peers/v1/<key>/<partition>.json`: ONE function, `engine.write_pool_object`; callers `run_batch` (the batch) and `main`'s single-subject path (without `--dry-run`).
**N = 1 function, 2 callers read** in `lib/`; scheduled producers outside `lib/research` were NOT enumerated, so the change-management sweep of every live worktree's open deploys
(condition 4) is the control. The route reads the stored object through `read_peer_set` and applies four decorators; none removes or reorders a member.

## BRANCHES

- **Branch 1:** exactly the table: 12 member lists change as listed, 231 equal, the member count equal for 243, only the fields in the diff table differ.
- **Branch 2 (STOP, and the new partition is superseded by a newer one built from the prior code, never deleted):** any subject whose member list differs from this table;
  any member FIELD of an unchanged member that differs; a member count that moved; `self_excluded_by_identity` naming a row the table does not; the rebuild refusing on the index.

## ROLLBACK -- stated honestly

The act writes 243 NEW objects at a new partition; this seat does not delete. If the CTO names a rollback, it is a NEWER partition built from the prior engine code (the
`python -m lib.research.peers.engine` command, no rule) from the same universe: readers then pick it by string order. The prior partition `2026-10-11T0707Z` stays whole.

## SEQUENCING (CTO half, rounds 91-92)

After (or in the window of) `AMGT-ss-5`; never in `AMGT-ss-4`'s window; the later act re-measures against the state the earlier left (the baseline is re-read on the GO day).

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-ss-3` @3318cd4e85 and `AMGT-qq-2` @9d4236533c; `engine.py` and `peers_rebuild.py` blobs at the pin are printed; the universe the batch reads is the pool object
   `date=2026-10-02` (digest `8e652b08...`) once `AMGT-ss-5` has landed, else the local cache (same digest).
2. Before: `r93_self_peer_census.py --write-baseline <file>` (the pair's before column, compared with `PEERS_BASELINE_20261011.json`), the single-subject dry run of the ten, a dry batch
   printed against this table (any difference from the table is a STOP); the prior partition's object count (243); the sweep of open deploys naming `peers/v1`.
3. After: `r93_self_peer_census.py --baseline <file>` reads `R93 SELF PEER CENSUS: YES` (S1-S4), the no-regression arm (`r89_peers_deployed.sh`, `r89_deployed_close.sh --want amgt-corpus-dossier/11`) YES,
   `r92_minor_unit_census.py` YES (currency unmoved), and the 243-subject member compare against the baseline prints each changed member (the table).
4. A change-management entry is opened before and closed after.

-- 2.0.0_SA_COO~R1
