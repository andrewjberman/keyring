# CTO~Z — the v2.1.170 PROD promote, and the withdrawal that preceded it, 0435-0600Z

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 04:35Z -> 06:00Z (continues
`ctoZ_D1_D4_architecture_gate_0045-0435Z.md`, whose A1-A7 amendment blocks carry this window's
corrections and are NOT repeated here)
**Basis:** Andrew-direct ~05:2xZ — *"Ok let's just get a /prod-deploy going i think we're ready at
least on that matter at this point."* That is his word on the PROD promote, one of four sovereign
calls carried at this seat all night.

---

## 1. WHAT LANDED

**`portal v2.1.170` IS ON PROD AND SERVED.** Merge `d4a048fd`, 35 commits published, base/rollback
`73afaccd`. Ledger `20260828T0532Z_portal-prod-promote-v2-1-170-satellites`: **4 of 5 legs CLOSED
with proof**; `ws-pointer` open and owned by `0.0.0_AB_MSTR~Z`.

Andrew's four smoke-test items all shipped: `5a4349a5` (hide Satellite 98 at the RENDER, retire the
firm selector, colour gradient), `1c5cdbe5` (shrink text/bars, clean at the 1440px floor),
`2858e7f5` (INT default, new users first visit only).

## 2. THE PROMOTE — GATES, IN ORDER

| Step | Result |
|---|---|
| 0 DT-only gate | Ran under the skill's own **"or explicitly Andrew-directed"** exemption; serial is not `0.x.0_DT_*`. Stated, not skipped. |
| 1 tree state | portal on DEV, local == `origin/DEV` == `2858e7f5`. No Step-1a push needed. |
| 2 typecheck | `bun run typecheck` (**`tsc -b`**) rc=0. ⛔ Bare `tsc --noEmit` checks NOTHING here — root tsconfig is `"files": []`. |
| 3 re-assert PROD | `update-ref` from `origin/PROD` before the worktree add (dry-run-pollution class). |
| 4 merge + parity | `d4a048fd`, parents `73afaccd` + `2858e7f5`. **Parity `git diff origin/DEV PROD` = 0 bytes, re-run from the MAIN repo, not the worktree.** |
| 4 push | ⛔ **BLOCKED — LD-0367/LD-0368, shared-branch push is INTEGRATOR-ONLY.** Escalated to `0.0.0_AB_MSTR~Z`; **the `# never-override:` escape was NOT taken.** Pushed 05:32:17Z. |
| 5 CI | run `33145060591` completed/success, re-read AFTER conclusion. |
| 7 teardown | `worktree remove` rc=255 *Filename too long* (documented Windows behaviour, dir is gitignored + inert); **`prune` run regardless**. portal back on DEV, cwd at workspace root. |

## 3. WHAT I GOT WRONG IN THIS WINDOW (4)

| Claim | Truth | Caught by |
|---|---|---|
| cause (1): `/api/general` unproxied, SPA fallback HTML-200 — sent as **"MEASURED"** | **Never existed.** The bare `/api` catch-all always proxied it; auth always forwarded | `0.4.0_DE_ClientPlatform~S`, before/after with one bearer |
| AC2 axis ruling (reachability) | Sound in form, **selected an axis with ZERO VARIANCE**; my PASS set contained the baseline | myself, once the baseline landed |
| `MERGE_RC=0` on a merge that died on git identity | **Piped through `tail` — that was tail's rc.** Lied in the reassuring direction | myself, on the parity output |
| `Origins.Items[0]` read as *the* origin -> `assets/` six months stale | **7 origins; default behavior targets `S3-opalinvest-portal`** | myself, on an impossible value |

⛔ **THE LAST ONE IS THE INSTRUCTIVE PAIR.** `0.0.0_AB_MSTR~Z` hit the same shape within the hour —
grepped the **entry bundle** for satellites literals, got four clean zeros, and was saved only by a
positive control that could not legitimately be absent (route code lives in a lazily-loaded chunk;
`0 hits` was OUT-OF-CORPUS, not absence). **Two seats, two corpora, one shape.**
>> **Neither of us was saved by noticing the query was narrow. Both were saved by the ANSWER BEING
IMPOSSIBLE** — a six-month-stale bundle, an absent pre-existing field. That is luck wearing rigour's
clothes, and it argues for **printing the DENOMINATOR on a resource query (7 origins) the way we
already do on a text census.**

## 4. THE RULING ISSUED THIS WINDOW

>> **A CRITERION THAT ASSERTS A CHANGE MUST STATE THE VALUE ITS OWN BASELINE PRODUCES, MEASURED, AT
CUT TIME.** Cost: one read at cut. **Non-application: binds only on change-assertions, never on
state-assertions** (a value present, a policy allows, a `file:line` citation). Tell: *what would this
criterion have scored yesterday?*

All three versions of `TX1DE-AC2` — the original, `2.0.0_SA_COO~Z`'s amendment, and **my own** — had
a PASS set containing the measured baseline of **403**. Each would have certified doing nothing.
**Three seats refined which values PASS; none asked what the baseline PRODUCES.** Adopted by
`3.0.0_SA_CVO~Z`, who vacated two classes of their own as subsumed; `0.7.0_AE_CloudOps~S` applied it
to a live criterion (`T6AE-AC3` scores FAIL yesterday — it can fail) and noted it was **not**
compliant when cut.

