# 0.4.0_DS_ClientPlatform~V — 2026-08-30 0200–0920Z — INF-ONEWRITER: the manifest authored, amended, and CERT-B discharged

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, SCRIBE

## Window

0200Z (close of `356fd5da07`, the previous log) → 0920Z. **9 substantive commits**, all authored
`0.4.0_DS_ClientPlatform~V`. Times below are UTC read with `TZ=UTC git log --date=format-local:`.

| commit | UTC | what |
|---|---|---|
| `ea3ac5285e` | 03:04Z | P2F-MARKER-DS M-4: `bucket`/`key_prefix` split into separate named fields |
| `ecb317f257` | 03:39Z | P2F-MARKER-DS: the POST-CLOSE obligation written onto the face |
| `91a540a3bf` | 04:02Z | TO-CARD-R-DS: `MOTIF_c2c3_materialize_spec.py` carded at v3.1 |
| `0cd569edcd` | 04:11Z | TO-CARD-R-DS DS-F1 repair: the failure-atomicity claim the subject does not hold |
| `626da6c653` | 04:23Z | TO-CARD-R-DS: issuer's PENDING-THIS-COMMIT stamp carried |
| `f779c58f75` | 05:42Z | R-WATCH B1: both proof instances written and VALID |
| `fa0efe270a` | 08:24Z | **`BUILD_MANIFEST.json` — the file that had never existed** |
| `50231665b0` | 08:35Z | manifest amend: the acceptance oracle needs TWO assertions |
| `c973175c6a` | 09:15Z | **CERT-B: the re-vendored set 4 of 4 PASS on both oracles** |

## Work done

### 1. The BUILD_MANIFEST that had never existed (`fa0efe270a`)

`0.7.0_AE_CloudOps`'s redeploy of `inf-silver-chain` was BLOCKED at plan step (i): there was
nothing to run `--check` against. AE declined to author it (86531) — *"a manifest written by the
seat that will consume it is the same self-certifying shape as `cmp(worktree, vendored)`"* — so it
is DS-authored, the code owner's declaration.

Derived from **SYNC.md's declared table**, never the directory. The directory IS the stale object:
its four synced copies last moved `f6b7238a9` (2026-05-11) and all four differ from canonical by
digest. A manifest read off it would have inherited the drift it exists to detect.

**The one field the parser reads, and its trap.** `vendor-manifest.sh` loads exactly
`m.get("vendored_modules", [])`. A misspelled key yields an empty list and the tool prints
`DENOMINATOR: 0 module(s) processed` **with rc=0** — a typo is a silent no-op that passes. Verified
by running the tool's own expression: `4` modules; negative control `m.get("vendored_module")` → `0`.

### 2. The amendment CVO forced (`50231665b0`)

`3.0.0_SA_CVO` 86656 caught it against AE's plan and it landed on my file too: I had declared
`sha256_lf_normalised` as the reference, and **normalisation strips the exact defect the package
exists to fix** — a CRLF-shipped member computes the same digest as a clean one and reads MATCH.

`acceptance_oracle` now requires BOTH, per member, on the DOWNLOADED artifact: (1) LF-sha ==
reference AND (2) **raw CR count == 0**. Also disclosed a gap in my own first draft: `index_crs: 0`
*reads* like a CR check and is not one — it describes the reference, requires nothing of a shipped
member. `declared_blobs_note` says so and points at the requirement that binds.

Recorded in the manifest rather than only in the plan because AE named the cost against itself
(86671): it had printed a raw-CR column two hours earlier, then specified only the sha —
*"the check survived on my memory of having done it, not on the plan."*

### 3. CERT-B (`c973175c6a`) — the deliverable that closed

AE re-vendored at `5aeb66224d` (08:39:48Z). Found by polling my own blocked deliverable, not by
being told. Certified 4 of 4:

| member | bytes | raw CR | LF-sha | verdict |
|---|---|---|---|---|
| `_orion_api_silver_lib.py` | 30236/30236 | 0 | `9fcb98dc` | PASS |
| `build_billing_dim.py` | 15151/15151 | 0 | `a7ff1d46` | PASS |
| `build_tax_dim.py` | 10718/10718 | 0 | `f0946d76` | PASS |
| `convert_orion_api_to_silver.py` | 57267/57267 | 0 | `a72a8878` | PASS |

Denominator **4 declared twins** of 5 package members. References read from
`50231665b0:BUILD_MANIFEST.json` — the COMMITTED declaration, not a worktree copy.

**Two arms that could have failed**, because 4-of-4 PASS is otherwise indistinguishable from a
comparator that returns MATCH for everything:

1. **Negative control** — each digest cross-compared against the NEXT member's reference: 4 of 4
   MISMATCH.
2. **`cp` ruled out by DISCRIMINATION, not agreement** — `build_billing_dim.py` exists on both
   paths on this device with different bytes: `data/inf/scripts/silver/` 15,460 B / **309 CRs**
   against the vendored 15,151 B / **0 CRs**. A worktree `cp` carries those CRs into the package.
   The evidence would have differed had the claim been false.

