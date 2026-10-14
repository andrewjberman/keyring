# Deploy Completion Record
**Date opened:** 2026-10-14T23:04:58.872790+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-p-1 ADDENDUM 1 (ADHOC.canon-r9-trend-publish-tonight, WORLD): ONE-TIME splice of the Trend groups onto the eight as-of-2026-10-13 gold objects -- s3://opal-data-assets/portal/gold/mdpf/{global,49financial,inflection,cottonwood}/{aggregate-aua-timeseries,category-views}/2026-10-13.json (prior VersionIds in addendum section 2) -- by put_object of bodies built by the issuer instrument round9/checks/build_publish_bodies.py, then ONE hand-run of opal-assets-mdpf-portal-publisher to copy them to the served keys s3://opal-data-portal-v2/platinum/mdpf/<scope>/<type>.json. Authority: Andrew-direct ~22:5xZ (CTO record 44eac4d919); addendum COO half in 1e52755b27 (sha256 02b24fb3...), CTO half 83ec2d7b0e (conditions C1-C3). The lambda mdpf-gold-lambda stays at pin 8e2dd0fb369043d5f23dca2d02dba7d51cfabd6f; no lambda is changed; nothing is deleted. PROVENANCE: the Trend keys are SPLICED by an issuer instrument on Andrew word, not produced by a scheduled run; the objects keep the 2026-10-13 run _provenance and are never to be cited as evidence of the lambda. GO: 2.0.0_SA_COO~D1 msg 5952. Deadline 2026-10-15 12:44Z.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions 2a-2f (GO, both halves signed, the two instrument hashes, deployed code is the pinned code, sentinels across every live worktree, clock) | all true or the order stops |  | OPEN |
| L1 | verify | before print: the eight gold keys (VersionId, ETag, LastModified, body sha256 equal to the addendum), the eight served keys, latest.json, publisher CodeSha256 and Scheduler input, the whole served listing under platinum/mdpf/ with VersionIds | equal to the addendum prior VersionIds or STOP |  | OPEN |
| L2 | verify | build_publish_bodies.py --from-s3 to a scratch dir, then r9_trend_groups_readback.py read --dir | OK x4 scopes, BUILT 8 bodies, exit 0; ten of eleven arms PASS, R9 the only FAIL |  | OPEN |
| L3 | activation | the eight put_object calls (category-views first, timeseries after, Global last) with read-back of each | each gold key body sha256 equals the built body, a new VersionId, the prior VersionIds still exist |  | OPEN |
| L4 | activation | the ONE hand-run of opal-assets-mdpf-portal-publisher with the schedule input verbatim | the eight pairs published, failed empty, the eight served keys equal their gold bodies |  | OPEN |
| L5 | verify | proofs: readback in S3 mode, the served Global timeseries parsed, the cache behaviour for /api/general/mdpf/*, the controls, deploy_ledger check | R1-R8, R10, R11 PASS; no muni on the served category-views; code unchanged |  | OPEN |

## Log

- 20261014T230458Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)
