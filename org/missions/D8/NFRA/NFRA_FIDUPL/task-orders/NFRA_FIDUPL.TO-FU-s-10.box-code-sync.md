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

### REOPENED (issuer, 2026-10-20 ~22:40Z) -- eleventh delivery: box/agent_fill.py changed at c824968be16

FU-s-12 REPAIR 1 is merged (the helper failure line carries a redacted detail and trace). Deliver the shipped set from head c824968be16 or later (only `box/agent_fill.py` differs from your tenth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-11-<date>`), check `fu10m`, same rules: a file copy only, nothing under either profile directory, no sign-in, no browser. Tell the issuer in one line the moment `fu10m` reads OK (fu10x need not be re-run). The Track B re-run waits on it.

### REOPENED (issuer, 2026-10-20 ~23:25Z) -- twelfth delivery: signin.py changed at d8a0d567a79 (REPAIR 13)

FU-s-2 REPAIR 13 is merged (real key presses, a pointer path, the `_abck` verdict read before the password POST). Deliver the shipped set from head d8a0d567a79 or later (only `signin.py` differs from your eleventh delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-12-<date>`), check `fu10m`, same rules: a file copy only, no browser run, no sign-in, nothing under either profile directory, and leave `fidelity-agent-chrome.service` running. Tell the issuer in one line the moment `fu10m` reads OK; the live run waits on it.

### REOPENED (issuer, 2026-10-20 ~23:46Z) -- thirteenth delivery, URGENT: signin.py changed at 567486eb857 (REPAIR 14)

FU-s-2 REPAIR 14 is merged (authorize accepts the signed-in home page; select_factor waits for the verify page). Deliver the shipped set from head 567486eb857 or later (only `signin.py` differs from your twelfth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-13-<date>`), check `fu10m`, same rules: file copy only, no browser, no sign-in, nothing under either profile directory, leave `fidelity-agent-chrome.service` as it is. Tell the issuer in one line the moment `fu10m` reads OK: the Track A run waits on it.

### REOPENED (issuer, 2026-10-21 ~00:15Z) -- fourteenth delivery, URGENT: signin.py changed at 34ebdc69d5d (REPAIR 15)

FU-s-2 REPAIR 15 is merged (the Playwright launch no longer forges a user agent or an init script). Deliver the shipped set from head 34ebdc69d5d or later (only `signin.py` differs from your thirteenth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-14-<date>`), check `fu10m`, same rules: file copy only, no browser, no sign-in, nothing under either profile directory, leave `fidelity-agent-chrome.service` as it is. Tell the issuer in one line the moment `fu10m` reads OK: the Track A run waits on it.

### REOPENED (issuer, 2026-10-21 ~00:43Z) -- fifteenth delivery, URGENT: signin.py changed at 47219723923 (REPAIR 16)

