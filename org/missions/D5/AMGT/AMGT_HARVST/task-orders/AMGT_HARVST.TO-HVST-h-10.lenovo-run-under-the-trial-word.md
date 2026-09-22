# AMGT_HARVST task order -- `HVST-h-10` -- H10: the ONE harvester run for Lenovo (`992_HK_Equity`) under Andrew's trial word -- all five publishers, backfill from 2026-01-01, plan printed first, Bloomberg's per-symbol call tried once; then bronze re-read byte for byte, silver from bronze, and a second same-day run with the network REFUSED; VENDOR EGRESS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~10</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); the run writes S3 objects, which is not a deploy, and arms nothing.
comp-iam: RUN at L5 on the DESIRED plane only; this box's S3 credential for opal-data-harvest bronze and silver is measured by the run's own conditional PUTs, and a refusal is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~10`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, and `lib/opal_data_harvest/test_retrieval_provenance.py` exist.
  - That last file is the predecessor's. If it is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~10;`.
- **NEVER RUN AN INSTALL. NEVER EDIT CODE IN THIS CELL.** It runs what `HVST-h-1`, `HVST-h-2`, `HVST-h-9` and `HVST-h-3`
  built, and a defect found in it is a row, never a patch.

## 1. THE CELL, inlined in full -- `HVST-h-10` (manifest row H10; outcomes FWD-1, FWD-2, FWD-3, and FWD-9 for Lenovo)

**THE WORD YOU RUN UNDER -- ANDREW-DIRECT 2026-09-22 ~13:5xZ, VERBATIM:** *"Let's try one sample first, let's run Lenovo
through the entire pipeline. Let's do every single thing for Lenovo and use that as the trial."*
- Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_135xZ_AMGT_LENOVO_SINGLE_SAMPLE_FULL_PIPELINE_TRIAL.md`.
- Its cap for this channel: **"Publications harvester: 1 run for Lenovo."**
- And: *"A channel whose cost is not knowable in advance runs only with its cost printed first."*
- The same record says the backfill holds are **"MET FOR LENOVO ONLY by this word"**.

**The contracts** (PRD v0.2 @9102ccfe81):
- `C-HV-EGRESS`: *"The validation security is Lenovo (`992_HK_Equity`), under his trial word (one run per publisher) ...
  with the listing page count per publisher printed BEFORE the run."*
- `C-HV-BOUNDARY`: *"The trial's one publications pass (its stage 9) is EXECUTED by this project's harvester ... so
  there is ONE pass, not two."*
- PRD s.3: Bloomberg's per-symbol `news()` is *"tried once in the validation run, inside the cap. It is adopted or
  recorded UNRESOLVED with its reason."*

**THE ONE-RUN RULE, which binds every step below:**
- You make exactly ONE live harvester run: one `run` invocation covering all five publishers.
- **If a publisher fails inside it** (logged out, challenged, throttled, rejected), that publisher is recorded UNRESOLVED
  with the run's own status. **You do NOT run it again.** Re-spending the word is Andrew's call.
- **If the invocation itself crashes before any vendor call,** re-invoking is allowed. Prove "before any vendor call"
  from the run's event ledger (zero `http` events).
- The second run in item 7 is NOT a vendor run: it runs with the network REFUSED.

**THE ORDER OF ACTS:**
1. **Resolve Lenovo.**
   - Look for `992_HK_Equity` in the universe file named by `config.json` `universe_source`. If it is present, use
     that record.
   - Otherwise write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/lenovo.security.json`
     as `{"key": "992_HK_Equity", "ticker": "992_HK_Equity", "company": "Lenovo Group", "aliases": ["Lenovo"], "sa_symbol": "LNVGY"}`.
     `LNVGY` is Lenovo's US ADR line, the only SA line the trial word admits.
   - Record which source you used.
2. **Resolve the runtime.** It is the MAIN workspace's `.runtime/opal-data-harvest`, which holds the signed-in publisher
   sessions. Derive it with `git worktree list --porcelain | head -1`, and never type a drive path. Pass it as
   `--runtime-root`.
