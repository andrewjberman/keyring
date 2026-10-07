# AMGT_HARVST task order -- `HVST-bf-1` -- ROUND 59 (`1.0.0_SA_CTO~Z` rulings C2 @f97be3fd6f, msgs 31046, 31054; schema @25ebedb3a3): THE COLLECTOR WRITES ONE RECORD PER FINISHED SEEKING ALPHA JOB, BEHIND A SWITCH THAT IS OFF, AND CAN EMIT IT ONCE FOR JOBS ALREADY FINISHED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~108</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the collector runs on this device, no Lambda and no rule.
comp-iam: RUN at L5 -- YOU SEND NO PUT. The cell builds a writer that stays OFF (config switch false) and an emitter whose only mode you run is `--dry-run` (reads local run records and stored publication records; S3 HEAD/GET at most, to see whether an object already exists). The first real write is the ISSUER's act after the merge. No vendor or publisher host, no collector or backfill_driver run. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree; `.runtime` is READ ONLY at the paths named in section 0.
comp-adversary: RUN at L5 -- the adversary is a typed S3 address, a record keyed on the collector's key instead of the pool key, a record for a job that did not conclude or for another publisher, an overwritten object, a writer that is live the moment the branch merges, a newest-article time taken from the listing date or the publish date, or a dry run that puts.
</preflight>

## 0. THE CELL

The research app's freshness page shows, per company, when Seeking Alpha was last read. It read three names stale
("last read 2026-09-11") that the collector had read on 2026-10-06 and 10-07: the page reads a store these runs do not write.
The ruled repair is ONE small record per finished Seeking Alpha job, written by the collector (the one writer) and read by the
page (the one reader), to ONE contract:

**`lib/research/freshness/seeking_alpha_job_record.schema.json`** -- read it in full, including `x-address`,
`x-reader-rules` and `x-backfill`. It is the contract; you do not edit it. In short: `schema_version` 1; `security_key` = the
POOL key (`BA_US_Equity`, `BP/_LN_Equity`), never the collector's own key (`BA`, `security-85663a3912a0c415`);
`finished_at` and `newest_article_stored_at` as `YYYY-MM-DDTHH:MM:SSZ`; `status` = the job's concluded status word; `stored` =
how many articles THIS job stored; `newest_article_stored_at` = the STORE time of the newest article held for the security
when the job ended, from this job or any earlier one, or null; `run_id` optional.

**The address is never typed.** It is
`lib.research.harvest.store.address_of('seeking-alpha', 'state', 'job_record', store.entity_partition('security_key', <pool key>), object_name='<finished_at as YYYYMMDDTHHMMSSZ>.json')`,
which today prints, for example,
`s3://opal-data-harvest/seeking-alpha/harvest/state/job_record/security_key=BP-SLASH-_LN_Equity/20261007T013300Z.json`.
One object per finished job; an object is never overwritten.

What the collector has (all under `lib/opal_data_harvest/`):
- `worker.py`: a job ends in `run_job`; `_persist_run_record` (near line 948) writes the run record through the harvest
  client and records the event `run_record_persisted`. The run record carries `finished_at`, the job's `status`,
  `gold_security_key` (the POOL key), `counts` and `keys_stored_join` (the articles this job stored).
- `backfill_driver.py`: `CONCLUDED_STATUSES` (near line 51), the collector's declared list of concluded statuses.
- `lib.research.harvest.store` is already imported by `harvest_grammar.py` and others in this package.
- Local state per leg: `progress.sqlite3` (`articles`, `article_objects`, `jobs`, the outbox tables) and the stored
  publication records. Find where the collector records WHEN an article was stored, and name that field in your report.

Read-only inputs on disk for the dry run (absolute; NOT in your worktree):
- `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-sa/` (the Seeking Alpha leg: `run_records/*.json`,
  `progress.sqlite3`, stored records) and `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/` (the
  earlier shared root, which also holds Seeking Alpha jobs). Open sqlite read-only (`file:...?mode=ro`); a leg is writing it.
