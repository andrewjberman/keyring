# AMGT_HARVST task order -- `HVST-ba-1` -- ROUND 53 (round-49 analysis ADDENDUM 4; CTO @22b49f7b04; row Z-S94): A PAIR THAT STOPPED IS RETRIED, NOT DONE; ONE DEAD ARTICLE DOES NOT END A JOB

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ba-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~103</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants only. NO publisher host is contacted, no collector or backfill_driver is run against a real runtime root, no S3 call, and never touch any `.runtime` directory (four collection legs are live there). Every plant uses the test substitutes the existing driver tests use.
comp-adversary: RUN at L5 -- the adversary is a retry that loops without a bound, a stop-status pair still counted as collected in the summary, a summary whose four counts do not sum to the pair count, a 401/403 that no longer stops the job, or an old checkpoint whose stop-status rows stay "done".
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/backfill_driver.py` drives one (publisher, name) job at a time and checkpoints after each.
- `drive()` (around line 314) does `checkpoint["done"].append([pub, key, status, run_id])` for EVERY job, whatever its
  status.
- `plan_pairs()` (line 117-125) skips every pair in `done`.
- So the pair a leg STOPPED on (status in `STOP_STATUSES`: `bot_check`, `unclassified`,
  `account_or_harvester_unavailable`, `sign_in_refused`, `throttled`, `upstream_unavailable`, `cooldown`, `error`,
  `upload_timeout`) is "done", and `--clear-stop` resumes at the pair AFTER it. Measured over the four live checkpoints
  (row AMGT_HARVST-Z-S94): 37 pairs ended on a stop status and were never retried (wsj 8, bbg 8, barrons 12, sa 9).
- `build_summary()` (line 346-360) reports `pairs_done` over `done`, so those 37 count as done.

`lib/opal_data_harvest/transport.py` `PacedSession._resolve` (line 477-502): 401/403 raise `RequestRejected`; 404, 410 and
5xx raise `UpstreamUnavailable(status)`; any other 4xx falls to `response.raise_for_status()`, a bare `RuntimeError`, which the
collector records as the JOB's `status: error` (`lib/opal_data_harvest/worker.py:770-772`). Measured: one barrons article URL
answering HTTP 400 ended two whole jobs (NKE US, BABA US), each of which had other candidates.

Statuses observed in the run records that are a CONCLUSION (the job ran to its end): `new_articles`, `no_new_articles`,
`no_acceptable_new_articles`, `listing_empty_200`, `soft_block`, `complete_candidates`, `candidate_set_unselective`.

## 1. THE BUILD (LOCAL)

1. **Done only on a conclusion** (`backfill_driver.py`). Declare ONE frozenset `CONCLUDED_STATUSES` with exactly the seven
   statuses above. A job whose status is in it is appended to `checkpoint["done"]` as today. Any other status (a stop status,
   or a status the set does not name) is NOT done: it goes to `checkpoint["retry"]`, a dict keyed `"<pub>|<key>"` holding
   `{"attempts": n, "last_status": s, "last_run_id": r, "at": iso}`.
2. **The bound.** Module constant `MAX_PAIR_ATTEMPTS = 3`. A pair whose retry record reaches that many attempts moves to
   `checkpoint["gave_up"]` (same key) with `{"attempts", "reason": last_status, "last_run_id", "at"}` and is not planned
   again. `plan_pairs` plans every pair that is neither done nor gave_up; a pair with a retry record is planned again, in
   its universe order. The existing leg-level behaviour is unchanged: a stop status still stops the leg (or auto-resumes it
   when transient), and `--clear-stop` still clears it; what changes is that the stopped pair is planned again.
3. **Old checkpoints heal.** On load, a `done` row whose status is not in `CONCLUDED_STATUSES` is moved to `retry` with
   `attempts: 1` (its status and run id kept), so an existing checkpoint's stopped pairs are planned on the next invocation.
   The move is idempotent and recorded once in `checkpoint["migrated_stop_rows"]` (the count).
4. **The summary** (`build_summary`, and the printed text): per publisher `collected` (done), `retry`, `gave_up`,
   `never_started`, with `collected + retry + gave_up + never_started == pairs_planned`. Keep `pairs_done` as an alias of
   `collected` so existing readers still work. Print one line per publisher:
   `PAIRS <pub>: collected <a> retry <b> gave_up <c> never_started <d> of <n>`.
5. **One dead article is skipped** (`transport.py` and the article loops in `lib/opal_data_harvest/publishers.py`). An
   ARTICLE request answering 400, 404 or 410 is skipped: the loop records
   `{"event": "article_skipped", "publisher", "path", "status"}`, counts it on the client, and goes on to the next candidate.
   401/403 still stop the job exactly as today, and a 5xx keeps today's behaviour. A LISTING or account request answering
   400 keeps today's behaviour (only article fetches are skipped). The wsj sitemap loop already continues on 404/410
   (`article_endpoint_unavailable`); give 400 the same treatment there and make the other article loops (dow_jones search,
   bloomberg, bloomberg sitemap, seeking_alpha, financial_times) do the same.
6. **Plants** in `lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py` (no network; reuse the driver tests' substitute
   collector):
   - (i) a run of three pairs where the second ends `bot_check`: `done` holds the first only, `retry` holds the second with
     `attempts: 1`, the leg stopped; a second invocation with the stop cleared runs the SECOND pair first, then the third;
   - (ii) a pair that ends on a stop status `MAX_PAIR_ATTEMPTS` times moves to `gave_up` with its reason and is not planned
     again;
   - (iii) the control: a pair that concluded (`no_new_articles`) is done and never re-run;
   - (iv) an old-shape checkpoint whose `done` holds one `error` row and one `new_articles` row loads with the `error` row
     in `retry` and the other in `done`; loading it twice changes nothing more;
   - (v) the summary's four counts sum to the pair count in (i), (ii) and (iv);
   - (vi) a job with three article candidates where the second answers 400: the first and third are yielded, one
     `article_skipped` event carries status 400, and the job does not end `error`; the same job with a 403 on the second
     still stops;
   - (vii) the mutant: appending every status to `done` (today's line) makes (i) fail.
7. **Existing tests** that pin today's behaviour (every status in `done`; `pairs_done` counting stop rows; a 400 ending the
   job) may be updated for that reason only; list each file and assertion in your report.
8. The harvest suite stays green: `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider`. Report the count.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py
lib/opal_data_harvest/test_ae4_backfill_driver.py
lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py
lib/opal_data_harvest/test_af4_sitemap_listing.py
lib/opal_data_harvest/test_af4_discovery_hookup.py
lib/opal_data_harvest/test_q6_barrons_guard_ft_body.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~103/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ba-1"><invocation>python -m pytest lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ba-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W103-S<k>`.
- If an existing test outside `<paths>` pins today's behaviour and fails, do not edit it: file a BLOCKING row naming the
  file and assertion, and report.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~103/AMGT_HARVST.TO-HVST-ba-1.stopped-pair-is-retried.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ba-1.stopped-pair-is-retried`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Round-49 analysis ADDENDUM 4 @22b49f7b04; decomposition section 67; row AMGT_HARVST-Z-S94 @5d5daf8c2f; the 37 pairs are
  listed in `deliverables/2.0.0_SA_COO_H/round52/stop_status_pairs.json`.
- Item 3 of the build (old checkpoints heal on load) is the issuer's addition to ADDENDUM 4's four items: it makes the 37
  legacy pairs re-run at each leg's next invocation with no separate `--names` run. No gate limb graded it.
- A running driver process holds the OLD driver code until it exits; the collector half (the article skip) is picked up at
  each job. So the close run is: after the merge, each leg's NEXT invocation loads its checkpoint, migrates its stop rows,
  and plans them; the issuer reads the `PAIRS` lines and the 37 against `stop_status_pairs.json`.
- The alias cell (ADDENDUM 3 item 2, section 66) moves to round 54.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>53</round>
<slot>~103</slot>
<fabric>site-z</fabric>
