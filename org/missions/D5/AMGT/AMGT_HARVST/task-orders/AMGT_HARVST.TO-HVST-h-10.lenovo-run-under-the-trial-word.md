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
- **NEVER RUN AN INSTALL.**
- **PHASE 0 EDITS CODE; PHASE 1 DOES NOT.** See THE TWO PHASES below. Outside Phase 0's three named files, a defect
  found is a row, never a patch.

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
- You make exactly ONE live harvester run IN PHASE 1: one `run` invocation covering all five publishers, under the
  grant quoted below. **Phase 0 makes NO network call at all.**
- **If a publisher fails inside it** (logged out, challenged, throttled, rejected), that publisher is recorded UNRESOLVED
  with the run's own status. **You do NOT run it again.** Re-spending the word is Andrew's call.
- **If the invocation itself crashes before any vendor call,** re-invoking is allowed. Prove "before any vendor call"
  from the run's event ledger (zero `http` events).
- The second run in item 7 is NOT a vendor run: it runs with the network REFUSED.

**THE SESSION STATE, MEASURED BY THE ISSUER WITHOUT ANY NETWORK CALL (2026-09-22 ~19:2xZ):** every session artifact in
the desktop runtime is dated **2026-09-15**, about **7.6 days** old (23 files; newest `barrons-challenge-url.dpapi` at
04:58Z, the `auth/` dir holding three 2026-09-15 envelopes). A publisher may therefore be logged out.
- **That changes nothing about the one-run rule.** A logged-out publisher is recorded UNRESOLVED with the run's own
  status and is NOT retried.
- **Record each publisher's auth verdict in `first_run.summary.json` BEFORE any listing or article call**, as
  `auth_verdicts`, so a wasted leg is legible and Andrew can decide whether to re-spend.
- Do NOT attempt a browser sign-in, a session repair or a credential entry. That is an operator act, not yours.

**THE GRANT THIS ORDER NOW RUNS UNDER** -- `1.0.0_SA_CTO~Z` msg 24390, records @`c5f33fe8a3`, carrying Andrew's word
**"granted"** for a second Lenovo publications run, under his session grant, VERBATIM: *"you have egress as needed for
the duration of this session, furthermore you have adjudication ability for any and all open calls you encounter for
the duration of this session as it pertains to AMGT projects."*
- **The granted bound, verbatim from that message:** *"one further publications run for `992_HK_Equity` covering
  Bloomberg.com, FT, WSJ, Barron's, plus a Seeking Alpha pass that persists the received bytes."*
- **It is conditioned on ONE thing, and that condition is physics, not permission:** *"fix and VERIFY the CLI harvest
  wiring first ... A run fired before that lands nothing, which is exactly what the first one did."*
- **The quota word is UNREPEALED** (Andrew ~13:0xZ, *"we want to be sensitive about our data quota"*): this act prints
  its SIZING BEFORE it fires and its SPEND AFTER.
- **The first attempt is on the record:** its SA leg fetched 21 Lenovo articles, 6 rejected, 31 http events, and
  NOTHING reached bronze or silver because harvest mode never engaged. Those 21 exist as normalised records with no
  as-received bytes, so FWD-1's byte-for-byte bar needs THIS pass's SA leg to persist bytes.

**THE TWO PHASES, AND THE ISSUER CHECKPOINT BETWEEN THEM:**
- **PHASE 0 -- CODE, NO NETWORK.** Fix the CLI harvest wiring (row `AMGT_HARVST-Z-W10-S2`): `__main__.py` must build
  and pass a `harvest_client` so `Worker`'s harvest path is reachable, and `--harvest-grammar` must actually turn it
  on. Measured at HEAD: `harvest_client` appears 9 times in `worker.py` and **0** times in `__main__.py`.
  - Also fix row `AMGT_HARVST-Z-W10-S1`: `--bbg-symbol-probe` must run INSIDE a five-publisher run, not instead of it.
  - Add the two arms AC7 names to `lib/opal_data_harvest/test_retrieval_provenance.py`.
  - **You may edit ONLY these three files:** `lib/opal_data_harvest/__main__.py`, `lib/opal_data_harvest/worker.py`,
    `lib/opal_data_harvest/test_retrieval_provenance.py`.
