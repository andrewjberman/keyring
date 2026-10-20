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

**FU-s-11** (RE-CUT 2026-10-20 ~18:35Z) -- Andrew-direct steer (CRO record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261020_1820Z_FIDUPL_REMOTE_AGENT_DRIVES_BOX_CHROME.md`), ruled by the CTO (`org/tier1_exec/1.0.0_SA_CTO/deliverables/`, message 8750): the BROWSER stays on the box (device trust is the box's address and fingerprint), the CONTROLLER is remote. No Claude account, no Claude Code login and no browser extension is needed on the box; the Claude-in-Chrome plan and its extension policy are WITHDRAWN. A dell1 agent will drive the box's headful Google Chrome by Playwright `connect_over_cdp` through an SSM port forward, the way the VNC screen is reached. Your part is the box side: a Chrome the agent can attach to. Track A (the scripted puller on `/opt/fidelity-uploader/profile`) is unchanged and runs FIRST.

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` section 7, your own VNC leg (`fidelity-vnc.service`, Xvnc `:1`, localhost 5901) and the feasibility record `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_feasibility.md` (Part 1 stands as a record; its plugin lines are superseded).

### WHAT TO DO

1. **Install now (a unit file only; do NOT start it).** On the box, a systemd unit `fidelity-agent-chrome.service`, NOT enabled at boot, that runs `/opt/google/chrome/chrome` headful on the display of the VNC screen (`DISPLAY=:1`, so a person can watch) with: `--remote-debugging-port=9222 --remote-debugging-address=127.0.0.1 --user-data-dir=/opt/fidelity-uploader/profile-agent --no-sandbox --no-first-run --no-default-browser-check`. The profile directory is the agent's OWN, never `/opt/fidelity-uploader/profile`. No extension policy, no credential, nothing printed. A ledger leg `agent-chrome-unit`. Record the unit text and the exact two commands Andrew or the agent would run (start the unit; the SSM port forward of 9222, like the VNC one) in `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_feasibility.md` under a new heading `CDP`.
2. **Start and check, ONLY after the issuer's message says START.** Start the unit, run the criterion below, and report. Stop the unit when the issuer says STOP. Never touch the puller's profile; never stop or start the instance.
3. **Sign-in record, ONLY after the issuer's message says GO** (a separate message; one Fidelity attempt at a time, and the scheduled puller's goes first). The drive itself is run by a dell1 agent, not by you; you only provide the Chrome and, after it, write `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_agent_signin_record.md` from the dell1 agent's run log the issuer gives you: lines `outcome=SIGNED_IN|REFUSED|ERROR`, `driver=cdp-remote`, `headful=true`, the step reached and the statuses of the password and code calls. Values never appear.

### ACCEPTANCE

<criterion id="FU11-AC1" cell_refs="FU-s-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu11c</invocation><expect>R1-FU11C-OK the box Chrome answers CDP on 127.0.0.1:9222 only</expect></criterion>
`FU11-AC1` -- after START: the agent Chrome answers CDP and is bound to 127.0.0.1 only (a CDP port on a public address would let anyone drive a signed-in browser).

<criterion id="FU11-AC2" cell_refs="FU-s-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu11s</invocation><expect>R1-FU11S-OK agent-driven headful sign-in recorded values-free</expect></criterion>
`FU11-AC2` -- after GO: the agent-driven sign-in record shows `outcome=SIGNED_IN`, the remote CDP driver and a headful browser. A second criterion, with its reason: it is the outcome Andrew asked for and the first cannot see it. A REFUSED outcome is Track B's measured result and ends the order; AC2 stays FAIL with the reason recorded, and the CTO rules.

<expected_criteria>FU11-AC1,FU11-AC2</expected_criteria>

Dry-run at the base (no unit, no record): `FU11-AC1` base: FAIL as expected; `FU11-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** A unit file on the box and, after START, a Chrome process; after GO, the box's Chrome takes one real sign-in driven from dell1. Ledger first, closed last. No alert, no new spend, no inbound port or security-group change (the CDP port is localhost-only, reached only by SSM forward). The box stays running.
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

**REPORT:** after step 1: the unit text, the two commands and the ledger id. After step 2: the check line verbatim. After step 3: the record's lines, the check lines verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; the dell1 agent reads nothing by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- one sign-in under Andrew's standing word that we are authorized users; the CDP port is localhost-only.
lane: the paths block.
</preflight>

Source: CTO ruling 8750 (Track B re-cut); Andrew-direct steer via CRO msg 8748/8749. Earlier rulings 8724 (separate agent profile, no standing extension policy) stand; the plugin parts are withdrawn.
