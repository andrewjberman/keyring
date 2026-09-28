# NFRA_OPLGTW task order -- `OG-h-1` -- ROUND 2 (E10): the batch cell -- eol rules, out-of-repo citations, test hygiene, and the probe-fixture card

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~13</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository hygiene; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- one read-only DynamoDB Scan (projection pk, sk) on an existing table; no write, policy or role.
comp-adversary: DECLARED-NOT-APPLICABLE -- every item is a graduated remediation row with its mechanism measured (REMEDIATION_v1.md).
EGRESS CLASS, declared: Opal's own AWS (one read-only Scan) plus the PyPI download for the venv below -- development egress permitted to this project's COO and its workers (Andrew-direct ~21:2xZ, record @7bfa5811c6).
</preflight>

## 1. THE CELL -- `OG-h-1` (decomposition addendum R2-E, item E10)

Five remediation rows, batched into one cell, plus one card for Andrew. Each item names the row, what was measured, and
what you do. The row texts live in
`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` and
`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/remediations/REMEDIATION_v1.md`; read each before you start.
This cell is handed LAST in the round, after `OG-x-2` has merged: re-read every cited test line at your HEAD before
you edit it.

### Item A -- eol rules for the gateway's shipped text (row W2-S8, ARMED, owner 2.0.0_SA_COO~O)
Measured: a deploy from a Windows worktree with `core.autocrlf=true` shipped 9 of 68 files with CRLF, every one an
extension with no `eol` rule. `/.gitattributes` carries `*.py text eol=lf` and `*.sh text eol=lf` but no rule
for `.service`, `.txt`, `.yaml`, `.json`, `.md`, `.html` or `.jsonl`.
Do: add ONE rule block to `/.gitattributes`, scoped to the gateway tree only, never a repo-wide glob:
`infra/aws/ec2/opal-gateway/**/*.<ext> text eol=lf` for each of the seven extensions, with a two-line comment naming
row W2-S8. The domain is the tracked gateway files with those extensions (41 at drafting: service 1, txt 2,
yaml 2, json 19, md 8, html 1, jsonl 8). One of them is stored CRLF in the index at drafting:
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (`git ls-files --eol` reads `i/crlf`). Renormalize it in the
same commit (`git add --renormalize` on that path) and state in your result that its shipped bytes change from CRLF to
LF at the next release. Re-run the census at your base; if more than that one file is `i/crlf`, renormalize them all
and name each (a file outside `<paths>` is a BLOCKING row, never an override).

