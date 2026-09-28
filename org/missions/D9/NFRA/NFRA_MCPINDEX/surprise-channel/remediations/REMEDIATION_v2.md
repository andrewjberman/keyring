# NFRA_MCPINDEX -- surprise channel, REMEDIATION v2 -- THE ROUND-2 SLUG

Author: 3.0.0_SA_CVO~O. Round: v2. Fabric: site-z. Recorded: 2026-09-28T15:00:22Z. **Reader:** `1.0.0_SA_CTO~O`.

20 rows: 8 REMEDIATED and 12 OPEN. Two of the OPEN rows hold the live Black Diamond credential (Z-S29, Z-S31, owner
1.0.0_SA_CTO~O). This seat found the CURRENT value still at HEAD in 6 tracked files, 4 of them shell-script defaults.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "record-terraform-deploy.sh read lambda-source-map.json with the device default encoding, which mangled and then refused UTF-8 bytes on a cp1252 device.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S12",
      "commit 981d0e931c",
      "record-terraform-deploy.sh:259 and :340 at HEAD (encoding='utf-8')"
    ],
    "remedy": "Executed: the recorder's reads and writes are pinned to UTF-8.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-S43",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The ported asset-dim document fetched two scripts whose import closure was not in the firm bucket.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S43",
      "infra/aws/ssm/opal-bd-asset-dim-download.json@0ff972bc38 (staged producer tree)",
      "MX-s-11 complete (the generated 49F pin)",
      "step 2 ssm:0626f927, DELTA=0 per the MX-s-10 ask @471c840a0a"
    ],
    "remedy": "Executed: the closure is published (the MX-s-11 pin replaces opal_naming and the registry), and the document stages the tree.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T15:00:22Z"
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-S44",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The instance role had no GetSecretValue on blackdiamond/49f/session, so the REST pull died with AccessDenied.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S44",
      "MX-s-10 A4/A5 @1853736322, @64bb58d8b8",
      "live aws iam get-role-policy bd-exporter-ec2-role AdditionalPermissions: carries blackdiamond/49f/session (read before 14:56Z)"
    ],
    "remedy": "Executed: the ARN was added to the existing AdditionalPermissions statement through Terraform, and it is live.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T15:00:22Z"
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-S46",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A bare run of build_bd_assets_dim.py rebuilt the served dim from the frozen source and dropped 1,204 ids for 4m19s.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S46",
      "s3api versions: 12:04:24 83ae55e0 (10,937 ids) then 12:08:43 a218b3dd == 06:22:06",
      "the document refuses the bare path (no OUTPUT_KEY gives rc 92)"
    ],
    "remedy": "Executed: restored byte-exact; the document can no longer take the bare path. Not measured: whether a consumer read the regressed object in the window.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal_discover was not registered in registry._load_builtin_factories, so enabling it added zero tools.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W2-S1",
      "registry.py:61 at HEAD",
      "commit 2c25c4c831"
    ],
    "remedy": "Executed: the factory is registered.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "data_entitlement.classify returned None for the discover tools, so the OG-z-1 guard would deny them.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W2-S2",
      "data_entitlement.py:115 at HEAD"
    ],
    "remedy": "Executed: both discover tools are in data_entitlement's table.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "data_entitlement.classify returned None for the portal_index tools.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W3-S1",
      "data_entitlement.py:114 at HEAD (the 3 mdpf tools of the amended cell)"
    ],
    "remedy": "Executed for the 3 tools in scope; the other 7 left scope with the cell.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "portal_index was not registered in registry._load_builtin_factories.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W3-S3",
      "registry.py:60 at HEAD"
    ],
    "remedy": "Executed: the factory is registered.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-S22",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "record-terraform-deploy.sh:218 selects its JSON tool by one device's hardcoded bun path, so the recorder behaves differently per device.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S22",
      "record-terraform-deploy.sh:218 at HEAD"
    ],
    "remedy": "OPEN: derive the tool (command -v) instead of a device path, per CLAUDE.md's device-logic rule.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S24",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "convert_assets_to_silver.py:153 guards its numeric conversion with dtype == object, which pandas 3 read_excel does not produce, so price, coupon_rate and last_dividend would land as strings.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S24",
      "convert_assets_to_silver.py:153 at HEAD"
    ],
    "remedy": "OPEN, latent: the production runner is on pandas 2 today. Remedy: test is_string_dtype or is_object_dtype. The DS lane owns the edit (rule 13).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S29",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A superseded Black Diamond 49F password was committed in tracked docs and is on pushed history.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S29",
      "commit e6482c530c (redaction)",
      "this seat's scan: fingerprint 7c3755be9e80 reads 0 in tracked files at HEAD"
    ],
    "remedy": "OPEN: the literal is out of the tree; the history is unpurged, and rotation is Andrew's act.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-S31",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The CURRENT live Black Diamond password is committed in tracked files, four of them as the default value of BD_PASSWORD in the bd-exporter stepwise shell scripts.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S31",
      "this seat's scan at HEAD: fingerprint 161ff0eb3831 (len 11), 6 occurrences in 6 tracked files, listed in Z-C-S24; no value read from Secrets Manager or printed"
    ],
    "remedy": "OPEN: the literal must leave the 6 files (the defaults replaced by a Secrets Manager read), and Andrew rotates the credential. Disarms on both.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-S42",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The BD asset dim is current only by ad-hoc pulls; the scheduled path is the dead portal document.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S42",
      "MX-s-10 PHASE A complete (A6 @471c840a0a); PHASE B re-cut after the slug"
    ],
    "remedy": "OPEN until PHASE B makes the REST document DEFAULT and the 22:10Z scheduled fire lands (G1-G3 @73e884bbbb).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-S47",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The fees Playwright producer fails on the MFA error while its SSM document, which has no exit statement, records Success.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S47",
      "MX-s-10 ask @471c840a0a section 1.3 (retires that leg); the second half @73e884bbbb G3"
    ],
    "remedy": "OPEN until PHASE B's retirement lands. The REST runner stays the one bronze/fees writer.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The discover family's routing marks a whole channel on one keyword and returns matches in catalog order, so 0 of 3 dataset asks route to the dataset first.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W2-S8"
    ],
    "remedy": "OPEN: a ranking cell. The order bound made it a row, never a fix.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "catalog_entries emits portal_* rows under the silver-dataset header ('no S3 key'), so they are described wrongly and 4 mdpf objects carry two rows.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W3-S4"
    ],
    "remedy": "OPEN: give served portal objects their own emitter section, or a key field the C1 schema admits.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The check helper pytest_named reads 0 passed and 0 failed lines for tests that print through capsys.disabled().",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W3-S12",
      "deliverables/2.0.0_SA_COO~O/round2/checks/_root.sh"
    ],
    "remedy": "OPEN: match the verdict on its own line. The error runs toward FAIL, never a false PASS.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W4-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Black Diamond gold canonical_lots_unrealized and canonical_lots_realized have not been written since 2026-07-23.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W4-S2",
      "s3api list read by this seat today: newest 2026-07-23.parquet in both"
    ],
    "remedy": "OPEN: establish whether a live consumer reads them; retire or reschedule the producer.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W5-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit's stager runs git add -f on any declared path present on disk, so a git rm --cached removal cannot be committed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W5-S1",
      ".tools/commit_gate_lib.sh:95-110 at HEAD"
    ],
    "remedy": "OPEN: a removal verb in the stager. The tool's owner, routed by the issuer.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W7-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "record-terraform-deploy.sh's CHANGELOG.json writer (a temp Node script) fails with a SyntaxError inside a run that still exits 0.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W7-S2",
      "record-terraform-deploy.sh:570 at HEAD"
    ],
    "remedy": "OPEN: fix the generated script's escaping, or write CHANGELOG through the python path.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
