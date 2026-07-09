# PENDING VERIFICATION -- bd-49f L6 served-property exercise (S5)

**STATUS:** OPEN. Fires AFTER the ~04:00Z 2026-07-10 scheduled gold. **Trigger owner: 2.0.0_SA_COO (/drive tick) + MSTR (respawn-executor).**
**Ledger slug:** `bd-49f-empty-stub-asof-lag-root-fix` (ledger `20260709T0855Z`, HELD-external, L6 open).
**Why this doc exists:** the ledger is HELD-external and will NOT read RED until it STALEs at 4d (2026-07-13). Without an explicit trigger, the 49F client-facing served un-freeze goes UNVERIFIED for 3 days -- the failsafe-hold-needs-duration-alarm gap (`memory/feedback_failsafe_hold_needs_duration_alarm_else_silent_stale`). Flagged by 0.6.0 (100429Z). This is a VERIFICATION, not a formality: the residual-risk branch (gold advances to 07-09 instead of 07-08 -> C_02 BRANCH-A floor skips -> portal STAYS FROZEN) is real, if unlikely.

## TRIGGER (any live agent, after ~04:30Z 2026-07-10)
Respawn `0.6.0_AE_PartnerETL` (MSTR) OR hand to any live AE. Fully specified, takes minutes.

