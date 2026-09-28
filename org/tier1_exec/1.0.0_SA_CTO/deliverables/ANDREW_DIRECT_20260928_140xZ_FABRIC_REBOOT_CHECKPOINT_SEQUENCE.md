# ANDREW-DIRECT 2026-09-28 ~14:0xZ at the 1.0.0_SA_CTO terminal -- the laptop fabric reboot checkpoint

**Verbatim:** "I agree with the recommended process here. Only thing I want to note is that COO~D is doing a lot of
work right now and I'd like their agents to have a clean winddown. I think each COO should write some kind of
standardized /log or /handoff so we can pick them up where they left off post-reboot. With that said, manage the sequence
of events to the reboot on the fabric according to your earlier recommendations."

**Context:** the device has been up 95 h, with 5.6 of 31.7 GB memory free (measured ~13:3xZ). Andrew asked for a
checkpoint analysis; this seat recommended rebooting AFTER the S19 purge CLOSE and push, with no deploy left half-landed.

## The sequence (managed by 1.0.0_SA_CTO; 0.0.0_AB_MSTR executes the device steps)

**Phase A -- now: start nothing new**
- No new walk window, deploy, TO issuance or worker seat on any seat.
- In-flight work finishes:
  - 2.0.0_SA_COO~P: irpt-status rebuild 3, apply plus live verification, then its ledger closes;
  - 2.0.0_SA_COO~M: R4's N1 (read-only). The rest of R4 is post-reboot.
- **2.0.0_SA_COO~D, a clean wind-down:**
  - seat NO further worker;
  - each running worker (IV-e-70, IV-e-74, IV-e-79) finishes its current criterion or stops at a clean point, commits
    what is done in its worktree, and writes its state into its task order's status note;
  - ~D drains what is complete. Nothing is left uncommitted.

**Phase B: 0.0.0_AB_MSTR's S19 purge CLOSE**
- The rewrite and the force-push complete;
- every worktree re-syncs by MSTR's named steps;
- local CLOUD equals origin/CLOUD (ls-remote read), which also puts the laptop's ~640 unpushed commits on origin.

**Phase C: every seat checkpoints in the standard form**
1. `/log`: the session log, committed (`org/ref/SESSION_LOG_STANDARD.md`).
2. `/handoff save`: the reinstantiation block, persisted to `org/{tier}/{serial}/handoffs/`.
3. `git status` clean of its own work in every worktree it owns; commits pushed or integrated by MSTR.
4. A one-line **READY-FOR-REBOOT** to 0.0.0_AB_MSTR, citing the log and handoff hashes.

Seats: 2.0.0_SA_COO~P, ~M, ~Y, ~D; 3.0.0_SA_CVO; 4.0.0_SA_CRO; 0.6.2_AE_PartnerETL~S; 1.0.0_SA_CTO.

**Phase D: the reboot**
- 0.0.0_AB_MSTR confirms: all READY lines are in; no open deploy is mid-apply (every worktree's `.open_deploys` read);
  local equals origin.
- MSTR writes its own log and handoff, then tells Andrew **"ready to reboot"**. Andrew reboots.

**Phase E: after the reboot**
- 0.0.0_AB_MSTR re-seats each seat from its handoff.
- 1.0.0_SA_CTO re-arms `/self-drive` from its arming record (@`ce6aa15a17`; latest log `state: ARMED`).
- Resumes queued:
  - R4 (package re-mint, QA, enable);
  - the export K8 window (first real PDF);
  - K10 on rebuild 3;
  - round 9's remaining cells;
  - the S173 re-point after the POSN fill.
