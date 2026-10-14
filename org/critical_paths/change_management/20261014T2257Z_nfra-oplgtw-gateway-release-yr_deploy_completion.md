# Deploy Completion Record
**Date opened:** 2026-10-14T22:57:14.961892+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T233802Z
**Deploy:** NFRA_OPLGTW OG-yr-1: the refreshed /yearinreview page AND the viewer gate widened to every Opal employee (both halves signed at bf7ffb62f4)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the deploy source is the signed release: C:/tmp/og-rel-yr2 HEAD = bf7ffb62f4ae5af8298d3c24960c63d2965542d9 and its parent = live deployed_commit bacec95ccd | both hashes read at the act | A1 guard read AT the act in C:/tmp/og-rel-yr2: git rev-parse HEAD = bf7ffb62f4ae5af8298d3c24960c63d2965542d9 (EQUAL to the signed release_sha in full) and HEAD^ = bacec95ccd6cafd2201f7433af24ae2748732355 (EQUAL to live deployed_commit). Re-read after the sparse-cone widening that fixed the first refusal, and corroborated independently by the deploy's own stale-base guard, which read the live ref from the artifact's git-ref S3 metadata at BOTH checkpoints (early and immediately-before-upload) and found bacec95ccd each time. | CLOSED 20261014T233801Z |
| L2 | activation | safe-ec2-deploy lands the three-file release and the service comes back | the deploy output plus GET /health on 127.0.0.1:8080 | safe-ec2-deploy.sh rc=0 2026-10-14T23:03:38Z-23:05:14Z, artifact opal-gateway-bf7ffb62f4.tar.gz (560K) uploaded then pulled by the host; SSM 768a6366-ab1a-4220-aea9-b8e7b2cfcda3 Success; 'OK: opal-gateway active'; GET /health on 127.0.0.1:8080 read {"ok":true} twice -- once in the deploy itself and once in the independent post-deploy harness (status 200). /mcp unauth still 401. ENV key NAMES 54 before and 54 after, the deploy's own two lists diffed to DELTA 0. | CLOSED 20261014T233801Z |
| L3 | ec2-baked-asset | the RUNNING path carries the release bytes, and the served page is the CHECKED-OUT form | SSM md5 over app/, deploy/, dashboard/ equal to the release, and the page's own md5 equal to 0d828b51d433a24f7e2ef2e6ea7967ee with the data date present | One SSM md5 read of the RUNNING paths (yr_served_harness.py under /opt/opal-gateway/.venv/bin/python, pulled from S3 per Rule 12; the harness's own md5 on the host 01edec3bee89d95fad39c61f5ff4a72e == the local file): 107 of 107 files under app/ and deploy/ md5-EQUAL to the release blobs, 0 mismatches, 0 paths present on only one side; dashboard/ holds 12 files, the vite build of mcportal@17dcbb28624eab147318052f58bcc39b8eb8029c produced at deploy time, so it is recorded by provenance and not diffed against a repo path. The served page: md5 of the RESPONSE BODY 0d828b51d433a24f7e2ef2e6ea7967ee == the page on the host's disk == the source (48235 bytes, 344 CRLFs -- the CHECKED-OUT form the deploy tars, per order A3, not the LF blob 3bbd5ab2), and it carries "until": "2026-10-11". | CLOSED 20261014T233802Z |
| L4 | verify | the widened gate admits an Opal identity and still refuses a guest and an outside domain, and the tool registry is unchanged | W/YR_SERVED.json with the admitted and refused arms, plus the registry count before and after | W/YR_SERVED.json, the three arms through the INSTALLED handler on i-07dccb1615503ac99: a synthetic Opal identity NOT on the live roster (roster size 1, membership checked and false) served 200 with the page and 48235 bytes, so the 200 is the widening and not the roster answering; the Entra guest form #EXT#@opalinvest.com refused 403 with 42 bytes and no page title, audit verdict denied/roster; an outside domain likewise 403. Registry 46 before (W/GT_REGISTRY_BEFORE.json) and 46 after, both from app.tools.mcp._tool_manager.list_tools() -- UNCHANGED. The audit sink was stubbed deliberately: its real path put_objects to AUDIT_S3_BUCKET and this order's BOUNDS forbid writing any object, so the gate ran as installed while the verdict the sink would have written was captured in-process. Public endpoint recorded: an unauthenticated GET of https://mcp.opalinvest.dev/yearinreview is 302 to the Entra authorize endpoint, so the page is not open to the internet. | CLOSED 20261014T233802Z |

## Log

- 20261014T225714Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20261014T233801Z LEG L1 closed: A1 guard read AT the act in C:/tmp/og-rel-yr2: git rev-parse HEAD = bf7ffb62f4ae5af8298d3c24960c63d2965542d9 (EQUAL to t
- 20261014T233801Z LEG L2 closed: safe-ec2-deploy.sh rc=0 2026-10-14T23:03:38Z-23:05:14Z, artifact opal-gateway-bf7ffb62f4.tar.gz (560K) uploaded then pul
- 20261014T233802Z LEG L3 closed: One SSM md5 read of the RUNNING paths (yr_served_harness.py under /opt/opal-gateway/.venv/bin/python, pulled from S3 per
- 20261014T233802Z LEG L4 closed: W/YR_SERVED.json, the three arms through the INSTALLED handler on i-07dccb1615503ac99: a synthetic Opal identity NOT on 
- 20261014T233802Z CLOSED -- all 4 legs proven
