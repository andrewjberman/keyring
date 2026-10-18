# NFRA_OPLGTW task order -- `OG-ev-6` -- EVIDENCE: the window page size measured on the host at 30, 60 and 120 partitions per page, under the hard guard, graded by a rule fixed here before any run (round 42; CTO round-41 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-6</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-6</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a measurement; no schedule or trigger is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the same objects are read through the gateway role, as in `OG-ap-36` and `OG-ap-38` Phase A.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-41 analysis item 1 ("the cell picks the new size from a measured sweep: page time and median growth at 30, 60 and 120 partitions, in a fresh process under the guard").
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ev-6` (decomposition addendum R3-T.119, round 42)

⛔ **THE HARD-GUARD RULE, BEFORE ANYTHING ELSE** (as `OG-ap-38`, amended A1). Every host run of this order that executes gateway code runs in a FRESH process under a HARD GUARD: `oom_score_adj` 1000 and a memory limit of 1400 MB, EITHER the address-space cap OR the cgroup limit (`systemd-run --scope -p MemoryMax=1400M -p OOMScoreAdjust=1000`; pyarrow cannot start its thread pools under the address-space cap, so the chain uses the cgroup guard, recorded as `oom_score_adj_1000_cgroup_memmax_1400mb`), and a wall limit of 120 s per run. Host memory is sampled every 0.25 s and a run stops at 75 percent used. A run without the guard is a STOP and a BLOCKING row. NO deploy, NO apply, NO file written to any bucket or table; scratch folders on the host are removed after.

THE QUESTION. The window page size is the module constant `PAGE_PARTITIONS = 30` in `app/client_adapter_bd49f.py` (one page = the newest `PAGE_PARTITIONS` partitions of a window per call). Since `OG-ap-36` a page reads in about 2 s against a 55 s limit, so 30 may no longer bind. Which of 30, 60 and 120 is the largest that stays inside the limits below?

THE RULE (fixed by the issuer BEFORE any run; `ev6.AC1` recomputes it from your runs, never from a flag of yours). THREE fresh-process runs per size. A size PASSES only if, in ALL THREE runs: the longest page took under 15 s; the host peak was under 75 percent; and the combined rows of the NEWEST 120 PARTITIONS hash equal (sha256 of the canonical rows, as `OG-ap-36`) to the hash size 30 produced (so every size returned the same rows over the same partitions); AND the median of the three run medians of RSS growth per page is 20 MB or less with no run median above 30 MB. `chosen_partitions` = the largest size that passes AND whose every smaller size also passed (a gap is not stepped over); 30 if 60 fails. A failed measurement is NOT re-run until it passes, and no limit is relaxed: report what the three runs read.

THE METHOD.
1. **Live ref and tree.** Read `deployed_commit` at HEAD (the live release; `d077cef043` when this order was cut). The candidate tree is trunk (`box/sitez`) at `trunk_sha`, which the issuer's GO names: it carries `PAGE_PARTITIONS = 30` and no change to the constant. Stage it in a SCRATCH folder on the host (as the Phase A runs of `OG-ap-38` did) and remove the scratch folder after. One SSM md5 read of the host's `app/` against the live ref first; a mismatch is a STOP.
2. **The sweep.** Use the guarded harness of `OG-ap-36`/`OG-ap-38` (`W/ap36_guarded.py`, `W/ap38_measure.py`, `W/ap38_guard.py`; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`) and the SAME 49F test account and the same chain method as `OG-ap-36`/`OG-ap-38` step 3(c), one call at a time. For each size S in 30, 60, 120, in each of three fresh processes: assign `client_adapter_bd49f.PAGE_PARTITIONS = S` IN THE PROCESS before the first call (no source file changes), call the transactions window through `client_core` for the account's window, following `next_cursor` page after page until the newest 120 partitions are covered (4 pages at 30, 2 at 60, 1 at 120). Per page record the wall seconds and the RSS growth since the previous page; per run record `max_page_wall_s`, `first_page_wall_s`, `median_growth_mb` (of the page-to-page growths; for a one-page run, the growth over the process baseline), `vmhwm_mb`, `host_peak_pct`, `pages`, and `rows_hash_120` (sha256 of the canonical JSON of all rows returned over the newest 120 partitions, in order). Hashes only; no row content, account number or name in any record.
3. **The record**, `W/PAGE_SWEEP.json` = `{"body": {"trunk_sha": "<40 hex>", "guard": "<named guard>", "rule_stated_before_runs": true, "sizes": {"30": {"runs": [3 x {"max_page_wall_s", "first_page_wall_s", "median_growth_mb", "vmhwm_mb", "host_peak_pct", "pages", "rows_hash_120"}], ...same for "60" and "120"}, "chosen_partitions": <30|60|120 by the rule>}}`. Commit it, run `ev6.AC1` (the invocation is below; it is the grade), REPORT the three numbers per size and the chosen size, and STOP. If a size cannot run (the account has fewer partitions than the size needs, a guard stop), record the runs you have, set `chosen_partitions` by the rule over what ran, say which size could not, and file a BLOCKING row; do not invent a run.

## 2. BOUNDS

- The measurement only. No deploy, no ledger, no Terraform, no IAM, no env key, no object or item written anywhere; scratch folders removed. Never: push, `git stash`, rebase, `checkout --` or `clean`; print an `.env` value, a credential, an account number, a person's name or email, or object content; **run gateway code on the host without the hard guard**.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ev6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)sweep record: 3 sizes x 3 fresh runs yes; every run carries its fields yes; the newest-120-partition row hash is one value across all runs and sizes yes.*the record says (\d+): agree.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record has three fresh runs for each of the three sizes with every field, the guard is named, one row hash covers all runs, and `chosen_partitions` equals the size the rule gives when recomputed from the runs. It PASSES whatever size the rule chooses (30 is an answer).

## 5. WHEN YOU ARE DONE

Run `ev6.AC1`, write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-6.round-42-window-page-size-sweep-on-the-host.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, and report once (counts, seconds, megabytes and booleans only). I flip the status after my own run of `ev6.AC1`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). Chain: this order -> `OG-en-29` (sets the constant to `chosen_partitions`) -> `OG-ap-39` (the batched release). The sweep needs no code change, so it runs at once on a GO naming `trunk_sha`; it is read-only (`<risk>WORLD</risk>` because gateway code runs on the host). The rule was written before any run, after the `OG-ap-38` lesson (a limit is never relaxed after a failed measurement; a statistic is fixed first).
- Pre-cut: `AC1` base FAIL as expected (the record is absent); the controls (a size too slow, a growth over the limit, a hash that differs, two runs, no guard named, a rule not stated first, a 12-digit number) all read NO in the dry-run.

- C4 READ (2.0.0_SA_COO~O, ~03:0xZ): `ev6.AC1` PASS on my run (script blob `93ae1c2507ba`), proof instance VALID; the rule recomputed from the nine runs: 30 passes (run medians 13.0, 7.8, 16.0 MB; longest page 1.89 s; host 43.2 percent), 60 fails growth only (38.8, 39.3, 29.6), 120 fails growth (193.6, 249.9, 225.0) AND the rows (127 over the newest 120 partitions against 222: the byte cap in `client_core._project`); `chosen_partitions` 30. The sweep ran after dell1's cg-3 ledger CLOSED (02:13:41Z) on the live ref `4257a2aa42`, host md5 139 of 139. `OG-en-29` is therefore superseded. Gate limb: none graded this flip.

<status>complete</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
