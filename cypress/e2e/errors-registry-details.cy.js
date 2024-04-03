import './base.cy'

describe('Error messages for registry details', () => {
  it('tries a series of bad or missing data', () => {
    cy.goToRegistryDetails()

    // click without entering anything
    cy.get('#id_submit').click()

    // page shouldn't change
    cy.checkPageTitleIncludes('Registrant details for publishing to the registry')

    // but display errors
    cy.confirmProblem('This field is required', 2)

    // enter just the registry
    cy.get('#id_registrant_role').clear().type('Littleton PC')
    cy.get('#id_submit').click()
    cy.confirmProblem('This field is required', 1)


    // enter a bad email address
    cy.fillOutRegistryDetails('clerk', 'joe@example')
    cy.confirmProblem('Please enter a valid email address')

    // enter valid details
    cy.fillOutRegistryDetails('clerk', 'joe@example.com')

    // No error, we've moved on to the next page
    cy.checkPageTitleIncludes('Check your answers')
  })
})
