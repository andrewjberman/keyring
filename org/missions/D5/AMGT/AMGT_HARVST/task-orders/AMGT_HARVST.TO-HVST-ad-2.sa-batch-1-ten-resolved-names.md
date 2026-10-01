# AMGT_HARVST task order -- `HVST-ad-2` -- ROUND 31 chain 2: SEEKING ALPHA BATCH 1 -- 10 RESOLVED `sa_symbol` NAMES, MEASURED-FIRST, STOP AT THE FIRST CHALLENGE, NEVER A SIGN-IN, UNDER A PAIR (FWD-7, FWD-9, FWD-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ad-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~88</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; one manual sa collection per name and one upload. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to Seeking Alpha ONLY, by the collector's own code (R-21 @b390c36444). NO request to bbg, wsj, barrons or ft (the playbook hard stop). S3 PUTs: the persisted run records, the upload's sa bronze and silver. NO sign-in, NO delete, NO gold write, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a job that signs in when a 401 or 402 answers (the crawl Andrew forbade), or a batch that keeps requesting after a challenge. AC1 requires 0 sign-ins across every run record and no request after the first stopping class.
</preflight>

## 0. THE ORDER OF ACTS

1. **PHASE A0 (LOCAL, no network), merged by the issuer:** the collector's `run` gains `--no-sign-in`.
   - With it, `TokenFirstSessions.refresh` (and every sign-in path) refuses. The job ends status `sign_in_refused` with its
     attempt rows. No sign-in, no browser, no credential read.
   - A 402 under `--no-sign-in` gets NO fresh-session retry (`ab-3` A0 is off in that mode) and ends
     `account_or_harvester_unavailable`.
   - Paths: `lib/opal_data_harvest/__main__.py`, `lib/opal_data_harvest/sessions.py`, `lib/opal_data_harvest/worker.py`,
     `lib/opal_data_harvest/test_ad2_no_sign_in.py`.
2. **BOTH never-widen halves are COMMITTED** on the merged code:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round31/NEVER_WIDEN_HALF_COO_AD2.md`;
   - `1.0.0_SA_CTO~Z`'s half.
3. **PHASE A (WORLD), the act, inside the halves.**

## 1. THE ACT (each command that reaches a put is named in the halves)

**The 10 names** are the first 10 rows of the collector's resolved universe (`universe(config)`, in order), each with a
`sa_symbol`: ASML, Adobe, Air Liquide, Alibaba, America Movil, AstraZeneca, BB Seguridade, BNP Paribas, BP, Boeing. Each
security file is that universe row, verbatim.

1. **The pre-run print,** with no request: the collector's `plan` per name for `sa`, floor `2026-01-01`, with the watermark.
2. **Collection, ONE invocation per name, in order:** `run --harvest-grammar --retrieval-mode backfill --floor 2026-01-01
   --new-only --no-sign-in --security-json <name> --publishers sa --max-jobs 1`.
   - **STOP the batch** (no further invocation) at the first job whose status is `bot_check`, `unclassified`,
     `account_or_harvester_unavailable` (a 402), `sign_in_refused` or `throttled`.
   - **Finish before 08:00Z 2026-10-01.** The playbook's first light is 09:00Z, and this box sends nothing to anyone in the
     hour before it.
3. **Upload, ONCE,** capped at the printed pending count.
4. **Run AC1 and AC2.**

## 2. SURFACES

<paths>
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/sessions.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_ad2_no_sign_in.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~88/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ad-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round31/checks/ad-2.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ad-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round31/checks/ad-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round30.md` @`6adebef352` section 4 item 2, ruling 1.
- **Measured at the cut** (ruling 4): the collector's resolved universe holds 89 rows, all with `sa_symbol`; the first 10 are
  listed above. Several have no `ticker`, so selection is by security file, one invocation per name (the `ab-3` finding).
- **Why phase A0:** inside the Worker, a 401 means a sign-in (`ab-1` A2), and a 402 means a fresh-session sign-in (`ab-3` A0).
  Ruling 1 says the batch stops at a 402 and never signs in. There is no CLI switch (measured: none in `__main__.py`).
