# IRPT_ANLREQ round 28, workstream ~G (ENGINE) -- decomposition: the yfinance checker at the door, and the ~G2 half of C-HOP-FAILURE

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msg 8968 (the door's resolver is built with no yfinance checker: a real symbol YCharts omits and yfinance knows is filed TICKER_NOT_FOUND; `~G2` wires it; fold into r34 if its D1 has not started; FWD-1 run 3 waits), `~Y2` msg 8965 (row `IRPT_ANLREQ-D2-W165-S2`), CTO msgs 8907 and 8971 (PRD v0.20/v0.21 C-HOP-FAILURE: `~G2` owns `hop_failure` in `durable_job.py` and `resident_worker.py`, and the code and words in `status.py`/`owned_status.py`; `~T2` owns the commentary `fail` op and the Terraform cell for its role's narrow UpdateItem; `~V2` owns the ticket page read), `~T2` msg 8948 (the writer signature, answered), `~V2` msg 8974 (waits on the merged status shape). r33 is CLOSED (AQ2 msg 8976); r34's D1 has not started.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The checker fix is `AR-g-110`, one file** (`ycharts/session/resident_session.py`): `template_resolver` builds `YfinanceChecker()` unless a test injects one. The repository has exactly one non-test `SecurityResolver(` and one non-test `template_resolver(` caller, both in the resident; no Lambda path builds a resolver (answer to CTO ruling item 1, "any Lambda path").
- **r34 is rebuilt to carry it** (CTO ruling item 2). `AR-g-112` is the rebuild (worker, BUILD ONLY) at a new tooling commit made after `AR-g-110` merges: the files-from list gains `intake/yfinance_check.py` (a new member) and the delta becomes 8 changed, 4 added. The signed r34 packet and the staged AQ2 order are superseded and re-cut; the CTO re-signs. Nothing was installed.
- **The `hop_failure` resident writers ship in r35, not r34.** `AR-g-109` merges only AFTER the r34 pin (the build reads git objects at the pin, so a later merge cannot enter r34). Reason: run 3 waits only on the checker; the writers are dormant until the status reader and the commentary writer exist, and a bigger r34 re-opens the signed blast radius for no run-3 gain. The Lambda leg (irpt-status and the `durable_job.py` re-pin) and the resident leg (r35) are packeted together, with the simulate battery the CTO asked for on the commentary role (that Terraform cell is `~T2`'s).
- **Response shape of the failure (cell `AR-g-111`, cut next):** the closed failure code travels as the existing `public_reason_code` (`^[A-Z0-9_]+$`, no schema change); the words as the description of one safe `NONE` action; the failed step as the hop name inside the words table. No new envelope field.
- **The packager precheck the CTO ordered ("first check that the packager can write the attribute")** is answered from source: the resident host role's statement `JobStateAcceptanceAndRetainedIndexes` (`ycharts/resident.tf`) grants `dynamodb:UpdateItem` on `irpt-jobs` with no attribute condition. DECLARED, the live policy NOT read: the r35 apply order carries a simulator read.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-109` | `DynamoGenerationStore.mark_hop_failure` + `get_state` carrying `hop_failure`; the ready-signal and packager writers | `durable_job.py`, `resident_worker.py`, `resident_installed.py`, one test file | WORLD (floor of an infrastructure path; source only) |
| `AR-g-110` | the door's resolver built with the yfinance checker | `resident_session.py`, one test file | WORLD (as above) |

`AR-g-108` (the AQ2 apply of the resident) is re-issued against the rebuilt r34 after its pair is re-signed.

## Edges and chains

- THREE independent chains: `AR-g-109` (store and writers) and `AR-g-110` (the checker). Their successors are cut in LATER rounds because the gate allows one issuance per round: round 29 `AR-g-112` (the r34 rebuild; decomposition `IRPT_ANLREQ_DECOMP_R29_G.md`), then the apply `AR-g-108`; the status reader `AR-g-111` (it reads `get_state`'s `hop_failure` key through test fixtures, so it does not wait on `AR-g-109`'s merge) in round 30. The merge of `AR-g-109` waits for the r34 pin.

## Four-postulate record

(i) Domain: one resolver constructor; one job-row attribute with three writers (resident ready-send, packager, commentary [another seat's]); one status shape. (ii) One closed code set (`HOP_FAILURE_CODES`) read by writer and reader. (iii) One intent per cell. (iv) What this cut does NOT move: the signed r34 until it is re-signed, IAM, the commentary writer, the ticket page, the classifier.

fanout: 2 of 2 chains, cap 8, reason: workers 250 (AR-g-110) and 251 (AR-g-109) spawned now; the rebuild (AR-g-112) is round 29, the status reader (AR-g-111) round 30.
