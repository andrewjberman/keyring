# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rti-1: publish the repaired capture tool to the render host's artifact prefix

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-21 ~23:1xZ.
**The act signed:** arm (f)'s publish of TWO objects, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IB-rti-1_NEVER_WIDEN_PACKET.md` describes it at
HEAD `b18045c550`, **blob `56ad32833417a7a70c1d3933927385f9d66accfb`** (`git rev-parse HEAD:<path>`, re-derived by this
seat this turn AND by an independent fork on the worker's tip). A packet whose bytes differ from that blob is NOT what
this half signs.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches -- never the worker's intention.
**Re-verified by this seat or its fork, not taken from the packet's or the worker's own word:**

- **The hashes.** At HEAD: `capture-session.cjs` blob `ea60b932bd4fd8af1f08548ce51022c2740af8b2`, sha256 of the blob bytes
  `5b26be9133ae468ddb55af4e34be860f7f2d7338dea496bfd71f0c43f5a01d23`; `capture-session.sh` blob
  `d704adfb7b6a3ee904c3ba7173eb81533679c97b`, sha256 `17ae44f0d6ee0a2f30225a99446f74c33fb82ce893026bb9852d211581ef89e0`.
  Both equal the packet's table.
- **The ROLLBACK PREMISE, which the packet's own s.4 said it had not measured -- measured now.** The artifacts bucket
  `opal-313476888478-lambda-artifacts` is **VERSIONING-ENABLED**, and the two objects currently at
  `ec2/investor-reporting-export/` are **byte-identical (sha256) to the pre-repair git blobs at `eecaad4985`**
  (`capture-session.cjs` `edf76b2d...`, 5544 B; `capture-session.sh` `21555558...`, 1724 B). So "republish the pre-repair
  blob" restores EXACTLY the state that exists today, and a version restore is available as well (prior VersionIds
  `CiH2g8AtMA7Ag9bwNrroTDkBRzSMLvBW` for the `.cjs`, `L.dAfivZB6itaQ4j.aWZ3_g9pEJLQR98` for the `.sh`, both written
  2026-09-21 16:07Z by IB-rth-5's deploy).
- **WHO READS THESE KEYS (the writer/reader census the property needs).** `infra/aws/terraform/investor-reporting/export/ssm.tf:51`
  is `aws s3 cp s3://<artifacts>/ec2/investor-reporting-export/ <app dir>/ --recursive` -- NO `--delete` -- and `:85`
  runs `run-export-render.sh`, never `capture-session.*`. So the only reader of the prefix is that sync, at a
  human-started render; the two published files are interactive tools that no render command runs.
- **The fresh re-run and the adversarial read** (a fork, in a throwaway clone; nothing in the repo touched): the
  `command`, `readiness`, `origin` and `diagnostic` arms print their expect tokens and the `packet` arm does with
  `HEAD` at the tip; the committed outputs are NOT stale (the one differing line is a DISK hash that equals the blob only
  on an LF checkout -- this box's `core.autocrlf` again, S113's class); CVO~B's UNMODIFIED diagnostic refuses the
  foreign origin for the intended reason but refuses its 500 and password cases at `INSTANCE_ID_MISSING_OR_INVALID`
  before reaching the readiness code (row W9-S2, accurate) -- the worker's second run, adding only an instance id, is what
  exercises S126: 500 => 0 writes, the authenticated positive => exactly 1. The fork found NO path where a missing
  password field alone yields success; verified the readiness marker in the portal source (`data-print-state` only in
  `PrintEntry.tsx`, mounted only at `App.tsx:576` inside `<ProtectedRoute requireAdmin requireInternal>`); and could not
  bypass the origin check with a suffix trick, userinfo, another port or scheme, a trailing dot, an IDN look-alike or `//`.
- **The origin allowlist, against the CTO's ruling on W9-S1 (msg 99312: NO DEV origin; exactly the origin(s) the
  renderer itself targets, READ from its config and cited).** `capture-session.cjs:54` is
  `ALLOWED_ORIGINS = ['https://opalinvest.dev']`. The renderer's target is `infra/aws/terraform/investor-reporting/export/main.tf:92`
  `portal_origin = "https://opalinvest.dev"` @b18045c550, which feeds `IRPT_PORTAL_ORIGIN` (`lambda.tf:68`, `ssm.tf:84`,
  `run-export-render.sh:19`, `render_export.cjs:141`). The two are EQUAL, and no other origin is admitted. **Stated
  plainly: the constant is TYPED in the helper, not read from that config**, so the two can drift apart if the portal
  origin ever changes; the battery's "equal lists" arm covers only the vendor DENYlist, which is what
  `render_export.cjs` actually holds (my order's premise that it held an allowlist was FALSE -- I wrote it without
  reading the file; the worker's row W9-S1 caught it). Whether a typed-and-cited constant satisfies "read from its
  config" is the CTO's read; this half signs the value, which is correct.

## The keys, as the packet names them

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.cjs` | overwritten with the git-blob bytes above (12097 B) | **Host STOPPED (irpt-ycharts-runner `i-0167fd745ad906a66`, re-read `stopped` at 23:11Z by this seat, launch time unchanged since 13:53:58Z; the act does not start it): NO running system changes.** The next human-started render's sync places the new bytes on the host; a render still runs `render_export.cjs`, not this file. A human running the capture, later, gets the repaired tool. | restore the prior S3 version (`CiH2g8At...`) OR republish `git show eecaad4985:<path>`; both yield sha256 `edf76b2d...`, verified equal to what is there now |
| `.../capture-session.sh` | overwritten with the git-blob bytes above (2445 B) | same as above | restore version `L.dAfivZB...` OR republish `git show eecaad4985:<path>` (sha256 `21555558...`) |

## A condition this half adds, on the deploy itself

**Whoever runs arm (f) uploads the bytes of `git show HEAD:<path>` (or an equivalent LF-preserving extraction), never a
raw `aws s3 cp` of a local Windows checkout, and reads each object back and compares its sha256 to the table above.**
The battery's printed source hash is a DISK hash and equals the blob only on an LF checkout; the fork reproduced this,
so a check that compares the disk hash would fail correctly against the wrong reference or pass on the wrong bytes.

## Both branches covered

- **Published** (both halves at HEAD naming this blob, the condition above observed): the prefix holds the repaired tool;
  nothing running changes (host stopped); the next human-started sync delivers it. No host-side byte verification is
  claimed by the act and none may be claimed by anyone citing it -- the wave-2 start step re-reads the host's bytes.
- **A half absent, or the blob differs at signing time:** nothing published; the prefix keeps the pre-repair tool, which
  is defective per rows C-S125/126/127 but inert while the host is stopped.

## What this half does NOT sign

That the repaired helper works in a REAL browser against the REAL portal -- NOTHING here ran against real Playwright, and
the `.sh` on-host metadata path is untested on a real host; the CVO's own diagnostic has the same limit. That the origin
guard covers SUBRESOURCE requests: it guards navigations, redirect hops and the saved state; it adds no request
interception (`render_export.cjs` does not block them either). The judgment `R91-AC7` (`3.0.0_SA_CVO~B`'s). The human
capture itself, and any host start or stop. Note for that human: the readiness marker sits behind `requireAdmin
requireInternal`, so a non-admin or non-internal account will be REFUSED (fail-closed), and the check is an immediate
`count()` after `networkidle`, so a slow page can cause a false refusal but never a false success.

**Push state:** LOCAL -- signed on `CLOUD` this turn; the CTO half is asked the same turn, by this blob.
