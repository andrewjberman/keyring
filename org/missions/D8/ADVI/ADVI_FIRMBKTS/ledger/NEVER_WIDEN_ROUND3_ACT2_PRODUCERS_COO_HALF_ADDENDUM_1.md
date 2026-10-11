# NEVER-WIDEN co-sign, ROUND 3 -- the COO half, ADDENDUM 1 of act 2: the blast radius as built (phases A3 and A4 merged)

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~09:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-9` phase B | **Amends:**
`ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF.md` @12b22ef020 | **Read against:** the CTO half `..._CTO_HALF.md`
@03c1c6f001 and its ADDENDUM 1 @6ac66a8950, `ROUND_ANALYSIS.round2.md` ADDENDA 4 and 5, `ledger/R3_ACT2_OUTSIDE_READERS_CENSUS.md`
@2ca11d3951 | **The other half:** `1.0.0_SA_CTO~DELL1` (the one signed half names this addendum's subject in its ADDENDUM 1:
"the pair's blast radius is amended to name the read, list and delete sites alongside the writer lines").

**Verdict:** SIGNED for the blast radius below, which REPLACES the first half's permitted-set table and nothing else.

## The permitted set, as built (the whole of it)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| `s3://opal-data-bd/code/gold/` -- 19 `.py` objects: the 14 writers (`C_05 C_06 C_07 C_08 D_00 D_00b D_00c D_00f D_01 D_02 D_03 D_04 E_01 E_24`) and `lib/{platinum_dest,platinum_dest_view,gold_utils,helpers,etf_classifier}.py` | the dormant build (phases A, A2, A3) reaches the runner's code prefix: it ships by the push hook at the next CLOUD push; the act READS that it did and copies by hand only if the hook has not | `git diff --name-only 96f3212d22 HEAD -- data/black_diamond/scripts/gold`, non-test, `.py`: 19; each hashed against its S3 object's bytes: 19 of 19 equal | the prior object versions of each key (bucket versioning, read by the actor before the leg and recorded per key) |
| `s3://opal-data-bd/code/gold/gold_dispatch.sh` -- ONE object | the file as merged at `2018982711`: the PLATINUM-MODE block (one conditional export), the GATE-READ-LOCATION block (the freshness gate reads `header_metrics.json` through the seam), 19 comment lines of non-ASCII cleared (14 comments, 5 printed strings: each em dash became `--`) | the object's bytes equal the repository file's; `git diff` against the prior object is those hunks only (35 insertions, 20 deletions); the deployed bytes read back with `cmp`; 0 bytes above 127 | re-upload the prior object version (recorded): the export is removed and the same hour's run is legacy again |
| the producers' runtime behavior | a SCHEDULED PRODUCTION CHAIN run (`--chain`, not `--dry-run`, not `GOLD_KEEP_ALIVE=1`, not the QA rebuild marker, never overriding a mode already set): every served-class write, read, list and delete of the 14 writers and the lib modules they import follows `lib/platinum_dest.py` (census: 127 S3 data call sites, ROUTED 88, NOT-SERVED 36, EXEMPT 3, UNROUTED 0), and the freshness gate reads the new home | after the first such run: the new home's served keys carry `LastModified` after the move; the legacy home's 11 classes carry none after it (bounded listing per class, denominator printed); the gate's `data_as_of` read is the new home's | the export removed and the script re-deployed; the next chain run writes the legacy home again; the new-home objects already written are inert |

## What is read, counted and stated

**Writers of the named property (N writers = N rules read):** the property is the home a served key's write, read, list or
delete lands in. LIVE and DECLARED: 1 rule, `lib/platinum_dest.py` (`destination` for writes and deletes, `source` for reads
and heads, `list_target` for listings), reached by 66 writer lines in 14 scripts and 88 routed read, list and delete sites;
1 carrier of the mode (the export). N printed: 1 rule, 1 carrier. The outside readers are NOT in this act: the router and the
two Lambdas move as acts 4, 4b and 4c; monitors and QA are follow-ups (the census, classes ii and iii).

**Stated facts the CTO half's ADDENDUM 1 asked this half to carry:**
- E_01 writes no served key (3 of 3 objects outside every served prefix; last written 2026-04-07). E_24 has no launcher and no
  SendCommand naming it in 45 days (0 of 4,010; one residual StartSession): the CTO ruled it needs no carrier. **The act-2
  change-management entry says: a hand run of E_24 exports `BD_PLATINUM_MODE=canonical` or it writes the legacy home.**
- Row `D1-W23-S6`: the gate's search of `$(dirname "$0")` reaches `lib/` on the production path (`run_gold_layer.sh`); a direct
  invocation of the dispatcher on a fresh instance falls to the legacy gate read, which is today's behavior and costs one
  chain run, never a wrong served byte.
- Row `D1-W20-S1`: the legacy-copy PUTs (D_01 and others) now land at the canonical home under `canonical`; nothing is left at
  the legacy home for them, by the CTO's ADDENDUM 5. Row `D1-W20-S4`: log text beside routed calls names the pipeline bucket
  under `canonical` (display only).
- **The window's state between act 2 and the cutovers, stated:** the router (act 4), `exec-summary-generator` (act 4b) and
  `opal-partners-data` (act 4c) still read the legacy home, so users read the last pre-move day until those acts. Acts 2, 3,
  4, 4b and 4c close in one window; the CTO's ADDENDUM 1 forbids closing it, or running act 4, before 4b and 4c are routed.

## Both branches (unchanged from the first half, restated for the 20-object set)

- **Branch A:** the 20 objects equal the build and the dispatch diff is the named hunks; prior versions recorded for all 20;
  the next scheduled chain exits normally; every served write of that run is at the new home; the legacy home's 11 classes
  are quiet; no read or list of the run names a legacy served prefix; a QA, `--single`, `--group` or `--dry-run` run reads
  its mode unset.
- **Branch B -- the act stops and rolls back:** any object differs from the build; the dispatch diff is more than the named
  hunks; a non-chain or QA run reads `canonical`; a served write appears at the legacy home after the move; a write lands in
  neither home; the chain exits non-zero on a mode error (`ValueError`, `NoSuchKey` on a served read); a read or list names
  a legacy served prefix. Rollback: the export removed and `gold_dispatch.sh` re-deployed from its recorded prior version,
  the same hour; the order stays open with a BLOCKING row.

## What this addendum does not know (stated)

- The producers' next scheduled start and that no run straddles the move: read by the actor from the runner's schedule
  immediately before the leg (`comp-schedule`).
- Whether the push hook has already shipped the 19 `.py` objects (it ships at a CLOUD push; the dormant build's push state is
  the integrator's): the actor reads each object's hash before any copy.
- Non-Python readers by instrument, cross-module constants and 97 BD-named files with dynamic keys (the census's own
  statement): not shown to read no served key.

-- 2.0.0_SA_COO~B1
