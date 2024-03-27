import './base.cy'

describe('Happy path - route 2 - 5', () => {
  it('performs a full transaction', () => {
    cy.goToRegistrarDetails()
    cy.fillOutRegistrarDetails('WeRegister', 'Joe Bloggs', '01225672345', 'joe@example.org')

    cy.checkPageTitleIncludes('Who is this domain name for?')
    cy.chooseRegistrantType(1) // Central government -> Route 2

    cy.checkPageTitleIncludes('Why do you want a .gov.uk domain name?')
    cy.chooseDomainPurpose(1) // Email+web -> Route 7

    cy.checkPageTitleIncludes('Does your registrant have an exemption from using the GOV.UK website?')
    cy.selectYesOrNo('exemption', 'yes')

    cy.checkPageTitleIncludes('Upload evidence of the exemption')
    cy.uploadDocument("image.png")

    cy.checkPageTitleIncludes('Upload evidence of the exemption')
    cy.confirmUpload('image.png')

    cy.checkPageTitleIncludes('Does your registrant have proof of permission to apply for a .gov.uk domain name?')
    cy.selectYesOrNo('written_permission', 'yes')

    cy.checkPageTitleIncludes('Upload evidence of permission to apply')
    cy.uploadDocument("image.png")

    cy.checkPageTitleIncludes('Upload evidence of permission to apply')
    cy.confirmUpload('image.png')

    cy.checkPageTitleIncludes('What .gov.uk domain name do you want?')
    cy.enterDomainName('something-pc')

    cy.checkPageTitleIncludes('Can you confirm if the something-pc.gov.uk domain name is correct?')
    cy.selectYesOrNo('domain_confirmation', 'yes')

    cy.checkPageTitleIncludes('Has a central government minister requested the something-pc.gov.uk domain name?')
    cy.selectYesOrNo('minister', 'yes')

    cy.checkPageTitleIncludes('Upload evidence of the minister\'s request')
    cy.uploadDocument("image.png")

    cy.checkPageTitleIncludes('Upload evidence of the minister\'s request')
    cy.confirmUpload('image.png')

    cy.checkPageTitleIncludes('Registrant details')
    cy.fillOutRegistrantDetails('HMRC', 'Rob Roberts', '01225672344', 'rob@example.org')

    cy.checkPageTitleIncludes('Registrant details for publishing to the registry')
    cy.fillOutRegistryDetails('Clerk', '01225672736', 'clerk@example.org')

    cy.checkPageTitleIncludes('Check your answers')
    cy.get('#button-continue').click()

    cy.checkPageTitleIncludes('Application submitted')

  })
})
