# TO NFRA_FIDUPL.TO-FU-s-10 -- keep the Fidelity box's code equal to the repo (re-deliver the shipped files)

<to_id>NFRA_FIDUPL.TO-FU-s-10</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-box-delivery</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-10` (`decompositions/NFRA_FIDUPL_DECOMP.md` section 9) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-2 repair 2 (merged f5abe66e28)

---

## WORKER FACE

### THE CELL

**FU-s-10** -- Keep the box's code equal to the repo: re-deliver every shipped file of `infra/aws/ec2/canonical-fidelity/` (and `box/`) to `/opt/fidelity-uploader/` by SSM, md5-checked, the box left running. Contract row: C-TF. The same delivery you made in FU-s-7 leg 3 and FU-s-9 leg 5.

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` and your own earlier ledger notes (the bridge symlinks under `/opt/fidelity-uploader`, row NFRA_FIDUPL-D1-S4).

### WHAT TO DO

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-box-code-sync-<date> ...`, one leg: code equal to the repo).
2. The FU-s-2 login-trace repair 2 is merged on box/dell1 at f5abe66e28 (signin.py gained a values-free network, form-state, console and fingerprint trace; tests 67 passing). Take the repo files at THAT head or later. Re-deliver exactly these seven to `/opt/fidelity-uploader/`, keeping the same relative layout you used before: `quo_otp.py`, `signin.py`, `signin_recon.py`, `fetch.py`, `land.py`, `box/run.py`, `box/bootstrap.sh`. Do not touch `config.json`, `profile/`, `work/`, `venv/` or the bridge symlinks. Do NOT run `bootstrap.sh`; do not run any sign-in; do not stop or start the instance (it is running; if it is stopped, tell the issuer, do not start it).
3. Run the criterion below, record the line verbatim, close the ledger leg and the entry.

### REOPENED (issuer, 2026-10-20 ~15:00Z) -- second delivery

The first delivery (your commit 63f72e9788) is done and verified. FU-s-2 repairs 3 and 4 are now merged at 15b8f23cc0 (`signin.py`: visible-text error detection, fingerprint hygiene, a version-matched user agent; `signin_recon.py`: the measured legacy-JSP G-switch probe). The box differs from the repo for `signin.py` and `signin_recon.py` again. Do steps 1 to 3 again from the head 15b8f23cc0 or later (same seven files, same rules: no bootstrap, no sign-in, no start or stop), with a NEW ledger entry (slug `nfra-fidupl-box-code-sync-2-<date>`), and run `fu10m`. Report the head you delivered from.

### REOPENED AGAIN (issuer, 2026-10-20 ~15:35Z) -- third delivery

FU-s-2 repair 5 (the failed-request trace: header names, body key names, response text, third-party failures, cookie names) is merged at 7f2baa8f47. The box differs for `signin.py` again. Same seven files, same rules (no bootstrap, no sign-in, no start or stop), a NEW ledger entry (slug `nfra-fidupl-box-code-sync-3-<date>`), head 7f2baa8f47 or later, check `fu10m`. Report the head you delivered from. Please act on this one in the same turn you read it; the live trace follows at once.

### SCOPE WIDENED (issuer, 2026-10-20 ~15:35Z) -- every shipped file, not seven

Round 2 added modules on the box path (`gswitch.py`, `attribute.py`, `split.py`, `backfill.py`, `box/daily.py`; `adapters.py` follows) and changed `box/run.py`. The check `fu10m` now compares EVERY `*.py` directly under `infra/aws/ec2/canonical-fidelity/` and every `*.py` and `*.sh` under its `box/` (not tests) with the box, so the third delivery ships all of them: deliver the full current set from head c8aa40c577 or later, not only seven names; the expectation reads `all N shipped files` for the N the check finds (now 13).

### REOPENED (issuer, 2026-10-20 ~16:05Z) -- fifth delivery, the round-2 set is FROZEN at f3a4761ed5

FR-s-6 is merged: `adapters.py` is new and `box/run.py` changed (the daily attribute stage is wired). Deliver the full current set from head f3a4761ed5 or later (13 files now), a NEW ledger (slug `nfra-fidupl-box-code-sync-5-<date>`), check `fu10m`, same rules (no bootstrap, no sign-in, no start or stop). Thank you for the fourth delivery. Nothing else of round 2 is pending in the repo; if a file changes after this I will say so.

### SCOPE WIDENED AGAIN (issuer, 2026-10-20 ~16:35Z; CTO ruling 8704) -- the box needs Xvfb, then the sixth delivery

The sign-in now launches a HEADED Google Chrome under a virtual display. Before (or with) the sixth delivery, install the package on the box: `sudo dnf install -y xorg-x11-server-Xvfb` through an SSM RunShellScript, idempotent, no reboot, the box left running (your ledger leg `xvfb-installed`, one more leg beside the code leg). The delivery head will be named by a message once the sign-in repair (REPAIR 7) merges; deliver all shipped files from that head. Criterion FU10-AC2 is checked after both. **CTO ruling @c618ca8c8c (Andrew-direct): the browser is real Google Chrome, not Chromium.** So the install leg is TWO packages: `xorg-x11-server-Xvfb` and Google Chrome stable (the RPM from `https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm` by `sudo dnf install -y <that url>`; Playwright cannot install the `chrome` channel on this OS, so use the RPM). The `fu10x` check now launches `channel='chrome'` headful under Xvfb. No bootstrap run, no sign-in, no start or stop.

### REOPENED (issuer, 2026-10-20 ~18:35Z) -- eighth delivery, signin.py changed at 5cb31dfa650

FU-s-2 REPAIR 10 is merged (the display is started before the Playwright driver). Deliver the shipped set from head 5cb31dfa650 or later (only `signin.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-8-<date>`), check `fu10m`, same rules: a file copy only, no browser, no bootstrap, no sign-in, nothing under either profile directory. The checker was renamed (commit 43ab0c6541): the invocations in this order now name `fidupl_round_checks.py`. Re-run `fu10x` as well (a browser launch under Xvfb on a scratch profile, as the check does) since it is the order's AC2. Tell the issuer in one line; the issuer then runs a launch-only probe.

### REOPENED (issuer, 2026-10-20 ~19:15Z) -- ninth delivery, signin.py changed at 132dc9c3061

FU-s-2 REPAIR 11 is merged (polling survives a navigation race; a failed step records a redacted message). Deliver the shipped set from head 132dc9c3061 or later (only `signin.py` differs from your eighth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-9-<date>`), check `fu10m` (and `fu10x`), same rules: a file copy only, no browser run beyond the check's scratch launch, no bootstrap, no sign-in, nothing under either profile directory. Tell the issuer in one line.

