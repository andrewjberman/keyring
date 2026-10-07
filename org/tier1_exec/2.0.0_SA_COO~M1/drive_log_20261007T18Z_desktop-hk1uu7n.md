# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-07 18Z

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL. RELEASE MODE.

| tick (UTC) | limb | outcome |
|---|---|---|
| ~18:0xZ | release | e48 clean-name write v2: precheck matched the signed numbers; WROTE 1360/1360; L2 ConsistentRead 1360/1360; ledger CLOSED @194ed263a8; published r2 |
| ~18:1xZ | release | e53 amendment 2 drained (~54, VALID, readers 7/7); cand-dell1-secclass-e53-r11 (portal 35002195) to the laptop CTO. e55/r2 LANDED (d06 52b9c843) |
| ~18:2xZ | release | e49 re-plan at contract 0.8.0: DIRECT 293 entries = same-placement subset of the signed 301; WROTE 278 keys, verified 278/278, ledger CLOSED @f31f9d63bf |
| ~18:3xZ | release | TO-DEPLOY-e66 to laptop ~S @a51619be90 (AC1/AC2 FAIL at base, control PASS); GO for the laptop CTO. e49 AI leg RESERVED card @12b69d757e |

Decisions closed this hour:
- A signed half's DIRECT leg may run on a re-plan that is a same-placement subset of the signed set. A superset, or a moved placement,
  goes back to the signers.
- An "AI leg within Andrew's word" ruling over a population his word does not name goes to Andrew as a sized card. The issuer does
  not run it on a reading.

Owed:
- the e32/e50 rebuild;
- the e66 push and nightly (owned by ~S);
- the E_18 / e65 close (23:00Z);
- the e57e61 apply and verify (14:00Z on 10-08);
- the e42 L2 read (12:45Z on 10-08);
- Andrew's word on the e49 AI leg;
- round 12, with the S60 COT producer cell first.