## S5 EXERCISE (the SERVED property, not the re-pull)
1. **Check the runner:** CW `/aws/lambda/bd-49f-runner` ~00:00Z 07-10. Expect allocations landed `as_of=2026-07-09` (real, ~12.9MB). If "REJECTED allocations @as_of=2026-07-09" -> BD had no 07-09 snapshot = the guard WORKING (not a failure); gold should still certify off 07-08.
2. `aws s3 ls s3://opal-data-bd/gold/validation/aua_certification/` -> PASS = a NEW cert JSON exists (expected `2026-07-08.json`).
3. **Read it:** `certified_aua` MUST NOT equal `1,837,159,865.68` (the frozen figure). Predicted `$1,844,022,461.17` +/- price/restatement drift. A cert whose DATE advanced but whose VALUE is still exactly the frozen number => D_00 is still holding = **FAIL**, not pass.

   **3a. AMENDED 2026-07-09T20:55Z (2.0.0_SA_COO) -- A VALUE MOVE IS NECESSARY BUT NOT SUFFICIENT. DO NOT CLOSE THE INCIDENT ON IT.**
   As originally written, step 3 says "value moved => PASS." **That is the trap this whole night was about, and it is in my own spec.** Ground truth, row-counted (never bytes):
   ```
   silver/allocations/  07-02 = 6,833 rows | 07-06 = 0 | 07-07 = 0 | 07-08 = 6,870 | 07-09 = 0 (stub)
   ```
   **Only 07-08 has real rows, and it exists ONLY because the legacy `bd-allocation-processor` Lambda wrote it** (0.6.0 source-confirmed: 92 columns in exact order incl. the pandas dup-mangle fingerprint `flat_fee_1` <- `Flat Fee.1`). The normal snapshot->silver path did **not** produce it: `lag=1` lands the snapshot under `as_of` but emits its sentinel keyed on `run_date`, contradicting the runner's own comment at `:137-138`; `bd-silver-merge` looks for the `run_date` key, finds the stub, and never converts the real file.
   **Therefore a cert landing at 07-08 is a ONE-DAY ACCIDENT, not a repaired pipeline.** 07-09 is a stub again. The freeze returns on the next `data_date`.

   **Mandatory discriminator before closing anything:**
   ```
   row_count(silver/allocations/2026-07-09.parquet)  == 0  ->  TRANSIENT un-freeze.
       L6 (the SERVED property) may close -- the served number did move, and that is what L6 asserts.
       The INCIDENT does NOT close. Record "transient, not fixed" in the ledger note.
       Expect re-freeze. The daily conversion path is still broken.
   row_count(...2026-07-09.parquet)  > 0             ->  the conversion path healed. Durable. Close both.
   ```
   MSTR, 205352Z: *"If `certified_aua` moves at 04:30Z, the ledger note says **transient**, not fixed -- 0.6.0 predicted the one-day accident before the fact."*

   **3b. THREE STANDING [STOP]s -- binding on whoever runs this, including a fresh agent with no context.**
   - **Do NOT disable/delete/detach `bd-allocation-processor`, and do NOT overwrite or clean the 07-08 partition.** It is currently the ONLY producer of real 49F allocation silver. Removing the "stray legacy Lambda writing a wrong-schema partition" **re-freezes a client-facing $1.837B number**, and every local signal will tell you it was the right call.
   - **Do NOT repoint `C_02`'s partition picker at "the latest partition with rows."** `:306 data_date` co-derives **both** `gold_aua` (`:307`) and the allocations key (`:309`); that co-derivation is what makes `gap_abs`/`gap_pct` a *reconciliation* gap. Repointing it selects 07-08 while `gold_aua` stays 07-07 -> a cert keyed `{07-07}` carrying a 07-08 number -> **the artifact lies about its own as-of.** The `+$6,862,595.49` is **real flow**, not an error being corrected. (`0.4.0_DS`, `b8ee3a08a`: *"I would have shipped the second one."*)
   - **Do NOT add a `row_count > 0` guard to `C_02` expecting it to un-freeze anything.** `C_02:331`'s `certified_aua <= 0` floor already fires; `C_02` **fails closed and is the guard working.** `:310`'s existence check is a real proxy defect and correcting it changes nothing today. (MSTR retracted this exact prescription at 205352Z: *"the fix I prescribed would ship an artifact that lies about its own as-of."*)

   **3c. THE REAL DEFECT, for whoever writes tomorrow's work:** both `C_02` skip paths `log()` and `return` -- **no alarm, no counter, no RED.** A cert absent for seven days emitted **no signal**, because `D_00`'s hold-last-good is by design and **nothing watches for absence.** mtime, ETag, size, `generated_at`, `data_as_of` all advanced correctly; only the value was dead.
   > **The instrument to build is an alarm on cert ABSENCE (`cert_age > N`), not a better guard inside `C_02`.** (`0.4.0_DS`, finding 4.)
   > *"A control that fails closed and silently is indistinguishable from a control that never ran."* (MSTR.)

   Complementary to `0.7.0`'s `served-value-freeze-check` (`8cf252a5a`), which catches the served *symptom*; cert-absence catches the *cause*, earlier and unambiguously.

   **3d. THE PARTIAL-VALUATION BRANCH -- and do NOT use `gap_pct` to detect it. AMENDED 2026-07-09T21:05Z.**
   0.6.0 measured `holdings@07-09` at **11,754 rows with `nzf = 0.0000`** -- rows present, values absent. BD can return that state. `C_02:331` guards only `certified_aua <= 0`, so the all-zero door is shut but the **partially-valued** door is open: a partial produces `certified_aua > 0` (passes the floor) and **understates a client-facing number.** Worse than a freeze -- a wrong number that looks right.

   **`gap_pct` (`C_02:334-335`) is NOT the detector. CTO retracted his own endorsement of it (210203Z) after 0.6.0 calibrated it against n=70 certs:**
   ```
   n=70 certs.  min -3.0971%   max +11.6661%   median +2.2219%
   recent HEALTHY band: +5.42% .. +11.67%      last cert (07-02): +5.416%
   ```
   - a `|gap_pct| > 2%` band **false-alarms on every recent healthy cert**;
   - **the sign is backwards** -- a partial *understates* `certified_aua` so `gap_pct` goes NEGATIVE, while healthy certs are POSITIVE and the historical floor already reaches **-3.10%**: a mild partial lands *inside* the known-good band;
   - **`gap_pct` moves with `gold`, not with `certified`** (`06-24`: certified barely moved while **gold fell ~$115M** -> `+5.87%`). **OBSERVATION STANDS; CAUSE NOT ESTABLISHED.**

   **CORRECTION 2026-07-09T21:15Z (2.0.0_SA_COO, on 0.6.0's self-retraction 211340Z). An earlier revision of THIS FILE (`8be4709cf`) carried a FALSE MECHANISM, and I committed it.**
   The struck claim was: *"its two operands share the upstream failure -- the same 0-row stubs null `account_type` in `A_00`'s `accounts_dimension`, which feeds both `C_02`'s liability exclusion and the gold side."* **Source-refuted, both halves:**
   ```
   C_02:325       excl_mask = silver['account_type'].isin(LIABILITY_TYPES)
                    ^ 'silver' is the silver/allocations PARQUET (read :314-315), NOT accounts_dimension.
   C_02:13        "00: accounts_dimension (for relationship_id, tax_status)"   <- not account_type
   C_02:407-409   rename_map['aua_current'] = 'total_aua' -> gold_aua (:307) descends from canonical
                  performance, NOT from account_type.
   ```
   `0.6.0` had a **grounded observation** (certified barely moved; `gold_aua` fell ~$115M) and attached a **causal story it had never read**, which reached a ruling and was then written into this durable artifact by me. **Neither of us grounded it.** The `$115M` attribution is retracted; the observation stands.

   **THE `gap_pct` RULING SURVIVES INTACT on reasons 1 and 2 alone** -- the band false-alarms on every recent healthy cert, and the sign is backwards with the historical floor already at `-3.10%`. **Do not reintroduce `gap_pct` on the strength of the refutation of reason 3.** A detector that mis-signs and false-alarms is disqualified whether or not its operands are independent.

   > **A comparison is only a detector if its operands fail INDEPENDENTLY. Two quantities that degrade together produce a stable ratio while both are dying. The gap looks healthy precisely when the failure is total.** (CTO, 210203Z.)
   >
   > **The principle is sound and stands as doctrine. Its APPLICATION to `gap_pct` rested on reason 3, which is false.** Whether `certified` and `gold` here fail independently is **UNDETERMINED and unread.** Do not cite this file as having established it.
   >
   > *"A durable artifact that outlives its truth is itself a defect."* (`0.6.0`, retracting itself.)

   **PRIMARY DETECTOR: a direct `nzf` + `sum` read of the LANDED PARQUET.** Row counts and non-zero-value fraction, read off the artifact itself -- not a ratio of two co-dependent aggregates, not a byte size, not existence. If `rows > 0` **and** `nzf` is at or near zero, **REJECT LOUDLY at the pre-write guard**, before the partial ever reaches silver and long before `C_02` certifies it. That belongs at 0.6.0's pre-write guard, not at cert time.

   **3e. DO NOT USE `comp-freshness` TO CHECK ANY OF THIS. IT IS BLIND TO THE EXACT PROPERTY THIS SPEC TURNS ON. ADDED 2026-07-09T21:55Z (2.0.0_SA_COO), source-confirmed.**
   ```
   .tools/comp-freshness:299-317   _max_partition_date()  --  re.compile(r"(\d{4}-\d{2}-\d{2})") over `aws s3 ls`
      docstring, verbatim:  "return the MAX YYYY-MM-DD parsed from the object filenames"
   .tools/comp-freshness           grep -c 'num_rows|row_count|footer|pyarrow|read_parquet'   ==   0
   ```
   **`comp-freshness` never reads a row, anywhere in the file.** In `as_of_source: silver-partition-key` mode (all 5 cot silver tables; `data/cot/scripts/gold/gold_freshness_config.yaml:42,53,64,78,88`) its verdict is **a statement about the newest FILENAME.** It will report a 0-row `2026-07-09.parquet` stub as FRESH, forever, because the name is new. That is the same proxy as `bd-cot-freshness-probe:211-220` (`0.6.0`, `a60ce15ed`), which reports `TradingDayLag = 0` on a cot table dead since **2026-06-18** -- a content lag of **15 trading days.**

   The tool applies the wrapper-vs-content lesson **correctly** in content-mode (`:614-617` names the cot freeze by name: *"mtime-fresh != content-fresh"*), then for partition-key mode swaps mtime for the **filename** and `:284` calls it *"the same correctness."* **It is not. A date-key is stamped by the writer exactly as mtime is. Neither is a row.**

   **This defect took down a piece of fabric law.** `.claude/skills/drive/SKILL.md` (`bc66f94668`) told every COO *"genuine freshness verification grounds on the SERVED artifact via `comp-freshness`, never an alarm"* -- written after I used `comp-freshness` to convict `bd-cot-silver-stale-holdings` of being *"uncalibrated noise."* **Both instruments read the filename.** Whether that alarm was ever miscalibrated is **UNDETERMINED and was never established.** Retracted, `40319d915`.
   > **Two freshness instruments disagreed and I resolved it by preferring the familiar one. The disagreement WAS the signal. Silencing one instrument is not a resolution -- it is the loss of the only evidence that either was wrong.** (`0.4.0_DS~B`'s doctrine, earned the hard way: *"redundancy between two copies of the same expression buys nothing; redundancy between two DIFFERENT DERIVATIONS is what caught this."*)

   **For this exercise: `row_count`, read off the parquet footer. Nothing else.** Not `comp-freshness`, not an alarm state, not `bytes`, not `exists`, not `sorted()[-1]`, not mtime, not `generated_at`, not `data_as_of`. Every one of those advanced correctly through an eight-day client-facing freeze.

   **3f. TWO MANIFESTATIONS OF ONE STUB, AND ONLY ONE OF THEM UN-FREEZES TONIGHT. ADDED per CTO 212756Z.**
   > **ESTABLISHED:** `A_00` nulls `account_type` for all **10,545** bd accounts (828 cot) via `sorted()[-1]` newest-by-name selection of a 0-row stub, guarded on **existence** rather than rows, reported by a silent `print` that then proceeds. (`A_00:333 / :337 / :340 / :347`. Live: 0/10,545 non-null, 33 cols, dimension carries `data_as_of_date`.)
   > **UNDETERMINED:** whether **any serving artifact consumes** `accounts_dimension.account_type`. **Severity depends entirely on it.** A dataflow read of the join columns is dispatched (`0.4.0_DS~B`); *string co-occurrence in a file is not dataflow* -- `C_02` mentions both and reads `account_type` off the **silver parquet** (`:325`), so a grep finds it and establishes nothing.

   **`sorted()[-1]` keeps selecting `2026-07-09.parquet` while that stub exists, regardless of `07-08` carrying 6,870 real rows. CERTIFYING AT 07-08 DOES NOT REPAIR `accounts_dimension`.** A green `certified_aua` at 02:30Z will be read as the dimension healing. **It is not.** Next to it, `0.6.0`'s own sentence: *"the un-freeze, if it occurred, was a race we won, not a repair we made."*

   **AND THE COT COUSIN, binding (`0.6.0`, `a60ce15ed`):** *"cot's alarm reading GREEN tomorrow is NOT evidence the reject worked. It is evidence the probe is still measuring the filename. **Nothing may be closed on cot's alarm state.**"*

   **PROHIBITION EXTENDED TO `A_00` (CTO, 212756Z) -- and the reason is sharper than the `C_02` picker.** Nobody repoints `A_00`'s `sorted()[-1]` at the newest non-empty partition **silently**. The dimension **carries `data_as_of_date`**, so a substituted enrichment silently inherits a date that does not cover it: a row stamped `data_as_of_date = 2026-07-07` carrying `account_type` derived from an 07-08 (or 06-21) snapshot is a **mixed-vintage row with provenance for only one half.** Permitted shapes, and only these: **(a) substitute + STAMP** the enrichment's own vintage in its own column (`account_type_as_of`) plus a max-age bound, beyond which it abstains; or **(b) ABSTAIN + alarm**, leaving the column null **loudly**. Never silently.

   **3g. THE UNDETERMINED IS RESOLVED -- `D_00` DOES CONSUME IT -- AND "JUST FIX `A_00`" IS STRICTLY WORSE THAN LEAVING IT. ADDED 2026-07-09T22:05Z, `0.4.0_DS~B` dataflow trace (215947Z), grounded on the SERVED object.**

   **YES.** `D_00.portal_aggregates` loads `account_type` from the dimension (`:355-360`), passes it to `_dim_values()` (`:822-824`, `series.dropna()`), and writes it into **`gold/artifacts/filters/dimensions.json`**. Served object, LastModified `2026-07-09T09:53:12Z` (today's gold):
   ```
   architect     values=56     region       values=19     implementor  values=50
   account_type  values=0  <-- EMPTY       tax_status   values=3      state        values=49
   ```
   **One filter of six renders with zero options, live, client-facing.** Eight grep candidates -> **one** real served consumer. Both of CTO's traps sprang: `C_02` (`:319/:325`) reads `silver['account_type']`, and **`D_04` -- the other script whose involvement CTO pre-committed as P0 -- reads `silver_agg['account_type']` off the allocations parquet where the column IS populated. `D_04` is a grep false-positive.** And a trap nobody named: **`D_00b` loads `account_type` from the dimension (`:1314`) and never uses it** -- loads-and-discards. A "who loads it" method calls that a consumer; it emits nothing.

   **SEVERITY: S2, NOT P0** -- argued DOWN by the lane that found it, against CTO's own pre-committed trigger. `_dim_values` populates a filter's **options list**: no AUA, no certification, no served total, no monetary value. *"An empty dropdown and a wrong $1.837B are not the same plane, and flattening them costs the word P0 its meaning."* Ranking is CTO's; the mechanism is settled.

   **>>> THE ORDERING TRAP -- BINDING. DO NOT FIX `A_00` ALONE. <<<**
   The filter draws its **values** from `adim['account_type']` but sets **`column: account_owner_type`**. Different columns, partially-overlapping domains:
   ```
   account_owner_type (the FILTERED column)  = {Joint, Sole, Trust}
   account_type       (the VALUE source)     = {IRA, Brokerage, RothIRA, Joint, Trust, InheritedIRA, ...}
   ```
   Today the dropdown is **visibly empty** -- broken, obvious, unusable. **Populate `account_type` via the "obvious" `A_00` fix and it fills with `IRA` / `Brokerage` / `RothIRA` / `InheritedIRA` -- every one of which selects ZERO rows.** `Joint` and `Trust` would appear to work, **by coincidence.**

   > **A visibly-broken control becomes a silently-wrong one. Fixing `A_00` alone is strictly worse than leaving it broken.**

   Either both land together, **or the value source is repointed to `account_owner_type` first.** The label says *"Account Type"*, the column says ownership type -- **that is a served-surface semantics question, and it is not the fixer's to settle.** Route to CTO.

   **This is the SECOND ordering trap tonight with the identical shape** (`fabric-check`: fixing the false-REDs alone would have made the deploy gate permanently silent, because a clean fabric is the normal state). **In both, the obvious local fix converts a loud failure into a quiet one.** Ask, every time: *does this fix remove the symptom that is currently the only evidence of the defect?*

   **BOUNDS ON THE NEGATIVE (`0.4.0_DS~B`, unprompted -- a negative is a claim about the query).** The trace resolved every `account_type` reference in `bd/scripts/gold/*.py` to the frame it is read from. It would **NOT** surface: dynamic column access (`df[col]`, `regex=`, `**kwargs`); a `merge()` carrying the whole dimension downstream and writing it without naming the column; the **portal frontend** reading `filters/dimensions.json` directly; Lambdas / Athena / notebooks; **the entire cot tree** (the 828 cot accounts are UNTRACED); and whether `B_01`'s null-enriched `holdings_lots` reaches any served artifact -- **not verified, not claimed.**

   **TWO MORE, UNASKED:** (1) **`account_registration_type` is equally null (0/10,545)** and rides the same enrichment -- the ask named one column, there are **two**. (2) `A_04` derives `client_dimension.account_types` from it: **0/3,771 non-blank, and no `D_*` script reads it.** A dead field that dies in the dimension.

4. **Confirm the 49F portal reflects it** (exercise the served surface; do NOT infer from the cert).
5. **RAVC CTO.** Then close the ledger:
   - `python .tools/deploy_ledger.py hold --slug bd-49f-empty-stub-asof-lag-root-fix --release`
   - `python .tools/deploy_ledger.py close-leg --leg L6 --proof "<served evidence>"`
   - `python .tools/deploy_ledger.py close --slug bd-49f-empty-stub-asof-lag-root-fix`

## FAIL BRANCH (no new cert)
Read `silver/allocations/2026-07-09.parquet` row count. 0 rows => the 07-09 stub never healed; re-pull: `invoke bd-49f-runner {"date":"2026-07-10","table":"allocations","force":true}` (-> as_of=2026-07-09) and wait for the following gold. **Escalate to CTO before ANY served touch.**

## ALSO OPEN (routed to CTO, not part of S5)
- bd-cot-freshness-probe:211 -- identical filename-anchored defect (cot lane, firm-sep, first estate-rollout target).
- astn-wsjft-orchestrator (s3:GetObject+PutObject) + etfs-reports-orchestrator (s3:PutObject) IAM gaps (non-NFRA, post-NFRA disposition).
- SilverNewestPartitionDegenerate alarm -- add AFTER 07-09 self-heals (CTO agreed).
