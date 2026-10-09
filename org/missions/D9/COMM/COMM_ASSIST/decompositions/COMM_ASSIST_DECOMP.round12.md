# COMM_ASSIST decomposition -- round 12: the FWD-4 mail deploy after r29 (issuer 2.0.0_SA_COO~ZZ; cut 2026-10-09 ~09:3xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO~Z`'s round-11 analysis `ledger/ROUND_ANALYSIS.round11.md` @4c14e95965 (msg 32606). Its enrichment list is
E1 (the deploy) and E2 (conditional). PRD v0.2 ADMITTED (`805fec22c5`). FWD-4, FWD-3; C-MAIL; C-PACKAGE.

**Measured at the base (`box/sitez` `b1b8f5b4fe`, ~09:2xZ):**

- Live: both `teams-global-chat-assist-handler-lambda` and `-ingress-lambda` carry `CodeSha256` `xWURpe/n...` (round 7, built at
  `a5fde91788`); neither has `MAIL_BEARER_SECRET`; the exec policy is at v3; `gateway/mail/commassist-bearer` is ABSENT.
- NFRA_OPLGTW `TO-OG-ap-3` (r29 apply, `0.7.0_AE_CloudOps~Z`) is `pending`, with a window of 11:00Z-23:00Z. It creates that secret.
- The packaged-path diff `a5fde91788..b1b8f5b4fe` is 12 files: 5 `teams_chat/` files (COMM rounds 8, 9 and 10) and 7
  `infra/logic/registry/` files, which sit OUTSIDE COMM and are measured additive (0 removed, 0 changed). This is wider than the
  analysis's three round-9 commits. The COO half binds the measured diff
  (`deliverables/2.0.0_SA_COO~ZZ/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R12_MAIL_DEPLOY_20261009.md`).

**Rule 24.** Domain: the analysis's enrichment list. E1 is one WORLD act and one cell. E2 has a stated precondition (the ~22:00Z
FWD-3 read reports `adds_up=False`) that is unmet at the cut, so it is NOT cut. If the read fails, it enters as this round's
second cell, recorded as an amendment to this file citing the read; the condition was declared in the analysis, not invented
mid-round. Values E2 does not move: FWD-4.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-d-2` | Commit `var.chat_assist_mail_bearer_secret_arn`'s default as the ARN of `gateway/mail/commassist-bearer`, then ONE targeted `safe-apply` of `module.ldo_001` (code + env var + one policy ARN) under the signed never-widen halves, with its NEVER-2 ledger. GO waits on `TO-OG-ap-3` AC1 PASS plus the CTO and CVO halves | FWD-4 | WORLD | chain 1, `0.7.0_AE_CloudOps~Z` |
| `CA-c-2` (E2) | NOT CUT: conditional on the ~22:00Z FWD-3 read | FWD-3 | -- | -- |

`fanout: 1 of 1 chains, cap 8, reason: one deploy cell; E2 is conditional and uncut.`

Battery: `comp-schedule` RUN (the act creates no schedule; the ingress keeps its 1-minute clock, and the End of Day window
20:00Z-21:45Z is a Branch B stop). `comp-iam` RUN (1 policy, 1 statement, +1 ARN, read live at v3). `comp-adversary` RUN on the half:
the passed-as-`-var` unwiring, a stale package (Branch B import test), and the secret's value (never read here).

**The issuer's real run at close (not a cell):** one real considered mail arrives as a text with a draft and the right flag, and one
that does not name him sends nothing. Separately, the ~22:00Z FWD-3 full-day read closes rows S1/S2 and decides E2.
