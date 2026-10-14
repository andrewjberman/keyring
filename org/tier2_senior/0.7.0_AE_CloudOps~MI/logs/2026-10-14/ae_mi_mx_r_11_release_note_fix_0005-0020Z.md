# MX-r-11 step 6 follow-up -- the EC2_MANIFEST release_note corrected to name MX-r-11's chain

**archetype:** SCRIBE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-14 00:05Z -> 00:20Z (prior log
`ae_mi_mx_r_11_v2_close_2325-0005Z.md` @`12ddf7c6f3`)
**Order:** `NFRA_MCPINDEX.TO-MX-r-11`, the A6 act's step 6 (in this seat's `<paths>`) | **risk:** LOCAL

---

## What happened

`2.0.0_SA_COO~MP` found that the `services.opal-gateway` block I wrote at `af58ea818a` carried **correct commit
fields over MP-z-5's `release_note`** (msg 33873, row `NFRA_MCPORTAL-Z-S49`), relayed by the issuer as msg 33875.
The catch is right and it is mine: both of my plane-2 writes moved only the five commit/stamp fields and never
touched the note, so the block described one release in its fields and a different one in its prose. It matters
because `MP-n-4` writes forward from this block.

**Corrected, `release_note` alone.** It now opens `NFRA_MCPINDEX MX-r-11` and names the chain
`64b3e54658 -> v1 ad2acc0a93` (served 22:51:28Z-23:49:56Z) `-> v2 7eff14b2e6` (catalog-only fix-forward,
`Z-S112`), with what shipped per act, why v2 exists and why the v1 rollback was not taken, both never-widen pairs
and their four signed pins, the three equal censuses, the read-backs with their negative controls, the artifact
and rollback keys with sizes and ETags, the v1 fail-closed refusal (`Z-S108` / `Z-S111`), the v2 single-blob cut
method with its 44-path control, and the recurring wrapper defect this correction is the second half of.

**Scope made mechanical rather than promised.** The script asserted three preconditions before writing
(`deployed_commit` still `7eff14b2e6`, `previous_deployed_commit` still `ad2acc0a93`, and `release_note` still
opening `NFRA_MCPORTAL MP-z-5`), then diffed the service block before and after and **refused unless the
changed-field set was exactly `['release_note']`**. It printed `['release_note']`. Both commit fields re-read
unchanged at HEAD. `numstat` 1 file / 1 insertion / 1 deletion; 27 services; 0 non-ASCII; the file parses.

## Blockers

**None.** `NFRA_MCPORTAL-Z-S49` is answerable (its disarm is `~MP`'s). The MX-r-11 items still outstanding are
the issuer's: the order's `<status>` flip, rows `Z-S108` / `Z-S109` / `Z-S111`, and teardown of
`C:/tmp/mx-dep-r11`.

## Current State

Unchanged in the world: the host serves `7eff14b2e620c8c1f688d41de6f37c09addde7b4`, the ledger
`nfra-mcpindex-r10-catalog-release` is CLOSED on 5 legs, the proof instance is VALID. Plane 2's
`services.opal-gateway` now reads `deployed_commit 7eff14b2e6`, `previous_deployed_commit ad2acc0a93`,
`mcportal_commit 0e02a1f` **and** a `release_note` that describes those commits. Deploy tree `C:/tmp/mx-dep-r11`
still kept at `7eff14b2e6` for the rollback path.

**Commit:** `642fe57f1d`. **Push state: LOCAL @`642fe57f1d`; origin `box/sitez` @`9323a39fd0`
(`git ls-remote` read).**

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `commit-gate.sh` | rode the `safe-commit` | WARN | `checked 0 of 1 file(s)` -- it reads only `.py/.sh/.tf`. **Not cited as validation**; the JSON was validated by `json.load` plus the before/after field diff and the `numstat` shape |
| `comp-*` | NOT RUN | N/A | declared: a one-field documentation correction to a committed record. No code, infra, IAM, Terraform or served artifact touched; nothing deployed and no host contact |

**What worked.** Writing the edit as a script with preconditions and a changed-field assertion, rather than as a
careful hand edit, is what makes "release_note alone" a measurement instead of a claim -- and it is the same
shape as the precondition I put on the two earlier manifest writes.

**What failed.** My own two plane-2 writes left the note stale, twice, and I did not notice either time: I
verified the fields I changed and never read the field beside them. A peer caught it.

**Gap found.** Two large bash heredocs failed this window and last with `unexpected EOF while looking for
matching ''` -- the shell does not reliably carry a big `<<'EOF'` payload here, and the failure mode looks like a
quoting bug in the content rather than a size limit, which sends you hunting the wrong thing. The reliable path
for a large script or JSON payload is to `Write` it to a file and run the file; that is now how both the proof
instance and this correction were produced.

## Next Steps

1. **[`2.0.0_SA_COO~MP`]** Disarm `NFRA_MCPORTAL-Z-S49`; `MP-n-4` can write forward from the block.
2. **[`2.0.0_SA_COO~MI`]** The standing MX-r-11 items: `<status>` flip, rows `Z-S108` / `Z-S109` / `Z-S111`,
   deploy-tree teardown.
3. **[`0.7.0_AE_CloudOps~MI`]** `MX-s-19` on its clock (`s19.AC2` reads 2026-10-19/20).
