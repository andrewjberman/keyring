import { chromium } from 'playwright-core'
import assert from 'node:assert/strict'
import { installOfflineRoutes } from './offline-routes.mjs'
const browser = await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', headless:true})
const results = []
async function run(name, exercise) {
  const page = await browser.newPage()
  await installOfflineRoutes(page)
  page.setDefaultTimeout(5000)
  const errors = []
  page.on('pageerror', e => errors.push(e.message))
  try {
    await page.goto('https://irpt-review.invalid/reviewer.html')
    await page.waitForFunction(() => Boolean(window.exercise))
    await exercise(page)
    assert.deepEqual(errors, [])
    results.push({name, pass:true})
  } catch (error) {
    results.push({name, pass:false, error:String(error), errors})
  } finally {await page.close()}
}
const input = page => page.getByRole('combobox', {name:'Client search'})
const options = page => page.getByRole('option')
const calls = (page, count) => page.waitForFunction(count => window.exercise.calls.length === count, count)
async function start(page, names=['First'], cursor=null) {
  await page.evaluate(() => window.exercise.set('ready'))
  await calls(page, 1)
  await page.evaluate(({names,cursor}) => window.exercise.resolve(0,names,cursor), {names,cursor})
  await input(page).click()
  await options(page).filter({hasText:names[0]}).waitFor()
}
try {
  await run('Bootstrap loading disables search and issues no browse', async page => {
    assert.equal(await input(page).isDisabled(), true)
    await page.getByText('Resolving your permitted scope', {exact:true}).waitFor()
    assert.deepEqual(await page.evaluate(() => window.exercise.calls), [])
    assert.equal(await page.locator('[data-slot="scope-error"]').count(), 0)
  })
  await run('Bootstrap refusal disables search and distinguishes error from loading', async page => {
    await page.evaluate(() => window.exercise.set('error'))
    await page.locator('[data-slot="scope-error"]').waitFor()
    assert.equal(await input(page).isDisabled(), true)
    assert.equal(await page.getByText('Resolving your permitted scope', {exact:true}).count(), 0)
    assert.deepEqual(await page.evaluate(() => window.exercise.calls), [])
  })
  await run('Missing directory revision disables browse with explanation', async page => {
    await page.evaluate(() => window.exercise.set('missing-revision'))
    assert.equal(await input(page).isDisabled(), true)
    await page.getByText('Client browsing is unavailable for this scope. Refresh the page to try again.').waitFor()
    assert.deepEqual(await page.evaluate(() => window.exercise.calls), [])
  })
  await run('Initial authorized request has exact bounded context and visible firm', async page => {
    await start(page)
    assert.equal(await page.locator('[data-slot="verified-firm"]').innerText(), 'Firm\nIndependent verified firm')
    const request = await page.evaluate(() => window.exercise.calls[0])
    assert.equal(request.query, '')
    assert.equal(request.limit, 25)
    assert.equal(request.revision, 'd'.repeat(64))
    assert.ok(request.tenant && request.scopeFingerprint)
    assert.equal('cursor' in request, false)
  })
  await run('Successful continuation appends rows and preserves exact request context', async page => {
    await start(page, ['First'], 'cursor-1')
    await input(page).press('Escape')
    await page.getByRole('button', {name:'Load more clients'}).click()
    await calls(page, 2)
    const pair = await page.evaluate(() => window.exercise.calls)
    assert.deepEqual(pair[1], {...pair[0], cursor:'cursor-1'})
    await page.evaluate(() => window.exercise.resolve(1,['Second']))
    await input(page).click()
    await options(page).filter({hasText:'Second'}).waitFor()
    assert.equal(await options(page).filter({hasText:'First'}).count(), 1)
    assert.equal(await page.getByRole('button', {name:'Load more clients'}).count(), 0)
  })
  await run('Continuation refusal clears previous rows and cursor without empty-state claim', async page => {
    await start(page, ['First'], 'cursor-1')
    await input(page).press('Escape')
    await page.getByRole('button', {name:'Load more clients'}).click()
    await calls(page, 2)
    await page.evaluate(() => window.exercise.reject(1))
    await page.getByRole('alert').waitFor()
    await input(page).click()
    assert.equal(await options(page).count(), 0)
    assert.equal(await page.getByRole('button', {name:'Load more clients'}).count(), 0)
    assert.equal(await page.getByText('No matching clients in your permitted scope.').count(), 0)
  })
  await run('Late rejected query cannot erase a newer successful query', async page => {
    await start(page)
    await input(page).fill('Old')
    await calls(page, 2)
    await input(page).fill('New')
    await calls(page, 3)
    await page.evaluate(() => window.exercise.resolve(2,['New result']))
    await options(page).filter({hasText:'New result'}).waitFor()
    await page.evaluate(() => window.exercise.reject(1))
    await page.waitForTimeout(50)
    assert.equal(await options(page).filter({hasText:'New result'}).count(), 1)
    assert.equal(await page.getByRole('alert').count(), 0)
  })
  await run('Directory-only context change remount clears query and suppresses old response', async page => {
    await start(page)
    await input(page).fill('Old context')
    await calls(page, 2)
    await page.evaluate(() => window.exercise.set('ready', 'e'.repeat(64)))
    await calls(page, 3)
    assert.equal(await input(page).inputValue(), '')
    const request = await page.evaluate(() => window.exercise.calls[2])
    assert.equal(request.query, '')
    assert.equal(request.revision, 'e'.repeat(64))
    await page.evaluate(() => window.exercise.resolve(1,['Stale context']))
    await page.evaluate(() => window.exercise.resolve(2,['Fresh context']))
    await input(page).click()
    await options(page).filter({hasText:'Fresh context'}).waitFor()
    assert.equal(await options(page).filter({hasText:'Stale context'}).count(), 0)
  })
} finally {await browser.close()}
console.log(JSON.stringify(results, null, 2))
process.exitCode = results.some(row => !row.pass) ? 1 : 0