3. **Print the plan BEFORE any vendor call.** Run `plan` with `--with-watermark`, which reads S3 only. Save it to
   `plan.json` in your deliverables folder. It prints each publisher's `planned_listing_pages`.
4. **The ONE run.** Use harvest mode, `--retrieval-mode backfill --floor 2026-01-01`, all five publishers, and
   `--bbg-symbol-probe`. Take the exact flags from `HVST-h-3`'s report, or from `python -m lib.opal_data_harvest run -h`
   at your HEAD. Save stdout, the job result files the run writes, and the event ledger lines of this run to your
   deliverables folder.
5. **Upload.** Run `upload-harvest --retrieval-mode backfill` until `remaining_pending` is 0. It writes bronze articles,
   bronze listings, silver `article` and silver `listing_hit`.
6. **Verify:**
   - (a) EVERY bronze key this run put is re-read from S3 with `get_object`, and its sha256 compared with the sha256 the
     capture recorded locally (the outbox rows).
   - (b) Silver `article` rows for this run's article keys are read back, and the count compared with the bronze
     article count.
   - (c) The planned against actual listing pages per publisher.
7. **The second same-day run, network REFUSED.** Repeat item 4's command with `HARVEST_REFUSE_NETWORK=1`, on the SAME
   UTC date as item 4. It must complete with zero `http` events and zero `network refused` hits. Every page and article
   it needs is held, so it replays from bronze. If the UTC date rolled over between items 4 and 7, record that and file
   a BLOCKING row; do NOT make another live run.
8. **Write `RUN_REPORT.md`** in your deliverables folder, containing:
   - per publisher: its status, `planned_listing_pages`, actual pages, its stop reason, articles accepted, articles
     rejected by the mention floor, and bronze or silver counts;
   - Bloomberg's probe result, with its verdict ADOPTED or UNRESOLVED and the reason;
   - the silver prefixes written;
   - the one line `AMGT_RESAPP` stage 9 reads: *"stage 9 publications for 992_HK_Equity: <N> articles in silver, run <stamp>"*.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 5 of 9. After `HVST-h-3`. The gold cells (`HVST-h-4`,
`HVST-h-5`, `HVST-h-6`) build on the silver you land. Gold is rebuildable from silver, so no second vendor pass is ever
needed. The issuer tells `AMGT_RESAPP`'s driver when you drain.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/
lib/research/harvest/store.py
org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/ft_rest_fetch.py
org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_135xZ_AMGT_LENOVO_SINGLE_SAMPLE_FULL_PIPELINE_TRIAL.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-10.lenovo-run-under-the-trial-word.md
</paths>

- **Everything under `lib/` and `org/tier1_exec/` is READ-ONLY for you.** AC6 fails if any of it changes.
- Your deliverables folder takes every artifact. **NEVER write a cookie, a session value, a credential or a request
  header into any file.** The run's own ledger already omits them.
- Scratch goes in `<your worktree>/.scratch/hv10/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~10 <0.9.0_WK_AMGT_HARVST~10@opal.agent>" -F <msgfile> -- <paths>`.
  Commit only files in your deliverables folder, the channel and this order.

