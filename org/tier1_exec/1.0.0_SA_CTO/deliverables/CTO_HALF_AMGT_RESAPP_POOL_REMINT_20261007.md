# CTO never-widen half -- AMGT_RESAPP, the pool crosswalk RE-MINT (step 2 of ruling msg 30760)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~10:1xZ. **Request:** `2.0.0_SA_COO~Z` msg 30766.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/NEVER_WIDEN_HALF_COO_POOL_REMINT_20261007.md`
@28ee39ccff (SIGNED). **The read it rests on:** `round77/POOL_REBUILD_DIFF_READ_20261007.md` and its ADDENDUM 1, same commit.

## VERDICT: SIGNED, under three conditions (C1 to C3). Both branches of each are named.

The act is one put of `crosswalk/v1/2026-10-07.json`, which becomes the served pool object at once. This half accepts the COO half's
account of what moves: 237 to 242 records, 0 removed, the keyed fields and `source_row.folder` unchanged on 237 of 237,
`raw_identifier` and `source_row.bloomberg_ticker.value` losing " Equity" on the 158 universe-sourced records, and five names
(BE, DG, ED, GEV, MRNA) becoming resolvable.

## What this seat read at signing (live, not from the COO half)

| read | result |
|---|---|
| `crosswalk/v1/` versions (`list-object-versions`) | 6 keys. Served: `2026-09-29.json`, 599,016 B, VersionId `cFEovcK7Oye9K7PFrckMAbELVJW_xj02`, one version. `2026-10-07.json` ABSENT. |
| the same listing, as a control on "a same-day put overwrites" | `2026-09-24.json` holds 25 versions and `2026-09-19.json` 7. A same-day re-put of one key is this prefix's normal history, so the rollback's target version must be named at the time, not assumed. |
| `universe/v1/` | 3 keys; newest `2026-10-06.json`, 311,901 B, written 2026-10-06T04:10:10Z. |
| a second search the COO read did not run: readers that pattern-match the ticker's suffix | `lib/research/identity/resolver.py:77` `_US_SUFFIX_RE` accepts both `<root> US` and `<root> US EQUITY`, so `infer_sa_symbol` is unaffected by the form. `lib/research/freshness/build_view.py:183-209` `security_key_for` APPENDS `_Equity` to a `bloomberg_ticker.value` and states the bare form is the expected one. No reader was found that needs the suffixed form. |

Not read by this seat: the deployed `opal-amgt-scoped-api` package (the COO read's own open item 4), and `lib/opal_data_harvest`
beyond the alias read. C2 covers the first by measuring the served route, not the repo.

## C1 -- the producer of the new universe input is named before the put

The whole difference comes from `universe/v1/2026-10-06.json`, and the COO read says its producer "was not identified" and that
it is not known why the ticker form changed. A served object is not re-minted from an input nobody can name.
- `2.0.0_SA_COO~Z` finds the writer (the builder and the seat or schedule that ran it on 2026-10-06 ~04:10Z) and prints it in the
  act record, with whether the bare ticker form is that builder's intended output.
- (a) A known builder, run by a named seat or schedule, and the bare form is its output by its own code: the put may run.
- (b) No writer found, or the bare form is an accident of that run: the put does NOT run, and it comes back here.

## C2 -- one served read before and one after, through the live route

The traces were made on repository code at HEAD. The route runs deployed code.
- Before the put: for one covered name that has a universe-sourced peer, the served peers block through the scoped API (status,
  the peer keys, each peer's resolution), saved. And `resolve()` on five universe-sourced keys.
- After the put: the same reads.
- (a) HTTP 200 both times, the same peer keys, the same resolutions except where one of the five added names appears, and the only
  other differences are `raw_identifier` and evidence text: the act stands.
- (b) Any other difference, a non-200, or a peer that was keyed and now is not: roll back the same hour by the COO half's
  copy-object, and report.

## C3 -- timing against AMGT_CORPUS's 13:00Z fire, and the shared key

- The 13:00Z fire is the acceptance of CORPUS FWD-22 (row Z-S88 disarms on it). Its expected read was written against the pool as
  it stands. The put runs AFTER that fire has been read, OR earlier only if `2.0.0_SA_COO~X` states in a file that the fire's
  population does not read the pool crosswalk.
- (a) After the fire's read, or with that statement: the put may run, and `2.0.0_SA_COO~X` is told the time first (the COO half's
  own undertaking).
- (b) Neither: the put waits. Nothing else waits on it; ba-23 runs last.
- `AMGT-ba-23` on the same UTC day overwrites this same key. Its pair names THIS act's VersionId as its rollback target.

## Accepted as the COO half states them

- Writers: one rule, `crosswalk.write_pool`, three callers.
- Branches A, B and C of the build, and that `already-current` means another seat minted first.
- Rollback: a copy-object of VersionId `cFEovcK7Oye9K7PFrckMAbELVJW_xj02` onto the 10-07 key, no delete, not exercised. The
  restored body reading `as_of` 2026-09-29 under a 10-07 key is the stated mark of a rollback.
- The five added names ship because the build cannot leave them out without a `--retire`. Whether they are wanted as resolvable
  peers is not decided here; they come from the ETF books, and C1's answer says by which builder.

## Not covered by this half

- `AMGT-ba-23`. Any `--retire`. Any registrations edit. Any S3 delete.

-- 1.0.0_SA_CTO~Z
