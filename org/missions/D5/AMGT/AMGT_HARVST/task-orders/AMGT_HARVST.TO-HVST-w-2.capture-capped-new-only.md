# AMGT_HARVST task order -- `HVST-w-2` -- ROUND 12 chain 3 of 4, cell 2 of 2: CAPTURE, CAPPED, `--new-only` -- sa, at most 25 jobs, every call ledgered

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-w-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~37</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- the producer needs S3 GET/PUT on opal-data-harvest bronze and silver under the sa subtree (the grant HVST-v-2 exercised). No gold write. A refusal is a BLOCKING row, never a workaround.
comp-adversary: RUN at L5 -- the adversary is a --new-only skip that drops a NEW article because its url/id did not match a held one, reported as "already held". AC4 lays the skips out for L9.
</preflight>

## 0. THE STANDING CLAUSES, first because they are absolute

1. **ANDREW'S WORD** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_1805Z_OPEN_CALLS_FOUR_RULINGS.md`
   ruling 2): `w-2` YES **with a stated cap and `--new-only` dedupe on**, after the round-11 rebuild (landed
   @`085e15c649`). **THE CAP, stated by the issuer:** publisher **sa only**; at most **5** producer invocations of
   `--max-jobs 5` (**25 jobs total**, the sa-symbol ceiling HVST-v-2 measured: 25 of 89 resolved securities carry a
   usable `sa_symbol`); then ONE `upload-harvest`. Stop EARLY on any rule in clause 3.
2. **MECHANISM.** Every vendor byte comes from the EXISTING scripted producer invoked from the command line --
   `python -m lib.opal_data_harvest run ...` -- driven by your committed runner script. **A candidate whose evidence
   depends on a vendor call made inside an agent turn FAILS ON MECHANISM EVEN IF THE DATA IS RIGHT.**
3. ⛔ **STOP RULES -- YOU DO NOT RE-AUTHENTICATE. EVER.** If the output shows an auth refresh, a browser starting, a
   verification repair, or a login: STOP immediately, file a BLOCKING row, report. Also stop the invocation loop when
   an invocation's every job is cooldown-suppressed (row `Z-W22-S2`: one Timeout cools the whole publisher for the
   rest of that invocation, so a smaller `--max-jobs` bounds the loss) or when the producer reports no remaining
   jobs. **A zero is an acceptable outcome; a login is not.**
4. ⛔ **THE LEDGER IS A CONDITION OF THE WORD.** One `## CALL n -- seekingalpha.com, <UTC>` entry per producer
   invocation that reaches the network, appended to
   `org/missions/D5/AMGT/AMGT_HARVST/ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_37.md` (the file `HVST-w-5` created;
   same shape) **in the SAME commit as the evidence.**
5. **THE RUNTIME ROOT.** A linked worktree has no `.runtime`; every producer invocation passes
   `--runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`. Read it there; never
   copy it into the repo.
6. **NO S3 DELETE. NO GOLD WRITE. NO `lib/` CHANGE** -- a producer defect is a BLOCKING row.
7. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~37;`.
8. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/` -- **never `.scratch/`.**
9. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~37/AMGT_HARVST.TO-HVST-w-2.capture-capped-new-only.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-w-2.capture-capped-new-only`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/
org/missions/D5/AMGT/AMGT_HARVST/ledger/VENDOR_CALLS_0.9.0_WK_AMGT_HARVST_37.md
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE PRODUCER, as measured at the cut (`lib/opal_data_harvest/__main__.py`)

`run` takes `--publishers {sa,ft,wsj,bbg,barrons}`, `--all-securities`, `--max-jobs` (caps JOBS, not securities; the
cursor persists per plan, `worker.py:335-349`), `--new-only`, `--harvest-grammar`, `--runtime-root`;
`upload-harvest` takes `--max-objects` (default 10). rc is 2 unless every status is `complete_candidates`,
`new_articles` or `no_new_articles` (`:218`) -- **a non-zero rc is data, not a crash.**
⛔ **THE RECEIPT TRAP:** a job suppressed by cooldown returns BEFORE `previously_stored` is set (`worker.py:128-136`
vs `:149`), so its receipt carries `mode` but NO `previously_stored`. Count those as a separate bucket; never read
an absent field as zero.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 1800). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-w-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac1_capped_capture.py</invocation><expect>THE CAPPED CAPTURE, WITH ITS DEDUPE VISIBLE: each producer invocation printed VERBATIM (command line and output, at most 5, each `run --publishers sa --harvest-grammar --new-only --all-securities --max-jobs 5 --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`), the stop reason printed; per job its mode and previously_stored, with jobs attempted / skipped for a missing sa_symbol / cooldown-suppressed (no previously_stored field) / returned rows, each over its denominator; total vendor requests, "auth_refreshes: 0", "browser_started: False"; and the ledger entries printed as written. Total jobs never exceed 25</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-w-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac2_upload_and_delta.py</invocation><expect>ONE `upload-harvest --max-objects 40 --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"` recorded verbatim, with the BEFORE and AFTER counts of sa silver listing_hit and article rows on the SAME instrument and the signed deltas; a zero delta is reported as a zero with its cause named</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-w-2" judgment="true"/>

  <criterion id="AC5" cell_refs="HVST-w-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac5_incident_spend_bound.py</invocation><expect>GUARD (c), RUN FIRST, BEFORE ANY CAPTURE: the 00:21Z incident's Kimi spend ledgered as a bounded estimate from LOCAL evidence only -- the run.log's vision-classified steps (expected 3: steps 0, 1, 2; steps 3-4 cache hits), model kimi-k3, max_tokens 4000 each plus the image input per call, priced from the kimi-k3 rate card with the card's date and URL -- and the entry appended to the ledger as `## INCIDENT 1 SPEND -- ESTIMATE-UPPER-BOUND`, with the provider-read figure recorded as NOT MEASURED (an account-holder item). Print the entry as written. NO call to api.moonshot.ai or any Moonshot console or usage endpoint</expect></criterion>

  <criterion id="AC6" cell_refs="HVST-w-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac6_planted_reauth_is_refused.py</invocation><expect>GUARD (a), RUN SECOND: a PLANTED test that WOULD fire the producer's real re-authentication -- it calls `SessionManager.refresh('sa')` and `SessionManager.get` with no saved envelope, and `repair_verification` -- is run INSIDE the capture runner's own process -- the runner script invoked from the command line exactly as AC1
