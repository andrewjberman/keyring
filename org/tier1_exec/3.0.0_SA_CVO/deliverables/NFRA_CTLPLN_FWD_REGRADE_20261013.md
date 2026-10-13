# NFRA_CTLPLN -- full re-grade of FWD-1..28 against PRD v0.28 (2026-10-13)

**Grader:** `3.0.0_SA_CVO~L` (laptop), on Andrew-direct ~13:4xZ via 4.0.0_SA_CRO msg 108750
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_134xZ_NFRA_CTLPLN_FULL_FWD_REGRADE_BY_CVO_L.md` @256574f3d1).
**Basis:** PRD v0.28 @5a2b425d6b, each outcome's DONE WHEN and ACCEPT. Earlier grades: the last full table
(`ledger/ROUND_ANALYSIS.20261009.md`) and the deltas in `ROUND_ANALYSIS.round6..round11.md`. Live reads by this seat, 2026-10-13
~14:0xZ-14:2xZ, after `git fetch`:
- `thread-trace.py --round 11 --order TO-CT-aa-2`
- `crossbox-matrix.py`
- the first-parent author census of origin/CLOUD
- the CT-x-1 proof instance
- RDP port 3389 and key SSH logins from the laptop to sitez, dell1 and dell2

**Rule:** REALIZED only when the DONE WHEN exercise has been read AND every ACCEPT clause holds. GATED names its gate. An outcome
with no new evidence since 2026-10-09 keeps that table's pin and says so.

## Tally: 2 REALIZED, 19 ADVANCED, 2 GATED, 3 NOT SERVED, 2 MOVED (28)

Change from 2026-10-09 (0 / 18 / -- / 6 / 2):
- FWD-1 and FWD-28 are REALIZED.
- FWD-4 moves from NOT SERVED to ADVANCED.
- FWD-6 moves from NOT SERVED to GATED.
- FWD-27 is new and GATED.
- FWD-28 is new and REALIZED.

| FWD | grade | pin | one sentence |
|---|---|---|---|
| 1 one real round planned on the laptop, worked on dell1, integrated, graded | **REALIZED** | `thread-trace.py --round 11 --order TO-CT-aa-2`: hops=5/5, orders_found=1 (6c3c63c05d -> 98e48fcbb2 dell1 -> 4899c05b9a CLOUD -> 793fc0c9dd grade), re-run today | Every hop is read from git refs, across two boxes and the trunk, in 4h40m. |
| 2 a box added once; every tool knows it | ADVANCED | `org/devices/DEVICES.json`; `.tools/to-pipeline-gate.py:93` FABRIC_ENUM still a literal (ADJUDICATION_v7 C-S15) | The Dells were added and seats run on them, but one gate still lists boxes by hand, so a fixture box would need an edit. |
| 3 a seat reaches a seat on any other box, read shown | ADVANCED | `crossbox-matrix.py` today: pairs=12 with_file=12 acked=11 closed_both=4 | 11 of 12 directed pairs carry a bus-id ack; dell1->sitez (XB-...-760d, opened 12:35Z) is the open pair. |
| 4 rounds reach the trunk without the box writing it; at most one unpushed round per lane | ADVANCED | origin/CLOUD first-parent since 2026-10-11: 1079 of 1079 commits by `0.0.0_AB_MSTR`; integrate merges of box/dell1 281, box/dell2 261, box/sitez 238, box/laptop 303 | Clause 1 holds as measured; the "no more than one unpushed round per lane" clause has no read. |
| 5 a push deploys only what a signed change names | ADVANCED | REMEDIATION_v2 D1-S8 (`pre-push-safe-deploy.sh:56-57,82,104`, OPEN, owner COO~C) | The gate is applied, but its deploy set is bounded by the box diff (a named file can miss its deploy), and the DONE WHEN push has not been read. |
| 6 routine work merges with no one's word; only a client-facing release waits for Andrew | **GATED** | box-sync integrates daily (row 4); round 11 analysis section 4: the portal `firmAccess.ts` PROD push (53506d4903) waits on Andrew | The routine arm runs every cycle; the held arm is live and waits on Andrew's word for that PROD release. GATE: Andrew. |
| 7 every project's box is visible; none split | ADVANCED | 2026-10-09 table (CVO PINS @a69d29a7b0; 26 overlaps then) | No placement read across four boxes since the Dells joined; carried unchanged. |
| 8 two boxes never edit one file at once | ADVANCED | ADJUDICATION_v10 C-S31 (crossbox per-box-file design MET); box-sync auto-resolves conflict classes | The fix for the crossbox class is designed, not built, and no conflict-free parallel round has been read. |
| 9 scarce-account leases | NOT SERVED | 2026-10-09 table | No order has named FWD-9 or C-LEASE. |
| 10 a Dell deploys its named commit unblocked; access changes refused | ADVANCED | TO-CT-x-1 proof (`...CT1/deliverables/NFRA_CTLPLN.TO-CT-x-1...proof_of_spec.json`, closed @ef9332dbfd): off-trunk read-back ok=True; refused IAM write AccessDenied | Both arms were exercised in driven form, but the "deploy" re-put an object with identical bytes (DELTA=0), so a Dell deploying its own changed work is still unread. |
| 11 a box restarts mid-round, nothing lost | NOT SERVED | 2026-10-09 table | No order has named FWD-11 or C-RESTART. |
| 12 every box's decisions in one list on the laptop; answers reach the box | ADVANCED | `org/devices/crossbox/XB-20261008T203134Z-a3f0.json` (dell2 -> laptop, "ANSWERED by Andrew (Yes do it)", acked by bus id, CLOSED-BOTH) | The answer round trip is real; the "one list on the laptop" half is not shown being read. |
| 13 a project moves between boxes by measured bid | NOT SERVED | 2026-10-09 table | No order has named FWD-13 or C-BID. |
| 14 RDP from the MacBook to four boxes and from the laptop to three | ADVANCED | laptop -> 100.99.180.19, 100.79.95.44, 100.104.84.87 port 3389: True, True, True (today) | The ports answer from the laptop over the tailnet; no session record exists for the seven sessions the DONE WHEN names. |
| 15 one real package laptop -> Dell, checked; the lane's work runs | ADVANCED | `...CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.receive.txt` @4899c05b9a (7/7 hashes, verify/prove ok, venv install, `CLICK 8.3.1`) | The package went the whole way to dell1, but no lane needed it, so "the lane's work then runs" is a version check only. |
| 16 approved or refused, read back by an outsider | ADVANCED | 2026-10-09 table (CRO assessments; CTO approvals) | No outsider read-back of both decisions since; carried unchanged. |
| 17 what was checked and what it cannot rule out, read aloud to Andrew | ADVANCED | `*.check.json` records; TO-CT-aa-2 plain summary graded NOT MET (ADJUDICATION_v13 C-S38) | The records exist, but the plain summary omits a stated limit and has not been read to Andrew. |
| 18 a download tried and stopped on a Dell and on site Z, told the route | ADVANCED | `...CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.blocked-download.txt` and `TO-CT-y-2.fresh-process-record.txt` @4899c05b9a | dell1 stopped pip with PIP_NO_INDEX=1, but the refusal names no route, nothing covers non-pip downloads, and site Z is untried. |
| 19 "what did this box download today" answered from a record | ADVANCED | `NFRA_CTLPLN.TO-CT-v-3.receive.txt` STEP 3 ("DOWNLOADS-TODAY requests=0", from the pip log at the time) | One box-day was answered inside an order record, but the waiting-lane view in the decision list is not built. |
| 20 Teams request end to end | MOVED | PRD v0.21 @805fec22c5 -> COMM_ASSIST FWD-1 | Graded by COMM_ASSIST. |
| 21 every manager keeps its fabric running and rules on nothing | ADVANCED | 2026-10-09 table (CT-s-4 @d59d9dbf7f); REMEDIATION_v5 S9117/S9118 | The unstick step is built, but no unattended recovery or day read is recorded, and the tree-kill tools crossed seat boundaries (5 seats lost on dell2). |
| 22 a lead settles its own box's calls; cross-box calls settled on the record | ADVANCED | `crossbox-matrix.py` today (11 of 12 acked); CVO verdict @a803dad6ae and addendum @89c1366b5f (superseded close) | The cross-box arm is close (11 of 12); no read exists of a one-box decision settled and never shown to Andrew. |
| 23 seat list readable; nothing finished without a reviewer's grade | ADVANCED | round-close-check: judgments graded 3/3 rounds 8-11 (laptop) | The grade half is live on the laptop; seats.json exists only for the laptop, and no person-names-each-seat read is recorded. |
| 24 research owed above the line, read alike by two leads | ADVANCED | 2026-10-09 table (CT-s-8) | Built; the two-leads comparison has not been run. |
| 25 a seat knows its role from its start; a tool stops or flags the forbidden act | ADVANCED | 2026-10-09 table (CT-s-2 @46831c5dfe, WARN mode) | The forbidden-act half was exercised in WARN mode; the seat-start half has no record. |
| 26 one voice file for drafts in Andrew's name | MOVED | PRD v0.21 -> COMM_ASSIST FWD-2 | Graded by COMM_ASSIST. |
| 27 every box answers an SSH login from the laptop by key, and nothing else | **GATED** | today from the laptop: `ssh -o BatchMode=yes` -> OPAL_BLOOMBERG, DESKTOP-HK1UU7N, DESKTOP-N8RJV0A (rc 0); the laptop itself refused (the Entra account is not resolvable by sshd); `PasswordAuthentication` unset (on) on all three | Key login works on three of four boxes; "nothing else" fails until password login is off (STEP 2, Andrew's elevated line per box), and the laptop needs a local account. GATE: Andrew. |
| 28 the data-proxy fence by route class | **REALIZED** | ROUND_ANALYSIS.round10 (CT-u-7, CT-w-3 applied and read back; 33/33 firm tests on DEV); PRD v0.28 text matches `lambda_function.py:2112` (review @0648bcbe0c) | Exercised on all 41 routes under the v0.28 wording; the Dev clause is named a widening, and CT-aa-5 removes it. |

## Limits of this grade

- **Not re-measured today; carried with the 2026-10-09 pin:** FWD-7, 9, 11, 13, 16, 21 (partly), 24, 25.
- **COMM_ASSIST's own grade not read here:** FWD-20, 26.
- **What the live reads are:** the RDP read is a port check, not a session. The SSH reads are this seat's own logins from the
  laptop.
