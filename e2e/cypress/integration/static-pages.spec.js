describe('Test static pages', () => {
    it('when clicking on About link, then should open respective page', () => {
        cy.visit('http://localhost/')

        cy.get('#header-about').click()

        cy.url().should('include', '/about')
        cy.contains('How to play Clever Birds Game?')
    })

    it('when clicking on Talk to Tweety link, then should open respective page', () => {
        cy.visit('http://localhost/')

        cy.get('#header-tweety').click()

        cy.url().should('include', '/tweety')
        cy.get('#tweety-img').should('have.attr', 'src', '/static/img/tweety-wait.gif')
    })

    it('when clicking on privacy policy document link, then should open respective page', () => {
        cy.visit('http://localhost/')

        cy.get('#footer-privacy-policy').click()

        cy.url().should('include', '/privacy')
        cy.contains('Privacy Policy')
    })

    it('should have correct github url', () => {
        cy.visit('http://localhost/')

        cy.get('#footer-github-repo').should('have.attr', 'href', 'https://github.com/SEPM-2022/CleverBirds')
    })

    it('when clicking on play now link, then should open game page', () => {
        cy.visit('http://localhost/')

        cy.get('#header-game').click()

        cy.url().should('include', '/playgame')
        cy.get('iframe').should('have.attr', 'src', 'http://localhost:8080?bird=birdy')
    })

    it('when clicking on chat icon, then should open chatbot', () => {
        cy.visit('http://localhost/')

        cy.get('df-messenger').find('#widgetIcon', { includeShadowDom: true }).click();

        cy.get('df-messenger').find('.df-messenger-wrapper', { includeShadowDom: true }).should('have.class', 'expanded')
    })

    it('when chatbot is open and clicking on close button, then should close chatbot', () => {
        cy.visit('http://localhost/')

        cy.get('df-messenger').find('#widgetIcon', { includeShadowDom: true }).click();
        cy.get('df-messenger').find('#widgetIcon', { includeShadowDom: true }).click();

        cy.get('df-messenger').find('.df-messenger-wrapper', { includeShadowDom: true }).should('not.have.class', 'expanded')
    })
})