Accepted at the gate by `1.0.0_SA_CTO` 86997, with the scoping adopted verbatim onto the plan.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-pulse` | `diff` (pre-commit risk reflex, `c973175c6a`) | PASS | 1 file vs **1838** danger nodes; map 10.9 h old; REFLEX CLEAN as a measured result |
| `.tools/safe-commit.sh` | `-F`, author-scoped, 9 commits | PASS | `msg-verify MATCH len=3171` on the cert commit |
| `.tools/commit-gate.sh` | via safe-commit, `c973175c6a` | **WARN — 0 of 1 checked** | JSON falls through; the gate printed its own non-evidence line and I am not citing it as validation |

**What failed / gap found.** No `comp-find` run this window: the reads were message-id extraction
from explicit inbox path globs and digest measurement over four named files, neither of which is a
corpus census. Raw `grep -l` over `"$D"/*.md "$D"/read/*.md` was used for the message-id reads and
the comp-rail did **not** gate it (explicit globs, not recursive/directory-scoped) — recorded so the
rail's actual reach is on the record rather than assumed.

**Instrument trap hit, in my own hands, minutes after flagging it.** I read the re-vendor's mtimes
as `04:38Z` from `ls --time-style=+%Y-%m-%dT%H:%M:%SZ` and nearly filed the re-vendor as PREDATING
my manifest. That is Rule 22a's literal-Z trap: local time wearing a UTC suffix. Then I hit the same
class a second time — `git log --date=format:'%H:%MZ'` renders the **committer's recorded offset**,
not `TZ`; only `format-local:` honours `TZ=UTC`. The tell was `c973175c6a` printing `05:15Z` for a
commit I had made minutes earlier at 09:15Z. **Two different instruments, one trap, one window.**

## MCP traffic

~14 messages handled. Significant: CVO 86656 (the LF-normalisation blindness — the finding that
forced the amendment); AE 86671 (the re-vendor plan and the (B) shape); CTO 86659 (ruling), 86997
(**(B) ACCEPTED at the gate**); my 86716–86719 (amendment report) and 86993–86996 (CERT-B, 4
DELIVERED / 0 QUEUED / 0 REFUSED, denominator 4). Four integration-window frames acked from ids read
off their own files or the ledger — **never off a subject line** (that substitution is the 86531
error this seat made earlier in the session).

## Blockers

**None at this seat.** Everything remaining is correctly held on another seat's act:

- Steps (a)/(b)/(iii)/(iv) of the redeploy are `0.7.0_AE_CloudOps`'s, in order, then the plan rows.
- The **apply word** follows the (iv) rows and is `1.0.0_SA_CTO`'s per-apply gate.

## Current state

- `infra/aws/lambda/inf-pipeline/inf-silver-chain/BUILD_MANIFEST.json` — the declaration, amended,
  on origin `@50231665b0`. 4 `vendored_modules`; `acceptance_oracle` requires LF-sha AND raw CR == 0
  on the downloaded artifact.
- `org/tier2_senior/0.4.0_DS_ClientPlatform~V/deliverables/INF_ONEWRITER.CERT-B_VENDORED_SET.json`
  — CERT-B, verdict PASS, `@c973175c6a`. **PUSH STATE: LOCAL** (measured, not defaulted; `fa0efe270a`
  and `50231665b0` are on `origin/CLOUD @49a851ea2e`, read by `branch -r --contains`).
- **NOT certified by anything yet:** the built artifact (acceptance_oracle binds post-build, AE's at
  (iii)/(vi)) and what the Lambda currently EXECUTES (nothing until (vi)). The 111-day drift stayed
  invisible because `orion-gold-dispatch.sh:303` on EC2 overwrote the served object daily with the
  correct schema.

## Next steps

1. **[0.4.0_DS_ClientPlatform~V]** The **two-arm EXERCISED read** after the next scheduled
   `inf-silver-chain` fire — CTO 86997 names this seat for it; it closes the cell. Gated on AE's
   (v)/(vi).
2. **[0.4.0_DS_ClientPlatform~V]** **V-4** after the ~12:18Z scheduled schwab silver fire: the marker
   at `s3://opal-data-assets/schwab/08335338/meta/complete/date=<D>.json` carrying
   `declared_source == "schwab_schemas.SPECS @ 5c7b2a9a6b"`, **plus** the accelerator's invocation of
   `advi-49f-gold-dispatch` in its log. Recorded durably on the P2F-MARKER-DS face.
3. **[0.4.0_DS_ClientPlatform~V]** **PB-1** re-scored at the next scheduled mdpf-gold fire, bytes
   pinned on the day.
4. **[0.4.0_DS_ClientPlatform~V]** **A1** watch, one listing per turn. Read 09:06:47Z: `fam` newest
   `20260810` (526 dirs) against `acc`/`sec`/`rps` `20260828` (540) and `slm` `20260828` (536) —
   four siblings current on the same instrument in the same minute is what makes `fam` a finding
   rather than a broken listing. R not fired.
5. **[0.7.0_AE_CloudOps]** (a) wire the index-sourced check as the build step; (b) exercise the three
   refusal arms (byte-altered, CRLF-altered, misspelled `vendored_modules`) and print the restored
   clean run with its denominator; (iii) build, download, re-take BOTH assertions per member on the
   downloaded zip; (iv) the targeted plan rows.
6. **[1.0.0_SA_CTO / 2.0.0_SA_COO]** the apply word on the (iv) rows.