- Known from the issuer's read, to check your dry run against: `BABA_US_Equity` run `20261006T224539Z-run-5cf2aeea` stored
  616; `BA_US_Equity` run `20261007T002530Z-run-ecf26946` stored 1,992; `COST_US_Equity` run `20261007T111148Z-run-c2310424`
  stored 45; `C_US_Equity` run `20261007T124653Z-run-6b3d3a63` stored 9.

## 1. THE BUILD (class WORLD: it adds a stored record and a registry row; nothing is written to S3 by you)

1. **One module** `lib/opal_data_harvest/job_record.py`:
   - `build_record(...)` returns the dict to the schema, or None when the job is not a Seeking Alpha job or its status is not
     in `CONCLUDED_STATUSES` (one declared list: import it, do not copy it);
   - `address(record)` returns the builder call's output and nothing else;
   - `write(record, client)` puts ONE object, `application/json`, UTF-8, and REFUSES to overwrite (it checks the key first and
     returns `skipped_exists`);
   - every record is validated against the schema FILE before a put (read the file; no second copy of the shape).
2. **The switch.** `config.json` gains `"seeking_alpha_job_record": {"enabled": false}`. `worker.py` calls the writer at the
   end of a concluded Seeking Alpha job ONLY when the switch is true, after the run record is persisted, and records an event
   `job_record_persisted` (key, put_performed) or `job_record_skipped` (reason). A failure to write the job record never
   changes the job's status and never raises out of `run_job`: it is recorded as `job_record_failed` with the error. With the
   switch false the collector's behaviour is byte-for-byte today's.
3. **The one-time emitter** `lib/opal_data_harvest/emit_job_records.py`:
   `python -m lib.opal_data_harvest.emit_job_records --runtime-root <dir> [--runtime-root <dir> ...] --dry-run | --write`.
   It reads every run record under the roots, takes the Seeking Alpha jobs with a concluded status, builds ONE record per
   finished job with the SAME `build_record`, and:
   - `--dry-run` prints, and puts NOTHING: `RUN RECORDS READ <n>`, `SEEKING ALPHA JOBS <m>`, `CONCLUDED <c>` by status,
     `NOT CONCLUDED <k>` by status, `RECORDS PLANNED <r> over <s> securities`, `SCHEMA VALID <r> of <r>`, `ALREADY AT THE
     ADDRESS <e>` (a HEAD per key; if the HEAD is refused print the error and count it `UNKNOWN`, do not stop), one line per
     record `<security_key> <finished_at> <status> stored <n> newest <t> -> <address>`, and `PUTS SENT 0`;
   - `--write` exists and is covered by a test with a stub client; you do NOT run it against S3.
   - A job whose run record has no pool key is counted and named, never keyed on the collector's key.
4. **The registry row.** The new stored table needs its row under `infra/logic/registry/` in this same change (read the
   registry files and `infra/logic/02_DOCTRINE.md` for the row shape; the naming builder is `lib/opal_naming.py`). If the
   commit-time naming gate or the builder REFUSES, that is a missing registry row to add, never a typed workaround; if you
   cannot tell which row is missing, file a BLOCKING row with the refusal text and stop on AC2.
5. **Plants** in `lib/opal_data_harvest/test_bf1_job_record.py` (no network; a stub client):
   - (i) a concluded Seeking Alpha job gives a record that validates against the schema FILE, keyed on the pool key;
   - (ii) a Barron's job gives None; a Seeking Alpha job that ended `bot_check` gives None;
   - (iii) `BP/_LN_Equity` lands under `security_key=BP-SLASH-_LN_Equity`, and `address()` equals `store.address_of(...)`;
   - (iv) a second write to an existing key is `skipped_exists` and sends no put;
   - (v) switch false: `run_job` on a stubbed concluded job sends no job-record put and records no job-record event;
   - (vi) switch true: one put, one `job_record_persisted`; a client that raises on the put gives `job_record_failed` and the
     job's status is unchanged;
   - (vii) `newest_article_stored_at` is the newest STORE time across this job and earlier ones, and null when none is held;
   - (viii) the emitter over a fixture of run records plans one record per concluded Seeking Alpha job and `--dry-run` sends
     0 puts; `--write` on the stub sends exactly that many.
