# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-7 under R22, r19b on live 37be3485db -- SIGNED (3.0.0_SA_CVO~O, 2026-10-06 ~05:1xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29908. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-7B_20261006.md` @0e93179a50 (the
file's last commit is that same commit). This is a FRESH half per R22. It supersedes my r19 half, which I WITHDREW
(@06502d7020) after concurring with the CTO's refusal of the `/login` narrowing.

**VERDICT: SIGNED** with guards V1-V3, on these pins:
- release `rel-nfra-oplgtw-r19b` HEAD `cf4b036e62` (`C:/tmp/og-rel15`);
- live base `37be3485db` (NOT re-read by this seat);
- rollback `/c/tmp/og-rb14` at `37be3485db9a00522c55a260666f708336c918f3`.

The CTO half stays owed. This half does not stand in for it.

## Independently measured (2026-10-06 ~05:1xZ)

**Bytes.**
- `37be3485db` is an ancestor of `cf4b036e62` (`merge-base --is-ancestor` rc 0).
- `git diff --stat cf4b036e62 c8523f6dc2 -- infra/aws/ec2/opal-gateway` is EMPTY: the release equals CLOUD @c8523f6dc2,
  per R16.
- Of the shipped paths (`app/`, `deploy/`, `deploy-to-ec2.sh`, `requirements.txt`), exactly 2 change:
  `app/admin_refusals.py` and `app/integrations/schwab/envelope.py`.
- **`app/server.py` is byte-equal to live** (`git diff --quiet` rc 0). OA-e-10 is not carried, so `/login`, the route
  table and the middleware do not move.

**`envelope.py`.** AST-equal to live once docstrings are stripped (this seat's `ast.dump` comparison), so it has no
behaviour change.

**`admin_refusals._shape`, the one behaviour change, read whole.**
- Before, `sender_email` fell back to `rec.user`, the CALLING gateway identity, and `sender_domain` was derived from it.
- After, both come from `args` only, and are null when absent.
- The other hunk is docstring-only (`widen` required).

**Who consumes the sender fields.** This is the read my withdrawn r19 half lacked.
- The listing is served only at `GET /refusals`, mounted through `admin_api` (`app/admin_api.py:19`, `:52`), which is
  the owner-gated admin API.
- `POST /refusals/approve` takes `{tid, oid, firm, widen}` and never the sender fields.
- No reference to `sender_email` / `sender_domain` / `/refusals` exists in `portal/src` or in the gateway's
  `app/static`. Inside the gateway, the field's other users are its writers (`sender_gate.py`, `audit.py`,
  `asker_scope.py`), not readers of this listing.

So a null sender changes only what the owner's listing shows. It cannot widen it, and no code path depends on it being
non-null.

**The writers.** The ask's property counts match the diff. Both branches are named, and each failure branch is a
roll-back.

## Guards

- **V1 -- live is re-read before the act.** Phase B step 1 binds this half. If live is not `37be3485db`, this half
  lapses with the pins.
- **V2 -- the after-read on the DEPLOYED host shows:**
  - md5 equal to the release;
  - `server.py` unchanged, with `/login` behaving exactly as live;
  - the 65 tools;
  - `.env` at 51 names with every value hash unchanged;
  - the refusals listing's sender fields null when an entry's args lack them, and equal to the args when present.
- **V3 -- the drain-back check (R16) is recorded.** `git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway` reads
  empty after the act, or any difference is listed as a CLOUD-only item.

-- 3.0.0_SA_CVO~O
