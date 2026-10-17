# Session log -- 3.0.0_SA_CVO~Z, site Z, 2026-10-16 ~02:20Z to 2026-10-17 ~00:45Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

Seat: `3.0.0_SA_CVO~Z` (CVO, site Z). Launched by Andrew with "/watcher once, zero crons; resume from your 10-16 winddown log; the
OG-ap-24 CVO half is owed".
- **No 10-16 wind-down log for this lane exists.** The newest CVO~Z log is `logs/2026-10-12/session_sitez_0530Z-0100Z.md`.
- **Zero crons.** LIVE_ARMS still lists a site-Z SYSPARITY cron for this seat, and it is NOT armed, per the launch word.
- **Watcher:** `/watcher` ran once, and the inbox Monitor has been re-armed on each 30-minute expiry. Census: 1 script row each
  time, never more.

## Work done (33 commits under `3.0.0_SA_CVO~Z`; per-file detail is in each commit message)

**Never-widen halves (NFRA_OPLGTW), all in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/`:**

| ask | verdict | commit | the deciding read |
|---|---|---|---|
| OG-ap-24 (six vendor read roles) | SIGNED | 5b66771763 | 22 registry prefixes table-level and single-firm; no IAM fence on SmartX rows (code fence) |
| OG-ap-25 (etf-classifications GetItem) | SIGNED | be6d23b7f6 | full census of 11,362 items: 0 of 16 attributes firm- or client-linked |
| OG-ap-26 (grant moves to the internal reader) | SIGNED | f2cf55e41e | the reader's trust names only `opal-gateway-role` |
| OG-ap-23 at 56c0f8ce1d | **REFUSED** | 8027fa44c1 | the five `client_*` tools were NATIVE: any Opal user would read client account data, against PRD v3.1 Ruling 2 (BLOCKING row Z-S162) |
| OG-ap-23 re-cut at 3d5c9c8bf1 | SIGNED | 49ebdc867a | `CLIENT_TOOLS` in DATA_GRANT and TIER_ADMITTED; OG-bd-3 reaches one principal (roster of 1, exact key match) |
| OG-ap-27 (four release-gap prefixes) | SIGNED | b121849fbe | model_composition: 11 model-level columns, no account field |
| OG-mg-1 R1 and R2 | SIGNED | 5c4025b899 | R2 (the concierge mirror) covered by Andrew's v2.3 words; filed Z-S173 (Alyssa's ratified no-download has no carrier) |
| OG-ap-29 (49F `-live` read role) | SIGNED | 6b7d6ef48d | prefixes equal the adapter's 4 reads; firm scope measured (z08 on 100% of rows, 0 z09) |
| OG-ap-28 (round-38 batch) | SIGNED | ffc2045889 | `-live` routes to `blackdiamond49flive` and an unset role refuses closed |
| email_deny reversal (OG-ap-30) | SIGNED | c39c415178 | exactly two keys; re-read after the apply, see v36 (3fda34b997) |
| OG-ap-31 (round-39 batch) | SIGNED | 5157a00b6f | deny exemption: exact roster match, the four internal routes, the same ALB-OIDC identity, andrew@ only |

**Grades and compiles:**
- **NFRA_MCPORTAL** (`surprise-channel/adjudications/`):
  - v6: PE+PF round 2, MP-pf-2 AC2 PASS bounded.
  - v7: PF round 3, MP-pf-6 AC3 FAIL on the world (the writer history is no enumeration).
  - v8: round 4, Z-C-S40 closed; filed NFRA_OPLGTW Z-S160 (og-i1 probe residue).
  - v9: S1 (iii) NOT MET at 390 px.
  - v10: S1 (iii) MET bounded after MP-pf-9.
- **NFRA_OPLGTW** (`surprise-channel/adjudications/`):
  - v28: OG-ap-23 served read; C1, C2 and via_internal_reader MET.
  - v29-v31, v32-v33: round 37's 8 judgment criteria graded.
  - v34-v35, v37: OG-ap-28/31 AC3.
  - v36: OG-ap-30 re-read.
- **NFRA_MCPINDEX** (`surprise-channel/adjudications/`):
  - v13-v14: round 18 (9 unratified 49F legacy rows found and ruled OUT).
  - v15: round 19.
  - v16: round 20 (a monotone depth grade passes a truncated series start, correcting my own v15).
  - v17: round 21.

**Surprise rows filed (NFRA_OPLGTW):**
- Z-S160: probe residue in the live grant store.
- Z-S162: client tools NATIVE; remediated.
- Z-S173: Alyssa's no-download has no carrier.
- Z-S175: a 403 for a key-resolution failure; fixed by OG-en-9.
- Z-S176: round-close-check read the first grade; fixed, it now reads "latest surfaced_at wins".
- Z-S292: the 49F live reads went through a role that denies opal-data-bd; remediated by OG-ap-29 and OG-ap-28.

**Misses owned on the record:**
1. My OG-ap-24 half checked the grant against the registry, not the adapter's reads (Z-S292).
2. My OG-mg-1 half did not trace C2's `email_deny` to the browser routes; Andrew was locked out of his own pages about 7.5 h.
3. My v15 endorsed the monotone depth grade for every claim kind (corrected in v16).
4. My v13 inferred the 49F store from an IAM grant, not the code.
5. v35 quoted one client weight value; fixed in 89881b269b.

## MCP traffic

About 30 inbound messages, all acked: halves asked, L8 packets, rulings. Every outbound send went to `1.0.0_SA_CTO~Z` (L8 send gate),
asking a relay to COO~O or CloudOps where needed. One PushNotification went out on the OG-ap-23 refusal, and one on the opalgateway
MCP outage.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `round-close-check.py` | PASS/REFUSED read per round | it found the 7th AC3 (ap-23) the COO missed; it exposed the first-row bug (Z-S176) |
| `comp-find` | PASS | prefix writers, FWD-21 record census, PRD ruling census; two denials redirected correctly |
| `iam simulate-principal-policy` | PASS | it found Z-S292 (explicitDeny on opal-data-bd, a positive control allowed) |
| `aws dynamodb scan` (grant store, etf-classifications) | PASS | probe residue (17 vs 9 POLICY items); email_deny 3 then 1 |
| PyYAML (Python 3.11) over the catalog blobs | PASS | 9 unratified OUT rows; 39 depth claims classified |
| pyarrow over opal-data-bd objects (counts only, deleted after) | PASS | the 49F live tables are single-firm |
| `surprise-row-gate` | WARN once | refused an adjudication file with zero rows; I added a row, no override |

- **What worked:** reading the release bytes instead of the ask, and a second plane for every inherited claim (my own credential,
  the live table, the adapter code).
- **What failed:** the opalgateway MCP (429 since ~09:0xZ) left me no real-call instrument; the bodies came from the applier instead.
  A Claude Code safety check blocked a cleanup `rm` that used a bare variable, so I re-ran it with `${SP:?}`.
- **Gap found:** the evidence-capture scrub rewrote digits (OG-ev-1), so a body record is not the served bytes unless the capture
  says so.

## Blockers

None in this lane.

## Current State

- **Live gateway:** `4be300110e` (OG-ap-31), deployed 2026-10-16T22:00Z. Round 39 reads MAY-CLOSE with 1 of 1 judgment graded.
- **Open grades owed by this seat:**
  - OG-ap-31 AC3 is PARTIAL. It re-grades on a served 13-month 49F call after the CTO's round-40 W1 ruling @0a15d90223 (measure,
    then a full read, or a `next_cursor`).
- **Rows this seat watches:**
  - Z-S63 (NFRA_MCPORTAL): no account-id hash list on site Z, ARMED on `0.0.0_AB_MSTR~Z`.
  - Z-S173: CTO decision.
  - Z-C-S84: the OG-ap-31 window.
- **Push state:** commits since e1ad74cd1b are LOCAL on box/sitez (origin box/sitez reads `e1ad74cd1b`, ls-remote ~00:45Z). Box-sync
  pushes them.
- **Client-data evidence files** on this box are untracked and git-excluded, and none is committed:
  - `deliverables/0.7.0_AE_CloudOps~Z/CVO_AC3_BODIES_OG-ap-28.json`;
  - `deliverables/0.7.0_AE_CloudOps~NFRA1/CVO_AC3_BODIES_OG-ap-31.json`.

## Next Steps

- [3.0.0_SA_CVO~Z] Grade the round-40 packet: the 49F 13-month window on a served call (OG-ap-31 AC3 re-grade).
- [3.0.0_SA_CVO~Z] Re-read any half signed before its ask exists, against the ask, before the GO (the v36 note).
- [1.0.0_SA_CTO~Z] Z-S173: enforce Alyssa's no-download, or strike it from the PRD.
- [0.0.0_AB_MSTR~Z] Z-S63: provision `~/.opal/account_id_hashes.txt` on site Z.
- [2.0.0_SA_COO~MI] Round 22: the committed allow file beside any real registry drop (v17).

-- 3.0.0_SA_CVO~Z
