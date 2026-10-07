# Deploy Completion Record
**Date opened:** 2026-10-07T06:34:47.657884+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T063536Z
**Deploy:** MDPF_SECCLASS-S39: roll back s3://opal-data-cot/code/gold/B_01b.classify_new_securities.py to VersionId _24mhLjaqbMSNl75DXKc7UjTnoG5B9nS (pre-8f67065e50 body) per CTO ruling CTO_RULING_MDPF_SECCLASS_S39_ROLL_BACK_COT_B01B_20261007.md; replaces Hh9lWlPap1OJnHH2MQMCmEr8_b14_KmP (04:16:37Z, unsigned). Rollback of the rollback = copy-object of Hh9lWlPap1OJ, which stays in version history
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R | activation | opal-data-cot code/gold/B_01b copy-object of _24mhLjaqbMSN over the key | new latest VersionId + copy-object output | 2026-10-07 06:34:58Z copy-object CopySourceVersionId _24mhLjaqbMSNl75DXKc7UjTnoG5B9nS -> new latest VersionId u_QyPqqoZOveegVfVxS6w9jrYX1Rl9i5, ETag eedfd1d1c5deb0c7e9e9e6100bbd3f77, 13737 bytes; replaced Hh9lWlPap1OJnHH2MQMCmEr8_b14_KmP (04:16:37Z, 14699 bytes), which remains in version history (7 versions listed after the act) | CLOSED 20261007T063536Z |
| V | verify | latest body byte-equal to git 8f67065e50^ blob, not equal to HEAD | cmp read-back | 2026-10-07 06:35Z get-object of latest (u_QyPqqoZOvee, 13737 bytes): cmp equal to git show 8f67065e50^:data/cot/scripts/gold/B_01b.classify_new_securities.py (13737 bytes); cmp NOT equal to HEAD a9a85869dc (14699 bytes) as the negative control. Pre-check before the copy: the source version read equal to the same blob | CLOSED 20261007T063536Z |

## Log

- 20261007T063447Z OPENED by 2.0.0_SA_COO~M with 2 leg(s)
- 20261007T063536Z LEG R closed: 2026-10-07 06:34:58Z copy-object CopySourceVersionId _24mhLjaqbMSNl75DXKc7UjTnoG5B9nS -> new latest VersionId u_QyPqqoZO
- 20261007T063536Z LEG V closed: 2026-10-07 06:35Z get-object of latest (u_QyPqqoZOvee, 13737 bytes): cmp equal to git show 8f67065e50^:data/cot/scripts/
- 20261007T063536Z CLOSED -- all 2 legs proven
