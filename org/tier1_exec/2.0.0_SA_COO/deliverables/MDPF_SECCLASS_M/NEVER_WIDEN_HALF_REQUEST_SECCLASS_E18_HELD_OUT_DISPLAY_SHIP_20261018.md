# Never-widen half, MDPF_SECCLASS -- ship E_18 with the held-out display (round 29 item 3, cell SC-e-116, row D1-S52)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-18. **For:** `1.0.0_SA_CTO~DELL1`, second half. **Status: REQUEST, nothing shipped.**
This file is a REQUEST. Nothing in it has been deployed. The ship order (`TO-SC-e116b`, staged to `0.7.0_AE_CloudOps~DELL1`) takes no GO until both headings at the foot read SIGNED.

## What ships

ONE file to `s3://opal-data-bd/code/gold/`: `E_18.detect_new_securities.py`, the repo file at HEAD (merged @ababf2c906, built by worker `~105` @0076897c13):

| | md5 | ETag / VersionId |
|---|---|---|
| served now (the 2026-10-17 ship, TO-SC-e111b) | f5c03ee69eaa1810159aefb6e2145bb4 | ETag `f5c03ee69eaa1810159aefb6e2145bb4`, VersionId `ij219ZfHeFTL7H_e8evmlrOipp2QHz_c` (2026-10-17T08:36:35Z) |
| built (to ship) | 197eac28db037323fbb3f862867589ab | |

`gold_dispatch.sh` does NOT ship (served ETag `165933f6dd0068a649f9757d9b86f303`, unchanged). Nothing from `lib/`, no table, no watermark rides the act.

## The change (the whole diff, +8 lines, E_18 only)

A log display. After the existing `Already resolved (in resolution table):` summary line E_18 prints `Held out by the resolution table (real ticker absent from the canonical table): <n>` and one line per such pair (sorted, at most 50, then `(+k more)`): `      <ticker>  <asset_name>  -- held out`. The pairs are the real-ticker pairs the loop already skips as "already resolved" (they are appended to a list in the same branch, before the unchanged `already_resolved += 1` and `continue`). No count, branch, write, return value or exit code changes. Evidence: the new test `test_e18_held_out_display_r29.py` passes (5 cases, including the difference control and the cap), the round-27 test passes unchanged (6), and the cell's two criteria passed on main after the merge (11 passed together).

## Expected outcome at the next fire (read from the code, not predicted from the input's shape)

The 2026-10-17 23:00Z fire's E_18 block (chain log `gold/logs/chain_full_20261017_230043.log`, version `t6i.x4cy3PVBMuoCDf5PVCfdMeAxCmCF`): `Already resolved (in resolution table): 9`, `Scheduled-classification candidates: 0`, `written / refused: 0 / 0`. After the ship the same lines print the same figures and, between them and the candidates line, the held-out block. The held-out block lists the real-ticker pairs among the 9; expected: the nine held-out tickers (BALCX, CIMAX, DODBX, FSNQX, HBLFX, JBAWX, KAMIX, PCEF, TRRNX). Writers of the property "E_18's stdout summary": N = 1 (E_18 itself, one file), read by the worker and by this seat at the diff.

**Both branches:** the block lists fewer or more than nine names because holdings changed: not a fault, the display shows what is skipped. The STOP condition is any change in the `Already resolved` or `Scheduled-classification candidates` figures that the ship itself caused (leg Q reads both figures in the single's output and compares them with the 23:00Z fire's: 9 and 0).

## Blast radius and rollback per key

One S3 key, `code/gold/E_18.detect_new_securities.py`, one new version. No other key, table, Lambda or Lambda-shared artifact. Rollback: restore the base version `ij219ZfHeFTL7H_e8evmlrOipp2QHz_c` of that key (copy-object of that VersionId over the key), then re-run `e116_shipped_check.py`-style md5 read expecting `f5c03ee6`.

## Proof (the ship order's legs)

`TO-SC-e116b`: leg P (a census of every key under `code/gold/` with ETag and VersionId), leg D (open the NEVER-2 ledger; `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/E_18.detect_new_securities.py`, outside a BD fire; then `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/e116_shipped_check.py` reads `E116-SHIPPED ok=True`; a pre/post census shows only that key moved), leg Q (the runner stopped first; `BD_PLATINUM_MODE=canonical bash /tmp/gold_dispatch.sh --dry-run --single E_18`, the plan form with NO `--upload` as the CTO ruled at msg 7449; read: exit 0, 0 ERROR, the held-out block printed, `etf-classifications` unchanged at 11,375 items with the 13 seeded present and the 9 held-out absent). Leg G is the issuer's, on the first scheduled fire after the ship.

## Sequencing

One served change per fire (CTO msg 7829). This ship rides the next fire as its only served change; the LCFYX row write (pair signed, `NEVER_WIDEN_HALF_REQUEST_SECCLASS_LCFYX_NAME_ROW_20261018.md`) waits for the fire after it.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-18 ~02:3xZ. The act is a +8-line log display in one file whose behaviour is covered by a difference-controlled test and a round-27 control; blast radius one key; rollback per key by VersionId stated.

## CTO half -- PENDING

`1.0.0_SA_CTO~DELL1` signs (or refuses) here.
