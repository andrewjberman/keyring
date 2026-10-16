# drive log 2.0.0_SA_COO~W1 -- 2026-10-15 17Z to 2026-10-16 04Z (desktop-hk1uu7n)

**archetype:** MIXED

Covers AMGT_HARVST rounds 86 and 87 after the 17:0xZ log. Push state of everything below: LOCAL on box/dell1 (origin/box/dell1 last read `15ef8949fc` at 02:3xZ; not re-measured since).

## What moved

- **Round 86 CLOSED in effect:** `HVST-ca-1` merged `d0c48b3946` (the wsj/barrons refresh is the in-profile renew, keyed on the contract fields and the account-check table); AC3 real job PASS (`de87f708fb`); Z-S121 answered (`D1-S17`).
- **Round 87** (CTO addenda 1 to 4, msgs 6075, 6081, 6094, 6099, 6335 to 6460): all four harvest publishers move to dell1 on Andrew's word. Cells and merges: `cb-1` (library stops naming site Z) `08c80a8f75`; `cb-5` (a tab session minimises its own window through the debug protocol; the flag `--start-minimized` was measured NOT to minimise) `e6649b1250`, AC3 PASS `2657939237`; `cb-8` (a profile-store publisher needs no saved bundle) `a879d12881`; `cb-10` (per-process S3 GET counters, ledger, cycle sums) `62fcc1978e`; `cb-11` (design B: a job's bound from a local watermark) `02d4090763`; `cb-12` (the uploader appends without reading the target table) `c1df06b1ef`; `cb-14` (the lookup matches date keys; seed and check command) `4d2a3e2187`. Seat orders: `cb-2` complete (runner registered); `cb-9` complete (re-pin, seed deleted); `cb-13` pending (SC1 mid-pass, runner live from pin `ddd7dcdc38` since T0 03:27:57Z); `cb-15` (sa and bbg join) staged behind cb-13's evidence.
- **The finding that drove the round:** every collector job re-read the whole silver `article` prefix (measured: one bbg job 747 GETs / 212,043,826 bytes; per call wsj 125.4 MiB, barrons 9.9, sa 80.4, bbg 202.2; a wsj cycle about 29.6 GiB by extrapolation). The CTO's 5 GiB bar stopped the runner by its stop file at 23:59Z; after cb-10/11 the same bbg job read 0/0; wsj on the new pin: 5 GETs / 94.6 KiB for 242 pairs. The uploader was the second copy (barrons measured 2.57 MiB per upload; sa `listing_hit` 284.2 MiB and bbg `article` 202.2 MiB would blow the bar), fixed by cb-12/cb-14.
- **Sign-offs given by the CTO:** first pair + erratum; addenda 1 to 4; amendments (seed order, narrowed list); C-d3. Each COO half is in `deliverables/2.0.0_SA_COO_W1/round87/`.
- **Rows filed by me:** `D1-S17` to `D1-S27` (answered/dispositioned worker and seat rows), the erratum ledger, the C-i record, the egress finding and real-read ledgers.
- **Other:** SC1 respawned at 03:15Z after its session ended with `cb-13` unread in its inbox (pre-flight clean); the security-metrics read surface (XA-cdcc) carried as a NAMED NEXT INCREMENT (section 116, CTO option A); keep-driving ON, my cron `e8625ea8` `/canonical-drive AMGT_HARVST` at :13 and :43.

## My errors, corrected in the record

- The pair named `opal-data-assets`; the runner writes `opal-data-harvest` (erratum, ratified).
- `HVST-cb-9` step 5's gate was circular (a stored session is returned before `browser_profile`); SC1 found it, the CTO ratified delete-first.
- `HVST-ca-1` assumed `sa` was bundle-seeded; `HVST-cb-12` called a datetime key limit acceptable without reading what the `listing_hit` key holds (a `date`); both repaired by amendment and `cb-14`.
- Timestamps: three surprise rows (`D1-S24`, `D1-S26`, `D1-S27`) carry a `surfaced_at` I wrote from estimate, not `date -u` (the gate WARNed on `D1-S27`, stamped 25 minutes ahead). Append-only; not edited; `date -u` from now on.
- A first pass of `cb-2` on the runner failed on an empty saved-session directory (my order's gap); SC1's stop was correct.

## Open at the end of this log

`cb-13` evidence: the first `upload-harvest` line under pin `ddd7dcdc38` and a duplicate check over parts read above zero (the 45-minute check read `parts_read=0`: vacuous, said so). Then `cb-15` (needs C-a4). sa session is a person's sign-in. No open call at Andrew from this seat.

## Compiler Tools

- `.tools/proof-of-spec-check.py <instance> --governing-order <order>`: VALID rc 0 on every worker instance (146, 147, 148, 149 re-run here) and on SC1's cb-2 and cb-9 instances.
- `.tools/round-close-check.py --project AMGT_HARVST --round 87`: MAY-CLOSE before each flip.
- `.tools/safe-merge.sh`: merged `d0c48b3946`, `08c80a8f75`, `e6649b1250`, `a879d12881`, `62fcc1978e`, `02d4090763`, `c1df06b1ef`, `4d2a3e2187` (fast lane, index check 0 differing paths each).
- `.tools/wk-provision.sh provision|remove`: sparse worktrees lacked `org/tier1_exec/4.0.0_SA_CRO/scripts` (test_ad1) and made corpus tests fail on files outside the cone; both read against the main tree.
- `.tools/safe-commit.sh`: GATE (viii) graded each modified order; the surprise-row gate WARNed once on a future-dated `surfaced_at`; one commit hit the 110 s tool timeout but landed. `comp-find` and the rail refused three Bash greps (F1, R6); native Grep and `comp-find --limit` answered.
- `.tools/unblock.py tick` with `--owed-ledger`/`--wait-until`; `.tools/drive-mode.py read`; `/mstr-spawn` pre-flight 1pt/1b/1c/1d then `spawn-agent.ps1` (SC1).
- Own probes (committed under `deliverables/2.0.0_SA_COO_W1/round87/`): `cb5_window_probe.py`, `cb10_job_get_probe.py`, `cb10_watermark_probe.py`, `cb10_silver_sizes_probe.py`, `ca1_real_job.py`.
