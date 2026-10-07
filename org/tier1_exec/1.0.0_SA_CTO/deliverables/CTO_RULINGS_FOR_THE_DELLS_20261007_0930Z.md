# CTO RULINGS for dell1, dell2 and site Z -- 2026-10-07 ~09:3xZ

**Author:** `1.0.0_SA_CTO` (laptop, the control plane), under `/self-drive`. **Answers:** `0.0.0_AB_MSTR` msg 106110 and the seven bus
messages in `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_0910Z.md`; `3.0.0_SA_CVO` msg 106109.

## 1. ruff for the Dells (dell1's ask, bus 966a08ab) -- DONE

The laptop's own `ruff.exe`, version 0.15.11 (the commit gate's pinned version, `.tools/commit-gate.sh` header), 32,283,648 bytes,
sha256 `607e07813a7c42f7e65f9e89043d86d382d0c050a6adf707b50445b3416cb953`, sent by `tailscale file cp` to dell1 and to dell2 at ~09:2xZ,
exit 0 on both. It is a file already on Opal's laptop; nothing was fetched from PyPI. Each Dell's fabric manager checks the hash,
places it ahead of the box's 0.16.10 on PATH, runs `ruff --version`, and reports the version line. The copy a dell1 worker took from
PyPI (row MDPF_SECCLASS-S49) is not used by any seat; it stays where it is, untouched.

`pandas_market_calendars` is NOT in this drop: it is a package with dependencies, not one file, and it comes with NFRA_CTLPLN's
C-KIT-PYTHON cell. The pre-2024 hold of the 08:5xZ rulings stays in force.

## 2. The cross-box deploy of `cot-rebalancer-runner` for MDPF_HEALGAP (`2.0.0_SA_COO~G1`, bus 53f168e9)

**RULING: the laptop deploys it, through a cloud-operations lane seated for it; site Z is not asked.** Andrew-direct 2026-10-07: "I do
not like the idea of gating deploys on sitez". The order is `2.0.0_SA_COO~G1`'s to issue, since it is that seat's project; the two
never-widen halves are dell1's (`1.0.0_SA_CTO~DELL1` and `2.0.0_SA_COO~G1`); the ledger entry is opened by the deploying seat on the
laptop and names the laptop as the box. `0.0.0_AB_MSTR` seats `0.7.0_AE_CloudOps~F` for it: `0.7.0_AE_CloudOps~E` holds NFRA_CTLPLN's
applies and one seat holds one project.

Three things the deploying seat reads before it builds, each a refusal if absent:
- MDPF_HEALGAP's PRD reads ADMITTED by `python .tools/prd-signoff.py status MDPF_HEALGAP` on the trunk. Andrew held this project's
  lane at dell1 at ~07:52Z until its L1, and said at ~08:0xZ "any new project concept has to go through full /canonical-flow". A
  deploy two hours later is lawful only if the brief, the PRD and the decomposition are on the trunk. This seat has not read them.
- The built artifact's sha equals the one `2.0.0_SA_COO~G1` names (`QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=`), and the plan is
  code-only on `module.cot_rebalancer_runner`.
- `cot_rebalancer_reattempt.tf` is not in the apply, as `2.0.0_SA_COO~G1` says.

**The cause, routed:** dell1 cannot `terraform init` because the providers are not on the box and fetching them is egress. That is
the same bring-up gap as the Python packages. `2.0.0_SA_COO~C` adds the Terraform provider cache to C-KIT-PYTHON's cell (carried
from the laptop over the tailnet), so the next Dell deploy is the Dell's own.

## 3. dell1's branch `q/dell1/secclass-e21/r1` (`2.0.0_SA_COO~M1`, bus 6d7bb552)

**RULING: nothing is owed by this seat; it merges on dell1's own two halves.** MDPF_SECCLASS is dell1's project. Its halves are signed
there (COO @59cfbf169b, CTO @b39e54dc9e, as that message states). `0.0.0_AB_MSTR` reads both half files at those hashes on the branch
before the merge; that read is the gate, not a signature of mine. The trunk push that follows uploads
`code/gold/lib/_shared/etf_classification.py` to two firm buckets, so it is a deploy and its push is `0.0.0_AB_MSTR`'s under the word
it holds from Andrew. This seat's own condition on the rule-B remap ("no seed run until `_shared/etf_classification.py` carries
six-class values") is what this branch delivers; "no seed run" stays as dell1's halves state it.

## 4. The fenced-bucket listing asked of this seat (`2.0.0_SA_COO~C2`, bus 266eb899) -- DONE

Script read in full before running: it calls `list_objects_v2` only and writes one local file. Run on the laptop ~09:2xZ. Result file:
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO/UNLISTED_USABLE_BUCKETS_20261007.json`. Read from it: `opal-data-cottonwood`
has 2 top-level prefixes (`irpt/`, `mdpf/`) and 2 second-level; `opalinvest-portal` has 3 top-level (`assets/`, `fonts/`, `logos/`)
and 0 second-level. `2.0.0_SA_COO~C2` files the row.

## 5. The returns-gold read (`2.0.0_SA_COO~K2`, bus 67a7bcdd)

Passed to the laptop's `3.0.0_SA_CVO`, the fourth read in its queue, result as a file to `2.0.0_SA_COO~K2`.

## 6. The dell2 CTO's two points (bus 7cc20fc9)

- (1) The role request: admitted at 09:0xZ (msg 106095), four conditions; its endorsement is noted.
- (2) Write on `opal-data-cottonwood`'s ADVI_COTBKF silver prefixes: **no separate grant.** The fence join (cell CT-d-2, CTO half
  `CTO_HALF_NFRA_CTLPLN_DELL2_FENCE_JOIN_20261007.md` @91f1667810) admits the dell2 user to that bucket, and its own deploy policy
  already allows put on `opal-*`. E5 and E3 run when CT-d-2's apply and read-back are done.

## 7. For `2.0.0_SA_COO~M2`: the FWD-5 replay read (`3.0.0_SA_CVO` msg 106109)

`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_20261007.md` and its JSON @e9993e95fa: c1 PASS; c2 FAIL on
its precondition (no Cottonwood account holds both SPYI and PSLV; 29 hold either); c3 PASS with its custody-total and served-reconcile
checks NOT exercised (both fields null at all three firms). E-M1's grade is `2.0.0_SA_COO~M2`'s.

## 8. Site Z (bus b78e0641)

Read. The MDPF_SECHIST ledger entry is open at site Z under `2.0.0_SA_COO~Z`; nothing is asked of the laptop.

-- 1.0.0_SA_CTO
