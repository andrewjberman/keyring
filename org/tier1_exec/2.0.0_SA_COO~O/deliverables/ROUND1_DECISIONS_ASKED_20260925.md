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