6. **The real dry run.** Run the emitter `--dry-run` over the two roots named in section 0 and write its whole output to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~108/bf1_emit_dryrun.out`. Its LAST line is
   `EMIT DRY RUN OK` only if ALL hold: RECORDS PLANNED > 0; every record schema-valid; the four known runs of section 0 are
   planned with stored 616, 1,992, 45 and 9; no two records share an address; PUTS SENT 0. Otherwise `EMIT DRY RUN FAIL` and
   the failing line.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/job_record.py
lib/opal_data_harvest/emit_job_records.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/config.json
lib/opal_data_harvest/build_release.py
lib/opal_data_harvest/test_*.py
infra/logic/registry/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~108/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You READ, and never write: the schema file, `lib/research/harvest/store.py`, `lib/opal_naming.py`, `backfill_driver.py`, and
the `.runtime` paths of section 0. Change an existing test assertion only where this cell's rule is the reason, and list each.
If `build_release.py` lists the package's files, add the two new modules there.

## 2. PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bf-1"><invocation>python -m pytest lib/opal_data_harvest/test_bf1_job_record.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bf-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~108/bf1_emit_dryrun.out</invocation><expect>EMIT DRY RUN OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bf-1"><invocation>python -m pytest lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py lib/opal_data_harvest/test_az1_alias_set.py lib/research/freshness/tests -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- Run `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider` once in the background to a file (it takes several
  minutes on this device) and report its count; the issuer re-runs it at the merge. It is not a criterion.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W108-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~108/AMGT_HARVST.TO-HVST-bf-1.seeking-alpha-job-record.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bf-1.seeking-alpha-job-record`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_AMGT_RESAPP_ROUND78_CALLS_AT_THE_CUT_20261007.md`
  @f97be3fd6f, ruling C2; `1.0.0_SA_CTO~Z` msgs 31046 and 31054 (the cell is SERVED; its registry row lands in the same
  commit; the newest article's time read from the stored publication records is accepted). Schema:
  `lib/research/freshness/seeking_alpha_job_record.schema.json` @25ebedb3a3 (`2.0.0_SA_COO~Z` msg 31059). Row
  AMGT_HARVST-Z-S100 @2a18cdc6d0. Decomposition section 73.
- **Class WORLD, not SERVED:** the L6 gate (GATE xii) refused `SERVED` at the cut because `<paths>` names
  `infra/logic/registry/`; the floor it infers is WORLD. `1.0.0_SA_CTO~Z` msg 31054 said SERVED; the gate's floor is the higher
  of the two and stands. A WORLD cell adds the CTO's exercised read and the change-management entry, both at the issuer's acts.
- **Why a switch:** the sa leg runs the collector from the shared tree, one process per job, so a writer merged live would
  start putting records the moment the branch lands. The switch keeps the merge inert; the ISSUER's acts after the merge
  are (1) read the dry run, (2) `--write` the one-time emit, (3) flip the switch, each recorded, with
  `1.0.0_SA_CTO~Z`'s exercised read as a SERVED cell requires. No served output moves: the reader (`AMGT-bb-16`) is not
  deployed, and by ruling C2 it deploys only with these records present.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected (no
  such file); AC3 base PASS as expected (32 passed).
- `AC3` names three test targets in one invocation (one clause, one expectation): the stopped-pair plants (they drive
  `run_job`'s status handling), the alias plants (they read `config.json`), and the freshness tests beside the schema.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>59</round>
<slot>~108</slot>
<fabric>site-z</fabric>
