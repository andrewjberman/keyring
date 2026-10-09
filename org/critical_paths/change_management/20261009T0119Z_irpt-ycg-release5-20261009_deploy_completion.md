# Deploy Completion Record
**Date opened:** 2026-10-09T01:19:16.947005+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND APPLY-Y72: irpt-ycharts-generate release 5 on dell2 -- E11 + the E9 report modules (custody_submission.py, composition.py, repository.py), superseding release 4 which rolled back on the E11 import gap (row D2-S16)
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks at pin 2f3ee8c15b | pin an ancestor of origin/box/dell2 rc 0; census changed_members=3 exactly composition.py custody_submission.py repository.py; live CodeSha256 Un0wVZqj..; rollback S3 version recorded | git fetch origin then git merge-base --is-ancestor 2f3ee8c15b origin/box/dell2 -> rc 0; release-census irpt-ycharts-generate --pin HEAD (50a1eb9849) -> changed_members=3, EXACTLY the declared set: composition.py (built 5b896004af77 live 6d2c3696d030), custody_submission.py (420ccd097831 / e347d1d198d0), repository.py (f01fcf549e8e / f255335beb26); live CodeSha256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= == the declared live and rollback target; rollback S3 object version recorded nA7hze1zlQfF55Q05.Vxr4E3v8kCE7HW, which is the version this seat re-promoted during the release-4 rollback, so the chain is continuous | CLOSED 20261009T011941Z |
| L2 | s3-prefix | the built artifact on the lambda-artifacts prefix, PLUS the symbol closure on the UPLOADED zip | build-and-upload SHA256 equals 4HEH1aDNa39+vwLFK24SldMOBit/hiBKF4aQjlsU1zk= with write VERIFIED, and symbol_closure.py on that zip prints missing=0 and symbol_closure PASS before any apply (CTO condition) | build-and-upload.sh: SHA256 4HEH1aDNa39+vwLFK24SldMOBit/hiBKF4aQjlsU1zk= == the declared built sha; s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip write VERIFIED (size 592042, sha256 metadata match), VersionId SbkpaWGWi6TNw0UFUvnvcN8tO96VLfOL. SYMBOL CLOSURE run on the UPLOADED ZIP, not a local temp copy: the object was downloaded back BY VERSION and hashed to 4HEH1aDN.. (592042 bytes) before the check, so the subject is provably the uploaded artifact. symbol_closure.py -> modules=62 pairs=273 missing=0, symbol_closure PASS. This is the CTO condition that exists because of row D2-S16, and it is the gate release 4 would have failed | CLOSED 20261009T012153Z |
| L3 | activation | irpt-ycharts-generate code (targeted apply of the ycharts root) | plan 0/1/0 on s3_object_version + source_code_hash only; live CodeSha256 re-read == built; re-plan 0 |  | OPEN |
| L4 | verify | the import census GATE plus the E11 offline suites and the X-1 actor read-back | import census failed:{} -- it gates everything after it (CTO condition), any failure goes straight to branch B; pytest 3 passed and 66 passed 2 skipped; X-1 graded on all THREE read-back booleans taken BEFORE any delete |  | OPEN |

## Log

- 20261009T011916Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261009T011941Z LEG L1 closed: git fetch origin then git merge-base --is-ancestor 2f3ee8c15b origin/box/dell2 -> rc 0; release-census irpt-ycharts-gene
- 20261009T012153Z LEG L2 closed: build-and-upload.sh: SHA256 4HEH1aDNa39+vwLFK24SldMOBit/hiBKF4aQjlsU1zk= == the declared built sha; s3://opal-3134768884
