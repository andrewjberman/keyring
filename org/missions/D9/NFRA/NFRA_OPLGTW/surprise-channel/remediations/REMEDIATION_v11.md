# NFRA_OPLGTW -- surprise channel, REMEDIATION v11 -- THE SLUG (round 24)

Author: 3.0.0_SA_CVO~Z. Round: v11. Fabric: site-z. Recorded: 2026-10-07T10:25:00Z. **Reader:** `1.0.0_SA_CTO~Z`
(ruling msg 30783; `1.0.0_SA_CTO~O` is not live).

4 rows, graduated by `adjudications/ADJUDICATION_v16.Z.md` C-S44. Round 24 has no L9 grade. All 3 orders are
complete; r25 @240ac2fe5a is live. This seat re-ran the 8 checks: 6 PASS; up1.AC2 and rl11.AC1 read FAIL only on
their live..CLOUD conjunct, because r26's cells and the chart route have since drained into CLOUD (C-S46).
- **OPEN, for the CTO (2):**
  - Z-S64: the rivalfunds audit record cannot say which page was served. The r26 chart route adds a fourth route
    with the same gap.
  - Z-W28-S11: the scoped identity's token keeps its full consented scopes until it signs in again through /login.
    The re-consent is Andrew's call.
- **OPEN, for the issuer (2):**
  - Z-S65: the unchecked execution_id is live on r25; the fix is built on CLOUD and ships with r26.
  - Z-W28-S13: the status tool's displayed_date is null against the served manifest; r26 carries no fix.

**Advanced in place this slug (C-S46), REMEDIATED:** Z-S63 and Z-W28-S7 (`REMEDIATION_v10.md`). **Still OPEN from
v10:** Z-S61 (fabric-wide), Z-W28-S9. **Still OPEN from v9:** Z-W28-S2.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S64",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "audit.py's _safe_args omits every arg of a tool that is not in _ARGS_ALLOWLIST, and rivalfunds_view is not in it; rivalfunds_view passes no bytes to audit.log_call. So the page, audit, archive and (from r26) chart routes write records that differ only in time, identity and outcome. Path and status are in journald, which is not shipped to the audit lake; size is in neither. The ETFS_RIVALS round-13 ruling names the gateway access record (status, identity, size, time) as the proof of a served audit page.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S64",
      "adjudications/ADJUDICATION_v16.Z.md#NFRA_OPLGTW-Z-C-S44"
    ],
    "remedy": "OPEN: the CTO rules whether rivalfunds_view's day, route and fund join the R8-PRIV args allowlist and whether the handler passes bytes_returned. That widens what the audit lake stores, so it is a ruling, not a cell the issuer cuts alone. Until then the proof of a served page is the audit record joined to the host access log by timestamp.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v11"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W28-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r25 narrows the scoped identity's consent URL and silent-acquire request to 9 scopes. Entra issues the access token from the existing refresh token, which still carries the consent granted earlier: 17 Graph scopes plus CallTranscripts.Read.All (Mail.Send, Mail.ReadWrite and Calendars.ReadWrite among them). The identity's Graph reach is therefore unchanged by the release; the tool allowlist remains the only narrowing in effect.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S11",
      "adjudications/ADJUDICATION_v16.Z.md#NFRA_OPLGTW-Z-C-S44"
    ],
    "remedy": "OPEN: the CTO carries one call to Andrew -- whether the scoped concierge signs in again through /login so the narrowed consent takes hold. Whether a fresh consent alone drops the earlier grants, or the earlier consent must also be revoked in Entra, is unread and is the first thing to read. REMEDIATED when a token acquired after the act lists only the narrowed scopes.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v11"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S65",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On live r25 @240ac2fe5a, opal_data_refresh_status formats the caller's execution_id into the status URL path after an empty-string check only; httpx collapses dot segments, so the tool can be steered to GET another path under the portal front door with the service account's JWT. What returns is narrow (a top-level status key or an HTTP code). The shape check is built on CLOUD (integration.py:170, commit 82da719ba2, tests/test_opal_portal_status_id_shape.py) and is in the r26 release set, not yet deployed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S65",
      "adjudications/ADJUDICATION_v16.Z.md#NFRA_OPLGTW-Z-C-S44"
    ],
    "remedy": "OPEN: ships with r26. REMEDIATED when r26 is live and a host read shows the status tool refusing an id that fails the shape before any GET. r26 also admits the scoped concierge to this tool (OG-al-2), so the check and the wider caller set land in one release; the release must not ship the allowlist row without the check.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v11"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W28-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "_manifest_date looks for displayed_date, date, as_of, asof, vintage, latest_date, data_date, updated; the served manifest's keys are generated_at, pipeline_execution_id, pipeline_started_at, source_count, sources. The structured displayed_date field is null on every call; the date is readable only inside the 300-character displayed text. The list is unchanged at CLOUD HEAD, so r26 does not fix it. Second half: the read-only status tool belongs to the mutating opal_portal spec and is gated at that spec's min_tier (standard); the through-the-wrapper path with a real principal was not exercised in Phase A.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S13",
      "adjudications/ADJUDICATION_v16.Z.md#NFRA_OPLGTW-Z-C-S44"
    ],
    "remedy": "OPEN: the issuer cuts one cell that reads the served manifest's own date key (generated_at, or the key the portal page displays) with a test against the live manifest's key set, and exercises the tool once through its wrapper with a real principal. The caller texts tell the sender to confirm the served date with this tool, so a null field is what the daily send reads until then.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v11"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