- **THE ISSUER CHECKPOINT.** When AC7 and AC8 pass, **COMMIT, then STOP and REPORT. Do NOT fire the run.**
  `2.0.0_SA_COO~Y` verifies the wiring on its own instruments and continues you for Phase 1. **Firing Phase 1 before
  that continuation violates this order**, because a build defect would waste a granted word a second time.
- **PHASE 0b -- THE REHEARSAL, CODE AND NO NETWORK** (added after the SECOND granted act was spent and landed
  nothing; granted conditional by `1.0.0_SA_CTO~Z` @`e78837e32e`).
  - **What went wrong, and it was the issuer's specification, not either worker's build:** Phase 0 made the bbg probe
    fall through into `Worker.run()` on its SUCCESS path. A probe FAILURE still propagated, so the real
    `transport.VerificationRequired` from `www.bloomberg.com` crashed the handler before `Worker.run()`, and sa, ft,
    wsj and barrons were never attempted. Row `AMGT_HARVST-Z-W10-S4`.
  - **THE CONTRACT ALREADY ANSWERED IT** (PRD s.3): the probe is *"adopted or recorded UNRESOLVED with its reason"*.
    **A probe failure is a RESULT, never an abort.**
  - **BUILD, in `__main__.py` (and `worker.py` only if the handler needs it):**
    - The probe's exception is CAUGHT. The publisher is recorded `UNRESOLVED-CHALLENGED` with its reason, and the run
      CONTINUES into `Worker.run()` for all five publishers.
    - **The same rule binds every publisher, not just the probe:** a challenged, logged-out, throttled or rejected
      publisher is a RECORDED OUTCOME and the run continues to the others. **It must never again die on the second
      publisher.** `1.0.0_SA_CTO~Z` requires this stated in the criteria rather than left to inference, because the
      rehearsal proves the HANDLER and cannot prove the SESSIONS: they are 7.6 days old, ONE of five has now
      demonstrably challenged, and the other four are UNMEASURED. The third act is worth firing even if more
      publishers challenge -- so long as each one is recorded and the run carries on.
  - **BUILD, the rehearsal harness** at `lib/opal_data_harvest/rehearse_run.py` plus its arms in
    `lib/opal_data_harvest/test_retrieval_provenance.py`. It drives the WHOLE handler with:
    - all five publishers and harvest mode ON;
    - an INJECTED probe failure of the EXACT exception class the live run raised (`transport.VerificationRequired`);
    - **the network POISONED at the real call sites** (`PacedSession.get`, `SessionManager.refresh`,
      `subprocess.run`), each raising loudly;
    - writes directed to an ISOLATED prefix or a stub store, never a live harvest prefix.
  - **NAME THE POISON, NEVER THE ABSENCE OF PERMISSION.** A no-network phase that PASSES is evidence only if the
    run COULD NOT have reached the network (`3.0.0_SA_CVO~Z`'s sharpening of @`3251308f2e`, which the CTO adopted).
    So the rehearsal carries its own POSITIVE CONTROL: a deliberate call attempt must RAISE, printed beside the
    result. A rehearsal with no positive control proves nothing.
  - **The rehearsal must prove the three things two spent acts never proved:** the handler REACHES `Worker.run()`
    after a probe failure; EVERY publisher job starts; and the harvest write path produces **bronze AND silver** rows.
  - **You may edit ONLY:** `lib/opal_data_harvest/__main__.py`, `lib/opal_data_harvest/worker.py`,
    `lib/opal_data_harvest/rehearse_run.py`, `lib/opal_data_harvest/test_retrieval_provenance.py`.
- **THE SECOND ISSUER CHECKPOINT.** When AC9, AC10 and AC11 pass, **COMMIT, then STOP and REPORT. Do NOT fire the
  run.** `2.0.0_SA_COO~Y` verifies the rehearsal on its own instruments and shows its evidence to `1.0.0_SA_CTO~Z`
  before the third act fires.
- **PHASE 0c -- THE SILVER REBUILD, CODE AND NO VENDOR CALL** (added after the THIRD act landed bronze but not silver).
  - **What the third act achieved:** all five publishers reached `job_finished` under real adversarial conditions, and
    the issuer measured bronze 89 -> 103 (+14, re-read 14 of 14, mismatch 0), the first 2 bronze listings and the
    first `listing_hit` row ever landed. **The Phase 0b fix is proven under fire.**
  - **What blocks AC2:** row `AMGT_HARVST-Z-W10-S8`. `silver_from_bronze`'s WSJ extractor pulls WSJ's entire
    `__NEXT_DATA__` frontend config (100+ non-article keys) into the silver row; one page held a string where its
    siblings held a boolean, so pyarrow's grouped-batch schema inference raised and ALL 11 new WSJ rows failed, twice.
  - **NO NEW VENDOR CALL IS NEEDED, AND NONE IS AUTHORISED HERE.** Bronze holds the received bytes and
    `C-HV-SILVER-FROM-BRONZE` makes silver replayable from them. The remaining work is entirely offline.
  - **THE ISSUER'S CONTRACT READING, which this phase builds to** (surfaced to `1.0.0_SA_CTO~Z`; if it rules
    otherwise, that ruling governs): `C-HV-SILVER-FROM-BRONZE` requires every vendor field KEPT with standard typing
    and nothing filtered or summarised. A frontend config blob whose sibling pages disagree on a key's type cannot be
    columnar-typed at all. So:
    - the ARTICLE-bearing fields stay typed exactly as they are today;
    - every remaining key of the page config is preserved VERBATIM in one JSON TEXT column;
    - **nothing is dropped, nothing is summarised**, and bronze remains the original either way.
  - **BUILD:**
    - fix the extractor in `lib/opal_data_harvest/silver_from_bronze.py` per that reading, for WSJ and for any other
      publisher whose page config can carry a mixed-type key;
    - add arms to `lib/opal_data_harvest/test_silver_from_bronze.py`, including a NO-KEY-LOSS arm: every top-level key
      present in a bronze fixture is recoverable from the silver row, counted, with the denominator printed;
    - and a REGRESSION arm reproducing the exact mixed-type conflict (a string where a sibling holds a boolean) and
      proving the grouped batch now writes;
    - then REBUILD silver from the ALREADY-HELD bronze for this run's articles, through the same uploader path, with
      no vendor call.
  - **You may edit ONLY:** `lib/opal_data_harvest/silver_from_bronze.py`,
    `lib/opal_data_harvest/test_silver_from_bronze.py`, and `lib/opal_data_harvest/uploads.py` if the rebuild needs a
    replay entry point.
  - **AC2 is then re-measured** on the rebuilt silver: `silver_article_rows` EQUAL to `bronze_articles`.
  - **AC3 stays as it is and may still FAIL honestly.** Its replay depends on what each publisher returned in the one
    run, and three of five had nothing replayable. Record it, do not chase it, and do NOT fire another run to move it.
