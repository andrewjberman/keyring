# NFRA_OPLGTW -- the disarm clock for ten ARMED rows (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v38. Fabric: site-z. Recorded: 2026-10-17 ~01:5xZ.
**Input:** `2.0.0_SA_COO~O` msg 35301 (acked), the disarm owner's word and evidence:
`deliverables/2.0.0_SA_COO~O/DISARM_EVIDENCE_TEN_ARMED_ROWS_20261017.md` @40b24efc5e. The CVO writes the clock (R-15). The investigation
rows are append-only, so the clock lands here as a `disarms` row, as on `NFRA_TRNSPT-D2-C-S1`.

**This seat's checks before writing (~01:5xZ):**
- **The ten rows:** each reads `hazard_standing: ARMED`, `disarm_owner: 2.0.0_SA_COO~O` in `investigations/INVESTIGATION_v1.md`.
- **Their adjudication:** each is named by its adjudicating row, Z-S178 to Z-S187 in order, all `DISMISSED_WITH_REASON`, each reason
  naming the order that ended the hazard.
- **The ending orders:** OG-ap-8, OG-ap-9, OG-ap-10, OG-rf-1, OG-wr-1, OG-bd-2, OG-bd-3 and OG-db-1 each read
  `<status>complete</status>`.
- **Read live by this seat earlier today:**
  - OG-bd-3's `decide()` branch (at `3d5c9c8bf1`, my OG-ap-23 re-cut half) is live;
  - the transcript allowlist line is in the deploy script's env printf at `3d5c9c8bf1` (the OG-ap-23 ask);
  - both are ancestors of the live `4be300110e`.

**Not disarmed, as the owner states:**
- `Z-S312` waits on Andrew's real browser run.
- `Z-S177` needs a real 429 in the audit.
- `Z-W94-S2` is carried to the CTO.

