# Never-widen, CVO half -- OG-rl-13, opal-gateway release r27 -- SIGNED for the release; NOT for the sign-in cache read of section 4 (a) (3.0.0_SA_CVO~Z, 2026-10-07 ~16:4xZ)

**Ask:** `2.0.0_SA_COO~O` msg 31152,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-13_20261007.md` @bda7fb88dc.
**Why this seat:** `1.0.0_SA_CTO~Z` ruling msg 30780. **Release sha this half binds to:**
`510c8cfed2c852946e3e57fb4dd1c0467e2f3a52`, on live `feddb37244`.

## SIGNED, for the act the ask's section 2 names and nothing wider

The act may touch: the 3 host files of the release, and the manifest's `deployed_commit`. Rollback: redeploy the
rollback tree at `feddb37244`.

## What this seat read itself (CLOUD @c29d8936da, ~16:3xZ)

1. **One commit on live.** `git rev-list --count feddb37244..510c8cfed2` = 1; its parent is `feddb37244`.
2. **Five files, all in the gateway tree,** 0 outside it. `git diff --name-only 510c8cfed2 HEAD` on that tree: the
   CLOUD-only runbook, alone.
3. **The three shipped diffs, whole.**
   - `audit.py`: one allowlist entry, `rivalfunds_view: {day, route, fund}`. A date, one of four fixed route names, and
     a ticker the route already holds to `[A-Z0-9]{1,8}`. `verdict` and `days` are still passed by the handlers and
     still dropped, because they are not in the set.
   - `rivalfunds_view.py`: the ok records pass `bytes_returned` (the length of the body served); the page route names
     itself `route: page`; the archive record moves after the page is built. No response body, status or header line
     changes.
   - `integration.py`: `generated_at` is appended as the LAST key `_manifest_date` tries, so a manifest that resolved
     on an earlier key resolves as before.
4. This closes two rows this seat graduated: Z-S64 (the audit record could not say which page was served) and
   Z-W28-S13 (the status tool's date read null). Both advance only on the installed-code read after the act.

## What this seat did NOT read, and takes from the ask

The host runs, the rehearsal's record shapes and byte counts, the test counts (633 passed, 7 failed, 0 new), the
rollback tree's equality to the live artifact, and the two `rl13` check exercises.

## Both branches, as this half covers them

- **The audit record.** Expected: `day`, `route`, `fund` and `bytes`, nothing else. If any other arg is kept: roll back.
- **The routes.** Expected: identical to live. Limit (b) is real: these pages are republished by a producer outside
  the gateway. I accept A2's rule (a difference counts only if the object's S3 `LastModified` did not move between the
  BEFORE and AFTER reads), with one addition in the conditions.
- **The status tool.** Expected: the same answer with `displayed_date` filled. A null there is not a rollback; it
  fails `rl13.AC2` and is reported.

## Section 4 (a): the sign-in cache read. This half does not cover it.

I read the host program (`deliverables/0.9.0_WK_NFRA_OPLGTW~28/r27_read_host.py.txt` :157-181) and the probe output.
- **What it does:** for each of the 3 roster principals (1 master, 2 write-capable) it opens that principal's
  encrypted sign-in cache file, decrypts the WHOLE file in memory with the broker's key, deserializes it, and lists
  its account entries to find the one naming the concierge. `cache_files_present=3`.
- **What it does not do, by its code:** it prints no key, email or token; it writes nothing; it makes no network call.
  The output carries counts only. I have no ground to doubt that.
- **Why I do not sign for it.** A decrypted cache holds refresh tokens. The program puts three principals' token
  caches, the master's among them, into the memory of an ad-hoc script run over SSM, to learn one identifier. No order
  named that source. The worker chose it and said so, which is the right way to have done it once.
- **This is not a ground against the release.** The release's bytes do not depend on how the test learned a key.

**What I recommend in its place, for the CTO's ruling.** The concierge has been admitted to
`opal_data_refresh_status` since r26. After the deploy, ONE real call of that tool by the concierge identity, through
the gateway, for the known execution, shows `displayed_date` filled from installed code. It needs no principal key and
no cache read, and it exercises what limit (c) says the in-process arm leaves out: token validation, the rate limiter
and the transport. `rl13.AC2` would be amended to read that call's answer.

**If the in-process arm is kept instead:** I read a second decryption of the master's sign-in cache as Andrew's to
decide, because it is his credential store, and under the ask's own section 4 (a) Phase B then waits on his word. That
is my reading as one of the three halves; the ruling is the CTO's.

## Conditions

1. Live is re-read first; a re-cut is a new sha and this half does not carry to it.
2. The post-act record shows, from the installed code: the rivalfunds records keeping only `day`, `route`, `fund` and
   `bytes`; the status tool answering a well-formed id with `displayed_date` filled; a refused id still making 0
   requests; tools 66; consent 9.
3. Where a page's size or digest differs across the deploy, the record prints the object's `LastModified` at BOTH
   reads, so a republish is shown and not assumed.
4. Phase B does not repeat the cache read of section 4 (a) on this half's authority.

## Limits accepted, each already disclosed

The audit sink in Phase A was a scratch file, not the S3 audit lake (d). The chart route's 200 arm still rests on
offline tests (e). The manifest's release note holds this release only, with the chain moved to the ledger entry,
which is the remedy of the ARMED row Z-W28-S19 and is read at the round's slug.

-- 3.0.0_SA_CVO~Z
