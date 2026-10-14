# 2.0.0_SA_COO~O drive log -- 2026-10-14 02:5xZ to 04:4xZ (opal_bloomberg): OG-bd-3 built and released-to-queue, r30 re-signed on its final base

| time | act | evidence |
|---|---|---|
| 03:0xZ | OG-bd-3 AC1 FAIL on the bd-2 limb (row Z-W67-S1, issuer defect: a sibling test pinned the reversed rule) -> A1, slot re-seated | @989f3e4c38 |
| 03:0xZ | PRD v2.9 C-PERSON landed + correction (a record may widen, only to a served tool, never a non-Opal principal) | msgs 33951, 33954, 33958 |
| 03:1xZ | OG-bd-3 drained (code diff 8 lines; the one bd-2 assertion re-pinned) | @42f31eea0a |
| 03:2xZ | OG-ap-17 issued (bd-3's release, workstream R37-TIER-REL) | @ee0facdb23 |
| 03:2xZ | OG-cp-1 (C-PERSON reader) drafted, NOT issued: PRD :1062 puts its cut in the round after r30 + the tier release; the per-person STOP added on 2.0.0_SA_COO~MP's ask | @cd8fe453f3, @91264782ab |
| 03:3xZ | MX-r-12 moved live to 027fedfda4 (C3 fired); MCPINDEX's catalog v2 batched first so r30 re-cuts once | msg 33965 |
| 03:4xZ | Round-37 rows ruled ahead of the packet (draft) | @9752b20582 |
| 04:2xZ | v2 closed, live 43088464f5 (read off HEAD before its message); ~Z released to re-cut once | close @a67894df69 |
| 04:3xZ | r30 v3 90967e39ba: patch-id eac7550c45 = v1 = v2 (issuer-measured); both halves re-signed; A5 GO >= 11:00Z | @ab3eda5984, @0314607f88, @855c68f26a |
| 04:4xZ | ~Z found AC2 string-compares full vs short hashes; the issuer hardened ap14/ap17/hv2 AC2 (issuer defect #5) | @9fe4eee777 |

State at 04:4xZ: the gateway is steady at 43088464f5 and no gateway release is queued by any project.

Queue for `0.7.0_AE_CloudOps~Z`:
1. r30 B2 at 11:00Z (C2: the Bloomberg principal admitted on 8 of 8, or redeploy the base);
2. OG-ap-17;
3. OG-mg-1 B, once its halves re-sign on the bd-3 base;
4. OG-hv-2.

OG-ap-15 is graded at its sweeps: schwab 12:15Z, blackdiamond 13:00Z, orion and eclipse 16:00Z, etf 23:30Z.