## 4. BOUNDS
- **Vendor egress ONLY in item 4, ONCE.** S3 only under `opal-data-harvest`, through the harvester's writers.
- **A refused S3 PUT is a BLOCKING row.** Never hand-type a key, and never use another bucket.
- **A publisher returning ZERO Lenovo articles is a RESULT, not a failure.** Record it with the stop reason.
- **Out of scope:** non-English press (the PRD's s.2). A Chinese-language result is recorded, never translated.
- **Surprise rows:** `AMGT_HARVST-Z-W10-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600 -- the live run is item 4 of section 1, NOT a criterion invocation)

Write `.scratch/hv10/verify.py`. It reads your deliverables folder's run records and the outbox rows of THIS run from the
main runtime's `progress.sqlite3`, opened read-only. It then prints:
- `bronze_reread <match> of <n> mismatch <m>` (every bronze key this run put, articles and listings, get_object sha256
  against the recorded sha256);
- `silver_article_rows <s> bronze_articles <a>`;
- one `publisher <code> status <s> planned <p> actual <q> stop <reason>` line per publisher.

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import json;d=[json.loads(l) for l in open('org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/plan.json',encoding='utf-8') if l.strip()];print('plan_lines',len(d));print(sorted(x.get('publisher','TOTAL') for x in d))"</invocation><expect>"plan_lines 6", and a sorted list naming barrons, bbg, ft, sa and wsj plus the total line -- the plan was saved (section 1 item 3 requires it BEFORE the run; AC5's reviewer reads its timestamp against the run's first http event)</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv10/verify.py</invocation><expect>"bronze_reread N of N mismatch 0" with N at least 1; "silver_article_rows" EQUAL to "bronze_articles"; five publisher lines, each with a status and a stop reason</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import json;r=json.load(open('org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/second_run.summary.json',encoding='utf-8'));print('same_utc_date',r['same_utc_date'],'http_events',r['http_events'],'network_refused_hits',r['network_refused_hits'],'status',r['status'])"</invocation><expect>"same_utc_date True http_events 0 network_refused_hits 0" -- the second same-day run fetched nothing we hold (FWD-3), proven with the network refused</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import json;r=json.load(open('org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/first_run.summary.json',encoding='utf-8'));print('live_run_invocations',r['live_run_invocations'],'bbg_symbol_probe',r['bbg_symbol_probe_verdict'])"</invocation><expect>"live_run_invocations 1" and bbg_symbol_probe either ADOPTED or UNRESOLVED -- the word spent exactly once and the probe tried once</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-h-10" judgment="true"/>
  <criterion id="AC6" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && git status --porcelain -- lib org/tier1_exec && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- lib org/tier1_exec && echo "--- end"</invocation><expect>NOTHING printed before "--- end" -- no code or CRO script was touched in the working tree or committed on this branch since it forked from SITEZ</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.**
- **AC5 is a JUDGMENT criterion** (graded by `3.0.0_SA_CVO~Z` at L9, never by you). Its question: does `RUN_REPORT.md`
  show that every article from each publisher, and the listing page that found it, is re-openable from the store and
  matches what was received, with every UNRESOLVED publisher carrying its reason?
- Record AC5 as `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.
- `first_run.summary.json` and `second_run.summary.json` are files YOU write from the run records, each carrying the
  fields AC3 and AC4 read.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/AMGT_HARVST.TO-HVST-h-10.lenovo-run-under-the-trial-word.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6`, which must return rc 0. The id
   list names EVERY row the instance carries, the judgment row AC5 included: the checker's coverage frame refuses a list
   that omits a carried row (row `AMGT_HARVST-Z-W8-S2`).
3. Flip to `complete` only if every mechanical criterion (AC1, AC2, AC3, AC4, AC6) passes.
4. Commit with `--only`.
5. Report once, with the `RUN_REPORT.md` stage-9 line verbatim.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The word.** The trial record (`1.0.0_SA_CTO~Z`'s narrow reading, stated as such) caps this channel at "1 run for
   Lenovo". The PRD's "one run per publisher" is the same act, because one `run` covers five publishers.
2. **Why the backfill rides this run.** The same record meets the backfill holds for Lenovo, and the contract's paging
   bound is the floor. So the validation run and Lenovo's 2026 backfill are ONE vendor pass.
3. **The worker is the actor on the vendor call. The spawn is the GO.** No broker message carries it.
4. **On drain, the issuer:**
   - tells `2.0.0_SA_COO~Z` (`AMGT_RESAPP`), by file and message, that stage 9 has landed (the RUN_REPORT line and the
     silver prefixes);
   - relays any UNRESOLVED publisher to `1.0.0_SA_CTO~Z` for Andrew, if a re-spend is wanted.

<status>pending</status>
<round>1</round>
<slot>~10</slot>
<fabric>site-z</fabric>
