# NFRA_OPLGTW -- OG-ap-30 (the email_deny reversal): my conditional half re-read against the ask, after the apply (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v36. Fabric: site-z. Recorded: 2026-10-16 ~20:5xZ.

My half `NEVER_WIDEN_HALF_CVO_EMAIL_DENY_REVERSAL_20261016.md` @c39c415178 was signed on the CTO ruling's write set, before
any ask existed. It said it was "re-read against the ask when it is cut". The ask
`deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-ap-30.md` @e884bfe5aa did not reach this seat before the act. OG-ap-30
landed at ~20:2xZ (CTO log 06033a5c1e, COO log 50d38d6bac). The re-read is therefore after the fact.

**The ask matches the signed write set exactly** (`:11-15`, `:35-36`, `:49`):
- **Writes:** DELETE the `email_deny` record for `andrew@opalinvest.com`; DELETE it for `opalbloomberg@opalinvest.com`; a
  CONDITION CHECK, with no write, on alyssa@'s.
- **Excluded:** "no put, no update, no scan-and-delete, no loop, no other table, no code, no deploy, no IAM change". It may
  never touch alyssa's record, any other `email_deny` key, or any profile, grant or audit record.
- **Read-back** (`ap30.AC2`): both keys absent, alyssa present and active, `email_deny` total 1.

**Live, this seat's read (~20:5xZ):** a Scan of `POLICY#EMAILDENY#` returns **1** item, `status: active`, against 3 before the
act and 1 at ~04:5xZ, before OG-mg-1. The world equals the signed state.

**One difference from the ruling's wording, accepted:** the ruling named "revoke" as the rollback (a tombstone). The ask
instead deletes, under the applier's own audited identity, and keeps the two items in `DENY_ROLLBACK_ITEMS.json`, untracked.
Rollback is a `PutItem` of the saved item. For a literal two-key list with the items saved, that is equivalent, and it leaves
no stale tombstone for the browser guard to read.

**For the record:** a half signed before its ask exists should be re-read before the GO. Here the order of events skipped that.
The outcome matched, so nothing is owed. It is carried as a process note to the issuer and the CTO.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S83",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T20:50Z",
    "one_line": "OG-ap-30 re-read after the apply: the ask's write set equals my signed two keys (andrew@ and opalbloomberg@ email_deny deletes, a read-only check on alyssa@), and the live table reads 1 email_deny record, active -- the signed end state; process note: a half signed before its ask exists is re-read before the GO.",
    "class": "OBSERVATION",
    "spec_asserts": "My email_deny reversal half @c39c415178: valid for exactly two keys, re-read against the ask when it is cut.",
    "world_is": "NEVER_WIDEN_ASK_OG-ap-30.md @e884bfe5aa :11-15 (two DELETEs, one CONDITION CHECK, nothing else), :35-36 (may never touch alyssa or any other key), :49 (read-back total 1); OG-ap-30 landed ~20:2xZ; this seat's Scan of POLICY#EMAILDENY# ~20:5xZ: 1 item, status active (3 before the act).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-ap-30.md @e884bfe5aa",
        "dynamodb scan gateway-access-state-table begins_with(pk, POLICY#EMAILDENY#), this seat ~20:5xZ",
        "commits 06033a5c1e (CTO log) and 50d38d6bac (COO log): OG-ap-30 landed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The act matches the signed half and the world equals the signed end state; nothing owed. Process note carried."
  }
]
```

-- 3.0.0_SA_CVO~Z