They stay ARMED. **Denominator:** the owner read 13 ARMED rows; 10 are disarmed here and 3 remain.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S85",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Ten ARMED rows whose hazards ended by named, complete orders were never disarmed: the investigation rows are append-only, and the issuer's adjudicating rows Z-S178..Z-S187 dismissed them without the clock, so each still read ARMED.",
    "evidence": [
      "deliverables/2.0.0_SA_COO~O/DISARM_EVIDENCE_TEN_ARMED_ROWS_20261017.md @40b24efc5e (the owner's word and evidence)",
      "investigations/INVESTIGATION_v1.md rows Z-S178..Z-S187 (each DISMISSED_WITH_REASON, each naming its target and the ending order)",
      "task-orders: OG-ap-8, OG-ap-9, OG-ap-10, OG-rf-1, OG-wr-1, OG-bd-2, OG-bd-3, OG-db-1 read complete (this seat ~01:5xZ)",
      "OG-bd-3 decide() branch read at 3d5c9c8bf1 and the transcript allowlist in the deploy env printf at 3d5c9c8bf1, both ancestors of live 4be300110e"
    ],
    "remedy": "Each hazard ended by its named order: R50 send-gate live (Z-S67, Z-W35-S1); the grant-writer Lambda rebuilt (Z-W42-S1); both drifts applied (Z-W39-S5); the window primed, warm read at most 12.1 s (Z-W43-S7); the KMS statement and one key rule and the registry-first grant (Z-W49-S1/S3/S4); the allowlist on trunk (Z-S85); the tier rule live (Z-W57-S2).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "disarms": [
      "NFRA_OPLGTW-Z-S67",
      "NFRA_OPLGTW-Z-W35-S1",
      "NFRA_OPLGTW-Z-W42-S1",
      "NFRA_OPLGTW-Z-W39-S5",
      "NFRA_OPLGTW-Z-W43-S7",
      "NFRA_OPLGTW-Z-W49-S1",
      "NFRA_OPLGTW-Z-W49-S3",
      "NFRA_OPLGTW-Z-W49-S4",
      "NFRA_OPLGTW-Z-S85",
      "NFRA_OPLGTW-Z-W57-S2"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-17T01:55:00Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v38"
    },
    "closed": true
  }
]
```

## The remediation rows the slug owes (the row gate's rowlessness and precondition limbs; adjudication v38)

Three ARMED items graduated in `ADJUDICATION_v38.Z.md` (Z-C-S86), carried OPEN and ARMED with their owner's clock. Seven items whose
authors set GRADUATED with no remediation row, each read from its own text:
- five are fully remediated in that text;
- Z-S135 leaves one record for the issuer, so it stays OPEN;
- Z-S146's latent half is Z-S145's.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S177",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The gateway's per-identity limiter (120 per 60 s) answered 429 to site Z seats sharing one Opal identity and wrote no audit row, so the count that tripped it was unread.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S177",
      "OG-en-10 (the 429 audit row, event gw_ratelimit) live in bf9d23b518 and every later release"
    ],
    "remedy": "Read the gw_ratelimit audit rows of a real 429, then choose between raising RL_MCP_IDENTITY_LIMIT and splitting the shared identity, as the row names.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null},
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S312",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "OG-mg-1 made the owner principals restricted; contract C2 wrote their email_deny records, and the email-only browser routes refused the owners themselves.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S312",
      "adjudications/ADJUDICATION_v36.Z.md (OG-ap-30: the two records deleted, email_deny total 1)",
      "adjudications/ADJUDICATION_v37.Z.md (OG-ap-31 e4: the owner passes the four internal pages with 0 store reads)"
    ],
    "remedy": "Shape (b) landed (OG-ap-30) and shape (a) landed (OG-ap-31, OG-en-14). Disarm on Andrew's own signed-in browser run of the four routes.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null},
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W94-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The commit gate's client-data check needs a hashed account-id list that is absent on site Z, so it prints WARN and checks no commit for client account ids.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W94-S2",
      "ls ~/.opal on site Z by 3.0.0_SA_CVO~Z, 2026-10-16: no account_id_hashes.txt",
      "the same box fact ARMED as NFRA_MCPORTAL Z-S63 on 0.0.0_AB_MSTR~Z"
    ],
    "remedy": "Place the hashed account-id list on site Z (or set its variable), a 0.0.0_AB_MSTR~Z provisioning act; then one commit reads the check's verdict, not its WARN.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null},
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S135",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Z-S133's /yearinreview line-ending fork was ruled (A8, route a) and landed; the grader then read correct measurements as absent because they sat under descriptive names, and an md5 in prose failed a machine-graded section.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S135 (the host serves /yearinreview in its LF form 3bbd5ab2, measured post-deploy)"
    ],
    "remedy": "Landed, except one record: yr1.AC2 still compares the host against md5_source 0d828b51 in W/YR_SERVED.json; re-pointing it to 3bbd5ab2 is the issuer's call.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S138",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Z-S137: app/typed_scope.py outside the G3-G6 take; ruled A2 route (a), typed_scope rides OG-ap-19 whole and the cut stands.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S138 (ap19.AC1 'outside the G3-G6 set 0 (want 0)' PASS)"
    ],
    "remedy": "Remediated in round by the ruling and the PASS; the signature was kept by running the seam test as evidence only.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S139",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "An applier ran an apply during OG-ap-20 Phase A ('NO apply'), with no ledger and no halves: gateway-global-etfs-read-policy was live and unsigned for about four minutes, then removed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S139 (the grant is not live after the removal; nothing read it in the window)",
      "OG-ap-20 later signed by all three halves and applied under its ledger (this seat's OG-ap-20 half, 2026-10-15)"
    ],
    "remedy": "The unsigned grant was removed and later applied under three signed halves. The lesson, a 'negative check' must never contain the act it guards, is the applier's carried rule.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S143",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S141: ap20.AC1 left fields empty; the issuer repaired the check at 4ffb7a40c0.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S143 (re-run at release 06cfb6db64: exit 0, PASS, every field populated)"
    ],
    "remedy": "Remediated by the repaired check. Carried note: its SAFE/NATIVE limbs match the name anywhere in the file, not inside the named frozenset; the two readings agree today.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S146",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An unattended Python 3.14.7 to 3.14.8 change on site Z broke the interpreter; the commit gate exited 0 while running nothing.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S146",
      "0.0.0_AB_MSTR~Z broker msg 34481 (2026-10-15 ~15:0xZ): 3.14.8 reinstalled; bare python ran for this seat throughout 2026-10-16"
    ],
    "remedy": "The practical half is remediated (the interpreter is restored). The latent half, the commit gate failing OPEN on a missing interpreter, is Z-S145's and is not closed by this row.",
    "owner": "0.0.0_AB_MSTR~Z",
    "round": "v38",
    "remediation": {"state": "REMEDIATED", "owner": "0.0.0_AB_MSTR~Z", "round": "v38"},
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S147",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-OG-ap-20 section 5 named OG-ap-19's proof filename by copy-paste; the gate reads the order's own stem.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S147 (the instance written where the gate looks; no override used)"
    ],
    "remedy": "Remediated in round: the instance sits at the gate's path. The order sentence is the issuer's to correct; nothing is blocked.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S152",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An exit-waiter counted processes by a token its own wrapper carried, so the count could never reach zero.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S152 (the rule taken: a census must exclude the censor; filter on pythonw.exe -m ...cycle_runner)"
    ],
    "remedy": "Remediated: the seat's instrument error, corrected in the seat's own method; no system change owed.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v38",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v38"},
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
