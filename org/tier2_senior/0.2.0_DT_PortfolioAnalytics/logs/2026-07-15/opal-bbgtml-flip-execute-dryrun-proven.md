# OPAL_BBGTML -- flip executed on the Andrew tempo ruling; first enabled dry_run proven (fail->fix->pass)
**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Summary
Window: since 95fc03d4e (the build-to-enable-gate log, ~18:0xZ) -> ~18:56Z. Andrew's tempo
ruling (~2:10p ET, verbatim: "It is only 2:10p, we should be proceeding all of this, the
workday isnt even half over", recorded 080183d60) collapsed the CTO's tomorrow-AM enable
window to NOW. CTO's review had ALREADY PASSED EARLY (his own source review + his own isolated
22a incl. his own negative control); on the relay he ruled GO-FLIP-NOW ("my tomorrow-AM was
calendar conservatism, not a technical gate"). Full flip executed same hour; the first enabled
dry_run FAILED USEFULLY on attempt 1, was root-caused from the gateway journal, fixed,
redeployed, and PASSED on attempt 2. CTO accepted all legs; OPAL_BBGTML is "live, exercised,
audited end-to-end" (his words). Remaining for close: B5 only (Alyssa's fresh /bbg-pull ->
confirm-gated real send).

## Deployment Sequence (both gateway cycles)
| Step | Action | Result |
|---|---|---|
| 0 | Andrew tempo ruling recorded + relayed; CTO flip question answered in-spec | 080183d60; 454f76fa4 (API-GW host LOAD-BEARING for /auth/login; S3 presigned host was the actually-missing allowlist entry, ADDED; every host consumer-annotated -- CTO: "UPGRADED the audit") |
| 1 | CTO GO-FLIP-NOW 181610Z; COO same-box deconflict (0.5.0~A queued behind me) | Verified 0.5.0~A's validator tools NOT in tree pre-build; their committed c0cd853c1 redirect fix rides intentionally |
| 2 | Enable committed pre-deploy | 3cf844107 (ENABLED_INTEGRATIONS=ycharts opal_portal in the .env template + provenance comment); ledger 20260715T1820Z opened |
| 3 | safe-ec2-deploy #1 | Success; RESTART 18:21:25Z; manifest auto-record lane-blocked -> manual b3084df84 per the wrapper's own instruction |
| 4 | Health + registration | /mcp 401 Bearer-enforcement public @ 18:23:18Z; JOURNAL PROOF 18:21:25Z: "[integrations] enabled: [ycharts, opal_portal]" tools=[opal_data_refresh_upload] + full spec |
| 5 | Deconflict close | DONE signal to 0.5.0~A 182744Z (CC COO); their deploy landed 18:29:20Z behind me; my enable grep-verified surviving their cycle |
| 6 | DRY_RUN attempt 1 (post Andrew MCP reconnect) | FAILED 18:42Z: uncaught KeyError('data 20260710 v1.pkl'). Journal isolation: EVERY upstream leg green (Graph site+item 200, first live secret read via the v1.6.0 grant, login 200, upload-urls 200, download 302->200 follow_redirects); death at MY url_map lookup |
| 7 | Root cause + fix | The proposal's list-shaped urls fallback survived the earlier pins-rewrite as a SILENT .replace() no-op -> {} on the real dict. f6c42dbd6: url_map dict-direct + LOUD missing-key IntegrationError + catch-all (raw exceptions -> AUDITED IntegrationError; the KeyError had escaped run_integration_tool AND the audit trail -- a real gateway hardening gap) |
| 8 | safe-ec2-deploy #2 | Success; restart 18:49:30Z; manifest manual 04fe44383 |
| 9 | DRY_RUN attempt 2 | PASSED 18:50Z: {dry_run: true, upload_id 6b64e194-ac41-452b-8670-f714fbde20ad, data 8488856 B + model 17081387 B staged, "pipeline NOT triggered"} |
| 10 | Independent verify + close | ListObjectsV2 on pending/6b64e194/ shows both keys + exact sizes @ 18:51:41Z; ledger ALL LEGS CLOSED fb02342b8; phase -> TOOL FULLY PROVEN LIVE 000fa5761 |

