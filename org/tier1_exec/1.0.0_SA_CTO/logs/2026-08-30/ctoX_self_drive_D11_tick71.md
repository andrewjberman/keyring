# /self-drive D11 -- tick 71 (the digest-grain rulings; the artifact-resolution arm; two faces closed, COX at re-cert)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, BUILD, SCRIBE

- seat: `1.0.0_SA_CTO~X` (design lane) -- cron **31950a5f**, 60m at :11 (fired 05:19Z); paired with
  `/drive D11 @ 2.0.0_SA_COO~X` (+15m). ticks covered: 71. state: **ARMED**.

## Steps

- Step 0 register: 12 live directives; D11 -> 2 members, both `active` / `EXECUTING`; claims scan 342 JSONs,
  1 PRD-path claim (already a member); device LAPTOP; **open TOs 8** (was 9): L3W3 **1** (COX; CCY closed
  @8e606c8ff8-era, CCX closed complete @8d38d444a0 on CVO~X's PASS) + carding 7. 2 of 2 REACHABLE.
- Step 1 /open-calls scoped D11: 0 calls. Step 2: no pitch. Step 3: 0 CVO verdicts in the loop sense; ledger
  21 rows, 0 unconsumed. Step 4 completion: NOT DONE -- 0 of 2 `complete`.

## Delta since tick 70 (driver acts)

1. **proof-of-spec-check ARTIFACT ROW RESOLUTION arm @3948c766a7** (on the issuer's proposal 85753, after two
   instances passed VALID with false provenance -- COX @c36a309f4d dead own-path, CCX @fa7b34274a misplaced
   PENDING sentinel): every repo artifact row's (commit, path) pair is resolved against git, a PENDING row's
   path against the worktree; cross-fabric pins and s3_object rows ANNOUNCED, never refused; the CCX
   sentinel-placement class named on the frame as NOT covered. Measured: COX @7595c2a3a5 VALID (13 rows
   resolved), CCX @217faaa693 VALID (3), the historical COX @c36a309f4d INVALID rc=1 on exactly its dead row;
   5 new controls + 4 existing green; gate clean. Broadcast 85802-7 with the gate change stated.
2. **CRO~X's joint-cert HOLD on COX AC6 (four sha256 values hash CRLF renderings, not the committed LF blobs
   at 2234620592) -> Addendum 1l @5805e3fa0c:** the identity of a repo artifact is its COMMITTED BLOB; rebuild
   on `git show <pin>:<path>` bytes with a worktree-differs negative; instrument gap named (the resolution arm
   checks (commit, path) only). **Narrowed @59904440d0** to the issuer's more restrictive reading (85828,
   latest + most-restrictive): NO rendering digest on a certified row, typed or not -- a device-local value
   in a certified record is the LD-0405 class; a rendering digest lives only in a local non-certified sidecar.
   The issuer corrected its routing to match (85867). Rulings 85821-4, 85857-60.
3. **The `digest_of` enum ruled and recorded as Addendum 1l(vi) @b7baa4c390** on CRO~X's AC2 census (5
   SHA-bearing inputs, 5 bare grains): {blob-at-pin (pin on the row), s3-etag (ETag-only identity), served-object
   (downloaded bytes; URI on the row), **content-addressed** (a FIFTH member: bytes in no commit and on no served
   plane -- the digest IS the identity; `retrieval` + the named gap "publish or track before the L4 cut"; the row
   that MOVES when the gap closes), worktree-rendering (sidecar-only, never a row value)}; a bare sha256 is
   FORM_DEFECT. Served view 1 = served-object (concur); the untracked stitch carrier (view 2, 7ac11d01...) is the
   first content-addressed row and carries its gap on the certification's face. Rule-24 record on the clause.
   Rulings 85853-6, 85903-6; the issuer's amended dispatch 85926 carries all five verbatim.
4. **COX at re-certification:** sweep measured (tick 70), 11 cells written @2234620592, N=20 battery (rho 0.956
   / J 0.931), proof re-presented @7595c2a3a5 then AC6 digests repaired @2ab182827d (4/4 now the blobs CRO
   named); the next candidate types all 5 AC2 + 4 AC6 rows per 1l(vi) and fixes the PENDING sentinels the
   builder derived for clean committed files. Certifiers finish on that candidate only. CCX: closed complete
   @8d38d444a0 -> W1-CCX carding opens at that seat. c69f-4 settled (a) on all sides (tick 70).
5. Also since tick 70: `/exec-sum D11` and `/open-calls` answered for Andrew (03:30Z; zero calls at this lane);
   the v3.1 set_by rule enforced @0b51b6c72a (tick 70, now ON ORIGIN @c723b323cf).

## Scope state (denominators printed)

| project | status | dep_stage | open TOs | reachable |
|---|---|---|---|---|
| NFRA_C3MATERIALIZE | active | EXECUTING | 1 of 3 L3W3 faces open (COX at joint value cert) | YES -- next: wave-3 joint cert, then the firm-carrying-view cut under 1k |
| NFRA_SUBSTRATECARDING | active | EXECUTING | 7 of 9 carding faces open (DS + W1-CCY closed) | YES -- cards under CVO~X boundary reads |

Completion test: NOT DONE, 0 of 2 (denominator 2). RESERVED cards at Andrew: 0. Owed by this seat: the numbers
at the firm-carrying-view cut (1k headroom, margin, null, (K, T)); a digest-grain checker arm once a committed
carrier instance exists (1l(v)) -- follow-on, not built on one instance.

## Push state (measured 05:19Z)

origin/CLOUD = c723b323cf (04:49Z CLOSE). LOCAL, riding the next window: 3948c766a7, 5805e3fa0c, 59904440d0,
b7baa4c390 and this log (is-ancestor NO for all four, own read). Push is `0.0.0_AB_MSTR`'s.

## Compiler Tools

| tool | result |
|---|---|
| `python .tools/directives-check.py --json` | 12 live; D11 2 members, open TOs 8 |
| `python .tools/to-check.py --project ...` | 1 + 7 active, scanned 2209 |
| `.tools/proof-of-spec-check.py` (new arm) + pytest + `.tools/commit-gate.sh` | 2 live instances VALID; historical defect FIRES; 9/9; gate 2/2 |
| `git show <pin>:<path>` + `git cat-file -e` | the retrieval instrument every digest/path ruling used |
| comp-find / comp-which | not run -- every read was a pinned `git show`, a single named file, or a register/TO instrument |
