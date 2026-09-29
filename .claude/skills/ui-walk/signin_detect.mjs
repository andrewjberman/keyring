// Pure sign-in page detector for walk.mjs (no imports, no browser).
// True on the portal's sign-in route (/login or a path under /login/), or when BOTH the email and the password
// inputs are visible. An email field alone, or a route that merely starts with "login" (/login-history), is not.
export function isSignInPage({ path, hasEmail, hasPassword } = {}) {
  const p = String(path || '').split(/[?#]/)[0].replace(/\/+$/, '')
  if (p === '/login' || p.startsWith('/login/')) return true
  return Boolean(hasEmail) && Boolean(hasPassword)
}
