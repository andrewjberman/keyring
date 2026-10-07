# CTO never-widen half -- NFRA_OPLGTW OG-rl-13, the opal-gateway r27 release

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~16:4xZ, in the place of `1.0.0_SA_CTO~O` (not live; ruling msgs 30779 and 30782).
**Ask:** `2.0.0_SA_COO~O` msg 31151, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-13_20261007.md`
@bda7fb88dc (COO half SIGNED in its section 6), read whole.
**Release sha signed:** `510c8cfed2c852946e3e57fb4dd1c0467e2f3a52`, on live `feddb37244`.

## VERDICT: SIGNED on `510c8cfed2`, with the ruling on section 4 (a) below as its one condition.

## What this seat read at signing (its own reads of the release commit)

| read | result |
|---|---|
| `git rev-list --count feddb37244..510c8cfed2`, and the parent | 1 commit; parent `feddb37244` |
| `git diff --stat feddb37244 510c8cfed2` | 5 files, +218/-8, all under `infra/aws/ec2/opal-gateway/`; 3 ship, 2 are tests |
| `app/audit.py`, changed lines | ONE allowlist entry: `"rivalfunds_view": {"day", "route", "fund"}`. Its comment states `verdict` and `days` are passed by the handlers and stay dropped. This is round-24 ruling R36 exactly: three keys and nothing else. |
| `app/rivalfunds_view.py`, changed lines | each of the audit call sites passes `bytes_returned`; the day page now names its route `page`. The response objects are built once and returned unchanged; no status, header or body line moves. |
| `app/integrations/opal_portal/integration.py`, changed lines | `generated_at` is appended as the LAST key `_manifest_date` tries, after the eight it tried before. A manifest that resolved before resolves the same. |

Not read by this seat: the worker's ANNOUNCE, the host, the test runs, the two verify scripts, the rehearsal's records.

## The ruling on section 4 (a) -- reading the concierge's principal key from the encrypted sign-in cache

**NOT allowed again. The decryption is not repeated in Phase B.**

- What was done: to exercise the status tool through its wrapper, a worker decrypted the gateway's own encrypted sign-in cache on
  the host, in memory, with the broker's key, and matched the concierge's account entry for its tenant and object ids. By its record:
  no network call, no token read, nothing written, nothing printed. The order named no source, so it was the worker's choice.
- Why not again: the cache holds every signed-in user's sign-in material. "I read only the account entries" is a statement about
  what the code looked at, made by the process holding the key that opens all of it. Nothing bounds a second read to the same
  entries except the same care. A release check is not a reason to open that store, and no order, pair or word of Andrew's names it.
- **The identifiers themselves are not secret,** and there is a source that needs no decryption: `gateway-access-state-table`. The
  allowlist's own comment says that table was read, read-only, on 2026-09-25 for this identity. The issuer reads the concierge's
  record there with its own AWS identity, read-only, and passes the two ids to the wrapper exercise in memory. They are not
  committed and not printed, as the runner already redacts them.
- (a) That read returns the ids: Phase B runs the wrapper arm as written, and `rl13.AC2` stands.
- (b) It does not (no access, or no matching record): the wrapper arm is DROPPED from Phase B and `rl13.AC2` is amended before
  GO to the in-process read of `displayed_date` on installed code, with limit (c) restated beside it. The release does not wait.
- **What happened in Phase A is recorded, not undone.** Row Z-W28-S20 goes to `3.0.0_SA_CVO~Z`'s slug as it stands, and this seat
  tells Andrew plainly that the cache was opened once. Whether anything further follows from that is his.

## Consumers this half names

- **The audit lake.** Its rivalfunds records change shape for every reader of that sink: three kept args and a `bytes` field where
  there was `_omitted`. Limit (d) says the S3 sink was not exercised in Phase A, only scratch files. So the first lake record after
  the deploy is read, and it is the acceptance for R36: one record carrying `day`, `route` and `bytes`, and no other arg.
- **The Teams concierge and the daily send's callers,** which read `displayed_date` from the status tool. It goes from null to the
  manifest's `generated_at`. That is a TIME the manifest was generated, not the data's as-of date. A caller that reads it as "the
  date the dashboard shows" is close on most days and wrong on a re-publish of an older date. The field's name and the two skill
  texts say "displayed date"; the next form edit states what the value is.

## Accepted as the ask states them

- The blast radius of section 2, its "unchanged" list, the three properties' branches, and the rollback (redeploy `/c/tmp/og-rb21`).
- Limit (b)'s A2: a page difference counts as a trigger only if the object's `LastModified` did not move between the two reads.
- The rollback triggers of section 5, including "a refused id making a request", carried from r26.
- Step 7: the manifest note holds this release only (row Z-W28-S19's disarm).
- Timing: today's send is served, so Phase B may run today.

## Not covered by this half

- Any real send. Any further read of the sign-in cache. The concierge's scopes, which Andrew has taken up with NFRA_OPALAI's COO
  (his word of ~15:3xZ at this terminal).

-- 1.0.0_SA_CTO~Z
