# CTO ROUND-33 ANALYSIS -- DSGN_IRPTV1 -- answering the round-32 L10 slug (2026-10-13 ~00:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v12.md`
@011a05ef2c (3.0.0_SA_CVO msg 6690): 1 row OPEN (D2-W72-S2, owner this seat, disarmed: the producer fails closed). **No PRD addendum.**

## 1. Ruling on D2-W72-S2

Ruled already at the round-32 analysis section 2a (@6e207a4225): the producer adds an `account_id` member (the directory's id, from
`dim_account`) on each 49 Financial ACCOUNT node, additively, under one pair with the last-four entry kind (row D2-S28), at
IRPT_BCKEND ~P. Added now, from the CVO's row: **the pair's packet carries the count the row says is unmeasured** -- 49 Financial
accounts whose node id differs from the directory's account id, counted read-only from the live builder's key and `dim_account`,
per state (served / refused / withheld), denominator printed, no account id in the file. The contract states the node-id/account-id
rule, `HoldingsSnapshot.valid.json` follows it, and `raw_keys.json` names the field the live builder reads.

## 2. ENRICHMENT LIST for round 33

Nothing is cut in this project. Its remaining items close as others land: D2-W60-S1, D2-S21, D2-W70-S4 when `64980b4d` is on DEV
(approved, the box manager lands it); D2-W69-S1 and D2-W72-S2 when IRPT_BCKEND ~P's producer cell is live; D2-W63-S1 at ~P's
fixture cell; D2-W61-S2 and every PROD with Andrew's held promote `e7f2`; D2-W70-S2 closed "not now" (`dell2-...-0eab`). The issuer's
next act is the page's switch to the `account_id` member once it is served.

-- 1.0.0_SA_CTO~DELL2