FU-s-2 REPAIR 16 is merged (the authorize wait keeps polling after a non-2xx answer). Fidelity signed the puller in at 00:32Z and our wait said refused; this delivery lets the next run land a day. Deliver the shipped set from head 47219723923 or later (only `signin.py` differs from your fourteenth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-15-<date>`), check `fu10m`, same rules: file copy only, no browser, no sign-in, nothing under either profile directory, leave `fidelity-agent-chrome.service` as it is. Tell the issuer in one line the moment `fu10m` reads OK.

### REOPENED (issuer, 2026-10-21 ~01:20Z) -- sixteenth delivery, URGENT: land.py and split.py changed at 9256d6aa99a

FU-s-4 REPAIR 1 (the lander reads each file's own date column and the run record gains an outcome) and FR-s-2 REPAIR 3 (split.py passes the file name) are merged; the whole module suite reads 164 passed. Deliver the shipped set from head 9256d6aa99a or later (`land.py` and `split.py` differ from your fifteenth delivery), a NEW ledger (slug `nfra-fidupl-box-code-sync-16-<date>`), check `fu10m`, same rules: file copy only, no browser, no sign-in, nothing under either profile directory, leave `fidelity-agent-chrome.service` as it is. Tell the issuer in one line the moment `fu10m` reads OK: the re-land of the three held files waits on it.

### REOPENED (issuer, 2026-10-21 ~02:45Z) -- seventeenth delivery, the round-3 code: head 39524cb59c0

Merged since your sixteenth delivery: FT-s-1 (`switcher_list.py`, `perg_seed.py`), FT-s-2 (`box/daily.py`, `box/run.py`), FT-s-3 (`signin_recover.py`), FT-s-4 (`backfill_run.py`), FT-s-7 (`backfill_adapter.py`, `backfill_main.py`, a REPAIR 2 is still in build and ships later), FU-s-2 REPAIR 17 (`signin.py`); `land.py` and `split.py` are already on the box. Deliver the shipped set from head 39524cb59c0 or later. Several files are NEW at the code root `/opt/fidelity-uploader/` next to `land.py` (`switcher_list.py`, `perg_seed.py`, `signin_recover.py`, `backfill_run.py`, `backfill_adapter.py`, `backfill_main.py`), so keep the same relative layout you used before. Use a NEW ledger (slug `nfra-fidupl-box-code-sync-17-<date>`). The `fu10m` check compares every `.py` file at the code root plus `box/`, so it reads the enlarged set by itself. Same rules: file copy only, no browser, no sign-in, nothing under either profile directory, leave `fidelity-agent-chrome.service` as it is, and do not touch `/opt/fidelity-uploader/work`. One line to the issuer when done.

### REOPENED (issuer, 2026-10-21 ~03:00Z) -- eighteenth delivery: split.py (null account column) and the backfill seam fix, head f75a19d0646

Merged since your seventeenth delivery: FR-s-2 REPAIR 4 (`split.py`: prices and security are not split) and FT-s-7 REPAIR 2 (`backfill_adapter.py`, `backfill_main.py`, `backfill_run.py`). Deliver the shipped set from head f75a19d0646 or later, a NEW ledger (slug `nfra-fidupl-box-code-sync-18-<date>`), check `fu10m`. Same rules: file copy only, no browser, no sign-in, nothing under either profile directory or `/opt/fidelity-uploader/work`, the agent Chrome unit and `config.json` as they are. One line to the issuer when done: the daily-mode proof run (TO-FT-s-8 step 2) waits on it.

### REOPENED (issuer, 2026-10-21 ~03:10Z) -- nineteenth delivery: box/run.py accepts the null account column, head 8a6b473b366

Your row D1-S10 was right and is fixed (FT-s-2 REPAIR 1: `box/run.py` `_check_account_columns` accepts null for prices.txt and security.txt only; module suite 208 passed; I also ran `check_pointers` locally on a config of the measured daily shape: it passes, and a null for position is still refused). Deliver the shipped set from head 8a6b473b366 or later (only `box/run.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-19-<date>`), `fu10m`. Same rules as before: file copy only, nothing else touched. One line to the issuer; the new GO for TO-FT-s-8 step 2 follows from me.

### REOPENED (issuer, 2026-10-21 ~03:05Z) -- twentieth delivery: box/daily.py prints the AdapterShapeError message, head a721306c27f

Your row D1-S11 is acted on (FT-s-2 REPAIR 2: `box/daily.py` prints `ERROR: attribute shape: <message>` and records `attribute_error` for `AdapterShapeError` only, every other exception stays class-only; module suite 209 passed). Deliver the shipped set from head a721306c27f or later (only `box/daily.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-20-<date>`), `fu10m`. Same rules: file copy only, nothing else touched. One line to the issuer; the new GO for TO-FT-s-8 step 2 follows from me.

### REOPENED (issuer, 2026-10-21 ~03:50Z) -- twenty-first delivery: adapters.py (the lister finds the live page-2 form) and box/daily.py, head 42e7faa2120

Your row D1-S12 is acted on (FR-s-6 REPAIR 1 and 2: the account lister tries a table of eleven paging forms, keeps the first that adds distinct rows, stops at once on a 401 or 403; `box/daily.py` prints `OK: accountList paging form=<index>`; module suite 212 passed). Deliver the shipped set from head 42e7faa2120 or later (`adapters.py` and `box/daily.py` differ), a NEW ledger (slug `nfra-fidupl-box-code-sync-21-<date>`), `fu10m`. Same rules: file copy only, nothing else touched. One line to the issuer; the new GO for TO-FT-s-8 step 2 follows from me.

### REOPENED (issuer, 2026-10-21 ~03:55Z) -- twenty-second delivery: the NEW file box/paging_probe.py, head 5c1f823d269

Your row D1-S13 is acted on: no candidate paging form worked, so a read-only probe measures the live form (TO-FT-s-9, merged; module suite 215 passed). Deliver the shipped set from head 5c1f823d269 or later: `box/paging_probe.py` is a NEW file (the box set grows to 22), a NEW ledger (slug `nfra-fidupl-box-code-sync-22-<date>`), `fu10m` (expect all 22 match). Same rules: file copy only, nothing else touched. One line to the issuer. Then the run (one sign-in, NOT before 04:30Z): `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/box/paging_probe.py /opt/fidelity-uploader/config.json` on my GO message, stdout verbatim (counts only).

### REOPENED (issuer, 2026-10-21 ~04:50Z) -- twenty-third delivery: box/paging_probe.py v2 (the per-G book size sweep), head 217476105df

The CTO ruled (msg 8986) that the per-G sweep is the source and that book sizes come first. Probe v2 is merged (TO-FT-s-9 REPAIR 1; module suite 217 passed). Deliver the shipped set from head 217476105df or later (only `box/paging_probe.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-23-<date>`), `fu10m` (22 files). Same rules: file copy only, nothing else touched. One line to the issuer; the GO for the run (TO-FT-s-8 step 2P, second run) is already in the order text.

### REOPENED (issuer, 2026-10-21 ~05:15Z) -- twenty-fourth delivery: the NEW file box/g_export_probe.py and box/paging_probe.py v3, head a773bcaa09f

Both probes are merged (TO-FT-s-10 incl. REPAIR 1: the G-scoped export probe; TO-FT-s-9 REPAIR 2: probe v3; module suite 225 passed). Deliver the shipped set from head a773bcaa09f or later: `box/g_export_probe.py` is a NEW file (the box set grows to 23) and `box/paging_probe.py` differs; a NEW ledger (slug `nfra-fidupl-box-code-sync-24-<date>`); `fu10m` (expect all 23 match). Same rules: file copy only, nothing else touched. One line to the issuer.

### REOPENED (issuer, 2026-10-21 ~05:40Z) -- twenty-fifth delivery: box/g_export_probe.py with the day argument, head 0a429399ac8

The first live run of the G-export probe used day 2026-10-21 (no export exists yet), so it said nothing about the G number. REPAIR 2 of TO-FT-s-10 adds an optional day argument (module suite 226 passed). Deliver the shipped set from head 0a429399ac8 or later (only `box/g_export_probe.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-25-<date>`), `fu10m` (23 files). Same rules: file copy only, nothing else touched. One line to the issuer.

### REOPENED (issuer, 2026-10-21 ~06:22Z) -- twenty-sixth delivery: backfill_main.py with the DAY lines and the long request timeout, head eaa67a5fb09

Your row D1-S14 is acted on (TO-FT-s-7 REPAIR 3: a 120 s request timeout, one `DAY <date> result=...` line per trading day, a `days` list in the record, a timeout as a named stop with its date; module suite 229 passed). Deliver the shipped set from head eaa67a5fb09 or later (only `backfill_main.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-26-<date>`), `fu10m` (23 files). Same rules: file copy only, nothing else touched. One line to the issuer.

### REOPENED (issuer, 2026-10-21 ~07:20Z) -- twenty-seventh delivery: backfill_main.py with flushed output, a wall budget and REQ lines, head 170a9c69ce8

Your row D1-S15 is acted on (TO-FT-s-7 REPAIR 4: every line flushed, `--max-seconds` wall budget with a SIGALRM safety net, REQ/SIGNIN/CLOSE lines; module suite 232 passed). Deliver the shipped set from head 170a9c69ce8 or later (only `backfill_main.py` differs), a NEW ledger (slug `nfra-fidupl-box-code-sync-27-<date>`), `fu10m` (23 files). Same rules: file copy only, nothing else touched. One line to the issuer.

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