- **PHASE 1 -- THE RUN.** Only on the issuer's continuation, then the acts below in order. **The third act's bound is
  the same as the second's** (bbg, ft, wsj, barrons, plus an SA pass that persists the received bytes), and the
  sizing goes on the record before it and the spend after it.

**THE ORDER OF ACTS (PHASE 1):**
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
- **Vendor egress ONLY in PHASE 1's item 4, ONCE, and only after the issuer continues you.** S3 only under
  `opal-data-harvest`, through the harvester's writers.
- **NEVER bound the live run with `timeout`.** The first attempt died exactly that way: a `timeout 590` killed a
  healthy SA job mid-flight and spent the word for nothing. The live run is NOT a bounded criterion invocation.
- **A refused S3 PUT is a BLOCKING row.** Never hand-type a key, and never use another bucket.
- **A publisher returning ZERO Lenovo articles is a RESULT, not a failure.** Record it with the stop reason.
- **Out of scope:** non-English press (the PRD's s.2). A Chinese-language result is recorded, never translated.
- **Surprise rows:** `AMGT_HARVST-Z-W10-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600 -- the live run is item 4 of section 1, NOT a criterion invocation)

Write `.scratch/hv10/ac8.py`. It reads `lib/opal_data_harvest/__main__.py` and `lib/opal_data_harvest/worker.py` as
text and prints `main_harvest_client <n>`, `worker_harvest_client <n>` and
`probe_returns_before_worker_run <bool>` (True only if the run handler's `bbg_symbol_probe` branch returns before it
calls `Worker.run`).

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
  <criterion id="AC6" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- lib org/tier1_exec && git status --porcelain -- lib org/tier1_exec && echo "--- end"</invocation><expect>before "--- end", ONLY the four files this order's phases authorise (lib/opal_data_harvest/__main__.py, lib/opal_data_harvest/worker.py, lib/opal_data_harvest/rehearse_run.py, lib/opal_data_harvest/test_retrieval_provenance.py), nothing else under lib, and nothing at all under org/tier1_exec -- corrected from "the three Phase 0 files", which Phase 0b's own amendment had already outgrown (row AMGT_HARVST-Z-W10-S7)</expect></criterion>
  <criterion id="AC7" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_retrieval_provenance.py -v --color=no -p no:cacheprovider 2>&1 | tail -20</invocation><expect>"15 passed" and no "failed" -- the thirteen arms already present plus test_cli_run_wires_harvest_client (the CLI run path supplies a non-None harvest_client when --harvest-grammar is passed, and None when it is not) and test_bbg_symbol_probe_runs_inside_a_five_publisher_run</expect></criterion>
  <criterion id="AC8" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv10/ac8.py</invocation><expect>"main_harvest_client" at least 1 (it was 0 at the first attempt), "worker_harvest_client" at least 9, and "probe_returns_before_worker_run False"</expect></criterion>
  <criterion id="AC9" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_retrieval_provenance.py -v --color=no -p no:cacheprovider 2>&1 | tail -24</invocation><expect>"18 passed" and no "failed" -- the fifteen arms already present plus test_probe_failure_is_recorded_not_raised, test_run_continues_to_every_publisher_after_a_probe_failure, and test_a_challenged_publisher_is_recorded_and_the_run_continues</expect></criterion>
  <criterion id="AC10" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest.rehearse_run</invocation><expect>"handler_reached_worker_run True", "publisher_jobs_started 5 of 5", "bronze_rows" at least 1, "silver_rows" at least 1, and "vendor_calls 0" -- the whole handler driven with an injected transport.VerificationRequired and the network poisoned at PacedSession.get, SessionManager.refresh and subprocess.run</expect></criterion>
  <criterion id="AC12" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_silver_from_bronze.py -v --color=no -p no:cacheprovider 2>&1 | tail -22</invocation><expect>"16 passed" and no "failed" -- the fourteen arms already present plus test_page_config_mixed_type_key_still_writes (the exact string-where-sibling-holds-boolean conflict) and test_no_key_loss_from_bronze_to_silver (every top-level bronze key recoverable, denominator printed)</expect></criterion>
  <criterion id="AC11" cell_refs="HVST-h-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest.rehearse_run --positive-control</invocation><expect>"poison_positive_control RAISED" on every one of the three poisoned call sites (PacedSession.get, SessionManager.refresh, subprocess.run) -- the rehearsal's PASS means the run could not have reached the network, not merely that it did not</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.**
- **AC5 is a JUDGMENT criterion** (graded by `3.0.0_SA_CVO~Z` at L9, never by you). Its question: does `RUN_REPORT.md`
  show that every article from each publisher, and the listing page that found it, is re-openable from the store and
  matches what was received, with every UNRESOLVED publisher carrying its reason?
- Record AC5 as `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.
- `first_run.summary.json` and `second_run.summary.json` are files YOU write from the run records, each carrying the
  fields AC3 and AC4 read. `first_run.summary.json` also carries `auth_verdicts`, one entry per publisher, written
  before any listing or article call.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/AMGT_HARVST.TO-HVST-h-10.lenovo-run-under-the-trial-word.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8,AC9,AC10,AC11,AC12`, which must return
   rc 0. The id list names EVERY row the instance carries, the judgment row AC5 included: the checker's coverage
   frame refuses a list that omits a carried row (row `AMGT_HARVST-Z-W8-S2`).
   - **At the FIRST ISSUER CHECKPOINT** (end of Phase 0), write the instance with AC7 and AC8 recorded, grade
     `AC7,AC8` to rc 0, commit, and report.
   - **At the SECOND ISSUER CHECKPOINT** (end of Phase 0b), record AC9, AC10 and AC11, grade `AC9,AC10,AC11` to
     rc 0, commit, and report. The full grading above applies at the END of Phase 1.
3. Flip to `complete` only if every mechanical criterion (AC1, AC2, AC4, AC6, AC7, AC8, AC9, AC10, AC11, AC12) passes
   AND AC2 reads silver EQUAL to bronze on the rebuilt silver, and NEVER at a checkpoint. **AC3 is EXEMPTED from the
   flip condition by the issuer:** its replay depends on what the publishers returned in the one authorised run, three
   of five had nothing replayable, and no further run is authorised to move it. It is recorded with its reason and
   carried to the round-1 analysis, not chased.
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
