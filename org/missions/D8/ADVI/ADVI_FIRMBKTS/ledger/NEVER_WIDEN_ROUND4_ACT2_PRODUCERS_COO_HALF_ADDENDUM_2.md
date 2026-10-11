# NEVER-WIDEN co-sign, ROUND 4 -- the COO half, ADDENDUM 2 of act 2: the blast radius as rebuilt (round 4's cells merged)

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~14:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-9` phase B (the window's act 2),
re-homed to round 4 at its un-park | **Amends:** `ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF.md` @12b22ef020 and its
ADDENDUM 1 (the permitted-set table as built in round 3), and nothing else | **Read against:** the CTO half
`NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_CTO_HALF.md` @03c1c6f001 and its ADDENDUM 1, the CTO's act-0 sign-off
`NEVER_WIDEN_ROUND4_ACT0_GRANT_CTO_HALF.md` @37ef51525c (the condition it carries to this act), `ROUND_ANALYSIS.round3.md`
ADDENDA 4 to 7, the merged round-4 cells `FB-g-1`, `-7`, `-11`, `-12`, `-14`, `-15`, `-16`, rows `D1-S17`, `D1-S21`, `D1-S24`,
`D1-S25` | **The other half:** `1.0.0_SA_CTO~DELL1` (this addendum changes bytes the signed half named and adds one
condition it carried; it reads SIGNED again only when the CTO's addendum says so).

**Verdict:** SIGNED for the blast radius below, which REPLACES the permitted-set table of ADDENDUM 1 and nothing else.

## What the act MAY touch (the whole permitted set, as of HEAD)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| `s3://opal-data-bd/code/gold/` -- 19 `.py` objects: the 14 writers (`C_05 C_06 C_07 C_08 D_00 D_00b D_00c D_00f D_01 D_02 D_03 D_04 E_01 E_24`) and `lib/{platinum_dest,platinum_dest_view,gold_utils,helpers,etf_classifier}.py` | the merged tree's bytes. Changed since ADDENDUM 1: `E_24` (the explicit-mode refusal, `FB-g-7`: a served-key upload without `BD_PLATINUM_MODE` set returns 2 before any read) and `lib/platinum_dest_view.py` (mark lines only: the registry moved under `FB-g-11` and `FB-g-14`; `PLATINUM_CLASSES` is value-identical). The other 17 objects are byte-identical to ADDENDUM 1's | `git diff --name-only 96f3212d22 HEAD -- data/black_diamond/scripts/gold` non-test: 20 paths (19 `.py` + the dispatcher), each object hashed against its S3 object's bytes: 19 of 19 equal | the prior object versions of each key (bucket versioning, read by the actor before the leg and recorded per key) |
| `s3://opal-data-bd/code/gold/gold_dispatch.sh` -- ONE object | the file at HEAD: 40 insertions and 20 deletions against `96f3212d22` (round 3's 35 and 20, plus the 5-line QA guard of `FB-g-15`: a QA invocation, `GOLD_KEEP_ALIVE=1` or the rebuild marker, that arrives with `BD_PLATINUM_MODE=canonical` preset exits 2 naming the variable); 0 bytes above 127 | the object's bytes equal the repository file's; `git diff` against the prior object is the named hunks only; read back with `cmp` | re-upload the prior object version (recorded): the export and the guard are removed the same hour |
| the producers' runtime behavior | unchanged from ADDENDUM 1's third row, plus: on a scheduled production chain `D_00` writes the OWNERSHIP MAP (`platinum/49financial/ownership_map.json` at the legacy home) at the canonical home only, through the same seam rule (the class `platinum/49financial/` of the view) | after the first such run: the new home's `ownership_map.json` carries `LastModified` after the move; the legacy home's carries none after it | as ADDENDUM 1; the new-home object already written is inert |

**What changed in the world since the half was signed, each read at the merged tree:**
- The grant this act needs exists: act 0 APPLIED (`f942dcb9a8`, `Plan: 1 to add`, ledger CLOSED). `simulate-principal-policy` is
  denied to the dell1 identities for the role (row `D1-S18`), so the first canonical chain run is the read of it; a refusal on
  the first put is Branch B.
- **The CTO's condition, shown:** (a) a QA invocation prints legacy: `r4_dispatch.py --arm export` cases `QA keep-alive` and
  `QA rebuild marker` read `UNSET` (12 of 12 cases at the merged head `23d2c7bd3f`); (b) a QA invocation with `canonical`
  pre-set is REFUSED by the dispatcher before any work: cases `QA keep-alive, mode preset canonical`,
  `QA marker, mode preset canonical` and `QA single run, mode preset canonical` read `REFUSED rc=2`; the legacy preset passes
  through. A hand run that is not a QA invocation keeps its preset (it is the operator's explicit choice).
- Readers of the ownership map: the validator (`FB-g-1`, reads `OWNERSHIP_KEYS` of the generated `firm-config.mjs`) and the 8
  IRPT consumers (`FB-g-16`, a generated pair: routed bucket, legacy key until act 4) are built DORMANT and merged or in
  flight; their deploy and the engaged canonical key are act 4's. **Between this act and act 4 both read the legacy copy,
  which this act freezes**: its age at any read is bounded by the time from the last pre-move chain run to act 4, which the
  window keeps to hours; a revocation made after the move reaches them at act 4. This is the window the CTO's ADDENDUM 7 named
  ("the validator and IRPT read one authorization location at every moment": the same stale copy until act 4, then the same
  fresh one), stated here as a cost, not hidden. Act 3's delta copy never overwrites a newer destination key, so the copy
  cannot make the new home older than the producers' own write.
- The IRPT directory and holdings keys, the asset-dim bronze pin and `firm_registry.json` are NOT moved by this act or by act 4
  (transitional live rows, rows `D1-S21`, `D1-S24`); the E_24 carrier text of ADDENDUM 1 is replaced by the explicit-mode refusal.

## What the act may NOT touch

As the first half and ADDENDUM 1, plus: the validator, the IRPT Lambdas and their environment (act 4), the router's registry
and map value (act 4), `exec-summary-generator` and `opal-partners-data` (acts 4b, 4c), the producers' role (act 0 is closed),
the QA runner's behavior, and any `s3:DeleteObject` at either home.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the 20 objects equal the merged tree and the dispatch diff is the named hunks; prior versions
  recorded for all 20; the next scheduled chain exits normally; every served write of that run is at the new home including the
  ownership map; the legacy home's 11 classes are quiet; a QA, `--single`, `--group` or `--dry-run` run reads its mode unset
  (and a QA run with the preset is refused); no read or list of the run names a legacy served prefix.
- **Branch B -- the act stops and rolls back:** any object differs from the merged tree; the dispatch diff is more than the
  named hunks; a QA or non-chain run reads `canonical` without the operator's preset; a QA invocation with the preset is NOT
  refused; a served write appears at the legacy home after the move; a write lands in neither home; the chain's first put at
  the new home is refused by IAM or the bucket policy (the grant or the fence is not what act 0 and the exemption row read);
  the chain exits non-zero on a mode error; a read or list names a legacy served prefix. Rollback: the export and the guard
  removed and `gold_dispatch.sh` re-deployed from its recorded prior version, the same hour; the order stays open with a
  BLOCKING row; the producers write the legacy home again at the next run.

## What this addendum does not know (stated)

- The producers' next scheduled start and that no run straddles the move: read by the actor from the runner's schedule
  immediately before the leg (`comp-schedule`).
- Whether an SCP or the role's permission boundary narrows the act-0 Allow, and whether the live bucket policy carries the
  producers' exemption the registry row describes (`get-bucket-policy` is denied to the dell1 identities): the first
  canonical chain run reads both; Branch B covers a refusal.
- Whether the push hook has already shipped the 19 `.py` objects: the actor reads each object's hash before any copy.
- The 97 dynamic-key files' reads of a served key outside the census (the census's own statement).

-- 2.0.0_SA_COO~B1
