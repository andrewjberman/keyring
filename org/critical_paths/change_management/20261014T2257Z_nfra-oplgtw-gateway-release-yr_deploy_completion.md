# Deploy Completion Record
**Date opened:** 2026-10-14T22:57:14.961892+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-yr-1: the refreshed /yearinreview page AND the viewer gate widened to every Opal employee (both halves signed at bf7ffb62f4)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the deploy source is the signed release: C:/tmp/og-rel-yr2 HEAD = bf7ffb62f4ae5af8298d3c24960c63d2965542d9 and its parent = live deployed_commit bacec95ccd | both hashes read at the act |  | OPEN |
| L2 | activation | safe-ec2-deploy lands the three-file release and the service comes back | the deploy output plus GET /health on 127.0.0.1:8080 |  | OPEN |
| L3 | ec2-baked-asset | the RUNNING path carries the release bytes, and the served page is the CHECKED-OUT form | SSM md5 over app/, deploy/, dashboard/ equal to the release, and the page's own md5 equal to 0d828b51d433a24f7e2ef2e6ea7967ee with the data date present |  | OPEN |
| L4 | verify | the widened gate admits an Opal identity and still refuses a guest and an outside domain, and the tool registry is unchanged | W/YR_SERVED.json with the admitted and refused arms, plus the registry count before and after |  | OPEN |

## Log

- 20261014T225714Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
