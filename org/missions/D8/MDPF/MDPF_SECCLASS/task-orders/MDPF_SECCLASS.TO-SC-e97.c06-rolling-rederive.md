# TO MDPF_SECCLASS.TO-SC-e97 -- round 23 SC-e-97: C_06 re-derives the producer's correction window on every fire

<to_id>MDPF_SECCLASS.TO-SC-e97</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~86</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-97` (`decompositions/MDPF_SECCLASS_DECOMP_R23.md`) |
**outcome_ref:** FWD-1 | **depends_on:** TO-SC-e96 (start only when its status reads `complete`; you are the same worker) |
**source:** CTO round-22 analysis section 2 (the ruling) and section 3 item 1, msg 4333

---

## WORKER FACE

### THE CELL

`SC-e-97`, rows MDPF_SECCLASS-D1-W83-S5 (ARMED, disarms at this ship's first post-act read) and D1-W80-S4. The CTO ruled **(a) a rolling re-derive**:
B_00 re-pulls the last N calendar days on every run and corrects canonical history inside that window by design, while C_06
(`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`) freezes a date at its first build. So on EVERY fire C_06 re-derives the dates
inside B_00's own window, with the number READ from B_00's rule at build time, never typed again. A date older than the window stays as built. The
served object announces it with `restated_through`.

Read first: your own record `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/WINDOW_READ_C06_ROLLING_20261012.json` (SC-e-96: where the
number lives, where C_06 can read it, the window, the cost, the orphans, the gap), then `build()` (:724-1150 at `4d2c87a73b`), `process_date`,
`_merge_and_write` and `_retained_only_pass` (SC-e-91; it keeps running on every date OUTSIDE the window and you do not change it), and
`build_firm_mix_summary` in `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` (:468-575).

**Build (C_06 and one pass-through in D_04; D_03 and the lib are READ ONLY):**

1. **Three module-level functions in C_06, with exactly these names and parameters** (the checker drives them; pure, no AWS call):
   - `producer_force_recent_days(catalog_text=None) -> int | None`: parse the `B_00|...|--upload --force-recent-days N` CATALOG line of
     `gold_dispatch.sh` and return N; return `None` when the text has no such line or is empty. When `catalog_text` is None read the source your
     record's `runtime_source` names (the sibling `gold_dispatch.sh` if present, else the S3 object `code/gold/gold_dispatch.sh` through the module's
     own client); a failed read returns `None`.
   - `rolling_window_dates(cube_dates, force_recent_days) -> list`: B_00's own arithmetic (`B_00.canonical_holdings.py:1119-1137`): anchor is the
     newest date, cutoff is the anchor minus N CALENDAR days, keep every date `>=` the cutoff, ascending. Empty for a missing or non-positive N.
   - `restate_window(existing_mix, existing_conc, rederived, window_dates) -> int`: for each date in `window_dates` set the relationship's entry from
     `rederived[date]` (`{'mix': {...}, 'total_mv': x, 'conc': [...]}`, the shape `process_date` returns), and REMOVE the date's entry where the
     partition no longer has the relationship on that date; never touch a date outside `window_dates`; return the number of DATES that changed;
     a second identical call returns 0 and changes nothing.
2. **`build()`.** Compute the window from the full key list BEFORE the `if not keys_to_process:` early return, and widen the incremental key set
   to the new partitions UNION the window's, so a fire with no new partition still re-derives the window and a fire with new ones re-derives both.
   For each relationship call `restate_window`, rewrite the relationship JSON and its period views ONLY when `restate_window` (or a new date)
   changed something, and print one line `C06-ROLLING-REDERIVE window=<first>..<last> dates=<n> relationships_read=<r> relationships_rewritten=<w>
   keys_written=<k>`. When the rule is unreadable (`None`) re-derive nothing, print `C06-ROLLING-RULE-UNREADABLE`, and behave exactly as today.
3. **The firm and advisor snapshots.** A re-derived date's firm and advisor day is REPLACED whole by the re-derived dollars (the existing
   `firm_daily_new` / `advisor_daily_new` accumulation already is the replacement for firm; for advisors, remove that date from an advisor whose
   relationships have no entry on it). Keep SC-e-91's `_apply_retained_moves(..., set(firm_daily_new))` so a window date is not adjusted twice.
4. **`restated_through`.** C_06 writes `restated_through` (the OLDEST date re-derived this fire, an ISO date string; unchanged from the stored
   value when nothing was re-derived) at the top level of `gold/views/mix_daily_summary.json` (`_write_mix_summary`), and D_04's
   `build_firm_mix_summary` copies it into `platinum/firm/mix_summary.json` as `restated_through`. Nothing else in D_04 changes.
5. **The cost cap.** Read `fits` and `largest_n_that_fits` from your record. If `fits` is true no cap exists. If it is false, add ONE module
   constant `ROLLING_MAX_DATES = <largest_n_that_fits>` that limits the re-derive to the newest that many window dates, with a comment citing the
   record, and state the gap in the half request in dollars from the record's `gap_if_truncated`. The constant name starts `ROLLING_MAX`; no other
   integer is assigned to a name containing RECENT or WINDOW.
6. **Orphans.** The `relationships_stored_not_in_partition` counts in your record say whether a relationship can hold a window date the partition
   no longer has. If every count is 0, say so in the half request and handle the removal only for the relationships the build already visits. If any
   is above 0, also visit the relationships NOT in the new data whose stored entries carry a window date (the listing `_retained_only_pass` already
   makes) and remove the date; state how many relationship JSONs that read touches per fire.
7. **Tests.** Add `data/black_diamond/scripts/gold/tests/test_c06_rolling_rederive_r23.py`, a pytest in the style of the sibling
   `test_c06_retained_unclassified_r21.py` (stub client, no AWS call): the rule parse (a value other than 14, an absent flag, empty text), the window
   arithmetic at the cutoff boundary, a re-derived date replaced, a date outside the window byte-identical, an orphan removed, idempotence, and one
   snapshot day replaced whole. The siblings must still pass; run the BD gold suite once at the end and report the count.
8. **The half request.** Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md` in the shape of
   `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md` (read it). Seven `## ` sections, in this order: **The act** (two code keys,
   C_06 and D_04, to `s3://opal-data-bd/code/gold/` by a CloudOps lane under a ledger opened at start, outside a BD gold run), **Blast radius**
   (what the act writes: two code objects; what the next fire writes: the relationship JSONs and views where a window date differs,
   `mix_daily_summary.json`, then D_03's outputs and D_04's `platinum/firm/mix_summary.json`), **Writers** (count the writers of the served
   `platinum/firm/mix_summary.json`, of `gold/views/mix_daily_summary.json` and of the relationship JSONs, `N = <n>` printed, each by file:line),
   **Both branches** (a window date whose partition differs, one that does not, a relationship absent from the partition, the rule unreadable;
   and the security-level list that stays Unclassified because no classifier places it, read from SC-e-98's record
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json` if it exists by then),
   **Rollback** (the prior C_06 object ETag `2e35d043163cc18b135d7698cf11dc56` VersionId `zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT`, the prior D_04 object
   by a head-object read you make, and the prior VersionIds of every key the next fire rewrites, recorded by the ship's pre-act read),
   **Expected outcome** (READ FROM THE RULE, never a point figure typed from the input: after the first post-ship fire, for every date in the
   window the served firm class dollars equal an independent rebuild from the then-current partitions within the rounding the code carries,
   $128.58 per snapshot (row D1-W85-S6); at 2026-10-09 the served Unclassified, $1,846,399.46 before SC-e-91's first fire, reads the rebuilt
   $883,483.05 (about -$962,915.51 against it) if no canonical byte moved), **Window and gap** (the N, whether a cap applies, and the gap in
   dollars). End with two lines left UNSIGNED: `COO half: UNSIGNED` and `CTO half: UNSIGNED`. Security-level and aggregate figures only; no
   relationship id, account id or client name appears in it.

### ACCEPTANCE

<criterion id="SC23-e97-AC1" cell_refs="SC-e-97"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py rederive</invocation><expect>ROLLING-REDERIVE ok=True</expect></criterion>
`SC23-e97-AC1` -- the module's own `producer_force_recent_days`, `rolling_window_dates` and `restate_window` parse a rule that is not 14, cut B_00's window at
the boundary, replace a re-derived date, leave an outside date byte-identical, remove an orphan and are idempotent.

<criterion id="SC23-e97-AC2" cell_refs="SC-e-97"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py wiring</invocation><expect>ROLLING-WIRING ok=True</expect></criterion>
`SC23-e97-AC2` -- `build()` computes the window before the early return, `restated_through` is written by C_06 and passed through by D_04, and no integer window is typed in C_06.

<criterion id="SC23-e97-AC3" cell_refs="SC-e-97"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py half org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md</invocation><expect>HALF-REQUEST ok=True</expect></criterion>
`SC23-e97-AC3` -- the half request exists with its seven sections, names both writers with N printed, and both halves unsigned.

<expected_criteria>SC23-e97-AC1, SC23-e97-AC2, SC23-e97-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~11:4xZ): AC1 FAIL as expected (`ROLLING-REDERIVE ok=False rule=False window=False restated=False
...`); AC2 FAIL as expected (`calls=False d04_passthrough=False`); AC3 FAIL as expected (`HALF-REQUEST ok=False error=absent`). A minimally
patched temp copy of C_06 and D_04 (the three functions, a call before the early return, the string in both) reads AC1 and AC2 `ok=True`; a copy
with `FORCE_RECENT_DAYS = 14` reads AC2 `no_typed_window=False`; a copy with `ROLLING_MAX_DATES = 7` reads AC2 `ok=True`; a half request with a section
missing, or with a half signed, reads `ok=False`. So every criterion can pass and can fail.

### AMENDMENT 1 -- what your own record settles, and four things the half request must carry (issuer 2.0.0_SA_COO~M1, 2026-10-12 ~12:2xZ; before you start)

Your record (`WINDOW_READ_C06_ROLLING_20261012.json`, SC-e-96 complete, merged @5d5e73ba2d) decides items 5 and 6 and sharpens the half request. Read it
with python; the numbers below are its, and you re-read them rather than copy them.
1. **No cap (item 5).** `fits` is true (cold 735.05 s against 1,800 s) and `largest_n_that_fits` is 15 of the 15 window dates: add NO
   `ROLLING_MAX_DATES`. The half request's **Window and gap** says the window is 15 dates, 2026-09-25 to 2026-10-09, the rule is N=14 read from
   `gold_dispatch.sh:99` (readable at runtime: `sync_scripts` places it beside C_06), and the gap is 0.
2. **Orphans (item 6) apply.** The record's `relationships_stored_not_in_partition` is above 0 on 14 of 15 dates (up to 15), so implement the
   removal for relationships the build would not otherwise visit: after the merge, visit the relationships NOT in the new data whose stored
   entries carry a window date (the listing `_retained_only_pass` already makes, 3,793 JSON keys at this read, 137.9 s to scan from this seat) and
   remove the date; state in the half request how many JSON reads a fire makes and that a second fire over unchanged partitions rewrites 0.
3. **The movement is large and the half request names it per date (Expected outcome and Blast radius).** The record's `per_date` shows the served
   Unclassified (D_04's rule) of $75.9M to $153.0M on each of 2026-09-30 to 2026-10-06 against a rebuilt $0 to $53,010, and about $1M on 10-07 and
   10-08, $1.85M on 10-09: the window restates those days by moving that Unclassified into other classes. Print the record's per-date table in
   the half request (served, rebuilt, delta), and in **Blast radius** name EVERY served object that embeds a window date's firm or advisor class
   dollars, read from the code and not guessed: D_03's period views (does a quarterly bar use the 2026-09-30 day?), D_04's `platinum/firm/mix_summary.json`
   (latest date only) and the advisor summaries; for each, say whether the move reaches it and by how much from the record.
4. **Memory (Blast radius).** The record's `peak_mb` (635.6) was taken in the scan process, not in a derive process; SC-e-95 measured 3.26 to 3.30
   GB for N = 1 to 5 including the static load (`RESIDUAL_READ_C06_FREEZE_20261012.json`, `rederive`). The build BULK-PRELOADS the window's
   partitions into `cube_cache` (:845-863). State: the total bytes of the 15 window partitions (head-object sizes), the runner instance type and its
   memory (a read-only `ec2 describe-instances` of `i-01003b035d2988dfb`; its instance type is in the launch template if stopped), and your
   estimate of the preload's resident size from one partition's in-memory size times 15; if the estimate exceeds 70 percent of the runner's
   memory, say so in the half request and say what you changed in the build (for example preloading in batches of the process pool's width).
   Mark each figure measured or inferred.
5. **Gate limb.** The issuer amends its own criteria without a CTO ruling; no gate limb grades an amendment to an existing order's criteria and
   `<status>` (this order declares `<placeholders>NONE`; the L6 gate grades newly-added orders and placeholders). The three criteria are
   unchanged.

### AMENDMENT 2 -- the rule is read from the sibling file only; no S3 key in C_06 (issuer 2.0.0_SA_COO~M1, 2026-10-12 ~12:2xZ; answers your row MDPF_SECCLASS-D1-W86-S6)

Your stop was right and your row is a RESULT, not something to route around. The naming gate (CLAUDE.md rule 30: every S3 address is
`lib/opal_naming.py address()` output; a builder refusal is a missing registry row, never a hand-typed workaround) refuses the literal
`code/gold/gold_dispatch.sh` in C_06, and you were right not to split it or borrow the prefix row. The S3 read is not needed: your own SC-e-96
record established that `sync_scripts` places `gold_dispatch.sh` flat BESIDE C_06 on the runner (`readable_at_runtime` true from that source).
1. **`producer_force_recent_days(catalog_text=None)` reads ONLY the sibling file** `gold_dispatch.sh` in the same directory as the module
   (`Path(__file__).resolve().parent / 'gold_dispatch.sh'`) when `catalog_text` is None. Remove the S3 fallback and `_read_dispatch_text`'s S3
   branch and the imports they brought. A missing or unreadable sibling returns `None`: no re-derive, `C06-ROLLING-RULE-UNREADABLE`, exactly
   today's behaviour (the fail-closed branch you already have).
2. **Say so in the half request** (Window and gap, Both branches): the rule's runtime source is the sibling file the runner's `sync_scripts`
   materializes with the gold scripts; if a later run ever lacks it the build is a no-op, never a typed 14.
3. The registry is NOT touched and no row is added there; your row S6 is dispositioned by this item. Rows S3 (the order's expected figure came
   from the CTO's text and does not match its inputs: state the move in the half request as `served minus rebuilt` per date from your record, and
   for 2026-10-09 against D_04's remainder, -$962,849.68; the key-based -$962,916.41 beside it), S4 and S5 are accepted as OBSERVATION.
4. **Then finish**: re-run AC1 to AC3 and the BD gold suite, validate the proof instance, flip the status to `complete` only when all three
   pass, and commit the build, the test, the half request, the proof instance and the order file (your `<paths>` plus those two). The two
   sibling tests that failed on a changed call text stay unedited: restore the call you changed, as you did.
5. **Gate limb.** The issuer amends its own criteria without a CTO ruling; no gate limb grades an amendment to an existing order's criteria and
   `<status>` (this order declares `<placeholders>NONE`). The three criteria are unchanged.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan, DynamoDB get_item): no write to any table or bucket, no deploy, no invoke, no model call. Never push.
  The deploy is NOT part of this cell; it is a later pair-gated act by a CloudOps lane.
- **Never edit** `lib/etf_classifier.py`, D_03, `.tools/`, the SC-e-91 retained pass, any test other than the new file, or B_00. The BD gold suite
  must stay green; run it once at the end and report the count.
- **Client data stays out.** Print no relationship id, account id or client name anywhere in the half request, the tests or the report.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W86-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken any test.

<paths>
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/tests/test_c06_rolling_rederive_r23.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R23.md</decomp_doc> (round 23), cell `SC-e-97`.
<owned_cells>SC-e-97</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC23-e97-AC1, SC23-e97-AC2, SC23-e97-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~86/MDPF_SECCLASS.TO-SC-e97.c06-rolling-rederive.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC23-e97-AC1,SC23-e97-AC2,SC23-e97-AC3`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, the cap decision from your record, the relationship JSON reads a
fire makes, the writer counts, the BD gold suite count, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the ship is a later pair-gated act by a CloudOps lane, outside a BD gold run; this cell ships no key.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only get_item and head-object under the seat's role).
comp-adversary: RUN -- a function-level test standing in for the served path (rounds 16, 20 and 21 each passed that way and the served bytes did not move at first; AC1 drives the module's own functions and AC2 reads the wiring of build() and D_04); a window typed as a literal 14 (AC2 refuses it); a pass that rewrites an unchanged relationship every fire (idempotence is in AC1 and the rewrite-only-on-change rule in item 2); a window date adjusted twice by the retained pass (item 3). BLIND: whether the runner can read the rule at build time (SC-e-96 verifies one source; the fail-closed branch makes an unreadable rule a no-op, so the ship cannot make today worse), and the chain's wall time on the first fire (the pair's runtime STOP rule watches it).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-22 analysis section 2 (ruling (a)) and section 3 item 1 (msg 4333); rows D1-W83-S5 and D1-W80-S4; SC-e-95's record; DECOMP_R23.
