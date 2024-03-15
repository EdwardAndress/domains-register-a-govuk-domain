import './base.cy'

describe('change registrant organisation name', () => {
    it('correctly changes registrant when the users goes back to change it', () => {
      cy.base('')
      // Change Organisation name
      cy.visit('registrant/?change');
      cy.get('#id_registrant_organisation_name').clear();
      cy.get('#id_registrant_organisation_name').type('Caladan')

      // Back to Answers
      cy.get('#id_cancel').click();
      cy.get('.govuk-summary-list__value').should('include.text', 'Caladan')
    })
  })
