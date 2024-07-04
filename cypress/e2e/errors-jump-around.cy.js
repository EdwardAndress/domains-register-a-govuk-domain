import './base.cy'

describe('Errors when user skips and jumps pages', () => {

  it('Throws a 404 when user skips to success page', () => {
    cy.goToRegistrantDetails()
    cy.request({ url: '/success', failOnStatusCode: false}).then(res => {
      expect(res.status).to.eq(404)
    })
  })

  it('Throws a 200 when user skips to success page with param', () => {

    cy.goToRegistrantDetails()

    cy.request({ url: '/success/abc', failOnStatusCode: false}).then(res => {
      expect(res.status).to.eq(200)
      expect(res.body).to.include('abc')
    })
  })

  it('Throws a 400 when user goes back 6 pages after submitting', () => {
    cy.goToConfirmation(1)
    cy.get('.govuk-button#id_submit').click()
    cy.checkPageTitleIncludes('Application submitted')
    cy.go(-6)
    cy.checkPageTitleIncludes('Invalid request')
  })

  it('Throws a 400 when user goes back 4 pages after submitting', () => {
    cy.goToConfirmation(1)
    cy.get('.govuk-button#id_submit').click()
    cy.checkPageTitleIncludes('Application submitted')
    cy.go(-4)
    cy.checkPageTitleIncludes('Invalid request')
  })

  it('Throws a 400 when user goes back and forth after submitting', () => {
    cy.goToConfirmation(1)
    cy.get('.govuk-button#id_submit').click()
    cy.checkPageTitleIncludes('Application submitted')
    cy.go(-4)
    cy.checkPageTitleIncludes('Invalid request')
    cy.go(3)
    cy.checkPageTitleIncludes('Invalid request')
  })

  it('Throws a 400 when user goes back after submitting', () => {
    cy.goToConfirmation(1)
    cy.get('.govuk-button#id_submit').click()
    cy.checkPageTitleIncludes('Application submitted')
    cy.go('back')
    cy.checkPageTitleIncludes('Invalid request')
  })


})
