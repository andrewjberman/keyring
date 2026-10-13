# Deploy Completion Record
**Date opened:** 2026-10-13T13:34:04.878714+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T142306Z
**Deploy:** IRPT_BCKEND TO-IB-pr-512: put the two minimal holdings packages at the runner host's scheduled Online (started_by scheduler: irpt-directory-refresh-role, 13:30:36Z), digest-gated; keys s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz (rollback VersionId fMLoOI6a8ZwNFWZCJjjP90ZadyRg9nFg) and s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz (rollback VersionId qR5sZza4EjUT_cbGA5hLo0ar6zu2NfpI); cottonwood NOT written; pair IB-pr-510 packet sha256 c2b7275939d0
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 (both firms: run principal exists, assume ok, admitted by the fence, apply principal may put) and step 1 schedule and started_by scheduler | the reads recorded in the apply record | step 0 for 49financial and inflection: run principals irpt-49f-holdings-role / irpt-inf-holdings-role exist, trust the host role, are not denied by DenyForeignFirmPrincipals (role/*-49f-*, role/*-inf-*), hold GetObject on the package key and PutObject on the four holdings prefixes; applier user is on both fences and simulate-principal-policy allows PutObject on both package keys. Schedule: backstop 12:52Z returned NOT-YET; the host was started 13:30:36Z by irpt-directory-refresh-role (Scheduler irpt-directory-refresh, 09:30 ET): started_by scheduler; Online observed 13:31:14Z. Record: IB178-1_apply_record.json. | CLOSED 20261013T142306Z |
| L2 | s3-prefix | 49financial: start read equals the packet, candidate rebuilt equals the packet, put-object to the same key with the candidate metadata, new VersionId, read-back hash and metadata | new VersionId and read-back sha256 | 49financial: start read equal the packet (ETag 8b482c8d.., VersionId fMLoOI6a.., object sha256 fe4000cb..); candidate rebuilt equals the packet f945da68..; put-object to the same key (--server-side-encryption AES256, metadata members-sha256=97515201.. member-count=44): new VersionId UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD, new ETag 0013f7af..; read-back of that version hashes f945da68.. (equal), carries members-sha256 97515201.. and member-count 44. Rollback VersionId fMLoOI6a8ZwNFWZCJjjP90ZadyRg9nFg not used. | CLOSED 20261013T133554Z |
| L3 | s3-prefix | inflection: same four gates, put, new VersionId, read-back | new VersionId and read-back sha256 | inflection: start read equal the packet (ETag 5daec38f.., VersionId qR5sZza4.., object sha256 7036a650..); candidate rebuilt equals the packet 8709a0d5..; put-object same key (AES256, metadata members-sha256=14f55af0.. member-count=44): new VersionId PzhCs97qVBXkZcIjaOklHmzWiFsOFafM, new ETag 4a294eb1..; read-back hashes 8709a0d5.. (equal) with the candidate metadata. Rollback VersionId qR5sZza4EjUT_cbGA5hLo0ar6zu2NfpI not used. | CLOSED 20261013T133643Z |
| L4 | verify | cottonwood ETag unchanged; first read: one read-only SSM count per firm of leftover temp files (49financial pattern, inflection pattern), counts only, no delete | counts and the cottonwood ETag after | cottonwood package ETag 01387cef.. VersionId oyIYMVdh.. before and after (unchanged). First read: two read-only SSM commands (one per firm pattern), both Success rc 0, counts 0 and 0. The 14:15Z scheduled holdings refresh ran after both puts: 49financial, inflection and cottonwood all Success rc 0, 44 package members verified each, no Traceback; Branch B not triggered. Nothing deleted. | CLOSED 20261013T142306Z |

## Log

- 20261013T133404Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261013T133554Z LEG L2 closed: 49financial: start read equal the packet (ETag 8b482c8d.., VersionId fMLoOI6a.., object sha256 fe4000cb..); candidate re
- 20261013T133643Z LEG L3 closed: inflection: start read equal the packet (ETag 5daec38f.., VersionId qR5sZza4.., object sha256 7036a650..); candidate reb
- 20261013T142306Z LEG L1 closed: step 0 for 49financial and inflection: run principals irpt-49f-holdings-role / irpt-inf-holdings-role exist, trust the h
- 20261013T142306Z LEG L4 closed: cottonwood package ETag 01387cef.. VersionId oyIYMVdh.. before and after (unchanged). First read: two read-only SSM comm
- 20261013T142306Z CLOSED -- all 4 legs proven
