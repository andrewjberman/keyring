# COMM_ASSIST decomposition -- round 20: the dell2 pick-up of the per-draft rows, a narrower package, one test batch (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-15 ~07:3xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s round-19 analysis `ledger/ROUND_ANALYSIS.round19.md` @b4f6d499d0 (msg 109356), over PRD v0.10 (ratified-text half SIGNED, current by ENDPOINT hash). The CVO's L10 slug `adjudications/ADJUDICATION_v9.md` @911adc8994 closed round 19: 4 of 4 orders complete, six rows dismissed with reason, nothing BLOCKING or ARMED.
The standing direction: the laptop drives COMM_ASSIST at normal pace (Andrew ~18:4xZ on 2026-10-14, CTO msg 109206).

**The analysis's three enrichment items and what the issuer does with each.**

1. The dell2 per-draft pick-up, as a crossbox read-only order (ruling 1) -> cell `CA-l-1`.
2. `build.sh` packages only the registry files the assistant reads (ruling 2) -> cell `CA-l-2`, then its deploy `CA-l-4` (NAMED, cut at the merge: a WORLD act with its own halves).
3. One batch: the three sibling tests with the bare-import defect (ruling 4) -> cell `CA-l-3`.
Not cut by ruling: the rollback reconcile of `pending_list` against `pending` (ruling 3); FWD-12 (waits on Andrew's period). `CA-k-5` (FWD-13's exercise) is cut the moment muse reports its three pieces built, not before (rulings 1 and the enrichment list's note): NAMED here, not cut; no cell waits idle on it.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-l-1` | dell2's reader seat confirms its checkout holds the CA-k-1 reader, starts the EXISTING task once, and reads the folder back; the issuer's `check_m1_perdraft.py` runs ON dell2 (one `drafts` row per open mail draft, distinct `seq`) beside `check_k4_folder.py` | FWD-13, FWD-4 | SERVED (read-only, another box) | crossbox ORDER to `0.7.0_AE_CloudOps~CA2`, workstream DELL2PERDRAFT | CA-k-1 merged (on `origin/box/dell2`) |
| `CA-l-2` | `build.sh` copies the registry files named in a new manifest `registry_files.txt` (twelve) instead of the whole directory (seventeen); the 17 equivalence probes still pass | FWD-4, FWD-13 (every deploy carries less foreign payload) | WORLD (inferred floor for an edit under infra/; edit only, deploys nothing) | chain 0, workstream BUILDNARROW, slot ~30 | none |
| `CA-l-3` | the three sibling tests (`jobs`, `eod_republish`, `stale_eod`) put the tests directory on `sys.path` before the bare sibling import; no product change | none of its own (hygiene) | LOCAL | chain 1, workstream SIBLINGIMPORT, slot ~31 | none |
| `CA-l-4` | DEPLOY of CA-l-2 (a targeted apply of `module.ldo_001`, code only: a smaller package), its own never-widen set | FWD-4, FWD-13 | WORLD | the CloudOps seat | CA-l-2 merged; halves |
| `CA-k-5` | FWD-13's exercise (restates CA-j-16): one real Teams item and one real C-MAIL mail each reach Andrew as a muse alert within 30 minutes, one not-for-him item none | FWD-13 | SERVED | needs muse's three pieces and Andrew's calls 44eb and e435 | muse built; Andrew's acts |

`fanout: 3 of 3 chains, cap 8, reason: CA-l-1 is an order to another box that changes nothing in the repository (its write set is its own deliverables folder); CA-l-2 writes infra/aws/lambda/teams-chat-assist/build.sh and registry_files.txt; CA-l-3 writes three test files; the write surfaces are disjoint, and none depends on another. CA-l-4 waits on CA-l-2's merge and its halves; CA-k-5 waits on muse and on Andrew.`

**Rule 24.** Domain: the analysis's enrichment items 1 to 3 (denominator 3). Item 1 is CA-l-1; item 2 is CA-l-2 (and CA-l-4); item 3 is CA-l-3. None uncovered. The rulings that cut nothing (3 and 5) are named above.

**Why CA-l-2 uses a manifest and not a rule.** The issuer measured that `lib/opal_naming.py` never globs the registry in packaged code: `load_registry()` opens a fixed tuple of eleven names, and `mail_requests.py` opens `mail_parties.json` by path; the other packaged readers (`registry_hash`, `registry_file_names`) are reached only by the CLI and the generator. A trace of the 17 probes plus a static scan of the packaged code gives twelve files; five (`catalog_fork_keys`, `event_rules`, `key_rulings`, `name_rulings`, `root_map`, about 690 KB of 1.09 MB) are never opened. A manifest makes the assistant's reads explicit, so an edit that starts a new read must name the file (the manifest header says so). The residual the check cannot see: a registry file opened lazily on a path the probes do not exercise; the deploy cell re-runs the equivalence probes against the live package for exactly that reason.

**Issuer checks (written first; base FAIL, green on a scratch reference removed afterwards; each finds the repository from the current directory's git toplevel, never from its own file location):**
`CA-l-1` -> `r20/checks/check_m1_perdraft.py` (`M1-PERDRAFT`): 6 of 6 on the trunk, 3 of 6 against `refresh.py` as of `ad67a9b9a4` (the reader before CA-k-1); the seam `M1_REFRESH` points it at another copy.
`CA-l-2` -> `r20/checks/check_m2_build.py` (`M2-BUILD`): base 3 of 7, scratch reference 7 of 7 (LF and CRLF manifest); four negative controls (omit `firm_pages.json`: `trace_equal` fails; omit `scopes.json`: `trace_equal` and `probes_same`; add `root_map.json`: `trace_equal` and `no_unreferenced`; add `catalog_fork_keys.json`: those and `foreign_absent`).
`CA-l-3` -> `r20/checks/check_m3_batch.py` (`M3-BATCH`): base 2 of 6 (the three `alone` arms and `combined` fail), scratch reference 5 of 5 (`no_product_change` skipped in a non-git mirror and biting in a worktree), negative control (a renamed test) fails `names`.

**The issuer's real runs at close:** after CA-l-1, the dell2 seat's own deciding lines plus the counts of `drafts.json` rows and distinct objects; after CA-l-4, `check_l4_equiv`-style probes and a served-code read of the new package's registry file list against the manifest (the live package carries twelve registry files, not seventeen), the dead-letter queue unchanged, and the mode still `enforce`. CA-l-3 is tests only and needs no real run; CA-l-2 is an edit (declared WORLD by the gate's inferred floor for an `infra/` path) whose real run is the CA-l-4 deploy above.
