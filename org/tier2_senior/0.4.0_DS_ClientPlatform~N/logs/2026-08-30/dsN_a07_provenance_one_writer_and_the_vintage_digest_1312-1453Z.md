# Session log -- 0.4.0_DS_ClientPlatform~N, 2026-08-30 13:12-14:53Z

Two cells: `C02-g-10` (ADVI_49F.c02-A07STAMP) closed except its timed limb, and `C02-g-13`
(ADVI_49F.c02-VINTAGEDIGEST) built end-to-end from a finding the first cell's own falsifier
produced. Commits `cfc15ce384`, `04498e9904`, `e05f1a4f02`, `1befd43cef`, `2d094cbdb9`.

## C02-g-10 -- the Atom-9 provenance pair gets ONE writer

a07 stamped `_ingested_at` from a wall clock and `source_pipeline` with a STAGE string. Measured
on the served object rather than inferred: `date=2026-08-28` carried
`_ingested_at = 2026-08-30T12:47:05Z`. Both sites now call `rc.stamp_provenance`.

**THE CELL WIDENED BECAUSE AN ARM FAILED HONESTLY.** A7-3(ii) predicted the chain-wide writer
census would read "exactly one writer". It read TWO -- the helper, and `a00_dim_account.py:353-354`
hand-rolling the same pair. a00's values were value-identical (the literal and `asof`), so nothing
served had ever diverged, and the easy move was to add a00 to the arm's allowlist. That would have
made the arm pass BY DEFINITION on a census that still read two. Reported NOT MET instead; the gate
rec'd widening (87523), the issuer widened the cell (87531), and the census now reads one because
the second carrier was REMOVED.

**A7-2's falsifier fired, and the third mover was not mine.** `_classifier_vintage` moved across
three runs while `content_hash` stayed identical. The pairing design is what made that
attributable: a07 classifies against LIVE DynamoDB, and `_manifests/2026-08-28/` already held TWO
builds of one date (4,164 -> 4,165 rows) one fire apart, so scoring against the served partition
alone would have let substrate drift read as the edit. Pre-registered at 13:26:28Z, before either
run, naming the falsifier and excluding `process_ts` by name in advance.

**A7-4 was filed UNCOMPUTABLE, not PASS.** The deploy limb is verified -- three served ETags equal
to their index blobs, ledger opened and closed on the running-artifact read -- but the second limb
reads what a FIRE emits, and today's fire had already run at 12:47Z. A criterion whose subject does
not exist yet is not a pass.

**The custody chain was read at source**, not inferred from a bucket name: `cron(45 12 * * ? *)` ->
Lambda `advi-49f-gold-dispatch` -> SSM `advi-49f-chain-dispatch` v3 ->
`aws s3 sync s3://opal-data-49financial/_code/ ... --delete` -> `chain_49f_entrypoint.py
--production`. That is what makes the ETag read a RUNNING-ARTIFACT read.

**The CRLF limb was load-bearing.** a07 is one of 9 of 82 tracked runner `.py` whose working tree
was CRLF against an LF index, and the pre-push gate ships worktree bytes. The convention was
established by measurement -- the pre-fix object is byte-equal to the pre-fix INDEX blob and not to
that content rendered CRLF -- and `0.0.0_AB_MSTR` hand-normalised 557 CRs before the push. A manual
act, recorded in the ledger so no future deploy of that key assumes it.

## C02-g-13 -- the vintage becomes a pure function of the substrate

The mechanism was NOT the obvious one. The digest was over `str(sorted(ticker_map[t].items()))`;
the keys and items ARE sorted, so **"DynamoDB scan order" is refuted at source** -- that is the
answer I would have filed had I not opened the line. But an item value is a DynamoDB string SET,
and `str()` of a set renders in per-process iteration order under CPython hash randomisation.