### REOPENED (issuer, 2026-10-20 ~21:20Z) -- tenth delivery, URGENT: signin.py changed at d8e08fbb331

FU-s-2 REPAIR 12 is merged (authorize accepts any 2xx; logout on close). Deliver the shipped set from head d8e08fbb331 or later (only `signin.py` differs from your ninth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-10-<date>`), check `fu10m`, same rules: a file copy only, nothing under either profile directory, no sign-in, no browser. The live attempt window is 21:35Z to 21:55Z: tell the issuer in one line the moment `fu10m` reads OK (fu10x need not be re-run for a signin.py-only change).

### ACCEPTANCE

<criterion id="FU10-AC1" cell_refs="FU-s-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu10m</invocation><expect>R1-FU10M-OK all \d+ shipped files match the repo on the box</expect></criterion>
`FU10-AC1` -- the seven shipped files on the box match the repo by md5.

<criterion id="FU10-AC2" cell_refs="FU-s-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu10x</invocation><expect>R1-FU10X-OK Xvfb present and a headed Google Chrome launches under it</expect></criterion>
`FU10-AC2` -- a second criterion, with its reason: the code md5s cannot see that the box can run a headed browser, which is the whole point of the sixth delivery.

<expected_criteria>FU10-AC1,FU10-AC2</expected_criteria>

Dry-run at the base (the box holds the pre-REPAIR-2 signin.py): `FU10-AC1` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** An SSM delivery to the box. Ledger first, closed last. Never read the Wealthscape secret; no sign-in; no alert.
- **Refusal clause.** A premise that fails (an md5 that will not match, the box stopped) is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1, section 9 addendum), cell `FU-s-10`.
<owned_cells>FU-s-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU10-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FU-s-10.box-code-sync.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU10-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the head you delivered from, the seven md5 lines, the check line verbatim, the ledger id, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a file delivery of already-merged code; no new surface.
lane: the paths block.
</preflight>

Source: FU-x-1 attempt 2 (worker row W1-S11), FU-s-2 repair 2 merged f5abe66e28.