⚠ I declined `2.0.0_SA_COO~Z`'s "sound on a false premise" exemption. I was ruling on whether a
criterion could discriminate, which **is** a question about the baseline.

## 5. Compiler Tools

**No `comp-*` tool was run this window, and that is correct rather than a lapse.** The window was a
git/AWS/CI deploy plus a doc-level ruling; the rail's instruments (`comp-find`, `comp-which`,
`comp-estate`) answer code-location and estate-shape questions, and every question here was
*"what does live state say"* — answered by `git rev-parse`/`merge-base`, `aws cloudfront`/`s3api`,
`gh run`, and `deploy_ledger.py`. Substituting a comp-tool would have been the wrong instrument.
**`deploy_ledger.py open/close-leg` — PASS**, and it is the reason the promote has a closable record.

## 6. Blockers

**NONE at this seat.** `ws-pointer` is open and is `0.0.0_AB_MSTR~Z`'s — **evidence-cited, not
assumption-blocked**: workspace gitlink `4ac152f8b93a` vs portal tip `2858e7f5ff02`, **34 commits
behind**, `git status --porcelain portal` -> `" M portal"`. Measured independently by
`2.0.0_SA_COO~Z` and by `0.0.0_AB_MSTR~Z`.

## 7. Current State (zero prior context)

- `origin/PROD` = **`d4a048fd5252833f6045e235d27fe8ee95b2799b`**, tag **`portal-v2.1.170`**
  (**PEELED** `^{commit}` == PROD head; raw `ls-remote` object sha `0d55beb7` appears nowhere in the
  promote — that is the double-merge misread, demonstrated). NEG CONTROL: `v2.1.169` peels to
  `73afaccd` = the rollback base.
- **SERVED**, two instruments, two planes: `0.0.0_AB_MSTR~Z` `curl -sI` on `opalinvest.dev`
  (alias read from the distribution's own `Aliases`) — index.html `Last-Modified 05:34:02 GMT`,
  `X-Cache: Miss from cloudfront`; this seat `s3api head-object` on **`opalinvest-portal`** —
  index.html `05:34:02Z`, `assets/*` `05:34:01Z`. ~1m45s after the push.
- CloudFront **`EVTSA9VEHNZVH`**, aliases `opalinvest.dev` / `www.opalinvest.dev`, **7 origins**;
  default cache behavior -> **`S3-opalinvest-portal`**. ⛔ `opal-data-portal-v2` is the **DATA**
  origin, not the site — its `assets/` are from 2026-02-06 and reading them as the site is a
  false-failure trap.
- ⛔ **UNTESTED RUNG NOW LIVE** (`2.0.0_SA_COO~Z`): every satellites render was verified against
  **FIXTURES with a STUBBED SESSION**. **No live cottonwood caller has ever been served.** PROD is
  its first real exercise — a difference there is that rung surfacing, NOT a regression.
- ⚠ **INT default will look broken to Andrew and will not be** — first-visit-only by his own ruling;
  a warm browser tests the persistence rule, not the change. **Cleared storage or it proves nothing.**
- ⚠ **Asset Category Views renders "not available at this scope" until ~13:30Z.** MEASURED 05:2xZ:
  zero objects matching `category` under `platinum/mdpf/`; positive control returns four siblings.
  Andrew's word: *"we'll wait and see what comes through."* **No ad-hoc run was made.**

## 8. Next Steps

1. **[`0.0.0_AB_MSTR~Z`]** `ws-pointer`: commit + push the submodule bump same-turn, then close the
   leg. **GO given** — verification complete, Step 7's sequencing condition met.
2. **[`2.0.0_SA_COO~Z` / `0.0.0_AB_MSTR~Z`]** Ledger closes when leg 5 does. ⚠ 12h window, and with
   the fabric at three seats **there is nobody else to close it** — if it cannot close, close it
   **SUPERSEDED** rather than let it blare.
3. **[time]** 07:00Z satellites (**invocation AND a successful write** — the only existing log stream
   is a FAILURE); 13:00Z ETFs on confirmed TO-7 bytes; 13:30Z mdpf floor. **No ad-hoc before any.**
4. **[ANDREW]** 3 open calls remain — design-pass accept, book-grain-return scope, CLAUDE.md Rule-21
   wording (now **two** limbs: the raw-`aws` hard-deny that does not fire, and the `head` prohibition
   being scoped to `comp-find` while three seats truncated a raw grep of one file in one hour).

## 9. One thing worth carrying

**The promote's two hardest moments were both a query answering a narrower question than the one
being asked** — my `Origins.Items[0]`, `0.0.0_AB_MSTR~Z`'s entry-bundle grep. Neither was a careless
read; both instruments were correctly operated on the wrong corpus, and both returned confident,
clean, wrong answers. **The night's other lesson — the baseline ruling — is the same defect one level
up: a PASS set correctly refined against a question nobody had measured.** *Being right about the
answer you computed is not the same as having computed the answer to the question.*
