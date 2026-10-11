# COMM_ASSIST decomposition -- round 14: deploy the round-13 package; the channel_poll cure (conditional); E1 carried (issuer 2.0.0_SA_COO~ZZ; cut 2026-10-11 ~01:4xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO~Z`'s round-13 analysis `ledger/ROUND_ANALYSIS.round13.md` @08b06f5d33 (msg 33121). Its enrichment
list is D1 (deploy E2 + E3 now), D2 (the channel_poll cure, conditional on D1's `error` field) and E1 (carried, ruling 2).
PRD v0.3 ADMITTED. FWD-3, FWD-4; C-MAIL; C-PACKAGE.

**Measured at the base (`box/sitez` `2fd32e12c2`, the pin, ~01:3xZ):**

- Live: both functions are at `SFSTGBQX...`, NFRA_CTLPLN `TO-APPLY-31`'s package built at `bde0c0fc90` (deploy `3af6f043b3`, 2026-10-09 23:03Z).
  So the live package is NOT COMM's round-12 package. The packaged-path diff `bde0c0fc90..2fd32e12c2` is exactly round 13's two
  files (+31 -9); root and module `.tf` are unchanged (COO half
  `deliverables/2.0.0_SA_COO~ZZ/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R14_DEPLOY_20261011.md`).
- `d1_errorfield.py` at base: 60 `channel_poll` lines in the last hour, 60 failed, 0 with an `error` field, 0
  `ingress_step_failed[channels]`.
- E1: `0.0.3_BG_BBGTerminal` holds the opalbloomberg@ gateway session. On the RAVC ask (msg 33122) it replied NOT SENT, held
  for Andrew's word under its seat hold (msg 33123). It recorded this as NOT-ATTEMPTED-BY-POLICY, not a tool refusal. The ask
  is in front of Andrew at that terminal and at the site Z MSTR's (msg 33074).

**Rule 24.** Domain: the analysis's enrichment list. D1 is one WORLD act and one cell. D2's stated precondition (D1's `error`
field names the cause) is unmet at the cut, so it is NOT cut. It enters this round by amendment, citing the read, and writes
whichever file that cause names. E1 has no worker chain: its act is the BBG seat's send on Andrew's word, and its grade is the
issuer's real run (`r13/checks/check_e1_mail_day.py`). Values D1 does not move: FWD-4's exercise; channel @mentions reaching him.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-f-1` (D1) | ONE targeted `safe-apply` of `module.ldo_001` from a clean detached checkout at `2fd32e12c2`, code only, under the never-widen pair, with its NEVER-2 ledger `comm-assist-r14-deploy` | FWD-3, FWD-4 | WORLD | chain 1, `0.7.0_AE_CloudOps~CA` |
| `CA-f-2` (D2) | NOT CUT: conditional on D1's `error` field | FWD-3 | -- | -- |
| `CA-e-1` (E1) | carried: the CA-e-1 text sent once from `0.0.3_BG_BBGTerminal`'s opalbloomberg@ session on Andrew's word; else his own act | FWD-4 | WORLD | chain 0 (the BBG seat and the issuer) |

`fanout: 1 of 1 chains, cap 8, reason: one deploy cell; D2 is conditional and uncut; E1 has no worker chain.`

Battery: `comp-schedule` RUN (the act creates no schedule; the ingress keeps its 1-minute clock; the End of Day window
20:00Z-21:45Z is a Branch B stop). `comp-iam` RUN (no policy moves: Branch A is code hash only). `comp-adversary` on the half:
- a second writer (NFRA_CTLPLN) moves the live hash before the act (Branch B: re-measure);
- a package built from the moving trunk (pinned checkout);
- the ~60 `ingress_step_failed` lines an hour read as a regression (named in the half as intended);
- the import-time registry read (named in the half; same failure outcome).

**A1 (2026-10-11 ~02:5xZ) -- D2's stated precondition is MET, and the cell is cut as a ROUTE.** CA-f-1 APPLIED (`c583d4f9e5`; live
`nIQW+3Xv...` 02:17Z). Its `error` field reads `route=teams status=404` on every invocation (rows Z-S10, Z-S11). COMM's client path
equals the gateway source's route, and the same prefix's chats route is served. So the cause is the deployed gateway not
serving `/hx/teams/teams`, which is outside COMM's write surface. Per the analysis ("or routes it to the owner the error names"),
`CA-f-2` is a route to NFRA_OPLGTW's issuer, with no COMM order. Its done-when is unchanged: an hour of `failed=0` and one real
channel @mention reaching Andrew, read by the issuer after the gateway serves the route.

**The issuer's real run at close (not a cell):** `d1_errorfield.py` naming the cause, which decides D2. E1's read on the send
day. The FWD-3 full-day read after D1.
