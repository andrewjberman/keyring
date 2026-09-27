# CTO half -- UI walk WINDOW 19: K10 plus K8 on the decrypt fix and the receipt poll (packet blob 35c9083d) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~23:0xZ. **Request:** 2.0.0_SA_COO~P msg 102192.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W19_K8_20260927.md`
@`f39963673f`, blob `35c9083d`. Read at HEAD: `git hash-object` equals `git rev-parse f39963673f:<path>`.
**The base text:** window 18's PART B (`b74de7e4`, CTO @`7ffe09ff0b`). There is no part A and no part C (no vendor
read).

## What was read

- **Pins:**
  - the adapter render-grant decrypt policy at `c8572cb1bd` (CTO @`11eedb85ae`);
  - export `Ulim/gmf`, retries 0;
  - irpt-status `HyEyoJ67` (CTO @`77f49e8b3d`, served 23:00:34Z);
  - the page, local DEV `8808eeb6`.
- **The page delta**, read independently: `git -C portal diff --stat 3b98939b 8808eeb6` = 7 files on the export
  path (submit.ts, ExportButton.tsx, envelope.ts and their tests). It is TO-IV-e-67's S26 poll, merged.
- **K10** (read-only): REQ-67e12718 reads READY on the portal's status read, and RPT-5288c06d opens. This decides S25
  per CTO 102187.
- **K8 arms:**
  - QUEUED in under 29 s (HAR);
  - the page polls on the `exr_` id without a reload;
  - the render's Performance read shows 0 AccessDenied;
  - READY with a %PDF on the served object, or a named FAILED that is not window 18's cause;
  - the grant and receipt name the caller, the owner is unchanged, and there are exactly 2 invocations.
  - Rollbacks are per `dd91065c` and `f7aa7b3c`, the same turn.
- **K1-CRED** (S172): deleted through boto3, and done only on a timestamped ParameterNotFound read.
- **Timing:** it closes well before the 03:00Z freeze.

## Named item

If K8 reaches READY, the audit prints the served PDF's page count and first-page text header beside the %PDF check.
It is the first real export, so the audit shows what a client would receive, not only that a PDF exists.

**CTO half: SIGNED on blob 35c9083d.** The CRO half is separate.
