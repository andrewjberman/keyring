# Deploy Completion Record
**Date opened:** 2026-10-16T11:32:30.878117+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T114729Z
**Deploy:** IRPT_DASHBD TO-PROMOTE-M33: promote ONE approved branch cand/dell2/irpt-series-mirror-contract-033 (head 831f974aa1, two commits, one file seriesContract.ts) DEV->PROD via /prod-deploy chosen-set release; type-only series mirror 0.3.3, no page changed, Opal-internal, CTO approved row 6099; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only the two approved commits | promoted sha and PROD before/after | origin/PROD 8012cd1afbaa -> 64f9dba10528 (push receipt 8012cd1a..64f9dba1; origin/PROD re-read before push = 8012cd1afbaa); non-merge payload a8d5dafc 831f974a only, ONE file seriesContract.ts (+10 -1), head 831f974aa1 = approval head; tag portal-v2.1.231 peels to 64f9dba10528 | CLOSED 20261016T114728Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 38895714333 --json: status completed, conclusion success, headSha 64f9dba10528593258b4b8a30b91763913122b76; the only workflow on that sha | CLOSED 20261016T114728Z |
| L3 | verify | dist of promoted tree equals dist of previous PROD byte for byte | file count and sha256 comparison | dist of the promoted tree vs a build of origin/PROD 8012cd1afbaa, both built on this seat: sha256 of every file, 88 of 88 identical, 0 only-in-one-side, 0 differing, 63 of 63 js/css chunks; control: one planted byte read differing 1 identical 87. Reads no served site and no account. | CLOSED 20261016T114728Z |

## Log

- 20261016T113230Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261016T114728Z LEG L1 closed: origin/PROD 8012cd1afbaa -> 64f9dba10528 (push receipt 8012cd1a..64f9dba1; origin/PROD re-read before push = 8012cd1afba
- 20261016T114728Z LEG L2 closed: gh -R Opal-Capital/portal run view 38895714333 --json: status completed, conclusion success, headSha 64f9dba10528593258b
- 20261016T114728Z LEG L3 closed: dist of the promoted tree vs a build of origin/PROD 8012cd1afbaa, both built on this seat: sha256 of every file, 88 of 8
- 20261016T114729Z CLOSED -- all 3 legs proven