### Item B -- out-of-repo evidence citations (row S43, ARMED, owner 2.0.0_SA_COO~O)
Measured on the laptop: every `C:/tmp/nfra-oplgtw-sealed/` and `C:/tmp/nfra-oplgtw-handoff/` path the project cites was
ABSENT. Since then the seal inputs became durable: 7 SSM parameters `/opal/nfra_oplgtw/ogv4/reseal_20260918/{RQ1..RQ6,SALT}`
(row S42). The `nfra-oplgtw-handoff/` tree (a lambda source map cited by `TO-OG-i-3.alb-browser-paths.md:46`, and
OG-v-3's partial scripts cited by `deliverables/0.9.0_WK_NFRA_OPLGTW~6/sealed-real-expectations.result.md:12`) is not
shown restored anywhere.
Do NOT edit any completed order, result or proof instance. Instead write ONE register,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/OUT_OF_REPO_CITATIONS.md`, with one row per
citation of a `C:/tmp/nfra-oplgtw-` path under `org/missions/D9/NFRA/NFRA_OPLGTW/` (file:line, the cited path, and a
state). Worktree paths `C:/tmp/wk-*` and `C:/tmp/og-*` are transient by design and are EXCLUDED; print how many you
excluded. The state is exactly one of:
- `DURABLE <location>` -- the same content exists in the repo or a named durable store (an SSM parameter, an S3 key);
  name it, and say how you matched it;
- `ABSENT-ON-SITE-Z` -- the path does not exist on this device (`test -e`), and no durable copy was found.
This device cannot read the laptop's `C:\tmp`; never write `ABSENT` without the device qualifier.
Register rows are Markdown table rows, one per cited LINE, in exactly this shape (the check parses it):
`| <repo-relative file>:<line> | <cited path> | <state> |`. The census the check runs is `git grep -nE` for a
`C:/tmp/nfra-oplgtw-` path (either slash) over `org/missions/D9/NFRA/NFRA_OPLGTW/`, excluding the register itself, this
order's file and `deliverables/2.0.0_SA_COO~O/`. At drafting the citing files numbered 10; your count at your HEAD is
the one that binds.

### Item C -- the suite writes a tracked file (row W3-S2)
Measured: `infra/aws/ec2/opal-gateway/app/audit.py:29-33` appends every record to `_cfg.AUDIT_PATH`, and
`app/config.py:307` defaults it to `./audit.jsonl`, which is TRACKED. A suite run appends to it.
Do: in `infra/aws/ec2/opal-gateway/tests/conftest.py`, set `AUDIT_PATH` to a per-session temporary file BEFORE any
`app` module is imported (the default is read at import time), unless the environment already sets it.

### Item D -- a process-wide fake clock (row W3-S6)
Measured: `infra/aws/ec2/opal-gateway/tests/test_ratelimit.py:19-20` sets `rl.time.monotonic = lambda: _clock["t"]` at
module import and never restores it, which freezes asyncio's loop clock for every later test in the same process
(re-measured at the issuance base: `test_ratelimit.py` then `test_schwab_engine.py::test_ogq1_ac02` in one process
HANGS past 100 s; `test_ogq1_ac02` alone passes in about 6 s).
Do: scope the fake clock to that module's tests with a fixture (`monkeypatch.setattr`), so it is restored after each
test. The module's own assertions stay as they are.

### Item E -- two nondeterministic tests (row W6-S9)
Measured, two consecutive per-module sweeps each failed a DIFFERENT module:
- `tests/test_schwab_engine.py:259`, `assert child_lag < 0.25` inside `test_ogq1_ac02` (measured 0.446 s under load).
  Make it load-tolerant WITHOUT losing the difference it proves: the child arm must stay far below the in-loop arm
  (`:260` asserts `loop_lag > 1.0`). Compare the two arms, or derive the bound from the in-loop arm; do not just raise
  the constant.
- `tests/test_schwab_export.py:217`, `assert ... "s3" not in url.lower()` on a URL whose fragment is a random
  `token_urlsafe(32)` ticket, which can contain `s3` by chance. Apply the substring checks to the URL with its fragment
  removed; keep the check that the URL is the Gateway page plus `#`.
Line numbers are the issuance base's; `OG-x-2` edits both files first, so find the assertions by content.

### Item F -- CARD ONLY: 8 probe fixtures in the production table (row W2-S6). You delete NOTHING.
Measured on 2026-09-18: `gateway-access-state-table` holds 8 synthetic items written by round-1 probes, pk shaped
`POLICY#probe-og-i1-<timestamp>[-ttl|-race]` and `RUNTIME#probe-og-i5-<timestamp>`. A delete in a production store needs
Andrew's confirmation, so this cell only prepares it. Run ONE read-only Scan with `ProjectionExpression` `pk, sk`
(print no other attribute), and write
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/CARD_W2-S6_PROBE_FIXTURES.md`: the literal
pk/sk list of every item whose pk matches `probe-og-`, the total item count scanned (the denominator), and the exact
delete command per key for Andrew to approve. If the Scan shows any item that is not a probe fixture, list only its
count, never its key.

## 2. BOUNDS

1. You never delete, put or update anything in AWS. The Scan in Item F is the only AWS call.
2. **Interpreter (`<SUITE_INTERPRETER>`, ruling Q6 cleared):** build `.venv-og` at your worktree root ONCE:
   `python -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt moto pytest`.
   This PyPI download is permitted development egress (Andrew-direct ~21:2xZ, record @7bfa5811c6). Site Z has no
   `py -3.12`; `python` is 3.11. Never commit `.venv-og/` or `.scratch/`. You install nothing else.
3. You never edit `tests/test_identity_scope.py` or `identity_tool_allowlist.txt` (row S1's known red test,
   `test_scoped_deny_by_default`, stays deselected).
4. You work in the worktree named in your identity line; commit there under your serial with `.tools/safe-commit.sh`;
   every `.py` you touch passes `.tools/commit-gate.sh`. Never push, merge, rebase, `stash`, `checkout --` or `clean`.
   If `.gitattributes` is refused by a lane gate, that is ONE BLOCKING row on AC1 -- never an override.
5. Spec frozen. REFUSE a criterion you cannot meet as written and report its measurement. Anything off-spec is ONE
   surprise row, and you keep working.

## 3. SURFACES

<paths>
.gitattributes
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/tests/conftest.py
infra/aws/ec2/opal-gateway/tests/test_ratelimit.py
infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W13-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-h-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hy.AC1.sh; echo "exit=$?"</invocation><expect>attr eol=lf on all; stored CRLF 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-h-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hy.AC2.sh; echo "exit=$?"</invocation><expect>moto-importing modules excluded 0 -- run 1 passed, run 2 passed; tracked files modified by the runs 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-h-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hy.AC3.sh; echo "exit=$?"</invocation><expect>missing 0; unclassified 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Item A) -- every tracked gateway file with the seven extensions resolves `eol: lf` and none is stored CRLF.
- `AC2` (Items C, D, E) -- two consecutive single-process runs over the repaired modules (`test_ratelimit.py`, then
  `test_ogq1_ac02`, `test_schwab_export.py`, `test_oauth_durable.py`, with AUDIT_PATH unset so Item C is exercised)
  each pass and leave no tracked file modified. The check uses `.venv-og` when present.
- `AC3` (Item B) -- the register classifies every `C:/tmp/nfra-oplgtw-` citation in the project tree.
- Item F is read by the issuer at the drain and carded to Andrew; it is not a criterion.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/NFRA_OPLGTW.TO-OG-h-1.batch-hygiene.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Flip `complete` only when AC1-AC3 PASS by output. The
result file names, per item, the row it answers and what the reader should now see. Report once, in your final message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- The batch cell runs LAST (addendum R2-E edge: after `OG-x-2` merges, which also writes `test_schwab_engine.py` and
  `test_schwab_export.py`). Slot ~13, queue position 3; handed only after `OG-x-2`'s drain.
- `<SUITE_INTERPRETER>` resolved: `.venv-og` from the gateway's requirements plus `moto` and `pytest` (ruling Q6 HELD at
  5676f4a48a, cleared by Andrew-direct ~21:2xZ @7bfa5811c6 for all four ~O COOs and their workers).
- hy.AC2 is bounded for the worker's 120 s limit: it runs the four modules the rows name, 50 s per run, not the whole
  suite (the full suite does not fit; `test_schwab_engine.py` alone takes about 64 s on site Z).
- Item F's delete is Andrew's (Agent Autonomy: deletes in a production store need human confirmation).
- Disarms owed at the drain, by this seat: W2-S8 on AC1 PASS; S43 on AC3 PASS (the register is the restatement).
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell deploys nothing.

<status>staged</status>
<round>3</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
