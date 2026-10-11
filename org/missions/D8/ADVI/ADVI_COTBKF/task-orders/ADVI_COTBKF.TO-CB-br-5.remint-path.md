# TO ADVI_COTBKF.TO-CB-br-5.remint-path -- round 70 CB-br-5: a re-mint path in the mint adapter: built, tested, NOT run; it replaces named day files and refuses any file not on its list

<to_id>ADVI_COTBKF.TO-CB-br-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~115</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-br-5` (`decompositions/ADVI_COTBKF_DECOMP.round70.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` ADDENDUM v0.7 (the last addendum); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_70_20261011.md` section 2 items 1 and 2 and section 3 item 5; rows
ADVI_COTBKF-D2-W107-S1 and D2-W107-S2 in the channel; the round-69 facts
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~107/REMINT_FACTS.json` and its `.md`;
`data/assets/scripts/silver/commonwealth_account_return_daily.py` in full (`build`, `source_addresses`, `minted_objects`, `apply_days`,
`verify_served`, `require_pinned_split_store`, the pair-file checks) and its tests `test_commonwealth_ard_*.py` and `conftest.py`.

**The gap.** No code replaces an existing day file of the served table. `apply_days` is a MINT: it refuses any target key that
exists, takes no date argument and loops over every day in the manifest. PRD ADDENDUM v0.7 parks the re-serve until the list of open
corrections closes; "No pair is written on a path that does not exist." So the path is BUILT AND TESTED now, and NOT RUN.

**Your item. No AWS call: tests fake S3. You do NOT run the new mode against the bucket, nor `--apply`, `--build` or `--verify-served`.**

1. **A new mode, `--remint`,** beside `--apply`, in the adapter. It takes: `--manifest` (the NEW build's stamped manifest, whose
   `split_store.pinned` must be true), `--days-dir` (the new build's day files), `--remint-list <file>` (a JSON list of dates: the
   ONLY day files it may replace), and `--capture <file>` (a JSON object, one entry per listed date, with the ETag and version id of
   the served `data.parquet` and `manifest.json` it expects to find: the capture a sign-off names).
2. **It REFUSES, before any write, with a `REFUSED:` line naming the cause, when:** the list is empty or names a date not in the
   manifest; the capture lacks a listed date or the served object's ETag or version id differs from the capture (the served table
   moved since the sign-off); a listed date's NEW day file equals the served one (nothing to replace: the list is wrong); **any day
   file NOT on the list differs between the new build and the served table** (compare by the content hash the manifest already
   carries per day against the served day's: the re-mint would leave the table inconsistent with its own manifest, or would need a
   file the list does not name); the manifest's hold list or split-store pin is absent; the two pair files `apply_days` already
   requires are absent.
3. **It writes** only the listed dates' `data.parquet` and per-day `manifest.json`, through the producer's own `emit_day` as
   `apply_days` does, then re-reads each written key and compares its content hash with the new day file. The sidecar and the
   method row are written ONLY if their content differs from what is served, and then they must be named in the capture too, else
   REFUSED. It prints one line per replaced date and a last line
   `ARD-COTTONWOOD-REMINT listed=<n> replaced=<n> unlisted_differing=0 sidecar=<unchanged|replaced> method_row=<unchanged|replaced>`.
4. **It deletes nothing.** The bucket keeps versions; rollback is a copy of the captured version id, done by a person under the
   sign-off, not by this code. Say so in the mode's help text.
5. **The build command carries the hold list.** `build` records the hold list the FWD-3 manifest states (the served one is three
   CUSIPs) into the mint's manifest next to `split_store`; `--remint` refuses a manifest without one. Find where the FWD-3 manifest
   records it (`commonwealth_fwd3_serve.py --hold-cusips`); if it records none, carry `[]` and say so.
6. **Tests** (synthetic, the faked bucket of the existing tests): a clean re-mint of 2 of 5 days replaces exactly those 4 objects and
   nothing else; each refusal in step 2 fires before any put (assert the put list is empty); an unlisted differing day refuses; a
   capture whose ETag moved refuses; the sidecar and method row are untouched when unchanged; `--apply` still refuses an existing key
   (the mint path is unchanged). Keep every existing `==`.

**You do not decide which dates are re-minted or when. You build the door and prove it stays shut on anything not named.**

### ACCEPTANCE

<criterion id="CB70br5-AC1" cell_refs="CB-br-5"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB70br5-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB70br5-AC2" cell_refs="CB-br-5"><invocation>python -c "a=open('data/assets/scripts/silver/commonwealth_account_return_daily.py',encoding='utf-8').read();t=open('data/assets/scripts/silver/tests/test_commonwealth_ard_remint.py',encoding='utf-8').read();print('ARD-REMINT-PATH mode=%s list_flag=%s capture_flag=%s last_line=%s tests=%d delete_calls=%d'%('--remint' in a,'--remint-list' in a,'--capture' in a,'ARD-COTTONWOOD-REMINT listed=' in a,t.count('def test_'),a.count('delete_object')))"</invocation><expect>ARD-REMINT-PATH mode=True list_flag=True capture_flag=True last_line=True</expect></criterion>
`CB70br5-AC2` -- the mode, its two flags and its last line exist, with its tests in their own file; the counts of tests and delete calls are
printed for the issuer to read (delete calls must read 0).

<criterion id="CB70br5-AC3" cell_refs="CB-br-5" judgment="true"/>
`CB70br5-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: every refusal fires before any write, by test; an
unlisted differing day refuses; a moved capture refuses; nothing is deleted; the mint path is unchanged; the mode was not run against
the bucket.

<expected_criteria>CB70br5-AC1,CB70br5-AC2,CB70br5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** `commonwealth_fwd3_serve.py`, `commonwealth_daily_valuation.py`, `commonwealth_sweep_regrade.py`,
  `commonwealth_flows.py`, the gold producer, the tracked mint manifest under another worker's deliverables, `lib/`. If the hold list
  cannot be carried without editing the serve script, stop: that is the refusal clause, and say what the serve script would need.
- **The new mode is NEVER run against S3 by you.** No AWS call of any kind.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids and reason codes only. A build log line carrying `read_account=` is never echoed.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W115-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round70.md</decomp_doc> (round 70), cell `CB-br-5`.
<owned_cells>CB-br-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB70br5-AC1, CB70br5-AC2, CB70br5-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~115/ADVI_COTBKF.TO-CB-br-5.remint-path.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB70br5-AC1,CB70br5-AC2,CB70br5-AC3` BEFORE the flip. Mechanical: CB70br5-AC1 and CB70br5-AC2. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the mode's arguments and help text; every refusal with its text and the test that shows it fires before any put; what it writes and how it reads back; how the hold list is carried, or why it cannot be without the serve script; tests added and changed, by name; the diff of the adapter; the pytest line; the `ARD-REMINT-PATH` line; a statement that the mode was not run against the bucket and nothing is deleted; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and its tests; the mode is not run.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; tests fake S3; BLIND: whether the applier's identity may overwrite those keys is not read here and belongs to the pair.
comp-adversary: RUN -- the path refuses a file not on its list, a moved capture, an empty or wrong list and an unlisted differing day, each before any put, by test; it deletes nothing; the mint path is asserted unchanged; the cell is barred from running it; BLIND: the upstream silver re-serve it presumes is another script's write, not built here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-70 analysis @991f749df1 (msg 5340), section 3 item 5; PRD ADDENDUM v0.7 @72d624cd26; `3.0.0_SA_CVO` REMEDIATION_v40 @90e1a7cbda.
