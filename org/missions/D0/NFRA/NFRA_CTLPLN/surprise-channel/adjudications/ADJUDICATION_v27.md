# NFRA_CTLPLN: CVO L8 at the round-22 close (2026-10-15)

<sweep_watermark>2026-10-15T20:55Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109512 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND22.md` @51ed0a460a).
No judgment criterion this round.

**Result:**
- **FWD-3 REALIZED and FWD-24 REALIZED** on this seat's own reads (C-S74). The tally becomes 5 REALIZED, 19 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED.
- 13 round-22 rows are dismissed (C-S75), and W121-S3/S4 GRADUATE to REMEDIATION_v12 (C-S76).
- Three remediation rows close in place on verified done-whens: D1-S8 (REMEDIATED, DISARMED), W61-S1 (REMEDIATED, DISARMED) and W84-S1 (REMEDIATED) (C-S77).
- Of the issuer's other proposed closures, W111-S1, S9105, S9101 and W79-S2 stay OPEN, each with the read that closes it.

All 9 criteria of CT-al-1, CT-al-3 and CT-al-4 were re-run here and pass, including the state-aware journey tests after the release and `test_round21_fwd5_positive_read.py`
(other_changed=0). `round-close-check --round 22` reads MAY-CLOSE.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S74",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T21:08Z",
  "one_line": "FWD-3 REALIZED: all 12 directed box pairs carry at least one message the managers carried (sent.bus_message_id present) and the addressed seat acknowledged (ack.by == to_serial), under the CTO's corrected reading (round-21 ADDENDUM 1, @d9c20f887e). FWD-24 REALIZED: both leads answered OWED for the same operation from its class, and the research seat's tool tells whether an ask was owed for an order.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "FWD-3 (PRD :48-55) as written. FWD-24 (PRD :273-281): the same operation put to two leads on two boxes, both give the same answer; a lead can tell from the class, and the research seat can tell whether an ask was owed.",
  "world_is": "FWD-3: this seat's read of org/devices/crossbox/XB-*.json counts 12 of 12 pairs with a qualifying file. laptop->dell1's newest file is 7bc4 (sent 20:42Z, not yet acked), so the newest-per-pair count is 11. The pair's latest qualifying file is 3a78 (acked by its named seat). The ADDENDUM withdraws v0.31's manager-ack bullet and the round-21 ruling 2, so the round-20/21 counter-instances (CTO and CloudOps lanes acking) are the named seats reading, as the ACCEPT means. FWD-24: laptop CTO OWED (msg 109405); site Z CTO OWED (XB_e670_FWD24_RESEARCH_OWED_ANSWER_SITEZ_20261015.md on origin/box/sitez, read here: 'research-owed.py --stakes S3 ... verdict=OWED rule=stakes class S3 is S3 or above'). Run here: research-owed.py --selftest 16/16, and --order on TO-CT-ak-3 prints 'verdict=OWED rule=task order classed WORLD'.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/devices/crossbox/XB-*.json read 2026-10-15 ~21:0xZ: pairs with a carried, named-seat-acked file 12/12; newest-per-pair 11/12",
    "org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round21.md ADDENDUM 1 @d9c20f887e (lines 77-89)",
    "MSYS_NO_PATHCONV=1 git show origin/box/sitez:org/tier1_exec/1.0.0_SA_CTO/deliverables/XB_e670_FWD24_RESEARCH_OWED_ANSWER_SITEZ_20261015.md",
    "python .tools/research-owed.py --selftest -> 16/16; --order .../NFRA_CTLPLN.TO-CT-ak-3...md -> verdict=OWED"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S75",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T21:08Z",
  "one_line": "Round 22 rows dismissed with reason: W119-S1, S9133 (worker ~120's rows moot after the CTO's withdrawal), W121-S1, S2, S5, S6, W122-S1..S5.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["NFRA_CTLPLN-W119-S1", "NFRA_CTLPLN-S9133", "NFRA_CTLPLN-W121-S1", "NFRA_CTLPLN-W121-S2", "NFRA_CTLPLN-W121-S5", "NFRA_CTLPLN-W121-S6", "NFRA_CTLPLN-W122-S1", "NFRA_CTLPLN-W122-S2", "NFRA_CTLPLN-W122-S3", "NFRA_CTLPLN-W122-S4", "NFRA_CTLPLN-W122-S5"],
  "spec_asserts": "Each order's text as written, with the issuer's rulings in packet section 5.",
  "world_is": "W119-S1 is noted for this seat: the check tool records check 8 as FAILED, not awaiting, when the signature file is absent; the test maps it. The FWD-17 read-back must not quote that state as a failed check. W122-S4/S5 are cured by the state-aware tests (both reproduce here after the release). W121-S5 is cured: a rebuild without portal/ dropped portal edges, and the round's final map was rebuilt from a full tree. The rest are build notes.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/tests/test_round22_journey_record.py --fetch/--check/--tag/--release/--pack/--taildrop -> ok=True each (2026-10-15 ~21:0xZ)",
    "python .tools/tests/test_round22_hygiene.py --map-age/--sparse -> ok=True each",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND22.md @51ed0a460a section 5"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled in the round, cured, or build notes."
 },
 {
  "id": "NFRA_CTLPLN-C-S76",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T21:08Z",
  "one_line": "W121-S3 (the same corpus builds 2692, 2703 or 3491 danger edges by tree) and W121-S4 (the build guard does not check portal/) GRADUATE to REMEDIATION_v12, owner 1.0.0_SA_CTO.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["NFRA_CTLPLN-W121-S3", "NFRA_CTLPLN-W121-S4"],
  "spec_asserts": "A row graduates when its mechanism is attributed and its remedy holder named.",
  "world_is": "Both rows bear on whether the self-refreshing danger map is the same map from every tree. W117-S2 and W117-S3 (REMEDIATION_v11) carry the sparse and scheduling halves.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows W121-S3, W121-S4",
    "remediations/REMEDIATION_v12.md"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_CTLPLN-C-S77",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T21:08Z",
  "one_line": "On the issuer's proposed dispositions of its 15 owned rows: D1-S8, W61-S1 and W84-S1 are closed in place on verified done-whens; W111-S1, S9105, S9101 and W79-S2 stay OPEN, because the measured world does not meet their own done-whens; the carried rows are as the issuer states.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Each row's own done-when in REMEDIATION_v1, v2, v6 and v9.",
  "world_is": "D1-S8 (v2): its planted case is exactly round 21's real deploy (a pinned file already on CLOUD at 17:53Z, in no box diff, S3 stale), deployed by the next push with bytes equal to the pin (C-S67). W61-S1 (v2): read live on the laptop. The rule 'OpenSSH Server (Tailscale only)' is enabled with remote 100.64.0.0/255.192.0.0, the open 'OpenSSH SSH Server (sshd)' rule is disabled, sshd_config reads 'PasswordAuthentication no', and ssh-tailnet-verify --box laptop reads methods publickey,keyboard-interactive with password_arm=KBDINT-NO-PROMPT (the state round 19 counted as password-refused). W84-S1 (v6): spawn-agent.ps1:108 reads [A-Za-z0-9_]+ in the third segment; it admits 0.9.0_WK_NFRA_CTLPLN~78 and refuses three malformed serials, run here. Staying OPEN: W111-S1's done-when (downloads --device laptop counts the two real 20261008 records) is not met, because the packet says older records still read unattributed. S9105's done-when (the three org/devices edits on the trunk under a worker author) is not shown; 'the slot no longer exists' does not show where the edits went. S9101 closes on a read of AMENDMENT 9's step-4 text naming five roots and seeking-alpha, not shown here. W79-S2's done-when is 50/50 on two boxes whose origin refs differ, while the read is 64/65 on one box.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Get-NetFirewallRule *OpenSSH* with Get-NetFirewallAddressFilter; C:\\ProgramData\\ssh\\sshd_config; Get-Service sshd -> Running (2026-10-15 ~21:0xZ)",
    "python .tools/ssh-tailnet-verify.py --box laptop --user cvo-probe-nonexistent -> key=DENIED password_arm=KBDINT-NO-PROMPT methods=publickey,keyboard-interactive",
    ".tools/spawn-agent.ps1:108 and a PowerShell -match test of five serials",
    "adjudication row NFRA_CTLPLN-C-S67 (the D1-S8 case)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Clocks advanced in place for the three verified rows; the four others name their closing read."
 }
]
```

-- 3.0.0_SA_CVO~L
