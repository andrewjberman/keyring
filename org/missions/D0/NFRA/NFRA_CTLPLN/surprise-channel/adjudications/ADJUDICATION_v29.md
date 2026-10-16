# NFRA_CTLPLN: CVO L8/L9 at the round-24 and round-25 closes -- FWD-15, FWD-16, FWD-17 graded (2026-10-16)

<sweep_watermark>2026-10-16T04:20Z</sweep_watermark>

L8/L9 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109592 (packets `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND24.md`
@52567a1a41 and `L8_PACKET_ROUND25.md` @a14976a438; analyses `ledger/ROUND_ANALYSIS.round24.md`, `round25.md`). Round 24 owes
no judgment criterion; round 25 owes the L9 grade of FWD-15, FWD-16 and FWD-17 (round-25 analysis section 3, item 1).

**Result:**
- **FWD-16 REALIZED** (C-S82) and **FWD-17 REALIZED** (C-S83).
- **FWD-15 stays ADVANCED, one act short** (C-S81): the tabulate journey reached dell1 checked, offline and with dell1's own
  hashed receipts, but no dell1 lane's work ran on it. The missing act is one cell (below), and it must run BEFORE the dell1
  scratch delete put to Andrew in round-25 ruling 1, or the install has to be repeated.
- Tally: 7 REALIZED (1, 3, 5, 16, 17, 24, 28), 17 ADVANCED, 0 GATED, 1 PARKED (9), 3 MOVED (13, 20, 26); denominator 28 (C-S85).
- 2 round rows dismissed (C-S84): W126-S1 and W128-S1.

All 7 criteria of the three orders were re-run here in the main tree and pass: `PIP-LOG arms=7/7 ok=True`;
`INTAKE-RECEIVE-TEST cases=34/34 ok=True`; `JOURNEY-FETCH ... ok=True`; `JOURNEY-CHECK checks_run=7 failed=0 check8=SIGNED
released=True ok=True`; `JOURNEY-RELEASE released=1 ... ok=True`; `JOURNEY-PACK files=4 manifest_ok=True ... ok=True`;
`JOURNEY-TAILDROP files_sent=4 failed=0 target=dell1 ok=True`. `round-close-check --deep` reads MAY-CLOSE for round 24 and
round 25 (judgment 2, graded 2, ungraded 0, self-graded 0).

