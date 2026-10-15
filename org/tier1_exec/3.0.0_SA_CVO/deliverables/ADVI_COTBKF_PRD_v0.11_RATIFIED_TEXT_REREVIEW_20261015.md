# L4-R re-review -- ADVI_COTBKF PRD v0.11 @e1c831e31c, ratified-text half: the C-RESTRICTED row only

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-15 ~19:2xZ. Asked by 1.0.0_SA_CTO~DELL1 msg 6155 (acked), answering this seat's refusal
`ADVI_COTBKF_PRD_v0.11_RATIFIED_TEXT_REVIEW_20261015.md` @7025977e0e.
**Graded:** the whole diff 438c699be3 -> e1c831e31c, which is that one row (1 insertion, 1 deletion). Everything else stands as read in the refusal.

## Verdict: SIGN

The row now carries option (a)'s limits itself, set against the card terms at `ANDREW_DIRECT_20261015_190xZ_D3CC_A_ONE_JOB_READS_RESTRICTED_CRM_ZIP.md` @6e96dd543a:

| Card term | The row's text |
|---|---|
| one named read role, one matching job | "ONE matching-job role for the length of ONE account-matching job"; "its allow names the one CRM key and nothing else (no list, no write)" |
| reads the zip in memory | "reads the zip in memory only, never to disk" |
| writes only account-link ids | "writes ONLY account-link rows (`commonwealth_account, bd_account_id, rule, tier`) and counts, and a criterion fails the job on any other column" |
| sends no personal data out | "no CRM value (name, tax ID, date of birth, address, license or passport number, or any other column) leaves the job in any output, log, message or commit" |
| is logged | "the job's run record is its log, listing every AssumeRole on the role" |
| withdrawn when the job ends (item 3) | "removed the same day the job ends, by 23:59Z at the latest" |

## Nit (not a ground to refuse)

Andrew's item 3 reads "withdrawn when the job ends"; the row allows removal later the same day. The idle window is bounded by 23:59Z, and
every assume of the role is listed (pair condition C1), so a use outside the job is visible. Removing the role as the job's last act would
match his words exactly. The "(v0.11, Andrew 2026-10-15, option (a) of call d3cc)" annotation inside the row remains; drop it at the next edit.

-- 3.0.0_SA_CVO
