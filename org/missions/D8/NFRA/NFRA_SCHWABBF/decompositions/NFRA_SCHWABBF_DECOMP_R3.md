# NFRA_SCHWABBF decomposition -- ROUND 3 (2026-10-20, issuer 2.0.0_SA_COO~SB): the per-master firm form, 0840 and Cottonwood only

Cut on the CTO's round-2 analysis `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/ROUND_ANALYSIS.round2.md` @0fd3b119fd (msgs 109921, 109922) as narrowed by Andrew-direct ~16:3xZ, relayed in CTO msg 109927, VERBATIM:
"I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
and on PRD v0.7 @ad57e2f73a (CTO msg 109930: the key-function hold on the shared puller is LIFTED against v0.7). Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_163xZ_SCHWABBF_0824_OUT_FOCUS_COTTONWOOD_AND_0840.md`.

**What v0.7 changes under the round-2 code.** C-KEYFORM applies PER MASTER: the key function holds the set of firm-form masters (**08403355 and the four Cottonwood masters 08719286, 08134043, 08165601, 08480305**) and returns today's key, byte for byte, for every other master. 08242234 (0824) and 08335338 (0833) are OUT: they keep their daily pull and their current keys; nothing moves, backfills, re-keys or records them. "One master is never stored in two forms."
Round 2 put all three 49F masters on the firm form in the key function, the move tool, the readers, the puller, the trace and the IAM text. Nothing is deployed, applied or moved, so this round REWORKS those merged files to the per-master rule.

**The gate.** The L6 gate reads the ratified-text half STALE (the ENDPOINT changed at v0.7; the CTO calls the re-sign a formality under proportionate sign-off, but the gate refuses a new order until the CVO's file lands). The decomposition is cut now; the orders issue the moment the half reads SIGNED. No override is taken.

Rounds 1 and 2 are `decompositions/NFRA_SCHWABBF_DECOMP.md` and `..._DECOMP_R2.md`, terminal and merged.

## The per-master contract (fixed here; every cell builds against it)

- `FIRM_FORM_MASTERS` = {08403355 -> `49financial`; 08719286, 08134043, 08165601, 08480305 -> `cottonwood`}. Key for these: `schwab/{firm}/bronze/{feed lower}/date={YYYY-MM-DD}/{vendor file name}` = `address('schwab', <firm>, 'bronze', <feed>, 'date=YYYY-MM-DD')` without `s3://opal-data-assets/`, plus `/` plus the vendor name (unchanged from round 2).
- Every other master (08242234, 08335338): TODAY'S key byte-for-byte: `schwab/{master}/bronze/{feed lower}/{YYYYMMDD}/{master}.CRS{YYYYMMDD}.{FEED}.zip`, and today's listers (the pre-round bytes of `list_bronze_dates` / `latest_bronze_date`, at commit `5f1ad506a4`).
- The set is a declared constant in both key-function mirrors; the test proves it is a subset of the registry's masters and contains 08403355 and the four Cottonwood masters. A master moves INTO the set only by a PRD change (C-ONEWRITER, C-ONBOARD), never by default.

## The rectangle (round 3)

| cell | item | PRD rows | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `BF-k-3` | the key function pair on the per-master rule | C-KEYFORM v0.7 | FWD-1, FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-m-3` | the move tool moves 08403355 only | C-MOVE v0.7 | FWD-1, FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | BF-k-3 |
| `BF-r-3` | the two hand-parsing readers (they read 0833) back to their pre-round bytes | C-READERS, C-SCOPE | FWD-5 | NOT-EVALUATED | laptop | LOCAL | worker-light | -- |
| `BF-w-3` | the puller: firm form for 0840 only, 0824 and 0833 byte-for-byte today's behavior | C-DAILY, C-BACKFILL | FWD-1, FWD-6 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing deployed) | worker | -- |
| `BF-t-3` | the trace: 0840 and Cottonwood only; any other master refuses | FWD-1 DONE WHEN | FWD-1 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-i-3` | IAM text: the firm-prefix write entry for 08403355 only (drop 0824 and 0833) | C-ALONGSIDE (shape), C-MOVE step 3 | FWD-1, FWD-6 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |
| `BF-n-3` | regenerate `modules/opal_name` for the new scope rows; add the `secret_name` output | C-NAMES | FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |

