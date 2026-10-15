# L4-R review -- ADVI_COTBKF PRD v0.11, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-15 ~19:2xZ. Asked by 1.0.0_SA_CTO~DELL1 msg 6151 and 2.0.0_SA_COO~C1 msg 6152 (both acked).
**Graded:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` @438c699be3 (v0.11) against v0.10 @4d488ab2f0, which this seat signed
(`ADVI_COTBKF_PRD_v0.10_RATIFIED_TEXT_REVIEW_20261012.md`).

## Verdict: REFUSE -- the C-RESTRICTED row is wider than Andrew's word

## The change (the whole diff: 17 insertions, 2 deletions)

1. Header `prd_version` v0.10 -> v0.11.
2. **CONTRACTS, C-RESTRICTED:** "no agent seat is in it" gains ", except ONE matching-job role for the length of one job (v0.11, Andrew
   2026-10-15)".
3. The v0.11 addendum at the foot. ENDPOINT is unchanged.

## The four checks

| Check | Result |
|---|---|
| Text against its pins | Andrew's words at `ANDREW_DIRECT_20261015_190xZ_D3CC_A_ONE_JOB_READS_RESTRICTED_CRM_ZIP.md` @6e96dd543a read "I agree with (a), let's see what we can do with that for now." The record's "What binds, verbatim in scope" item 1 lists option (a) as the card stated it: the job "reads the restricted CRM zip in memory; writes only account-link ids; sends no personal data out of the job; is logged", and item 3 says the grant "is withdrawn when the job ends". |
| Every operative constraint present | **NO.** The C-RESTRICTED row carries only "ONE matching-job role for the length of one job". None of the card's four limits is in the ratified text: in memory, account-link ids only, no personal data out, logged. The withdrawal at the job's end is implied by "for the length of one job" and is not stated. The addendum carries in memory, the four link columns, "no CRM value leaves it" and same-day withdrawal; it does not carry "is logged". The round-88 pair carries all of them, including logging as C1 (every AssumeRole listed from CloudTrail). But the addendum is history and the pair binds one act; the CONTRACTS row is the standing permission a later decomposition reads. As written, the row permits an agent role to read tax ids, dates of birth and license and passport numbers for a job's length with no limit on what it writes or sends. That is wider than Andrew approved. |
| No annotation, history or seat name inside the section | "(v0.11, Andrew 2026-10-15)" inside the row is an annotation. Nit; it goes with the fix. |
| CONTRACTS agrees with the counterpart PRD | ENDPOINT unchanged; C-SENSITIVE unchanged and consistent with the exception (the four fields stay in the raw files only). |

## What would make this signable

Bring the card's limits into the C-RESTRICTED row itself, in substance: the one role may GetObject the one CRM key only, for one
account-matching job; the job reads the zip in memory, writes only account-link ids (`commonwealth_account, bd_account_id, rule, tier`)
and match counts, sends no personal data out of the job, and every assume of the role is logged; the role and its exception are removed
when the job ends. Nothing else changes. This seat signs the next version on a re-read of that row alone.

## Not in question

The round-88 pair (`ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_{COO,CTO}_HALF.md`) covers the act well: one key, in memory, the column allow-list,
CloudTrail assume listing, the 23:59Z absolute withdrawal. This refusal concerns only the standing text.

-- 3.0.0_SA_CVO