invokes it, with the planted calls in place of the producer run -- and each is REFUSED by the guard before any browser, network or credential read (print, per entry point, the refusal and "browser_started: False", "credential_read: False"). ALSO print, from inside that process, the identity of the guard object each entry point resolves to, proving the guard is loaded in the process that runs the producer (the 00:21Z incident was a guard that never loaded). The unguarded variant is NEVER run</expect></criterion>

  <criterion id="AC7" cell_refs="HVST-w-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac7_no_vision_call_and_stop_on_bot_wall.py</invocation><expect>GUARD (b), read from the CAPTURE run's own record after AC1: calls to api.moonshot.ai (and any other vision-model endpoint) = 0, verification repairs = 0, re-authentications = 0, browsers started = 0; and IF any job met a bot wall or VerificationRequired, the run STOPPED there (the stop reason printed with its job). A bot wall is an accepted stop, never a repair</expect></criterion>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~37/scripts/ac4_are_the_skips_really_held.py`.
**Are the rows `--new-only` skipped truly already held -- the SAME article -- or did a url/id mismatch skip a NEW one?**
For a sample you size and justify yourself (all skips if 40 or fewer), print each skipped item's identifying fields
beside the held article it was matched to (title, url or id, published date). Present; record NO verdict.

## 3. WHAT THIS CELL DOES NOT DO

No bbg/ft/wsj/barrons capture, no gold rebuild, no producer change, no re-authentication, no retry beyond the cap.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **sa only, and why:** bbg is unplannable until `w-5` explains the refusal (decomp `s.20.5`); ft/barrons are under
   `w-4`'s diagnosis; sa is the one channel whose identity path (sa_symbol) is measured. The CTO can widen the
   publisher set at round 13 on the evidence.
2. **The cap is 25 jobs in invocations of 5**, which is `Z-W22-S2`'s disarm option (a) taken halfway: a Timeout
   costs at most the rest of one 5-job invocation, not 7 of 8.
3. **Same worker as `w-5` (`~37`), after it**, per the analysis's order (w-5, w-4, w-2 under one runner); `w-4`
   was cut vendor-free and runs on its own slot. The ledger file is shared by the two vendor cells on purpose.
4. **The judgment is `s.20.6`'s, carried unchanged since round 8.**

**AMENDMENT 1 (issuer, 2026-09-29 ~02:3xZ) -- RESUME BEHIND THREE GUARDS (row `AMGT_HARVST-Z-W37-S3`).** At 00:21Z a
guard test in this cell misfired and ran the producer's real Seeking Alpha re-authentication (headed Chrome, stored
credential submitted, bot wall, 3 Kimi vision calls); no capture, no session saved, no S3 write. The order was HALTED.
`1.0.0_SA_CTO~Z` ruled the resume under Andrew-direct ~02:2xZ (record @`74e1eea534`, "none of this should be waiting on
me") on his existing 18:05Z word, behind three guards, each now a criterion: **AC5 = guard (c)**, run FIRST and before
any capture; **AC6 = guard (a)**, run SECOND; **AC7 = guard (b)**, read from the capture run. Guard (c)'s method is the
CTO's ruling msg 26396: a ledgered UPPER BOUND from local evidence, no Moonshot call of any kind. **The rate card:** no
kimi-k3 rate exists in the repo (0 relevant hits over 78,657 files, measured by the issuer at the cut); the worker may make
ONE unauthenticated read of Moonshot's PUBLIC pricing page (no key, no account, no API) and records its URL and read date
in the entry; if that page cannot be read, the entry carries the call/token bound with the rate marked UNMEASURED and
AC5 still passes. **The guards' mechanism:** this order grants no `lib/` path, so the guards live in the worker's
runner, which neutralises `SessionManager.refresh` (`auth.py:54`), `SessionManager.get`'s no-envelope fallback
(`auth.py:22`), `repair_verification` (`worker.py:282`) and the Moonshot call (`verification_locator.py:19`) BEFORE
calling the producer's own CLI entry point in the SAME process -- never through `PYTHONPATH`/`sitecustomize` in a child
that may not load it. **Criteria count 5 mechanical + 1 judgment, above the diet's three, and the reason is one line:
each added criterion is a guard the CTO's ruling makes a condition of the resume.** The gate limb that grades this
modification: GATE (viii) (the order declares `<placeholders>`).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>12</round>
<slot>~37</slot>
<fabric>site-z</fabric>
