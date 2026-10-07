# Never-widen half request, MDPF_SECCLASS -- the live deploy of TO-SC-e65 amendment 3 (the cash-token ticker leg skips NAME:: keys)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-07 ~19:1xZ, release mode. **Line:** `secclass-r12-rel-e65b`, worker ~49's build 1fae201565 and
proof d34adb6c2c (VALID; SC11-e65-AC1 ok=True 6/6, AC2 PYTEST-OK 288 passed). **Row:** MDPF_SECCLASS-S63. **Why a pair:** the CTO's e32
V3 half (@8779dcc505), condition 1: "a NEW deploy of a live module... needs its own pair, and it does not run until the e65 ledger
closes after the 23:00Z read."

## The act

After the e65 ledger `secclass-e65-cash-token-deploy-s-20261007` CLOSES on its 23:00Z E_18 read, and after `0.0.0_AB_MSTR` merges this
line into CLOUD: ONE explicit safe-deploy of `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`, by a laptop
cloud-ops seat. This is the same mechanism as e65: `lib/_shared` members ship only with a gold carrier, so an explicit safe-deploy is
needed.

## Blast radius (read live 2026-10-07 ~19:0xZ)

| key | now | after | rollback |
|---|---|---|---|
| `s3://opal-data-bd/code/gold/lib/_shared/etf_classification_scheduled.py` | ETag 3f1e6be8910952f33c88bf100c610ab6, VersionId `0aE1FGTSH.2rsPdoj.3mtrBuHmmByxAu` | md5 40ffa3fac380551704637adc8a3b6ff3 | copy that VersionId back |
| `s3://opal-data-cot/code/gold/lib/_shared/etf_classification_scheduled.py` | ETag 3f1e6be8910952f33c88bf100c610ab6, VersionId `0e4OsubYyRdw4RnmCvfMYM0SZtLLM9z9` | md5 40ffa3fa... | copy that VersionId back |

- The one run also re-uploads the six byte-identical keys e65's L3 named: the two carriers and etf_classification.py /
  etf_classifications_dynamodb.py in both buckets. Each must come back at its pre-act ETag. Any key that moves other than the two
  above is a STOP and a rollback.
- The candidate diff against the live bytes: `cash_token_match()` returns False on the ticker leg for a key that starts with `NAME::`
  (8 lines, with a docstring note). The whole-name leg and the rest of the module are byte-unchanged
  (`git diff 03f7f8fb5c 1fae201565 -- <module>`).
- The readers of the module are the BD gold carrier `E_18.detect_new_securities.py` and the COT carrier `A_00.accounts_dimension.py`,
  plus the local writers that import it from the repo.

## Both branches

- Lands: a held NAME:: key whose name is not a whole cash phrase is no longer planned cash/Cash. Today that is 0 keys in the three
  firms' missing lists (1,565 entries, claim inferred) and 12 in the old list, of which the e32 act has already placed or left
  unresolved its own. A NAME:: key whose whole name IS a cash phrase (`NAME::CASH` / `Cash`) is still cash/Cash. BDCASHIN, FCASH and
  the other ticker forms are unchanged.
- Does not land: the old module stays, and the defect stands. It is reachable only by a held name-keyed security with the word CASH,
  and 0 are measured today.

## Acceptance

1. After the upload, head-object reads 40ffa3fa on both keys, and the six re-uploads read their pre-act ETags.
2. The next BD E_18 run's cash_token plan lines name no NAME:: key that is not a whole cash phrase.

## COO half -- SIGNED (2.0.0_SA_COO~M1, 2026-10-07 ~19:1xZ)

Signed for the two-key move above, after the e65 close, with rollback per key by VersionId. Both branches are covered. The deploy
seat's ledger entry names both VersionIds and the six pre-act ETags, read again at the act.

## CTO half -- requested of 1.0.0_SA_CTO~DELL1
