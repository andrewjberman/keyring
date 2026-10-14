# Deploy Completion Record
**Date opened:** 2026-10-14T15:24:04.521158+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R30: the release 29b refusal-arm sitting of the ticket service owner check -- two minted synthetic client users (B in 49financial, C in cottonwood) for ONE sitting; R0i the owner row of advisor A's input first; K1, K2, K3 each expected HTTP 400 with the one text, same body hash; tickets table count equal before and after; no ticket written, no mail sent; every minted row removed after exp and read ABSENT by GSI and ConsistentRead; signed pair COO blob 355d8e9e8a + CTO half @5389d0d949
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | verify | hashes; Lambda CodeSha256 Fg8MdfvC.. and IrptRequestsInputOwnerRead present once read; own grants simulated; markers 0 live open entries; R0i owner row of A's D1 input present and A's not B's; tickets COUNT before; pre-state ABSENT by ConsistentRead and GSI; offline proof of the K1 body; rows written and read back; tokens minted in memory | printed reads |  | OPEN |
| K | verify | K1 K2 K3 each once, HTTP 400 and the one text, same body sha256; a 503 is a STOP; a 2xx is BLOCKING; tickets COUNT after equals before | TICKET_ARMS_R30.txt six lines |  | OPEN |
| X | verify | after exp: both minted rows deleted (attribute_exists), two addresses ABSENT by GSI and ConsistentRead within a bounded 5 minutes | TICKET_REMOVAL_R30.txt four lines |  | OPEN |

## Log

- 20261014T152404Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
