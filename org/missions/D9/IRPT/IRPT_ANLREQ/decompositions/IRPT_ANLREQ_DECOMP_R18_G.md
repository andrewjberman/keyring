# IRPT_ANLREQ round 18, workstream ~G (ENGINE) -- decomposition: the source of resident release r32

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** CTO msg 8568 (ruling `CTO_RULING_DELL2_ANLREQ_PROD_PROMOTE_RELEASE_AFTER_FWD1_WINDOW2_20261015.md` ADDENDUM 2 @87fe24c71d: the ONE resident release carries `irpt-anlreq-x10-v1` and run 3's new producer address), `~Y2` msg 8570 (the address: `fwd1-staff-r41b@opal.invalid`; the list must read exactly `("andrew@opalinvest.com", "fwd1-staff-r41b@opal.invalid")`, r41a leaving in the same edit, with the list's comment, the pinned test and the installer's second check agreeing), the merged cells `AR-g-85` (`002a88bdc3`, per-variant map selection), `AR-g-87` (`38620fe9f2`, the commentary revision), `AR-g-90` (`ce2256554b`, the `opal_pricing` binding), the issuer's reference build.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Source now, delivery later.** r32 is ONE artifact under ONE never-widen pair. This round makes its source: the builder and the producer list, with their tests. Building the delivered tarball at the merge pin, the pair (COO half from this seat, CTO half from `1.0.0_SA_CTO~DELL2`), the CloudOps apply and the change-ledger entry are the release act that follows the merge. They are not cut as a worker cell: a worker has no send tool and must not build for delivery.
- **The three maps.** The Comparison and Multi-Comp maps are pinned beside the Overview with their own binding names (`opal_map_comparison`, `opal_map_multicomp`), the names `AR-g-85`'s loader reads. Map bytes are unchanged (the layout fix `AR-g-88` is in the engine, not the map), so the Overview pin stays `21a8f6d690bb...`.
- **Pricing ships OFF.** The bindings carry `opal_pricing` with `enabled` false. The host has no pandas, pyarrow or yfinance, and the DEMQUE and YCharts grants are unruled; switching pricing on is a bindings edit after those are in. r32 therefore changes which map an Opal report uses and who is routed to Opal, not what a report's figures are.
- **The builder takes the price modules without a change.** It packages every tracked file of `ycharts/research` except tests and fixtures; the eight new modules are in. The tarball test names them so a later exclusion would fail.
- **Reproducibility is asserted on members and bindings,** not on the tarball's own hash: the gzip header carries the build time.
- **Not in r32:** the YCharts and DEMQUE price tiers, the swap for an unpriced symbol, the benchmark and risk-free series, `lib/trading_calendar.py` (T-1 comes from the clock).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-91` | `resident_worker.py`: the list reads andrew and r41b; `build_resident_package.py`: two map members and bindings, `opal_pricing` off, `built_by`; the three list-pinning tests edited by the address; `tests/test_resident_r32_source.py` (5 named tests) | the six product files named in the order + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain; every dependency is merged. Round 17's `AR-g-90` merged `ce2256554b`.

## After the merge (the release act, in this order)

1. Re-run the three gates on the merged tree (g91 and its regress, `ar_g90`, `ar_g85`), then read the merge pin.
2. Build the tarball at that pin with the builder (`MSYS_NO_PATHCONV=1`, a Windows-form worktree path, the wrapper and library sha256 of the host's pinned files), record its sha256 and member count.
3. Draft the COO half of the never-widen pair: blast radius = the producer list (r41a leaves, r41b enters), the per-variant map selection (Comparison and Multi-Comp records render their own map instead of refusing), the commentary revision (the package attach), pricing off; rollback = the previous tarball (r31) re-applied. Send it to `1.0.0_SA_CTO~DELL2` for its half; message `~Y2` when the build is staged and when it is applied.

## Four-postulate record

(i) Domain: what the resident package contains and who the resident routes to the Opal producer. (ii) One builder, one list. (iii) One intent: r32's source is complete and tested. (iv) What this cut does NOT move: any deployed byte, the delivered tarball, IAM, the host, pricing.

fanout: 1 of 1 chain, cap 8, reason: one builder file, one list file and their tests; slot 193.
