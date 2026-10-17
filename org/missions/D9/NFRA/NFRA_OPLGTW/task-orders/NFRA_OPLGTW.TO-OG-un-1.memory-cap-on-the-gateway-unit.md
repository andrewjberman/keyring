# NFRA_OPLGTW task order -- `OG-un-1` -- a memory cap on the gateway's systemd unit, so a runaway request can never take the host's system daemons (round 41; repair of the ARMED hazard row Z-S375, CTO decision 35541)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-un-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-un-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~140</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a unit file and an offline test; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision 35541 on row Z-S375: "a MemoryMax on the gateway unit, so an OOM can never take the system daemons".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-un-1` (decomposition addendum R3-T.116, round 41, workstream ENRICH-R41-T)

THE DEFECT. On 2026-10-17 at 17:21Z a runaway request (a whole gold table converted to Python, row `Z-S375`) used the 1.8 GB gateway host's memory; the unit `deploy/opal-gateway.service` sets no memory limit and no OOM score, so the kernel OOM killer took the gateway and then eight system daemons (`irqbalance`, `chronyd`, `atd`, `acpid`, `lsmd`, `agetty`, `systemd-resolved`, `-logind`, `-networkd`, `-homed`, `-userdbd`, `gssproxy`; the shell that ran the harness had `oom_score_adj` -900). `chronyd` read unsynchronised afterwards, and this host signs every AWS call, so clock drift breaks SigV4.

THE FIX (a unit file only):
1. In `infra/aws/ec2/opal-gateway/deploy/opal-gateway.service`, in the `[Service]` section, add `MemoryHigh=1200M`, `MemoryMax=1400M` and `OOMScoreAdjust=300` (a cgroup that passes `MemoryMax` is killed and restarted by `Restart=on-failure` inside its own cgroup, and a positive score makes the gateway the preferred victim ahead of every daemon), each with a one-line comment saying why; change NOTHING else in the file (`ExecStart`, `--workers 1`, the hardening lines and every comment stay byte for byte). The measured working set of the gateway is about 100 to 450 MB across the page chains of `OG-ap-36`; 1400 MB of a 1846 MB host leaves about 440 MB for the system.
2. Do not touch `deploy-to-ec2.sh` (it already copies the unit and runs `daemon-reload` and `restart` on every deploy), `EC2_MANIFEST.json`, or any app file.

TESTS (new file `tests/test_og_un1.py`; read an existing test that reads a file under `deploy/` for the pattern):
- `test_ogun1_ac01`: the unit file has `MemoryMax=` between 1000M and 1500M inclusive, `MemoryHigh=` strictly below `MemoryMax`, and `OOMScoreAdjust=` a positive integer up to 500, all inside `[Service]`; every other line of the file equals the line at the base (read the base text with `git show HEAD:infra/aws/ec2/opal-gateway/deploy/opal-gateway.service` ONLY if the file is tracked in your worktree; otherwise embed the base's non-added lines in the test as a literal and assert the file equals them plus exactly the three new directives and their comments).
- `test_ogun1_ac02`: `deploy-to-ec2.sh` still copies `deploy/opal-gateway.service` to `/etc/systemd/system/` and still runs `systemctl daemon-reload` before `systemctl restart` (a text check that the three commands exist, in that order), so the new limits take effect on the next deploy; and `--workers 1` and `NoNewPrivileges=true` and `ProtectSystem=strict` are still in the unit.
If an existing test pins the unit file's text, update it to the new truth with the smallest edit and name it in your report.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no change to `deploy-to-ec2.sh`, the manifest or any app file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy/opal-gateway.service
infra/aws/ec2/opal-gateway/tests/test_og_un1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `deploy/opal-gateway.service` and `tests/test_og_un1.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~140/`. Rows: id `NFRA_OPLGTW-Z-W140-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-un-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_un1.py test_ogun1_ac01 test_ogun1_ac02; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 2 of 2; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-un-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~140 '^infra/aws/ec2/opal-gateway/(deploy/opal-gateway\.service|tests/test_og_un1\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~140: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the unit carries the three directives in range and nothing else changed; the deploy still installs and restarts it. `AC2`: the commits of this serial touch only the two files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-un-1.memory-cap-on-the-gateway-unit.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the AC lines).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41-T (decomposition addendum R3-T.116): the CTO's decision 35541 on row `Z-S375`. It ships in the next gateway release under its own never-widen (a unit-file change takes effect on the deploy's `daemon-reload` and `restart`); the applier's Phase A reads the limits on a scratch process if it can, never by repeating the OOM on the live host.
- A limit that is too low would make the gateway restart under a legitimate load: the values come from the measured working set (100 to 450 MB across the window chains, plateau 386 MB) with a wide margin; the applier's release read-back is the check.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent).

<status>complete</status>
<round>41</round>
<workstream>ENRICH-R41-T</workstream>
<slot>~140</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
