# Deploy Completion Record
**Date opened:** 2026-10-06T08:14:05.193028+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-8 PHASE B+D: opal-gateway app release cf4b036e62 -> rel-nfra-oplgtw-r20 2c27f3a795 (R24 as amended R25: /login tier admit backstop in login_admit_decision + gw_login audit record audit.log_login; engine.py RSS-poll ctypes reuse OG-fl-1; 3 shipped behaviour files server.py audit.py engine.py; 5-file commit incl 2 test files) via safe-ec2-deploy.sh from /c/tmp/og-rel16; never-widen COO 1eeeb17ff6 CTO c94393604a (no condition) CVO fcd7f4c457 (W1-W3) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared cf4b036e62 == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r20_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with every value sha256 equal, /login arms 10 of 10 (CVO W2: non-restricted ADMITTED reason tier_graph_tools, restricted REFUSED, one gw_login per request, no address/token/state), engine RSS equal, floor rl4.AC1 + ht.AC2 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous cf4b036e62 | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb16 at cf4b036e62 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified |  | OPEN |
| drain-back | git | R16 drain-back (CVO W3): git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway empty; LINEAGE_R18 CLOUD-only list updated | recorded diff output |  | OPEN |

## Log

- 20261006T081405Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
