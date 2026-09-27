# Deploy Completion Record
**Date opened:** 2026-09-27T02:54:08.980851+00:00
**Status:** OPEN
**Deploy:** Window 7: the Analysis chain second attempt (packet 3ab51a52 = fffdca65 + D1-D5; CTO @c226ade7a3, CRO @d9b4142aa6; Andrew 'yes to all three' @6039c2f680); principal kept until jobs terminal (120-min cap); K1-CRED deleted after the logins
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | served pins re-read (generate G/TqLPdL, resident fe64236bbb-xv); pre-read + censuses; put + read-back |  | OPEN |
| K1C | verify | K1-CRED deleted after ~D and ~Y logins (CRO condition) | ParameterNotFound |  | OPEN |
| V1 | verify | the chain outcome | K4 branch; K5 job terminal (READY + report id, or named refusal); K10; vendor calls named from the journal |  | OPEN |
| D1 | verify | K1 delete after every job is terminal | failing read + CloudFront login refused + ~D reload /login |  | OPEN |
| A1 | verify | route audit + write-set trace | 0 outside the classes; keys traced to K4/K5/K9; users == baseline; no auth after last exp |  | OPEN |

## Log

- 20260927T025408Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
