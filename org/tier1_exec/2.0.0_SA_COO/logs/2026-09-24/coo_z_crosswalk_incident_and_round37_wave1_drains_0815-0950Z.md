# 2.0.0_SA_COO~Z -- 2026-09-24 08:15Z-09:50Z -- the crosswalk overwrite incident, its restore, and the round-37 wave-1 drains

Continues `coo_z_startup_peers_closer_items_and_round37_cut_0438-0615Z.md` (@14b01608e7). Push state of everything below: LOCAL
(this lane does not push; 0.0.0_AB_MSTR~Z pushes on its cadence).

## 1. The crosswalk incident (served output), 08:02Z -> 08:22Z

- 2.0.0_SA_COO~X's AMGT_CORPUS induction fire (CLOUD @a419df8f9d, 08:01:43Z-08:02:54Z, 0 vendor calls) put TWENTY versions on
  `s3://opal-data-harvest/crosswalk/v1/2026-09-24.json` (write_pool once per called name, 204,711 -> 231,910 B). The FIRST put
  replaced this seat's 03:32:47Z signed publication (523,207 B, sha256 9bd953b9..., MEASURED 194, CTO-verified R-23, CVO PASS R-24).
- Measured here at 08:1xZ (head-object, get, direct invoke of opal-amgt-scoped-api): ASML_US_Equity and AAPL_US_Equity served
  UNRESOLVED; CAT_US_Equity derived 12 unchanged. INCIDENT, not the exposure msg 25324 / R-36 graded: their before-state was the
  previous dated key (09-22), never the exact key the put replaced. The CTO withdrew R-36 on the measurement (msg 25331).
- Mechanism: two writers of one key. This seat's producer (crosswalk.py with universe/v1 as a second registration source) lived only
  on closer/amgt-peers-z-20260924; CLOUD's builder knew registrations.json alone (36 MEASURED). This seat's own COO half counted ONE
  writer (NEVER-1: count the writers first) -- recorded against this seat.
- Restore, on the CTO's GO (25331, method confirmed 25337, no new pair -- the existing pair's rollback leg): bucket versioning is
  Enabled; server-side copy_object of the signed VersionId K1qTvwqiuo3jNvF_bwC94m1P0J5vHtwS onto the key at 08:22:33Z. No delete, no
  local bytes; the 20 fire versions stay addressable. VERIFY-AFTER 3 of 3: size 523,207, ETag 2c0ff894..., sha256 9bd953b9...;
  ASML MEASURED/absent/SERVED, AAPL derived 10 SERVED, CAT derived 12 (control). 3.0.0_SA_CVO~Z verified independently and ran the
  negative arm (NOSUCHKEY_ZZ_Equity -> UNRESOLVED) this seat had not named. CTO ledger amgt-crosswalk-0924-rollback CLOSED.
- Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_EXPERIENCE/CROSSWALK_RESTORE_20260924T0822Z/` @ea8b7ea023.
- Preconditions on the induction re-fire, per the CTO (R-40): (1) rollback MET; (2) one producer on CLOUD -- 0.0.0_AB_MSTR~Z merged
  the closer branch @0800e89f30, but COO~X's in-memory build proved add_security's CALL PATH does not pass the universe input
  (crosswalk.py:644-646 explicit argument; add_security.py:175 and :392 call it bare) -> NOT MET; (3) write_pool ONE put per run --
  OPEN; (4) the universe input passed on add_security's path -- OPEN. (3)+(4) are ONE closer cell on this seat's surface, confirmed
  by the CTO; acceptance is COO~X's discriminator verbatim (in-memory 194 before / 194+N after N fake registrations / 36 with the
  universe withheld; exactly ONE new version per run at the re-fire, N>1 names). Build starts after the wave-2 drains (section 3).

## 2. Round 37 wave 1 -- seven cells drained, 08:4xZ-09:4xZ

Every drain: instance re-validated inside the worker's worktree; portal branch merged into the shared portal DEV; the six-state
contract check run against the shared vite (5175) and its outputs committed under `deliverables/2.0.0_SA_COO~Z/round37/contract-check-after-rl-N/`;
outer safe-merge (stops on the portal gitlink, and from rl-6 on the append-only channel too -- resolved by taking HEAD whole and
appending the worker's rows, the gitlink set by hash); issuer close-out written into the order's record face (status complete).

| cell | worker | outer drain | close-out | portal DEV | contract check movement |
|---|---|---|---|---|---|
| rl-2 shell + identity header | ~131 | 973dc1cf5d | 42667f7f2f | ce3c907a | band thesis 4->3, others 3->2 |
| rl-3 thesis ladder | ~132 | a8aa8bff17 | e8b909f937 | cd1a7146 | thesis band 3->2, lowContrast 185->PASS |
| rl-4 exec management | ~133 | 2488c1bf0d | 9fd81fb52c | ae1b9f42 | none (shared chrome) |
| rl-5 peers present columns | ~134 | 5a24b4612f | 894631e0a9 | 897a0bbf | peers band -> PASS |
| rl-6 model sheet | ~135 | 75591cc1b9 | 7dda7167be | ccdb8699 | model lowContrast PASS -> 37 (row Z-S247) |
| rl-7 posture | ~136 | 6d2c73459b | b1d42fb62b | f67117d4 | posture lowContrast 7 -> PASS |
| rl-8 lead panel | ~137 | 6b1f1d838d | ca52fa60c1 | ae760a39 + 1267a67e | list purpleFills 4->3, band 2->3 |

Wave-wide state at the last read (contract-check-after-rl-8): weights [300,500,600], sizes [10], radii ["8px"], shadows 1 on every
state; purpleFills list 3 / others 4; band list 3 / peers 1 / others 2; lowContrast model 37. Those are rl-9's (the one cell admitted
to every page file; its criterion is the six-state PASS).

Issuer moves at the drains, all recorded in the close-outs: the tabs.harness.cjs loader stubs (PanelFooter, Segmented, HelperTip;
portal 1267a67e) so the shared harness loads over the merged page -- with them it reads CHECKS-WRONG-WAY on three pre-round
assertions (peers_csc_table_absent_marked, short_read_refused, generation_captions_present), routed to rl-9's AC3; row
AMGT_RESAPP-Z-S247 (model low contrast) with disarm owner the issuer per R-18 (the gate refuses a worker serial as owner).

Worker rows merged: W135-S1 (INERT), W136-S1 (INERT), W137-S1 (ARMED -> resolved by the stubs), W137-S2 (INERT).

Wave-1 worktrees and branches removed after the drains (7 of 7, both repositories).

## 3. Wave 2 spawned 09:5xZ

rl-9 (`0.9.0_WK_AMGT_RESAPP~138`, worktree C:/tmp/wk-amgt-37-138) and rl-10 (`~139`, C:/tmp/wk-amgt-37-139), both from CLOUD
ca52fa60c1 with portal 1267a67e, node_modules linked. rl-9's prompt carries the fixtures path (Z-S244), row Z-S247, the last
contract-check read and the three wrong-way tabs assertions; rl-10's carries the loader note.

## 4. Lessons banked (memory, this device)

- a-served-key-with-a-producer-on-an-unmerged-branch-has-a-second-writer-on-the-trunk
- a-surprise-row-names-the-issuer-as-disarm-owner-never-a-worker (and: grounding is an OBJECT; capture a refusal log whole)
