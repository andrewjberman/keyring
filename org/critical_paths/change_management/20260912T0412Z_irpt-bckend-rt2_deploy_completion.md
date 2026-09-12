# Deploy Completion Record
**Date opened:** 2026-09-12T04:12:23.915248+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-2 (amendment 5 E4): the SECOND and final deploy of this cell -- the holdings C1 mark, the v0.14 envelope work, the post-read business_date emission and the W2-S39 cache-lifetime fix. SIX roots applied one at a time; irpt-ycharts-generate HELD on the E3 guard.
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | irpt-directory-search (root .../directory) ROLLBACK: restore prior S3 object version, artifact sha aZg2fjOS40UhHY7jhivPVIknES6LjVAdaVUJpg97sxs=; handler entry.lambda_handler is unchanged by this deploy | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed |  | OPEN |
| R1V | verify | irpt-directory-search extract-and-import of the DEPLOYED artifact, flat /var/task, fresh interpreter, repo off sys.path, NO layer | IMPORT-OK + negative control FIRES |  | OPEN |
| R2 | activation | irpt-performance-adapter (root .../performance) ROLLBACK: prior sha 41ICV4HKj+qzy7xwqHqGjSg2UP1LjqT20Y5XeAHcyBE=; handler unchanged | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed |  | OPEN |
| R2V | verify | irpt-performance-adapter extract-and-import, layer mounted as /opt/python | IMPORT-OK + negative control FIRES |  | OPEN |
| R3 | activation | irpt-narrative (root .../narrative) ROLLBACK: prior sha bgjDRDUFzDitZCaZVMLP2bnUZcS9vVW02vyAFZqc/wI=; handler unchanged | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed |  | OPEN |
| R3V | verify | irpt-narrative extract-and-import, layer mounted | IMPORT-OK + negative control FIRES |  | OPEN |
| R4 | activation | irpt-export-render (root .../export) ROLLBACK: prior sha g4R4nDLA4MS/PrVPAUL75NM5yA+/jh4D+pP8fly0Uk0=; handler unchanged | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed |  | OPEN |
| R4V | verify | irpt-export-render extract-and-import, layer mounted | IMPORT-OK + negative control FIRES |  | OPEN |
| R5 | activation | irpt-status (root .../ops) ROLLBACK: prior sha xardX7EA2Fqzx0j1ZnP4NXHZqXk9JPbXfaZZ5UrbH34=; handler unchanged | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed |  | OPEN |
| R5V | verify | irpt-status extract-and-import, NO layer | IMPORT-OK + negative control FIRES |  | OPEN |
| R6 | activation | irpt-holdings (root .../holdings) THE C1 MARK, the one handler that MOVES: snapshot.lambda_handler -> entry.lambda_handler. ROLLBACK: handler back to snapshot.lambda_handler AND restore artifact sha yOiMCrewFEMtE6GCJzBjNdLQsRpliY8zrM3t1AMyynI= | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed |  | OPEN |
| R6V | verify | irpt-holdings extract-and-import, layer mounted; its enforce/errors/resolve are its OWN PINNED staged copies per STAGE_MANIFEST.json, only entry/served/loaders come from the tree | IMPORT-OK + negative control FIRES |  | OPEN |
| R7 | activation | irpt-ycharts-generate (root .../ycharts) NOT APPLIED, HELD on the amendment 5 E3 guard. RIDER NAMED: IB-rt-11's intake/settings.json edit is a DECLARED BUILD INPUT of this function and this apply would ship it. E3 re-measured at HEAD: settings.json DECLARED, fixtures/holdings/security_mapping.json absent, parse.py declared by 0 of 214 functions -- the literal STOP condition is TRUE, so this root is not applied. ROLLBACK: none, nothing applied | a ruling from 2.0.0_SA_COO~B on the E3 guard |  | OPEN |

## Log

- 20260912T041223Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 13 leg(s)
