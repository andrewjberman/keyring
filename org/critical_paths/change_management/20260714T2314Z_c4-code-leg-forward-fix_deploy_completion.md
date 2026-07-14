# DEPLOY COMPLETION LEDGER -- c4-code-leg-forward-fix

**Opened:** 2026-07-14T23:14Z by 0.5.0_AE_OpalETL
**Gate:** CTO FORWARD-FIX GO 230335Z (full sequence executed by 0.5.0 under that gate; plan must be
source_code_hash + s3_object_version ONLY or STOP).
**Ledger JSON:** `org/critical_paths/.open_deploys/c4-code-leg-forward-fix.json`

## What this deploy is

The CODE LEG of OPAL_ASSETS.C4, completing the deploy the 03:05:41Z apply left HALF-LANDED. That apply
flipped the two TF locals (BRONZE_BUCKET=opal-data-assets, BRONZE_GRAMMAR=monolith) onto a lambda whose
artifact (S3 LastModified 2026-07-13T22:41:11Z) PREDATES the C4 bucket-split commit d69efaad2 -- the
running code reads neither variable, so tonight's 22:00:09Z fire wrote legacy-only and monolith C4 AC1
could not occur. A stale S3 artifact is invisible in a TF plan diff, which is why the pre-cleared 0/2/0
plan looked complete; the 09:37Z env read then ratified "APPLIED" off a config read (Rule 22a class,
self-identified by 0.5.0 in the 230221Z escalation).

## Why the ledger closes on deploy-verified, not behavior

CTO ruling 230335Z item 2: NO ad-hoc re-fire. The parity day-2 measurement is banked (52/52 GREEN);
a re-fire would rewrite today's _cloudprobe artifacts; validate-on-the-scheduled-fire is the law.
Tomorrow's 22:00Z fire is the behavioral proof (day-3 parity + first monolith bronze in ONE run).
This ledger closes on the THREE-WAY TIE (live CodeSha256 == uploaded metadata == build-from-HEAD).

## Legs

Tracked in the JSON. L1 build (CLOSED at open: 12736B, 40KaO/7jI/JKjT4fahkTPZznpzdJwt8htZn38BmEQJA=),
L2 commit-before-apply, L3 upload+read-back, L4 plan-gate/apply/0-diff, L5 three-way tie,
L6 tag+record+close.
