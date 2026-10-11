# NFRA_OPLGTW -- ROUND-34 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~22:4xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33409,
`remediations/REMEDIATION_v17.md` @8503c3f3e8. L8: `ADJUDICATION_v25.Z.md`. **Issuer:** `2.0.0_SA_COO~O`.

## 1. Round 34, as read

MAY-CLOSE: 9 of 10 complete, with OG-bd-1 STOPPED correctly before the deny, by its own census.
- **Z-S85 is disarmed:** trunk's `deploy-to-ec2.sh` has 5 allowlist references, up from 0, so a trunk-cut release no
  longer revokes the meeting allowlist.
- **CT-i-11 is live and corroborated on a second plane:** COMM_ASSIST's channel_poll reads 29 of 29 `failed: 0`, up from
  59 of 59 failing. That meets COMM_ASSIST's un-park condition 1 (its D2 read cell).
- 9 rows are dismissed and 4 graduate.
- Still owed from round 33: OG-tl-1 and OG-rl-16. **The CVO grades tl-1 now**, from dell2's row D2-S30 plus the live
  route. rl-16 stays dell2's debt.

## 2. Rulings

| row | ruling | cell |
|---|---|---|
| **Z-W57-S2** (ARMED): `blackdiamond_list_fees` has 2 unprofiled callers (one master_admin; 5 calls 10-01..10-08) | **The census did its job: the deny does not ship.** Admitting a principal by profile is Andrew's act (C8); the call is with him via `0.0.0_AB_MSTR~Z` msg 33359, and this seat has put it on his list. On his yes, OG-bd-1 re-cuts: write both profiles and grants, read both back, then ship the deny. On his no, the deny ships and the two lose the tool. **It stays ARMED, owner `2.0.0_SA_COO~O`, held on Andrew** | E4, conditional |
| **Z-S91**: each family's 16:00Z silver sweep drains the WHOLE shared DLQ and reports other families' failures as its own (also names Z-S77's actor) | **Code cell:** each sweep keeps only its own family's messages and returns the rest to the queue (visibility timeout 0), reporting only its own. Grade: one planted message of family A survives family B's sweep and is reported by A's | E1 |
| **Z-W55-S2**: the `.pptx` `market_update` key is content-addressed (`date=<UTC>/deck_<sha16>.pptx`); the `quarter` argument is unused | **Stated, not changed** (round-32 ruling W49-S3 chose one content-addressed rule for both writers). The `.pptx` release pair states the key form and how a reader finds a quarter's decks: list `date=` partitions in the quarter. The vestigial `quarter` argument is validated but documented as not naming the key | E2 (the release) |
| **Z-S92**: `gateway/teams/bearer` is readable by `cloudops-dell-agents-group` with no named consumer | **READ first:** name the dell consumer from CloudTrail `GetSecretValue` events on that secret (90-day management events), per principal. **None in 90 days:** remove the group's read under a pair. **One found:** it gets its own bearer, the commassist pattern. Record each holder's reason | E3 |

## 3. ROUND 35 -- cut in ONE issuance

E1 (per-family DLQ drain), E2 (the `.pptx` OG-mu-1 release, after its grant, with the key-form statement), E3 (Teams bearer
holders: read, then narrow or split), E4 (OG-bd-1 re-cut, ONLY on Andrew's admission answer).

-- 1.0.0_SA_CTO~Z
