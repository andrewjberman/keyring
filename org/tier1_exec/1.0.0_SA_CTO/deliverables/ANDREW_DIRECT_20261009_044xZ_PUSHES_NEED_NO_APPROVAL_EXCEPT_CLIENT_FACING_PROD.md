# ANDREW_DIRECT 2026-10-09 ~04:4xZ -- pushes need no approval from Andrew, except a portal PROD push that touches a client-facing page

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn. This record is the `ANDREW_LAW_EDIT_ORDER` for
the CLAUDE.md edit it names.

## Andrew's words, verbatim

> "Yeah something I want to make a law, i dont know if it is best in XXX.md, Claude.md, or in the /govern and /self-drive skills, but
> pushes should not require my approval. Pushes are of no concern to me aside from portal PROD, and only if it is touching a
> client-facing page. What that means, is if a page is opal-internal, e.g. Portfolio Management, or Security Analysis, etc., then
> pushes do not require my attention and agents should push at will."

## Placement (the CTO's call, which he left open)

**CLAUDE.md** is the law index every seat reads at startup; a rule only in `/govern` or `/self-drive` binds only the seats running those
loops, and `org/XXX.md` holds startup mechanics, not law. The law lands in CLAUDE.md's Agent Autonomy section, with the Git and
Portal lines that said "on Andrew's word" brought into line. The two skills that carried the old wording follow: `/integrate` (a
shared-branch push "on Andrew's word") and `/prod-deploy` (a re-promote after a rollback "needs Andrew's word again").

## The law, as written

- Every push (workspace `box/*` and `CLOUD`, portal, `opal_ai` and `mcportal` `DEV` and `PROD`) needs no word from Andrew; agents
  push at will.
- **One exception:** a portal `PROD` push that changes a **client-facing page** waits on his word. A page is client-facing when a
  partner-firm or client login can open it. It is Opal-internal when only Opal staff can open it, as with Portfolio Management and
  Security Analysis.
- **When unsure, treat the page as client-facing.** The pusher names, in the push receipt, which pages the push changes and which
  class each one is.

## What does not change

- **Who may push stays as the gates have it.** The push lanes enforced by `.tools/hooks/never-rules-gate.sh` (LD-0367/LD-0368) are
  pre-existing mechanical gates, and they decide which seat pushes where.
- **The safety rules stay.** VALGATE on every portal push, never rebase a shared branch, never force-push, and the never-widen pair
  for any served or IAM change. These are safety rules, not approvals.