- **The positive arm** (the analysis's "serializing dry run's put count per name") is shown in the COO half at signing, on the
  merged A0 code. Stub evidence covers the per-invocation run-record put and the upload's per-article puts.
- **The checks and halves are issuer-written after A0 merges.** AC1 covers: 0 sign-ins; no job after the first stop; writes
  only on the sa root plus the run records; the outbox empty after upload. AC2 prints the measured pages per name and the
  re-based sa ceiling for the other 79 names.

**AMENDMENT 1 (issuer, 2026-09-30 ~23:5xZ) -- rows `Z-W88-S1` and `Z-W88-S2`: re-run the 9 names that made NO request, in universe order, with two added STOP statuses. Under a RE-SIGNED pair.**
- **What ran** (the record is in `~88/`):
  - BA ran FIRST, because the issuer's plan file was dumped with sorted keys (`ad2_common.dump` `sort_keys=True`) and the
    worker ran in key order. That is an issuer defect (`Z-W88-S1`).
  - BA took 1 listing page OK (span 2026-09-21..09-30). Its one article answered 502, so the job ended `upstream_unavailable`
    and set a 15-minute sa cooldown.
  - The other 9 invocations ended `cooldown` with **0 requests**, because `cooldown` and `upstream_unavailable` were not STOP
    statuses (`Z-W88-S2`).
  - 0 names were reached; nothing was measured.
- **The re-run (phase A2), ONLY the 9 zero-request names,** one invocation each, in the collector's universe order:
  ASML `security-81a74ed057551e58`, Adobe `security-37dddff4d4357038`, Air Liquide `security-dac5b3449b489f3f`, Alibaba
  `security-b05e0ccdc9868504`, America Movil `security-dc7848a34d3ffabd`, AstraZeneca `security-5f0ff2697ffe2748`, BB Seguridade
  `security-2674f09dec47231a`, BNP Paribas `security-e1596d485e713579`, BP `security-a37b3e6572f2baa4`. BA is NOT re-run.
- **The argv is the same** (`--no-sign-in`, sa only, `--max-jobs 1`).
- **Before each invocation:** read the runtime `cooldown` table. If sa is under cooldown, STOP.
- **The STOP statuses gain `upstream_unavailable` and `cooldown`:** a 5xx ends the batch, and so does a skip.
- **Timing:** it ENDS by 08:00Z, and no invocation starts after 07:45Z.
- **Upload once, and AC1/AC2 over the COMBINED record:** the first pass plus A2, in one `ad2_runs.json`.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

**AMENDMENT 2 (issuer, 2026-10-01 ~01:2xZ) -- the A2 result, and rulings on `Z-W88-S3` and `Z-W88-S4`.**
- **A2 ran** (drained @`46469b1acf`):
  - ASML: 1 listing page OK and 8 articles fetched, then a ProxyError on its 9th article. The job ended `error`, with a
    collector cooldown.
  - Adobe: 2 listing pages and 20 articles, then a 502. The job ended `upstream_unavailable`, a STOP.
  - Names 3-9 did not start.
  - 31 objects were uploaded. 0 sign-ins, sa only.
- **`Z-W88-S3`, ACCEPTED:** the worker waited out the collector's own cooldown before Adobe, which honours the
  check-before-each-name rule. `error` is NOT added to the STOP set: it was a transport (proxy) failure on one article, after
  the listing completed.
- **`Z-W88-S4`, the issuer's check bug, FIXED:**
  - `ad-2.AC2.py`'s STOP print formatted a 2-tuple with one `%s`;
  - and pages were MEASURED only on concluded jobs, though a job whose listing reached a span has measured its pages whatever a
    late article error did.

  On the trunk, AC2 then PASSES:
  - measured mean **1.33 pages per name** over 3 jobs (BA 1, ASML 1, Adobe 2);
  - the re-based sa ceiling for the other 79 names is **105 listing pages** (DEFAULT 1,975);
  - names REACHED (concluded): 0.
- **The finding for the round:** sa REST serves listings and articles. Each job's terminal failure is a late article-level
  transport or 5xx error (a ProxyError; a 502), not a challenge and not the account. The sa egress is the collector's
  `existing-residential-proxy` (`contracts.json`), so the ProxyError sits on that hop.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>31</round>
<slot>~88</slot>
<fabric>site-z</fabric>
