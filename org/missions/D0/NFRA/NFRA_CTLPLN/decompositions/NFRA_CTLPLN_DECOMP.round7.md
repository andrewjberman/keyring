# NFRA_CTLPLN decomposition -- round 7: exercise what is built, stop dell1's unguarded download, register the firm-set module (issuer 2.0.0_SA_COO~C; cut 2026-10-12)

**Status: ISSUED in one issuance (two worker orders and one staged seat order, plus the issuer acts below). FROZEN at the cut.**

**Input.** The L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round6.md` (1.0.0_SA_CTO msg 108476), section 4: E1-E8
as the 2026-10-09 analysis lists them, plus E9 (FWD-27), E10 (FWD-28) and E11 (D1-S8). Cut on PRD v0.25. Round 6 closed first:
`python .tools/round-close-check.py --project NFRA_CTLPLN --round 6` reads `verdict=MAY-CLOSE`, proof_bad 0, judgments 4 of 4 graded
(`TO-CT-x-2` superseded with its FAILED-WITH-ROW disposition, `TO-DELL-1` withdrawn, both per the analysis section 2).

## Measured at the base (issuer, 2026-10-12 ~07:0xZ, box/laptop)

1. **E1 read, already true:** `python .tools/thread-trace.py --project LGIC_BLANKFIX --round 9 --fetch` prints `HOP 1..5` all found and
   `THREAD project=LGIC_BLANKFIX round=9 hops=5/5 pushed_by_working_box=False elapsed=2h14m23s` (plan by `2.0.0_SA_COO~B1` on
   `origin/box/dell1` 2026-10-09T05:34Z; work by `0.9.0_WK_LGIC_BLANKFIX~1`; integrated by `0.0.0_AB_MSTR` on `origin/CLOUD`; graded by `3.0.0_SA_CVO`).
   The artifact is committed with this decomposition as `deliverables/2.0.0_SA_COO~C/E1_THREAD_TRACE_LGIC_BLANKFIX_R9.txt`.
2. **E2 done:** `TO-CT-x-1` complete @ef9332dbfd: read-back `ok=True` on commit d5cd8a81c4 (off trunk, scratch ref), refused IAM write real.
3. **E4:** `python .tools/crossbox-matrix.py` prints `CROSSBOX-MATRIX pairs=12 with_file=11 acked=9 closed_both=5 none=1`. The pair with no file is
   laptop->dell2. Two newest files are OPEN with no ack: dell2->laptop (`XB-20261012T024226Z-0dce`, to `0.7.0_AE_CloudOps~ANL`, a stood-down seat) and
   dell1->dell2 (`XB-20261012T033435Z-54b6`, to `2.0.0_SA_COO~P2`).
4. **E7:** `python .tools/seat-list.py show` reads `boxes=1 read=1 stale=laptop`: only the laptop publishes `seats.json`, and its file is older than 90 minutes.
5. **E3 premise:** row `NFRA_CTLPLN-D1-S1`: `python -m pip download ... --index-url https://pypi.org/simple` on dell1 returned rc=0 (NOT-BLOCKED).
6. **E8:** `box-sync-conflicts.py --since 2026-10-05 --fetch` did not finish in 110 s on the shared tree; the issuer reruns it in the background at the close.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-v-1` | `org/devices/kit_pip_no_egress.py`: the pip counterpart of `kit_bun_no_egress.py`. `measure` runs pip against two loopback listeners (an index that counts requests, a proxy that counts requests) in the order of proof, and finds which disarms (a config no-index, an env, a wrapper that refuses an explicit public `--index-url`) stop `python -m pip install/download` WITHOUT a request leaving the machine; `wrap` applies the passing form and refuses a registry verb, naming the laptop route. No request leaves the machine. | FWD-18 | WORLD by path floor (applies nothing) | `0.9.0_WK_NFRA_CTLPLN~63` |
| `CT-v-2` | A PROPOSAL, no change applied: where the firm-access sets for the two class-(i) data-proxy routes live in the `opal_naming` registry so the Lambda carries no hand-typed firm token (rule 30). Reads `lib/opal_naming.py` (VIEWS, WHOLE_FILE_TARGETS, the renderer table), `infra/logic/registry/`, `portal/src/lib/firmAccess.ts`, the CT-u-6 branch history; writes one proposal document with the exact registry rows, the generated target, the handler diff and the tests, and the open questions for the CTO. | FWD-28 | LOCAL | `~64` |
| `CT-v-3` | dell1, the click route finished: the issuer Taildrops the packed, checked click pack (act A3); the lane runs `intake_receive.py verify`, `prove`, `install` (into a fresh venv), the lane's work, counts outbound requests, applies the CT-v-1 form, and makes one deliberate install attempt that the form must stop and that names the laptop route. | FWD-15, FWD-17, FWD-18, FWD-19 | WORLD | `0.7.0_AE_CloudOps~CT1` (dell1), staged until CT-v-1 is merged and the pack has arrived |

E9 (FWD-27) is served by the orders ALREADY issued in workstream REMOTE round 1: `CT-u-1`, `CT-u-2` (complete), `CT-u-3`, `CT-u-4`, `CT-u-5` (staged on Andrew's
keys and his elevated lines). E10's apply is `CT-u-7` (complete); its second half is `CT-v-2` here. E11 (D1-S8) is the CVO's act when `CT-u-3/4/5` are terminal.

## Rule 24

**Domain:** the eleven items E1-E11.

| item | served by |
|---|---|
| E1 | measured at the base (1 above), artifact committed with this cut; no cell |
| E2 | `TO-CT-x-1`, complete |
| E3 | `CT-v-1` (the stop), `CT-v-3` (the route), issuer act A3 (the pack and the Taildrop; read aloud to Andrew) |
| E4 | issuer act A4 (one CALL laptop->dell2 through `0.0.0_AB_MSTR`; the two OPEN files are read, their owners asked through their managers) |
| E5 | `TO-CT-t-3`, complete (the census and the moves); no cell |
| E6 | issuer act A6 (the CVO reads XB-20261008T203134Z-a3f0; Andrew reads `open-calls.py list --all --cloud` once) |
| E7 | issuer act A7 (each box's manager runs `seat-list.py write`; one real spawn of each seat kind is asked of MSTR); `TO-CT-t-4`, complete, is the manager-day read |
| E8 | issuer act A8 (`box-sync-conflicts.py` at the close; one HELD-DEPLOY line from a box push carrying an unnamed pipeline script) |
| E9 | `CT-u-1..5` already issued |
| E10 | `CT-u-7` complete; `CT-v-2` |
| E11 | the CVO's act at the drain |

No item is unowned. **Same grain / one intent each.** **State coherence:** `CT-v-1` and `CT-v-2` change nothing on any machine except new files in this repo; `CT-v-3` changes dell1's pip behaviour by the CT-v-1 form and installs one package into a venv.

## Dependency chains and fan-out

- Chain A: `CT-v-1` then `CT-v-3` (the seat order consumes the kit). Chain B: `CT-v-2` alone. M = 2 chains; N = 2 workers (`~63`, `~64`). The seat order is not a worker.

`fanout: 2 of 2 chains, cap 8, reason: the pip kit (chain A head) and the registry proposal are independent builds; the dell1 exercise is a staged seat order behind the kit`

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A3:** build the click pack (`org/devices/intake/intake_check.py pack`, the CTO's signature already on file) and Taildrop it to dell1; hand `CT-v-3` its GO.
- **A4:** one `crossbox-call.py` CALL laptop->dell2 to `0.0.0_AB_MSTR~DELL2` asking an ack; ask `0.0.0_AB_MSTR` to have the two OPEN files read by their owners.
- **A6, A7, A8** as the table says; each carried through `0.0.0_AB_MSTR` (a cross-box ask goes to MSTR, never to a manager's inbox).
