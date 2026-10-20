# TO NFRA_FIDUPL.TO-FU-s-11 -- the agent-driven headful Google Chrome fallback on the Fidelity box (Claude-in-Chrome)

<to_id>NFRA_FIDUPL.TO-FU-s-11</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-chrome-fallback</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-11` (`decompositions/NFRA_FIDUPL_DECOMP.md` section 10) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-10 (Google Chrome and Xvfb on the box)

---

## WORKER FACE

### THE CELL

**FU-s-11** -- Andrew's words (CRO record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261020_1630Z_FIDUPL_HEADFUL_CHROME_CLAUDE_PLUGIN.md`): the agent navigates the whole Fidelity sign-in itself, in a headful real Google Chrome, through the Claude-in-Chrome plugin, so that a repeatable agent-driven fallback exists. The CTO's ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_FIDUPL_HEADFUL_CHROME_20261020.md`, Track B) makes this your order: real Google Chrome with the plugin, on a display an agent can drive (VNC or Xvfb), on this box, with the SAME persistent profile directory the scheduled puller uses (`/opt/fidelity-uploader/profile`, see the worker reference section 7).

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` section 7 and your own ledger notes of FU-s-10; the login flow to navigate: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261020_NFRA_FIDUPL_LOGIN_FLOW_HAR5.md` (login, then the button "Text me the code", then the code from the Quo line, then Submit, then the home page).

### WHAT TO DO

**Part 1, feasibility, NOW (no sign-in).**
1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-chrome-fallback-<date> ...`), leg 1: feasibility.
2. Measure and record, values-free, in `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_feasibility.md` (create it) these four lines, each as `key=value` with a one-line reason: `plugin_installable=yes|no` (can the Claude-in-Chrome extension be installed into the Google Chrome on this box, and how), `claude_session_runs=yes|no` (can a Claude session be attached to that Chrome on this box, and with which credential or login it needs: say WHICH, never print one), `display=xvfb|vnc|none` (what the agent drives), `needs=<list>` (everything missing: packages, accounts, an Andrew act). Install what is installable with no new spend. Do NOT sign in to Fidelity in Part 1. Never read the Wealthscape secret. Do not stop or start the instance.
3. If the plugin cannot run on the box, say exactly why in the feasibility file; that is a complete and acceptable Part 1 (the CTO then rules the host). Report to the issuer and STOP.

**Part 2, the agent-driven sign-in, ONLY after the issuer's message says GO.** Only one Fidelity sign-in attempt may run at a time, and the scheduled puller's attempt goes first. When the message names GO: the agent session drives the headful Chrome from the login page through "Text me the code", reads the code from Quo (line `...3066`, the same reader as the puller, `quo_otp.py`), submits it, and stops at the home page. Never print the credential, the code, a cookie value, an account number or a G number. Record `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_agent_signin_record.md` with the lines `outcome=SIGNED_IN|REFUSED|ERROR`, `driver=claude-in-chrome`, `headful=true`, the step reached, and the response status of each of the password and code calls (statuses only). ONE attempt; no retry on a refusal.

### RULINGS (CTO msg 8724, 2026-10-20 ~16:52Z) -- they change Part 1 and Part 2

1. **A long-lived claude.ai login may live on the box.** Andrew's `/login` on the box and his extension sign-in over VNC are HIS acts, listed for him, and they block nothing: the scheduled puller's attempt goes first. **Part 1b, NOW:** install a VNC server on the box (dnf, no spend), bound to localhost only, reached only through an SSM port forward (the box has no inbound port); no password or token printed; record the install and the exact port-forward command Andrew would run, in the feasibility file under a new line `vnc=installed|failed` with its reason. A new ledger leg, `vnc-installed`.
2. **The agent's Chrome gets its OWN profile directory**, `/opt/fidelity-uploader/profile-agent`, not the puller's `/opt/fidelity-uploader/profile` (this supersedes "the SAME profile" above). The puller's Chrome will run with extensions disabled (the issuer cuts that one-flag change to `signin.py`), so a machine-wide plugin policy does not change its fingerprint. **Do NOT install any standing ExtensionInstallForcelist policy yet:** it waits for the issuer's message, which comes after that flag is delivered.
3. If Part 2 halts at the login page, as the vendor documents, **record that as Track B's measured result** (`outcome=REFUSED` with the step reached, in the sign-in record); that is a complete answer, not a failure of the order.

### ACCEPTANCE

<criterion id="FU11-AC1" cell_refs="FU-s-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu11f</invocation><expect>R1-FU11-OK feasibility record carries 4 facts</expect></criterion>
`FU11-AC1` -- Part 1: the feasibility record exists with its four facts.

<criterion id="FU11-AC2" cell_refs="FU-s-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu11s</invocation><expect>R1-FU11S-OK agent-driven headful sign-in recorded values-free</expect></criterion>
`FU11-AC2` -- Part 2 (after GO): the agent-driven sign-in record shows `outcome=SIGNED_IN`, the plugin as driver and a headful browser. A second criterion, with its reason: it is the outcome Andrew asked for and the first cannot see it.

<expected_criteria>FU11-AC1,FU11-AC2</expected_criteria>

Dry-run at the base (neither record exists): `FU11-AC1` base: FAIL as expected; `FU11-AC2` base: FAIL as expected. If the plugin cannot run on the box, AC2 stays FAIL with the reason in the feasibility file and the order is terminal-blocked for the CTO's ruling, not forced.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** Installs on the box and, in Part 2 only, one real sign-in. Ledger first, closed last. No alert, no new spend (a paid service, a residential proxy, a new instance is NOT yours: stop and tell the issuer). The box stays running.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1, section 10 addendum), cell `FU-s-11`.
<owned_cells>FU-s-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU11-AC1, FU11-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FU-s-11.chrome-fallback.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU11-AC1,FU11-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** after Part 1: the four facts and the ledger id. After Part 2: the record's lines, the check lines verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes unless Part 1 finds the plugin needs one, then it is a surprise row first.
comp-adversary: DECLARED-NOT-APPLICABLE -- one sign-in under Andrew's standing word that we are authorized users.
lane: the paths block.
</preflight>

Source: CTO ruling @c618ca8c8c (Track B); Andrew-direct via CRO msg 8711.
