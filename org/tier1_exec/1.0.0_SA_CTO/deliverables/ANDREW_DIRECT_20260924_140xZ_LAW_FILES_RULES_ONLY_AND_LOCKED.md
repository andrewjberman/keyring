# ANDREW-DIRECT 2026-09-24 ~14:0xZ at the 1.0.0_SA_CTO terminal -- law files cut to rules only and LOCKED; portal dev port 5174

Verbatim, in order:
1. "Strike all incident reporting from claude.md. cut it hard right now to the rules/directives only."
2. "furthermore strike all incident reporting/temporal updates/etc from XXX.md. Be harsh about it, just cut. Then make
   it so no agent can edit claude.md or XXX.md without my express order."
3. "then give me /open-calls recs on the cuts that you say need my word."
4. "also portal only uses 5174 from now on for dev builds"

Recorded by 1.0.0_SA_CTO the same turn. Acts on this word:
- `CLAUDE.md` rewritten to rules only (imperative + mechanism + pointer); every incident report, measurement, dated
  quotation and "found by" line removed; pure ASCII. The long-form text stays in `docs/doctrine/CLAUDE_ANNEX.md` and
  git history.
- `org/XXX.md` rewritten to mechanics only; stood-down and superseded loop rows removed (their records stay in git);
  live arms listed one line each with their record paths.
- LOCK: `.tools/git-hooks/law-lock-check.sh` (wired by `install-law-lock.sh`, fail-closed) refuses any commit staging
  `CLAUDE.md` or `org/XXX.md` unless `ANDREW_LAW_EDIT_ORDER=<org/**/ANDREW_DIRECT_*.md>` names a record of his order
  that exists; every pass and refusal is appended to `org/law-edit-audit.log`. This edit is the first commit under it,
  ordered by this record.
- Portal dev builds: port 5174 only (CLAUDE.md Portal section; XXX.md Step 1a and quick reference).
- Item 3 is answered as `/open-calls` cards at the CTO terminal.
