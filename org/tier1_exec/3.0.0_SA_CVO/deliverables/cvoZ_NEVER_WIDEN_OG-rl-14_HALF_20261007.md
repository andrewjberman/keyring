# Never-widen, CVO half -- OG-rl-14, opal-gateway release r28 -- SIGNED (3.0.0_SA_CVO~Z, 2026-10-07 ~21:3xZ)

**Ask:** `2.0.0_SA_COO~O` msg 31419,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-14_20261007.md` @9ece15debe.
**Why this seat:** `1.0.0_SA_CTO~Z` ruling msg 30780. **Release sha this half binds to:**
`aa75078e1b72a28219e6148d3ec8e9bf705ea111`, on live `510c8cfed2`. A re-cut is a new sha and this half does not carry.

## SIGNED, for the act the ask's section 3 names and nothing wider

The act may touch: the host's `app/audit.py` and the manifest's `deployed_commit`. The one movement of served
behaviour: a lake object for a record with no usable `ts` gets a time part in its key. Rollback: redeploy the tree at
`510c8cfed2`.

## What this seat read itself (CLOUD @ the time of writing)

1. **One commit on live.** `git rev-list --count 510c8cfed2..aa75078e1b` = 1; its parent is `510c8cfed2`.
2. **Eight files, all in the gateway tree,** 0 outside it. Against CLOUD the gateway tree differs by the runbook alone.
3. **`app/audit.py`, the diff whole.** `_lake_key` replaces three lines of `_emit`. A record whose `ts` is a string of
   10 or more characters gets the same key as before. Any other record gets the writer's current UTC time and the
   day from that same time. The record is not changed. One edge the ask does not state: before, a `ts` that was not
   a string was turned into one and used; now it is replaced by the write time. I know of no writer that sends one.
4. **`deploy-to-ec2.sh`, the diff whole, which I did not read for r27.** Two hunks.
   - Lines 206-211: the pre-check runs in the same subshell as the install, joined by `&&`. A miss, a pre-check read
     error (its exit 2) and a missing python each exit before `bun install`.
   - Line 307: the host's pip self-upgrade is removed. Line 308, `pip install -r requirements.txt`, is unchanged.
5. **`ops/bun_cache_precheck.py`, `_entry_state` and `_state`.** An entry counts only when its directory holds a
   `package.json` naming the exact name and version. An empty directory reads `empty`, which is the negative control
   R46 asked for.
6. **The five test files, run by me at CLOUD on the same blobs: 25 passed.**

## What this seat did NOT read, and takes from the ask

The host md5 comparison (97 of 97), the full test run (652 passed, 7 failed, 0 new), the rehearsal's lake-key reads,
the rollback tree's equality to the live artifact, and the pre-check's 77 of 77 on the real cache.

## Both branches, as this half covers them

- **A record with no time:** a stamped key, or roll back.
- **A record with a time:** the same key shape, or roll back.
- **R45, whether the deploy fetched:** 0 cache entries touched, or stop, file the BLOCKING row and roll back. I accept
  the CTO's addition (the cache's total bytes before and after), because the count reads to depth 2 only.
- **The host's pip step:** every line `already satisfied`, or the line is reported with the package named. Not a
  rollback.

## One thing that is Andrew's, stated so it is not lost

Line 308 runs pip on the EC2 host against `requirements.txt`, where 8 of 12 lines are lower bounds (the CTO's count, msg 31255). On a host that
already holds them it fetches nothing. On a new host, or after a changed line, it reaches the package index. Whether
the EC2 host is a box under Andrew's no-fetch word is unanswered. This release does not change that line and its
`requirements.txt` is not in the diff, so it is not a ground against r28. It stays open until he says.

## Conditions

1. Live is re-read first; if it moved, the halves are void.
2. R45's read comes before any criterion runs, and `RL14_BUN_CACHE.json` carries the count and the two byte totals.
3. The post-act record shows, from installed code: a no-`ts` record keyed with a non-empty time part; a record with
   `ts` keyed as before; the rivalfunds records still keeping only `day`, `route`, `fund` and `bytes`; tools 66;
   consent 9; a refused id making 0 requests.
4. The host pip output is kept whole in the deploy record, so a `Collecting` or `Downloading` line can be read and
   not inferred.
5. No sign-in cache is opened.

## Limits accepted, each already disclosed

(a) the stamp is the write time, not the record's `observed_at`; (b) no check writes a lake object; (c) R45's depth;
the undetermined metadata request. Row Z-W28-S26 advances only on a real lake key written by the installed r28.

-- 3.0.0_SA_CVO~Z
