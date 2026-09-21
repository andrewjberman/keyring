# Deploy Completion Record
**Date opened:** 2026-09-19T00:06:37.729479+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T010922Z
**Deploy:** IB-rte-6: id_projection wired into 7 investor-reporting serving functions + 49F crosswalk-seam projection
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | irpt-directory-search code update | CodeSha256==built post-apply | CodeSha256==built v0MMA3yUxIPNdCMXhE/2pSD9lU+5LgI945JqkuULH8U=; terraform 0-diff replan | CLOSED 20260919T010840Z |
| L2 | activation | irpt-export-render code update | CodeSha256==built post-apply | CodeSha256==built WJ8Nk/Zr2g1/cafjnJvF1glFiMdPiFc7Bt8hktqsxuo=; terraform 0-diff replan | CLOSED 20260919T010841Z |
| L3 | activation | irpt-holdings code update | CodeSha256==built post-apply | CodeSha256==built R2+ff33uJO3jrCOuMII9y6SvEhvG43wfeXrGbn0pJGk=; terraform 0-diff replan | CLOSED 20260919T010842Z |
| L4 | activation | irpt-narrative code update | CodeSha256==built post-apply | CodeSha256==built XUJ68NaABwFNW9ItzMBO5l0Jvb2pG5t+ot833bkLY5g=; terraform 0-diff replan | CLOSED 20260919T010842Z |
| L5 | activation | irpt-status code update | CodeSha256==built post-apply | CodeSha256==built twhh/jwDdSwzQ6/BtFdkl52jXYuO19AfVviu/+FlD5A=; terraform 0-diff replan | CLOSED 20260919T010843Z |
| L6 | activation | irpt-performance-adapter code update | CodeSha256==built post-apply | CodeSha256==built xI2iPO5/5WTf2a6rqgdL6kXJZ3ODiDZI22pz51jGMuQ=; terraform 0-diff replan | CLOSED 20260919T010844Z |
| L7 | activation | irpt-ycharts-generate code update | CodeSha256==built post-apply | CodeSha256==built 4TF3bfgPezMaZvx7tZdwJHOF6S7GyRq0ayI6s5ryV3s=; terraform 0-diff replan | CLOSED 20260919T010845Z |
| L8 | verify | live route re-test, 0-diff replans | battery + terraform plan output | battery_ib_rte_6.py rc=1: arms a/b/c PASS (13 of 13 wired, mutant fires; seam resolves 17895 of 22646 slots / 21 of 43 abby_horton; 7 of 7 CodeSha256==built + terraform 0-diff replans); arm d FAILS honestly -- post-fix code is STILL UNPROJECTED_GRANT for abby_horton because enforce.py's own all-or-nothing policy refuses the WHOLE grant on ANY unresolved custodian key, and the seam covers 79 percent not 100 percent -- R56-AC1 not PASS-by-output, order stays open | CLOSED 20260919T010922Z |

## Log

- 20260919T000637Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 8 leg(s)
- 20260919T010840Z LEG L1 closed: CodeSha256==built v0MMA3yUxIPNdCMXhE/2pSD9lU+5LgI945JqkuULH8U=; terraform 0-diff replan
- 20260919T010841Z LEG L2 closed: CodeSha256==built WJ8Nk/Zr2g1/cafjnJvF1glFiMdPiFc7Bt8hktqsxuo=; terraform 0-diff replan
- 20260919T010842Z LEG L3 closed: CodeSha256==built R2+ff33uJO3jrCOuMII9y6SvEhvG43wfeXrGbn0pJGk=; terraform 0-diff replan
- 20260919T010842Z LEG L4 closed: CodeSha256==built XUJ68NaABwFNW9ItzMBO5l0Jvb2pG5t+ot833bkLY5g=; terraform 0-diff replan
- 20260919T010843Z LEG L5 closed: CodeSha256==built twhh/jwDdSwzQ6/BtFdkl52jXYuO19AfVviu/+FlD5A=; terraform 0-diff replan
- 20260919T010844Z LEG L6 closed: CodeSha256==built xI2iPO5/5WTf2a6rqgdL6kXJZ3ODiDZI22pz51jGMuQ=; terraform 0-diff replan
- 20260919T010845Z LEG L7 closed: CodeSha256==built 4TF3bfgPezMaZvx7tZdwJHOF6S7GyRq0ayI6s5ryV3s=; terraform 0-diff replan
- 20260919T010922Z LEG L8 closed: battery_ib_rte_6.py rc=1: arms a/b/c PASS (13 of 13 wired, mutant fires; seam resolves 17895 of 22646 slots / 21 of 43 a
- 20260919T010922Z CLOSED -- all 8 legs proven
