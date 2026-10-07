# TO NFRA_CTLPLN.TO-CT-b-2 -- round 2 CT-b-2: the RDP lock read -- each box's Remote Desktop rules scoped to the tailnet, and the Dells reachable over it

<to_id>NFRA_CTLPLN.TO-CT-b-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~2</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-b-2` (`decompositions/NFRA_CTLPLN_DECOMP.round2.md`) | **outcome_ref:** FWD-14 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-b-2`, FWD-14 (C-RDP): Remote Desktop (port 3389) is reachable over the tailnet on every box and nowhere else -- the Windows firewall scopes
3389 to the tailnet range `100.64.0.0/10` (shown by Windows as `100.64.0.0/255.192.0.0`). You build two read-only checks and run them on
THIS box (the laptop). The same script is run later on each Dell by its seat or by Andrew; it changes nothing anywhere.

**Measured (laptop, 2026-10-07 ~01:0xZ):** the three enabled Remote Desktop inbound rules -- `Remote Desktop - User Mode (TCP-In)`,
`Remote Desktop - User Mode (UDP-In)`, `Remote Desktop - Shadow (TCP-In)` -- are on profile Any with remote address `100.64.0.0/255.192.0.0`.
Tailnet addresses: dell1 100.79.95.44, dell2 100.104.84.87 (also in `org/devices/DEVICES.json`, fields `tailnet_name`, `tailnet_address`).
This shell is NOT elevated; reading firewall rules does not need elevation.

**Build:**
1. `org/devices/rdp_lock_check.ps1` (Windows PowerShell 5.1, read-only): reads every ENABLED inbound firewall rule whose local port includes
   3389 or whose display group is "Remote Desktop", prints one line per rule (name, protocol, profile, remote addresses), and a rule is
   LOCKED when its remote address set is exactly the tailnet range (accept `100.64.0.0/10` and `100.64.0.0/255.192.0.0`). LAST line exactly:
   `RDP-LOCK box=<the box's AGENTBUS_DEVICE setting, else the computer name> rules=<n> locked=<k> all_locked=<True|False>`. A box with no
   such rule prints `rules=0 ... all_locked=False`. It never changes a rule.
2. `org/devices/rdp_reach_check.py`: reads `org/devices/DEVICES.json` and, for every box other than this one that has a `tailnet_address`,
   opens a TCP connection to `<address>:3389` with a 5 s timeout; prints one line per box (open / refused / timeout) and as the LAST line
   `RDP-REACH <box>=<open|closed> ...` in register order, followed by `checked=<n>`. Read-only.

### ACCEPTANCE

<criterion id="CT2b2-AC1" cell_refs="CT-b-2"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File org/devices/rdp_lock_check.ps1</invocation><expect>all_locked=True</expect></criterion>
`CT2b2-AC1` -- on the laptop, every enabled Remote Desktop rule is scoped to the tailnet.

<criterion id="CT2b2-AC2" cell_refs="CT-b-2"><invocation>python org/devices/rdp_reach_check.py</invocation><expect>dell1=open dell2=open</expect></criterion>
`CT2b2-AC2` -- from the laptop over the tailnet, both Dells answer on 3389.

<expected_criteria>CT2b2-AC1,CT2b2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read only:** never change a firewall rule, a Remote Desktop setting or a tailnet setting on any box.
- **Refusal clause.** If a criterion cannot be met as written (a Dell's 3389 does not answer), stop, write the measured result in your report
  and a surprise row (id `NFRA_CTLPLN-W2-S<k>`), and do not weaken the check.

<paths>
org/devices/rdp_lock_check.ps1
org/devices/rdp_reach_check.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round2.md</decomp_doc> (round 2), cell `CT-b-2`.
<owned_cells>CT-b-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT2b2-AC1, CT2b2-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~2/NFRA_CTLPLN.TO-CT-b-2.rdp-lock-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT2b2-AC1,CT2b2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both check outputs in full, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no cloud call.
comp-adversary: RUN -- read only (no rule changed); the negative arm of S14 (a non-tailnet connection refused) is a later act from outside the tailnet, not provable from this box; BLIND: the Dells' own rules until each Dell runs the script.
lane: the <paths> block IS the grant (worker RULING 1); org/devices/** is lane NFRA_CTLPLN_FAST_C.
</preflight>

Source: PRD v0.6 C-RDP, FWD-14, S14; CTO msg 105915 (add a read of each Dell's RDP rules); decomposition round 2.
