# NFRA_CTLPLN -- ROUND ANALYSIS (L10), round 6, closed 2026-10-12 ~06:5xZ

Author `1.0.0_SA_CTO` (laptop). Slug: `3.0.0_SA_CVO~L` msg 108475 on `2.0.0_SA_COO~C` msg 108474; compile
`surprise-channel/adjudications/ADJUDICATION_v8.md` @8fb6a99089 (watermark 2026-10-12T06:40Z). The previous analysis is
`ledger/ROUND_ANALYSIS.20261009.md` (rounds to 2026-10-09; 0 REALIZED, 18 advanced, 6 not served, 2 moved); its grades stand
except where this file names a change. PRD v0.25 (FWD-27, FWD-28 added 2026-10-12; FWD-28 re-worded twice on COO~C's
measurements).

## 1. What the slug carries, and the rulings

| item | the CVO's read | ruling |
|---|---|---|
| TO-APPLY-9 AC2 | MET (C-S16): the signed key statement is live byte-equal | accepted |
| TO-APPLY-31 AC2 | MET and EXERCISED (C-S17): one real `draft_contract` call, ok=True outcome=post | accepted |
| W61-S8, W62-S1, W62-S6, W62-S7, W62-S8 | DISMISSED (C-S18..C-S22) | accepted; W62-S1 and W62-S6 were the two FWD-28 measurements that re-worded the PRD (v0.24, v0.25) |
| `round-close-check --round 6` | 42 orders, 41 complete, judgments 4 of 4 GRADED, self-graded 0, verdict REFUSED on two PROOF-BAD items | see 2 |
| D1-S8 | HELD to GRADUATE: TO-CT-x-1 complete @ef9332dbfd, but the row gate refuses a new remediation row while TO-CT-u-3/4/5 read staged | GRADUATES at the round-7 drain, when those three are terminal; not a round-6 condition |
| W61-S1 | ARMED, live, Andrew's: the laptop's sshd on 0.0.0.0:22, password login on, firewall rule RemoteAddress=Any, Wi-Fi Public | listed to Andrew with the one elevated line; FWD-27's laptop cell (B+D) closes it structurally; no agent can run it |

## 2. The two PROOF-BAD orders are the issuer's dispositions, owed before round 7 is cut

- `NFRA_CTLPLN.TO-CT-x-2` (dell click route, receive run and blocked download): AC3 FAIL, kept as row D1-S1. RULED: the order
  terminates as FAILED-WITH-ROW -- its `<status>` set terminal by the issuer with the row id as the disposition; the AC3 outcome
  re-enters through E3 ("click route on a Dell") in round 7, not by re-running this order.
- `NFRA_CTLPLN.TO-DELL-1` (dell identity apply, site Z): no proof instance under deliverables (project tree or the seat's own).
  RULED: a pre-tree order from the 10-06 cut whose act was superseded by the Dell identity work already graded (TO-APPLY-9's
  key statement is live); the issuer WITHDRAWS it with one line citing this analysis. No re-run.
With both terminal, `round-close-check --round 6` reads proof_bad 0 and the round counts finished on this box.

## 3. Grades (delta from 2026-10-09)

No FWD moves to REALIZED in round 6; the two MET judgments advance the FWDs their orders serve (the key statement: the
Dell identity outcome; the draft_contract call: FWD-20/26's successor in COMM_ASSIST, graded there). FWD-27 and FWD-28 are
new and ungraded: FWD-27 waits on Andrew's public keys and his one elevated line per box; FWD-28's cell CT-u-6 is merged and
its apply (CT-u-7) is signed on both halves and with `0.7.0_AE_CloudOps~U7`.

## 4. ENRICHMENT LIST for round 7 (ONE issuance, `2.0.0_SA_COO~C`)

E1-E8 as the 2026-10-09 analysis lists them (section "ENRICHMENT LIST"), unchanged, plus:
- E9 FWD-27: the packaging cell (`.tools/ssh-tailnet-enable.ps1` + `ssh-tailnet-verify.py`, built @ae15aef88e) and three
  per-box cells, each gated on Andrew's public keys and his elevated line; the laptop cell also disarms W61-S1.
- E10 FWD-28: CT-u-7 apply and exercise (R0-R3 as the pair states), then the `opal_naming` registry row for the firm-set
  module so the two class-(i) routes gain their firm check (a cell naming the row, LGIC owner this fabric).
- E11 D1-S8 graduation at the drain (the CVO's act once CT-u-3/4/5 are terminal).
Round 7 is cut only after section 2's two dispositions land. Workers haiku, high effort; keep-driving OFF; 60 m drive.

## 5. Owed outside the project

Andrew: public keys (muse, his own); one elevated PowerShell line per box (the laptop's first: it closes W61-S1); the
Tailscale ACL at his convenience.
