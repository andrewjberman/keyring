# 3.0.0_SA_CVO~Z -- delta 2330-0110Z: R-12 class census, two corrections, one self-correction

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

**Window:** 2026-09-23 23:30Z -> 2026-09-24 01:10Z. **2 substantive commits** (`4eee2d0317`,
`63c3dfde02`) plus the two log commits that closed the prior entry. Prior log:
`session_close_2045-2330Z.md` @`948dc9661d` / `a7880e97c2`.

**Why this entry exists:** the largest pieces of work in this window -- the class census and the
denominator reconciliation -- produced **NO commit of mine**. They were measurements reported by
message. Without this entry a successor reading my commits sees two surprise rows and none of the
numbers behind them.

## WHAT WAS DONE

**1. The incomplete-teardown CLASS census (`AMGT_RESAPP-Z-S241` @`4eee2d0317`).**
`1.0.0_SA_CTO~Z` ruled the five leftover `.tf` files were "the instance rather than the finding",
named the signature, and said it was not driving the census. No seat held it. Run here: **477 tracked
`.tf` across 77 directories, signature returns ZERO**, and the zero was **controlled** -- a probe
planted at `globgrph/.cvo_control_probe.tf`, query returned 1, probe removed. The five were confirmed
**GONE by name** by a seat that did not perform the deletion.

**2. R-12 refinement, adopted.** The ruled verify-after was "an `ls` or a `terraform plan` -- NEVER a
git read". Offered: `git status --porcelain --untracked-files=all` is a git read that reads the
**working tree**, so the real distinction is **history-plane vs worktree-plane, not git vs not-git**.
Adopted in full as **R-12** @`6b47ded436`. Practical point, not pedantic: an `ls` needs to know which
directory, so it verifies one teardown; one `git status -uall` covers every directory with a printed
denominator.

**3. The excluded false hit, corrected (`AMGT_RESAPP-Z-S242` @`63c3dfde02`).** R-12's amendment
excluded one tracked-modification hit as "that seat's live work" -- my worktree, and I made no such
edit. **No edit exists:** working file and `HEAD` blob are **byte-identical**, 2,815 bytes, sha256
`dd840e19c098c330`, 82 CRLF each. Same bytes in every worktree sampled. **1 of 15 says MODIFIED, 14 say
CLEAN, on identical content.** Mechanism: `.gitattributes` says `eol: lf` but the committed blob
carries CRLF on every ref, from `39810307ce` (Andrew Berman, 2026-02-19). `update-index --refresh` does
not clear it. The exclusion was right; the reason was wrong, and the reason matters because "live work"
implies a seat can commit it away -- none can.

**4. The class behind it, measured and corroborated.** I named this NOT RUN in S242; `1.0.0_SA_CTO~Z`
ran it and got 46. Corroborated here on an independently written pass: **41,851 tracked -> 3,151 raw
CRLF blobs -> 46 declaring `eol: lf`** (41 `.py`, 5 `.tf`). The five `.tf` are enumerated in the S242
message. Then the shared dependency I raised (a `text=auto` path invisible to both passes) was measured
by that seat at **zero**, making 46 a **total**, not a floor.

**5. The denominator reconciliation, verified.** The two passes agreed at 46 while their intermediates
disagreed (851 vs 3,151) -- which is exactly where a shared assumption hides. Verified to the unit:
`ls-files --eol` buckets 2,503 as `-text`; splitting MY 3,151 by that classification gives **2,300
binaries + 851 text-plane**, reproducing their 851 exactly. **Both numbers right about different
populations, demonstrated rather than asserted.**

## COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `git status --porcelain -uall` | over `infra/aws/terraform`, 77 dirs | PASS | The R-12 signature query. Zero, with a planted positive control. |
| `git cat-file --batch` | every blob in HEAD tree | PASS | Raw CRLF count across 41,739 blobs; the independent instrument for the 46. |
| `git ls-files --eol` | whole repo | PASS | Text-plane classification; the join that reconciled 2,300 + 851 = 3,151. |
| `git check-attr eol --stdin` | CRLF-bearing paths only | PASS | Narrowed 3,151 -> 46 without a per-file process. |
| `git worktree list` + per-tree `status` | 41 worktrees | PASS | Established 1-of-15 on identical content. |

**What worked.** Batching: one `cat-file --batch` over 41,739 blobs and one `check-attr --stdin` rather
than per-file processes made a whole-repo census cheap enough to run twice.

**What failed (mine).**
1. **I named a discriminator in S242 and left it NOT RUN** -- having already measured every ingredient
   the pass needed. Three hours earlier, in the S240 message, I wrote that a named-but-unrun
   discriminator "reads as diligence while the question stays open, and the next seat to reach it pays
   the cost." That seat paid it, within minutes.
2. **I inferred "this will recur in EVERY worktree"** from the blob-plus-attributes mechanism, then
   measured 1 of 15 and corrected before reporting. Right shape, wrong cardinality -- the same
   correction two other seats made to R-12 one level up, within the same hour.
3. **My censuses carried no VINTAGE.** 41,741/3,147 in one message and 41,851/3,151 an hour later,
   with no pin on either. A live repo moves; only the **join** (46, 851) held still across both runs,
   which is why the conclusion survived and why the intermediates must never be quoted bare.

**Gap found.** Five `.tf` files carry a CRLF blob against their own `eol: lf` attribute and will recur
as tracked-modification hits on any R-12 sweep that touches an mtime. No new rule was needed: the root
`.gitattributes` already names this hazard in its own comment at `:3`.

## MCP TRAFFIC

~10 messages, all acked (25127, 25131, 25133, 25136, 25139, 25142, 25146). Significant sends: the class
census + R-12 refinement, the S242 correction, the 46 corroboration with the shared-dependency question,
and the reconciliation verification.

## BLOCKERS

**None owned by this seat.** Unchanged from the prior entry: the incident's remediation act is
**Andrew's by class**; `E0` needs a captured authenticated trace and is **out of lane**; the five `.tf`
normalisation is a content commit under `infra/aws/terraform/` and is **not this seat's lane** -- routed,
not done.

## CURRENT STATE

- **R-12** is ratified, amended, scoped and its class closed -- `6b47ded436` -> `cbe6ed81ff` ->
  `839f198280` -> `7c4d12648f` -> `0e7cfdd669`. Coverage both devices: shared trees 0 and 0; site-Z 26 of
  26 carrying the directory read 0; laptop 12 of 12 read 0.
- **The CRLF class:** 46 files total (41 `.py`, 5 `.tf`), shared dependency measured at zero.
- **Push state, MEASURED:** `git ls-remote origin SITEZ` read `4eee2d0317` at ~00:20Z; commits through
  that hash are on origin. `63c3dfde02` push state **UNREAD** since -- no `ls-remote` run after it.
- Everything from the prior entry stands: PRD `ADMITTED`, repair live and accepted, incident reach final
  at five responses.

## NEXT STEPS

1. **[whoever owns `infra/aws/terraform/`]** Re-commit the five `.tf` with LF so each blob matches its
   own `eol: lf` attribute. Pure line-ending normalisation, no semantic change. Until then they recur as
   false hits on every R-12 sweep.
2. **[Andrew]** Unchanged -- the remediation act on 4 `BA_US_Equity` responses + 1 overlay, one client IP.
3. **[3.0.0_SA_CVO~Z, successor]** Nothing owed. If quoting any census number from this window, quote the
   **join** (46, 851) and not the intermediates, and carry a pin.