Reused as merged: `BF-c-2` (the converter, manifest, guard and census handle BOTH key forms; the firm-form tests stay valid), the event-rule text and converter read in `BF-i-2` (0840 and Cottonwood use the firm prefixes), `BF-e-1` (equality, by master).
Held, not in this rectangle: the retire-banners (R3-3; the amendment fixes 0824/0833 as LIVE old-form writers, so a RETIRED banner on `sdd-backfill-08335338.ps1` and `remap-bronze-to-monolith.py` waits for the CTO's word on them); FWD-2 backfill and FWD-3 record for 0840 (they follow the cutover); the 1,245 legacy members (withdrawn by v0.7).

**Chains (M = 6; fan-out 6 of 6, cap 8).** A = BF-k-3 -> BF-m-3 (slot ~1); R = BF-r-3 (slot ~2); W = BF-w-3 (slot ~3); T = BF-t-3 (slot ~4); I = BF-i-3 (slot ~5); N = BF-n-3 (slot ~6).

**Write sets (disjoint).**
- BF-k-3: `data/black_diamond/scripts/bronze/_monolith_bronze.py`, `data/canonical/schwab/silver/_canonical_silver_lib.py`, `data/canonical/schwab/tests/test_bronze_key_form.py`.
- BF-m-3: `data/canonical/schwab/keyform/move_bronze_key_form.py`, `data/canonical/schwab/tests/test_move_bronze_key_form.py`, `data/canonical/schwab/tests/fixtures/move_listing.json`.
- BF-r-3: `data/canonical/schwab/build_canonical_daily.py`, `data/canonical/schwab/silver/build_fact_tax_1099div.py`, `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`.
- BF-w-3: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py`.
- BF-t-3: `data/canonical/schwab/keyform/thread_trace.py`, `data/canonical/schwab/tests/test_thread_trace.py`.
- BF-i-3: `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf`, `data/canonical/schwab/tests/test_firm_prefix_grants.py`.
- BF-n-3: `infra/aws/terraform/modules/opal_name/{generated_locals.tf,main.tf,variables.tf,tests/opal_name.tftest.hcl,tests/fifo.tftest.hcl,tests/vectors.json}`, `data/canonical/schwab/tests/test_opal_name_generated_current.py`.

**The deploy hazard this round removes.** `_monolith_bronze.py` is mapped by the deploy gate to `s3://opal-data-bd/code/`. At HEAD it holds the round-2 ALL-firm rule, which would make the live bd converters (0824, via `PURPOSE_MASTER`) look in the firm folder and refuse "not moved". The gate holds it only because no OPEN change entry names it. No entry is opened until `BF-k-3` has merged.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: every round-2 artifact that keys bronze by master or firm (the 8 cells of round 2: z-2, k-2, m-2, r-2, w-2, t-2, c-2, i-2) plus the CTO's R3-2 name module = nine members. By subtraction: z-2 (a restore, done) = unchanged; k-2 -> BF-k-3; m-2 -> BF-m-3; r-2 -> BF-r-3; w-2 -> BF-w-3; t-2 -> BF-t-3; i-2 -> BF-i-3; c-2 = reused (tolerates both forms); R3-2 -> BF-n-3. Remainder: none.
- **Same grain. Intent coherence. State coherence.** One cell per write set; none writes to S3, applies Terraform, deletes, deploys, or contacts Schwab.

## Battery (round 3)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. The pull-fire times (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z) are inlined into BF-w-3.
- `comp-iam`: RUN. Denominator: `monolith-iam.tf` and `iam.tf` (2 Terraform files), `silver.tf` (event rules and the converter read), 3 masters enumerated before this round and 1 (08403355) after it for the firm prefix. Blind: the live IAM plane (0 roles read).
- `comp-adversary`: DECLARED-NOT-APPLICABLE as a lens run. Findings inlined: (1) the round-2 all-firm key function would break the live 0824/0833 bd converters if deployed (above); (2) the two hand-parsing readers read 0833, so under v0.7 they need NO change and the round-2 edit must come back out; (3) the puller serves three masters from one script, so the firm form is conditional on the master and the 0824/0833 paths must stay byte-for-byte; (4) 0840's firm folder is shared only with Cottonwood masters after the move, and Cottonwood masters never write it (one writer per master, C-ONEWRITER) -- the master filter still applies; (5) `terraform test` runs offline on the name module and reads `Success! 48 passed` today.

## Not in round 3

The release acts R0-R8 on 0840 only (re-cut after this round drains; they also wait on Andrew's silver-scope answer); the 0840 backfill (FWD-2) and held-days record (FWD-3); the retire-banners; the Alongside workstream (`~SA`); silver, meta and `_ops` scope.