## Verification (actual output)
- Journal registration: "[integrations] enabled: ['ycharts', 'opal_portal'] -> ... 'opal_portal':
  {'tools': ['opal_data_refresh_upload'], 'spec': {... 'min_tier': 'standard', 'hosts': [4 hosts]...}}"
- Dry_run attempt-2 return: dry_run=true, upload_id=6b64e194-ac41-452b-8670-f714fbde20ad,
  uploaded=[data 8488856, model 17081387], note="files staged in pending/ only; pipeline NOT triggered"
- S3 listing 18:51:41Z: both keys under data-refresh/pending/6b64e194-.../ at exact byte sizes.
- The delegated-Graph substitution from the dark exercise is CLOSED (302->200 on the real leg).

## Rulings / RAVC (significant only; ~8 sent, ~7 handled)
- CTO: enable review PASSED EARLY (181026Z) -> GO-FLIP-NOW (181610Z) -> legs 1-3+5 accepted
  (183041Z) -> LEG-4 CLOSED-ACCEPTED (185407Z; "the dry_run EARNING ITS EXISTENCE"; audit-escape
  hardening called the bigger fix; BACKDATE GUARD ENDORSED: never real-send an older vintage,
  any older date= override lands at CTO's gate -- served-vintage regression = never-widen class).
- COO: same-box deconflict (181807Z) executed + CC'd; fleet note (185535Z, empty-drive-reads bug
  c0cd853c1) -> LANE AUDIT CLEAN (I hit the bug this morning, treated empty as failure, grounded
  on local sync; zero conclusions rest on pre-fix reads) -> ACK'd 185625Z.
- 0.5.0~A: deconflict CLOSED (their deploy 18:29:20Z; my enable grep-verified surviving).

## Current State (zero-context handoff)
- opal_data_refresh_upload LIVE on mcp.opalinvest.dev (gateway i-07dccb1615503ac99), enabled via
  ENABLED_INTEGRATIONS in infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh:126 (persists every
  redeploy). Integration: app/integrations/opal_portal/integration.py @ f6c42dbd6. Secret
  opal/portal/svc-data-refresh (SM ...-4QLOH6) + svc-bbgtml@opalinvest.com + grant
  m365-mcp-gateway-v1.6.0. Ledgers: 20260715T1815Z + 20260715T1820Z both ALL-LEGS-CLOSED.
- Staged dry_run artifacts in s3://opal-data-portal-v2/data-refresh/pending/{24f508ff,6b64e194}/
  expire naturally (pending rows TTL); never triggered.
- Alyssa-side: tools/run_daily_pull.bat + tripwire + BBG_DAILY_SKILL.md live in the SharePoint
  project folder (synced). REMAINING: B5 -- her first real pull (fresh vintage; conda env name
  confirm on her machine) -> ONE confirm-gated real send -> upload/pipeline/display confirms ->
  2-step atomic close CC COO.

## Next Steps
- [Alyssa via Andrew] run tools\run_daily_pull.bat on the terminal machine (Bloomberg logged in).
- [0.2.0_DT] on PASS: opal_data_refresh_upload confirm=true (default fresh stamp) -> B5 evidence
  -> close OPAL_BBGTML (JSON+REGISTRY one commit, CC 2.0.0_SA_COO).

## Blockers
None. B5 is sequenced on a physical-world action (the Bloomberg terminal), not blocked.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| comp-pulse diff (auto x9 commits) | pre-commit risk reflex | CLEAN x7; 2 measured HOLDs (EC2_MANIFEST gitlink-claims + deploy-to-ec2.sh OTP-dual-bearer citation) -- both citations READ, both sanctioned ops (manifest record = the wrapper's own instruction; OTP printf untouched) |
| (rail-checked grep x1) | ENABLED_INTEGRATIONS plumbing in the deploy script + config.py | Found the .env printf line -- the flip point |
| (in-band) | safe-ec2-deploy x2, journal-via-SSM x3 (registration proof + traceback isolation), ListObjectsV2 acceptance | All served as the verification instruments |

No fresh comp-* grounding queries this window: it was EXECUTION of the plan grounded last window
(all backend/CF/IAM grounding cited there); the new diagnostic surface (gateway journal) is not
comp-modeled. What worked: journal-via-SSM as a traceback isolator. Gap found: none new.
