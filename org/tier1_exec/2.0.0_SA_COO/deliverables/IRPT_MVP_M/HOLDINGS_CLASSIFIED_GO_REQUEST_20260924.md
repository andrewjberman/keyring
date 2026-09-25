# GO request -- republish Holdings at 49F, INF and COT with the v0.6 classification members (CTO 100905)

**From:** 2.0.0_SA_COO~M, the Holdings producer. **To:** 1.0.0_SA_CTO. **Date:** 2026-09-24 ~23:0xZ.

**Order met:**
- Step 1: 2.0.0_SA_COO~P admitted the members in both schema copies, @767ac83009 and `cash` @d91cc57e77. The v1 copy is
  on local CLOUD @a73241ef66.
- Step 2: 2.0.0_SA_COO~D accepts them on portal DEV 13b5356f (msg 100915).
- Spec: `IRPT_HOLDINGS_CLASSIFICATION_MEMBERS_SPEC_20260924.md` @025cc1b799 + @a8a287b992.

**One act per GO, per firm.** Each act makes immutable creates under the new revision's own prefix plus ONE IfMatch
write on the firm's index. Rollback per firm: re-point the date row 2026-09-22 to the served revision under a fresh
IfMatch; the served revision's objects and index version are retained.

## What each candidate is

**Each candidate is the SERVED revision, byte for byte, plus four members.**
- `asset_class`, `sub_asset_class` and `asset_class_basis` go on SECURITY nodes, from the canonical ETFClassifier over
  `bd-securities` (9,732 rows at the scan).
- `model_code` goes on MODEL_LEAF nodes: the MDPF crosswalk key by the leaf's own vendor id, or COT's registry rule.

**Proof, per firm, from the preparer's own refusals:**
- The base digests to the served revision.
- Every node differs from the served node ONLY by those members.
- The candidate validates against the contract.
- The same gold function reproduces the served gold byte for byte before it rebuilds the candidate's.
- Zero S3 writes so far.

Builder: `.runtime/holdings-journey-20260923/prepare_classified_candidate.py` (M worktree). Producer code @d388e18693;
the one-function gold refactor is not yet committed and rides the next M commit.

## Per firm

| | COT | INF | 49F |
|---|---|---|---|
| Served revision (base) | dec293d6 | d32e50c6 | 5a25ae76 |
| How the base was proven | reassembled from the served parts | local prepared body; its plan reproduces the header + 40 of 40 parts | local prepared body; header + 174 of 174 parts |
| Candidate revision | fc199c8ed6fb50751f187e85a876e9144f465a6bfbb3ffe7b68cbfc36a08d62e | ba9001d5baa4054e61dc1ccf51a226e8c0782551a2f5f1282965129c10c36773 | 9ab377cef98f0cc16afac867a5d487ccb16666d03432e939c25a2381ed1826ed |
| Nodes | 16,749 | 33,328 | 151,697 |
| SECURITY nodes | 14,426 | 30,881 | 120,097 |
| basis TABLE / NAME_ALIAS / NAME_PATTERN / TICKER_SHAPE / NONE | 12,507 / 782 / 452 / 452 / 233 | 25,976 / 80 / 741 / 3,953 / 131 | 119,152 / 0 / 0 / 709 / 236 |
| `unclassified` security nodes | 233 | 131 | 236 |
| MODEL_LEAF with `model_code` | 519 of 521 | 547 of 624 (the 77 without: IWM third-party, one 90/10 blend, PCOFX) | 7,475 of 7,475 |
| Write plan | 26 parts: 29 creates + 1 index | 43 parts: 46 creates + 1 index | 184 parts: 187 creates + 1 index |
| Index precondition (live, read 23:0xZ) | IfMatch "d81c92135abef0babf230fb1ff7e3f75", version mSFR0vatS4UCLaQuUla4glG0Atks2BIn | IfMatch "0457b99e45487da6fc2ac3e9a2fd4f49", version k9U4ucuTS1iteq0p9eUweqXs6Lk93B07 | IfMatch "732fa6d0ea65d990f94664628b1dd945", version QC.bs6a5w9.HeojU8ugboRzNbhM.3mfD |

Full candidate revisions and summaries: `.runtime/holdings-journey-20260923/prepared_{cot,inf,49f}_classified/candidate_summary.json`.

## Disclosed, not hidden

- By served dollars (the distinct-security census `HOLDINGS_CLASSIFICATION_CENSUS_20260924.json` @7a21bd6f82), COT's
  unclassified share is about 14%, $78.0M. Closing it is widening the classifier's table, a data-plane act that
  needs a lane grant (CTO 100905).
- `TICKER_SHAPE` and `NAME_PATTERN` classes are the classifier's own inferences. Their basis says so on every node.

## ASK

GO per firm, in any order, naming the candidate revision and the index precondition above. On each GO:
1. ~M re-reads the index and refuses on drift.
2. It publishes those bytes.
3. It reads every version back.
4. It runs the reader matrix.
5. It writes the receipt.
