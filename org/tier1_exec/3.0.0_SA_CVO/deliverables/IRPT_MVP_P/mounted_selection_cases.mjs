import { chromium } from 'playwright-core'
import assert from 'node:assert/strict'
const origin = process.env.IRPT_TEST_ORIGIN
const browser = await chromium.launch({ executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', headless: true })
try {
  const page = await browser.newPage()
  const errors = [], blocked = []
  page.on('pageerror', error => errors.push(error.message))
  await page.route('**/*', route => {
    const url = new URL(route.request().url())
    if (url.origin !== origin || /^\/(api|auth|v1)\//.test(url.pathname)) {
      blocked.push(url.origin + url.pathname)
      return route.abort()
    }
    return route.continue()
  })
  await page.goto(`${origin}/src/pages/InvestorReporting/__tests__/m-selection/header-race.html`)
  await page.waitForSelector('[data-slot="selection-required"]')
  assert.deepEqual(await page.evaluate(() => window.exercise.calls), [])
  const choose = async name => {
    await page.getByRole('combobox', { name: 'Client search' }).fill(name)
    await page.getByRole('option').filter({ hasText: name }).click()
    await page.waitForFunction(name => window.exercise.pending(`client-${name}`), name)
    assert.equal(await page.locator('[data-slot="holdings-tab"]').count(), 0)
    assert.equal(await page.locator('[data-slot="reporting-tab"]').count(), 0)
  }
  await choose('Alpha')
  await page.evaluate(() => window.exercise.resolve('client-Alpha', 'a'))
  await page.waitForFunction(() => window.exercise.calls.some(c => c.kind === 'performance'))
  let calls = await page.evaluate(() => window.exercise.calls)
  const performance = calls.find(c => c.kind === 'performance').request
  assert.equal(performance.accountSetId, `sel_${'a'.repeat(64)}`)
  assert.equal(performance.scopeFingerprint, 'selected-a')
  assert.equal(performance.revision, 'directory-accepted')
  assert.match(performance.start, /^\d{4}-\d{2}-\d{2}$/)
  assert.match(performance.end, /^\d{4}-\d{2}-\d{2}$/)
  assert.notEqual(performance.start, '1970-01-01')
  assert.equal(calls.filter(c => c.kind === 'holdings').length, 0)
  await page.getByRole('button', { name: 'Refresh', exact: true }).click()
  await page.waitForFunction(() => window.exercise.calls.filter(c => c.kind === 'performance').length === 2)
  calls = await page.evaluate(() => window.exercise.calls)
  assert.deepEqual(calls.filter(c => c.kind === 'performance')[1].request, performance)
  await page.getByRole('button', { name: 'Holdings', exact: true }).click()
  await page.waitForSelector('[data-slot="holdings-tab"]')
  await choose('Beta')
  await choose('Gamma')
  await page.evaluate(() => window.exercise.resolve('client-Gamma', 'c'))
  await page.waitForSelector('[data-slot="holdings-tab"]')
  await page.evaluate(() => window.exercise.reject('client-Beta'))
  await page.waitForTimeout(100)
  assert.equal(await page.getByText('This selection could not be authorized. Search and select it again.').count(), 0)
  calls = await page.evaluate(() => window.exercise.calls)
  assert.deepEqual(calls.filter(c => c.kind === 'holdings').map(c => c.request.accountSetId),
    [`sel_${'a'.repeat(64)}`, `sel_${'c'.repeat(64)}`])
  const beforeReset = calls.length
  await page.evaluate(() => window.exercise.reset())
  await page.waitForSelector('[data-slot="selection-required"]')
  assert.equal(await page.locator('[data-slot="holdings-tab"]').count(), 0)
  await page.getByRole('button', { name: 'Analysis', exact: true }).click()
  await page.waitForSelector('[data-slot="analysis-tab"]')
  assert.equal((await page.evaluate(() => window.exercise.calls)).length, beforeReset)
  assert.deepEqual(errors, [])
  assert.deepEqual(blocked, [])
  console.log(JSON.stringify({ checks: ['no eager custody calls', 'accepted selection reaches mounted performance',
    'explicit dates replace bootstrap sentinel', 'refresh preserves exact request', 'only active custody tab fetches',
    'late rejected selection cannot replace current success', 'context reset clears accepted state',
    'prospect analysis mounts without custody fetch'], page_errors: errors, blocked_network: blocked, calls }))
} finally { await browser.close() }
