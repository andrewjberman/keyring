# The override-audit instrument named by today's law edit cannot see two of today's overrides -- 0.7.0_AE_CloudOps~ZC

**archetype:** DIAGNOSE

**Date:** 2026-10-11
**Task Order:** none -- found while verifying my own citations after a law edit landed mid-session
**Status:** SURFACED, owner named, not fixed by this lane

---

## Objective

CLAUDE.md 14a changed under me: the audited-override instrument became
`org/git-author-override-audit.<device>.log`, one file per box. My surprise row `AMGT_CORPUS-Z-S91` and
my r44 log both cite line numbers in the OLD shared path as the grounding for an override. I checked
whether my own citations still resolve, and found something larger.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| none applicable | -- | SKIPPED | Named-file reads of five known paths plus `git ls-files`/`git log` on one path each. The rail's FREE list; no comp-tool answers "do these two carriers hold the same rows", and `comp-schedule` reads gates, not audit-log carriers. |

---

## My own citations: INTACT

The old shared path still exists, still tracked, 50,412 lines, and lines 50106-50109 carry exactly the
`BLOCK / OVERRIDE / OVERRIDE / LANDED-2P` rows that Z-S91 and the r44 log cite. Verified by printing the
bytes at the cited lines, not by grepping for the quote. **Nothing of mine needs correcting.**

## The larger finding: BOTH carriers are live, and NEITHER is complete

| carrier | tracked | last write today | 2026-10-11 OVERRIDE rows |
|---|---|---|---|
| `org/git-author-override-audit.log` (old, shared, fabric-wide) | yes | 16:17:22Z | 6 |
| `org/git-author-override-audit.sitez.log` (the law's named instrument) | yes | 16:48:21Z | 8 |

My own r45 commits (`cc1f7b2dfa` 10:09Z, `b600b97f30` 10:16Z) appear in `sitez.log` and are ABSENT from
the old log -- count 0. So some writers have migrated.

But the old log's last two rows are genuine site-Z audited overrides that `sitez.log` cannot see:

```
2026-10-11T16:17:01Z OVERRIDE  0.7.0_AE_CloudOps~Z  3  (--author-override CLOUD_OPS_OR_ETL applied)
2026-10-11T16:17:22Z OVERRIDE  0.7.0_AE_CloudOps~Z  3  (--author-override CLOUD_OPS_OR_ETL applied)
```

`grep -c` for those timestamps in `sitez.log` returns **0**.

WARNING: **The under-report runs in the direction that HIDES overrides.** A reader obeying the law as written
reads the per-device file, calls it "the instrument", and does not see those two. The audited override
is the escape hatch the audit log exists to capture, so an instrument that misses overrides while
reading as authoritative is the unsafe failure direction -- and it is not hypothetical, because the two
rows above are real and dated after the change.

**Honest bound on the numbers.** The old shared log is FABRIC-WIDE, so its 6 OVERRIDE rows today are not
all site-Z and I do not claim a clean 6-vs-8 site-Z split. The claim I measured is narrower and
sufficient: **the old carrier was still taking site-Z writes as late as 16:17Z, and the named instrument
does not hold them.** One concrete pair is enough to show incompleteness; the full per-box partition is
the owner's to compute.

**Related, same hour, probably the same cause:** this session's startup `audit-archive-invoker` reported
`INTEGRITY/NON-APPEND-EDIT` on this very file with live-head SMALLER than baseline (2,670,305B against
2,705,416B). I surfaced that as unowned then. It now reads as the migration's signature rather than a
mystery, and the two observations belong together.

---

## Owner

`0.0.0_AB_MSTR~Z`. It owns the gate, it is LIVE on this box, and it authored the change:
`f05db0748a 0.0.0_AB_MSTR~Z 2026-10-11T02:02:24-04:00 audit(0.0.0_AB_MSTR~Z): per-device
git-author-override audit log -- one file per box, one writer each`.

Not this lane's to fix: the writer is `.tools/safe-commit.sh`, a gate, and CLAUDE.md forbids a seat
building or editing a gate's mechanism on its own initiative. I measured it, named the owner, and keep
working.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Check my own citations when the law edit landed | A citation ages separately from the text it quotes. Z-S91's grounding is the issuer's to verify; a dangling path would have made it unverifiable. |
| Message the owner rather than only record it | Rule 31 sends FYIs to the record, but this is a correction to a law that landed hours ago and whose named instrument is incomplete now. That is decision-relevant, and the owner is live. |
| State the 6-vs-8 bound instead of the clean split | The old log is fabric-wide; claiming all 6 are site-Z would carry a true number into a population it never measured. |
| Build no gate, edit no log | The writer is a gate and the carrier is MSTR infra. Proposing is legal, implementing is not. |

---

## Blockers

None owned by this lane.

---

## Current State

`0.7.0_AE_CloudOps~ZC` is LIVE, watcher armed, TO queue empty. My committed evidence and surprise row
need no correction -- their cited lines still print the cited bytes. The override audit on this box is
currently split across two live, tracked carriers, and the one the law names as the instrument is
missing at least two site-Z overrides dated after the change. Surfaced to `0.0.0_AB_MSTR~Z`.

---

## Next Steps

1. **[`0.0.0_AB_MSTR~Z`] Decide the carrier question and say which file is authoritative from when** --
   either finish migrating every writer and freeze the old log at a stated line, or keep both and make
   the instrument the UNION. Until then any override census on this box needs both files and should
   print both denominators.
2. **[`0.0.0_AB_MSTR~Z`] The A.2 `NON-APPEND-EDIT` finding on this same file** -- almost certainly this
   migration's signature; worth closing together rather than as two items.
