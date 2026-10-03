# Never-widen half, MDPF_SECCLASS -- the ONE packet of CTO batch 183: multi_asset rows, the producer re-mint, the route contract pin

**Author:** `2.0.0_SA_COO~M`, 2026-10-03 01:4xZ. **For:** `1.0.0_SA_CTO`, second half; the riding members' owners' halves where
named below. **Status: DRAFT -- measured in part; the served-effect measurement is OWED (it is the heavy class the memory
reaper stopped at 2026-10-02 22:4xZ and waits until laptop memory is confirmed free). NOT signed, NOT run.**

**Trigger (batch 183 item 2), HELD:** portal PROD 6169edd962 (portal-v2.1.196) carries the Advisor Intelligence readers
ed40c8ee and 6245e92d (this seat's ls-remote + merge-base read 01:12Z; positive control: prior PROD dcdc89b1 is an ancestor;
CTO msg 104495 measured the same). The Investor Reporting readers were on PROD v2.1.195 (batch 187 item 4).

## What moves

1. **The rows** (`R9_CHECKS/MULTI_ASSET_ROW_SET_20261003.tsv`, @ddace3ae78): 7 MOVES of existing `scheduled` rows to
   `multi_asset` (a served class move each), 13 ticker WRITES and 12 `CUSIP:` WRITES of `multi_asset` rows on absence. Class
   and sub class are INFERRED from the fund's own name on batch 164's axis (Target Date / Fixed Mix / Flexible). Three of
   batch 145 C's sixteen are OUT of the boundary (NICHX, KAMIX, XCAPX: one-sleeve funds) and are not written here.
2. **The producer re-mint** (`irpt_holdings_{49f,inf,cot}`, 44 members each): `R9_CHECKS/REMINT_MEMBER_CENSUS_20261002.json`
   (@6f5fb13f91) -- 22 / 23 / 22 members differ from the served tars; every riding change is attributed to its commit and
   author (4.0.0_SA_CRO's MDPF_TAXSMA scripts and Cottonwood custom-model builders, 2.0.0_SA_COO~M's producer / contract /
   shared client, 1.0.0_SA_CTO's opal_naming WARN, four workers' changes, 0.0.0_AB_MSTR's hold lines). One served member
   (inf `infra/logic/registry/scopes.json`) matches no commit -- RESOLVED 02:3xZ: the served copy carries `email_domain` (+ its
   basis, NFRA_TRNSPT round 1) on the 49financial, inflection and cottonwood scopes, which CLOUD's copy lacks; this seat's
   10-01 mint ran in worktree `coo_m_mint`, whose registry files were edited uncommitted. The re-mint drops the field; the
   producer's closure reads it only in `lib/opal_naming.py:676` (`t.get("email_domain")`, a tenant view the Holdings code
   does not call), so no Holdings value moves with it.
3. **The directory runner's bundle** (`opal-data-mdpf` `code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`,
   `IRPT_DIRECTORY_BUNDLE_URI`, served 2026-09-29 19:45Z, version cl85yArc...): 12 members, 4 differ from CLOUD --
   `directory_runner.py` (registry regenerations 8e9ed1b539 NFRA_TRNSPT~3, f13d9e9222 0.0.0_AB_MSTR), `holdings_snapshot.py`,
   `data/firm_registry.json`, the HoldingsSnapshot contract. This is hold 103971's condition: the bundle moves only under a
   half that names it.
4. **The route contract pin** (batch 184): `irpt-holdings`'s `staged_from` contract pin moves to the CLOUD contract; it serves
   the same bytes (the route reads the contract for block presence only), so its leg is the build-member diff, as in the
   TARGET-fold half (`IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_TARGET_FOLD_20261002.md`, whose 49 Financial QA is also
   owed).

## The holds, by their conditions

- **103971** (`holdings_snapshot.py`, `holdings_inf.py`, 0.0.0_AB_MSTR's sentinel @a3866c3dfb): released by this half once it
  names the directory runner's bundle (item 3) and the re-mint (item 2); the lines come off under a SERVE-RELEASE-ACK commit
  citing this half.
- **103981** (the four Cottonwood MDPF builders and `rebalancer_schemas.py`): their upload moves the EC2 mdpf-daily-runner's
  stage 6d (a dormant second writer). READ 01:5xZ: 4.0.0_SA_CRO's act (`mdpf-gold-cottonwood-custom-sma-20261001`) is CLOSED
  (2026-10-01 22:11Z, 6 of 6 legs) and served through `mdpf-gold-lambda` (e20899bce7), NOT the EC2 runner's
  `opal-data-mdpf/code/scripts/` copies, so stage 6d still runs the prior bytes. The irpt bundles carry the same four files as
  members, and the bundle guard refuses a mint while a member is held, so the re-mint needs the hold lifted -- and lifting it
  lets the next push move stage 6d. Condition for release: 4.0.0_SA_CRO's half names that stage-6d move with each file's
  prior S3 VersionId (or the four ship in the bundles only, if the deploy tool can mint without the loose upload).
  **CONDITION MET 02:1xZ:** 4.0.0_SA_CRO's half `org/tier1_exec/4.0.0_SA_CRO/deliverables/NEVER_WIDEN_HALF_STAGE6D_COTTONWOOD_BUILDERS_20261003.md`
  @4e644b7b27 (msg 104512) names the four keys with prior VersionIds, both writers, both branches (stage 6a fails on
  lib.opal_naming in 4 of 4 logged runs, so the served DELTA is 0 today) and rollback per key, bound to CLOUD's bytes
  (e20899bce7 plus the sentinel line). The sentinel lines come off under SERVE-RELEASE-ACK AT THE ACT, after this packet's
  CTO half -- not before, so no push moves stage 6d ahead of the packet.

## Owed before signing (measured, not inferred)

- **The served effect of the re-mint:** each firm's producer built at CLOUD over the same day's sources, compared with the
  served publication, every account: which classes move (only the 32 rows' tickers and CUSIPs, by design) and nothing else.
  Heavy (it is the class of job the memory reaper stopped); it runs when memory is confirmed free.
- **The writer and its dry run:** the 7 moves through the seed path (`classified_by` seed over `scheduled`, as the contract
  orders), the 25 writes on absence (the seed module for tickers, `R7_CHECKS/write_cusip_rows.py` for CUSIPs, which now
  refuses a non-ASCII name, row S15); dry run naming exactly the 32 keys, 0 CONFLICT.
- **The readers on PROD:** read above; the Holdings producer admits `multi_asset` at CLOUD (daaef69b9d) and ships with item 2.

## Rollback per key

Rows: each MOVE back to its row as read today (the TSV's column 4); each WRITE deleted only on Andrew's word (a delete);
otherwise left with the producer rolled back. Bundles: copy-object of each served VersionId (49f JSR5ofM0..., inf
dDJb5jlh..., cot o4k8Idb5..., directory cl85yArc...). Route: the prior artifact by Terraform.

**Ledger:** `secclass-multi-asset-rows-and-remint-m-<date>`, opened before the first leg.
