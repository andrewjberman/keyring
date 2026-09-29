# AMGT_HARVST task order -- `HVST-w-4` -- ROUND 12 chain 4 of 4: the ft/barrons DIAGNOSTIC, answered WITHOUT a vendor call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-w-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~38</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates; this cell reads and diagnoses, writes no data and arms nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on opal-data-harvest ft silver article parts and the newest article_security_mention gold snapshot. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a diagnosis that reports a double-count from the device-local sqlite rows when gold never reads them. AC1 follows the rows to the table gold actually reads.
</preflight>

## 0. THE STANDING CLAUSES

1. ⛔ **NO VENDOR CALL AND NO NETWORK OTHER THAN OPAL S3 READS.** Andrew's word (ruling 2, 18:05Z) PERMITS one
   bounded ft/barrons run; the measurement at the cut shows the question does not need one, so none is made. Every
   harvest-code invocation runs with `HARVEST_REFUSE_NETWORK=1` (`lib/opal_data_harvest/transport.py:11-15`).
2. **NO WRITE of any kind to S3, the runtime root or `lib/`.** A defect is a surprise ROW, never a fix here.
3. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~38/scripts/` -- **never `.scratch/`.**
4. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~38/AMGT_HARVST.TO-HVST-w-4.ft-barrons-diagnostic-without-a-vendor-call.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-w-4.ft-barrons-diagnostic-without-a-vendor-call`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~38/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

Read-only, never write: the MAIN tree's runtime root
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/` (`progress.sqlite3`: open it READ-ONLY with
a `file:...?mode=ro` URI). A linked worktree has no `.runtime`.

## 1. THE TWO QUESTIONS

**(ft) row `AMGT_HARVST-Z-S31`:** ft holds 15 rows under 14 distinct `article_id`s; does any GOLD count double-count
it? **Measured at the cut, and your starting point, not your conclusion:** `articles` in `progress.sqlite3` has
`PRIMARY KEY(publisher, security_key, article_id)` (`lib/opal_data_harvest/worker.py:32-33`), so the row's "no unique
constraint" premise is false; the one duplicate id `79c86a189372f457e82c5969` is held under `COST` and `HD` with the
same body sha256 -- one story naming two securities. Gold reads SILVER `article` collapsed to one row per
`article_key` (`lib/research/harvest/publication_gold.py:714-718`), assigns securities by text match
(`mention_rows` `:223-270`), never from the sqlite `security_key`, and `articles_total` counts a SET of article_keys
(`:584`, `:621`). **The one thing not yet measured is on S3:** whether ft silver holds that article under ONE
`article_key` or two. Andrew (quoted in `Z-S31`): "im not perturbed by the FT duplicate either".

**(barrons) the quarantined test:** `lib/opal_data_harvest/test_verification.py:11-18` is `@unittest.skip` for a
flaky barrons verification repair (`ledger/ROUND_ANALYSIS.round8.md:42-44`). A stray `unused/` directory sits at the
repo root, consistent with `repair()` reaching `folder.mkdir` at `lib/opal_data_harvest/verification.py:72` with an
unset folder. Diagnose the flake's ROOT CAUSE locally; do not un-skip or change the test.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). TWO mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-w-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~38/scripts/ac1_ft_duplicate_reaches_gold.py</invocation><expect>FOLLOW THE DUPLICATE TO THE TABLE GOLD READS: print the sqlite rows for ft article_id 79c86a189372f457e82c5969 (read-only), then how many ft SILVER article rows and distinct article_keys carry that article (read from S3, denominator = ft silver rows scanned), then every newest article_security_mention gold row for it (article_key, security_key) and the articles_total contribution per security. Verdict line: "gold double-counts: YES/NO" with the counts that decide it. If silver holds the article under TWO article_keys, that is the finding and is filed as a row</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-w-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~38/scripts/ac2_barrons_flake_root_cause.py</invocation><expect>THE QUARANTINED BARRONS TEST'S ROOT CAUSE, reproduced OFFLINE (HARVEST_REFUSE_NETWORK=1): run the skipped test's body in-process N times (N printed, at least 20), print the pass/fail split and the failure signature distribution, and name the file:line that decides the outcome; state whether the repo-root unused/ directory is produced by this path (reproduce it in a temp cwd, never in the repo). If it cannot be reproduced in N runs, say so with N, and name what differs from the environment in which it flaked</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No vendor call, no write anywhere but your deliverables and the channel, no test un-skipped, no producer change.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Narrowed from a vendor diagnostic to a no-vendor one, and the reason is a measurement, not a preference.** The
   round-11 analysis lists `w-4` as "one bounded run, same word". The fact sheet at the cut (sqlite PRAGMA, the
   gold reader's own collapse to article_key) answers the ft question up to ONE Opal S3 read, and the barrons half
   is a local test flake. Andrew's word is a PERMISSION; spending it where no vendor byte is needed would be an act
   with no question behind it. If AC1 or AC2 surfaces a question only a live call can answer, that is a row and a
   round-13 card.
2. **Risk LOCAL**: Opal S3 reads and in-process tests only. Its own chain (no vendor ledger, no session vault).
3. Base: both criteria FAIL at the base by construction (scripts absent); worker-written as in prior rounds.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>12</round>
<slot>~38</slot>
<fabric>site-z</fabric>
