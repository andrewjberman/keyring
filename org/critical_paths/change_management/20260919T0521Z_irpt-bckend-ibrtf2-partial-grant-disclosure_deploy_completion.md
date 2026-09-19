# Deploy Completion Record
**Date opened:** 2026-09-19T05:21:05.674671+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T060612Z
**Deploy:** IB-rtf-2: refusal-order inversion + unprojected_grant disclosure field deployed to 7 investor-reporting serving functions
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | irpt-directory-search code update | CodeSha256==built post-apply | irpt-directory-search served=aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOmhmU= built=aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOmhmU= MATCH=True (rte6_package_deploy.py verify, this run) | CLOSED 20260919T060555Z |
| L2 | activation | irpt-export-render code update | CodeSha256==built post-apply | irpt-export-render served=4Dp6e0Vy+SfziPY+9wUSWSBS4JzS9diUtduOTxIqclQ= built=4Dp6e0Vy+SfziPY+9wUSWSBS4JzS9diUtduOTxIqclQ= MATCH=True | CLOSED 20260919T060555Z |
| L3 | activation | irpt-holdings code update | CodeSha256==built post-apply | irpt-holdings served=oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs= built=oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs= MATCH=True | CLOSED 20260919T060555Z |
| L4 | activation | irpt-narrative code update | CodeSha256==built post-apply | irpt-narrative served=sgolF/uXedgXpePoBoi5y1dIgOybQkgcokihEJFM+0I= built=sgolF/uXedgXpePoBoi5y1dIgOybQkgcokihEJFM+0I= MATCH=True | CLOSED 20260919T060555Z |
| L5 | activation | irpt-status code update | CodeSha256==built post-apply | irpt-status served=LHprxKSP1lM3VhoP2ijEcUVCtI+yeZt8tPRkZwpRBdY= built=LHprxKSP1lM3VhoP2ijEcUVCtI+yeZt8tPRkZwpRBdY= MATCH=True | CLOSED 20260919T060555Z |
| L6 | activation | irpt-performance-adapter code update | CodeSha256==built post-apply | irpt-performance-adapter served=/Cn8XUZoSn1EGBax3+/UaVjJSAQiybZQ84vRVwiRcWs= built=/Cn8XUZoSn1EGBax3+/UaVjJSAQiybZQ84vRVwiRcWs= MATCH=True | CLOSED 20260919T060556Z |
| L7 | activation | irpt-ycharts-generate code update | CodeSha256==built post-apply | irpt-ycharts-generate served=1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o= built=1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o= MATCH=True | CLOSED 20260919T060556Z |
| L8 | verify | live route re-test: abby_horton served with disclosure, cross-firm refused, pre-fix negative control | battery + live reads | battery_ib_rtf_2.py arm_e_live_proof, this run @HEAD: abby_horton/49financial served k=21 count=12 denominator=33 (self-consistent k+count=denominator); cross-firm swap refused EMPTY_GRANT; pre-fix zip (content-sha256 v0MMA3yUxIPNdCMXhE/2pSD9lU+5LgI945JqkuULH8U=, verified by content) reads UNPROJECTED_GRANT; inflection/cottonwood refused EMPTY_GRANT | CLOSED 20260919T060556Z |

## Log

- 20260919T052105Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 8 leg(s)
- 20260919T060555Z LEG L1 closed: irpt-directory-search served=aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOmhmU= built=aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOm
- 20260919T060555Z LEG L2 closed: irpt-export-render served=4Dp6e0Vy+SfziPY+9wUSWSBS4JzS9diUtduOTxIqclQ= built=4Dp6e0Vy+SfziPY+9wUSWSBS4JzS9diUtduOTxIqclQ
- 20260919T060555Z LEG L3 closed: irpt-holdings served=oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs= built=oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs= MAT
- 20260919T060555Z LEG L4 closed: irpt-narrative served=sgolF/uXedgXpePoBoi5y1dIgOybQkgcokihEJFM+0I= built=sgolF/uXedgXpePoBoi5y1dIgOybQkgcokihEJFM+0I= MA
- 20260919T060555Z LEG L5 closed: irpt-status served=LHprxKSP1lM3VhoP2ijEcUVCtI+yeZt8tPRkZwpRBdY= built=LHprxKSP1lM3VhoP2ijEcUVCtI+yeZt8tPRkZwpRBdY= MATCH
- 20260919T060556Z LEG L6 closed: irpt-performance-adapter served=/Cn8XUZoSn1EGBax3+/UaVjJSAQiybZQ84vRVwiRcWs= built=/Cn8XUZoSn1EGBax3+/UaVjJSAQiybZQ84vRV
- 20260919T060556Z LEG L7 closed: irpt-ycharts-generate served=1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o= built=1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyV
- 20260919T060556Z LEG L8 closed: battery_ib_rtf_2.py arm_e_live_proof, this run @HEAD: abby_horton/49financial served k=21 count=12 denominator=33 (self-
- 20260919T060612Z CLOSED -- all 8 legs proven
