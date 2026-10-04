# Deploy Completion Record
**Date opened:** 2026-10-04T23:09:05.718802+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-5: opal-gateway app release af2d762970 -> rel-nfra-oplgtw-r16 (R9 grain, R9a single-page fallback, dim_transaction data prefixes, query-path dim_asset guard deleted) via safe-ec2-deploy.sh from /c/tmp/og-rel10; never-widen COO a197f29422 CTO 75d651b7f4 (C1) CVO d370d16fe3 (Q1-Q3) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared af2d762970 == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl5_verify.sh after: md5 94 of 94 = release bytes, health 200, 65 tools, 50 key names unchanged, paging pages OK, census, held check, download control, census_after_other 14 per master, ungranted reads refused; rl4.AC1 ht.AC2 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous af2d762970 | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb10 at af2d762970 equal to the live artifact, command recorded | diff 97 of 97 equal (PHASE A) and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261004T230905Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