**Baseline first, over a FROZEN substrate.** The substrate was snapshotted before any measurement,
so the LOADER could not confound the form -- the limit V-3 names, closed by construction rather
than by a sentence. Failing baseline: 3 processes -> 3 distinct vintages. After canon-json-v1:
3 processes -> ONE value, and three runs of the REAL a07 path produced that same value. Both
polarities: alias added -> different; aliases reordered -> same. `content_hash` unchanged.

**Only 6 of 9,538 tickers carry a set-valued attribute.** A cause that small randomised an entire
served field on 2 tables x 540 dates, and a sampling census would have missed it.

**The digest-field census returned clean, and the instrument choice mattered.** 8 fields over 34
modules, zero further findings. An AST census, chosen after comp-find on the same tokens returned
1,801 hits across 73 pages dominated by CONFIG data files -- a text sweep answers "where does this
word appear", not "what fields does this code emit". The one worth opening was `desc_hash`
(a03:80): its underlying key is `hashlib.md5`, not Python's per-process `hash()`. Had it been the
latter, the same defect would have been sitting in a security KEY.

**The arms drive PYTHONHASHSEED explicitly.** Spawning three default-seeded processes and asserting
they disagree is a coin-flip dressed as a control. The legacy form is committed as a STANDING
failing baseline so the determinism arm beside it cannot quietly become a dead arm.

## Corrections and instrument notes

1. **The cmd.exe caret.** `git show <sha>^:<path>` through Python `subprocess(shell=True)` -- on
   Windows the shell is cmd.exe, `^` is the escape character, it was consumed, both refs resolved to
   the SAME commit, and the run returned two identical digests and a confident "S3 matches neither".
   Caught by a content control that was in the script for an unrelated reason ("does the pre-fix
   blob contain `rc.stamp_provenance`?" printed 2, which is impossible). Re-run with `~1` and
   `shell=False`, the controls read 0 and 2 and the verdict INVERTED.
2. **HEAD moved under the measurement.** Other seats commit to this shared branch, so `HEAD~1` was
   never my baseline. The PIN is what makes a baseline one.
3. **A deploy state stated in a message is a CLAIM.** The issuer's 87999 said the g-13 bytes would
   deploy at a later window; the object said they were already served at 14:42:52Z. The issuer
   corrected the clause on that measurement. Had the message been believed, V-4's ledger would have
   opened against the wrong window and Monday's fire been attributed to the wrong bytes.
4. **A verdict at a stale instrument vintage is not a verdict.** proof-of-spec-check was repaired at
   `cec2a9b663` after the A7 instance validated at `3948c766a7`; the committed instance was re-run
   rather than assumed to hold. Still VALID.
5. **My own proof failed the checker twice before passing**, and both failures are recorded IN the
   instance: rc=2 (a USAGE error -- ids are comma-separated, and rc=2 is "usage/read error", which a
   seat reading only "non-zero" would file as a validation failure that never happened), then rc=1
   on two real violations (an enum value outside the schema, and an artifact with no acceptance row
   the coverage rule could see).
6. **`vintage_quality` at perfrp_emit_core:715 already carried the claim-field pattern** g-13
   installs, declaring itself "read-time-only ... NOT a reproducible vintage". Two independent
   arrivals at the same convention; recorded so g-13's form is not later described as novel.

## Owed, and all of it timed

Nothing here is blocked on another seat. Three reads ride scheduled fires:
- **Monday 2026-08-31 12:45Z** -- a06's registered map line (two named skips to 2026-08-28,
  `map_carried=False`, registered at 87710 from the READ 08-30 partition, header-only, landed
  13:17:40Z); A7-4's second limb; V-4's first fire.
- **Tuesday 2026-09-01 12:45Z** -- V-4's second fire. One fire cannot settle a determinism claim: a
  single run of a randomised digest also produces exactly one value.

The deployed bytes were exercised ad-hoc in the meantime -- synced from `_code/` as the SSM document
does and run to a scratch root, nothing served touched -- and all three tables emit correctly. That
closes identity-vs-behaviour without consuming the discriminator the scheduled fire exists to
produce.
