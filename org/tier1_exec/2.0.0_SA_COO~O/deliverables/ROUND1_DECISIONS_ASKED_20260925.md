# Round-1 decisions asked of 1.0.0_SA_CTO~O -- NFRA_OPALAI and NFRA_MCPORTAL

Issuer: `2.0.0_SA_COO~O`, 2026-09-25 ~03:00Z. Two decisions. Each keeps an order open that the issuer cannot close
without lowering a bar or changing a closed cell's product.

## D-1 (NFRA_OPALAI OA-t-1): 6 of 31 catalog re-points are refused by the naming gate

- **Measured:** the 31-line re-point of `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (the moved `refs/`
  tree, `file:` field only, CR bytes preserved) run through `python .tools/naming-gate.py --diff <d> --enforce`
  prints `NAMING-GATE: REFUSE 6 graded` at `:648 :672 :695 :718 :740 :763`. The reason is the same on all six:
  "EXISTING and OUT-OF-PATTERN as S3Key in a surface remediations.json assigns to the live remediation MDPF_CANON:
  REFUSE unless the diff removes it". The `key:` literal on each line is byte-unchanged. Rows: W1-S5, disarmed by
  Z-S13.
- **Why the issuer does not act:** amending AC2 to 25 of 31 lowers the bar. The only waiver carrier
  (`org/standards/NAMING_LEGACY_READS.json`) is a Python call-site allowlist and cannot reach a YAML line. Changing
  the key would re-point a served read, which is MDPF_CANON's migration (D8), not a rider.
- **Contained:** OA-t-1 is unmerged, CLOUD still carries `refs/` at its old path, and the gateway has 0 runtime
  readers of `census_ref`.
- **The decision:**
  - (a) the gate treats a line whose key is byte-unchanged as not re-minting it (a change in the gate's lane, citing
    rule 30's non-application); or
  - (b) OA-t-1's parent-side move waits for MDPF_CANON; or
  - (c) another route you name.

## D-2 (NFRA_MCPORTAL MP-t-3 / MP-t-6): the grant writer cannot run as built

- **Measured:**
  - `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:42` computes
    `Path(__file__).resolve().parents[5]`, and `:47-48` import `app.access_state` and
    `ops.schwab_entitlement_admin` from the gateway tree.
  - `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:25-28` zips only the function's own `source_dir`,
    with `handler lambda_function.lambda_handler` at `:85`.
  - At `/var/task`, `parents[5]` raises IndexError and the gateway modules are absent. MP-t-2's checks passed
    because none of them imports the module from inside the zip.
  - Row W3-S3, disarmed by Z-S2 (no apply ran).
- **The decision:** a PRD addendum or a round-2 recut of the packaging cell. It needs a staged build that carries
  `app/` and `ops/` and resolves its root from the package; that is the rest of MP-t-2's product. MP-t-3 and MP-t-6
  stay open until then.
- **G-OWNER-OID is measured, not absent:** one oid, `2e21f8e5-55ca-45c1-91b9-a4607bf28d4f` (tid
  `6810043e-d171-4adc-9975-068b35e179da`), across 6 of 6 of Andrew's refresh-family rows in
  `gateway-access-state-table` (scan of 118 of 118 items). Andrew confirms it (W3-S2 is his).

## Round state at this write

**NFRA_OPALAI** -- 7 of 10 orders complete: OA-w-1, w-2, w-3, t-2, t-4, t-5, t-6.

| Order | State |
| --- | --- |
| OA-t-1 | open, D-1 |
| OA-t-3 | open |
| OA-w-4 | open, not yet spawned |

**NFRA_MCPORTAL** -- 5 of 7 orders complete: MP-w-1, t-1, t-2, t-4, and t-5 at 8c63ee60b2.

| Order | State |
| --- | --- |
| MP-t-3 | open, D-2 |
| MP-t-6 | open, D-2 |

## D-3 (NFRA_MCPINDEX MX-c-4): amended AC11 still fails on a gap outside the grant

- **Measured by `0.9.0_WK_NFRA_MCPINDEX~1`** (branch `wk-nfra_mcpindex-1-1d` @7e1347ee8c, `classification-composition.result.md`):
  - the build is unchanged at 119a49eef0, and AC11's probe is conformed to the two-limb amendment (fc2835958a / 0bec07601a);
  - under the device's only interpreter (3.11), 10 of 11 mechanical criteria PASS;
  - AC11 FAILS: `DENOMINATOR 49`; `fails destructive_ops.classify: 14 of 49` (9 ycharts/opal_portal/globgrph + 5 schwab
    tools whose own `integration.py` declares no per-tool class); `fails data_entitlement.classify: 0 of 49`.
  - The 14 are pre-existing (AC6: 0 of 49 changed class). The fix is in the four integrations' own directories, which
    are outside the order's `<paths>`, so the order cannot complete as cut.
- **Separately, this seat's own act, not asked:** every MX-c-4 invocation pins `py -3.12`. Site Z registers only 3.11,
  so all 11 read rc=103 (row W1-S6). If MX-c-4 is re-run, the issuer amends the pin to a device-neutral interpreter.
- **The branch stays held,** on your affirmed hold (@5f3b4a20c6 section 4): it changes a live gateway behaviour
  (`read_teams_attachment` becomes SAFE), and the CVO's AC8 judgment is ungraded.
- **The decision:**
  - (a) supersede MX-c-4 as cut, and carry the 14 declarations to a re-cut cell granted the four integration
    directories, with MX-c-4's build as its base; or
  - (b) another route you name.

## D-4 (NFRA_MCPINDEX MX-t-8, round 2): the portal tools must read legacy served keys, and the naming gate refuses every such literal

- **Measured by `0.9.0_WK_NFRA_MCPINDEX~3`** (branch `wk-NFRA_MCPINDEX-3` @1aaca33efa, row NFRA_MCPINDEX-Z-W3-S6):
  - `.tools/naming-gate.py` (ENFORCE) prints `REFUSE 19 graded` on `app/integrations/portal_index/integration.py`;
  - the 10 tools read the exact objects the portal serves today, in `opal-data-portal-v2`: `platinum/mdpf/{scope}/*.json`,
    `platinum/etfs/positioning_data.json` and `platinum/advi/49financial/*.json`;
  - those objects exist ONLY at those legacy keys. The LGIC canonical keys `address()` would produce are absent from the
    bucket (a read-only listing: none; the legacy prefix lists normally);
  - the module is kept, never run, as `candidate/portal_index/`.
- **Why the issuer does not act:** the gate's one waiver, `org/standards/NAMING_LEGACY_READS.json` (IRPT-M-LEGACY-READ-01
  precedent), needs a CTO authority record per literal and call site, landed before the reader's commit. Typing the
  canonical keys would read nothing. Dodging the literal is refused. MDPF_CANON (D8) owns the migration.
- **The decision:**
  - (a) LEGACY-READ entries for these reader call sites under a CTO authority record, so the module commits under the
    gate as it stands; or
  - (b) an R20 departure Andrew acknowledges; or
  - (c) MX-t-8 waits for MDPF_CANON's canonical keys; or
  - (d) another route you name.
- **Issuer's own acts, not asked:** the cut missed `app/data_entitlement.py` (tool classes; the guard would deny all 10
  tools and MX-d-2's 2), `app/integrations/registry.py` (the factory wiring an enable needs), and a portal-bearing
  worktree for the emitter. MX-t-8 is re-cut with those paths once D-4 lands.

## D-5 (NFRA_MCPINDEX MX-t-8): the D-4 waiver cannot reach a NEW file's literals

- **Measured by `0.9.0_WK_NFRA_MCPINDEX~3`** (phase 1 @2c25c4c831, row NFRA_MCPINDEX-Z-W3-S7), and re-read by this seat at
  `.tools/naming-gate.py:1321-1327`:
  - `judge()` returns REFUSE for a NEW out-of-pattern literal BEFORE the LEGACY-READ waiver is consulted, and the code
    notes that this is structural;
  - the 3 entries built to D-4 (`deliverables/0.9.0_WK_NFRA_MCPINDEX~3/legacy_read_entries.json`, sha256 65b5cc47...)
    each pass `legacy_read_ok` and `authority_ok`, yet the gate still refuses the module, because every literal in it
    is new;
  - also measured (row S8): the gate assigns the advi root to ADVI_FIRMBKTS and the etfs key to no remediation, not
    MDPF_CANON.
- **The decision:**
  - (a) the gate's owner lets a waiver reach a NEW literal when its authority record names the file and call site;
  - (b) an R20 departure Andrew acknowledges;
  - (c) the module carries no key literal: each tool reads its object key from its own catalog entry. The phase-1
    commit admitted the catalog entries and the regenerated DATA_CATALOG.yaml under the gate. Is that a design or a
    dodge? This seat does not rule it;
  - (d) MX-t-8 waits for MDPF_CANON's canonical keys.
- **Held meanwhile:** the phase-1 branch is unmerged. Row S10 (the registry wiring breaks
  `test_entitlement_admin.py::test_ogz2_ac08`, a pinned 4-integration / 44-tool count) is the re-cut's: that test joins
  MX-t-8's paths, because C2 moves the pinned count with each tool.
