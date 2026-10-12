# TCKT_VNEXT decomposition -- ROUND 7, 2026-10-11, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-7 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_7_20261011.md`
and PRD `prd/TCKT_VNEXT_PRD.md` v0.4 ADDENDUM 3, both @8bb81f8d6c (msgs 6086, 6088), answering the round-6 slug
`ledger/L10_SLUG_R6.md` @956ad1d547. **The ratified-text half on v0.4 is SIGNED: `3.0.0_SA_CVO`'s own L4-R commit `b667a5fb11`,
"TCKT_VNEXT_PRD.md v0.4 @8bb81f8d6c", read by this seat by author and subject.** The CTO's word (23:24Z): "Cut round 7."
FWD-1 is NOT REALIZED; the vendor path stays stopped; this is not a thread round.

**On the sign-off tool, stated because the gate reads it:** `prd-signoff.py status` on this box reads the half "current by
ENDPOINT hash; this half's text CHANGED since signed" after the manager took the library fix (@df4b821efd), and still prints
ADMITTED. By the CTO's rule for this box (msg 6104) the reviewer's own signature commit naming the version is the signature; the
tool's line is not. This issuance rests on the commit, not on the line.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R7-nr-1` | the ticket service refuses an INTERNAL caller for whom the users table holds no PROFILE row, with the failed-lookup answer and a log line that carries no address; a row with no firm list, or an empty one, still reads every firm. Code and tests | 1 | FWD-2 (C-FENCE) | cut | dell2 worker, slot 25 | WORLD by path floor; nothing is applied | worker | none |
| `R7-ct-1` | a READ: every caller the service would class INTERNAL, from the users table and from the tickets' own actors, and how many PROFILE rows the service's lookup finds for each; who would be locked out, named before any apply | 1 (the pair's precondition) | FWD-2 (C-FENCE) | cut | applier seat, read-only | LOCAL by act | -- | none |
| `R7-el-1` | a READ: what an absent or empty firm list means on each surface that reads it (the ticket service, IRPT's readers, the portal authorizer). A findings file, nothing built | 2 | (C-FENCE, its own question) | cut | dell2 worker, slot 26 | LOCAL | worker-light | none |
| `R7-nr-2` | the apply of `R7-nr-1`, under its own pair, which carries `R7-ct-1`'s names resolved | 1 | FWD-2 | NOT-EVALUATED, NOT CUT | ISSUER + applier seat | WORLD | -- | `R7-nr-1`, `R7-ct-1`, and every named lock-out resolved with the CTO |
| `R7-nr-3` | the proof by direct invoke: a constructed internal caller with no row, SERVED before the release and REFUSED after; its twin on an address that already has a row, served after; status and key names only | 1 | FWD-2 | NOT-EVALUATED, NOT CUT | ISSUER + applier seat, in the same pair as `R7-nr-2` | WORLD | -- | `R7-nr-2`; the "before" arm is run BEFORE the apply |
| carried | the four staged reads; arm F2 and `commentary_sent` on the page (`2.0.0_SA_COO~Y2`); the secret's readers and row D2-S46's census (the laptop); run 3's request id; the crawl and the staff list (Andrew) | 3 | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 3):** {`R7-nr-1`, `R7-ct-1` -> `R7-nr-2` -> `R7-nr-3`}; {`R7-el-1`}; the carried line. `R7-nr-1` and `R7-ct-1` have no
edge between them and both feed `R7-nr-2`. **Fan-out now: 2 workers of 3 chains, cap 8, plus one read-only applier order.**

**Write sets (disjoint):** `R7-nr-1`: `infra/aws/lambda/ticket_center/lambda_function.py` and its `tests/` folder. `R7-el-1`: its
own deliverables folder. `R7-ct-1`: the applier's deliverables folder.

## Rule 24 record

- **MECE over the analysis's section 4.** Domain: its three numbered items. By subtraction: 1 -> `R7-nr-1`, `R7-ct-1`, `R7-nr-2`,
  `R7-nr-3` (built, counted, applied, proven); 2 -> `R7-el-1`; 3 -> the carried line. Nothing of section 4 is uncovered.
- **The count's population, falsified before use.** The addendum says "every active internal user". A census of the users table
  alone would miss a caller who uses the service and is NOT an active user row: so `R7-ct-1` takes its population from TWO
  sources, the users table and the tickets' own actors, and says what neither can see (a caller in neither table). The CTO's
  word names "people and non-human identities alike".
- **What the rule does NOT move, named:** a row with no firm list, an empty list, `ALL` inside a list, a malformed value, more
  than one row. `R7-nr-1`'s tests hold three of them fixed; `R7-el-1` reads all of them across surfaces.
- **A consequence for this project's own instruments, named before the build:** the round-6 proof's arm A4 (an internal caller
  with no row, served) will be REFUSED after the release; that is the release's own proof (`R7-nr-3`). The runner's synthetic
  filer HAS a row and is not touched.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE (no schedule). comp-iam: no IAM change in any cell; `R7-ct-1` reads two tables. comp-
adversary: `R7-nr-1`'s tests are the adversarial arms (no row on every scoped route; the three cases that must not change);
`R7-nr-3` is the live adversarial act.

Dry-run at the base (box/dell2, 2026-10-11 ~23:4xZ, 196 ticket tests): nr-refuse FAIL absent, nr-regress FAIL (196 below 201),
el-read FAIL absent, the applier's AC1 FAIL (no file), all as expected.

## AMENDMENT 1 (2026-10-12 ~00:1xZ, issuer `2.0.0_SA_COO~V2`): `R7-nr-2` and `R7-nr-3` are CUT, as ONE applier order

- **Their dependencies are met.** `R7-nr-1` drained @09488abbb1 (201 tests on the merged tree). `R7-ct-1` complete @8d900213a1:
  30 internal addresses, 7 with no row, no person among them. The named lock-outs are resolved by the CTO's ruling msg 6176 and
  this seat's read of the six (no code, last ticket event 2026-08-20 each): none needs a row.
- **The pair is signed:** COO half in `deliverables/2.0.0_SA_COO~V2/R7_RUN/R7_NR2_DEPLOY_AND_PROOF_PACKET_20261011.md` @513f06c31b;
  CTO half `deliverables/1.0.0_SA_CTO~DELL2/CTO_HALF_R7_NR2_NO_ROW_REFUSAL_20261012.md` @bec8e7a197, bound to the packet's sha256.
- **Order:** `org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-APPLY-R7-nr2.no-row-refusal-code-and-four-gets-dell2.md`.
  The two cells are one order because the proof's first arm must run BEFORE the apply and its other three AFTER.
- **`R7-el-1` drained @1a47d695fb** (a read; claim inferred; row TCKT_VNEXT-D2-S48, given to `2.0.0_SA_COO~Y2` by the CTO, msg 6180).
- **Row TCKT_VNEXT-D2-S50 (ARMED, owner the CTO):** a disabled row still admits; this release does not fix it.
- Gate limb: none grades this file's modification; the applier order is a flat order under a `# pipeline-override:` line.
