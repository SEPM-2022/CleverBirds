describe('Test dynamic pages', () => {
    const randomNumber = Math.floor(Math.random() * 1000);
    const name = 'cypress_name' + randomNumber;
    const password = 'cypress_password' + randomNumber;
    const username = 'cypress_username' + randomNumber;
    const email = 'email' + randomNumber + '@cypress.com';

    it('when clicking on create an account, then should open respective page', () => {
        cy.visit('http://localhost/')

        cy.get('#signup').click()

        cy.url().should('include', '/signup')
        cy.contains('Create your profile')
    })

    it('when filling out registration form, should create account', () => {
        cy.visit('http://localhost/signup')


        cy.get('#form-name')
            .type(name)
            .should('have.value', name)

        cy.get('#form-password')
            .type(password)
            .should('have.value', password)

        cy.get('#form-username')
            .type(username)
            .should('have.value', username)

        cy.get('#form-email')
            .type(email)
            .should('have.value', email)

        cy.get('[type="radio"]').check('girl')
        cy.get('#next-step').click();
        cy.get('#form-daisy').click()

        cy.contains('Congrats! Your acount has been successfully created!')
    })

    it('when filling out correct login details, should be directed to dashboard', () => {
        cy.visit('http://localhost')

        cy.get('#Username')
            .type(username)
            .should('have.value', username)

        cy.get('#password')
            .type(password)
            .should('have.value', password)

        cy.get('#form-login').submit()

        cy.url().should('include', '/login')
        cy.contains('User Dashboard')
    })

    it('when filling out false login details, should stay on same page', () => {
        cy.visit('http://localhost')

        const notExistUsername = 'notExistUsername'
        const notExistPassword = 'notExistPassword'

        cy.get('#Username')
            .type(notExistUsername)
            .should('have.value', notExistUsername)

        cy.get('#password')
            .type(notExistPassword)
            .should('have.value', notExistPassword)

        cy.get('#form-login').submit()

        cy.url().should('include', '/login')
        cy.contains('Not Registered?')
    })
})
