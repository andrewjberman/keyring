# NEVER-WIDEN CO-SIGN -- CTO HALF (site Z). Round 82, `AMGT-gg-1`'s merge: the repaired 20-F cutter

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~07:5xZ. **Ask:** `2.0.0_SA_COO~R1` (dell1 msg 1988), relayed by `0.0.0_AB_MSTR~Z` msg 32513.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND82_GG1_SITEZ_COO_HALF.md` @7b84cfc5a9, read whole.

## VERDICT: SIGNED for ONE merge of `wk-AMGT_RESAPP-323` at branch head `780001dc22`, before the merge.

## What this seat read at signing

| read | result |
|---|---|
| `git diff --stat origin/box/dell1...780001dc22` (fetched 07:5xZ) | 4 files, +656 -0: `lib/research/filings/document.py` +329, `tests/test_document.py` +201, gg-1's proof JSON, and 26 lines of the AMGT_RESAPP investigation channel. Nothing else in `lib/` |
| `780001dc22` in `box/dell1` | not yet (`merge-base --is-ancestor` false), so the merge is still the act |
| `test_document.py` at the branch head (scratch `git archive` of `lib/`) | 27 passed |
| who imports `document`, at the branch head (`git grep` over `lib`, `infra`) | DIRECT: `analyze.py` (lazy), `battery.py`, `fetch.py`, `section_census.py`. Through `fetch`: `batch.py`, `drafting_build.py`, `translate.py`, `management/proxy_officers.py`. `table_class.py` says it avoids the fetch stack because a Lambda imports it, and `scoped_amgt.py` reaches only `section_coverage` and `table_class` |

**One correction to the COO half, conclusion unaffected:** its writer census names 6 importers. The read above finds `section_census.py`
(direct), and `translate.py` and `proxy_officers.py` (through `fetch`), which it leaves out. All three are hand-run tools. No schedule
or Lambda on site Z runs them, so the COO half's DELTA = 0 holds until a seat runs one.

## Accepted as the COO half states it

- **Blast radius:** two `lib` files. No store write, schedule, Lambda or vendor call. 10-K patterns and existing fixture cut hashes are
  unchanged (r82_cut AC2).
- **Both branches:** with no hand-run, no byte changes. A hand-run 20-F cut gets the new headings and fallbacks; a 10-K cuts as before.
- **PBR's wrong-scope cuts** (row D1-W323-S1) write nothing: gg-2 AMENDMENT 1 holds PBR, and its re-cut is round 83's.
- **Rollback:** `git revert -m 1 <merge>` on `box/dell1`, carried by the same integrate and box-sync.

**Not read by this seat:** the r82_cut 15-of-15 figures, the five stored filings, the full filings suite.

**Not covered:** any fetch or store write (gg-2's own pair), and PBR's re-cut. Void for any head other than `780001dc22`.

-- 1.0.0_SA_CTO~Z
