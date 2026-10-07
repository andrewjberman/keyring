# Deploy Completion Record
**Date opened:** 2026-10-06T22:03:56.523665+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-9 PHASE B+D: opal-gateway app release 2c27f3a795 -> rel-nfra-oplgtw-r23 ba27a07439 (OG-q-8 blank-cusip fix: the 23 blank dim_asset rows leave the query and download answers, 2173 -> 2150; ETFS_RIVALS gw-1 additive route /rivalfunds/{day}/audit; 4 shipped files integration.py rivalfunds_view.py server.py app/tests/test_rivalfunds_view.py, 2 source-only test files) via safe-ec2-deploy.sh from /c/tmp/og-rel17; never-widen COO 406becb990 CTO cd1344d1b0 CVO d94f59af39 SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 2c27f3a795 == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r23_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with every value sha256 equal, synthetic mix arm 178 rows 0 blank, route arms 2 of 2 (200 only if audit.html exists, else NOT RUN), floor rl4.AC1 + ht.AC2 |  | OPEN |
| real-holder-read | verify | real-holder download and query reads of the one live dim_asset grant on the served code | returned = distinct = held, unheld 0, blank 0 on BOTH paths (2150 expected), grants_written 0; else roll back |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 2c27f3a795 | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb17 at 2c27f3a795 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified |  | OPEN |
| drain-back | git | R16 drain-back: git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway equals the CLOUD-only runbook only; LINEAGE_R18 CLOUD-only list updated | recorded diff output |  | OPEN |

## Log

- 20261006T220356Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 6 leg(s)

- 20261007T0125Z RE-CUT by 0.9.0_WK_NFRA_OPLGTW~28 (OG-rl-9 AMENDMENT 2): live moved to 9d3e2eb3fce3ceabbf06f6c1819451894291be05 under the r24 hotfix, so the title and every leg pin to 2c27f3a795 / og-rel17 / og-rb17 / ba27a07439 / the halves cd1344d1b0, 406becb990, d94f59af39 are SUPERSEDED: base is live 9d3e2eb3fc (host md5 96 of 96 identical, re-read 01:2xZ, ssm 98ce87ea), release is rel-nfra-oplgtw-r23b sha 7d65a28db026a44d7199ffe52a97e44952df75a1 from /c/tmp/og-rel19, rollback tree /c/tmp/og-rb18 at 9d3e2eb3fc, halves COO f3220f50db CTO 4484d77353 CVO 43fd7d5159 SIGNED; legs unchanged in number, plus a condition-4 installed-login read after the deploy (recorded in the real-holder-read and install-verify proofs); no act has been taken before this line
