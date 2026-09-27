# Deploy Completion Record
**Date opened:** 2026-09-27T14:55:54.625794+00:00
**Status:** OPEN
**Deploy:** window 14: K8, the FIRST real export, re-cut on local portal DEV 55bbdd71 (IV-e-64: submit/receipt/download carry selectedTenant) -- window 12's shape (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W14_K8_EXPORT_20260927.md); no vendor call; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; pins + portal HEAD 55bbdd71 re-read equal; pre-read + censuses; put + read-back |  | OPEN |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound |  | OPEN |
| K8 | verify | ONE export | exactly 1 export POST; READY with %PDF page_count>=1 (served object) or a named NOT_READY/DEPENDENCY_UNAVAILABLE; render token ParameterNotFound |  | OPEN |
| D1 | verify | K1 delete after the export is terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; export rows/objects traced to the exportId; users == baseline; 0 new media in git; K1 absent |  | OPEN |

## Log

- 20260927T145554Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
