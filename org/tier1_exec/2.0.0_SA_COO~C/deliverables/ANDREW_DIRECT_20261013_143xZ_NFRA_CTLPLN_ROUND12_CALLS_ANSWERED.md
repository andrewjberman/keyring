# Andrew-direct 2026-10-13 ~14:3xZ at the 2.0.0_SA_COO~C terminal -- NFRA_CTLPLN round-12 open calls answered, and his answers on the acts only he can do

**Recorded by:** `2.0.0_SA_COO~C` (laptop), same turn. **Cards answered:** the two cards printed at this terminal ~14:2xZ (`/open-calls`, forks needed to cut round 12 wide).

## 1. Andrew's words, VERBATIM

> 1.) Yes sure. 2.) Rec approved. Then onto the acts only I can do: for FWD-27, check that this is not already done as I may have done it across all boxes (check this box first, we can have MSTR issue an order for the other managers to check their respective boxes). Regarding FWD-14, what do you need from me exactly here? FWD-12, I've run it below: [the output of `python .tools/open-calls.py list --all --cloud`, read 2026-10-13T14:35:36Z: boxes=4 read=4 absent=none open=13 (fork 0, act 13) closed=105] . Regarding FWD-17, not sure what you are asking for here. Row S9112 this can be done programmatically, i shouldnt need to be involved directly.

## 2. The rulings, as they bind

| card | question | ruling |
|---|---|---|
| CALL 1 | May one Dell be taken offline on purpose, once for FWD-9 (a box holding a scarce account switched off, another box takes it) and once for FWD-11 (a box restarted mid-round, nothing lost)? | **YES.** The REC rides: dell1, at most 15 minutes each, its manager parks the seats first, a time announced in advance. |
| CALL 2 | The `firmAccess.ts` carrier to PROD: (a) cherry-pick the one commit `53506d49` now, or (b) wait for the CRO's brief? | **(a), REC approved.** A DT cherry-picks `53506d49` alone onto portal PROD through `/prod-deploy`; the receipt names the pages touched and their class. No whole-DEV promote. |
| S9112 | The purge of the data proxy log group's pre-fix events and the invalidation of the refresh tokens in the 16 recent lines | **Delegated: "this can be done programmatically, i shouldnt need to be involved directly."** It is no longer an act only Andrew can do; a seat performs it under an order (the log purge is a deletion: this sentence is his confirmation for it). |

## 3. The other acts, as measured at this terminal after his answer

- **FWD-27, measured 2026-10-13 ~14:4xZ from the laptop** (`python .tools/ssh-tailnet-verify.py --user probe-only`): all four boxes (laptop 100.96.167.100, sitez, dell1, dell2) answer port 22 and still ADVERTISE `publickey,password,keyboard-interactive`, so password login is ON on every box. On the laptop itself the firewall half is done (`OpenSSH SSH Server (sshd)` rule disabled; `OpenSSH Server (Tailscale only)` enabled, remote 100.64.0.0/10) and `sshd_config` sets no `PasswordAuthentication` (default yes). The script `.tools/ssh-tailnet-enable.ps1` has a `-DisablePassword` switch that has not been applied on any box. Known defect (msg 108698): a first install leaves the default sshd rule enabled.
- **FWD-14:** what is needed is stated in the COO's reply (the seven sessions, and one refused attempt from off the private network); the logon records on each box are read by seats.
- **FWD-12:** the cluster list was read by Andrew (above). The outcome still needs one Dell-raised call answered by him and that answer read on the Dell.
- **FWD-17:** the DONE WHEN (PRD line 187) is "one delivered package's record read aloud to Andrew, including what was not checked"; the COO's reply says what that asks of him.
