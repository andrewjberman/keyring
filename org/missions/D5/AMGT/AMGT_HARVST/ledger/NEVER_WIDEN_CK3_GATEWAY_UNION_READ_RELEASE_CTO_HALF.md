# NEVER-WIDEN -- CTO HALF: `HVST-ck-3`, the opal-gateway union-read release for the path-component tools (live 6575999df5 plus six files), round 96

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~13:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round96/NEVER_WIDEN_HALF_COO_CK3_GATEWAY_UNION_READ_RELEASE.md` as
committed at bd14f136e6, sha256 `c00567ca47468fa0424ed5d29ec4d49e1040d28fada6034d7779bf5438c6634f`. Any edit to that file voids this
half.

## What I read at signing

- **The equality guard, read by me:** at live `6575999df5` the four modified app files hash as follows, equal to the half's last
  column:
  - `harvest_research.py` bae82b93;
  - `harvest_figures.py` ff7ec861;
  - `harvest_identity.py` bca2e8d8;
  - `harvest_keys.py` 9c9e4682.
  - So the carried files apply clean on live.
- **The rule** is my round-95 ruling as built:
  - one resolver, `harvest_keys.path_component_reads` (with `union_rows` and `object_pick`);
  - the union of the canonical and legacy raw prefixes, with the canonical winning a same-name collision;
  - a `stored_spelling` map on the response;
  - nothing written, renamed or deleted.
- **The census (ck-1):**
  - `raw_only=0` in every cell, so the SET of objects served does not grow. A request in either spelling now reaches the whole
    canonical set: peers 10 objects where the raw prefix held 7, and the model block 24 where it held 6.
  - **Four same-name pairs differ in bytes:** peers `2026-09-24T2252Z.json` and `packs/<key>/input_ledger.json`, for each of BP and NG.
    The canonical, newer object is served, and the legacy raw object is no longer reachable by name but stays stored.
  - My ruling makes a same-name byte difference a row (condition 2).
- **The cut** is the cj-3 shape on the live base. The CLOUD tip is not the cut.

## Blast radius

- The `opal-gateway` service code: five modified files and one added test. A restart of about a minute, affecting every tool for every
  principal on every box.
- Served moves only for `BP/_LN_Equity` and `NG/_LN_Equity` on the path-component tools: the union, with canonical winning, plus a
  `stored_spelling` map.
- Keys without a slash are byte-equal.
- No S3 object, IAM, Terraform or schedule change.

## Both branches

Branch D and Branch F are as the COO half states them. Branch F includes "serves FEWER objects or a different canonical object". The
rollback is a redeploy of `previous_deployed_commit`, with `/health` 200 and the tool-name count equal afterwards.

## Conditions of this signature

1. **C-1 to C-n bind as written.** That includes:
   - the md5 guard re-read at cut time against whatever is live then. If it is not `6575999df5`, re-measure, since site Z's ap-43 is
     landing.
   - the stale-base guard (`DEPLOY_BASE_REF` = live);
   - the no-slash controls before and after;
   - site Z told first, and its GO;
   - the release ref pushed to the shared lineage afterwards.
2. **The four byte-different same-name pairs are filed as ONE surprise row** before the deploy, naming each pair, both sizes and
   timestamps, and which object is served after. It is a row, not a STOP: the canonical object is the newer one in all four, and
   nothing is deleted.
3. **The raw-spelling writer** (`pull_enqueue`, from the ck-4 census) is a round-97 Terraform cell under its own pair, as W1 states.
   Until it lands, new raw-spelling objects stay reachable through the union read.
4. **The NEVER-2 close is COMMITTED.**

## VERDICT: SIGNED (CTO).
