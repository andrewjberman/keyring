# SELF-DRIVE laptop directives -- ticks 68-70 (2026-09-27 ~21:20Z to ~22:48Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 66-67 log (@`3451d6e7cf`). **State: ARMED.**

## Window 18 closed (~P @`614594fff7`)

- K8 arms 1, 2, 4 and 5 PASS on the served async export.
- Arm 3 was a named FAILED at the print route. The final cause was the adapter lacking kms:Decrypt on the render grant
  under an S3 Bucket Key.
- S172: a path-mangled credential delete. From now on, a delete counts only with a ParameterNotFound read-back
  (CRO 102122).

## Rulings

1. **The print-route defect** (~P 102124 -> 102129 -> 102134):
   - my 21:26Z print-key ruling is withdrawn;
   - the decrypt grant is scoped to one key, ViaService s3, and the bucket-ARN context (a Bucket Key sends the bucket,
     not the object);
   - decrypt reach equals the role's GetObject set (render_grant.json only).
   - **CTO half @`11eedb85ae`**; CRO @`b994f81153`.
2. **S26** (~P 102136): my 102114 is withdrawn, because R2 makes QUEUED data optional. It goes to ~D's page:
   TO-IV-e-67 polls when the receipt is null.
3. **Comparison** (~M 102140, ~Y 102148):
   - 49financial first;
   - the benchmark never-renders proof is accepted, so INF and COT are admitted;
   - the certifier's cross-firm name check is built as durable cover;
   - the GRANT is re-cut through the registry (@`2d0f83e962`).
4. **UIC-16** (~M 102110): no self-written Schwab decode. INF lands on Monday; 49F waits on Schwab's list (carded).
5. **Site Z OG-s-1 relay** (MSTR 102143): the cited "CTO half @815dac7460" is not this seat's. Attribution was noted to
   MSTR.
6. **Round 8, L10:** the CVO slug 102159 (ADJUDICATION_v6 @`6e820aa89b`) was answered by the **ROUND-8 ANALYSIS
   @`071e09aa18`**:
   - C-S60: the first pinned sample is the grade;
   - W35-S1: firm names from the registry's generated view (no R20, no exemption);
   - UIR-37: the asset-class palette yields;
   - S25: diagnose, then route;
   - E1-E12.
   ~D issued round 9 (IV-e-68..77) @`9bfc7eb31d`.
7. **CRO cleanup brief** (Andrew-direct /ui-walk, 102100): placed as DSGN_IRPTV1 **PRD v0.18** @`5d44d0fa62`,
   UIC-01..23.
8. **Generate + resident release** (catalogue v2 + consumer, Static-only tolerance):
   - **CTO half @`a4ed7d7933`**; D2 re-signed on install script `638addc8` @`0f4ea3c451`;
   - generate `ykJltfTd` is served from 22:33:55Z; D2 (resident st) is next.

## Capacity (BLOCKING round 9's workers)

- C: has 9.8 GB free. MSTR 102172: the 5 GB git floor plus the ~4 GB 03:00Z purge leaves 0 worker slots before the
  purge, and ~2 after ~05:00Z.
- Andrew's ~5.7 GB Downloads scratch is carded (MSTR has asked too). ~D is told to seat E9 first.

## Open calls at Andrew

1. BLOCKING: remove the ~5.7 GB Downloads scratch? REC: yes, if nothing there is needed.
2. CARRIED: Schwab's registration-code list for 49F's full account types (UIC-16).

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

state: ARMED
