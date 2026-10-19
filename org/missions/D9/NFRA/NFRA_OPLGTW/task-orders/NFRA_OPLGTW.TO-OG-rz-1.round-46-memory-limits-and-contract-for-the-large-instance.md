# NFRA_OPLGTW task order -- `OG-rz-1` -- CODE: the gateway unit's memory limits, their test bounds and the contract's target instance type, for the `t4g.large` host (round 46; Andrew-direct ~18:3xZ 2026-10-19: "lets raise it to large")

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rz-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rz-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~164</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- three repository edits; no schedule, trigger or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS call; the order edits files only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew-direct ~18:3xZ 2026-10-19 relayed by `1.0.0_SA_CTO~Z` (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_183xZ_GATEWAY_EC2_RESIZE_TO_T4G_LARGE.md` @439343a969) and by `0.0.0_AB_MSTR~Z` msg 36070 ("we need to get it up to a larger EC2 because it's choking on large requests on small"). The gateway host is `t4g.small` (2 GiB); the unit holds `MemoryHigh=1200M` and `MemoryMax=1400M`; the host is moving to `t4g.large` (8 GiB).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-rz-1` (decomposition addendum R3-T.123 amendment A5, round 46, workstream ENRICH-R46-E)

Your worktree is `C:/tmp/og-rz1` (branch `wk-NFRA_OPLGTW-164`), created by the issuer from `box/sitez` at `96cca43b19604141f85b819037a3b92f6c2bdf03`. Work ONLY there; every path below is relative to it, under `infra/aws/ec2/opal-gateway/`.

Make exactly these edits, and no other:

1. **`deploy/opal-gateway.service`:** set `MemoryHigh=5600M` (was `1200M`) and `MemoryMax=6400M` (was `1400M`). Leave every other line, including the comments, as they are, except that a comment line that states the old numbers or the 2 GiB host is reworded to the new numbers and the 8 GiB host (change nothing else in a comment).
2. **`tests/test_og_un1.py`:** move the bounds to match. The `MemoryMax` range assertion `1000 <= max_mb <= 1500` becomes `4000 <= max_mb <= 7000`, its message and the module docstring line that names `1000M..1500M` follow, and the expected-line list entries `"MemoryHigh=1200M"` and `"MemoryMax=1400M"` become `"MemoryHigh=5600M"` and `"MemoryMax=6400M"`. The `MemoryHigh` strictly-below-`MemoryMax` assertion stays as it is.
3. **`deploy/NFRA_OPLGTW_CONTRACT.json`:** `"target_instance_type": "t4g.small"` becomes `"t4g.large"` (line 351). Change no other key; keep the file's formatting and line endings byte-for-byte elsewhere.

**Do NOT touch** the Terraform (`infra/aws/terraform/opal-gateway/main.tf` is the applier's), `deploy-to-ec2.sh`, `EC2_MANIFEST.json`, any `app/` file, any other test, or any other line. If a second test or file names the old limits (search with `comp-find`, count the hits as the denominator), do NOT edit it: report it in a row (`NFRA_OPLGTW-Z-W164-S<k>`, `BLOCKING` only if a test then fails) and keep working.

Run `python3 -I -m pytest tests/test_og_un1.py -q` from `infra/aws/ec2/opal-gateway/` in your worktree: it must pass. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPLGTW~164 <0.9.0_WK_NFRA_OPLGTW~164@opal.agent>" -F <msgfile> -- <the three paths>`, the message file written by a non-shell writer. Do NOT push; never rebase, stash, `checkout --` or `clean`.

## 2. BOUNDS

- Three files, the lines above. No new file. No AWS call, no network, no deploy.
- The new values are the issuer's; do not tune them. A reason to think they are wrong is a row, not an edit.
- REFUSE a criterion you cannot meet as written. File a row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy/opal-gateway.service
infra/aws/ec2/opal-gateway/tests/test_og_un1.py
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; run from the repo root of YOUR worktree)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rz-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/rz1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)unit MemoryHigh 5600M MemoryMax 6400M \(want 5600M and 6400M\): yes; MemoryHigh strictly below MemoryMax: yes.*contract target_instance_type t4g\.large \(want t4g\.large\): yes.*files changed against the base 3 \(want 3\); lines changed outside the named ones 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rz-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/rz1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)unit MemoryMax=6400M; test_og_un1: \d+ passed, 0 failed.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the unit, the test bounds and the contract carry the new values and nothing else changed (3 files, only the named lines).
- `AC2`: the unit reads `MemoryMax=6400M` and `tests/test_og_un1.py` passes against it.

## 5. WHEN YOU ARE DONE

Report once in your final message: the commit hash, the output of both checks, and the denominator of any other file you found naming the old limits.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, a mid-round cell on Andrew-direct via the CTO and `0.0.0_AB_MSTR~Z` (msg 36070), amendment A5 of R3-T.123. Values: `t4g.large` has 8 GiB; `MemoryMax=6400M` leaves about 1.6 GiB for the OS, the SSM agent and the cgroup-guarded fresh-process reads (separate scopes, `MemoryMax=1400M` each); `MemoryHigh=5600M` keeps the soft throttle 800M below the hard limit. The old pair was 1200M and 1400M on a 2 GiB host.
- Pre-cut: `rz1.AC1` and `rz1.AC2` base FAIL as expected (the unit reads 1200M and 1400M).
- The applier cell `OG-rz-2` takes this worker's commit whole into the release; the Terraform edit and the live instance change are its own.

<status>pending</status>
<status>complete</status>
<round>46</round>
<workstream>ENRICH-R46-E</workstream>
<slot>~164</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
