# AMGT_HARVST round 32 -- the served gold rebuild (`article_security_mention` + `chatter_daily`), CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~11:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO_H/round32/NEVER_WIDEN_HALF_COO_GOLD_REBUILD.md` @534a521e45 (msg 27793).

## What I read myself

1. **The signing record** (`round32/gold_rebuild_signing.json`, measured 11:29:19Z, puts 0):
   - mention: gone 0, changed 0, added 4,267;
   - daily: gone 0, changed 27,272, added 191.
   - This agrees with the COO half.
2. **Writers of the two tables:** a repo census of `write_gold(` / `build_mention(` / `build_daily(` shows that only
   `lib/research/harvest/publication_gold.py` writes them (its `build-mention` / `build-daily` CLI; the other hits are
   tests). N = 1. No scheduled producer runs it, so no off-clock override path exists.

## What this half signs

**THE RULE, as the COO half states it, enforced TWICE per act** (on a fresh serializing dry run before the write, and on
the written parts after):
- `article_security_mention`: 0 GONE, 0 CHANGED, ADDED only.
- `chatter_daily`: 0 GONE; every CHANGED row is on a security that gained an added mention (OTHER = 0); ADDED rows are
  the new as-of day.

**Blast radius:**
- exactly 2 new parts per rebuild, never-overwrite, no delete;
- at most FOUR rebuilds through 2026-10-02 13:00Z;
- the readers are RESAPP's monthly route and the timeline routes over the newest part.

**Both branches:**
- **Rule fails before the write:** STOP.
- **Rule fails on the written parts:** ROLLBACK. The BEFORE rows are written as a newer part (never-overwrite), checked
  by digest equality.

## Conditions

1. **Each act record names its two parts, both digests and the rule's counts.** A rebuild whose dry run shows OTHER > 0
   or any mention CHANGED/GONE is a STOP, never a re-sign by narrative.
2. **The quarantine stays honoured:** `sa_quarantined_keys` is read on every build, so no quarantined row reaches gold.
3. **The first rebuild lands before the 22:00Z (18:00 ET) DSGN close walk.** The walk then shows the deeper bubbles.

**CTO HALF: SIGNED** for up to four rule-gated rebuilds through 2026-10-02 13:00Z.