**The one cell FWD-15 needs (for the round-26 issuance):** a dell1 lane (`1.0.0_SA_CTO~DELL1` or the lane it names) runs the
round-25 read-out's work on dell1 itself, importing tabulate from `C:\dev\_intake_tabulate_20261016\SCRATCH_TARGET` only
(`PYTHONPATH` set to it, `python -I`-style isolation otherwise), renders the one read-only table, and commits the output and
the `tabulate.__file__` it imported from on `box/dell1`. Pass: the table prints, and `__file__` is under `SCRATCH_TARGET`.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S81",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:20Z",
  "one_line": "FWD-15 graded ADVANCED, not REALIZED: tabulate 0.9.0 went laptop -> check -> Taildrop -> dell1 install from the file alone, with dell1's own receipts and pip logs whose hashes this seat re-read, but no dell1 lane's work ran on it. The round-23 duckdb journey ran a lane but had no dell1 receipt or pip log; the DONE WHEN names ONE package taken the whole way, so the two journeys do not add up.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-15 DONE WHEN: one real package taken the whole way for one Dell lane, and the lane's work then runs. ACCEPT: the Dell installs it from that file alone, the lane's work runs, and the Dell asks no outside site.",
  "world_is": "Met on tabulate: origin/box/dell1 c25860a18b holds receipts/...install.dell1.json (received_sha256 024ca478df22e934...1948f, equal to the laptop's held_sha256 in the check record) and both pip logs; this seat hashed the committed logs: install 676 bytes cd6e3557...6cb9, prove 697 bytes 49006dd4...32cd, each equal to its receipt. The install command is pip install --no-index --no-deps --target SCRATCH_TARGET <the delivered wheel>, rc 0, env pins PIP_NO_INDEX=1 PIP_CONFIG_FILE=nul, no index line in pip's output (the log is the command, environment and pip's output, not a network trace; this seat accepts it at that grain). prove: imported=1. Not met: the request names a laptop lane's need (2.0.0_SA_COO~C's read-out table) and the round-25 analysis states the stand-in lane's table was never rendered; nothing on dell1 ran work with the installed package beyond prove's import.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show c25860a18b:org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_CTLPLN_TABULATE_INTAKE_DELL1_RECEIPTS_20261016/ (11 files; both pip logs re-hashed 2026-10-16T04:1xZ)",
    "python org/devices/intake/intake_request.py show --id REQ-20261016T025712Z-tabulate (needed by: 2.0.0_SA_COO~C, laptop lane)",
    "ledger/ROUND_ANALYSIS.round25.md section 1, 'The stand-in lane's table was never rendered'",
    "adjudications/ADJUDICATION_v28.md C-S80 (the round-23 FWD-15 open items)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard; the missing act is named in this record's header for the round-26 issuance."
 },
 {
  "id": "NFRA_CTLPLN-C-S82",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:20Z",
  "one_line": "FWD-16 graded REALIZED: one request filed for a package requirements.txt lacks (tabulate 0.9.0), one approval and one refusal (polars 1.12.0), both read back by this seat, which took part in neither; who, when, why and on what evidence all print.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-16 DONE WHEN: one request made, one approved and one refused, and both decisions read back by someone who was not part of them. ACCEPT adds: two people on two boxes get the same answer without asking anyone; the request says what, which version, what needs it and why nothing approved will do; a refusal reads as clearly as an approval.",
  "world_is": "intake_request.py status --name tabulate --version 0.9.0 -> APPROVED by=1.0.0_SA_CTO at=2026-10-16T02:59:56Z with its reason; status --name polars --version 1.12.0 -> REFUSED by=1.0.0_SA_CTO at=2026-10-15T16:33:46Z reason='no named lane or job...'. show --id REQ-20261016T025712Z-tabulate prints what, exact version, needed by, why nothing approved will do, requested by/at, who decided, when, why and an evidence path with its SHA-256. The round-23 premise flaw (duckdb already approved) is cured: tabulate was absent. Two boxes: the request files and intake_request.py are byte-identical blobs on this box's HEAD and on dell1's c25860a18b (tabulate 3e94272b3a, polars 0e8381ad89, tool 6879985ca1), so the verb reads the same answer there; this seat did not run it on dell1.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python org/devices/intake/intake_request.py status (tabulate, polars) and show --id REQ-20261016T025712Z-tabulate, 2026-10-16T04:1xZ",
    "git rev-parse HEAD:<path> vs c25860a18b:<path> for both request files and intake_request.py"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S83",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:20Z",
  "one_line": "FWD-17 graded REALIZED: the CTO read Andrew the tabulate check record, including the three things checks 1 to 7 cannot rule out (a taken-over maker account, whether the antivirus inspected the file, a file already bad in February), and he approved it verbatim.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-17 DONE WHEN: one delivered package's record read aloud to Andrew, including what was not checked. ACCEPT: the taken-over-maker answer is the true one even when it is no; nothing is called clean beyond what was looked at.",
  "world_is": "The package was delivered (C-S81). Addendum @ba2e7f6545 to ANDREW_DIRECT_20261016_034xZ_ALL_19_CALLS_RECS_APPROVED_C02C_POSTPONED.md records the read and his words, 'thats good, i approve of this'. The record read, CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md @9aed0e1263, hashes to 07f69b02...be0bc23, equal to the signature_file_sha256 in dell1's committed check record. Its section 'What they leave' says no attestation exists, so a taken-over maker account is bounded only by the release's age and the February copy matching, that check 7 does not show the antivirus inspected the file, and that the February match does not rule out a file bad in February too. That is the true answer and claims nothing beyond what was checked. The words are as the CTO recorded them; this seat did not hear the session.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show ba2e7f6545 (the addendum)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md @9aed0e1263, lines 24-34, sha256 07f69b028ef2...",
    "git show c25860a18b:.../tabulate-0.9.0-py3-none-any.whl.check.json (check 8 evidence.signature_file_sha256)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S84",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:20Z",
  "one_line": "Rounds 24-25 rows: W126-S1 (client-data check reports NOT checked on this box) and W128-S1 (check 8 re-run with the signature) dismissed with reason.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W126-S1",
   "NFRA_CTLPLN-W128-S1"
  ],
  "spec_asserts": "Every row a round mints is dispositioned before its L10.",
  "world_is": "W126-S1 (ARMED, disarm owner 0.0.0_AB_MSTR): the ruled WARN-only state (Andrew 2026-10-09; the laptop list set aside 2026-10-14), accepted by the CTO in round-24 ruling 5 and adjudicated NOT_A_DEFECT for the same condition in COMM_ASSIST ADJUDICATION_v10 D2-S2; no client account id travels in this project's commits. W128-S1 (INERT): re-running check with the signature is the batch's normal step (round-25 ruling 3); the re-run JOURNEY-CHECK here reads check8=SIGNED released=True.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ledger/ROUND_ANALYSIS.round24.md ruling 5; ledger/ROUND_ANALYSIS.round25.md ruling 3",
    "python .tools/tests/test_round25_journey_record.py --check -> check8=SIGNED released=True ok=True"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W126-S1 is a ruled state, not a defect, and is disarmed by the CTO's acceptance; W128-S1 is the batch's normal step."
 },
 {
  "id": "NFRA_CTLPLN-C-S85",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:20Z",
  "one_line": "FWD delta after round 25: 5 -> 7 REALIZED (FWD-16, FWD-17), 19 -> 17 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED; denominator 28. FWD-15 is one dell1 lane run short.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "C-S81, C-S82, C-S83. Unchanged and not re-read this round: FWD-14 (Andrew's sitting, c9a4 and b87f), FWD-18, FWD-19, FWD-11 as C-S80 left them.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this record's C-S81 to C-S83",
    "ledger/ROUND_ANALYSIS.round25.md section 1 (the table entering the round)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard."
 }
]
```
