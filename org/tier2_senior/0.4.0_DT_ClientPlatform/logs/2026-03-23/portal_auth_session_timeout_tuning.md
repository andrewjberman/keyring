# Portal Auth & Session Timeout Tuning — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-23
**Branch:** portal DEV

---

## Problem

Two user-facing issues with the portal session management:

1. **Auto sign-out too aggressive** — 5-minute idle threshold + 60-second countdown meant users got logged out after 6 minutes of reading dashboards, being on calls, or stepping away briefly. Most enterprise SaaS uses 15-30 minute idle timeouts.

2. **JWT expires while user is active** — AdvisorIntelligence would lose access to data even though the user was still moving the mouse. Root cause: the activity throttle (30s) and refresh check interval (60s) created up to a 90-second window where mouse movement could reset the idle timer but NOT trigger a token refresh. The 15-minute JWT would expire silently, and the next batch of parallel API calls would all 401 simultaneously.

---

## Root Cause Analysis

Three independent timing systems with misaligned windows:

| Timer | Duration | Controlled By |
|-------|----------|---------------|
| Idle threshold | 5 min | `useActivityTracker.ts` (browser) |
| Token refresh age | 12 min (checked every 60s, only if active < 5 min) | `AuthContext.tsx` (browser) |
| JWT expiration | 15 min | Backend Lambda (hard expiry) |

The activity-aware refresh at `AuthContext.tsx:191-202` asked `userIsActive = Date.now() - lastActivityRef.current < 5 min`. But `lastActivityRef` was only updated every 30 seconds (throttle). If the 60-second refresh poll landed during a throttle gap, `userIsActive` evaluated false and the refresh was **skipped** — even for a user actively using the app.

Meanwhile, AdvisorIntelligence fires multiple parallel queries on tab switches (leaderboard, rolling flows, composition, etc.). When the JWT expired mid-session, all parallel requests hit 401 simultaneously. The mutex refresh handled one, but others could fail or return stale data before retry.

---

## Changes

### Timing Constants

**`useActivityTracker.ts`**

| Constant | Before | After |
|----------|--------|-------|
| `IDLE_THRESHOLD_MS` | 5 min | 30 min |
| `THROTTLE_MS` | 30 sec | 5 sec |

**`AuthContext.tsx`**

| Constant | Before | After |
|----------|--------|-------|
| `TOKEN_REFRESH_AGE_MS` | 12 min | 10 min |
| `TOKEN_STALE_AGE_MS` | 10 min | 8 min |
| `REFRESH_CHECK_INTERVAL_MS` | 60 sec | 15 sec |
| `WARNING_COUNTDOWN_SEC` | 60 sec | 120 sec |
| `userIsActive` window | 5 min | 30 min |

### Structural: Proactive Token Refresh (`api-client.ts`)

Added `ensureFreshToken()` — called before every `apiRequest` and `publicApiRequest`. If the token is > 10 min old, it refreshes synchronously (through the existing mutex) before the request fires. This eliminates the batch-401 race condition entirely.

Added `notifyTokenIssued()` export — called by AuthContext on every successful token set (login and refresh) so api-client tracks token age independently of the AuthContext refresh interval.

The existing 401 retry path remains as a fallback.

### Net Effect

| Metric | Before | After |
|--------|--------|-------|
| Time to auto-logout (idle) | 6 min (5 + 1) | 32 min (30 + 2) |
| Activity sampling rate | Every 30 sec | Every 5 sec |
| Token refresh check | Every 60 sec | Every 15 sec |
| Proactive refresh before API call | No | Yes (> 10 min age) |
| Warning countdown | 60 sec | 120 sec |

---

## Files Modified

| File | Change |
|------|--------|
| `src/hooks/useActivityTracker.ts` | Idle 5m->30m, throttle 30s->5s |
| `src/contexts/AuthContext.tsx` | Refresh age 12m->10m, stale 10m->8m, check 60s->15s, warning 60s->120s, active window 5m->30m, import+call `notifyTokenIssued` |
| `src/api/api-client.ts` | Added `ensureFreshToken()`, `notifyTokenIssued()`, proactive refresh before every API request |

---

## Backend Note

The JWT access token lifetime (15 min) and refresh token lifetime (7 days) are set in the auth Lambda backend. No backend changes were made in this session. The frontend now refreshes proactively at 10 minutes, well before the 15-minute hard expiry.
